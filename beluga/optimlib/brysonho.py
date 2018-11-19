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
    augmented_initial_cost, augmented_initial_cost_units = make_augmented_cost(initial_cost, initial_cost_units, constraints, location='initial')
    initial_lm_params = make_augmented_params(constraints, location='initial')
    augmented_terminal_cost, augmented_terminal_cost_units = make_augmented_cost(terminal_cost, terminal_cost_units, constraints, location='terminal')
    terminal_lm_params = make_augmented_params(constraints, location='terminal')
    hamiltonian, costates = make_hamiltonian(states, states_rates, path_cost)
    costates_rates = make_costate_rates(hamiltonian, states, costates, derivative_fn)

    for var in quantity_vars.keys():
        hamiltonian = hamiltonian.subs(Symbol(var), quantity_vars[var])

    bc_initial = make_boundary_conditions(constraints, states, costates, augmented_initial_cost, derivative_fn, location='initial')
    bc_terminal = make_boundary_conditions(constraints, states, costates, augmented_terminal_cost, derivative_fn, location='terminal')
    bc_terminal = make_time_bc(constraints, hamiltonian, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    control_law = make_control_law(dHdu, controls)
    # Generate the problem data
    tf_var = sympify('tf')
    dyna_parameters = [tf_var] + parameters
    nond_parameters = initial_lm_params + terminal_lm_params
    out = ws
    out['costates'] = costates
    out['initial_lm_params'] = initial_lm_params
    out['terminal_lm_params'] = terminal_lm_params
    out['problem_data'] = {'method': 'brysonho',
        'problem_name': problem_name,
        'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
        'state_list':[str(x) for x in it.chain(states, costates)],
        'deriv_list': [tf_var * rate for rate in states_rates] + [tf_var * rate for rate in costates_rates],
        'states': states,
        'costates': costates,
        'constants': constants,
        'constants_of_motion': constants_of_motion,
        'dynamical_parameters': dyna_parameters,
        'nondynamical_parameters': nond_parameters,
        'control_list': [str(x) for x in it.chain(controls)],
        'controls': controls,
        'quantity_vars': quantity_vars,
        'hamiltonian': hamiltonian,
        'num_states': 2 * len(states),
        'num_params': len(nond_parameters) + 1,
        'dHdu': dHdu,
        'bc_initial': [_ for _ in bc_initial],
        'bc_terminal': [_ for _ in bc_terminal],
        'control_options': control_law,
        'num_controls': len(controls),
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
