"""
Computes the necessary conditions of optimality using Bryson & Ho's method
"""

from beluga.ivpsol import Trajectory
from .optimlib import *
from beluga.utils import sympify
import itertools as it
import logging
import numpy as np
from sympy import cos, pi
# from math import cos

def ocp_to_bvp(ocp):
    """

    :param ocp:
    :return: bvp, map, map_inverse
    """

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
    constraints_activators = ws['constraints_activators']
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
    # states += [independent_variable]
    # states_rates += [sympify('0')]
    # states_units += [independent_variable_units]

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

    for ii, c in enumerate(constraints['path']):
        if constraints_lower['path'][ii] is None or constraints_upper['path'][ii] is None:
            raise NotImplementedError('Lower and upper bounds on path constraints MUST be defined.')

        hamiltonian += constraints_activators['path'][ii]/(cos(pi/2*(2*c - constraints_upper['path'][ii] - constraints_lower['path'][ii]) / (constraints_upper['path'][ii] - constraints_lower['path'][ii])))

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

    # if bc_initial[-1] == bc_terminal[-1]:
    #     breakpoint()
    #     del initial_lm_params[-1]
    #     del bc_initial[-1]
    time_bc = make_time_bc(constraints, derivative_fn, hamiltonian, independent_variable)

    if time_bc is not None:
        bc_terminal += [time_bc]

    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)

    control_law = make_control_law(dHdu, controls)

    # Generate the problem data
    # TODO: We're not handling time well. This is hardcoded.

    tf = sympify('_tf')
    bc_terminal = [bc.subs(independent_variable, tf) for bc in bc_terminal]
    dynamical_parameters = parameters + [tf]
    dynamical_parameters_units = parameters_units + [independent_variable_units]
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units
    control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]

    out = {'method': 'brysonho',
           'problem_name': problem_name,
           'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x) for x in it.chain(states, costates)],
           'states_rates':
               [str(tf * rate) for rate in states_rates] +
               [str(tf * rate) for rate in costates_rates],
           'states_units': [str(x) for x in states_units + costates_units],
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
           'control_list': [str(x) for x in it.chain(controls)],
           'controls': [str(u) for u in controls],
           'hamiltonian': str(hamiltonian),
           'hamiltonian_units': str(hamiltonian_units),
           'num_states': len(states + costates),
           'dHdu': str(dHdu),
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal],
           'control_options': control_law,
           'num_controls': len(controls)}

    def guess_map(sol):
        solout = Trajectory(sol)
        nodes = len(solout.t)
        solout.y = np.column_stack((solout.y, solout.dual))
        solout.dual = np.array([])
        solout.dynamical_parameters = np.hstack((solout.dynamical_parameters, solout.t[-1]))
        solout.nondynamical_parameters = np.ones(len(nondynamical_parameters))
        solout.t = solout.t / solout.t[-1]
        solout.u = np.array([]).reshape((nodes, 0))
        return solout

    def guess_map_inverse(sol, num_costates=len(costates)):
        sol.t = sol.t*sol.dynamical_parameters[-1]
        sol.dual = sol.y[:, -num_costates:]
        sol.y = np.delete(sol.y, np.s_[-num_costates:], axis=1)
        return sol

    return out, guess_map, guess_map_inverse


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
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.info('Control found')
    control_options = ctrl_sol
    return control_options
