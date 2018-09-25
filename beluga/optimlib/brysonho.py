"""
Computes the necessary conditions of optimality using Bryson & Ho's method
"""

from .optimlib import *
from beluga.utils import sympify
import logging


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
    quantities = ws['quantities']
    initial_cost = ws['initial_cost']
    terminal_cost = ws['terminal_cost']
    path_cost = ws['path_cost']
    quantity_vars, quantity_list, derivative_fn = process_quantities(quantities)
    augmented_initial_cost = make_augmented_cost(initial_cost, constraints, constraints_adjoined, location='initial')
    initial_lm_params = make_augmented_params(constraints, constraints_adjoined, location='initial')
    augmented_terminal_cost = make_augmented_cost(terminal_cost, constraints, constraints_adjoined, location='terminal')
    terminal_lm_params = make_augmented_params(constraints, constraints_adjoined, location='terminal')
    hamiltonian, costates = make_ham_lamdot(states, path_cost, derivative_fn)
    bc_initial = make_boundary_conditions(constraints, constraints_adjoined, states, costates, augmented_initial_cost, derivative_fn, location='initial')
    bc_terminal = make_boundary_conditions(constraints, constraints_adjoined, states, costates, augmented_terminal_cost, derivative_fn, location='terminal')
    bc_terminal = make_time_bc(constraints, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    parameters = make_parameters(initial_lm_params, terminal_lm_params)
    costate_eoms, bc_list = make_constrained_arc_fns(states, costates, controls, parameters, constants, quantity_vars, hamiltonian)
    control_law = make_control_law(dHdu, controls)
    # Generate the problem data
    tf_var = sympify('tf')
    out = ws
    out['costates'] = costates
    out['initial_lm_params'] = initial_lm_params
    out['terminal_lm_params'] = terminal_lm_params
    out['problem_data'] = {'method': 'brysonho',
        'problem_name': problem_name,
        'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
        'state_list':[str(x) for x in it.chain(states, costates)],
        'parameter_list': [str(tf_var)] + [str(p) for p in parameters],
        'x_deriv_list': [tf_var * state.eom for state in states],
        'lam_deriv_list': [tf_var * costate.eom for costate in costates],
        'deriv_list': [tf_var * state.eom for state in states] + [tf_var * costate.eom for costate in costates],
        'states': states,
        'costates': costates,
        'constants': constants,
        'constants_of_motion': constants_of_motion,
        'parameters': [tf_var] + parameters,
        'controls': controls,
        'quantity_vars': quantity_vars,
        'costate_eoms': costate_eoms,
        'ham': hamiltonian,
        'num_states': 2 * len(states),
        'num_params': len(parameters) + 1,
        'dHdu': dHdu,
        'bc_initial': [_ for _ in bc_initial],
        'bc_terminal': [_ for _ in bc_terminal],
        'control_options': control_law,
        'control_list': [str(u) for u in controls],
        'num_controls': len(controls),
        'ham_expr': str(hamiltonian),
        'quantity_list': quantity_list,
        'nOdes': 2 * len(states)}
    return out


def make_control_law(dhdu, controls):
    r"""
    Solves control equation to get control law.

    .. math::
        \frac{dH}{d\textbf{u}} = 0

    :param dhdu: The expression for :math:`dH / d\textbf{u}`.
    :param controls: A list of control variables, :math:`[u_1, u_2, \cdots, u_n]`.
    :return: Control law options.
    """
    var_list = list(controls)
    from sympy import __version__
    logging.info("Attempting using SymPy (v" + __version__ + ")...")
    logging.debug("dHdu = "+str(dhdu))
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.info('Control found')
    logging.debug(ctrl_sol)
    control_options = ctrl_sol
    return control_options
