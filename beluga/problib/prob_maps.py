from .bvp_classes import SymBVP, default_tol
from .ocp_classes import SymOCP
from .dual_classes import SymDual
from beluga.optimlib import rash_mult, recursive_sub, epstrig_path, utm_path, total_derivative,\
    make_standard_symplectic_form, make_hamiltonian_vector_field, noether, make_control_law
import copy
import sympy
import logging


def scale_time(prob: (SymBVP, SymOCP), new_ind_name=None, in_place=False) -> (SymBVP, SymOCP):
    if not in_place:
        prob = copy.deepcopy(prob)

    delta_t_name = '_delta_' + prob.ind_var['name']
    delta_t_sym = sympy.Symbol(delta_t_name)
    prob.parameters.append({'name': delta_t_name, 'sym': sympy.Symbol(delta_t_name), 'units': prob.ind_var['units']})
    prob.add_symbolic_local(prob.parameters[-1]['name'], prob.parameters[-1]['sym'])

    for state in prob.states + prob.quads:
        state['eom'] *= delta_t_sym

    if hasattr(prob, 'cost'):
        prob.cost['path'] *= delta_t_sym

    if new_ind_name is None:
        new_ind_name = '_tau_scaled'
    prob.ind_var.update({'name': new_ind_name, 'sym': sympy.Symbol(new_ind_name), 'units': sympy.Integer(1)})
    prob.add_symbolic_local(prob.ind_var['name'], prob.ind_var['sym'])

    return prob


def momentum_shift(prob: (SymBVP, SymOCP), new_ind_name=None, in_place=False) -> (SymBVP, SymOCP):
    if not in_place:
        prob = copy.deepcopy(prob)

    ind_state = copy.copy(prob.ind_var)
    ind_state.update({'eom': sympy.Integer(1)})
    prob.states.append(ind_state)

    if new_ind_name is None:
        new_ind_name = '_tau_ms'
    prob.ind_var.update({'name': new_ind_name, 'sym': sympy.Symbol(new_ind_name)})
    prob.add_symbolic_local(prob.ind_var['name'], prob.ind_var['sym'])

    for symmetry in prob.symmetries:
        symmetry['field'].append(sympy.Integer(0))

    independent_symmetry = True
    for state in prob.states:
        if state['eom'].diff(ind_state['sym']):
            independent_symmetry = False

    if independent_symmetry:
        prob.symmetries.append({'field': [sympy.Integer(0)] * (len(prob.states) - 1) + [sympy.Integer(1)],
                               'units': ind_state['units'], 'remove': True})

    return prob


def rashs(prob: (SymBVP, SymOCP), in_place=False) -> (SymBVP, SymOCP):
    if not in_place:
        prob = copy.deepcopy(prob)

    # TODO: compose switches
    for switch in prob.switches:
        if isinstance(switch['function'], list):
            true_value = 0
            for func_i, cond_i in zip(switch['function'], switch['conditions']):
                temp_value = func_i
                for cond_ij in cond_i:
                    temp_value *= rash_mult(cond_ij, switch['tolerance'])
                true_value += temp_value
            switch['function'] = true_value

    """
    Make substitutions with the switches
    """

    sub_dict = {}
    for switch in prob.switches:
        sub_dict.update({switch['symbol']: switch['function']})

    # TODO: Seek more elegant replacement to recursive sub
    if hasattr(prob, 'cost'):
        prob.cost['initial'], _ = recursive_sub(prob.cost['initial'], sub_dict)
        prob.cost['path'], _ = recursive_sub(prob.cost['path'], sub_dict)
        prob.cost['terminal'], _ = recursive_sub(prob.cost['terminal'], sub_dict)

    for state in prob.states + prob.quads:
        state['eom'], _ = recursive_sub(state['eom'], sub_dict)

    return prob


def epstrig(prob: SymOCP, in_place=False) -> SymOCP:
    if not in_place:
        prob = copy.deepcopy(prob)

    constraint = prob.constraints['path'][0]

    if not constraint['method'].lower() == 'epstrig':
        raise RuntimeWarning('Constraint on {} not implemented using epstrig method\nReturning problem unchanged'
                             .format(constraint['expr']))

    control_syms = [control['sym'] for control in prob.controls]
    if constraint['expr'] in control_syms:
        control_idx = control_syms.index(constraint)
    else:
        raise NotImplementedError('Epsilon-Trig must be used with pure control-constraints.')

    activator_unit = None
    for constant in prob.constants:
        if constraint['activator'] == constant['sym']:
            activator_unit = constant['units']

    if activator_unit is None:
        raise Exception('Activator \'' + str(constraint['activator']) + '\' not found in constants.')

    if prob.cost['units'] * prob.ind_var['units'] != activator_unit:
        logging.warning('Dimension mismatch in path constraint \'' + str(constraint['expr']) + '\'')

    prob.cost['path'] += epstrig_path(
        constraint['expr'], constraint['lower'], constraint['upper'], constraint['activator'])

    sub_dict = dict(zip([constraint['expr']],
                        [(constraint['upper'] - constraint['lower']) / 2 * sympy.sin(constraint['expr'])
                         + (constraint['upper'] + constraint['lower']) / 2]))
    for state in prob.states:
        state['eom'] = state['eom'].subs(sub_dict, simultaneous=True)

    prob.constraints['path'].pop(0)

    return prob


def utm(prob: SymOCP, in_place=False) -> SymOCP:
    if not in_place:
        prob = copy.deepcopy(prob)

    constraint = prob.constraints['path'].pop(0)

    activator_unit = None
    for constant in prob.constants:
        if constraint['activator'] == constant['sym']:
            activator_unit = constant['units']

    if activator_unit is None:
        raise Exception('Activator \'' + str(constraint['activator']) + '\' not found in constants.')

    prob.cost['path'] += utm_path(constraint['expr'], constraint['lower'], constraint['upper'], constraint['activator'])

    return prob


def dualize(prob: SymOCP, method='indirect') -> SymDual:

    dual_prob = SymDual()
    dual_prob.load_from_ocp(prob)

    # TODO: Simplify this
    # Make lagrange multipliers and augment cost
    for idx, constraint in enumerate(dual_prob.constraints['initial']):
        nu_name = '_nu_0_{}'.format(idx)
        nu_sym = sympy.Symbol(nu_name)
        dual_prob.add_symbolic_local(nu_name, nu_sym)
        nu = {'name': nu_name, 'sym': nu_sym, 'units': dual_prob.cost['units']/constraint['units']}
        dual_prob.constraint_multipliers['initial'].append(nu)
        dual_prob.cost['initial'] += nu_sym*constraint['expr']

    for idx, constraint in enumerate(dual_prob.constraints['terminal']):
        nu_name = '_nu_f_{}'.format(idx)
        nu_sym = sympy.Symbol(nu_name)
        dual_prob.add_symbolic_local(nu_name, nu_sym)
        nu = {'name': nu_name, 'sym': nu_sym, 'units': dual_prob.cost['units']/constraint['units']}
        dual_prob.constraint_multipliers['terminal'].append(nu)
        dual_prob.cost['terminal'] += nu_sym * constraint['expr']

    # Make costates TODO Check if quads need costates
    dual_prob.hamiltonian.update({'expr': dual_prob.cost['path'], 'units': dual_prob.cost['units']})
    for state in dual_prob.states:
        lam_name = '_lam_{}'.format(state['name'])
        lam_sym = sympy.Symbol(lam_name)
        dual_prob.add_symbolic_local(lam_name, lam_sym)
        lam = {'name': lam_name, 'sym': lam_sym, 'eom': None,
               'units': dual_prob.cost['units']/state['units'], 'tol': dual_prob.cost['tol']/state['tol']}
        dual_prob.costates.append(lam)
        dual_prob.hamiltonian['expr'] += lam_sym * state['eom']

    dual_prob.constants_of_motion.append({'name': 'hamiltonian'}.update(dual_prob.hamiltonian))

    # Calc costate rates
    if method == 'indirect':
        for state, costate in zip(dual_prob.states, dual_prob.costates):
            costate['eom'] = -dual_prob.hamiltonian['expr'].diff(state['sym'])
    elif method == 'diffyg':
        state_syms = [state['sym'] for state in dual_prob.states]
        costate_syms = [costate['sym'] for costate in dual_prob.costates]
        omega = make_standard_symplectic_form(state_syms, costate_syms)
        x_h = make_hamiltonian_vector_field(
            dual_prob.hamiltonian['expr'], omega, state_syms + costate_syms, total_derivative)
        costate_rates = x_h[-len(dual_prob.states):]
        for costate, rate in zip(dual_prob.costates, costate_rates):
            costate['eom'] = rate
        dual_prob.omega = omega

        for idx, symmetry in enumerate(dual_prob.symmetries):
            g_star, units = noether(dual_prob, symmetry)
            dual_prob.constants_of_motion.append({'name': 'com_{}'.format(idx), 'expr': g_star, 'units': units})

    # Handle coparameters
    coparameters = []
    for parameter in dual_prob.parameters:
        mu_name = '_mu_{}'.format(parameter['name'])
        mu_sym = sympy.Symbol(mu_name)
        dual_prob.add_symbolic_local(mu_name, mu_sym)
        mu_eom = -dual_prob.hamiltonian['expr'].diff(parameter['sym'])
        mu = {'name': mu_name, 'sym': mu_sym, 'eom': mu_eom, 'units': dual_prob.cost['units']/parameter['units']}
        coparameters.append(mu)
        dual_prob.quads.append(mu)

    # Make costate constraints
    for state, costate in zip(dual_prob.states, dual_prob.costates):
        initial_constraint = costate['sym'] + dual_prob.cost['initial'].diff(state['sym'])
        dual_prob.constraints['initial'].append(
            {'expr': initial_constraint, 'units': costate['units'], 'tol': costate['tol']})

        terminal_constraint = costate['sym'] - dual_prob.cost['terminal'].diff(state['sym'])
        dual_prob.constraints['terminal'].append(
            {'expr': terminal_constraint, 'units': costate['units'], 'tol': costate['tol']})

    # Make time/Hamiltonian constraints
    dual_prob.constraints['initial'].append(
        {'expr': dual_prob.cost['initial'].diff(dual_prob.ind_var['sym']) - dual_prob.hamiltonian['expr'],
         'units': dual_prob.hamiltonian['units'], 'tol': dual_prob.cost['tol']/dual_prob.ind_var['tol']})
    dual_prob.constraints['terminal'].append(
        {'expr': dual_prob.cost['terminal'].diff(dual_prob.ind_var['sym']) + dual_prob.hamiltonian['expr'],
         'units': dual_prob.hamiltonian['units'], 'tol': dual_prob.cost['tol'] / dual_prob.ind_var['tol']})

    return dual_prob


def algebraic_control_law(prob: SymDual, in_place=False) -> SymDual:
    if not in_place:
        prob = copy.deepcopy(prob)

    control_syms = [control['sym'] for control in prob.controls]
    dh_du = [prob.hamiltonian['expr'].diff(control_sym) for control_sym in control_syms]
    logging.debug("Solving dH/du...")
    control_options = sympy.solve(dh_du, control_syms, minimal=True, simplify=True)
    logging.debug('Control found')

    for control in prob.controls:
        control.update({'options': []})
    for option in control_options:
        for control, option_k in zip(prob.controls, option):
            control['options'].append(option_k)

    return prob


def differential_control_law(prob: SymDual, in_place=False, method='indirect', bc_location='terminal') -> SymDual:
    if not in_place:
        prob = copy.deepcopy(prob)

    x = sympy.Matrix([state['sym'] for state in prob.states])
    u = sympy.Matrix([control['sym'] for control in prob.controls])
    f = sympy.Matrix([state['eom'] for state in prob.states])

    g = sympy.Matrix([prob.hamiltonian['expr'].diff(u_k) for u_k in u])

    dg_dx = g.jacobian(x)
    dg_du = g.jacobian(u)

    u_dot = dg_du.LUsolve(-dg_dx * f)  # dg_du * u_dot + dg_dx * x_dot = 0
    if sympy.zoo in u_dot.atoms():
        raise NotImplementedError('Complex infinity in ICRM control law. Potential bang-bang solution.')

    for g_k, control in zip(g, prob.controls):
        constraint = {'expr': g_k, 'units': prob.hamiltonian['units']/control['units'],
                      'tol': default_tol}
        prob.constraints[bc_location].append(constraint)

    if method == 'indirect':
        for control_rate in u_dot:
            control = prob.controls.pop(0)
            control.update({'eom': control_rate})
            prob.states.append(control)
    elif method == 'diffyg':
        pass

    return prob
