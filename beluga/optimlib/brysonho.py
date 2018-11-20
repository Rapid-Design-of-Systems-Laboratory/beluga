"""
Computes the necessary conditions of optimality using Bryson & Ho's method
"""

from .optimlib import *
from beluga.utils import sympify
import itertools as it
import logging


def ocp_to_bvp(ocp, guess):
    ws = init_workspace(ocp, guess)
    problem_name = ws['problem_name']
    independent_variable = ws['independent_var']
    states = ws['states']
    states_rates = ws['states_rates']
    controls = ws['controls']
    constants = ws['constants']
    constants_of_motion = ws['constants_of_motion']
    constraints = ws['constraints']
    quantities = ws['quantities']
    quantities_values = ws['quantities_values']
    parameters = ws['parameters']
    initial_cost = ws['initial_cost']
    initial_cost_units = ws['initial_cost_units']
    terminal_cost = ws['terminal_cost']
    terminal_cost_units = ws['terminal_cost_units']
    path_cost = ws['path_cost']

    quantity_vars, quantity_list, derivative_fn = process_quantities(quantities, quantities_values)
    for var in quantity_vars.keys():
        for ii in range(len(states_rates)):
            states_rates[ii] = states_rates[ii].subs(Symbol(var), quantity_vars[var])

    augmented_initial_cost, augmented_initial_cost_units = make_augmented_cost(initial_cost, initial_cost_units, constraints, location='initial')
    initial_lm_params = make_augmented_params(constraints, location='initial')
    augmented_terminal_cost, augmented_terminal_cost_units = make_augmented_cost(terminal_cost, terminal_cost_units, constraints, location='terminal')
    terminal_lm_params = make_augmented_params(constraints, location='terminal')
    hamiltonian, costates = make_hamiltonian(states, states_rates, path_cost)
    costates_rates = make_costate_rates(hamiltonian, states, costates, derivative_fn)
    bc_initial = make_boundary_conditions(constraints, states, costates, augmented_initial_cost, derivative_fn, location='initial')
    bc_terminal = make_boundary_conditions(constraints, states, costates, augmented_terminal_cost, derivative_fn, location='terminal')
    bc_terminal = make_time_bc(constraints, hamiltonian, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    control_law = make_control_law(dHdu, controls)

    # Generate the problem data
    tf_var = sympify('tf')
    dyna_parameters = [tf_var] + parameters
    nond_parameters = initial_lm_params + terminal_lm_params
    control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]
    out = ws
    out['costates'] = costates
    out['initial_lm_params'] = initial_lm_params
    out['terminal_lm_params'] = terminal_lm_params
    out['problem_data'] = {'method': 'brysonho',
        'problem_name': problem_name,
        'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
        'states': [str(x) for x in it.chain(states, costates)],
        'deriv_list': [str(tf_var * rate) for rate in states_rates] + [str(tf_var * rate) for rate in costates_rates],
        'constants': [str(c) for c in constants],
        'constants_of_motion': [str(c) for c in constants_of_motion],
        'dynamical_parameters': [str(c) for c in dyna_parameters],
        'nondynamical_parameters': [str(c) for c in nond_parameters],
        'control_list': [str(x) for x in it.chain(controls)],
        'controls': [str(u) for u in controls],
        'hamiltonian': str(hamiltonian),
        'num_states': 2 * len(states),
        'dHdu': str(dHdu),
        'bc_initial': [str(_) for _ in bc_initial],
        'bc_terminal': [str(_) for _ in bc_terminal],
        'control_options': control_law,
        'num_controls': len(controls)}
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
