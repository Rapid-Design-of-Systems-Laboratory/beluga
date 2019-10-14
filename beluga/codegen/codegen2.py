import logging
import numpy as np
from numba import njit, float64, errors
from sympy import lambdify, sympify
# from beluga.utils import sympify
from collections.abc import Iterable

import cloudpickle

filename = 'moon.beluga'

with open(filename, 'rb') as file:
    raw_bvp = cloudpickle.load(file)

logging.basicConfig(level=logging.DEBUG)


class SymBVP:
    def __init__(self, problem_data):
        # Unpack and sympify problem data

        # self.t = sympify(problem_data['independent'])
        self.x = sympify(problem_data['states'])
        self.u = sympify(problem_data['controls'])
        self.p_d = sympify(problem_data['dynamical_parameters'])
        self.k = sympify(problem_data['constants'])
        self.q = sympify(problem_data['quads'])
        self.p_n = sympify(problem_data['nondynamical_parameters'])

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

        control_options = problem_data['control_options']
        self.algebraic_control_options = \
            [[sympify(option[str(u_i)]) for u_i in self.u] for option in control_options]

        self.path_constraints = problem_data['path_constraints']

        self.name = problem_data['problem_name']

    def __repr__(self):
        return '{}_SymbolicBVP'.format(self.name)


class FuncBVP(object):
    def __init__(self):
        self.deriv_func = None
        self.deriv_jac_func = None
        self.quad_func = None
        self.bc_func = None
        self.bc_func_jac = None
        self.compute_control = None
        self.initial_cost = None
        self.path_cost = None
        self.terminal_cost = None
        self.ineq_constraints = None
        self.ham_func = None

        self.raw = dict()

        self.name = None

        self.calc_x_dot = None

    def __repr__(self):
        return '{}_FunctionalBVP'.format(self.name)


def preprocess(problem_data):
    # TODO Handle custom functions
    sym_bvp = SymBVP(problem_data)
    compile_bvp(sym_bvp)


def compile_bvp(sym_bvp):

    func_bvp = FuncBVP()  #

    func_bvp.name = sym_bvp.name  #
    compile_deriv_func(sym_bvp, func_bvp)
    compile_deriv_jac_func(sym_bvp, func_bvp)
    compile_cost_func(sym_bvp, func_bvp)
    compile_constraint_func(sym_bvp, func_bvp)
    compile_bc_func(sym_bvp, func_bvp)
    compile_bc_jac_func(sym_bvp, func_bvp)

    return func_bvp


def compile_control(sym_bvp, func_bvp):

    compiled_options = tuple([lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], option)
                              for option in sym_bvp.algebraic_control_options])

    ham_func = func_bvp.ham_func

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

    func_bvp.compute_control = jit_function(calc_u, 3, func_name='calc_u')

    return func_bvp.compute_control


def compile_deriv_func(sym_bvp, func_bvp):

    if len(sym_bvp.u) == 0:

        calc_x_dot = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.x_dot)
        func_bvp.calc_x_dot = calc_x_dot
        calc_q_dot = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.q_dot)

        func_bvp.ham_func = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.ham)

        def deriv_func(x, p_d, k):
            return np.array(calc_x_dot(x, p_d, k))

        def quad_func(x, p_d, k):
            return np.array(calc_q_dot(x, p_d, k))

    else:
        func_bvp.ham_func = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.ham)

        calc_x_dot = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.x_dot)
        func_bvp.calc_x_dot = calc_x_dot
        calc_q_dot = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.q_dot)
        calc_u = compile_control(sym_bvp, func_bvp)

        def deriv_func(x, p_d, k):
            u = calc_u(x, p_d, k)
            return np.array(calc_x_dot(x, u, p_d, k))

        def quad_func(x, p_d, k):
            u = calc_u(x, p_d, k)
            return np.array(calc_q_dot(x, u, p_d, k))

    func_bvp.deriv_func = jit_function(deriv_func, 3, func_name='deriv_func')
    func_bvp.quad_func = jit_function(quad_func, 3, func_name='quad_func')


def compile_bc_func(sym_bvp, func_bvp):

    if len(sym_bvp.u) == 0:

        bc_0_func = lambdify_([sym_bvp.x, sym_bvp.q, sym_bvp.p_d, sym_bvp.p_n, sym_bvp.k], sym_bvp.bc_0)
        bc_f_func = lambdify_([sym_bvp.x, sym_bvp.q, sym_bvp.p_d, sym_bvp.p_n, sym_bvp.k], sym_bvp.bc_f)

        def bc_func(x_0, q_0, x_f, q_f, p_d, p_n, k):

            bc_0 = bc_0_func(x_0, q_0, p_d, p_n, k)
            bc_f = bc_f_func(x_f, q_f, p_d, p_n, k)

            return np.concatenate((bc_0, bc_f))

    else:

        bc_0_func = lambdify_([sym_bvp.x, sym_bvp.q, sym_bvp.u, sym_bvp.p_d, sym_bvp.p_n, sym_bvp.k], sym_bvp.bc_0)
        bc_f_func = lambdify_([sym_bvp.x, sym_bvp.q, sym_bvp.u, sym_bvp.p_d, sym_bvp.p_n, sym_bvp.k], sym_bvp.bc_f)

        def bc_func(x_0, q_0, x_f, q_f, p_d, p_n, k):

            u_0 = func_bvp.compute_control(x_0, p_d, k)
            u_f = func_bvp.compute_control(x_f, p_d, k)

            bc_0 = bc_0_func(x_0, q_0, u_0, p_d, p_n, k)
            bc_f = bc_f_func(x_f, q_f, u_f, p_d, p_n, k)

            return np.concatenate((bc_0, bc_f))

    func_bvp.bc_func = bc_func


def compile_cost_func(sym_bvp, func_bvp):

    func_bvp.initial_cost = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.initial_cost)
    func_bvp.path_cost = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.path_cost)
    func_bvp.terminal_cost = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.terminal_cost)


def compile_constraint_func(sym_bvp, func_bvp):

    func_bvp.ineq_constraints = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.path_constraints)


def compile_bc_jac_func(sym_bvp, func_bvp):

    calc_u = func_bvp.compute_control

    if len(sym_bvp.u) == 0:

        dbc_0_dy = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_0_dy)
        dbc_f_dy = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_f_dy)
        dbc_0_dp = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_0_dp)
        dbc_f_dp = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_f_dp)

        def bc_func_jac(x_0, x_f, p_d, k):
            return dbc_0_dy(x_0, p_d, k), dbc_f_dy(x_f, p_d, k), dbc_0_dp(x_0, p_d, k), dbc_f_dp(x_f, p_d, k)

    else:

        dbc_0_dy = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_0_dy)
        dbc_f_dy = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_f_dy)
        dbc_0_dp = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_0_dp)
        dbc_f_dp = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.dbc_f_dp)

        def bc_func_jac(x_0, x_f, p_d, k):
            u_0 = calc_u(x_0, p_d, k)
            u_f = calc_u(x_f, p_d, k)

            out = (dbc_0_dy(x_0, u_0, p_d, k), dbc_f_dy(x_f, u_f, p_d, k), dbc_0_dp(x_0, u_0, p_d, k),
                   dbc_f_dp(x_f, u_f, p_d, k))

            return out

    func_bvp.bc_func_jac = jit_function(bc_func_jac, 4, func_name='bc_func_jac')


def compile_deriv_jac_func(sym_bvp, func_bvp):

    calc_u = func_bvp.compute_control

    if len(sym_bvp.u) == 0:

        df_dy = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.df_dy)
        df_dp = lambdify_([sym_bvp.x, sym_bvp.p_d, sym_bvp.k], sym_bvp.df_dp)

        def deriv_func_jac(x, p_d, k):
            df_dy_out = df_dy(x, p_d, k)
            df_dp_out = df_dp(x, p_d, k)
            return df_dy_out, df_dp_out

    else:

        df_dy = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.df_dy)
        df_dp = lambdify_([sym_bvp.x, sym_bvp.u, sym_bvp.p_d, sym_bvp.k], sym_bvp.df_dp)

        def deriv_func_jac(x, p_d, k):
            u = calc_u(x, p_d, k)
            return df_dy(x, u, p_d, k), df_dp(x, u, p_d, k)

    func_bvp.deriv_func_jac = jit_function(deriv_func_jac, 3, func_name='deriv_func_jac')


def lambdify_(args, sym_func):

    mods = ['numpy']

    # print(lambdastr(args, sym_func))
    tup_func = tuplefy(sym_func)
    lam_func = lambdify(args, tup_func, mods)
    jit_func = jit_function(lam_func, len(args), func_name=repr(sym_func))

    return jit_func


def jit_function(func, num_args, func_name=None):
    try:
        arg_types = tuple([float64[:] for _ in range(num_args)])
        jit_func = njit(arg_types)(func)
        # logging.debug('Successfully Compiled: {}'.format(func_name))
        return jit_func

    except errors.NumbaError as e:
        # logging.debug(e)
        logging.debug('Cannot Compile Function: {}'.format(func_name))
        return func


def tuplefy(iter_var):

    if isinstance(iter_var, Iterable):
        iter_var = tuple([tuplefy(item) for item in iter_var])

    return iter_var


# preprocess(raw_bvp)

s_bvp = SymBVP(raw_bvp)
f_bvp = compile_bvp(s_bvp)

x_test = np.random.rand(len(s_bvp.x))
u_test = np.random.rand(len(s_bvp.u))
p_d_test = np.random.rand(len(s_bvp.p_d))
p_n_test = np.random.rand(len(s_bvp.p_n))
k_test = np.random.rand(len(s_bvp.k))
q_test = np.random.rand(len(s_bvp.q))
