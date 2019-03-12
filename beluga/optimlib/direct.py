"""
Computes the necessary conditions of optimality using Bryson & Ho's method
"""

from .optimlib import init_workspace, process_quantities
from sympy import Symbol
import itertools as it
import numpy as np
import copy


def ocp_to_bvp(ocp, **kwargs):
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
    constraints_lower = ws['constraints_lower']
    constraints_upper = ws['constraints_upper']
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

    # Adjoin time as a state
    states += [independent_variable]
    states_rates += [0]
    states_units += [independent_variable_units]

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

    # Generate the problem data
    # tf_var = sympify('tf')
    dynamical_parameters = parameters
    dynamical_parameters_units = parameters_units
    bc_initial = [c for c in constraints['initial']]
    bc_terminal = [c for c in constraints['terminal']]

    path_constraints = []
    path_constraints_units = []
    for ii, c in enumerate(constraints['path']):
        if constraints_lower['path'][ii] is not None:
            path_constraints += [constraints_lower['path'][ii] - c]
            path_constraints_units += [constraints_units['path'][ii]]

        if constraints_upper['path'][ii] is not None:
            path_constraints += [c - constraints_upper['path'][ii]]
            path_constraints_units += [constraints_units['path'][ii]]


    out = {'method': 'direct',
           'problem_name': problem_name,
           'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
           'initial_cost': str(initial_cost),
           'initial_cost_units': str(initial_cost_units),
           'path_cost': str(path_cost * states[-1]),
           'path_cost_units': str(path_cost_units * independent_variable_units),
           'terminal_cost': str(terminal_cost),
           'terminal_cost_units': str(terminal_cost_units),
           'states': [str(x) for x in it.chain(states)],
           'states_rates': [str(states[-1] * rate) for rate in states_rates],
           'states_units': [str(x) for x in states_units],
           'quads': [],
           'quads_rates': [],
           'quads_units': [],
           'path_constraints': [str(c) for c in path_constraints],
           'path_constraints_units': [str(u) for u in path_constraints_units],
           'constants': [str(c) for c in constants],
           'constants_units': [str(c) for c in constants_units],
           'constants_values': [float(c) for c in constants_values],
           'constants_of_motion': [str(c) for c in constants_of_motion],
           'dynamical_parameters': [str(c) for c in dynamical_parameters],
           'dynamical_parameters_units': [str(c) for c in dynamical_parameters_units],
           'nondynamical_parameters': [],
           'nondynamical_parameters_units': [],
           'control_list': [str(u) for u in controls],
           'controls': [str(u) for u in controls],
           'hamiltonian': None,
           'hamiltonian_units': None,
           'num_states': len(states),
           'dHdu': None,
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal],
           'control_options': None,
           'num_controls': len(controls)}

    def guess_map(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        # Append time as a state
        sol = copy.deepcopy(sol)
        sol.y = np.column_stack((sol.y, sol.t[-1]*np.ones((sol.y.shape[0],1))))
        sol.t = sol.t / sol.t[-1]
        return sol

    def guess_map_inverse(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol = copy.deepcopy(sol)
        sol.t = sol.t*sol.y[:, -1]
        sol.y = np.delete(sol.y, np.s_[-1:], axis=1)
        return sol


    return out, guess_map, guess_map_inverse
