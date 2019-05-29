
import copy
from .optimlib import *
from beluga.utils import sympify
import itertools as it
import logging
import numpy as np
import sympy
# from scipy.optimize import minimize


def ocp_to_bvp(ocp, **kwargs):
    """
    Converts an OCP to a BVP using indirect methods.

    :param ocp: An OCP.
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
    constraints_method = ws['constraints_method']
    switches = ws['switches']
    switches_values = ws['switches_values']
    switches_conditions = ws['switches_conditions']
    switches_tolerance = ws['switches_tolerance']
    parameters = ws['parameters']
    parameters_units = ws['parameters_units']
    initial_cost = ws['initial_cost']
    initial_cost_units = ws['initial_cost_units']
    terminal_cost = ws['terminal_cost']
    terminal_cost_units = ws['terminal_cost_units']
    path_cost = ws['path_cost']
    path_cost_units = ws['path_cost_units']

    control_method = kwargs.get('control_method', 'pmp').lower()

    if initial_cost != 0:
        cost_units = initial_cost_units
    elif terminal_cost != 0:
        cost_units = terminal_cost_units
    elif path_cost != 0:
        cost_units = path_cost_units*independent_variable_units
    else:
        raise ValueError('Initial, path, and terminal cost functions are not defined.')

    """
    Deal with path constraints
    """
    for ii, c in enumerate(constraints['path']):
        if constraints_method['path'] is None:
            raise NotImplementedError

        if constraints_method['path'][ii].lower() == 'utm':
            path_cost += utm_path(c, constraints_lower['path'][ii], constraints_upper['path'][ii],
                                  constraints_activators['path'][ii])
        elif constraints_method['path'][ii].lower() == 'epstrig':
            path_cost += epstrig_path(c, constraints_lower['path'][ii], constraints_upper['path'][ii],
                                  constraints_activators['path'][ii])
            upper = constraints_upper['path'][ii]
            lower = constraints_lower['path'][ii]
            subber = dict(zip([constraints['path'][ii]], [(upper - lower)/2*sympy.sin(constraints['path'][ii]) + (upper+lower)/2]))
            for ii in range(len(states_rates)):
                states_rates[ii] = states_rates[ii].subs(subber, simultaneous=True)
        else:
            raise NotImplementedError('Unknown path constraint method \"' + str(constraints_method['path'][ii]) + '\"')

    """
    Deal with staging and switches
    """
    for ii in range(len(switches)):
        if isinstance(switches_values[ii], list):
            true_value = 0
            for jj in range(len(switches_values[ii])):
                temp_value = switches_values[ii][jj]
                for kk in range(len(switches_conditions[ii][jj])):
                    temp_value *= rash_mult(switches_conditions[ii][jj][kk], switches_tolerance[ii])
                true_value += temp_value
            switches_values[ii] = true_value

    """
    Make substitutions with the switches
    """
    switch_vars, switch_list, derivative_fn = process_quantities(switches, switches_values)
    for var in switch_vars.keys():
        initial_cost = initial_cost.subs(Symbol(var), switch_vars[var])
        path_cost = path_cost.subs(Symbol(var), switch_vars[var])
        terminal_cost = terminal_cost.subs(Symbol(var), switch_vars[var])
        for ii in range(len(states_rates)):
            states_rates[ii] = states_rates[ii].subs(Symbol(var), switch_vars[var])

    terminal_bcs_to_aug = [[bc, units] for bc, units in zip(constraints['terminal'], constraints_units['terminal']) if
                           derivative_fn(bc, independent_variable) == 0]
    terminal_bcs_time = [[bc, units] for bc, units in zip(constraints['terminal'], constraints_units['terminal']) if
                         derivative_fn(bc, independent_variable) != 0]

    constraints['terminal'] = [bc[0] for bc in terminal_bcs_to_aug]
    constraints_units['terminal'] = [bc[1] for bc in terminal_bcs_to_aug]

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

    constraints['terminal'] += [bc[0] for bc in terminal_bcs_time]
    bc_terminal += [bc[0] for bc in terminal_bcs_time]
    constraints_units['terminal'] += [bc[1] for bc in terminal_bcs_time]

    # if bc_initial[-1] == bc_terminal[-1]:
    #     breakpoint()
    #     del initial_lm_params[-1]
    #     del bc_initial[-1]
    time_bc = make_time_bc(constraints, derivative_fn, hamiltonian, independent_variable)

    if time_bc is not None:
        bc_terminal += [time_bc]

    dh_du = make_dhdu(hamiltonian, controls, derivative_fn)
    if control_method == 'pmp':
        control_law = make_control_law(dh_du, controls)
        control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]
        dae_states = []
        dae_rates = []
        dae_units = []
        dae_bc = []
        num_dae = 0
    elif control_method == 'icrm':
        dae_states, dae_rates, dae_bc, temp_dgdX, temp_dgdU = make_control_dae(states, costates, states_rates,
                                                                               costates_rates, controls, dh_du,
                                                                               derivative_fn)
        dae_units = controls_units
        controls = []
        control_law = []
        num_dae = len(dae_states)
    else:
        raise NotImplementedError('Unknown control method \"' + control_method + '\"')

    # Generate the problem data
    # TODO: We're not handling time well. This is hardcoded.

    tf = sympify('_tf')
    bc_terminal = [bc.subs(independent_variable, tf) for bc in bc_terminal]
    dynamical_parameters = parameters + [tf]
    dynamical_parameters_units = parameters_units + [independent_variable_units]
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units
    # breakpoint()

    out = {'method': 'brysonho',
           'problem_name': problem_name,
           'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x) for x in it.chain(states, costates, dae_states)],
           'states_rates':
               [str(tf * rate) for rate in states_rates] +
               [str(tf * rate) for rate in costates_rates] +
               [str(tf * rate) for rate in dae_rates],
           'states_units': [str(x) for x in states_units + costates_units + dae_units],
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
           'dHdu': str(dh_du),
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal + dae_bc],
           'control_options': control_law,
           'num_controls': len(controls)}

    def guess_map(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol_out = copy.deepcopy(sol)
        nodes = len(sol.t)

        if num_dae == 0:
            sol_out.y = np.column_stack((sol.y, sol.dual))
        else:
            sol_out.y = np.column_stack((sol.y, sol.dual, sol.u))

        sol_out.dual = np.array([])
        sol_out.dynamical_parameters = np.hstack((sol.dynamical_parameters, sol.t[-1]))
        sol_out.nondynamical_parameters = np.ones(len(nondynamical_parameters))
        sol_out.t = sol.t / sol.t[-1]
        sol_out.u = np.array([]).reshape((nodes, 0))
        return sol_out

    def guess_map_inverse(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol = copy.deepcopy(sol)
        sol.t = sol.t*sol.dynamical_parameters[-1]
        sol.u = np.vstack([_compute_control(yi, None, sol.dynamical_parameters, sol.const) for yi in sol.y])
        if num_dae == 0:
            sol.dual = sol.y[:, -len(costates):]
        else:
            sol.u = sol.y[:, -num_dae:]
            sol.dual = sol.y[:, -len(costates)-num_dae:-num_dae]
        sol.y = np.delete(sol.y, np.s_[-len(costates)-num_dae:], axis=1)
        sol.dynamical_parameters = np.delete(sol.dynamical_parameters, np.s_[-1:])
        sol.nondynamical_parameters = np.delete(sol.nondynamical_parameters, np.s_[-len(nondynamical_parameters):])
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
    logging.debug("Attempting using SymPy (v" + __version__ + ")...")
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.debug('Control found')
    control_options = ctrl_sol
    return control_options
