import numpy as np
from abc import ABC
import copy
import sympy
from typing import Iterable
# from beluga import LocalCompiler
from ..codegen import jit_compile_func, LocalCompiler


empty_array = np.array([])


class Solution:
    def __init__(self, t=np.array([]), y=np.array([[]]), u=np.array([[]]), p=np.array([]), p_con=np.array([]),
                 k=np.array([]), q=empty_array, lam=empty_array, nu=np.array([]), mu=np.array([[]])):

        self.t = t          # indepedent
        self.y = y          # states
        self.u = u          # controls
        self.p = p          # parameters
        self.p_con = p_con  # constraint parameters
        self.k = k          # constants
        self.q = q          # quads
        self.lam = lam      # costate
        self.nu = nu        # constraint lagrange multipliers
        self.mu = mu        # coparameters


class SolSet:
    def __init__(self):
        self.solutions = [[]]

    def add_continuation_set(self, cont_set=None):
        if cont_set is None:
            cont_set = []
        elif not isinstance(cont_set, Iterable):
            cont_set = [cont_set]
        elif not isinstance(cont_set, list):
            cont_set = list(cont_set)

        self.solutions.append(cont_set)

    def add_solution(self, sol):
        self.solutions[-1].append(sol)

    def apply_to_all(self, mapping):
        self.solutions = [mapping(sol) for sol in self.solutions]
        return self


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
        sol = copy.deepcopy(sol)

        if self.ind_state_idx is None:
            self.ind_state_idx = np.shape(sol.y)[1]

        sol.y = np.insert(sol.y, self.ind_state_idx, sol.t, axis=0)

        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.ind_state_idx is None:
            self.ind_state_idx = np.shape(sol.y)[1] - 1

        sol.t = sol.y[:, self.ind_state_idx]
        np.delete(sol.y, self.ind_state_idx, axis=0)

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

        for idx, t_i, y_i, p_i in enumerate(zip(sol.t, sol.y, sol.p)):
            sol.u[idx, self.control_idx] = self.map_func(sol.u[idx, self.control_idx], t_i, y_i, p_i, sol.k)

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

        for idx, t_i, y_i, p_i in enumerate(zip(sol.t, sol.y, sol.p)):
            sol.u[idx, self.control_idx] = self.inv_map_func(sol.u[idx, self.control_idx], t_i, y_i, p_i, sol.k)

        return sol


class DualizeMapper(SolMapper):
    def map(self, sol: Solution, lam=empty_array, nu=empty_array) -> Solution:
        sol.lam = lam
        sol.nu = nu
        return sol

    def inv_map(self, sol: Solution, retain_dual=True) -> Solution:

        if not retain_dual:
            sol.lam = empty_array
            sol.nu = empty_array

        return sol


class NormalizeTimeMapper(SolMapper):
    def __init__(self, delta_ind_idx=None):
        self.delta_ind_idx = delta_ind_idx

    def map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(sol.p)[0]

        delta_t = sol.t[-1] - sol.t[0]
        sol.p = np.insert(sol.p, self.delta_ind_idx, delta_t)

        sol.t = (sol.t - sol.t[0])/delta_t

        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol = copy.deepcopy(sol)

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(sol.p)[0] - 1

        sol.t = sol.t * sol.p[self.delta_ind_idx]
        np.delete(sol.p, self.delta_ind_idx)

        return sol


class AlgebraicControlMapper(SolMapper):
    def __init__(self, prob):

        num_options = len(prob.control_law)

        _args = \
            [prob.independent_variable.sym, prob.extract_syms(prob.states), prob.extract_syms(prob.costates),
             prob.extract_syms(prob.parameters), prob.extract_syms(prob.constants)]

        _args_w_control = copy.copy(_args)
        _args_w_control.insert(3, prob.extract_syms(prob.controls))

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
        sol.u = np.array([self.compute_u(_t, _y, _lam, _p, _k) for _t, _y, _lam, _p, _k
                          in zip(sol.t, sol.y.T, sol.lam.T, sol.p, sol.k)])
        return sol


class DifferentialControlMapper(SolMapper):
    def __init__(self, control_idxs):
        self.control_idxs = control_idxs

    def map(self, sol: Solution) -> Solution:
        sol.y = np.insert(sol.y, sol.u, self.control_idxs)
        sol.u = empty_array
        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol.u = sol.y[:, self.control_idxs]
        sol.y = np.delete(sol.y, self.control_idxs)
        return sol


class SquashToBVPMapper(SolMapper):
    def __init__(self, costate_idxs, coparameter_idxs, constraint_adjoints_idxs):
        self.costate_idxs = costate_idxs
        self.coparameter_idxs = coparameter_idxs
        self.constraint_adjoints_idxs = constraint_adjoints_idxs

    def map(self, sol: Solution) -> Solution:
        sol.y = np.concatenate((sol.y, sol.lam))
        sol.q = np.concatenate((sol.q, sol.mu))
        sol.p_con = np.concatenate((sol.p_con, sol.nu))

        sol.lam = empty_array
        sol.mu = empty_array
        sol.nu = empty_array

        return sol

    def inv_map(self, sol: Solution) -> Solution:
        sol.lam = sol.y[self.costate_idxs]
        sol.mu = sol.q[self.coparameter_idxs]
        sol.nu = sol.p[self.constraint_adjoints_idxs]

        sol.y = np.delete(sol.y, sol.lam)
        sol.q = np.delete(sol.q, sol.mu)
        sol.p_con = np.delete(sol.p_con, sol.nu)

        return sol
