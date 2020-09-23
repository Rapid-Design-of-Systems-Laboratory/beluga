import numpy as np
import sympy
import copy
import logging

from beluga.symbolic.data_classes.symbolic_problem import Problem
from beluga.symbolic.data_classes.components_structures import (extract_syms, combine_component_lists,
                                                                getattr_from_list, sym_one,
                                                                NamedDimensionalStruct, DynamicStruct,
                                                                DimensionalExpressionStruct,
                                                                NamedDimensionalExpressionStruct, SymmetryStruct)
from beluga.symbolic.differential_geometry import make_standard_symplectic_form, make_hamiltonian_vector_field, noether
from beluga.numeric.data_classes.trajectory_mappers import (MomentumShiftMapper, EpsTrigMapper, IdentityMapper, DualizeMapper,
                                                            AlgebraicControlMapper, DifferentialControlMapper,
                                                            SquashToBVPMapper, NormalizeTimeMapper)
from beluga.numeric.data_classes.NumericProblem import NumericProblem


"""
Functional Maps    
"""


def ensure_sympified(prob):
    if not prob.sympified:
        prob.sympify_self()


def ensure_dualized(prob):
    if not prob.dualized:
        dualize(prob)


def apply_quantities(prob: Problem):
    ensure_sympified(prob)

    # TODO Find a more elegant solution to this
    for quantity_i in prob.quantities:
        for quantity_j in prob.quantities:
            if quantity_i.sym in quantity_j.free_symbols:
                quantity_j.subs_self(quantity_i.sym, quantity_i.expr)

    for quantity in prob.quantities:
        prob.subs_all(quantity.sym, quantity.expr)

    # TODO add quantity calculation to Trajectory class


def momentum_shift(prob: Problem, new_ind_name=None):
    ensure_sympified(prob)

    ind_var = prob.independent_variable
    new_state = DynamicStruct(
        ind_var.name, sympy.Integer(1), ind_var.units, local_compiler=prob.local_compiler).sympify_self()
    prob.states.append(new_state)

    if new_ind_name is None:
        new_ind_name = '_' + prob.independent_variable.name

    prob.independent_variable = NamedDimensionalStruct(new_ind_name, ind_var.units,
                                                       local_compiler=prob.local_compiler)
    prob.independent_variable.sympify_self()

    for symmetry in prob.symmetries:
        symmetry.field = np.append(symmetry.field, sympy.Integer(0))

    independent_symmetry = True
    for state in prob.states:
        if state.eom.diff(new_state.sym) != 0:
            independent_symmetry = False

    if independent_symmetry:
        prob.symmetries.append(
            SymmetryStruct([sympy.Integer(0)] * (len(prob.states) - 1) + [sympy.Integer(1)], new_state.units,
                           remove=True, local_compiler=prob.local_compiler))

    # Set solution mapper
    ind_state_idx = len(prob.states) - 1
    prob.sol_map_chain.append(MomentumShiftMapper(ind_state_idx=ind_state_idx))

    return prob


def epstrig(prob: Problem):
    ensure_sympified(prob)

    for constraint_idx, _constraint in enumerate(prob.constraints['path']):
        if _constraint.method.lower() == 'epstrig':
            constraint = prob.constraints['path'].pop(constraint_idx)
            break
    else:
        raise RuntimeWarning('No path constraint using epstrig method found\nReturning problem unchanged')
        # return prob

    control_syms = [control.sym for control in prob.controls]
    if constraint.expr in control_syms:
        control_idx = control_syms.index(constraint.expr)
        new_control_name = '_' + str(constraint.expr) + '_trig'
        new_control = \
            NamedDimensionalStruct(new_control_name, '1', local_compiler=prob.local_compiler).sympify_self()
        prob.controls[control_idx] = new_control

    else:
        raise NotImplementedError('Epsilon-Trig must be used with pure control-constraints.')

    prob.cost.path += -constraint.activator * (sympy.cos(new_control.sym))

    prob.subs_all(constraint.expr, (constraint.upper - constraint.lower) / 2 * sympy.sin(new_control.sym)
                  + (constraint.upper + constraint.lower) / 2)

    # TODO Rewrite mapper
    prob.sol_map_chain.append(EpsTrigMapper(control_idx, constraint.lower, constraint.upper,
                                            prob.independent_variable.sym,
                                            np.array([state.sym for state in prob.states]),
                                            np.array([parameter.sym for parameter in prob.parameters]),
                                            np.array([constant.sym for constant in prob.constants]),
                                            local_compiler=prob.local_compiler))

    return prob


def utm(prob: Problem):
    ensure_sympified(prob)

    for constraint_idx, constraint in enumerate(prob.constraints['path']):
        if constraint.method.lower() == 'utm':
            break
    else:
        raise RuntimeWarning('No path constraint using utm method found\nReturning problem unchanged')
        # return prob

    activator_units = None
    for constant in prob.constants:
        if constraint.activator == constant.sym:
            activator_units = constant.units

    if activator_units is None:
        raise Exception('Activator \'' + str(constraint['activator']) + '\' not found in constants.')

    expr, activator, upper, lower = constraint.expr, constraint.activator, constraint.upper, constraint.lower
    prob.cost.path += activator * (1 / (sympy.cos(sympy.pi / 2 * (2 * expr - upper - lower) / (upper - lower))) - 1)

    prob.sol_map_chain.append(IdentityMapper())

    prob.constraints['path'].pop(constraint_idx)

    return prob


def rashs(prob: Problem):
    ensure_sympified(prob)

    for switch in prob.switches:
        prob.subs_all(switch.sym, switch.sym_func)

    return prob


def dualize(prob: Problem, method='traditional'):
    ensure_sympified(prob)

    ocp = copy.deepcopy(prob)

    for idx, constraint in enumerate(prob.constraints['initial']):
        nu_name = '_nu_0_{}'.format(idx)
        nu = NamedDimensionalStruct(
            nu_name, prob.cost.units / constraint.units, local_compiler=prob.local_compiler).sympify_self()
        prob.constraint_adjoints.append(nu)
        prob.cost.initial += nu.sym * constraint.expr

    for idx, constraint in enumerate(prob.constraints['terminal']):
        nu_name = '_nu_f_{}'.format(idx)
        nu = NamedDimensionalStruct(
            nu_name, prob.cost.units / constraint.units, local_compiler=prob.local_compiler).sympify_self()
        prob.constraint_adjoints.append(nu)
        prob.cost.terminal += nu.sym * constraint.expr

    # Make costates TODO Check if quads need costates
    prob.hamiltonian = \
        DimensionalExpressionStruct(prob.cost.path, prob.cost.units
                                    / prob.independent_variable.units).sympify_self()
    for state in prob.states:
        lam_name = '_lam_{}'.format(state.name)
        lam = DynamicStruct(lam_name, '0', prob.cost.units / state.units,
                            local_compiler=prob.local_compiler).sympify_self()
        prob.costates.append(lam)
        prob.hamiltonian.expr += lam.sym * state.eom

    # Handle coparameters
    for parameter in prob.parameters:
        lam_name = '_lam_{}'.format(parameter.name)
        prob.coparameters.append(DynamicStruct(lam_name, '0', prob.cost.units / parameter.units))

    prob.constants_of_motion.append(
        NamedDimensionalExpressionStruct('hamiltonian', prob.hamiltonian.expr, prob.hamiltonian.units,
                                         local_compiler=prob.local_compiler).sympify_self())

    if method.lower() == 'traditional':
        for state, costate in zip(prob.states + prob.parameters, prob.costates + prob.coparameters):
            costate.eom = -prob.hamiltonian.expr.diff(state.sym)
    elif method.lower() == 'diffyg':
        state_syms = extract_syms(prob.states + prob.parameters)
        costate_syms = extract_syms(prob.costates + prob.coparameters)
        omega = make_standard_symplectic_form(state_syms, costate_syms)
        x_h = make_hamiltonian_vector_field(prob.hamiltonian.expr, omega, state_syms + costate_syms, sympy.diff)
        costate_rates = x_h[-len(prob.states):]
        for costate, rate in zip(prob.costates, costate_rates):
            costate.eom = rate
        prob.omega = omega

        for idx, symmetry in enumerate(prob.symmetries):
            g_star, units = noether(prob, symmetry)
            prob.constants_of_motion.append(NamedDimensionalExpressionStruct('com_{}'.format(idx), g_star, units))

    # Make costate constraints
    for state, costate in zip(prob.states + prob.parameters, prob.costates + prob.coparameters):
        constraint_expr = costate.sym + prob.cost.initial.diff(state.sym)
        prob.constraints['initial'].append(
            DimensionalExpressionStruct(constraint_expr, costate.units, local_compiler=prob.local_compiler))

        constraint_expr = costate.sym - prob.cost.terminal.diff(state.sym)
        prob.constraints['terminal'].append(
            DimensionalExpressionStruct(constraint_expr, costate.units, local_compiler=prob.local_compiler))

    # TODO: Check Placement of Hamiltonian Constraint Placement
    # Make time/Hamiltonian constraints
    # constraint_expr = prob.cost.initial.diff(prob.independent_variable.sym) - prob.hamiltonian.expr
    # prob.constraints['initial'].append(DimensionalExpressionStruct(
    #         constraint_expr, prob.hamiltonian.units, local_compiler=prob.local_compiler))

    constraint_expr = prob.cost.terminal.diff(prob.independent_variable.sym) + prob.hamiltonian.expr
    prob.constraints['terminal'].append(DimensionalExpressionStruct(
        constraint_expr, prob.hamiltonian.units, local_compiler=prob.local_compiler))

    prob.sol_map_chain.append(DualizeMapper(len(prob.costates), len(prob.constraint_adjoints), ocp))

    prob.dualized = True

    return prob


def algebraic_control_law(prob: Problem):
    ensure_dualized(prob)

    control_syms = extract_syms(prob.controls)
    prob.dh_du = [prob.hamiltonian.expr.diff(control_sym) for control_sym in control_syms]
    logging.debug("Solving dH/du...")
    control_options = sympy.solve(prob.dh_du, control_syms, minimal=True, simplify=True)
    logging.debug('Control found')

    # TODO Use algebraic equations and custom functions in future
    prob.control_law = control_options

    prob.sol_map_chain.append(AlgebraicControlMapper(prob))

    prob.prob_type = 'bvp'

    return prob


def differential_control_law(prob: Problem, method='traditional'):
    ensure_dualized(prob)

    _dynamic_structs = [prob.states, prob.costates]

    state_syms = sympy.Matrix(extract_syms(combine_component_lists(_dynamic_structs)))
    control_syms = sympy.Matrix(extract_syms(prob.controls))
    eom = sympy.Matrix([state.eom for state in combine_component_lists(_dynamic_structs)])

    g = sympy.Matrix([prob.hamiltonian.expr.diff(u_k) for u_k in control_syms])

    dg_dx = g.jacobian(state_syms)
    dg_du = g.jacobian(control_syms)

    u_dot = dg_du.LUsolve(-dg_dx * eom)  # dg_du * u_dot + dg_dx * x_dot = 0
    if sympy.zoo in u_dot.atoms():
        raise NotImplementedError('Complex infinity in differential control law. Potential bang-bang solution.')

    for g_k, control in zip(g, prob.controls):
        constraint = DimensionalExpressionStruct(
            g_k, prob.hamiltonian.units / control.units, local_compiler=prob.local_compiler)
        prob.constraints['terminal'].append(constraint)

    control_idxs = []
    if method == 'traditional':
        for control_rate in u_dot:
            control = prob.controls.pop(0)
            control_idxs.append(len(prob.states))
            prob.states.append(DynamicStruct(control.name, control_rate, control.units,
                                             local_compiler=prob.local_compiler).sympify_self())
    elif method == 'diffyg':
        # TODO: Finsih this when you know what's up
        raise NotImplementedError('Need to reimplement diffyg')
    else:
        raise NotImplementedError('Method {} not implemented for differential control'.format(method))

    prob.sol_map_chain.append(DifferentialControlMapper(control_idxs=control_idxs))

    prob.prob_type = 'bvp'

    return prob


def mf(prob: Problem, com_index=0):
    constant_of_motion = prob.constants_of_motion[com_index]

    state_syms = getattr_from_list(prob.states, 'sym')
    parameter_syms = getattr_from_list(prob.parameters, 'sym')
    constant_syms = getattr_from_list(prob.constants, 'sym')




def squash_to_bvp(prob: Problem):
    costate_idxs = slice(len(prob.states), len(prob.states) + len(prob.costates))
    prob.states += prob.costates
    prob.costates = []

    coparameter_idxs = slice(len(prob.quads), len(prob.quads) + len(prob.coparameters))
    prob.quads += prob.coparameters
    prob.coparameters = []

    prob.constraint_parameters += prob.constraint_adjoints
    constraint_adjoints_idxs = \
        slice(len(prob.constraint_parameters),
              len(prob.constraint_parameters) + len(prob.constraint_adjoints))
    prob.constraint_adjoints = []

    prob.sol_map_chain.append(SquashToBVPMapper(costate_idxs, coparameter_idxs, constraint_adjoints_idxs))

    prob.dualized = False

    return prob


def normalize_time(prob: Problem, new_ind_name=None):
    ensure_sympified(prob)

    delta_t_name = '_delta' + prob.independent_variable.name
    delta_t = NamedDimensionalStruct(delta_t_name, prob.independent_variable.units,
                                     local_compiler=prob.local_compiler).sympify_self()
    prob.parameters.append(delta_t)

    _dynamic_structs = [prob.states, prob.costates]

    for state in combine_component_lists(_dynamic_structs):
        state.eom = state.eom * delta_t.sym

    prob.cost.path *= delta_t.sym

    if new_ind_name is None:
        new_ind_name = '_tau'
    prob.independent_variable = \
        NamedDimensionalStruct(new_ind_name, sym_one, local_compiler=prob.local_compiler).sympify_self()

    # Set solution mapper
    delta_t_idx = len(prob.parameters) - 1
    prob.sol_map_chain.append(NormalizeTimeMapper(delta_ind_idx=delta_t_idx))

    return prob


def ignore_quads(prob: Problem):
    prob.states += prob.quads
    prob.quads = []

    return prob


def compute_analytical_jacobians(prob: Problem):

    states = sympy.Matrix(extract_syms(prob.states))
    dynamic_parameters = sympy.Matrix(extract_syms(prob.parameters))
    parameters = sympy.Matrix(extract_syms(prob.parameters) + extract_syms(prob.constraint_parameters))
    quads = sympy.Matrix(extract_syms(prob.quads))
    eom = sympy.Matrix(getattr_from_list(prob.states, 'eom'))
    phi_0 = sympy.Matrix(getattr_from_list(prob.constraints['initial'], 'expr'))
    phi_f = sympy.Matrix(getattr_from_list(prob.constraints['terminal'], 'expr'))

    prob.func_jac['df_dy'] = eom.jacobian(states)
    prob.bc_jac['initial']['dbc_dy'] = phi_0.jacobian(states)
    prob.bc_jac['terminal']['dbc_dy'] = phi_f.jacobian(states)

    if len(parameters) > 0:
        prob.func_jac.update({'df_dp': eom.jacobian(dynamic_parameters)})
        prob.bc_jac['initial']['dbc_dp'] = phi_0.jacobian(parameters)
        prob.bc_jac['terminal']['dbc_dp'] = phi_f.jacobian(parameters)

    if len(quads) > 0:
        prob.bc_jac['initial']['dbc_dq'] = phi_0.jacobian(quads)
        prob.bc_jac['terminal']['dbc_dq'] = phi_f.jacobian(quads)

    return prob


def compile_direct(prob: Problem, analytical_jacobian=True, reduction=False,
                   do_momentum_shift=False, do_normalize_time=False):
    ensure_sympified(prob)

    """
    Substitute Quantities
    """
    apply_quantities(prob)

    """
    Make time a state.
    """
    if do_momentum_shift:
        momentum_shift(prob)

    """
    Deal with path constraints
    """
    for path_constraint in copy.copy(prob.constraints['path']):
        if path_constraint.method.lower() == 'epstrig':
            epstrig(prob)
        elif path_constraint.method.lower() == 'utm':
            utm(prob)
        else:
            raise NotImplementedError('Unknown path constraint method \"' + str(path_constraint.method) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(prob.switches) > 0:
        rashs(prob)

    """
    Scale eom to final time
    """
    if do_normalize_time:
        normalize_time(prob)

    """
    Reduce if needed
    """
    # TODO Implement MF
    if reduction:
        pass

    """
    Ignore quads (until the bvp solver gets better)
    """
    ignore_quads(prob)

    """
    Form analytical jacobians
    """
    if analytical_jacobian:
        compute_analytical_jacobians(prob)

    compile_problem(prob)


def compile_indirect(prob: Problem, analytical_jacobian=True, control_method='differential', method='traditional',
                     reduction=False, do_momentum_shift=True, do_normalize_time=True):

    ensure_sympified(prob)

    """
    Substitute Quantities
    """
    apply_quantities(prob)

    """
    Make time a state.
    """
    if do_momentum_shift:
        momentum_shift(prob)

    """
    Deal with path constraints
    """
    for path_constraint in copy.copy(prob.constraints['path']):
        if path_constraint.method.lower() == 'epstrig':
            epstrig(prob)
        elif path_constraint.method.lower() == 'utm':
            utm(prob)
        else:
            raise NotImplementedError(
                'Unknown path constraint method \"' + str(path_constraint.method) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(prob.switches) > 0:
        rashs(prob)

    """
    Dualize Problem
    """
    dualize(prob, method=method)

    """
    Form Control Law
    """
    if control_method.lower() == 'algebraic':
        algebraic_control_law(prob)
    elif control_method.lower() == 'differential':
        differential_control_law(prob, method=method)
    elif control_method.lower() == 'numeric':
        raise NotImplementedError('Numerical control method not yet implemented')
    else:
        raise NotImplementedError('{} control method not implemented. Try differential or algebraic')

    """
    Scale eom to final time
    """
    if do_normalize_time:
        normalize_time(prob)

    """
    Reduce if needed
    """
    # TODO Implement MF
    if reduction:
        pass

    """
    Ignore quads (until the bvp solver gets better)
    """
    ignore_quads(prob)

    """
    Squash dual problem to normal BVP
    """
    squash_to_bvp(prob)

    """
    Form analytical jacobians
    """
    if analytical_jacobian:
        if control_method == 'algebraic':
            logging.info('Analytical Jacobians not available for algebraic control mode')
        else:
            compute_analytical_jacobians(prob)

    compile_problem(prob)

    return prob


def compile_problem(prob: Problem, use_control_arg=False):
    ensure_sympified(prob)

    prob.functional_problem = NumericProblem(prob, local_compiler=prob.local_compiler)

    prob.functional_problem.compile_problem(use_control_arg=use_control_arg)
    prob.lambdified = True

    return prob
