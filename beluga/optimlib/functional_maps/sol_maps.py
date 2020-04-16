from abc import ABC
from  collections.abc import Iterable
from beluga.problib.sol_classes import *
import copy
import sympy
from typing import Union
from beluga import LocalCompiler


class SolMapper(ABC):
    def map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        pass

    def inv_map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        pass


class IdentityMapper(SolMapper):
    def map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        return copy.deepcopy(sol)

    def inv_map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        return copy.deepcopy(sol)


class MomentumShiftMapper(SolMapper):
    def __init__(self, ind_state_idx=None):
        self.ind_state_idx = ind_state_idx

    def map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        sol = copy.deepcopy(sol)

        if self.ind_state_idx is None:
            self.ind_state_idx = np.shape(sol.y)[1]

        sol.y = np.insert(sol.y, self.ind_state_idx, sol.t, axis=0)

        if isinstance(sol, DualSol):
            sol.lam = np.insert(sol.lam, self.ind_state_idx, sol.lam_t, axis=0)

        return sol

    def inv_map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        sol = copy.deepcopy(sol)

        if self.ind_state_idx is None:
            self.ind_state_idx = np.shape(sol.y)[1] - 1

        sol.t = sol.y[:, self.ind_state_idx]
        np.delete(sol.y, self.ind_state_idx, axis=0)

        if isinstance(sol, DualSol):
            sol.lam_t = sol.lam[:, self.ind_state_idx]
            np.delete(sol.lam, self.ind_state_idx, axis=0)

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

    def map(self, sol: Union[OCPSol, DualSol]) -> Union[OCPSol, DualSol]:
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

    def inv_map(self, sol: Union[OCPSol, DualSol]) -> Union[OCPSol, DualSol]:
        sol = copy.deepcopy(sol)

        if self.inv_map_func is None:
            u_trig = sympy.Symbol('_u_trig')

            u_min = self.lower_expr
            u_max = self.upper_expr

            u_range = u_max - u_min
            u_offset = (u_max + u_min) / 2

            u_expr = u_range*sympy.sin(u_trig) + u_offset

            self.map_func = self.local_compiler.lambdify([u_trig] + self.args, u_expr)

        for idx, t_i, y_i, p_i in enumerate(zip(sol.t, sol.y, sol.p)):
            sol.u[idx, self.control_idx] = self.map_func(sol.u[idx, self.control_idx], t_i, y_i, p_i, sol.k)

        return sol


class DualizeMapper(SolMapper):
    def map(self, sol: OCPSol, lam_t=None, lam=None, nu=None, mu=None) -> DualSol:
        return DualSol(sol.t, sol.y, sol.u, sol.p, sol.k, sol.q, lam_t, lam, nu, mu)

    def inv_map(self, sol: DualSol, retain_dual=True) -> OCPSol:

        ocp_sol = OCPSol(sol.t, sol.y, sol.u, sol.p, sol.k, sol.q)
        ocp_sol.dual = ocp_sol.DualInfo(sol.lam_t, sol.lam, sol.nu, sol.mu)

        return ocp_sol


class NormalizeTimeMapper(SolMapper):
    def __init__(self, delta_ind_idx=None):
        self.delta_ind_idx = delta_ind_idx

    def map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        sol = copy.deepcopy(sol)

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(sol.p)[0]

        delta_t = sol.t[-1] - sol.t[0]
        sol.p = np.insert(sol.p, self.delta_ind_idx, delta_t)

        sol.t = (sol.t - sol.t[0])/delta_t

        return sol

    def inv_map(self, sol: Union[BVPSol, OCPSol, DualSol]) -> Union[BVPSol, OCPSol, DualSol]:
        sol = copy.deepcopy(sol)

        if self.delta_ind_idx is None:
            self.delta_ind_idx = np.shape(sol.p)[0] - 1

        sol.t = sol.t * sol.p[self.delta_ind_idx]
        np.delete(sol.p, self.delta_ind_idx)

        return sol


class DifferentialControlMapper(SolMapper):
    def __init__(self, control_idxs):
        self.control_idxs = control_idxs

    def map(self, sol: DualSol) -> DualSol:
        sol.y[:, self.control_idxs] = sol.u
        return sol

    def inv_map(self, sol: DualSol) -> DualSol:
        sol.u = sol.y[:, self.control_idxs]
        return sol


class SquashToBVPMapper(SolMapper):
    def __init__(self, costate_idxs, coparameter_idxs, constraint_adjoints_idxs):
        self.costate_idxs = costate_idxs
        self.coparameter_idxs = coparameter_idxs
        self.constraint_adjoints_idxs = constraint_adjoints_idxs

    def map(self, sol: DualSol) -> BVPSol:
        bvp_sol = BVPSol(sol.t, np.concatenate((sol.y, sol.lam)), sol.p, sol.k, sol.q)
        return bvp_sol

    def inv_map(self, sol: BVPSol) -> DualSol:
        pass


class InterfaceSolverMapper(SolMapper):
    pass
