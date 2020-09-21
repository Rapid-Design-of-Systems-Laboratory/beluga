import numpy as np
from abc import ABC
import copy
import sympy

from beluga.numeric.compilation import jit_compile_func, LocalCompiler
from beluga.numeric.compilation.component_compilation import compile_control, compile_cost
from beluga.numeric.ivp_solvers import Trajectory as Solution
from beluga.symbolic.data_classes.symbolic_problem import Problem
from beluga.symbolic.data_classes.components_structures import extract_syms


empty_array = np.array([])


class SolMapper(ABC):
    def map(self, sol: Solution) -> Solution:
        pass

    def inv_map(self, sol: Solution) -> Solution:
        pass


class IdentityMapper(SolMapper):
    def map(self, sol: Solution) -> Solution:
        return sol

    def inv_map(self, sol: Solution) -> Solution:
        return sol


class MomentumShiftMapper(SolMapper):
    def __init__(self, ind_state_idx=None):
        self.ind_state_idx = ind_state_idx

    def map(self, sol: Solution) -> Solution:
        if self.ind_state_idx is None:
            self.ind_state_idx = np.shape(sol.y)[1]

        if len(sol.dual_t) == 0:
            sol.dual_t = np.zeros_like(sol.t)

        sol.y = np.insert(sol.y, self.ind_state_idx, sol.t, axis=1)
        sol.dual = np.insert(sol.dual, self.ind_state_idx, sol.dual_t, axis=1)

        return sol

    def inv_map(self, sol: Solution) -> Solution:
        if self.ind_state_idx is None:
            self.ind_state_idx = np.shape(sol.y)[1] - 1

        sol.t = sol.y[:, self.ind_state_idx]
        np.delete(sol.y, self.ind_state_idx, axis=1)

        sol.dual_t = sol.dual[:, self.ind_state_idx]
        np.delete(sol.dual, self.ind_state_idx, axis=1)

        return sol


class EpsTrigMapper(SolMapper):
    def __init__(self, control_idx, lower_expr: sympy.Expr, upper_expr: sympy.Expr,
                 ind_var_sym, state_syms, parameter_syms, constant_syms,
                 local_compiler: LocalCompiler = None):

        self.control_idx = control_idx

        self.lower_expr = lower_expr
        self.upper_expr = upper_expr

        self.args = [ind_var_sym, state_syms, parameter_syms, constant_syms]

        if local_compiler is None:
            self.local_compiler = LocalCompiler()
        else:
            self.local_compiler = local_compiler

        self.map_func = None
        self.inv_map_func = None

    def map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.map_func is None:
            u = sympy.Symbol('_u')

            u_min = self.lower_expr
            u_max = self.upper_expr

            u_range = u_max - u_min
            u_offset = (u_max + u_min)/2

            u_trig_expr = sympy.asin((u - u_offset)/u_range)

            self.map_func = self.local_compiler.lambdify([u] + self.args, u_trig_expr)

        for idx, t_i, y_i, p_i in enumerate(zip(sol.t, sol.y, sol.dynamical_parameters)):
            sol.u[idx, self.control_idx] = self.map_func(sol.u[idx, self.control_idx], t_i, y_i, p_i, sol.const)

        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.inv_map_func is None:
            u_trig = sympy.Symbol('_u_trig')

            u_min = self.lower_expr
            u_max = self.upper_expr

            u_range = u_max - u_min
            u_offset = (u_max + u_min) / 2

            u_expr = u_range*sympy.sin(u_trig) + u_offset

            self.inv_map_func = self.local_compiler.lambdify([u_trig] + self.args, u_expr)

        for idx, t_i, y_i, p_i in enumerate(zip(sol.t, sol.y, sol.dynamical_parameters)):
            sol.u[idx, self.control_idx] = self.inv_map_func(sol.u[idx, self.control_idx], t_i, y_i, p_i, sol.const)

        return sol


class DualizeMapper(SolMapper):
    def __init__(self, dual_len, nu_len, ocp: Problem):
        self.dual_len = dual_len
        self.nu_len = nu_len

        _state_syms = extract_syms(ocp.states)
        _control_syms = extract_syms(ocp.controls)
        _parameter_syms = extract_syms(ocp.parameters)
        _constant_syms = extract_syms(ocp.constants)
        _quad_syms = extract_syms(ocp.quads)
        _constraint_parameters_syms = extract_syms(ocp.constraint_parameters)

        _dynamic_args = [_state_syms, _control_syms, _parameter_syms, _constant_syms]
        _bc_args = [_state_syms, _quad_syms, _parameter_syms, _constant_syms]

        self.compute_cost = compile_cost(ocp.cost, _dynamic_args, _bc_args, ocp.lambdify)

    def map(self, sol: Solution, lam=empty_array, nu=empty_array) -> Solution:

        # sol.dual = lam
        if len(sol.nondynamical_parameters) == 0:
            sol.nondynamical_parameters = np.ones(self.nu_len)

        return sol

    def inv_map(self, sol: Solution, retain_dual=True) -> Solution:

        if not retain_dual:
            sol.dual = empty_array
            sol.nondynamical_parameters = empty_array

        sol.cost = self.compute_cost(
            sol.t, sol.y, sol.q, sol.u, sol.dynamical_parameters, sol.const)

        return sol


class NormalizeTimeMapper(SolMapper):
    def __init__(self, delta_ind_idx=None):
        self.delta_ind_idx = delta_ind_idx

    def map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(sol.dynamical_parameters)[0]

        delta_t = sol.t[-1] - sol.t[0]
        sol.dynamical_parameters = np.insert(sol.dynamical_parameters, self.delta_ind_idx, delta_t)

        sol.t = (sol.t - sol.t[0])/delta_t

        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(sol.dynamical_parameters)[0] - 1

        sol.t = sol.t * sol.dynamical_parameters[self.delta_ind_idx]
        sol.dynamical_parameters = np.delete(sol.dynamical_parameters, self.delta_ind_idx)

        return sol


class AlgebraicControlMapper(SolMapper):
    def __init__(self, prob: Problem):

        num_options = len(prob.control_law)

        _args = \
            [prob.independent_variable.sym, extract_syms(prob.states), extract_syms(prob.costates),
             extract_syms(prob.parameters), extract_syms(prob.constants)]

        _args_w_control = copy.copy(_args)
        _args_w_control.insert(3, extract_syms(prob.controls))

        self.compute_u = compile_control(prob.control_law, _args, prob.hamiltonian.expr, lambdify_func=prob.lambdify)

        if num_options == 0:
            raise RuntimeError

        elif num_options == 1:
            compiled_option = prob.lambdify(_args, prob.control_law[0])

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

    def map(self, sol: Solution) -> Solution:
        sol.u = empty_array
        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol.u = np.array([self.compute_u(_t, _y, _lam, sol.dynamical_parameters, sol.const) for _t, _y, _lam,
                          in zip(sol.t, sol.y, sol.dual)])
        return sol


class DifferentialControlMapper(SolMapper):
    def __init__(self, control_idxs):
        self.control_idxs = control_idxs

    def map(self, sol: Solution) -> Solution:
        idx_u_list = []
        for idx_u, (idx_y, u) in enumerate(sorted(zip(self.control_idxs, sol.u.T))):
            sol.y = np.insert(sol.y, idx_y, u, axis=1)
            idx_u_list.append(idx_u)
        sol.u = np.delete(sol.u, idx_u_list, axis=1)
        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol.u = sol.y[:, self.control_idxs]
        sol.y = np.delete(sol.y, self.control_idxs, axis=1)
        return sol


class MF(SolMapper):
    def __init__(self):
        pass


class SquashToBVPMapper(SolMapper):
    def __init__(self, costate_idxs, coparameter_idxs, constraint_adjoints_idxs):
        self.costate_idxs = costate_idxs
        self.coparameter_idxs = coparameter_idxs
        self.constraint_adjoints_idxs = constraint_adjoints_idxs

    def map(self, sol: Solution) -> Solution:

        if len(sol.dual) > 0:
            sol.y = np.concatenate((sol.y, sol.dual), axis=1)

        sol.dual = empty_array
        sol.dual_t = empty_array
        sol.dual_u = empty_array

        return sol

    def inv_map(self, sol: Solution) -> Solution:

        sol.dual = sol.y[:, self.costate_idxs]
        sol.y = np.delete(sol.y, self.costate_idxs, axis=1)
        sol.nondynamical_parameters = np.delete(sol.nondynamical_parameters, self.constraint_adjoints_idxs)

        return sol
