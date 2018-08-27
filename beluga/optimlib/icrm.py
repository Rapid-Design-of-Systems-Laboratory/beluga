from .optimlib import *
import sympy as sym
from beluga.utils import sympify2, keyboard
import simplepipe as sp
from beluga.problem import SymVar
import logging
import numpy as np


def ocp_to_bvp(ocp, guess):
    ws = init_workspace(ocp, guess)
    problem_name = ws['problem_name']
    independent_variable = ws['indep_var']
    states = ws['states']
    controls = ws['controls']
    constants = ws['constants']
    constants_of_motion = ws['constants_of_motion']
    constraints = ws['constraints']
    constraints_adjoined = ws['constraints_adjoined']
    path_constraints = ws['path_constraints']
    quantities = ws['quantities']
    initial_cost = ws['initial_cost']
    terminal_cost = ws['terminal_cost']
    path_cost = ws['path_cost']
    quantity_vars, quantity_list, derivative_fn, jacobian_fn = process_quantities(quantities)
    states, controls, constants, constraints, path_cost, s_list, mu_vars, xi_init_vals, derivative_fn, jacobian_fn = process_path_constraints(states, controls, constants, constraints, path_constraints, derivative_fn, quantity_vars, quantity_list, path_cost, terminal_cost, independent_variable)
    augmented_initial_cost = make_augmented_cost(initial_cost, constraints, constraints_adjoined, location='initial')
    initial_lm_params = make_augmented_params(constraints, constraints_adjoined, location='initial')
    augmented_terminal_cost = make_augmented_cost(terminal_cost, constraints, constraints_adjoined, location='terminal')
    terminal_lm_params = make_augmented_params(constraints, constraints_adjoined, location='terminal')
    hamiltonian, costates = make_ham_lamdot_with_eq_constraint(states, constraints, path_cost, derivative_fn)
    bc_initial = make_boundary_conditions(constraints, constraints_adjoined, states, costates, augmented_initial_cost, derivative_fn, location='initial')
    bc_terminal = make_boundary_conditions(constraints, constraints_adjoined, states, costates, augmented_terminal_cost, derivative_fn, location='terminal')
    bc_terminal = make_time_bc(constraints, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    parameters = make_parameters(initial_lm_params, terminal_lm_params, s_list)
    bc_free_mask = make_bc_mask(states, controls, [], initial_cost, augmented_initial_cost, derivative_fn)
    # TODO: More path constraints are processed here. Ref #51
    costate_eoms, bc_list = make_constrained_arc_fns(states, costates, controls, parameters, constants, quantity_vars, hamiltonian, mu_vars, s_list)
    mu_vars, mu_lhs, dae_states, dae_equations, dae_bc, guess, temp_dgdX, temp_dgdU = make_control_dae(states, costates, controls, constraints, dHdu, xi_init_vals, guess, derivative_fn)

    # Generate the problem data
    tf_var = sympify('tf')

    dgdX = []
    for i, row in enumerate(temp_dgdX.tolist()):
        for j, expr in enumerate(row):
            if expr != 0:
                dgdX.append('dgdX[{},{}] = {}'.format(i, j, expr))

    dgdU = []
    for i, row in enumerate(temp_dgdU.tolist()):
        for j, expr in enumerate(row):
            if expr != 0:
                dgdU.append('dgdU[{},{}] = {}'.format(i, j, expr))

    out = ws
    out['states'] = states
    out['costates'] = costates
    out['s_list'] = s_list
    out['initial_lm_params'] = initial_lm_params
    out['terminal_lm_params'] = terminal_lm_params
    out['problem_data'] = {'method': 'icrm',
        'problem_name': problem_name,
        'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
        'state_list':[str(x) for x in it.chain(states, costates)],
        'parameter_list': [str(tf_var)] + [str(p) for p in parameters],
        'x_deriv_list': [str(tf_var * state.eom) for state in states],
        'lam_deriv_list': [str(tf_var * costate.eom) for costate in costates],
        'deriv_list': [str(tf_var * state.eom) for state in states] + [str(tf_var * costate.eom) for costate in costates],
        'states': states,
        'costates': costates,
        'constants': constants,
        'constants_of_motion': constants_of_motion,
        'parameters': [tf_var] + parameters,
        'controls': controls,
        'mu_vars': mu_vars,
        'quantity_vars': quantity_vars,
        'dae_var_list': [str(dae_state) for dae_state in dae_states],
        'dae_eom_list': ['(tf)*(' + str(dae_eom) + ')' for dae_eom in dae_equations],
        'dae_var_num': len(dae_states),
        'costate_eoms': costate_eoms,
        'bc_list': [],
        'ham': hamiltonian,
        's_list': [],
        'num_states': 2 * len(states),
        'num_params': len(parameters) + 1,
        'dHdu': [str(_) for _ in it.chain(dHdu, mu_lhs)],
        'bc_initial': [str(_) for _ in bc_initial],
        'bc_terminal': [str(_) for _ in it.chain(bc_terminal, dae_bc)],
        'num_bc': len(bc_initial) + len(bc_terminal) + len(dae_bc),
        'control_options': [],
        'control_list': [str(u) for u in controls + mu_vars],
        'num_controls': len(controls) + len(mu_vars),
        'ham_expr': str(hamiltonian),
        'quantity_list': quantity_list,
        'bc_free_mask': bc_free_mask,
        'dgdX': dgdX,
        'dgdU': dgdU,
        'nOdes': 2 * len(states) + len(dae_states)}
    return out


def make_control_dae(states, costates, controls, constraints, dhdu, xi_init_vals, guess, derivative_fn):
    """
    Make's control law for dae (ICRM) formulation.

    :param states:
    :param costates:
    :param controls:
    :param constraints:
    :param dhdu:
    :param xi_init_vals:
    :param guess:
    :param derivative_fn:
    :return:
    """
    equality_constraints = constraints.get('equality', [])
    if len(equality_constraints) > 0:
        mu_vars = [sympify('mu'+str(i+1)) for i in range(len(equality_constraints))]
        mu_lhs = [sympify(c.expr) for c in equality_constraints]
    else:
        mu_vars = mu_lhs = []

    g = dhdu + mu_lhs
    X = [state for state in states] + [costate for costate in costates]
    U = [c for c in controls] + mu_vars

    xdot = sym.Matrix([sympify(state.eom) for state in states] + [sympify(lam.eom) for lam in costates])
    # Compute Jacobian
    dgdX = sym.Matrix([[derivative_fn(g_i, x_i) for x_i in X] for g_i in g])
    dgdU = sym.Matrix([[derivative_fn(g_i, u_i) for u_i in U] for g_i in g])

    udot = dgdU.LUsolve(-dgdX*xdot) # dgdU * udot + dgdX * xdot = 0

    dae_states = U
    dae_equations = list(udot)
    dae_bc = g

    if guess.start is not None:
        guess.start.extend(xi_init_vals)
    guess.dae_num_states = len(U)

    yield mu_vars
    yield mu_lhs
    yield dae_states
    yield dae_equations
    yield dae_bc
    yield guess
    yield dgdX
    yield dgdU
