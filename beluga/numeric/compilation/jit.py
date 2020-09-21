import logging
from numba import njit, float64, complex128, errors
from sympy import lambdify
from typing import Collection, Iterable

from beluga.utils.utils import tuplefy


def jit_lambdify(args, sym_func, complex_numbers=False):

    mods = ['numpy', 'math']

    tup_func = tuplefy(sym_func)
    lam_func = lambdify(args, tup_func, mods)
    jit_func = jit_compile_func(lam_func, args, func_name=repr(sym_func), complex_numbers=complex_numbers)

    return jit_func


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
        logging.beluga('Cannot Compile FunctionComponent: {}\n\tError: {}'.format(func_name, e))
        return func

    except TypeError:
        logging.beluga('Cannot Compile FunctionComponent: {} (probably NoneType)'.format(func_name))
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
