from .optimlib import *
import sympy as sym
import itertools as it
import numpy as np
import copy


def ocp_to_bvp(ocp):
    ws = init_workspace(ocp)
    problem_name = ws['problem_name']
    independent_variable = ws['independent_var']
    independent_variable_units = ws['independent_var_units']
    states = ws['states']
    states_rates = ws['states_rates']
    states_units = ws['states_units']
    controls = ws['controls']
    controls_units = ws['controls_units']
    constants = ws['constants']
    constants_units = ws['constants_units']
    constants_values = ws['constants_values']
    constants_of_motion = ws['constants_of_motion']
    constants_of_motion_values = ws['constants_of_motion_values']
    constants_of_motion_units = ws['constants_of_motion_units']
    constraints = ws['constraints']
    constraints_units = ws['constraints_units']
    quantities = ws['quantities']
    quantities_values = ws['quantities_values']
    parameters = ws['parameters']
    parameters_units = ws['parameters_units']
    initial_cost = ws['initial_cost']
    initial_cost_units = ws['initial_cost_units']
    terminal_cost = ws['terminal_cost']
    terminal_cost_units = ws['terminal_cost_units']
    path_cost = ws['path_cost']
    path_cost_units = ws['path_cost_units']

    if initial_cost != 0:
        cost_units = initial_cost_units
    elif terminal_cost != 0:
        cost_units = terminal_cost_units
    elif path_cost != 0:
        cost_units = path_cost_units*independent_variable_units
    else:
        raise ValueError('Initial, path, and terminal cost functions are not defined.')

    quantity_vars, quantity_list, derivative_fn = process_quantities(quantities, quantities_values)
    for var in quantity_vars.keys():
        for ii in range(len(states_rates)):
            states_rates[ii] = states_rates[ii].subs(Symbol(var), quantity_vars[var])

    augmented_initial_cost, augmented_initial_cost_units, initial_lm_params, initial_lm_params_units = \
        make_augmented_cost(initial_cost, cost_units, constraints, constraints_units, location='initial')

    augmented_terminal_cost, augmented_terminal_cost_units, terminal_lm_params, terminal_lm_params_units = \
        make_augmented_cost(terminal_cost, cost_units, constraints, constraints_units, location='terminal')

    hamiltonian, hamiltonian_units, costates, costates_units = \
        make_hamiltonian(states, states_rates, states_units, path_cost, cost_units)

    costates_rates = make_costate_rates(hamiltonian, states, costates, derivative_fn)

    coparameters = make_costate_names(parameters)
    coparameters_units = [path_cost_units / parameter_units for parameter_units in parameters_units]
    coparameters_rates = make_costate_rates(hamiltonian, parameters, coparameters, derivative_fn)

    bc_initial = make_boundary_conditions(
        constraints, states, costates, parameters, coparameters,
        augmented_initial_cost, derivative_fn, location='initial')

    bc_terminal = make_boundary_conditions(
        constraints, states, costates, parameters, coparameters,
        augmented_terminal_cost, derivative_fn, location='terminal')

    time_bc = make_time_bc(constraints, derivative_fn, hamiltonian, independent_variable)
    if time_bc is not None:
        bc_terminal += [time_bc]

    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)

    nondynamical_parameters = initial_lm_params + terminal_lm_params
    costate_eoms, bc_list = make_constrained_arc_fns(states, costates, costates_rates, controls, nondynamical_parameters, constants, quantity_vars, hamiltonian)
    dae_states, dae_equations, dae_bc, temp_dgdX, temp_dgdU = make_control_dae(states, costates, states_rates, costates_rates, controls, dHdu, derivative_fn)

    # Generate the problem data
    tf = sympify('_tf')
    bc_terminal = [bc.subs(independent_variable, tf) for bc in bc_terminal]
    dynamical_parameters = parameters + [tf]
    dynamical_parameters_units = parameters_units + [independent_variable_units]
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units

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

    out = {'method': 'icrm',
           'problem_name': problem_name,
           'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x) for x in it.chain(states, costates)],
           'states_units': [str(x) for x in states_units + costates_units],
           'states_rates':
               [str(tf * rate) for rate in states_rates] +
               [str(tf * rate) for rate in costates_rates] +
               [str(tf*dae_eom) for dae_eom in dae_equations],
           'quads': [str(x) for x in coparameters],
           'quads_rates': [str(tf * x) for x in coparameters_rates],
           'quads_units': [str(x) for x in coparameters_units],
           'path_constraints': [],
           'path_constraints_units': [],
           'constants': [str(c) for c in constants],
           'constants_units': [str(c) for c in constants_units],
           'constants_values': [float(c) for c in constants_values],
           'constants_of_motion': [str(c) for c in constants_of_motion],
           'dynamical_parameters': [str(c) for c in dynamical_parameters],
           'dynamical_parameters_units': [str(c) for c in dynamical_parameters_units],
           'nondynamical_parameters': [str(c) for c in nondynamical_parameters],
           'nondynamical_parameters_units': [str(c) for c in nondynamical_parameters_units],
           'controls': [str(u) for u in controls],
           'hamiltonian': str(hamiltonian),
           'num_states': len(states + costates + coparameters),
           'dHdu': [str(_) for _ in it.chain(dHdu)],
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in it.chain(bc_terminal, dae_bc)],
           'num_bc': len(bc_initial) + len(bc_terminal) + len(dae_bc),
           'control_options': [],
           'control_list': [str(u) for u in controls],
           'num_controls': len(controls),
           'ham_expr': str(hamiltonian),
           'dgdX': dgdX,
           'dgdU': dgdU,
           'nOdes': 2 * len(states) + len(dae_states)}

    def guess_map(sol):
        sol.y = np.column_stack((sol.y, sol.u))
        sol.u = np.array([])
        sol.dynamical_parameters[-1] = sol.t[-1]
        sol.t = sol.t / sol.t[-1]
        return sol

    def guess_map_inverse(sol, num_controls=len(controls)):
        sol.t = sol.t * sol.dynamical_parameters[-1]
        sol.u = sol.y[:, -num_controls:]
        sol.y = np.delete(sol.y, np.s_[-num_controls:], axis=1)
        return sol


    return out, guess_map, guess_map_inverse


def make_control_dae(states, costates, states_rates, costates_rates, controls, dhdu, derivative_fn):
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

    g = dhdu
    X = [state for state in states] + [costate for costate in costates]
    U = [c for c in controls]
    xdot = sym.Matrix([sympify(state) for state in states_rates] + [sympify(lam) for lam in costates_rates])
    # Compute Jacobian
    dgdX = sym.Matrix([[derivative_fn(g_i, x_i) for x_i in X] for g_i in g])
    dgdU = sym.Matrix([[derivative_fn(g_i, u_i) for u_i in U] for g_i in g])

    udot = dgdU.LUsolve(-dgdX*xdot) # dgdU * udot + dgdX * xdot = 0

    dae_states = U
    dae_equations = list(udot)
    dae_bc = g

    yield dae_states
    yield dae_equations
    yield dae_bc
    yield dgdX
    yield dgdU
