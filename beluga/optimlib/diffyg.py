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

    ocp_num_states = len(states)
    ocp_num_controls = len(controls)

    analytical_jacobian = kwargs.get('analytical_jacobian', False)
    control_method = kwargs.get('control_method', 'pmp').lower()

    if initial_cost != 0:
        cost_units = initial_cost_units
    elif terminal_cost != 0:
        cost_units = terminal_cost_units
    elif path_cost != 0:
        cost_units = path_cost_units*independent_variable_units
    else:
        raise ValueError('Initial, path, and terminal cost functions are not defined.')

    states += [independent_variable]
    states_units += [independent_variable_units]
    states_rates += [sympify('1')]
    independent_index = len(states) - 1

    """
    Deal with path constraints
    """

    control_constraint_mapping = dict()

    for ii, c in enumerate(constraints['path']):
        if constraints_method['path'] is None:
            raise NotImplementedError

        if constraints_method['path'][ii].lower() == 'utm':
            path_cost += utm_path(c, constraints_lower['path'][ii], constraints_upper['path'][ii],
                                  constraints_activators['path'][ii])
        elif constraints_method['path'][ii].lower() == 'epstrig':
            constraint_is_control = False
            for jj, val in enumerate(controls):
                if constraints['path'][ii] == val:
                    constraint_is_control = True
                    control_constraint_mapping.update({ii: jj})

            if not constraint_is_control:
                raise NotImplementedError('Epsilon-Trig must be used with pure control-constraints.')

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

    """
    Begin dualization process
    """
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

    omega = make_standard_symplectic_form(states, costates)
    X_H = make_hamiltonian_vector_field(hamiltonian, omega, states + costates, derivative_fn)
    n = len(states)

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

    time_bc = make_time_bc(constraints, derivative_fn, hamiltonian, independent_variable)

    if time_bc is not None:
        bc_terminal += [time_bc]

    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    if control_method == 'pmp':
        control_law = make_control_law(dHdu, controls)
        control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]
        dae_states = []
        dae_rates = []
        dae_units = []
        dae_bc = []
        num_dae = 0
    elif control_method == 'icrm':
        n0 = len(states)
        dae_states, dae_rates, dae_bc, temp_dgdX, temp_dgdU = make_control_dae(states, costates, X_H[:n],
                                                                               X_H[n:], controls, dHdu,
                                                                               derivative_fn)

        lamU = make_costate_names(dae_states)
        ndae = len(dae_states)
        lamU_units = [cost_units/unit for unit in controls_units]
        states += dae_states
        costates += lamU
        states_units += controls_units
        costates_units += lamU_units

        n = len(states)
        omega_new = make_standard_symplectic_form(states, costates)

        # Add (du - u' dt) ^ (dlamU - 0 dt) to omega
        for ii, u in enumerate(dae_rates):
            # breakpoint()
            omega_new[int(n - ndae + ii), int(2*n - ndae + ii)] = 1
            omega_new[int(2*n - ndae + ii), int(n - ndae + ii)] = -1
            omega_new[independent_index, int(2*n - ndae + ii)] = -dae_rates[ii]
            omega_new[int(2*n - ndae + ii), independent_index] = dae_rates[ii]

        for ii, lU in enumerate(lamU):
            bc_initial += [lU]

        omega = omega_new
        dae_units = controls_units
        controls = []
        control_law = []
        # breakpoint()
        bc_terminal += dae_bc
        num_dae = len(dae_states)
    elif control_method == 'numerical':
        dae_states = []
        dae_rates = []
        dae_units = []
        dae_bc = []
        num_dae = 0
        control_law = []
    else:
        raise NotImplementedError('Unknown control method \"' + control_method + '\"')

    # Generate the problem data
    # TODO: We're not handling time well. This is hardcoded.

    tf = sympify('_tf')
    dynamical_parameters = parameters + [tf]
    dynamical_parameters_units = parameters_units + [independent_variable_units]
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units

    # Scale the differential structure by time.
    omega = omega/tf
    # hamiltonian = hamiltonian*tf
    if not is_symplectic(omega):
        logging.warning('Hamiltonian BVP improperly formed!')
    basis = states + costates
    X_H = make_hamiltonian_vector_field(hamiltonian, omega, basis, derivative_fn)

    """
    Dualization complete
    """

    if analytical_jacobian:
        if control_method == 'pmp':
            raise NotImplementedError('Analytical Jacobian calculation is not implemented for PMP control method.')

        df_dy = [['0' for f in X_H] for s in basis]
        for ii, f in enumerate(X_H):
            for jj, s in enumerate(states + costates):
                df_dy[ii][jj] = str(derivative_fn(f, s))

        df_dp = [['0' for s in dynamical_parameters] for f in X_H]
        for ii, f in enumerate(X_H):
            for jj, s in enumerate(dynamical_parameters):
                df_dp[ii][jj] = str(derivative_fn(f, s))

        dbc_dya = [['0' for s in basis] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_initial):
            for jj, s in enumerate(basis):
                dbc_dya[ii][jj] = str(derivative_fn(f, s))

        dbc_dyb = [['0' for s in basis] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_terminal):
            for jj, s in enumerate(basis):
                dbc_dyb[ii + len(bc_initial)][jj] = str(derivative_fn(f, s))

        dbc_dp_a = [['0' for s in dynamical_parameters + nondynamical_parameters] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_initial):
            for jj, s in enumerate(dynamical_parameters + nondynamical_parameters):
                dbc_dp_a[ii][jj] = str(derivative_fn(f, s))

        dbc_dp_b = [['0' for s in dynamical_parameters + nondynamical_parameters] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_terminal):
            for jj, s in enumerate(dynamical_parameters + nondynamical_parameters):
                dbc_dp_b[ii + len(bc_initial)][jj] = str(derivative_fn(f, s))

    else:
        df_dy = None
        df_dp = None
        dbc_dya = None
        dbc_dyb = None
        dbc_dp_a = None
        dbc_dp_b = None

    out = {'method': 'brysonho',
           'problem_name': problem_name,
           'control_method': control_method,
           'consts': [str(k) for k in constants],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x) for x in it.chain(states, costates)],
           'states_rates': [str(rate) for rate in X_H],
           'states_units': [str(x) for x in states_units + costates_units],
           'states_jac': [df_dy, df_dp],
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
           'dHdu': [str(x) for x in dHdu],
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal],
           'bc_initial_jac': dbc_dya,
           'bc_terminal_jac': dbc_dyb,
           'bc_initial_parameter_jac': dbc_dp_a,
           'bc_terminal_parameter_jac': dbc_dp_b,
           'control_options': control_law,
           'num_controls': len(controls)}

    def guess_map(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol_out = copy.deepcopy(sol)
        nodes = len(sol.t)

        if len(sol.dual_t) == 0:
            sol.dual_t = np.zeros_like(sol.t)

        if len(sol.dual_u) == 0:
            sol.dual_u = np.zeros_like(sol.u)

        if num_dae == 0:
            sol_out.y = np.column_stack((sol.y, sol.t, sol.dual, sol.dual_t))
        else:
            sol_out.y = np.column_stack((sol.y, sol.t, sol.u, sol.dual, sol.dual_t, sol.dual_u))

        sol_out.dual = np.array([])
        sol_out.dual_t = np.array([])
        sol_out.dynamical_parameters = np.hstack((sol.dynamical_parameters, sol.t[-1] - sol.t[0]))
        sol_out.nondynamical_parameters = np.ones(len(nondynamical_parameters))

        sol_out.t = sol.t / sol.t[-1]
        sol_out.u = np.array([]).reshape((nodes, 0))
        return sol_out

    def guess_map_inverse(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol_out = copy.deepcopy(sol)
        sol_out.t = sol.y[:, independent_index]
        sol_out.dual_t = sol.y[:, (independent_index + 1) * 2 - 1 + num_dae]

        if num_dae == 0:
            sol_out.u = np.vstack([_compute_control(yi, None, sol.dynamical_parameters, sol.const) for yi in sol.y])
            sol_out.dual_u = np.full_like(sol_out.u, np.nan)
        else:
            sol_out.u = sol.y[:, ocp_num_states+1:ocp_num_states+1+ocp_num_controls]
            sol_out.dual_u = sol.y[:, -ocp_num_controls:]

        sol_out.y = sol.y[:, :ocp_num_states]
        sol_out.dual = sol.y[:, ocp_num_states+1+num_dae:2*ocp_num_states+1+num_dae]
        sol_out.dynamical_parameters = sol.dynamical_parameters[:-1]
        sol_out.nondynamical_parameters = sol.nondynamical_parameters[:-len(nondynamical_parameters)]

        cmap = dict(zip([str(c) for c in constants], np.arange(0, len(constants))))

        for ele in control_constraint_mapping.keys():
            ctrl = control_constraint_mapping[ele]
            lower = str(constraints_lower['path'][ele])
            upper = str(constraints_upper['path'][ele])
            for ele2 in cmap.keys():
                upper = upper.replace(ele2, str(sol.const[cmap[ele2]]))
                lower = lower.replace(ele2, str(sol.const[cmap[ele2]]))

            upper = eval(upper)
            lower = eval(lower)
            sol_out.u[:, ctrl] = (upper - lower) * (np.sin(sol_out.u[:, ctrl]) + 1) / 2 + lower

        return sol_out

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
    logging.debug("Solving dH/du...")
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.debug('Control found')
    control_options = ctrl_sol
    return control_options
