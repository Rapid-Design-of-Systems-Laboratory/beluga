import copy
from typing import Iterable, Union

import numpy as np
import sympy

from beluga.compilation import jit_compile_func
from beluga.data_classes.problem_components import extract_syms, combine_component_lists, DimensionalExpressionStruct,\
    DynamicStruct
from beluga.data_classes.symbolic_problem import Problem
from beluga.symbolic.differential_geometry import make_hamiltonian_vector_field, make_standard_symplectic_form
from beluga.data_classes.trajectory import Trajectory
from beluga.mappings.trajectory_mapper import TrajectoryMapper
from beluga.utils.logging import logger

sym_zero = sympy.Integer(0)
empty_array = np.array([])


class AlgebraicControlMapper(TrajectoryMapper):
    def __init__(self, prob: Problem):
        super(AlgebraicControlMapper, self).__init__()

        num_options = len(prob.control_law)

        _args = \
            [prob.independent_variable.sym, extract_syms(prob.states), extract_syms(prob.costates),
             extract_syms(prob.parameters), extract_syms(prob.constants)]

        _args_w_control = copy.copy(_args)
        _args_w_control.insert(3, extract_syms(prob.controls))

        # self.compute_u = compile_control(prob.control_law, _args, prob.hamiltonian.expr, lambdify_func=prob.lambdify)

        if num_options == 0:
            raise RuntimeError

        elif num_options == 1:
            compiled_option = prob.lambdify(_args, [*prob.control_law.values()])

            def calc_u(_t, _y, _lam, _p, _k):
                return np.array(compiled_option(_t, _y, _lam, _p, _k))

        else:
            compiled_options = prob.lambdify(_args, prob.control_law)
            ham_func = prob.lambdify(_args_w_control, prob.hamiltonian.expr)

            def calc_u(_t, _y, _lam, _p, _k):
                u_set = np.array(compiled_options(_t, _y, _lam, _p, _k))

                u = u_set[0, :]
                ham = ham_func(_t, _y, _lam, u, _p, _k)
                for n in range(1, num_options):
                    ham_i = ham_func(_t, _y, _lam, u_set[n, :], _p, _k)
                    if ham_i < ham:
                        u = u_set[n, :]

                return u

        self.compute_u = jit_compile_func(calc_u, _args, func_name='control_function')

    def map(self, traj: Trajectory) -> Trajectory:
        return traj

    def inv_map(self, traj: Trajectory) -> Trajectory:
        # TODO Vectorize
        traj.u = np.array([self.compute_u(_t, _y, _lam, traj.dynamical_parameters, traj.const) for _t, _y, _lam,
                           in zip(traj.t, traj.y, traj.dual)])
        return traj


def algebraic_control_law(prob: Problem):
    control_syms = extract_syms(prob.controls)
    prob.dh_du = [prob.hamiltonian.expr.diff(control_sym) for control_sym in control_syms]
    logger.debug("Solving dH/du...")
    control_options = sympy.solve(prob.dh_du, control_syms, minimal=True, simplify=False)
    logger.debug('Control found')

    # TODO Use algebraic equations and custom functions in future
    prob.control_law = control_options

    traj_mapper = AlgebraicControlMapper(prob)

    prob.prob_type = 'prob'

    return prob, traj_mapper


class DifferentialControlMapper(TrajectoryMapper):
    def __init__(self, control_idxs):
        super(DifferentialControlMapper, self).__init__()
        self.control_idxs = control_idxs

    def map(self, sol: Trajectory) -> Trajectory:
        idx_u_list = []
        for idx_u, (idx_y, u) in enumerate(sorted(zip(self.control_idxs, sol.u.T))):
            sol.y = np.insert(sol.y, idx_y, u, axis=1)
            idx_u_list.append(idx_u)
        sol.u = np.delete(sol.u, idx_u_list, axis=1)
        return sol

    def inv_map(self, sol: Trajectory) -> Trajectory:
        sol.u = sol.y[:, self.control_idxs]
        sol.y = np.delete(sol.y, self.control_idxs, axis=1)
        return sol


class DifferentialControlMapperDiffyG(TrajectoryMapper):
    def __init__(self, control_idxs):
        super(DifferentialControlMapperDiffyG, self).__init__()
        self.control_idxs = control_idxs

    def map(self, sol: Trajectory, control_costate: Union[float, np.ndarray] = 0.) -> Trajectory:
        idx_u_list = []

        for idx_u, (idx_y, u) in enumerate(sorted(zip(self.control_idxs, sol.u.T))):
            sol.y = np.insert(sol.y, idx_y, u, axis=1)

            if isinstance(control_costate, Iterable):
                if not isinstance(control_costate, np.ndarray):
                    control_costate = np.array(control_costate)
                costate_insert = control_costate[idx_u] * np.ones_like(sol.t)
            else:
                costate_insert = control_costate * np.ones_like(sol.t)

            sol.dual = np.insert(sol.dual, -1, costate_insert, axis=1)
            if len(sol.dual_u) == 0:
                sol.dual_u = np.array([costate_insert])
            else:
                sol.dual_u = np.insert(sol.dual_u, -1, costate_insert, axis=1)

            idx_u_list.append(idx_u)

        sol.u = np.delete(sol.u, idx_u_list, axis=1)
        return sol

    def inv_map(self, sol: Trajectory) -> Trajectory:
        sol.u = sol.y[:, self.control_idxs]
        sol.y = np.delete(sol.y, self.control_idxs, axis=1)
        sol.dual = np.delete(sol.dual, self.control_idxs, axis=1)
        return sol


def differential_control_law(prob: Problem, method='traditional'):
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
                g_k, prob.hamiltonian.units / control.units)
        prob.equality_constraints['terminal'].append(constraint)

    control_idxs = []
    if method == 'traditional':
        for control_rate in u_dot:
            control = prob.controls.pop(0)
            control_idxs.append(len(prob.states))
            prob.states.append(DynamicStruct(control.name, control_rate, control.units).sympify_self())

        traj_mapper = DifferentialControlMapper(control_idxs=control_idxs)

    elif method == 'diffyg':
        independent_index = len(prob.states) - 1
        control_costates = []
        for control, control_rate in zip(prob.controls, u_dot):
            control_idxs.append(len(prob.states))
            prob.states.append(DynamicStruct(control.name, control_rate, control.units).sympify_self())
            lam_name = '_lam_{}'.format(control.name)
            lam = DynamicStruct(lam_name, '0', prob.cost.units / control.units).sympify_self()
            prob.costates.append(lam)
            control_costates.append(lam)

        omega_new = make_standard_symplectic_form(prob.states, prob.costates)
        n_states = len(prob.states)
        n_controls = len(prob.controls)
        # Add (du - u' dt) ^ (dlamU - 0 dt) to omega
        for idx, u_dot_i in enumerate(u_dot):
            omega_new[int(n_states - n_controls + idx), int(2 * n_states - n_controls + idx)] = 1
            omega_new[int(2 * n_states - n_controls + idx), int(n_states - n_controls + idx)] = -1
            omega_new[independent_index, int(2 * n_states - n_controls + idx)] = -u_dot_i
            omega_new[int(2 * n_states - n_controls + idx), independent_index] = u_dot_i

        prob.omega = omega_new
        chi_h = make_hamiltonian_vector_field(prob.hamiltonian.expr, omega_new,
                                              extract_syms(prob.states + prob.costates))

        for idx, state in enumerate(prob.states + prob.costates):
            state.eom = chi_h[idx]

        for lam_u in control_costates:
            prob.equality_constraints['initial'].append(
                    DimensionalExpressionStruct(lam_u.sym, lam_u.units))

        prob.controls = []

        traj_mapper = DifferentialControlMapperDiffyG(control_idxs=control_idxs)

    else:
        raise NotImplementedError('Method {} not implemented for differential control'.format(method))

    prob.prob_type = 'prob'

    return prob, traj_mapper


def differential_control_law_traditional(prob: Problem):
    return differential_control_law(prob, method='traditional')


def differential_control_law_diffy_g(prob: Problem):
    return differential_control_law(prob, method='diffyg')
