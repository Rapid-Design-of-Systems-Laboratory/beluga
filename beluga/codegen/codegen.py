import logging
import numba
import re
import sympy
from autograd import grad
from autograd import numpy as np

# The following import statements *look* unused, but is in fact used by the code compiler. This enables users to use
# various basic math functions like `cos` and `atan`. Do not delete.
import math
from math import *


def make_control_and_ham_fn(control_opts, states, parameters, constants, controls, ham):
    r"""
    Makes the control and Hamiltonian functions.

    :param control_opts: Control options.
    :param states: List of states.
    :param parameters: List of parameters.
    :param constants: List of constants.
    :param controls: List of controls.
    :param ham: The Hamiltonian function.
    :return: (compute_control_fn, hamiltonian_fn) - Functions that compute the optimal control and the Hamiltonian.
    """
    ham_args = [*states, *parameters, *constants, *controls]
    u_args = [*states, *parameters, *constants]
    control_opt_mat = [[option.get(u, '0') for u in controls] for option in control_opts]

    u_str = 'np.array(['
    for ii in range(len(control_opts)):
        if ii > 0:
            u_str += ','
        u_str += '['
        u_str += ','.join(control_opt_mat[ii])
        u_str += ']'

    u_str += '])'
    control_opt_fn = make_jit_fn(u_args, u_str)

    hamiltonian_fn = make_sympy_fn(ham_args, ham)
    num_options = len(control_opts)
    num_states = len(states)
    num_controls = len(controls)
    num_params = len(parameters)

    if num_controls > 0:
        def compute_control_fn(X, u, p, C):
            p = p[:num_params]
            u_list = np.array(control_opt_fn(*X, *p, *C))
            # u_list = ucont_wrap(*X, *p, *C)
            ham_val = np.zeros(num_options)

            for i in range(num_options):
                ham_val[i] = hamiltonian_fn(*X, *p, *C, *u_list[i])

            return u_list[np.argmin(ham_val)]
    else:
        def compute_control_fn(X, u, p, C):
            return np.array([])

    return compute_control_fn, hamiltonian_fn


def make_cost_func(initial_cost, path_cost, terminal_cost, states, parameters, constants, controls):
    r"""
    Makes the cost function.

    :param initial_cost: Initial cost function.
    :param path_cost: Path cost function.
    :param terminal_cost: Terminal cost function.
    :param states: List of states.
    :param parameters: List of parameters.
    :param constants: List of constants.
    :param controls: List of controls.
    :return: (initial_cost, path_cost, terminal_cost) - Functions for the 3 cost functions.
    """
    boundary_args = [*states, *parameters, *constants, *controls]
    path_args = [*states, *parameters, *constants, *controls]
    initial_fn = make_jit_fn(boundary_args, initial_cost)
    path_fn = make_jit_fn(path_args, path_cost)
    terminal_fn = make_jit_fn(boundary_args, terminal_cost)

    def initial_cost(X0, u0, p, C):
        return initial_fn(*X0, *p, *C, *u0)

    def path_cost(X, u, p, C):
        return path_fn(*X, *p, *C, *u)

    def terminal_cost(Xf, uf, p, C):
        return terminal_fn(*Xf, *p, *C, *uf)

    return initial_cost, path_cost, terminal_cost


def make_constraint_func(path_constraints, states, parameters, constants, controls):
    r"""
    Makes the path constraint functions.

    :param path_constraints: List of path constraints.
    :param states: List of states.
    :param parameters: List of parameters.
    :param constants: List of constants.
    :param controls: List of controls.
    :return: path_constraints - Function for the path constraints.
    """
    path_args = [*states, *parameters, *constants, *controls]
    path_fn = [make_jit_fn(path_args, f) for f in path_constraints]
    num_constraints = len(path_constraints)

    def path_constraints(X, u, p, C):
        constraint_vals = np.zeros(num_constraints)
        for ii in range(num_constraints):
            constraint_vals[ii] = path_fn[ii](*X, *p, *C, *u)
        return constraint_vals

    return path_constraints


def make_deriv_func(deriv_list, states, parameters, constants, controls, compute_control):
    r"""
    Makes the derivative functions for each state.

    :param deriv_list: A list of derivative functions.
    :param states: List of states.
    :param parameters: List of parameters.
    :param constants: List of constants.
    :param controls: List of controls.
    :param compute_control: The compute_control function.
    :return: deriv_func - The derivative function.
    """
    ham_args = [*states, *parameters, *constants, *controls]
    eom_fn = make_jit_fn(ham_args, '(' + ','.join(deriv_list) + ')')
    num_controls = len(controls)
    num_params = len(parameters)
    num_eoms = len(deriv_list)

    if compute_control is not None:
        def deriv_func(X, u, p, C):
            p = p[:num_params]
            u = compute_control(X, u, p, C)
            eom_vals = eom_fn(*X, *p, *C, *u)
            return eom_vals
    else:
        def deriv_func(X, u, p, C):
            p = p[:num_params]
            eom_vals = eom_fn(*X, *p, *C, *u)
            return eom_vals

    return deriv_func


def make_quad_func(quads_rates, states, quads, parameters, constants, controls, compute_control):
    r"""
    Makes the derivative functions for each quad.

    :param quads_rates: A list of derivative functions.
    :param states: List of states.
    :param quads: List of quads.
    :param parameters: List of parameters.
    :param constants: List of constants.
    :param controls: List of controls.
    :param compute_control: The compute_control function.
    :return: quad_func - The derivative function.
    """
    quads_args = [*states, *parameters, *constants, *controls]
    quad_fn = [make_sympy_fn(quads_args, eom) for eom in quads_rates]

    num_controls = len(controls)
    num_params = len(parameters)
    num_quads = len(quad_fn)
    if num_quads == 0:
        def dummy_quad_func(*_, **__):
            return np.array([])
        return dummy_quad_func

    def quad_func(X, u, p, C):
        p = p[:num_params]
        u = compute_control(X, u, p, C)
        quad_vals = np.zeros(num_quads)
        for ii in range(num_quads):
            quad_vals[ii] = quad_fn[ii](*X, *p, *C, *u)

        return quad_vals

    return quad_func


def make_bc_func(bc_initial, bc_terminal, states, quads, dynamical_parameters, nondynamical_parameters, constants,
                 controls, compute_control):
    r"""
    Makes the boundary condition functions.

    :param bc_initial: Initial boundary conditions.
    :param bc_terminal: Terminal boundary conditions.
    :param states: List of states.
    :param quads: List of quads.
    :param dynamical_parameters: List of dynamical parameters.
    :param nondynamical_parameters: List of nondynamical parameters.
    :param constants: List of constants.
    :param controls: List of controls.
    :param compute_control: The compute_control function.
    :return: bc_func - The boundary condition function.
    """
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
        def bc_func_all(X0, q0, u0, Xf, qf, uf, params, ndp, C):
            bc_vals = np.zeros(num_bcs_initial + num_bcs_terminal)
            ii = 0
            for jj in range(num_bcs_initial):
                bc_vals[ii] = bc_fn_initial[jj](*X0, *q0, *params, *ndp, *C, *u0)
                ii += 1

            for jj in range(num_bcs_terminal):
                bc_vals[ii] = bc_fn_terminal[jj](*Xf, *qf, *params, *ndp, *C, *uf)
                ii += 1

            return bc_vals

        def bc_func(y0, q0, u0, yf, qf, uf, p, ndp, C):
            u0 = compute_control(y0, u0, p, C)
            uf = compute_control(yf, uf, p, C)
            return bc_func_all(y0, q0, u0, yf, qf, uf, p, ndp, C)

    else:
        def bc_func(X0, q0, u0, Xf, qf, uf, params, ndp, C):
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
    r"""
    Main process that generates callable functions from the problem data.

    :param problem_data: Problem data from optimlib.
    :returns: (deriv_func, quad_func, bc_func, control_fn, ham_fn, initial_cost, path_cost, terminal_cost, ineq_constraints) - Several functions to define a BVP.
    """
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

    path_constraints = problem_data['path_constraints']

    ham = problem_data['hamiltonian']
    logging.info('Making unconstrained control')
    if problem_data['method'] is not 'direct':
        control_fn, ham_fn = make_control_and_ham_fn(unc_control_law, states, dynamical_parameters,
                                                     constants, controls, ham)

        def initial_cost(*_, **__):
            return 0

        def path_cost(*_, **__):
            return 0

        def terminal_cost(*_, **__):
            return 0
    else:
        def control_fn(X, u, p, C):
            return u
        ham_fn = None
        initial_cost, path_cost, terminal_cost = make_cost_func(initial_cost, path_cost, terminal_cost, states,
                                                                dynamical_parameters, constants, controls)

    if problem_data['method'] is not 'direct' and len(path_constraints) > 0:
        raise NotImplementedError('Path constraints not implemented for indirect-type methods.')
    else:
        ineq_constraints = make_constraint_func(path_constraints, states, dynamical_parameters, constants, controls)

    logging.info('Making derivative function and bc function')
    deriv_list = problem_data['states_rates']

    deriv_func = make_deriv_func(deriv_list, states, dynamical_parameters, constants, controls, control_fn)
    quad_func = make_quad_func(quads_rates, states, quads, dynamical_parameters, constants, controls, control_fn)
    bc_initial = problem_data['bc_initial']
    bc_terminal = problem_data['bc_terminal']
    bc_func = make_bc_func(bc_initial, bc_terminal, states, quads, dynamical_parameters, nondynamical_parameters,
                           constants, controls, control_fn)

    return deriv_func, quad_func, bc_func, control_fn, ham_fn, initial_cost, path_cost, terminal_cost, ineq_constraints


def make_jit_fn(args, fn_expr):
    r"""
    JIT compiles a string function to a callable function.

    :param args: Arguments taken by the string function.
    :param fn_expr: The string function.
    :return: A callable function.
    """
    fn_str = 'lambda ' + ','.join([a for a in args]) + ':' + fn_expr

    f = eval(fn_str)
    try:
        jit_fn = numba.jit(nopython=True)(f)
        jit_fn(*np.ones(len(args), dtype=float))
    except numba.errors.UnsupportedError:
        logging.info(fn_str + ' can not be jit compiled. Defaulting to uncompiled evaluation.')
        jit_fn = f

    return jit_fn


def make_sympy_fn(args, fn_expr):
    r"""
    JIT compiles a sympy function to a callable function.

    :param args: Arguments taken by the SymPy function.
    :param fn_expr: The SymPy function.
    :return: A callable function.
    """
    if hasattr(fn_expr, 'shape'):
        output_shape = fn_expr.shape
    else:
        output_shape = None

    if output_shape is not None:
        jit_fns = [make_jit_fn(args, str(expr)) for expr in fn_expr]
        len_output = len(fn_expr)

        def vector_fn(*_):
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

    :param problem_data: Problem data from optimlib.
    :return: A BVP.
    """
    # Register custom functions as global functions
    custom_functions = problem_data['custom_functions']
    for ii, f in enumerate(custom_functions):
        derivs = []
        for jj, arg in enumerate(f['args']):
            if len(f['derivs']) == len(f['args']) and f['derivs'][jj] is not None:
                derivs += [f['derivs'][jj]]
            else:
                derivs += [grad(f['handle'], jj)]
        custom_functions[ii]['derivative'] = derivs

    for ii, f in enumerate(custom_functions):
        globals()[f['name']] = f['handle']
        for jj, g in enumerate(f['derivative']):
            globals()[f['name'] + '_d' + f['args'][jj]] = g

    if len(custom_functions) > 0:
        new_states = []
        for state_rate in problem_data['states_rates']:
            s = sympy.sympify(state_rate)
            derivs = s.atoms(sympy.Derivative)
            for deriv in derivs:
                name = re.sub('[\\(\\[].*?[\\)\\]]', '', str(deriv.expr))
                dx = deriv.args[1]
                name += '_d' + str(dx[0])
                df = sympy.Function(name)(*deriv.expr.args)
                s = s.subs(deriv, df)
            new_states += [str(s)]

        problem_data['states_rates'] = new_states

    deriv_func, quad_func, bc_func, compute_control, ham_fn, initial_cost, path_cost, terminal_cost, ineq_constraints\
        = make_functions(problem_data)

    bvp = BVP(deriv_func, quad_func, bc_func, compute_control, initial_cost, path_cost, terminal_cost, ineq_constraints)

    return bvp


class BVP(object):
    def __init__(self, *args, **__):
        self.deriv_func = args[0]
        self.quad_func = args[1]
        self.bc_func = args[2]
        self.compute_control = args[3]
        self.initial_cost = args[4]
        self.path_cost = args[5]
        self.terminal_cost = args[6]
        self.ineq_constraints = args[7]
        self.raw = dict()

    def __repr__(self):
        return 'BVP Object'
