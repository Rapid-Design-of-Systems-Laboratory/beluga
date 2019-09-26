
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

    analytical_jacobian = kwargs.get('analytical_jacobian', False)
    control_method = kwargs.get('control_method', 'pmp').lower()

    independent_var = ocp._properties['independent']['symbol']
    independent_var_units = ocp._properties['independent']['unit']

    ocp, gam, gam_inv = F_momentumshift(ocp)
    signature = 'F_momentumshift . ' + signature
    cat_chain += [ocp]
    gamma_map_chain += [gam]
    gamma_map_inverse_chain += [gam_inv]
    independent_index = len(ocp.states()) - 1

    """
    Deal with path constraints
    """
    while len(ocp.constraints()['path']) > 0:
        if ocp.constraints()['path'][0]['method'] is None:
            raise NotImplementedError

        elif ocp.constraints()['path'][0]['method'].upper() == 'UTM':
            ocp, gam, gam_inv = F_UTM(ocp)
            signature = 'F_UTM . ' + signature
            cat_chain += [ocp]
            gamma_map_chain += [gam]
            gamma_map_inverse_chain += [gam_inv]

        elif ocp.constraints()['path'][0]['method'].upper() == 'EPSTRIG':
            ocp, gam, gam_inv = F_EPSTRIG(ocp)
            signature = 'F_EPSTRIG . ' + signature
            cat_chain += [ocp]
            gamma_map_chain += [gam]
            gamma_map_inverse_chain += [gam_inv]

        else:
            raise NotImplementedError('Unknown path constraint method \"' + str(ocp.constraints()['path'][0]['method'].upper()) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(ocp.switches()) > 0:
        ocp, gam, gam_inv = F_RASHS(ocp)
        signature = 'F_RASHS . ' + signature
        cat_chain += [ocp]
        gamma_map_chain += [gam]
        gamma_map_inverse_chain += [gam_inv]

    """
    Dualize the problem.
    """
    bvp, gam, gam_inv = Dualize(ocp, independent_var, independent_var_units)
    signature = 'D . ' + signature
    cat_chain += [bvp]
    gamma_map_chain += [gam]
    gamma_map_inverse_chain += [gam_inv]

    """
    Build a control law.
    """
    if control_method.upper() == 'PMP':
        bvp, gam, gam_inv = F_PMP(bvp)
        signature = 'F_PMP . ' + signature
        cat_chain += [bvp]
        gamma_map_chain += [gam]
        gamma_map_inverse_chain += [gam_inv]

    elif control_method.upper() == 'ICRM':
        bvp, gam, gam_inv = F_ICRM(bvp)
        signature = 'F_ICRM . ' + signature
        cat_chain += [bvp]
        gamma_map_chain += [gam]
        gamma_map_inverse_chain += [gam_inv]

    elif control_method.upper() == 'NUMERICAL':
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

        df_dy = [['0' for f in bvp.states()] for s in bvp.states()]
        for ii, f in enumerate(bvp.states()):
            for jj, s in enumerate(bvp.states()):
                df_dy[ii][jj] = str(total_derivative(f['eom'], s['symbol']))

        df_dp = [['0' for s in bvp.parameters()] for f in bvp.states()]
        for ii, f in enumerate(bvp.states()):
            for jj, s in enumerate(bvp.parameters()):
                df_dp[ii][jj] = str(total_derivative(f['eom'], s['symbol']))

        dbc_dya = [['0' for s in bvp.states()] for f in bvp.all_bcs()]
        for ii, f in enumerate(bvp.initial_bcs()):
            for jj, s in enumerate(bvp.states()):
                dbc_dya[ii][jj] = str(total_derivative(f['function'], s['symbol']))

        dbc_dyb = [['0' for s in bvp.states()] for f in bvp.all_bcs()]
        for ii, f in enumerate(bvp.terminal_bcs()):
            for jj, s in enumerate(bvp.states()):
                dbc_dyb[ii + len(bvp.initial_bcs())][jj] = str(total_derivative(f['function'], s['symbol']))

        dbc_dp_a = [['0' for s in bvp.all_parameters()] for f in bvp.all_bcs()]
        for ii, f in enumerate(bvp.initial_bcs()):
            for jj, s in enumerate(bvp.all_parameters()):
                dbc_dp_a[ii][jj] = str(total_derivative(f['function'], s['symbol']))

        dbc_dp_b = [['0' for s in bvp.all_parameters()] for f in bvp.all_bcs()]
        for ii, f in enumerate(bvp.terminal_bcs()):
            for jj, s in enumerate(bvp.all_parameters()):
                dbc_dp_b[ii + len(bvp.initial_bcs())][jj] = str(total_derivative(f['function'], s['symbol']))

    else:
        df_dy = None
        df_dp = None
        dbc_dya = None
        dbc_dyb = None
        dbc_dp_a = None
        dbc_dp_b = None

    logging.info('Problem formulation: Lambda := ' + signature)

    dHdu = make_dhdu(bvp._properties['constants_of_motion'][0]['function'], bvp._properties.get('controls', []), total_derivative)

    out = {'method': 'brysonho',
           'problem_name': cat_chain[0].name,
           'control_method': control_method,
           'consts': [str(k['symbol']) for k in ocp.constants()],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x['symbol']) for x in bvp.states()],
           'states_rates': [str(x['eom']) for x in bvp.states()],
           'states_units': [str(x['unit']) for x in bvp.states()],
           'states_jac': [df_dy, df_dp],
           'quads': [str(x['symbol']) for x in bvp.quads()],
           'quads_rates': [str(x['eom']) for x in bvp.quads()], # TODO: Maybe multiply this by tf?
           'quads_units': [str(x['unit']) for x in bvp.quads()],
           'path_constraints': [],
           'path_constraints_units': [],
           'constants': [str(c['symbol']) for c in ocp.constants()],
           'constants_units': [str(c['unit']) for c in ocp.constants()],
           'constants_values': [float(c['value']) for c in ocp.constants()],
           'constants_of_motion': [str(c['function']) for c in ocp.constants_of_motion()],
           'dynamical_parameters': [str(c['symbol']) for c in bvp.parameters()],
           'dynamical_parameters_units': [str(c['unit']) for c in bvp.parameters()],
           'nondynamical_parameters': [str(c['symbol']) for c in bvp.nd_parameters()],
           'nondynamical_parameters_units': [str(c['unit']) for c in bvp.nd_parameters()],
           'control_list': [str(x['symbol']) for x in bvp.controls()],
           'controls': [str(u['symbol']) for u in bvp.controls()],
           'hamiltonian': str(bvp._properties['constants_of_motion'][0]['function']),
           'hamiltonian_units': str(bvp._properties['constants_of_motion'][0]['unit']),
           'num_states': len(bvp._properties['states']),
           'dHdu': [str(x) for x in dHdu],
           'bc_initial': [str(x['function']) for x in bvp.initial_bcs()],
           'bc_terminal': [str(x['function']) for x in bvp.terminal_bcs()],
           'bc_initial_jac': dbc_dya,
           'bc_terminal_jac': dbc_dyb,
           'bc_initial_parameter_jac': dbc_dp_a,
           'bc_terminal_parameter_jac': dbc_dp_b,
           'control_options': bvp._control_law,
           'num_controls': len(bvp.controls())}

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
            gamma = morphism(gamma, _compute_control=_compute_control)
        return gamma

    return out, guess_map, guess_map_inverse
