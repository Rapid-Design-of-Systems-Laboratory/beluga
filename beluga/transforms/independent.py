import numpy as np
import sympy

from beluga.data_classes.problem_components import combine_component_lists, NamedDimensionalStruct, DynamicStruct,\
    SymmetryStruct, sym_one
from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.trajectory import Trajectory
from beluga.transforms.trajectory_transformer import TrajectoryTransformer


class MomentumShiftTransformer(TrajectoryTransformer):
    """
    Class for applying a momentum shift (making the independent variable a state variable) to solutions
    """
    def transform(self, traj: Trajectory) -> Trajectory:
        if len(traj.dual_t) == 0:
            traj.dual_t = np.zeros_like(traj.t)

        traj.y = np.append(traj.y, traj.t[:, np.newaxis], axis=1)
        traj.dual = np.append(traj.dual, traj.dual_t[:, np.newaxis], axis=1)

        return traj

    def inv_transform(self, traj: Trajectory) -> Trajectory:
        traj.t = traj.y[:, -1]
        traj.y = np.delete(traj.y, -1, axis=1)

        traj.dual_t = traj.dual[:, -1]
        traj.dual = np.delete(traj.dual, -1, axis=1)

        return traj


def momentum_shift(prob: Problem):

    ind_var = prob.independent_variable
    new_state = DynamicStruct(
        ind_var.name, sympy.Integer(1), ind_var.units).sympify_self()
    prob.states.append(new_state)

    # TODO Reimplement custom names or ensure no collision
    new_ind_name = '_' + prob.independent_variable.name

    prob.independent_variable = NamedDimensionalStruct(new_ind_name, ind_var.units,)
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
                           remove=True))

    # Set trajectory mapper
    traj_mapper = MomentumShiftTransformer()

    return prob, traj_mapper


class NormalizeIndependentTransformer(TrajectoryTransformer):
    def __init__(self, delta_ind_idx=None):
        super(NormalizeIndependentTransformer, self).__init__()
        self.delta_ind_idx = delta_ind_idx

    def transform(self, traj: Trajectory) -> Trajectory:

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(traj.dynamical_parameters)[0]

        delta_t = traj.t[-1] - traj.t[0]
        traj.dynamical_parameters = np.insert(traj.dynamical_parameters, self.delta_ind_idx, delta_t)

        traj.t = (traj.t - traj.t[0]) / delta_t

        return traj

    def inv_transform(self, traj: Trajectory) -> Trajectory:
        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(traj.dynamical_parameters)[0] - 1

        traj.t = traj.t * traj.dynamical_parameters[self.delta_ind_idx]
        traj.dynamical_parameters = np.delete(traj.dynamical_parameters, self.delta_ind_idx)

        return traj


def normalize_independent(prob: Problem):
    delta_t_name = '_delta' + prob.independent_variable.name
    delta_t = NamedDimensionalStruct(delta_t_name, prob.independent_variable.units).sympify_self()
    prob.parameters.append(delta_t)

    _dynamic_structs = [prob.states, prob.costates]

    for state in combine_component_lists(_dynamic_structs):
        state.eom = state.eom * delta_t.sym

    prob.cost.path *= delta_t.sym

    prob.independent_variable = \
        NamedDimensionalStruct('_tau', sym_one).sympify_self()

    # Set trajectory mapper
    delta_ind_idx = len(prob.parameters) - 1
    traj_mapper = NormalizeIndependentTransformer(delta_ind_idx=delta_ind_idx)

    return prob, traj_mapper

