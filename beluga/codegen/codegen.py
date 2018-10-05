import collections as cl
import logging
import numba
import numpy as np
import sympy as sym

from sympy.utilities.lambdify import lambdastr

# The following import statements *look* unused, but is in fact used by the code compiler. This enables users to use
# various basic math functions like `cos` and `atan`. Do not delete.
import math
from math import *
from numpy import imag as im
from sympy import I #TODO: This doesn't fix complex step derivatives.


def make_control_and_ham_fn(control_opts, states, costates, parameters, constants, controls, quantity_vars, ham, is_icrm=False):
    controls = sym.Matrix([_._sym for _ in controls])
    constants = sym.Matrix([_._sym for _ in constants])
    states = sym.Matrix([_.name for _ in states])
    costates = sym.Matrix([_.name for _ in costates])
    parameters = sym.Matrix(parameters)
    unknowns = list(controls)
    ham_args = [*states, *costates, *parameters, *constants, *unknowns]
    u_args = [*states, *costates, *parameters, *constants]

    control_opt_mat = sym.Matrix([[option.get(u, '0')
                                   for u in unknowns]
                                  for option in control_opts])

    control_opt_fn = make_sympy_fn(u_args, control_opt_mat)
    ham_fn = make_sympy_fn(ham_args, ham.subs(quantity_vars))

    num_options = len(control_opts)
    num_states = len(states)
    num_params = len(parameters)
    if is_icrm:
        def compute_control_fn(t, X, p, aux):
            return X[num_states*2:]
    else:
        def compute_control_fn(t, X, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            u_list = control_opt_fn(*X, *p, *C)
            ham_val = np.zeros(num_options)
            for i in range(num_options):
                ham_val[i] = ham_fn(*X, *p, *C, *u_list[i])

            return u_list[np.argmin(ham_val)]

    return compute_control_fn, ham_fn


def make_deriv_func(deriv_list, states, costates, parameters, constants, controls, quantity_vars, compute_control, is_icrm=False):
    controls = sym.Matrix([_._sym for _ in controls])
    constants = sym.Matrix([_._sym for _ in constants])
    states = sym.Matrix([_.name for _ in states])
    costates = sym.Matrix([_.name for _ in costates])
    parameters = sym.Matrix(parameters)
    unknowns = list(controls)
    ham_args = [*states, *costates, *parameters, *constants, *unknowns]

    eom_fn = [make_sympy_fn(ham_args, eom.subs(quantity_vars)) for eom in deriv_list]

    num_states = len(states)
    num_params = len(parameters)
    num_eoms = len(eom_fn)

    if is_icrm:
        def deriv_func(t, X, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            u = compute_control(t, X, p, aux)
            eom_vals = np.zeros(num_eoms)
            _X = X[:2*num_states]
            for ii in range(num_eoms):
                eom_vals[ii] = eom_fn[ii](*_X, *p, *C, *u)

            return eom_vals
    else:
        def deriv_func(t, X, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            u = compute_control(t, X, p, aux)
            eom_vals = np.zeros(num_eoms)
            for ii in range(num_eoms):
                eom_vals[ii] = eom_fn[ii](*X, *p, *C, *u)

            return eom_vals

    return deriv_func

def make_bc_func(bc_initial, bc_terminal, states, costates, dynamical_parameters, nondynamical_parameters, constants, controls, quantity_vars, compute_control, ham_fn, constraint_name=None, is_icrm=False):
    controls = sym.Matrix([_._sym for _ in controls])
    constants = sym.Matrix([_._sym for _ in constants])
    states = sym.Matrix([_.name for _ in states])
    costates = sym.Matrix([_.name for _ in costates])
    dynamical_parameters = sym.Matrix(dynamical_parameters)
    unknowns = list(controls)
    ham_args = [*states, *costates, *dynamical_parameters, *constants, *unknowns]
    u_args = [*states, *costates, *dynamical_parameters, *constants]
    if constraint_name is not None:
        ham_args.append(constraint_name)
        u_args.append(constraint_name)
    else:
        ham_args.append('___dummy_arg___')
        u_args.append('___dummy_arg___')
    num_states = len(states)
    num_dynamical_params = len(dynamical_parameters)
    num_nondynamical_params = len(nondynamical_parameters)
    constraint_name = str(constraint_name)

    def bc_func_left(_y, u, p, ndp, aux, bcf=bc_initial):
        C = aux['const'].values()
        p = p[:num_dynamical_params]
        _x0 = aux['initial']
        _xf = aux['terminal']
        ham_args_num = (*_y, *p, *C, *u)
        _H = ham_fn(*ham_args_num)
        ii = 0
        for a in states:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in costates:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in dynamical_parameters:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in constants:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in unknowns:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        ii = 0
        for a in nondynamical_parameters:
            exec(str(a) + ' = ' + 'ndp[' + str(ii) + ']')
            ii += 1

        bc = []
        for s in bcf:
            exec('bc.append(' + s + ')')

        return np.array(bc)

    def bc_func_right(_y, u, p, ndp, aux, bcf=bc_terminal):
        C = aux['const'].values()
        p = p[:num_dynamical_params]
        _x0 = aux['initial']
        _xf = aux['terminal']
        ham_args_num = (*_y, *p, *C, *u)
        _H = ham_fn(*ham_args_num)
        ii = 0
        for a in states:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in costates:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in dynamical_parameters:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in constants:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        for a in unknowns:
            exec(str(a) + ' = ' + 'ham_args_num[' + str(ii) + ']')
            ii += 1

        ii = 0
        for a in nondynamical_parameters:
            exec(str(a) + ' = ' + 'ndp[' + str(ii) + ']')
            ii += 1

        bc = []
        for s in bcf:
            exec('bc.append(' + s + ')')

        return np.array(bc)

    if is_icrm:
        def bc_func(t0, y0, q0, tf, yf, qf, p, ndp, aux):
            u0 = compute_control(t0, y0, p, aux)
            uf = compute_control(tf, yf, p, aux)
            res_left = bc_func_left(y0[:2*num_states], u0, p, ndp, aux)
            res_right = bc_func_right(yf[:2*num_states], uf, p, ndp, aux)
            return np.hstack((res_left, res_right))
    else:
        def bc_func(t0, y0, q0, tf, yf, qf, p, ndp, aux):
            u0 = compute_control(t0, y0, p, aux)
            uf = compute_control(tf, yf, p, aux)
            res_left = bc_func_left(y0, u0, p, ndp, aux)
            res_right = bc_func_right(yf, uf, p, ndp, aux)
            return np.hstack((res_left.flatten(), res_right.flatten()))

    return bc_func


def make_functions(problem_data):
    unc_control_law = problem_data['control_options']
    states = problem_data['states']
    costates = problem_data['costates']
    nondynamical_parameters = problem_data['nondynamical_parameters']
    dynamical_parameters = problem_data['dynamical_parameters']
    constants = problem_data['constants']
    controls = problem_data['controls']
    quantity_vars = problem_data['quantity_vars']
    is_icrm = problem_data['method'].lower() == 'icrm'
    ham = problem_data['hamiltonian']
    logging.info('Making unconstrained control')
    control_fn, ham_fn = make_control_and_ham_fn(unc_control_law, states, costates, dynamical_parameters, constants, controls, quantity_vars, ham, is_icrm=is_icrm)

    logging.info('Making derivative function and bc function')
    deriv_list = problem_data['deriv_list']

    deriv_func = make_deriv_func(deriv_list, states, costates, dynamical_parameters, constants, controls, quantity_vars, control_fn, is_icrm=is_icrm)

    bc_initial = problem_data['bc_initial']
    bc_terminal = problem_data['bc_terminal']
    bc_func = make_bc_func(bc_initial, bc_terminal, states, costates, dynamical_parameters, nondynamical_parameters, constants, controls, quantity_vars, control_fn, ham_fn, is_icrm=is_icrm)

    return deriv_func, bc_func, control_fn, ham_fn


def make_jit_fn(args, fn_expr):
    fn_str = lambdastr(args, fn_expr).replace('MutableDenseMatrix', '') \
        .replace('(([[', '[') \
        .replace(']]))', ']')

    f = eval(fn_str)
    try:
        jit_fn = numba.jit(nopython=True)(f)
        jit_fn(*np.ones(len(args), dtype=float))
    except:
        jit_fn = f
    return jit_fn


def make_sympy_fn(args, fn_expr):
    if hasattr(fn_expr, 'shape'):
        output_shape = fn_expr.shape
    else:
        output_shape = None

    if output_shape is not None:
        jit_fns = [make_jit_fn(args, expr) for expr in fn_expr]
        len_output = len(fn_expr)

        def vector_fn(*args):
            output = np.zeros(output_shape)
            for i in numba.prange(len_output):
                output.flat[i] = jit_fns[i](*args)
            return output
        return vector_fn
    else:
        return make_jit_fn(args, fn_expr)


def preprocess(problem_data):
    r"""
    Code generation and compilation before running solver.

    :param problem_data:
    :param use_numba:
    :return: Code module.
    """
    # Register custom functions as global functions
    custom_functions = problem_data['custom_functions']
    for f in custom_functions:
        globals()[f['name']] = f['handle']
    deriv_func, bc_func, compute_control, ham_fn = make_functions(problem_data)

    bvp = BVP(deriv_func, bc_func, compute_control)

    return bvp


BVP = cl.namedtuple('BVP', 'deriv_func bc_func compute_control')
