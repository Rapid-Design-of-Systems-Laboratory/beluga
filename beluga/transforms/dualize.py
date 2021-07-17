import copy

import numpy as np
import sympy

from beluga.compilation.compilation_functions import compile_cost
from beluga.data_classes.problem_components import NamedDimensionalStruct, DimensionalExpressionStruct, DynamicStruct, \
    NamedDimensionalExpressionStruct, extract_syms
from beluga.data_classes.symbolic_problem import SymbolicProblem
from beluga.data_classes.trajectory import Trajectory
from beluga.symbolic.differential_geometry import make_standard_symplectic_form, make_hamiltonian_vector_field, noether
from beluga.transforms.trajectory_transformer import TrajectoryTransformer

sym_zero = sympy.Integer(0)
empty_array = np.array([])


class DualizeTransformer(TrajectoryTransformer):
    def __init__(self, ocp, num_costates, num_adjoints):
        super(DualizeTransformer, self).__init__()
        self.num_costates = num_costates
        self.num_adjoints = num_adjoints

        self.default_costate_values = -np.ones(num_costates)
        self.default_adjoint_values = np.ones(num_adjoints)

        _state_syms = extract_syms(ocp.states)
        _control_syms = extract_syms(ocp.controls)
        _parameter_syms = extract_syms(ocp.parameters)
        _constant_syms = extract_syms(ocp.constants)
        _quad_syms = extract_syms(ocp.quads)
        # _constraint_parameters_syms = extract_syms(ocp.constraint_parameters)

        _dynamic_args = [_state_syms, _control_syms, _parameter_syms, _constant_syms]
        _bc_args = [_state_syms, _quad_syms, _parameter_syms, _constant_syms]

        self.compute_cost = compile_cost(ocp.cost, _dynamic_args, _bc_args, ocp.lambdify)

    def transform(self, traj: Trajectory, lam=None, nu=None) -> Trajectory:
        if len(traj.lam) == 0:
            traj.lam = self.default_costate_values

        if len(traj.nu) == 0:
            traj.nu = self.default_adjoint_values

        return traj

    def inv_transform(self, traj: Trajectory, retain_dual=True) -> Trajectory:
        if not retain_dual:
            traj.lam = empty_array
            traj.nu = empty_array

        traj.cost = self.compute_cost(traj.t, traj.y, traj.q, traj.u, traj.p, traj.k)

        return traj


def dualize(prob: SymbolicProblem, method='traditional'):
    # TODO Maybe pull is apart a little more (or not)

    ocp = copy.deepcopy(prob)

    for idx, constraint in enumerate(prob.equality_constraints['initial']):
        nu_name = '_nu_0_{}'.format(idx)
        nu = NamedDimensionalStruct(
                nu_name, prob.cost.units / constraint.units).sympify_self()
        prob.constraint_adjoints.append(nu)
        prob.cost.initial += nu.sym * constraint.expr

    for idx, constraint in enumerate(prob.equality_constraints['terminal']):
        nu_name = '_nu_f_{}'.format(idx)
        nu = NamedDimensionalStruct(
                nu_name, prob.cost.units / constraint.units).sympify_self()
        prob.constraint_adjoints.append(nu)
        prob.cost.terminal += nu.sym * constraint.expr

    # Make costates TODO Check if quads need costates
    prob.hamiltonian = \
        DimensionalExpressionStruct(prob.cost.path, prob.cost.units
                                    / prob.independent_variable.units).sympify_self()
    for state in prob.states:
        lam_name = '_lam_{}'.format(state.name)
        lam = DynamicStruct(lam_name, '0', prob.cost.units / state.units).sympify_self()
        prob.costates.append(lam)
        prob.hamiltonian.expr += lam.sym * state.eom

    symmetry_costate_addition = np.array([sym_zero for _ in prob.costates])
    for idx, symmetry in enumerate(prob.symmetries):
        symmetry.field = np.concatenate((symmetry.field, symmetry_costate_addition))

    # Handle coparameters
    for parameter in prob.parameters:
        lam_name = '_lam_{}'.format(parameter.name)
        prob.coparameters.append(DynamicStruct(lam_name, '0', prob.cost.units / parameter.units))

    prob.constants_of_motion.append(
            NamedDimensionalExpressionStruct('hamiltonian', prob.hamiltonian.expr,
                                             prob.hamiltonian.units).sympify_self())

    if method.lower() == 'traditional':
        for state, costate in zip(prob.states + prob.parameters, prob.costates + prob.coparameters):
            costate.eom = -prob.hamiltonian.expr.diff(state.sym)

    elif method.lower() == 'diffyg':
        state_syms = extract_syms(prob.states + prob.parameters)
        costate_syms = extract_syms(prob.costates + prob.coparameters)
        omega = make_standard_symplectic_form(state_syms, costate_syms)
        chi_h = make_hamiltonian_vector_field(prob.hamiltonian.expr, omega, state_syms + costate_syms)
        costate_rates = chi_h[-len(prob.states):]
        for costate, rate in zip(prob.costates, costate_rates):
            costate.eom = rate
        prob.omega = omega

        for idx, symmetry in enumerate(prob.symmetries):
            g_star, units = noether(prob, symmetry)
            prob.constants_of_motion.append(NamedDimensionalExpressionStruct('com_{}'.format(idx), g_star, units))

    # Make costate constraints
    for state, costate in zip(prob.states + prob.parameters, prob.costates + prob.coparameters):
        constraint_expr = costate.sym + prob.cost.initial.diff(state.sym)
        prob.equality_constraints['initial'].append(
                DimensionalExpressionStruct(constraint_expr, costate.units))

        constraint_expr = costate.sym - prob.cost.terminal.diff(state.sym)
        prob.equality_constraints['terminal'].append(
                DimensionalExpressionStruct(constraint_expr, costate.units))

    # TODO: Check Placement of Hamiltonian Constraint Placement
    # Make time/Hamiltonian constraints
    # constraint_expr = prob.cost.initial.diff(prob.independent_variable.sym) - prob.hamiltonian.expr
    # prob.equality_constraints['initial'].append(DimensionalExpressionStruct(
    #         constraint_expr, prob.hamiltonian.units))

    constraint_expr = prob.cost.terminal.diff(prob.independent_variable.sym) + prob.hamiltonian.expr
    prob.equality_constraints['terminal'].append(DimensionalExpressionStruct(
            constraint_expr, prob.hamiltonian.units))

    prob.dualized = True
    prob.prob_type = 'prob'

    traj_mapper = DualizeTransformer(ocp, len(prob.costates), len(prob.constraint_adjoints))

    return prob, traj_mapper


def dualize_traditional(prob: SymbolicProblem):
    return dualize(prob, method='traditional')


def dualize_diffyg(prob: SymbolicProblem):
    return dualize(prob, method='diffyg')
