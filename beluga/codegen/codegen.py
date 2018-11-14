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


def make_control_and_ham_fn(control_opts, states, parameters, constants, controls, quantity_vars, ham, is_icrm=False):
    controls = sym.Matrix([_ for _ in controls])
    constants = sym.Matrix([_ for _ in constants])
    states = sym.Matrix([_ for _ in states])
    parameters = sym.Matrix(parameters)
    unknowns = list(controls)
    ham_args = [*states, *parameters, *constants, *unknowns]
    u_args = [*states, *parameters, *constants]

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
            return X[num_states:]
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


def make_deriv_func(deriv_list, states, parameters, constants, controls, quantity_vars, compute_control, is_icrm=False):
    controls = sym.Matrix([_ for _ in controls])
    constants = sym.Matrix([_ for _ in constants])
    states = sym.Matrix([_ for _ in states])
    parameters = sym.Matrix(parameters)
    unknowns = list(controls)
    ham_args = [*states, *parameters, *constants, *unknowns]

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
            _X = X[:num_states]
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

def make_bc_func(bc_initial, bc_terminal, states, dynamical_parameters, nondynamical_parameters, constants, controls, quantity_vars, compute_control, ham_fn, is_icrm=False):
    controls = sym.Matrix([_ for _ in controls])
    constants = sym.Matrix([_ for _ in constants])
    states = sym.Matrix([_ for _ in states])
    dynamical_parameters = sym.Matrix(dynamical_parameters)
    unknowns = list(controls)
    ham_args = [*states, *dynamical_parameters, *constants, *unknowns]
    u_args = [*states, *dynamical_parameters, *constants]
    bc_args = [*states, *dynamical_parameters, *nondynamical_parameters, *constants, *unknowns]
    num_states = len(states)
    num_dynamical_params = len(dynamical_parameters)
    num_nondynamical_params = len(nondynamical_parameters)
    bc = bc_terminal[-1]
    bc_fn_initial = [make_jit_fn(bc_args, bc) for bc in bc_initial]
    bc_fn_terminal = [make_jit_fn(bc_args, bc) for bc in bc_terminal]
    num_bcs_initial = len(bc_fn_initial)
    num_bcs_terminal = len(bc_fn_terminal)

    def bc_func_all(t0, X0, q0, u0, tf, Xf, qf, uf, params, ndp, aux):
        C = aux['const'].values()
        bc_vals = np.zeros(num_bcs_initial + num_bcs_terminal)
        ii = 0
        for jj in range(num_bcs_initial):
            bc_vals[ii] = bc_fn_initial[jj](*X0, *params, *ndp, *C, *u0)
            ii += 1

        for jj in range(num_bcs_terminal):
            bc_vals[ii] = bc_fn_terminal[jj](*Xf, *params, *ndp, *C, *uf)
            ii += 1

        return bc_vals

    if is_icrm:
        def bc_func(t0, y0, q0, tf, yf, qf, p, ndp, aux):
            u0 = compute_control(t0, y0, p, aux)
            uf = compute_control(tf, yf, p, aux)
            return bc_func_all(t0, y0[:num_states], q0, u0, tf, yf[:num_states], qf, uf, p, ndp, aux)
    else:
        def bc_func(t0, y0, q0, tf, yf, qf, p, ndp, aux):
            u0 = compute_control(t0, y0, p, aux)
            uf = compute_control(tf, yf, p, aux)
            return bc_func_all(t0, y0, q0, u0, tf, yf, qf, uf, p, ndp, aux)

    return bc_func


def make_functions(problem_data):
    unc_control_law = problem_data['control_options']
    states = problem_data['state_list']
    nondynamical_parameters = problem_data['nondynamical_parameters']
    dynamical_parameters = problem_data['dynamical_parameters']
    constants = problem_data['constants']
    controls = problem_data['controls']
    quantity_vars = problem_data['quantity_vars']
    is_icrm = problem_data['method'].lower() == 'icrm'
    ham = problem_data['hamiltonian']
    logging.info('Making unconstrained control')
    control_fn, ham_fn = make_control_and_ham_fn(unc_control_law, states, dynamical_parameters, constants, controls, quantity_vars, ham, is_icrm=is_icrm)

    logging.info('Making derivative function and bc function')
    deriv_list = problem_data['deriv_list']

    deriv_func = make_deriv_func(deriv_list, states, dynamical_parameters, constants, controls, quantity_vars, control_fn, is_icrm=is_icrm)

    bc_initial = problem_data['bc_initial']
    bc_terminal = problem_data['bc_terminal']
    bc_func = make_bc_func(bc_initial, bc_terminal, states, dynamical_parameters, nondynamical_parameters, constants, controls, quantity_vars, control_fn, ham_fn, is_icrm=is_icrm)

    return deriv_func, bc_func, control_fn, ham_fn


def make_jit_fn(args, fn_expr):
    fn_str = 'lambda ' + ','.join([str(a) for a in args]) + ':' + str(fn_expr)
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
