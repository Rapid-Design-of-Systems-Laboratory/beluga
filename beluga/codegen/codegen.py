import logging
import numpy as np
import sympy
from numba import njit, float64, complex128, errors
from sympy import lambdify
from collections.abc import Iterable, Collection


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
        logging.debug(e)
        logging.debug('Cannot Compile FunctionComponent: {}'.format(func_name))
        print(e)
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

    except errors.NumbaError as e:
        logging.debug(e)
        logging.debug('Cannot Compile FunctionComponent: {}'.format(func_name))
        print(e)
        return func

    except TypeError:
        logging.debug('Cannot Compile FunctionComponent: {} (probably NoneType)'.format(func_name))
        return func


def tuplefy(iter_var):

    if isinstance(iter_var, Iterable):
        iter_var = tuple([tuplefy(item) for item in iter_var])

    return iter_var


class LocalCompiler:
    def __init__(self):
        self.sym_locals = dict()
        self.func_locals = dict()

    def __repr__(self):
        return 'LocalCompiler:\n\tSymbolic Locals: ' + str(self.sym_locals) \
               + '\n\tFunctionComponent Locals: ' + str(self.func_locals)

    def __deepcopy__(self, memodict=None):
        return self

    def add_symbolic_local(self, name, local=None):
        if local is None:
            local = sympy.Symbol(name)
        self.sym_locals[name] = local
        return self.sym_locals

    def sympify(self, expr):
        return sympy.sympify(expr, locals=self.sym_locals)

    def add_function_local(self, name, function):
        self.func_locals[name] = function
        return self.func_locals

    # noinspection PyTypeChecker
    def lambdify(self, args, sym_func, additional_modules=None, array_inputs=True, complex_numbers=False):

        default_modules = ['numpy', 'math']
        if additional_modules is None:
            modules = [self.func_locals] + default_modules
        else:
            modules = [{**self.func_locals, **additional_modules}] + default_modules

        tup_func = tuplefy(sym_func)
        lam_func = sympy.lambdify(args, tup_func, modules)
        jit_func = jit_compile_func(lam_func, args, func_name=repr(sym_func), complex_numbers=complex_numbers)
        return jit_func
