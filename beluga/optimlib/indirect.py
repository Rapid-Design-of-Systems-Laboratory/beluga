
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
    signature = []
    cat_chain = [ocp]
    gamma_map_chain = []
    gamma_map_inverse_chain = []

    analytical_jacobian = kwargs.get('analytical_jacobian', False)
    control_method = kwargs.get('control_method', 'pmp').lower()
    method = kwargs.get('method', 'indirect').lower()
    reduction = kwargs.get('reduction', False)

    """
    Make time a state.
    """
    ocp, gam, gam_inv = F_momentumshift(ocp)
    signature += ['F_momentumshift']
    cat_chain += [ocp]
    gamma_map_chain += [gam]
    gamma_map_inverse_chain += [gam_inv]

    """
    Deal with path constraints
    """
    while len(ocp.get_path_constraints()) > 0:
        if ocp.get_path_constraints()[0]['method'] is None:
            raise NotImplementedError

        elif ocp.get_path_constraints()[0]['method'].upper() == 'UTM':
            ocp, gam, gam_inv = F_UTM(ocp)
            signature += ['F_UTM']
            cat_chain += [ocp]
            gamma_map_chain += [gam]
            gamma_map_inverse_chain += [gam_inv]

        elif ocp.get_path_constraints()[0]['method'].upper() == 'EPSTRIG':
            ocp, gam, gam_inv = F_EPSTRIG(ocp)
            signature += ['F_EPSTRIG']
            cat_chain += [ocp]
            gamma_map_chain += [gam]
            gamma_map_inverse_chain += [gam_inv]

        else:
            raise NotImplementedError('Unknown path constraint method \"' + str(ocp.path_constraints()[0]['method'].upper()) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(ocp.get_switches()) > 0:
        ocp, gam, gam_inv = F_RASHS(ocp)
        signature += ['F_RASHS']
        cat_chain += [ocp]
        gamma_map_chain += [gam]
        gamma_map_inverse_chain += [gam_inv]

    """
    Dualize the problem.
    """
    bvp, gam, gam_inv = Dualize(ocp, method=method)
    signature += ['D_' + method]
    cat_chain += [bvp]
    gamma_map_chain += [gam]
    gamma_map_inverse_chain += [gam_inv]

    """
    Build a control law.
    """
    if control_method.upper() == 'PMP':
        bvp, gam, gam_inv = F_PMP(bvp)
        signature += ['F_PMP']
        cat_chain += [bvp]
        gamma_map_chain += [gam]
        gamma_map_inverse_chain += [gam_inv]

    elif control_method.upper() == 'ICRM':
        bvp, gam, gam_inv = F_ICRM(bvp, method=method)
        if method.lower() == 'diffyg':
            signature += ['F_SymplecticICRM']
        else:
            signature += ['F_ICRM']
        cat_chain += [bvp]
        gamma_map_chain += [gam]
        gamma_map_inverse_chain += [gam_inv]

    elif control_method.upper() == 'NUMERICAL':
        raise NotImplementedError
        dae_states = []
        dae_rates = []
        dae_units = []
        num_dae = 0
        control_law = []
    else:
        raise NotImplementedError('Unknown control method \"' + control_method + '\"')

    """
    Scale the EOMs to final time.
    """
    bvp, gam, gam_inv = F_scaletime(bvp)
    signature += ['F_scaletime']
    cat_chain += [bvp]
    gamma_map_chain += [gam]
    gamma_map_inverse_chain += [gam_inv]

    if is_symplectic(bvp.the_omega()) and reduction:
        while len(bvp.get_constants_of_motion()) > 1:
            bvp, gam, gam_inv = F_MF(bvp)
            signature += ['F_MF']
            cat_chain += [bvp]
            gamma_map_chain += [gam]
            gamma_map_inverse_chain += [gam_inv]
    elif not is_symplectic(bvp.the_omega()):
        logging.warning('BVP is not symplectic. Skipping reduction.')

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

    logging.debug('Problem formulation: Lambda := (' + ' . '.join(reversed(signature)) + ')(Sigma)')

    dHdu = make_dhdu(bvp._properties['constants_of_motion'][0]['function'], bvp.controls(), total_derivative)

    out = {'method': 'brysonho',
           'control_method': control_method,
           'consts': [str(k['symbol']) for k in ocp.get_constants()],
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
           'constants': [str(c['symbol']) for c in bvp.get_constants()],
           'constants_units': [str(c['unit']) for c in bvp.get_constants()],
           'constants_values': [float(c['value']) for c in bvp.get_constants()],
           'constants_of_motion': [str(c['function']) for c in bvp.get_constants_of_motion()],
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

    def guess_map(gamma, map_chain=gamma_map_chain):
        gamma = copy.deepcopy(gamma)
        for morphism in map_chain:
            gamma = morphism(gamma)
        return gamma

    def guess_map_inverse(gamma, map_chain=gamma_map_inverse_chain):
        gamma = copy.deepcopy(gamma)
        for morphism in reversed(map_chain):
            gamma = morphism(gamma)
        return gamma

    return out, guess_map, guess_map_inverse
