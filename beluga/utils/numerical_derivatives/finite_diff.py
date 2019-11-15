import numpy as np
import numba
from numba import njit, float64, complex128, types, errors
from numba.unsafe.ndarray import to_fixed_tuple
import logging
import inspect


def gen_fin_diff(func, arg_idx=0, deriv_order=1, step_size=1e-6, acc_order=1, method='central', complex_arg=False):

    arg_len = len(inspect.signature(func).parameters)

    if complex_arg:
        arg_type = complex128
    else:
        arg_type = float64

    try:
        arg_list = [arg_type] * arg_len

        if type(func) is numba.targets.registry.CPUDispatcher:
            if complex_arg:
                func.disable_compile(False)
                func = func.compile(tuple(arg_type))
        else:
            func = njit(tuple(arg_list))(func)

    except errors.NumbaError as e:
        logging.debug(e, 'Cannot jit compile {} to compile numerical derivative'.format(func.__name__))

    if arg_idx > arg_len:
        raise SyntaxError('Argument index exceeds number of arguments')

    num_pnts = deriv_order + acc_order

    if method == 'forward':
        grid_pnts = np.arange(0, num_pnts)
    elif method == 'backward':
        grid_pnts = np.arange(-(num_pnts - 1), 1)
    elif method == 'central':
        if num_pnts % 2 == 0:
            num_pnts += 1
        grid_pnts = np.arange(-(num_pnts - 1) / 2, (num_pnts - 1) / 2 + 1)
    else:
        raise NotImplementedError('{} method is not implemented'.format(method))

    coeff_array = gen_fin_diff_coeff(deriv_order, grid_pnts)[-1]
    non_zero_pnts = np.where(coeff_array)[0]
    coeff_array = coeff_array[non_zero_pnts]
    step_array = step_size*grid_pnts[non_zero_pnts]

    if arg_len == 1:
        def fin_diff(arg):
            diff = 0
            for coeff, h in zip(coeff_array, step_array):
                diff += coeff * func(arg + h)
            return diff/step_size**deriv_order

        try:
            fin_diff = njit((arg_type,))(fin_diff)
        except errors.NumbaError as e:
            logging.debug(e, 'Cannot jit compile numerical derivative of {}'.format(func.__name__))

    else:
        arg_select = np.concatenate((np.zeros((arg_idx,)), np.array([1.]), np.zeros((arg_len - arg_idx - 1,))))

        try:
            def fin_diff(*args):
                diff = 0.
                arg_array = np.array(args)
                for coeff, h in zip(coeff_array, step_array):
                    args_k = arg_array + h*arg_select
                    diff += coeff * func(*to_fixed_tuple(args_k, arg_len))
                return diff/step_size**deriv_order

            fin_diff = njit((types.UniTuple(arg_type, arg_len),))(fin_diff)

        except errors.NumbaError as e:
            logging.debug(e, 'Cannot jit compile numerical derivative of {}'.format(func.__name__))

            def fin_diff(*args):
                diff = 0.
                for coeff, h in zip(coeff_array, step_array):
                    diff += coeff * func(*(args + h*arg_select))
                return diff/step_size**deriv_order

    return fin_diff


def gen_fin_diff_coeff(order_deriv, grid_pnts):
    """Reference: Generation of Finite Difference Formulas on Arbitarily Spaced Grids, Bengt Fornberg"""

    num_pnts = len(grid_pnts)
    coef_array = np.zeros((order_deriv + 1, num_pnts, num_pnts))

    if num_pnts <= order_deriv:
        raise RuntimeWarning('Number of grid points should exceed order of derivative')

    coef_array[0, 0, 0] = 1
    c1 = 1
    for n in range(1, num_pnts):
        c2 = 1
        for nu in range(0, n):
            c3 = grid_pnts[n] - grid_pnts[nu]
            c2 *= c3
            for m in range(0,  min(n, order_deriv) + 1):
                coef_array[m, n, nu] = (grid_pnts[n]*coef_array[m, n-1, nu] - m*coef_array[m-1, n-1, nu])/c3

        for m in range(0, min(n, order_deriv) + 1):
            coef_array[m, n, n] = c1/c2*(m*coef_array[m-1, n-1, n-1] - grid_pnts[n-1]*coef_array[m, n-1, n-1])
        c1 = c2

    return coef_array[:, -1, :]
