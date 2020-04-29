import logging
import numpy as np
import sympy
from numba import njit, float64, complex128, errors
from sympy import lambdify
from collections.abc import Iterable


def jit_lambdify(args, sym_func, array_inputs=True, complex_numbers=False):

    mods = ['numpy', 'math']

    tup_func = tuplefy(sym_func)
    lam_func = lambdify(args, tup_func, mods)
    jit_func = jit_compile_func(lam_func, len(args),
                                func_name=repr(sym_func), complex_numbers=complex_numbers, array_inputs=array_inputs)

    return jit_func


def jit_compile_func(func, num_args, func_name=None, complex_numbers=False, array_inputs=True):
    if func_name is None:
        if hasattr(func, 'name'):
            func_name = func.__name__

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
        logging.debug('Cannot Compile Function: {}'.format(func_name))
        print(e)
        return func

    except TypeError:
        logging.debug('Cannot Compile Function: {} (probably NoneType)'.format(func_name))
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
               + '\n\tFunction Locals: ' + str(self.func_locals)

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
        jit_func = jit_compile_func(lam_func, len(args), func_name=repr(sym_func),
                                    complex_numbers=complex_numbers, array_inputs=array_inputs)
        return jit_func


def compile_control(control_options, hamiltonioan, controls, states, parameters, constants,
                    local_compiler=LocalCompiler()):

    num_options = len(control_options)

    if num_options == 0:
        def calc_u(_, __, ___):
            return None

    elif num_options == 1:
        calc_u = local_compiler.lambdify([states, parameters, constants], control_options[0])

    else:
        compiled_options = local_compiler.lambdify([states, parameters, constants], control_options)
        ham_func = local_compiler.lambdify([states, controls, parameters, constants], hamiltonioan)

        def calc_u(x, p, k):

            u_set = np.array(compiled_options(x, p, k))

            u = u_set[0, :]
            ham = ham_func(x, u_set[0, :], p, k)

            for n in range(1, num_options):
                ham_i = ham_func(x, u_set[n, :], p, k)
                if ham_i < ham:
                    u, ham = u_set[n, :], ham_i

            return u

    control_function = jit_compile_func(calc_u, 3, func_name='control_function')

    return control_function
