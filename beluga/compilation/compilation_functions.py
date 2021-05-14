import numpy as np
from scipy.integrate import simps

from .jit import jit_lambdify, jit_compile_func


def compile_control(control_options, args, ham_func, lambdify_func=jit_lambdify):

    num_options = len(control_options)

    if num_options == 0:
        return None

    elif num_options == 1:
        compiled_option = lambdify_func(args, [*control_options.values()])

        def calc_u(_y, _p, _k):
            return np.array(compiled_option(_y, _p, _k))

    else:
        compiled_options = lambdify_func(args, control_options)

        def calc_u(_y, _p, _k):
            u_set = np.array(compiled_options(_y, _p, _k))

            u = u_set[0, :]
            ham = ham_func(_y, u, _p, _k)
            for n in range(1, num_options):
                ham_i = ham_func(_y, u_set[n, :], _p, _k)
                if ham_i < ham:
                    u = u_set[n, :]

            return u

    return jit_compile_func(calc_u, args, func_name='control_function')


def compile_cost(symbolic_cost, dynamic_args, bc_args, lambdify_func=jit_lambdify):

    compute_initial_cost = lambdify_func(bc_args, symbolic_cost.initial)
    compute_terminal_cost = lambdify_func(bc_args, symbolic_cost.terminal)
    compute_path_cost = lambdify_func(dynamic_args, symbolic_cost.path)

    def compute_cost(_t, _y, _q, _u, _p, _k):

        if len(_q) > 0:
            cost = compute_initial_cost(_y[0, :], _q[0, :], _p, _k) \
                   + compute_terminal_cost(_y[-1, :], _q[-1, :], _p, _k)
        else:
            cost = compute_initial_cost(_y[0, :], _q, _p, _k) + compute_terminal_cost(_y[-1, :], _q, _p, _k)

        path_cost = np.array([compute_path_cost(yi, ui, _p, _k) for yi, ui in zip(_y, _u)])
        cost += simps(path_cost, _t, even='last')

        return cost

    return compute_cost
