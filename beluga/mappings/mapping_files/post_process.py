import numpy as np
import sympy

from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.problem_components import getattr_from_list, extract_syms
from beluga.data_classes.trajectory import Trajectory
from beluga.mappings.trajectory_mapper import TrajectoryMapper


class SquashToBVPMapper(TrajectoryMapper):
    def __init__(self, costate_idxs, coparameter_idxs, constraint_adjoints_idxs):
        super(SquashToBVPMapper, self).__init__()

        self.costate_idxs = costate_idxs
        self.coparameter_idxs = coparameter_idxs
        self.constraint_adjoints_idxs = constraint_adjoints_idxs

    def map(self, traj: Trajectory) -> Trajectory:
        if len(traj.dual) > 0:
            traj.y = np.concatenate((traj.y, traj.dual), axis=1)

        return traj

    def inv_map(self, traj: Trajectory) -> Trajectory:
        traj.dual = traj.y[:, self.costate_idxs]
        traj.y = np.delete(traj.y, self.costate_idxs, axis=1)
        traj.nondynamical_parameters = np.delete(traj.nondynamical_parameters, self.constraint_adjoints_idxs)

        return traj


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

    prob.dualized = False

    traj_mapper = SquashToBVPMapper(costate_idxs, coparameter_idxs, constraint_adjoints_idxs)

    return prob, traj_mapper


def ignore_quads(prob: Problem):
    prob.states += prob.quads
    prob.quads = []

    return prob, None


def compute_analytical_jacobians(prob: Problem):
    states = sympy.Matrix(extract_syms(prob.states))
    dynamic_parameters = sympy.Matrix(extract_syms(prob.parameters))
    parameters = sympy.Matrix(extract_syms(prob.parameters) + extract_syms(prob.constraint_parameters))
    quads = sympy.Matrix(extract_syms(prob.quads))
    eom = sympy.Matrix(getattr_from_list(prob.states, 'eom'))
    phi_0 = sympy.Matrix(getattr_from_list(prob.equality_constraints['initial'], 'expr'))
    phi_f = sympy.Matrix(getattr_from_list(prob.equality_constraints['terminal'], 'expr'))

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

    return prob, None
