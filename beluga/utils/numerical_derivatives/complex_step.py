import numpy as np
import beluga.utils.numerical_derivatives.finite_diff
import math
import numba
from numba import njit, float64, complex128, types, errors
from numba.unsafe.ndarray import to_fixed_tuple
import logging
import inspect


def gen_csd(func, deriv_order=None, step_size=1e-6, complex_arg=False):

    if max(deriv_order) > 2:
        logging.debug('Complex-step derivative not supported for order > 2.'
                      ' Falling back to finite difference for {}'.format(func.__name__))
        return beluga.utils.numerical_derivatives.gen_fin_diff(func, deriv_order=deriv_order, step_size=step_size)

    if len(np.nonzero(deriv_order)[0]) > 1:
        logging.debug('Complex-step derivative not supported for multivariate derivatives.'
                      ' Falling back to finite difference for {}'.format(func.__name__))
        return beluga.utils.numerical_derivatives.gen_fin_diff(func, deriv_order=deriv_order, step_size=step_size)
    else:
        arg_idx = np.nonzero(deriv_order)[0][0]
        deriv_order = max(deriv_order)

    arg_len = len(inspect.signature(func).parameters)

    if arg_idx > arg_len:
        raise SyntaxError('Argument index exceeds number of arguments')

    if complex_arg:
        arg_type = complex128
    else:
        arg_type = float64

    try:
        arg_list_re = [float64] * arg_len
        arg_list_im = [complex128] * arg_len
        if type(func) is numba.targets.registry.CPUDispatcher:
            func.disable_compile(False)
            func_re = func.compile(tuple(arg_list_re))
            func_im = func.compile(tuple(arg_list_im))
        else:
            func_re = njit(tuple(arg_list_re))(func)
            func_im = njit(tuple(arg_list_im))(func)

    except errors.NumbaError as e:
        logging.debug(e, 'Cannot jit compile {} to compile numeric derivative'.format(func.__name__))

    if arg_len == 1:
        if deriv_order == 1:
            step = 1e-50

            def csd(arg):
                return func_im(arg + step*1j).imag/step

        else:
            # On generalization of ... (94)
            im_step_size = math.sqrt(3 + 2*math.sqrt(2))*step_size

            def csd(arg):
                return 2*(func_re(arg + step_size) - (func_im(arg + step_size - im_step_size * 1j)).real) \
                       / im_step_size**2

        try:
            csd = njit((arg_type,))(csd)
        except errors.NumbaError as e:
            logging.debug(e, 'Cannot jit compile numeric derivative of {}'.format(func.__name__))

    else:
        arg_select = np.concatenate((np.zeros((arg_idx,), dtype=float), np.array([1.]),
                                     np.zeros((arg_len - arg_idx - 1,), dtype=float)))

        try:
            if deriv_order == 1:
                step = 1e-50

                def csd(*args):
                    args_k = np.array(args) + step*1j*arg_select
                    return func_im(*to_fixed_tuple(args_k, arg_len)).imag/step

            else:
                im_step_size = math.sqrt(3 + 2 * math.sqrt(2)) * step_size
                step_re = step_size * arg_select
                step_im = (step_size - im_step_size * 1j) * arg_select

                def csd(*args):
                    args_array = np.array(args)
                    args_k_re = args_array + step_re
                    args_k_im = args_array + step_im
                    return 2 * (func_re(*to_fixed_tuple(args_k_re, arg_len)) -
                                func_im(*to_fixed_tuple(args_k_im, arg_len))).real / im_step_size ** 2

            csd = njit((types.UniTuple(arg_type, arg_len),))(csd)

        except errors.NumbaError as e:
            logging.debug(e, 'Cannot jit compile numeric derivative of {}'.format(func.__name__))

            if deriv_order == 1:
                step = 1e-50

                def csd(*args):
                    args_k = np.array(args) + step * 1j * arg_select
                    return func_im(*to_fixed_tuple(args_k, arg_len)) / step

            else:
                im_step_size = math.sqrt(3 + 2 * math.sqrt(2)) * step_size
                step_re = step_size * arg_select
                step_im = (step_size - im_step_size * 1j) * arg_select

                def csd(*args):
                    args_array = np.array(args)
                    args_k_re = args_array + step_re
                    args_k_im = args_array + step_im
                    return 2 * (func_re(*args_k_re) - func_im(*args_k_im)).real / im_step_size ** 2

    return csd
