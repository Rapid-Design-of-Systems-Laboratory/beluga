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


def make_control_and_ham_fn(control_opts, states, parameters, constants, controls, ham, is_icrm=False):
    ham_args = [*states, *parameters, *constants, *controls]
    u_args = [*states, *parameters, *constants]
    control_opt_mat = [[option.get(u, '0') for u in controls] for option in control_opts]

    u_str = '['
    for ii in range(len(control_opts)):
        if ii > 0:
            u_str += ','
        u_str += '['
        u_str += ','.join(control_opt_mat[ii])
        u_str += ']'

    u_str += ']'
    control_opt_fn = make_jit_fn(u_args, u_str)

    ham_fn = make_sympy_fn(ham_args, ham)
    num_options = len(control_opts)
    num_states = len(states)
    num_controls = len(controls)
    num_params = len(parameters)
    if is_icrm:
        def compute_control_fn(t, X, p, aux):
            return X[-num_controls:]
    else:
        def compute_control_fn(t, X, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            u_list = np.array(control_opt_fn(*X, *p, *C))
            ham_val = np.zeros(num_options)
            for i in range(num_options):
                ham_val[i] = ham_fn(*X, *p, *C, *u_list[i])

            return u_list[np.argmin(ham_val)]

    return compute_control_fn, ham_fn


def make_cost_func(initial_cost, path_cost, terminal_cost, states, parameters, constants, controls):
    boundary_args = [*states, *parameters, *constants, *controls]
    initial_fn = make_jit_fn(boundary_args, initial_cost)
    path_rn = make_jit_fn(boundary_args, path_cost)
    terminal_fn = make_jit_fn(boundary_args, terminal_cost)
    def initial_cost(t0, X0, q0, u0, p, aux):
        C = aux['const'].values()
        return initial_fn(*X0, *p, *C, *u0)

    def path_cost(t, X, q, u, p, aux):
        C = aux['const'].values()
        return path_rn(*X, *p, *C, *u)

    def terminal_cost(tf, Xf, qf, uf, p, aux):
        C = aux['const'].values()
        return terminal_fn(*Xf, *p, *C, *uf)

    return initial_cost, path_cost, terminal_cost


def make_deriv_func(deriv_list, states, parameters, constants, controls, compute_control, is_icrm=False):
    ham_args = [*states, *parameters, *constants, *controls]
    eom_fn = make_jit_fn(ham_args, '(' + ','.join(deriv_list) + ')')

    num_controls = len(controls)
    num_params = len(parameters)
    num_eoms = len(deriv_list)

    if compute_control is not None:
        if is_icrm:
            def deriv_func(t, X, p, aux):
                C = aux['const'].values()
                p = p[:num_params]
                u = compute_control(t, X, p, aux)
                _X = X[:-num_controls]
                eom_vals = eom_fn(*_X, *p, *C, *u)
                return eom_vals
        else:
            def deriv_func(t, X, p, aux):
                C = aux['const'].values()
                p = p[:num_params]
                u = compute_control(t, X, p, aux)
                u = compute_control(t, X, p, aux)
                eom_vals = eom_fn(*X, *p, *C, *u)
                return eom_vals
    else:
        def deriv_func(t, X, u, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            eom_vals = eom_fn(*X, *p, *C, *u)
            return eom_vals

    return deriv_func


def make_quad_func(quads_rates, states, quads, parameters, constants, controls, compute_control, is_icrm=False):
    quads_args = [*states, *parameters, *constants, *controls]
    quad_fn = [make_sympy_fn(quads_args, eom) for eom in quads_rates]

    num_controls = len(controls)
    num_params = len(parameters)
    num_quads = len(quad_fn)
    if num_quads == 0:
        def dummy_quad_func(*args, **kwargs):
            return np.array([])
        return dummy_quad_func

    if is_icrm:
        def quad_func(t, X, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            u = compute_control(t, X, p, aux)
            quads_vals = np.zeros(num_quads)
            _X = X[:-num_controls]
            for ii in range(num_quads):
                quads_vals[ii] = quad_fn[ii](*_X, *p, *C, *u)

            return quads_vals
    else:
        def quad_func(t, X, p, aux):
            C = aux['const'].values()
            p = p[:num_params]
            u = compute_control(t, X, p, aux)
            quad_vals = np.zeros(num_quads)
            for ii in range(num_quads):
                quad_vals[ii] = quad_fn[ii](*X, *p, *C, *u)

            return quad_vals

    return quad_func


def make_bc_func(bc_initial, bc_terminal, states, quads, dynamical_parameters, nondynamical_parameters, constants, controls, compute_control, is_icrm=False):
    ham_args = [*states, *dynamical_parameters, *constants, *controls]
    u_args = [*states, *dynamical_parameters, *constants]
    bc_args = [*states, *quads, *dynamical_parameters, *nondynamical_parameters, *constants, *controls]
    num_states = len(states)
    num_controls = len(controls)
    num_dynamical_params = len(dynamical_parameters)
    num_nondynamical_params = len(nondynamical_parameters)
    bc = bc_terminal[-1]
    bc_fn_initial = [make_jit_fn(bc_args, bc) for bc in bc_initial]
    bc_fn_terminal = [make_jit_fn(bc_args, bc) for bc in bc_terminal]
    num_bcs_initial = len(bc_fn_initial)
    num_bcs_terminal = len(bc_fn_terminal)
    if compute_control is not None:
        def bc_func_all(t0, X0, q0, u0, tf, Xf, qf, uf, params, ndp, aux):
            C = aux['const'].values()
            bc_vals = np.zeros(num_bcs_initial + num_bcs_terminal)
            ii = 0
            for jj in range(num_bcs_initial):
                bc_vals[ii] = bc_fn_initial[jj](*X0, *q0, *params, *ndp, *C, *u0)
                ii += 1

            for jj in range(num_bcs_terminal):
                bc_vals[ii] = bc_fn_terminal[jj](*Xf, *qf, *params, *ndp, *C, *uf)
                ii += 1

            return bc_vals

        if is_icrm:
            def bc_func(t0, y0, q0, tf, yf, qf, p, ndp, aux):
                u0 = compute_control(t0, y0, p, aux)
                uf = compute_control(tf, yf, p, aux)
                return bc_func_all(t0, y0[:-num_controls], q0, u0, tf, yf[:-num_controls], qf, uf, p, ndp, aux)
        else:
            def bc_func(t0, y0, q0, tf, yf, qf, p, ndp, aux):
                u0 = compute_control(t0, y0, p, aux)
                uf = compute_control(tf, yf, p, aux)
                return bc_func_all(t0, y0, q0, u0, tf, yf, qf, uf, p, ndp, aux)

    else:
        def bc_func(t0, X0, q0, u0, tf, Xf, qf, uf, params, ndp, aux):
            C = aux['const'].values()
            bc_vals = np.zeros(num_bcs_initial + num_bcs_terminal)
            ii = 0
            for jj in range(num_bcs_initial):
                bc_vals[ii] = bc_fn_initial[jj](*X0, *q0, *params, *ndp, *C, *u0)
                ii += 1

            for jj in range(num_bcs_terminal):
                bc_vals[ii] = bc_fn_terminal[jj](*Xf, *qf, *params, *ndp, *C, *uf)
                ii += 1

            return bc_vals

    return bc_func


def make_functions(problem_data):
    unc_control_law = problem_data['control_options']
    states = problem_data['states']
    quads = problem_data['quads']
    quads_rates = problem_data['quads_rates']
    nondynamical_parameters = problem_data['nondynamical_parameters']
    dynamical_parameters = problem_data['dynamical_parameters']
    constants = problem_data['constants']
    controls = problem_data['controls']
    initial_cost = problem_data['initial_cost']
    path_cost = problem_data['path_cost']
    terminal_cost = problem_data['terminal_cost']
    is_icrm = problem_data['method'].lower() == 'icrm'
    ham = problem_data['hamiltonian']
    logging.info('Making unconstrained control')
    if problem_data['method'] is not 'direct':
        control_fn, ham_fn = make_control_and_ham_fn(unc_control_law, states, dynamical_parameters, constants, controls, ham, is_icrm=is_icrm)
        def initial_cost(*args, **kwargs):
            return 0
        def path_cost(*args, **kwargs):
            return 0
        def terminal_cost(*args, **kwargs):
            return 0
    else:
        control_fn = None
        ham_fn = None
        initial_cost, path_cost, terminal_cost = make_cost_func(initial_cost, path_cost, terminal_cost, states, dynamical_parameters, constants, controls)

    logging.info('Making derivative function and bc function')
    deriv_list = problem_data['deriv_list']

    deriv_func = make_deriv_func(deriv_list, states, dynamical_parameters, constants, controls, control_fn, is_icrm=is_icrm)
    quad_func = make_quad_func(quads_rates, states, quads, dynamical_parameters, constants, controls, control_fn, is_icrm=is_icrm)
    bc_initial = problem_data['bc_initial']
    bc_terminal = problem_data['bc_terminal']
    bc_func = make_bc_func(bc_initial, bc_terminal, states, quads, dynamical_parameters, nondynamical_parameters, constants, controls, control_fn, is_icrm=is_icrm)

    return deriv_func, quad_func, bc_func, control_fn, ham_fn, initial_cost, path_cost, terminal_cost


def make_jit_fn(args, fn_expr):
    fn_str = 'lambda ' + ','.join([a for a in args]) + ':' + fn_expr
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
        jit_fns = [make_jit_fn(args, str(expr)) for expr in fn_expr]
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
    deriv_func, quad_func, bc_func, compute_control, ham_fn, initial_cost, path_cost, terminal_cost = make_functions(problem_data)

    bvp = BVP(deriv_func, quad_func, bc_func, compute_control)

    return bvp, initial_cost, path_cost, terminal_cost


BVP = cl.namedtuple('BVP', 'deriv_func quad_func bc_func compute_control')
