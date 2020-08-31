import numpy as np
import copy
from collections import Iterable

from ..ivp_solvers.ivpsol import Trajectory
from ..compilation import LocalCompiler, jit_compile_func, compile_control
from ...symbolic.problem_classes.components_structures import extract_syms, getattr_from_list


class FuncProblem:
    def __init__(self, prob, local_compiler=None):

        if local_compiler is None:
            self.local_compiler = LocalCompiler()
        else:
            self.local_compiler = local_compiler

        self.lambdify = self.local_compiler.lambdify

        self.prob = prob

        self.ham_func = None
        self.compute_u = None
        self.compute_y_dot = None
        self.compute_q_dot = None

        self.deriv_func = None
        self.quad_func = None
        self.deriv_func_jac = None

        self.compute_initial_bc = None
        self.compute_terminal_bc = None

        self.bc_func = None
        self.bc_func_jac = None

        self.initial_cost_func, self.path_cost_func, self.terminal_cost_func = None, None, None
        self.ineq_constraints = None

        self.compute_scale_factors = None
        self.scale_sol = None

        self._state_syms = []
        self._control_syms = []
        self._parameter_syms = []
        self._constraint_parameters_syms = []
        self._constant_syms = []

        self._dynamic_args = []
        self._dynamic_args_w_controls = []

        self._bc_args = []
        self._bc_args_w_quads = []

        self._initialized = False

    def _initialize(self):

        self._state_syms = extract_syms(self.prob.states)
        self._control_syms = extract_syms(self.prob.controls)
        self._parameter_syms = extract_syms(self.prob.parameters)
        self._constant_syms = extract_syms(self.prob.constants)

        self._quad_syms = extract_syms(self.prob.quads)
        self._constraint_parameters_syms = extract_syms(self.prob.constraint_parameters)

        self._dynamic_args = \
            [self._state_syms, self._parameter_syms, self._constant_syms]
        self._dynamic_args_w_controls = \
            [self._state_syms, self._control_syms, self._parameter_syms, self._constant_syms]

        self._bc_args = \
            [self._state_syms, self._parameter_syms,
             self._constraint_parameters_syms, self._constant_syms]
        self._bc_args_w_quads = \
            [self._state_syms, self._quad_syms, self._parameter_syms,
             self._constraint_parameters_syms, self._constant_syms]
        self._bc_args_w_controls = \
            [self._state_syms, self._control_syms, self._parameter_syms,
             self._constraint_parameters_syms, self._constant_syms]
        self._bc_args_w_quads_controls = \
            [self._state_syms, self._quad_syms, self._control_syms, self._parameter_syms,
             self._constraint_parameters_syms, self._constant_syms]

        self._units_args = \
            [self.prob.independent_variable.sym, self._state_syms, self._quad_syms,
             self._parameter_syms, self._constraint_parameters_syms, self._constant_syms]

        # self._dynamic_args = \
        #     [self.prob.independent_variable.sym, self._state_syms, self._parameter_syms, self._constant_syms]
        # self._dynamic_args_w_controls = \
        #     [self.prob.independent_variable.sym, self._state_syms, self._control_syms,
        #      self._parameter_syms, self._constant_syms]
        #
        # self._bc_args = \
        #     [self.prob.independent_variable.sym, self._state_syms, self._parameter_syms,
        #      self._constraint_parameters_syms, self._constant_syms]
        # self._bc_args_w_quads = \
        #     [self.prob.independent_variable.sym, self._state_syms, self._quad_syms, self._parameter_syms,
        #      self._constraint_parameters_syms, self._constant_syms]
        #
        # self._units_args = \
        #     [self.prob.independent_variable.sym, self._state_syms, self._quad_syms, self._control_syms,
        #      self._parameter_syms, self._constant_syms]

        self._initialized = True

    def compile_problem(self, use_time_arg=False, use_control_arg=False, use_quad_arg=True):

        self._initialize()

        if hasattr(self.prob.hamiltonian, 'expr'):
            self.ham_func = self.lambdify(self._dynamic_args_w_controls, self.prob.hamiltonian.expr)

        self.compile_control()
        self.compile_deriv_func(use_control_arg=use_control_arg)

        self.compile_bc(use_quad_arg=use_quad_arg)

        self.compile_cost(use_quad_arg=use_quad_arg, use_control_arg=use_control_arg)

        self.compile_scaling()

        return self

    def compile_control(self):

        self.compute_u = compile_control(self.prob.control_law, self._dynamic_args, self.ham_func, self.lambdify)

        return self.compute_u

    def compile_deriv_func(self, use_control_arg=False):
        sym_eom = getattr_from_list(self.prob.states, 'eom')
        sym_eom_q = getattr_from_list(self.prob.quads, 'eom')

        if self.compute_u is None:
            if use_control_arg:
                _args = self._dynamic_args_w_controls
            else:
                _args = self._dynamic_args

            self.compute_y_dot = self.lambdify(_args, sym_eom)
            self.compute_q_dot = self.lambdify(_args, sym_eom_q)

            self.deriv_func, self.quad_func = self.compute_y_dot, self.compute_q_dot

        else:
            self.compute_y_dot = self.lambdify(self._dynamic_args_w_controls, sym_eom)
            self.compute_q_dot = self.lambdify(self._dynamic_args_w_controls, sym_eom_q)

            compute_u = self.compute_u
            compute_y_dot = self.compute_y_dot
            compute_q_dot = self.compute_q_dot

            def deriv_func(_y, _p, _k):
                _u = compute_u(_y, _p, _k)
                return np.array(compute_y_dot(_y, _u, _p, _k))

            def quad_func(_y, _p, _k):
                _u = compute_u(_y, _p, _k)
                return np.array(compute_q_dot(_y, _u, _p, _k))

            self.deriv_func = jit_compile_func(deriv_func, self._dynamic_args)
            self.quad_func = jit_compile_func(quad_func, self._dynamic_args)

        return self.deriv_func, self.quad_func

    def compile_bc(self, use_quad_arg=True):

        sym_initial_bc = getattr_from_list(self.prob.constraints['initial'], 'expr')
        sym_terminal_bc = getattr_from_list(self.prob.constraints['terminal'], 'expr')

        if use_quad_arg:
            if self.compute_u is None:
                _args = self._bc_args_w_quads

                compute_initial_bc = self.lambdify(_args, sym_initial_bc)
                compute_terminal_bc = self.lambdify(_args, sym_terminal_bc)

                def bc_func(_y0, _q0, _yf, _qf, _p, _p_con, _k):
                    bc_0 = np.array(compute_initial_bc(_y0, _q0, _p, _p_con, _k))
                    bc_f = np.array(compute_terminal_bc(_yf, _qf, _p, _p_con, _k))
                    return np.concatenate((bc_0, bc_f))
            else:
                _args = self._bc_args_w_quads_controls

                compute_initial_bc = self.lambdify(_args, sym_initial_bc)
                compute_terminal_bc = self.lambdify(_args, sym_terminal_bc)

                compute_u = self.compute_u

                def bc_func(_y0, _q0, _yf, _qf, _p, _p_con, _k):

                    _u0 = compute_u(_y0, _p, _k)
                    _uf = compute_u(_yf, _p, _k)

                    bc_0 = np.array(compute_initial_bc(_y0, _q0, _u0, _p, _p_con, _k))
                    bc_f = np.array(compute_terminal_bc(_yf, _qf, _uf, _p, _p_con, _k))
                    return np.concatenate((bc_0, bc_f))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms + self._quad_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms
            self.bc_func = jit_compile_func(bc_func, _combined_args)
            self.compute_initial_bc, self.compute_terminal_bc = compute_initial_bc, compute_terminal_bc

        else:
            if self.compute_u is None:
                _args = self._bc_args

                compute_initial_bc = self.lambdify(_args, sym_initial_bc)
                compute_terminal_bc = self.lambdify(_args, sym_terminal_bc)

                def bc_func(_y0, _yf, _p, _p_con, _k):
                    bc_0 = np.array(compute_initial_bc(_y0, _p, _p_con, _k))
                    bc_f = np.array(compute_terminal_bc(_yf, _p, _p_con, _k))
                    return np.concatenate((bc_0, bc_f))

            else:
                _args = self._bc_args_w_quads

                compute_initial_bc = self.lambdify(_args, sym_initial_bc)
                compute_terminal_bc = self.lambdify(_args, sym_terminal_bc)

                compute_u = self.compute_u

                def bc_func(_y0, _yf, _p, _p_con, _k):

                    _u0 = compute_u(_y0, _p, _k)
                    _uf = compute_u(_yf, _p, _k)

                    bc_0 = np.array(compute_initial_bc(_y0, _u0, _p, _p_con, _k))
                    bc_f = np.array(compute_terminal_bc(_yf, _uf, _p, _p_con, _k))
                    return np.concatenate((bc_0, bc_f))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms

            self.bc_func = jit_compile_func(bc_func, _combined_args)
            self.compute_initial_bc, self.compute_terminal_bc = compute_initial_bc, compute_terminal_bc

        return self.bc_func

    def compile_deriv_jac_func(self, use_control_arg=False):

        if any([item is None for item in self.prob.func_jac.items()]):
            return None

        elif use_control_arg:
            df_dy = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dy'])
            df_dp = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dp'])

            def deriv_func_jac(_y, _u, _p, _k):
                return np.array(df_dy(_y, _u, _p, _k)), np.array(df_dp(_y, _u, _p, _k))

            self.deriv_func_jac = jit_compile_func(deriv_func_jac, self._dynamic_args_w_controls,
                                                   func_name='deriv_func_jac')

        elif self.compute_u is not None:
            df_dy = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dy'])
            df_dp = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dp'])

            compute_u = self.compute_u

            def deriv_func_jac(_y, _p, _k):
                _u = compute_u(_y, _p, _k)
                return np.array(df_dy(_y, _u, _p, _k)), np.array(df_dp(_y, _u, _p, _k))

            self.deriv_func_jac = jit_compile_func(deriv_func_jac, self._dynamic_args,
                                                   func_name='deriv_func_jac')

        else:
            df_dy = self.lambdify(self._dynamic_args, self.prob.func_jac['df_dy'])
            df_dp = self.lambdify(self._dynamic_args, self.prob.func_jac['df_dp'])

            def deriv_func_jac(_y, _p, _k):
                return np.array(df_dy(_y, _p, _k)), np.array(df_dp(_y, _p, _k))

            self.deriv_func_jac = jit_compile_func(deriv_func_jac, self._dynamic_args,
                                                   func_name='deriv_func_jac')

        return self.deriv_func_jac

    def compile_bc_jac_func(self, use_quad_arg=True):

        if all([item is None
                for item in list(self.prob.bc_jac['initial'].values()) + list(self.prob.bc_jac['terminal'].values())]):
            return None

        elif use_quad_arg:
            _args = self._bc_args_w_quads

        else:
            _args = self._bc_args

        dbc_0_dy = self.lambdify(_args, self.prob.bc_jac['initial']['dbc_dy'])
        dbc_f_dy = self.lambdify(_args, self.prob.bc_jac['terminal']['dbc_dp'])
        dbc_0_dp = self.lambdify(_args, self.prob.bc_jac['initial']['dbc_dy'])
        dbc_f_dp = self.lambdify(_args, self.prob.bc_jac['terminal']['dbc_dp'])

        if use_quad_arg:
            dbc_0_dq = self.lambdify(_args, self.prob.bc_jac['initial']['dbc_dq'])
            dbc_f_dq = self.lambdify(_args, self.prob.bc_jac['terminal']['dbc_dq'])

            def bc_func_jac(_y0, _q0, _yf, _qf, _p, _p_con, _k):
                return np.array(dbc_0_dy(_y0, _q0, _p, _p_con, _k)), \
                       np.array(dbc_f_dy(_yf, _qf, _p, _p_con, _k)), \
                       np.array(dbc_0_dq(_y0, _q0, _p, _p_con, _k)), \
                       np.array(dbc_f_dq(_yf, _qf, _p, _p_con, _k)), \
                       (np.array(dbc_0_dp(_y0, _q0, _p, _p_con, _k))
                        + np.array(dbc_f_dp(_yf, _qf, _p, _p_con, _k)))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms + self._quad_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms

        else:
            def bc_func_jac(_y0, _q0, _yf, _qf, _p, _p_con, _k):
                return np.array(dbc_0_dy(_y0, _p, _p_con, _k)), \
                       np.array(dbc_f_dy(_yf, _p, _p_con, _k)), \
                       (np.array(dbc_0_dp(_y0, _p, _p_con, _k))
                        + np.array(dbc_f_dp(_yf, _p, _p_con, _k)))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms

        self.bc_func_jac = jit_compile_func(bc_func_jac, _combined_args, func_name='bc_func_jac')

        return self.bc_func_jac

    def compile_cost(self, use_quad_arg=True, use_control_arg=False):

        if use_quad_arg:
            _bc_args = self._bc_args_w_quads
        else:
            _bc_args = self._bc_args

        self.initial_cost_func = self.lambdify(_bc_args, self.prob.cost.initial)

        self.terminal_cost_func = self.lambdify(_bc_args, self.prob.cost.terminal)

        if self.compute_u is None:
            if use_control_arg:
                _dyn_args = self._dynamic_args_w_controls
            else:
                _dyn_args = self._dynamic_args

            self.path_cost_func = self.lambdify(_dyn_args, self.prob.cost.path)

        else:
            _compute_u = self.compute_u
            _compute_path_cost = self.lambdify(self._dynamic_args_w_controls, self.prob.cost.path)

            def path_cost_func(_y, _p, _k):
                _u = _compute_u(_y, _p, _k)
                return np.array(_compute_path_cost(_y, _u, _p, _k))

            self.path_cost_func = jit_compile_func(path_cost_func, self._dynamic_args)

        return self.initial_cost_func, self.path_cost_func, self.terminal_cost_func

    def compile_scaling(self):

        lambdify = self.lambdify

        units = self.prob.units
        units_syms = getattr_from_list(units, 'sym')
        units_func = getattr_from_list(units, 'expr')

        compute_unit_factors = lambdify(self._units_args, units_func)

        scalable_components_list = [
            self.prob.independent_variable,
            self.prob.states,
            self.prob.quads,
            self.prob.controls,
            self.prob.parameters,
            self.prob.constraint_parameters,
            self.prob.constants]

        compute_factors = [
            lambdify(units_syms, getattr_from_list(component, 'units')) for component in scalable_components_list
        ]

        def compute_scale_factors(sol: Trajectory):

            ref_vals = tuple(
                [max_mag(_arr) for _arr in [sol.t, sol.y, sol.q]]
                + [np.fabs(_arr) for _arr in [sol.dynamical_parameters, sol.nondynamical_parameters, sol.const]])
            # ref_vals = tuple([max_mag(_arr) for _arr in [sol.t, sol.y, sol.q, sol.u]]
            #                  + [np.fabs(_arr) for _arr in [sol.dynamical_parameters, sol.const]])

            unit_factors = compute_unit_factors(*ref_vals)

            return tuple([compute_factor(*unit_factors) for compute_factor in compute_factors])

        def scale_sol(sol: Trajectory, scale_factors, inv=False):

            sol = copy.deepcopy(sol)

            if inv:
                op = np.multiply
            else:
                op = np.divide

            sol.t = op(sol.t, scale_factors[0])
            sol.y = op(sol.y, scale_factors[1])
            sol.q = op(sol.q, scale_factors[2])
            sol.u = op(sol.u, scale_factors[3])
            sol.dynamical_parameters = op(sol.dynamical_parameters, scale_factors[4])
            sol.nondynamical_parameters = op(sol.nondynamical_parameters, scale_factors[5])
            sol.const = op(sol.const, scale_factors[6])

            return sol

        self.compute_scale_factors = compute_scale_factors
        self.scale_sol = scale_sol

        return self


def max_mag(arr: np.ndarray, axis=0):
    if arr is None:
        return np.array([])
    elif not isinstance(arr, Iterable):
        return abs(arr)
    elif not isinstance(arr, np.ndarray):
        arr = np.array(arr)

    if arr.size == 0:
        return np.array([])
    else:
        return np.max(np.fabs(arr), axis=axis)
