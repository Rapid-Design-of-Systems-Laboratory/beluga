"""
Computes the necessary conditions of optimality using Bryson & Ho's method
"""

from .optimlib import *
from beluga.utils import sympify
import itertools as it
import logging


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

    augmented_initial_cost, augmented_initial_cost_units, initial_lm_params, initial_lm_params_units = make_augmented_cost(initial_cost, cost_units, constraints, constraints_units, location='initial')
    augmented_terminal_cost, augmented_terminal_cost_units, terminal_lm_params, terminal_lm_params_units = make_augmented_cost(terminal_cost, cost_units, constraints, constraints_units, location='terminal')
    hamiltonian, hamiltonian_units, costates, costates_units = make_hamiltonian(states, states_rates, states_units, path_cost, cost_units)
    costates_rates = make_costate_rates(hamiltonian, states, costates, derivative_fn)
    bc_initial = make_boundary_conditions(constraints, states, costates, augmented_initial_cost, derivative_fn, location='initial')
    bc_terminal = make_boundary_conditions(constraints, states, costates, augmented_terminal_cost, derivative_fn, location='terminal')
    bc_terminal = make_time_bc(constraints, hamiltonian, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    control_law = make_control_law(dHdu, controls)

    # Generate the problem data
    tf_var = sympify('tf')
    dynamical_parameters = [tf_var] + parameters
    dynamical_parameters_units = [independent_variable_units] + parameters_units
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units
    control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]

    out = {'method': 'brysonho',
           'problem_name': problem_name,
           'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
           'states': [str(x) for x in it.chain(states, costates)],
           'states_units': [str(x) for x in states_units + costates_units],
           'deriv_list': [str(tf_var * rate) for rate in states_rates] + [str(tf_var * rate) for rate in costates_rates],
           'constants': [str(c) for c in constants],
           'constants_units': [str(c) for c in constants_units],
           'constants_values': [float(c) for c in constants_values],
           'constants_of_motion': [str(c) for c in constants_of_motion],
           'dynamical_parameters': [str(c) for c in dynamical_parameters],
           'dynamical_parameters_units': [str(c) for c in dynamical_parameters_units],
           'nondynamical_parameters': [str(c) for c in nondynamical_parameters],
           'nondynamical_parameters_units': [str(c) for c in nondynamical_parameters_units],
           'independent_variable': str(independent_variable),
           'independent_variable_units': str(independent_variable_units),
           'control_list': [str(x) for x in it.chain(controls)],
           'controls': [str(u) for u in controls],
           'hamiltonian': str(hamiltonian),
           'hamiltonian_units': str(hamiltonian_units),
           'num_states': 2 * len(states),
           'dHdu': str(dHdu),
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal],
           'control_options': control_law,
           'num_controls': len(controls)}

    def guess_mapper(sol):
        return sol

    return out, guess_mapper


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
