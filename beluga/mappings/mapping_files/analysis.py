import copy

import numpy as np
import sympy

from beluga.compilation.compiler import lambdify
from beluga.data_classes.problem_components import extract_syms, combine_component_lists
from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.trajectory import Trajectory
from beluga.mappings.trajectory_mapper import TrajectoryMapper

sym_zero = sympy.Integer(0)
empty_array = np.array([])


class HamiltonianSensitivityCalculator(TrajectoryMapper):
    def __init__(self, prob: Problem, dh_dux, dh_duu):
        super(HamiltonianSensitivityCalculator, self).__init__()

        _args = \
            [prob.independent_variable.sym, extract_syms(prob.states), extract_syms(prob.controls),
             extract_syms(prob.costates), extract_syms(prob.parameters), extract_syms(prob.constants)]

        self.dh_dux_func = lambdify(_args, dh_dux)
        self.dh_duu_func = lambdify(_args, dh_duu)

    map = None

    def inv_map(self, traj: Trajectory) -> Trajectory:
        # TODO Vectorize
        traj.u = np.array([self.dh_dux_func(_t, _y, _lam, traj.dynamical_parameters, traj.const) for _t, _y, _u, _lam,
                           in zip(traj.t, traj.y, traj.u, traj.dual)])
        return traj


def hamiltonian_sensitivity_handler(prob: Problem):
    _dynamic_structs = [prob.states, prob.costates]

    state_syms = sympy.Matrix(extract_syms(combine_component_lists(_dynamic_structs)))
    control_syms = sympy.Matrix(extract_syms(prob.controls))

    ham_u = sympy.Matrix([prob.hamiltonian.expr.diff(u_k) for u_k in control_syms])

    ham_ux = ham_u.jacobian(state_syms)
    ham_uu = ham_u.jacobian(control_syms)

    prob.aux['H_ux'] = ham_ux
    prob.aux['H_uu'] = ham_uu

    traj_mapper = None

    return prob, traj_mapper
