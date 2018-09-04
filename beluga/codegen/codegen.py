import beluga
import collections as cl
import imp
import importlib
import itertools as it
import logging
import numba
import numpy as np
import pystache
import sympy as sym
import sys
from beluga.utils import keyboard

from sympy.utilities.lambdify import lambdastr

# The following import statements *look* unused, but is in fact used by the code compiler. This enables users to use
# various basic math functions like `cos` and `atan`. Do not delete.
from math import *
from numpy import imag as im
from sympy import I #TODO: This doesn't fix complex step derivatives.


def load_eqn_template(problem_data, template_file, renderer = pystache.Renderer(escape=lambda u: u)):
    r"""
    Loads pystache template and uses it to generate code.

    :param problem_data: Workspace defining variables for template.
    :param template_file: Path to template file to be used.
    :param renderer: Renderer used to convert template file to code.
    :return: Code generated from template file.
    """
    template_path = beluga.root()+'/optimlib/templates/'+problem_data['method']+'/'+template_file
    with open(template_path) as f:
        tmpl = f.read()
        # Render the template using the data
        code = renderer.render(tmpl, problem_data)
        return code


def create_module(problem_data):
    r"""
    Creates a new module for storing compiled code.

    :param problem_data: Data structure of an optimal control problem.
    :return: A module for holding compiled code.
    """
    problem_name = problem_data['problem_name']
    module = imp.new_module('_beluga_'+problem_name)

    # Put the custom functions into the newly created code module.
    for func in problem_data['custom_functions']:
        module.__dict__[func['name']] = func['handle']

    return module


def make_control_and_ham_fn(control_opts, states, costates, parameters, constants, controls, mu_vars, quantity_vars, ham, custom_functions, constraint_name=None):
    controls = sym.Matrix([_._sym for _ in controls])
    constants = sym.Matrix([_._sym for _ in constants])
    states = sym.Matrix([_.name for _ in states])
    costates = sym.Matrix([_.name for _ in costates])
    parameters = sym.Matrix(parameters)
    tf_var = sym.sympify('tf')
    unknowns = list(it.chain(controls, mu_vars))
    ham_args = [*states, *costates, *parameters, *constants, *unknowns]
    u_args = [*states, *costates, *parameters, *constants]

    if constraint_name is not None:
        ham_args.append(constraint_name)
        u_args.append(constraint_name)
    else:
        ham_args.append('___dummy_arg___')
        u_args.append('___dummy_arg___')
    control_opt_mat = sym.Matrix([[option.get(u, '0')
                                   for u in unknowns]
                                  for option in control_opts])

    control_opt_fn = make_sympy_fn(u_args, control_opt_mat, custom_functions)


    # print('Making ham fn with args', ham_args)
    ham_fn = make_sympy_fn(ham_args, ham.subs(quantity_vars), custom_functions)

    num_unknowns = len(unknowns)
    num_options = len(control_opts)
    num_states = len(states)
    num_params = len(parameters)
    constraint_name = str(constraint_name)

    def compute_control_fn(t, X, p, aux):
        X = X[:(2*num_states+1)]
        C = aux['const'].values()
        p = p[:num_params]
        s_val = aux['constraint'].get((constraint_name, 1), -1)

        try:
            u_list = control_opt_fn(*X, *p, *C, s_val)
        except Exception as e: # TODO: When is this error ever thrown?
            raise
        ham_val = np.zeros(num_options)
        for i in range(num_options):
            try:
                ham_val[i] = ham_fn(*X, *p, *C, *u_list[i], s_val)
            except:
                print(X, p, C, u_list[i])
                raise

        return u_list[np.argmin(ham_val)]

    yield compute_control_fn
    yield ham_fn


def make_functions(problem_data, module):
    custom_functions = problem_data['custom_functions']
    unc_control_law = problem_data['control_options']
    states = problem_data['states']
    costates = problem_data['costates']
    parameters = problem_data['parameters']
    constants = problem_data['constants']
    controls = problem_data['controls']
    mu_vars = problem_data['mu_vars']
    quantity_vars = problem_data['quantity_vars']
    ham = problem_data['ham']

    logging.info('Making unconstrained control')
    control_fn, ham_fn = make_control_and_ham_fn(unc_control_law,states,costates,parameters,constants,controls,mu_vars,quantity_vars, ham, custom_functions)

    module.ham_fn = ham_fn
    control_fns = [control_fn] # Also makethiss
    logging.info('Processing constraints')
    for arc_type, s in enumerate(problem_data['s_list'],1):
        u_fn, ham_fn = make_control_and_ham_fn(s['control_law'], states, costates, parameters, constants, controls, mu_vars, quantity_vars, s['ham'], custom_functions, s['name'])
        control_fns.append(u_fn)

    module.control_fns = control_fns
    module.ham_fn = ham_fn

    yield module
    yield control_fns[0]


def compile_code_py(code_string, module, function_name):
    r"""
    Compiles a function specified by template in filename and stores it in a module.

    :param code_string: String containing the python code to be compiled.
    :param module: Module in which the new functions will be defined.
    :param function_name: Name of the function being compiled (this must be defined in the template with the same name).
    :return: module: A module for the compiled function.
    """
    # For security
    module.__dict__.update({'__builtin__': {}})
    exec(code_string, module.__dict__)
    return getattr(module, function_name, None)


def make_jit_fn(args, fn_expr, custom_functions, nopython=False):
    fn_str = lambdastr(args, fn_expr).replace('MutableDenseMatrix', '') \
        .replace('(([[', '[') \
        .replace(']]))', ']')

    f = eval(fn_str)
    jit_fn = numba.jit(nopython=nopython)(eval(fn_str))
    jit_fn(*np.ones(len(args)))
    return jit_fn


def make_sympy_fn(args, fn_expr, custom_functions):
    if hasattr(fn_expr, 'shape'):
        output_shape = fn_expr.shape
    else:
        output_shape = None

    if output_shape is not None:
        jit_fns = [make_jit_fn(args, expr, custom_functions) for expr in fn_expr]
        len_output = len(fn_expr)

        # @numba.jit(parallel=True, nopython=True)
        def vector_fn(*args):
            output = np.zeros(output_shape)
            for i in numba.prange(len_output):
                output.flat[i] = jit_fns[i](*args)
            return output
        return vector_fn
    else:
        return make_jit_fn(args, fn_expr, custom_functions, nopython=False)


def preprocess(problem_data, use_numba=False):
    r"""
    Code generation and compilation before running solver.

    :param problem_data:
    :param use_numba:
    :return: Code module.
    """
    out_ws = dict()
    custom_functions = problem_data['custom_functions']
    # Register custom functions as global functions
    for f in custom_functions:
        globals()[f['name']] = f['handle']
    code_module = create_module(problem_data)
    code_module, compute_control_fn = make_functions(problem_data, code_module)
    out_ws['code_module'] = code_module
    deriv_func_code = load_eqn_template(problem_data, template_file='deriv_func.py.mu')
    bc_func_code = load_eqn_template(problem_data, template_file='bc_func.py.mu')
    deriv_func_fn = compile_code_py(deriv_func_code, code_module, 'deriv_func')
    bc_func_fn = compile_code_py(bc_func_code, code_module, 'bc_func')
    out_ws['deriv_func_code'] = deriv_func_code
    out_ws['bc_func_code'] = bc_func_code
    logging.debug(out_ws['bc_func_code'])
    logging.debug(out_ws['deriv_func_code'])
    if use_numba:
        deriv_func = numba.njit(parallel=False, nopython=True)(code_module.deriv_func_nojit)
    else:
        deriv_func = code_module.deriv_func_nojit

    deriv_func_fn = deriv_func
    code_module.deriv_func = deriv_func
    out_ws['code_module'].deriv_func = deriv_func

    bvp = BVP(deriv_func_fn, bc_func_fn, compute_control_fn)

    sys.modules['_beluga_' + problem_data['problem_name']] = out_ws['code_module']
    return out_ws['code_module'], bvp


BVP = cl.namedtuple('BVP', 'deriv_func bc_func compute_control')
