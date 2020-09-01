import numpy as np
import numba
from numba import njit, float64, complex128, types, errors
from numba.unsafe.ndarray import to_fixed_tuple
import logging
import inspect
import itertools


def gen_fin_diff(func, deriv_order=None, step_size=1e-6, acc_order=1, method='central', complex_arg=False):
    arg_len = len(inspect.signature(func).parameters)

    if len(deriv_order) > arg_len:
        raise SyntaxError('Argument index exceeds number of arguments')

    if deriv_order is None:
        deriv_order = tuple([1] + [0 for _ in range(1, arg_len)])

    if complex_arg:
        arg_type = complex128
    else:
        arg_type = float64

    try:
        arg_list = [arg_type] * arg_len

        if type(func) is numba.targets.registry.CPUDispatcher:
            if complex_arg:
                func.disable_compile(False)
                func = func.compile(tuple(arg_list))
        else:
            func = njit(tuple(arg_list))(func)

    except errors.NumbaError as e:
        logging.beluga(e, 'Cannot jit compile {} to compile numerical derivative'.format(func.__name__))

    step_array = []
    coeff_array = []

    # TODO This process can be greatly optimized
    for deriv_order_k in deriv_order:
        num_pnts = deriv_order_k + acc_order

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

        coeff_array_k = gen_fin_diff_coeff(deriv_order_k, grid_pnts)
        non_zero_pnts = np.where(coeff_array_k)[0]
        coeff_array.append(coeff_array_k[non_zero_pnts])
        step_array.append(step_size * grid_pnts[non_zero_pnts])

    coeff_prod = tuple([np.product(out) for out in itertools.product(*coeff_array)])
    step_prod = tuple([out for out in itertools.product(*step_array)])

    total_deriv_order = sum(deriv_order)

    if arg_len == 1:
        coeffs = tuple(coeff_array[0])
        steps = tuple(step_array[0])

        def fin_diff(arg):
            diff = 0
            for coeff, h in zip(coeffs, steps):
                diff += coeff * func(arg + h)
            return diff / step_size ** total_deriv_order

        try:
            fin_diff = njit((arg_type,))(fin_diff)
        except errors.NumbaError as e:
            logging.beluga(e, 'Cannot jit compile numerical derivative of {}'.format(func.__name__))

    else:
        try:
            def fin_diff(*args):
                diff = 0.
                arg_array = np.array(args)
                for coeff, step in zip(coeff_prod, step_prod):
                    args_k = arg_array + np.array(step)
                    diff += coeff * func(*to_fixed_tuple(args_k, arg_len))
                return diff / step_size ** total_deriv_order

            fin_diff = njit((types.UniTuple(arg_type, arg_len),))(fin_diff)

        except errors.NumbaError as e:
            logging.beluga(e, 'Cannot jit compile numerical derivative of {}'.format(func.__name__))

            def fin_diff(*args):
                diff = 0.
                arg_array = np.array(args)
                for coeff, step in zip(coeff_prod, step_prod):
                    diff += coeff * func(*(arg_array + step))
                return diff / step_size ** total_deriv_order

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
            for m in range(0, min(n, order_deriv) + 1):
                coef_array[m, n, nu] = (grid_pnts[n] * coef_array[m, n - 1, nu] - m * coef_array[m - 1, n - 1, nu]) / c3

        for m in range(0, min(n, order_deriv) + 1):
            coef_array[m, n, n] = c1 / c2 * (
                    m * coef_array[m - 1, n - 1, n - 1] - grid_pnts[n - 1] * coef_array[m, n - 1, n - 1])
        c1 = c2

    return coef_array[-1, -1, :]
