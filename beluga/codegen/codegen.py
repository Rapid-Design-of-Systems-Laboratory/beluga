import logging
import numpy as np
from numba import njit, float64, errors
from sympy import lambdify
from beluga.utils import sympify
from collections.abc import Iterable


def lambdify_(args, sym_func):

    mods = ['numpy']

    tup_func = tuplefy(sym_func)
    lam_func = lambdify(args, tup_func, mods)
    jit_func = jit_compile_func(lam_func, len(args), func_name=repr(sym_func))

    return jit_func


def jit_compile_func(func, num_args, func_name=None):
    try:
        arg_types = tuple([float64[:] for _ in range(num_args)])
        jit_func = njit(arg_types)(func)
        return jit_func

    except errors.NumbaError as e:
        # logging.debug(e)
        logging.debug('Cannot Compile Function: {}'.format(func_name))
        return func

    except TypeError as e:
        logging.debug('Cannot Compile Function: {} (probably NoneType)'.format(func_name))
        return None


def tuplefy(iter_var):

    if isinstance(iter_var, Iterable):
        iter_var = tuple([tuplefy(item) for item in iter_var])

    return iter_var


class SymBVP:
    def __init__(self, problem_data):
    
        self.raw = problem_data    
    
        # Unpack and sympify problem data
        # self.t = sympify(problem_data['independent'])
        self.x = sympify(problem_data['states'])
        self.u = sympify(problem_data['controls'])
        self.p_d = sympify(problem_data['dynamical_parameters'])
        self.k = sympify(problem_data['constants'])
        self.q = sympify(problem_data['quads'])
        self.p_n = sympify(problem_data['nondynamical_parameters'])
        self.p = self.p_d + self.p_n  # TODO: The parameter usage is inconsistent. Should clean-up down the line

        self.x_dot = sympify(problem_data['states_rates'])
        self.q_dot = sympify(problem_data['quads_rates'])
        self.ham = sympify(problem_data['hamiltonian'])
        self.bc_0 = sympify(problem_data['bc_initial'])
        self.bc_f = sympify(problem_data['bc_terminal'])

        self.dhdu = sympify(problem_data['dHdu'])
        self.initial_cost = sympify(problem_data['initial_cost'])
        self.path_cost = sympify(problem_data['path_cost'])
        self.terminal_cost = sympify(problem_data['terminal_cost'])

        self.df_dy = sympify(problem_data['states_jac'][0])
        self.df_dp = sympify(problem_data['states_jac'][1])

        self.dbc_0_dy = sympify(problem_data['bc_initial_jac'])
        self.dbc_f_dy = sympify(problem_data['bc_terminal_jac'])
        self.dbc_0_dp = sympify(problem_data['bc_initial_parameter_jac'])
        self.dbc_f_dp = sympify(problem_data['bc_terminal_parameter_jac'])

        self.path_constraints = problem_data['path_constraints']

        control_options = problem_data['control_options']
        if control_options is None:
            self.algebraic_control_options = []
        else:
            self.algebraic_control_options = \
                [[sympify(option[str(u_i)]) for u_i in self.u] for option in control_options]

        self.name = problem_data['problem_name']

    def __repr__(self):
        return '{}_SymbolicBVP'.format(self.name)


class FuncBVP(object):
    def __init__(self, sym_bvp):

        self.sym_bvp = sym_bvp
        self.name = sym_bvp.name
        self.raw = sym_bvp.raw

        self.ham_func = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.ham)
        self.compute_control = self.compile_control()

        self.compute_x_dot, self.deriv_func, self.quad_func = self.compile_deriv_func()
        self.deriv_jac_func = self.compile_deriv_jac_func()
        
        self.bc_func = self.compile_bc_func()
        self.bc_func_jac = self.compile_bc_jac_func()

        self.initial_cost = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.initial_cost)
        self.path_cost = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.path_cost)
        self.terminal_cost = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.terminal_cost)
        self.ineq_constraints = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.path_constraints)

    def __repr__(self):
        return '{}_FunctionalBVP'.format(self.name)

    def compile_control(self):

        sym_bvp = self.sym_bvp

        compiled_options = tuple([lambdify_([self.sym_bvp.x, self.sym_bvp.p_d, self.sym_bvp.k], option)
                                  for option in sym_bvp.algebraic_control_options])

        ham_func = self.ham_func

        if len(compiled_options) == 1:
            compiled_option = compiled_options[0]

            def calc_u(x, p_d, k):
                return np.array(compiled_option(x, p_d, k))

        else:
            def calc_u(x, p_d, k):
                u = np.array(compiled_options[0](x, p_d, k))
                ham = ham_func(x, u, p_d, k)

                for option in compiled_options[1:]:
                    u_i = np.array(option(x, p_d, k))
                    ham_i = ham_func(x, u_i, p_d, k)

                    if ham_i < ham:
                        u = u_i

                return u

        control_function = jit_compile_func(calc_u, 3, func_name='control_function')

        return control_function

    def compile_deriv_func(self):

        # TODO control u is expected to feed into functions, look into changing
    
        if len(self.sym_bvp.u) == 0:
    
            calc_x_dot = lambdify_([self.sym_bvp.x, self.sym_bvp.p_d, self.sym_bvp.k], self.sym_bvp.x_dot)
            calc_q_dot = lambdify_([self.sym_bvp.x, self.sym_bvp.p_d, self.sym_bvp.k], self.sym_bvp.q_dot)
    
            def deriv_func(x, _, p_d, k):
                return np.array(calc_x_dot(x, p_d, k))
    
            def quad_func(x, _, p_d, k):
                return np.array(calc_q_dot(x, p_d, k))
    
        else:    
            calc_x_dot = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p_d, self.sym_bvp.k],
                                   self.sym_bvp.x_dot)
            calc_q_dot = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p_d, self.sym_bvp.k],
                                   self.sym_bvp.q_dot)
            calc_u = self.compute_control
    
            def deriv_func(x, _, p_d, k):
                u = calc_u(x, p_d, k)
                return np.array(calc_x_dot(x, u, p_d, k))
    
            def quad_func(x, _, p_d, k):
                u = calc_u(x, p_d, k)
                return np.array(calc_q_dot(x, u, p_d, k))
    
        deriv_func = jit_compile_func(deriv_func, 4, func_name='deriv_func')
        quad_func = jit_compile_func(quad_func, 4, func_name='quad_func')
        
        return calc_x_dot, deriv_func, quad_func

    def compile_deriv_jac_func(self):

        calc_u = self.compute_control

        if any([item is None for item in [self.sym_bvp.df_dy, self.sym_bvp.df_dp]]):
            deriv_func_jac = None

        elif len(self.sym_bvp.u) == 0:
            df_dy = lambdify_([self.sym_bvp.x, self.sym_bvp.p_d, self.sym_bvp.k], self.sym_bvp.df_dy)
            df_dp = lambdify_([self.sym_bvp.x, self.sym_bvp.p_d, self.sym_bvp.k], self.sym_bvp.df_dp)

            def deriv_func_jac(x, _, p_d, k):
                return np.array(df_dy(x, p_d, k)), np.array(df_dp(x, p_d, k))

        else:
            df_dy = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p_d, self.sym_bvp.k], self.sym_bvp.df_dy)
            df_dp = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p_d, self.sym_bvp.k], self.sym_bvp.df_dp)

            def deriv_func_jac(x, _, p_d, k):
                u = calc_u(x, p_d, k)
                return np.array(df_dy(x, u, p_d, k)), np.array(df_dp(x, u, p_d, k))

        deriv_func_jac = jit_compile_func(deriv_func_jac, 4, func_name='deriv_func_jac')
        
        return deriv_func_jac

    def compile_bc_func(self):
    
        if len(self.sym_bvp.u) == 0:
            bc_0_func = lambdify_([self.sym_bvp.x, self.sym_bvp.q, self.sym_bvp.p_d, self.sym_bvp.p_n, self.sym_bvp.k],
                                  self.sym_bvp.bc_0)
            bc_f_func = lambdify_([self.sym_bvp.x, self.sym_bvp.q, self.sym_bvp.p_d, self.sym_bvp.p_n, self.sym_bvp.k],
                                  self.sym_bvp.bc_f)
    
            def bc_func(x_0, q_0, _, x_f, q_f, __, p_d, p_n, k):
                bc_0 = bc_0_func(x_0, q_0, p_d, p_n, k)
                bc_f = bc_f_func(x_f, q_f, p_d, p_n, k)
                return np.concatenate((bc_0, bc_f))
    
        else:
            bc_0_func = lambdify_(
                [self.sym_bvp.x, self.sym_bvp.q, self.sym_bvp.u, self.sym_bvp.p_d, self.sym_bvp.p_n, self.sym_bvp.k],
                self.sym_bvp.bc_0)
            bc_f_func = lambdify_(
                [self.sym_bvp.x, self.sym_bvp.q, self.sym_bvp.u, self.sym_bvp.p_d, self.sym_bvp.p_n, self.sym_bvp.k],
                self.sym_bvp.bc_f)
    
            def bc_func(x_0, q_0, _, x_f, q_f, __, p_d, p_n, k):
                u_0 = self.compute_control(x_0, p_d, k)
                u_f = self.compute_control(x_f, p_d, k)
                
                bc_0 = bc_0_func(x_0, q_0, u_0, p_d, p_n, k)
                bc_f = bc_f_func(x_f, q_f, u_f, p_d, p_n, k)
                return np.concatenate((bc_0, bc_f))
    
        return jit_compile_func(bc_func, 9, func_name='bc_func')

    def compile_bc_jac_func(self):
    
        calc_u = self.compute_control

        if any([item is None for item in
                [self.sym_bvp.dbc_0_dy, self.sym_bvp.dbc_f_dy, self.sym_bvp.dbc_0_dp, self.sym_bvp.dbc_f_dp]]):
            bc_func_jac = None
    
        elif len(self.sym_bvp.u) == 0:
    
            dbc_0_dy = lambdify_([self.sym_bvp.x, self.sym_bvp.p, self.sym_bvp.k], self.sym_bvp.dbc_0_dy)
            dbc_f_dy = lambdify_([self.sym_bvp.x, self.sym_bvp.p, self.sym_bvp.k], self.sym_bvp.dbc_f_dy)
            dbc_0_dp = lambdify_([self.sym_bvp.x, self.sym_bvp.p, self.sym_bvp.k], self.sym_bvp.dbc_0_dp)
            dbc_f_dp = lambdify_([self.sym_bvp.x, self.sym_bvp.p, self.sym_bvp.k], self.sym_bvp.dbc_f_dp)

            # TODO: Expects u argument, is this needed
            def bc_func_jac(x_0, x_f, _, p, k):
                return np.array(dbc_0_dy(x_0, p, k)), np.array(dbc_f_dy(x_f, p, k)),\
                    (np.array(dbc_0_dp(x_0, p, k)) + np.array(dbc_f_dp(x_f, p, k)))
    
        else:
    
            dbc_0_dy = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p, self.sym_bvp.k],
                                 self.sym_bvp.dbc_0_dy)
            dbc_f_dy = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p, self.sym_bvp.k],
                                 self.sym_bvp.dbc_f_dy)
            dbc_0_dp = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p, self.sym_bvp.k],
                                 self.sym_bvp.dbc_0_dp)
            dbc_f_dp = lambdify_([self.sym_bvp.x, self.sym_bvp.u, self.sym_bvp.p, self.sym_bvp.k],
                                 self.sym_bvp.dbc_f_dp)

            num_p_d = len(self.sym_bvp.p_d)
    
            def bc_func_jac(x_0, x_f, _, p, k):
                p_d = p[:num_p_d]
                u_0 = calc_u(x_0, p_d, k)
                u_f = calc_u(x_f, p_d, k)
    
                return np.array(dbc_0_dy(x_0, u_0, p, k)), np.array(dbc_f_dy(x_f, u_f, p, k)),\
                    (np.array(dbc_0_dp(x_0, u_0, p, k)) + np.array(dbc_f_dp(x_f, u_f, p, k)))
    
        bc_func_jac = jit_compile_func(bc_func_jac, 5, func_name='bc_func_jac')
        
        return bc_func_jac
