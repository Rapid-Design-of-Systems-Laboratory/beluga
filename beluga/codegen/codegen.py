import numba
import functools as ft
import simplepipe as sp
import logging
from sympy.utilities.lambdify import lambdastr
import pystache
import imp
import sympy as sym
import itertools as it
# from beluga.bvpsol.algorithms import Shooting
import beluga
import sys
import numpy as np
from math import *
from beluga.utils import keyboard


def load_eqn_template(problem_data, template_file, renderer = pystache.Renderer(escape=lambda u: u)):
    """
    Loads pystache template and uses it to generate code.

    Parameters
    ----------
        problem_data - dict
            Workspace defining variables for template

        template_file - str
            Path to template file to be used

        renderer
            Renderer used to convert template file to code

    Returns
    -------
    Code generated from template
    """
    template_path = beluga.root()+'/optimlib/templates/'+problem_data['method']+'/'+template_file
    with open(template_path) as f:
        tmpl = f.read()
        # Render the template using the data
        code = renderer.render(tmpl, problem_data)
        return code


def create_module(problem_data):
    """
    Creates a new module for storing compiled code.

    Parameters
    ----------
    problem_data - dict
        Problem data dictionary

    Returns
    -------
    New module for holding compiled code
    """
    problem_name = problem_data['problem_name']
    module = imp.new_module('_beluga_'+problem_name)



    # module.corner_fns = problem_data['corner_fns']
    # module.compute_hamiltonian = problem_data['ham_fn']
    # module.costate_eoms = problem_data['costate_eoms']

    return module


def make_control_and_ham_fn(control_opts, states, costates, parameters, constants, controls, mu_vars, quantity_vars, ham, constraint_name=None):
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


    # control_opt_fn = sym.lambdify(u_args, control_opt_mat)
    # print('Making control fn with args',u_args)
    control_opt_fn = make_sympy_fn(u_args, control_opt_mat)

    # print('Making ham fn with args', ham_args)
    ham_fn = make_sympy_fn(ham_args, ham.subs(quantity_vars))

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
        except Exception as e:
            # print('oh nooes')
            # from beluga.utils import keyboard
            # keyboard()
            raise

            # keyboard()
        ham_val = np.zeros(num_options)
        for i in range(num_options):
            try:
                ham_val[i] = ham_fn(*X, *p, *C, *u_list[i], s_val)
            except:
                print(X, p, C, u_list[i])
                raise
        # if len(ham_val) == 0:
        #     keyboard()
        return u_list[np.argmin(ham_val)]

    yield compute_control_fn
    yield ham_fn


def make_functions(problem_data, module):

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
    control_fn, ham_fn = make_control_and_ham_fn(unc_control_law,states,costates,parameters,constants,controls,mu_vars,quantity_vars,ham)

    # problem_data['ham_fn'] = ham_fn
    module.ham_fn = ham_fn
    control_fns = [control_fn] # Also makethiss
    logging.info('Processing constraints')
    for arc_type, s in enumerate(problem_data['s_list'],1):
        u_fn, ham_fn = make_control_and_ham_fn(s['control_law'], states, costates, parameters, constants, controls, mu_vars, quantity_vars, s['ham'], s['name'])
        control_fns.append(u_fn)

    module.control_fns = control_fns
    module.ham_fn = ham_fn

    yield module
    yield control_fns[0]


def compile_code_py(code_string, module, function_name):
    """
    Compiles a function specified by template in filename and stores it in
    self.compiled

    Parameters
    ----------
    code_string - str
        String containing the python code to be compiled

    module - dict
        Module in which the new functions will be defined

    function_name - str
        Name of the function being compiled (this must be defined in the
        template with the same name)

    Returns:
        Module for compiled function
        Compiled function
    """
    # For security
    module.__dict__.update({'__builtin__': {}})
    exec(code_string, module.__dict__)
    return getattr(module, function_name, None)


def make_njit_fn(args, fn_expr):
    fn_str = lambdastr(args, fn_expr).replace('MutableDenseMatrix', '')\
                                                  .replace('(([[', '[') \
                                                  .replace(']]))', ']')
    jit_fn = numba.njit(parallel=True, nopython=True)(eval(fn_str))
    return jit_fn


def make_sympy_fn(args, fn_expr):
    if hasattr(fn_expr, 'shape'):
        output_shape = fn_expr.shape
    else:
        output_shape = None

    if output_shape is not None:
        jit_fns = [make_njit_fn(args, expr) for expr in fn_expr]
        len_output = len(fn_expr)

        # @numba.jit(parallel=True, nopython=True)
        def vector_fn(*args):
            output = np.zeros(output_shape)
            for i in numba.prange(len_output):
                output.flat[i] = jit_fns[i](*args)
            return output
        return vector_fn
    else:
        return make_njit_fn(args, fn_expr)
