import logging
from typing import Iterable, Collection

import numpy as np
from numba import complex128, float64, njit
from numba.core import errors
from scipy.integrate import simps
from sympy import lambdify

from ..utils import tuplefy


def jit_lambdify(args, sym_func, complex_numbers=False):

    mods = ['numpy', 'math']

    tup_func = tuplefy(sym_func)
    lam_func = lambdify(args, tup_func, mods)
    jit_func = jit_compile_func(lam_func, args, func_name=repr(sym_func), complex_numbers=complex_numbers)

    return jit_func


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


def jit_compile_func(func, args, func_name=None, complex_numbers=False):
    if func_name is None:
        if hasattr(func, 'name'):
            func_name = func.name

    if complex_numbers:
        scalar_type = complex128
        array_type = complex128[:]
    else:
        scalar_type = float64
        array_type = float64[:]

    # TODO Make more elegant
    if not isinstance(args, Iterable):
        args = [args]

    arg_types = []
    for arg in args:
        if isinstance(arg, str):
            if arg == 'scalar':
                arg_types.append(scalar_type)
            elif arg == 'array':
                arg_types.append(array_type)
            else:
                logging.debug('{} not able to be specified. Type specified should be either scalar or array.\n'
                              'Defaulting to "array" type'.format(arg))
                arg_types.append(array_type)
        else:
            if isinstance(arg, Collection):
                arg_types.append(array_type)
            else:
                arg_types.append(scalar_type)
    arg_types = tuple(arg_types)

    try:
        jit_func = njit(arg_types)(func)
        return jit_func

    except errors.NumbaError as e:
        logging.debug('Cannot Compile FunctionComponent: {}\n\tError: {}'.format(func_name, e))
        return func

    except TypeError:
        logging.debug('Cannot Compile FunctionComponent: {} (probably NoneType)'.format(func_name))
        return func


def jit_compile_func_num_args(func, num_args, func_name=None, complex_numbers=False, array_inputs=True):
    if func_name is None:
        if hasattr(func, 'name'):
            func_name = func.__name__

    # TODO Handle mixed singleton and array inputs
    try:
        if complex_numbers and array_inputs:
            arg_types = tuple([complex128[:] for _ in range(num_args)])
        elif array_inputs:
            arg_types = tuple([float64[:] for _ in range(num_args)])
        elif complex_numbers:
            arg_types = tuple([complex128 for _ in range(num_args)])
        else:
            arg_types = tuple([float64 for _ in range(num_args)])
        jit_func = njit(arg_types)(func)
        return jit_func

    except errors.NumbaError:
        logging.debug('Cannot Compile FunctionComponent: {}'.format(func_name))
        return func

    except TypeError:
        logging.debug('Cannot Compile FunctionComponent: {} (probably NoneType)'.format(func_name))
        return func