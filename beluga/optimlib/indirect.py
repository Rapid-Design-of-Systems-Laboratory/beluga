
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
    signature = 'Sigma'
    cat_chain = [ocp]
    gamma_map_chain = []
    gamma_map_inverse_chain = []
    # ws = init_workspace(ocp)
    # problem_name = ws['problem_name']
    # independent_variable = ws['independent_var']
    # independent_variable_units = ws['independent_var_units']
    # states = ws['states']
    # states_rates = ws['states_rates']
    # states_units = ws['states_units']
    # controls = ws['controls']
    # controls_units = ws['controls_units']
    # constants = ws['constants']
    # constants_units = ws['constants_units']
    # constants_values = ws['constants_values']
    # constants_of_motion = ws['constants_of_motion']
    # constants_of_motion_values = ws['constants_of_motion_values']
    # constants_of_motion_units = ws['constants_of_motion_units']
    # constraints = ws['constraints']
    # constraints_units = ws['constraints_units']
    # constraints_lower = ws['constraints_lower']
    # constraints_upper = ws['constraints_upper']
    # constraints_activators = ws['constraints_activators']
    # constraints_method = ws['constraints_method']
    # switches = ws['switches']
    # switches_values = ws['switches_values']
    # switches_conditions = ws['switches_conditions']
    # switches_tolerance = ws['switches_tolerance']
    # parameters = ws['parameters']
    # parameters_units = ws['parameters_units']
    # initial_cost = ws['initial_cost']
    # initial_cost_units = ws['initial_cost_units']
    # terminal_cost = ws['terminal_cost']
    # terminal_cost_units = ws['terminal_cost_units']
    # path_cost = ws['path_cost']
    # path_cost_units = ws['path_cost_units']

    analytical_jacobian = kwargs.get('analytical_jacobian', False)
    control_method = kwargs.get('control_method', 'pmp').lower()

    # if initial_cost != 0:
    #     cost_units = initial_cost_units
    # elif terminal_cost != 0:
    #     cost_units = terminal_cost_units
    # elif path_cost != 0:
    #     cost_units = path_cost_units*independent_variable_units
    # else:
    #     raise ValueError('Initial, path, and terminal cost functions are not defined.')
    independent_var = ocp._properties['independent']['symbol']
    independent_var_units = ocp._properties['independent']['unit']

    _ocp, _gam, _gam_inv = F_momentumshift(ocp)
    signature = 'F_momentumshift . ' + signature
    cat_chain += [_ocp]
    gamma_map_chain += [_gam]
    gamma_map_inverse_chain += [_gam_inv]
    independent_index = len(_ocp.states()) - 1

    """
    Deal with path constraints
    """

    control_constraint_mapping = dict()

    while len(_ocp.constraints()['path']) > 0:
        if _ocp.constraints()['path'][0]['method'] is None:
            raise NotImplementedError

        elif _ocp.constraints()['path'][0]['method'].upper() == 'UTM':
            _ocp, _gam, _gam_inv = F_UTM(_ocp)
            signature = 'F_UTM . ' + signature
            cat_chain += [_ocp]
            gamma_map_chain += [_gam]
            gamma_map_inverse_chain += [_gam_inv]

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
    # TODO: compose switches
    # for ii in range(len(switches)):
    #     if isinstance(switches_values[ii], list):
    #         true_value = 0
    #         for jj in range(len(switches_values[ii])):
    #             temp_value = switches_values[ii][jj]
    #             for kk in range(len(switches_conditions[ii][jj])):
    #                 temp_value *= rash_mult(switches_conditions[ii][jj][kk], switches_tolerance[ii])
    #             true_value += temp_value
    #         switches_values[ii] = true_value

    """
    Make substitutions with the switches
    """
    # # TODO: compose switches
    # switch_vars, switch_list, derivative_fn = process_quantities(switches, switches_values)
    # for var in switch_vars.keys():
    #     initial_cost = initial_cost.subs(Symbol(var), switch_vars[var])
    #     path_cost = path_cost.subs(Symbol(var), switch_vars[var])
    #     terminal_cost = terminal_cost.subs(Symbol(var), switch_vars[var])
    #     for ii in range(len(states_rates)):
    #         states_rates[ii] = states_rates[ii].subs(Symbol(var), switch_vars[var])

    _bvp, _gam, _gam_inv = Dualize(_ocp, independent_var, independent_var_units)
    signature = 'D . ' + signature
    cat_chain += [_bvp]
    gamma_map_chain += [_gam]
    gamma_map_inverse_chain += [_gam_inv]


    if control_method == 'pmp':
        control_law = make_control_law(dHdu, controls)
        control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]
        dae_states = []
        dae_rates = []
        dae_units = []
        num_dae = 0
    elif control_method == 'icrm':
        _bvp, _gam, _gam_inv = F_ICRM(_bvp)
        signature = 'F_ICRM . ' + signature
        cat_chain += [_bvp]
        gamma_map_chain += [_gam]
        gamma_map_inverse_chain += [_gam_inv]

    elif control_method == 'numerical':
        dae_states = []
        dae_rates = []
        dae_units = []
        num_dae = 0
        control_law = []
    else:
        raise NotImplementedError('Unknown control method \"' + control_method + '\"')

    # Generate the problem data
    # TODO: We're not handling time well. This is hardcoded.
    # bc_terminal = [bc.subs(independent_variable, tf) for bc in bc_terminal]
    # dynamical_parameters = parameters + [tf]
    # dynamical_parameters_units = parameters_units + [independent_variable_units]
    # nondynamical_parameters = initial_lm_params + terminal_lm_params
    # nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units

    # states_rates = [tf*f for f in states_rates]
    # costates_rates = [tf*f for f in costates_rates]
    # dae_rates = [tf*f for f in dae_rates]
    if analytical_jacobian:
        if control_method == 'pmp':
            raise NotImplementedError('Analytical Jacobian calculation is not implemented for PMP control method.')
        states = [s['symbol'] for s in _bvp._properties['states']]
        rates = [s['eom'] for s in _bvp._properties['states']]
        df_dy = [['0' for f in rates] for s in states]
        for ii, f in enumerate(states_rates + costates_rates + dae_rates):
            for jj, s in enumerate(states + costates + dae_states):
                df_dy[ii][jj] = str(total_derivative(f, s))

        df_dp = [['0' for s in dynamical_parameters] for f in states_rates + costates_rates + dae_rates]
        for ii, f in enumerate(states_rates + costates_rates + dae_rates):
            for jj, s in enumerate(dynamical_parameters):
                df_dp[ii][jj] = str(total_derivative(f, s))

        dbc_dya = [['0' for s in states + costates + dae_states] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_initial):
            for jj, s in enumerate(states + costates + dae_states):
                dbc_dya[ii][jj] = str(total_derivative(f, s))

        dbc_dyb = [['0' for s in states + costates + dae_states] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_terminal):
            for jj, s in enumerate(states + costates + dae_states):
                dbc_dyb[ii + len(bc_initial)][jj] = str(total_derivative(f, s))

        dbc_dp_a = [['0' for s in dynamical_parameters + nondynamical_parameters] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_initial):
            for jj, s in enumerate(dynamical_parameters + nondynamical_parameters):
                dbc_dp_a[ii][jj] = str(total_derivative(f, s))

        dbc_dp_b = [['0' for s in dynamical_parameters + nondynamical_parameters] for f in bc_initial + bc_terminal]
        for ii, f in enumerate(bc_terminal):
            for jj, s in enumerate(dynamical_parameters + nondynamical_parameters):
                dbc_dp_b[ii + len(bc_initial)][jj] = str(total_derivative(f, s))

    else:
        df_dy = None
        df_dp = None
        dbc_dya = None
        dbc_dyb = None
        dbc_dp_a = None
        dbc_dp_b = None

    logging.info('Problem formulation: Lambda := ' + signature)

    dHdu = make_dhdu(_bvp._properties['constants_of_motion'][0]['function'], _bvp._properties.get('controls', []), total_derivative)

    out = {'method': 'brysonho',
           'problem_name': _ocp.name,
           'control_method': control_method,
           'consts': [str(k['symbol']) for k in ocp.constants()],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x['symbol']) for x in _bvp._properties['states']],
           'states_rates': [str(x['eom']) for x in _bvp._properties['states']],
           'states_units': [str(x['unit']) for x in _bvp._properties['states']],
           'states_jac': [df_dy, df_dp],
           'quads': [str(x['symbol']) for x in _bvp.quads()],
           'quads_rates': [str(x['eom']) for x in _bvp.quads()], # TODO: Maybe multiply this by tf?
           'quads_units': [str(x['unit']) for x in _bvp.quads()],
           'path_constraints': [],
           'path_constraints_units': [],
           'constants': [str(c['symbol']) for c in _ocp.constants()],
           'constants_units': [str(c['unit']) for c in _ocp.constants()],
           'constants_values': [float(c['value']) for c in _ocp.constants()],
           'constants_of_motion': [str(c['function']) for c in ocp.constants_of_motion()],
           'dynamical_parameters': [str(c['symbol']) for c in _bvp._properties['parameters']],
           'dynamical_parameters_units': [str(c['unit']) for c in _bvp._properties['parameters']],
           'nondynamical_parameters': [str(c['symbol']) for c in _bvp._properties['nd_parameters']],
           'nondynamical_parameters_units': [str(c['unit']) for c in _bvp._properties['nd_parameters']],
           'control_list': [str(x['symbol']) for x in _bvp._properties.get('controls', dict())],
           'controls': [str(u['symbol']) for u in _bvp._properties.get('controls', dict())],
           'hamiltonian': str(_bvp._properties['constants_of_motion'][0]['function']),
           'hamiltonian_units': str(_bvp._properties['constants_of_motion'][0]['unit']),
           'num_states': len(_bvp._properties['states']),
           'dHdu': [str(x) for x in dHdu],
           'bc_initial': [str(x['function']) for x in _bvp._properties['bc_initial']],
           'bc_terminal': [str(x['function']) for x in _bvp._properties['bc_terminal']],
           'bc_initial_jac': dbc_dya,
           'bc_terminal_jac': dbc_dyb,
           'bc_initial_parameter_jac': dbc_dp_a,
           'bc_terminal_parameter_jac': dbc_dp_b,
           'control_options': [],
           'num_controls': len(_bvp._properties.get('controls', dict()))}

    def guess_map(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol_out = copy.deepcopy(sol)
        nodes = len(sol.t)

        if len(sol.dual_t) == 0:
            sol.dual_t = np.zeros_like(sol.t)

        if num_dae == 0:
            sol_out.y = np.column_stack((sol.y, sol.t, sol.dual, sol.dual_t))
        else:
            sol_out.y = np.column_stack((sol.y, sol.t, sol.dual, sol.dual_t, sol.u))

        sol_out.dual = np.array([])
        sol_out.dual_t = np.array([])
        sol_out.dual_u = np.array([])
        sol_out.dynamical_parameters = np.hstack((sol.dynamical_parameters, sol.t[-1] - sol.t[0]))
        sol_out.nondynamical_parameters = np.ones(len(nondynamical_parameters))

        sol_out.t = sol.t / sol.t[-1]
        sol_out.u = np.array([]).reshape((nodes, 0))
        return sol_out

    def guess_map_inverse(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol = copy.deepcopy(sol)
        sol.t = sol.y[:, independent_index]
        sol.dual_t = sol.y[:, (independent_index+1)*2-1]
        if num_dae == 0:
            sol.u = np.vstack([_compute_control(yi, None, sol.dynamical_parameters, sol.const) for yi in sol.y])
            sol.y = np.delete(sol.y, np.s_[independent_index, (independent_index + 1) * 2 - 1], axis=1)
            sol.dual = sol.y[:, -(len(costates)-1):]
        else:
            sol.u = sol.y[:, -num_dae:]
            sol.y = np.delete(sol.y, np.s_[independent_index, (independent_index + 1) * 2 - 1], axis=1)
            sol.dual = sol.y[:, -(len(costates)-1)-num_dae:-num_dae]

        sol.y = np.delete(sol.y, np.s_[-(len(costates)-1)-num_dae:], axis=1)
        sol.dynamical_parameters = np.delete(sol.dynamical_parameters, np.s_[-1:])
        sol.nondynamical_parameters = np.delete(sol.nondynamical_parameters, np.s_[-len(nondynamical_parameters):])

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
            sol.u[:, ctrl] = (upper - lower) * (np.sin(sol.u[:, ctrl]) + 1)/2 + lower

        return sol

    def guess_map(gamma, _compute_control=None, map_chain=gamma_map_chain):
        gamma = copy.deepcopy(gamma)
        for morphism in map_chain:
            gamma = morphism(gamma)
        return gamma

    def guess_map_inverse(gamma, _compute_control=None, map_chain=gamma_map_inverse_chain):
        gamma = copy.deepcopy(gamma)
        for morphism in reversed(map_chain):
            gamma = morphism(gamma)
        return gamma

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
