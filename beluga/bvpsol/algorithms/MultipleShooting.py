# from autodiff import Function, Gradient
import numpy as np

import beluga
from .. import Solution
from beluga.utils import keyboard, timeout
from beluga.integrators import ode45
from .BaseAlgorithm import BaseAlgorithm
from beluga.problem import BVP
from sympy.utilities.lambdify import lambdastr
import numba

from math import *
import logging
import imp
import functools as ft
import itertools as it
import sympy as sym
import pystache

import simplepipe as sp
import math

def make_njit_fn(args, fn_expr):
    fn_str = lambdastr(args, fn_expr).replace('MutableDenseMatrix', '')\
                                                  .replace('(([[', '[') \
                                                  .replace(']]))', ']')
    jit_fn = numba.njit(parallel=True)(eval(fn_str))
    return jit_fn

def make_sympy_fn(args, fn_expr):
    if hasattr(fn_expr, 'shape'):
        output_shape = fn_expr.shape
    else:
        output_shape = None

    if output_shape is not None:
        jit_fns = [make_njit_fn(args, expr) for expr in fn_expr]
        len_output = len(fn_expr)
        # @numba.njit(parallel=True)
        @numba.jit(parallel=True)
        def vector_fn(*args):
            output = np.zeros(output_shape)
            for i in numba.prange(len_output):
                output.flat[i] = jit_fns[i](*args)
            return output
        return vector_fn
    else:
        return make_njit_fn(args, fn_expr)

def load_eqn_template(problem_data, template_file,
                        renderer = pystache.Renderer(escape=lambda u: u)):
    """Loads pystache template and uses it to generate code.

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
    """Creates a new module for storing compiled code.

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

    ham_args = [*states, *costates, tf_var, *parameters, *constants, *unknowns]
    u_args = [*states, *costates, tf_var, *parameters, *constants]

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

    print('Making unconstrained control')
    control_fn, ham_fn = make_control_and_ham_fn(unc_control_law,states,costates,parameters,constants,controls,mu_vars,quantity_vars,ham)

    # problem_data['ham_fn'] = ham_fn
    module.ham_fn = ham_fn
    control_fns = [control_fn] # Also makethiss
    print('Processing constraints')
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
    module.__dict__.update({'__builtin__':{}})
    exec(code_string, module.__dict__)
    return getattr(module,function_name)

PythonCodeGen = sp.Workflow([
    # Create module for holding compiled code
    sp.Task(ft.partial(create_module), inputs='problem_data', outputs=('code_module')),

    sp.Task(make_functions, inputs=('problem_data', 'code_module'), outputs=('code_module','compute_control_fn')),
    # Load equation template files and generate code
    sp.Task(ft.partial(load_eqn_template,
                template_file='deriv_func.py.mu'),
            inputs='problem_data',
            outputs='deriv_func_code'),
    sp.Task(ft.partial(load_eqn_template,
                template_file='bc_func.py.mu'),
            inputs='problem_data',
            outputs='bc_func_code'),

    # Compile generated code
    sp.Task(ft.partial(compile_code_py, function_name='deriv_func'),
            inputs=['deriv_func_code', 'code_module'],
            outputs='deriv_func_fn'),
    sp.Task(ft.partial(compile_code_py, function_name='bc_func'),
            inputs=['bc_func_code', 'code_module'],
            outputs='bc_func_fn'),
], description='Generates and compiles the required BVP functions from problem data')

class MultipleShooting(BaseAlgorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, max_error=10, derivative_method='fd', verbose=True):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.max_error = max_error
        self.derivative_method = derivative_method
        if derivative_method not in ['fd']:
            raise ValueError("Invalid derivative method specified. Valid options are 'csd' and 'fd'.")

    def preprocess(self, problem_data):
        """Code generation and compilation before running solver."""
        out_ws = PythonCodeGen({'problem_data': problem_data})
        print(out_ws['bc_func_code'])
        print(out_ws['deriv_func_code'])
        self.bvp = BVP(out_ws['deriv_func_fn'],
                       out_ws['bc_func_fn'], out_ws['compute_control_fn'])#out_ws['compute_control_fn'])

        self.stm_ode_func = ft.partial(self._stmode_fd, odefn=self.bvp.deriv_func)
        self.bc_jac_multi  = ft.partial(self.__bc_jac_multi, bc_func=self.bvp.bc_func)
        return out_ws['code_module']

    def bc_jac_params():
        P = np.zeros((nBCs, p.size))
        ya = np.array(ya, ndmin=1)
        yb = np.array(yb, ndmin=1)

        # if parameters is not None:
        p  = np.array(parameters)
        h = StepSize

        nOdes = ya.shape[0]

        fx = bc_func(ya,yb,p,aux)
        nBCs = len(fx)
        for i in range(p.size):
            p[i] = p[i] + h
            f = bc_func(ya,yb,p,aux)
            P[:,i] = (f-fx)/h
            p[i] = p[i] - h
        J = np.hstack((M+np.dot(N,phi),P))

    def __bc_jac_multi(self, nBCs, phi_list, ya, yb, parameters, aux, bc_func, StepSize=1e-6):

        # if parameters is not None:
        p  = np.array(parameters)
        h = StepSize

        nOdes = ya.shape[0]
        num_arcs = len(phi_list)

        fx = bc_func(ya,yb,p,aux)
        nBCs = len(fx)

        M = np.zeros((nBCs, nOdes))
        N = np.zeros((nBCs, nOdes))
        P = np.zeros((nBCs, p.size))

        J = np.zeros((nBCs, (nOdes)*num_arcs+p.size))
        J_num_cols = nOdes

        for arc_idx, phi in zip(it.count(), phi_list):
            # Evaluate for all arcs
            for i in range(nOdes):
                ya[i, arc_idx] = ya[i, arc_idx] + h
                f = bc_func(ya,yb,p,aux)
                M[:,i] = (f-fx)/h
                ya[i, arc_idx] = ya[i, arc_idx] - h

                yb[i, arc_idx] = yb[i, arc_idx] + h
                f = bc_func(ya,yb,p,aux)
                N[:,i] = (f-fx)/h
                yb[i, arc_idx] = yb[i, arc_idx] - h

            J_i = M+N @ phi
            J_slice = slice(nOdes*arc_idx, nOdes*(arc_idx+1))
            J[:,J_slice] = J_i

        for i in range(p.size):
            p[i] = p[i] + h
            f = bc_func(ya,yb,p,aux)
            P[:,i] = (f-fx)/h
            p[i] = p[i] - h

        J[:,nOdes*num_arcs:] = P
        return J


    def _stmode_fd(self, x, y, p, aux, arc_idx, odefn, StepSize=1e-7,show=False):
        "Finite difference version of state transition matrix"
        N = y.shape[0]
        nOdes = int(0.5*(sqrt(4*N+1)-1))

        phi = y[nOdes:].reshape((nOdes, nOdes)) # Convert STM terms to matrix form
        Y = np.array(y[0:nOdes], copy=True)  # Just states
        F = np.zeros((nOdes,nOdes))

        # Compute Jacobian matrix, F using finite difference
        fx = odefn(x,Y,p,aux,arc_idx)
        if show:
            print(x, fx, self.bvp.deriv_func(x,Y,p,aux,arc_idx))
            from beluga.utils import keyboard
            keyboard()
        if np.any(np.isnan(fx)):
            print('NAAAAAAAAAAAN')
            from beluga.utils import keyboard
            keyboard()

        Yh = y[:nOdes] + np.eye(nOdes)*StepSize
        for i,y_h in enumerate(Yh):
            # Y[i] = Y[i] + StepSize
            F[:,i] = (odefn(x, y_h, p,aux,arc_idx)-fx)/StepSize
            # Y[i] = Y[i] - StepSize

        # Phidot = F*Phi (matrix product)
        phiDot = F @ phi
        return np.hstack( (fx, np.reshape(phiDot, (nOdes*nOdes) )) )

    def solve(self,solinit):
        """Solve a two-point boundary value problem
            using the single shooting method

        Args:
            deriv_func: the ODE function
            bc_func: the boundary conditions function
            solinit: a "Solution" object containing the initial guess
        Returns:
            solution of TPBVP
        Raises:
        """
        x  = solinit.x
        # Get initial states from the guess structure
        y0g = solinit.y[:,0]
        paramGuess = solinit.parameters

        deriv_func = self.bvp.deriv_func
        bc_func = self.bvp.bc_func

        aux = solinit.aux
        # Only the start and end times are required for ode45
        arcs = solinit.arcs

        if arcs is None:
            arcs = [(0, len(solinit.x)-1)]
            solinit.arcs = arcs

        arc_seq = aux['arc_seq']
        num_arcs = len(arc_seq)
        if len(arcs) % 2 == 0:
            raise Exception('Number of arcs must be odd!')

        left_idx, right_idx = map(np.array, zip(*arcs))
        ya = solinit.y[:,left_idx]
        yb = solinit.y[:,right_idx]

        tmp = np.arange(num_arcs+1, dtype=np.float32)
        tspan_list = [(a, b) for a, b in zip(tmp[:-1], tmp[1:])]
        # Extract number of ODEs in the system to be solved
        nOdes = y0g.shape[0]
        if solinit.parameters is None:
            nParams = 0
        else:
            nParams = solinit.parameters.size

        # Initial state of STM is an identity matrix
        stm0 = np.eye(nOdes).reshape(nOdes*nOdes)
        n_iter = 1            # Initialize iteraiton counter
        converged = False   # Convergence flag

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None

        y0stm = np.zeros((len(stm0)+nOdes))
        yb = np.zeros_like(ya)
        try:
            while True:
                phi_list = []
                with timeout(seconds=10):
                    for arc_idx, tspan in enumerate(tspan_list):
                        y0stm[:nOdes] = ya[:,arc_idx]
                        y0stm[nOdes:] = stm0[:]
                        # print(arc_idx, tspan, ya[:,arc_idx])

                        t,yy = ode45(self.stm_ode_func, tspan, y0stm, paramGuess, aux, arc_idx, abstol=1e-6, reltol=1e-4)
                        # tt,yy2 = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-8, reltol=1e-4)
                        # _,yy2 = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-8, reltol=1e-3)
                        yb[:,arc_idx] = yy[-1,:nOdes]
                        phi = np.reshape(yy[-1,nOdes:],(nOdes, nOdes)) # STM
                        phi_list.append(np.copy(phi))

                # Iterate through arcs
                if n_iter>self.max_iterations:
                    logging.warn("Maximum iterations exceeded!")
                    break

                res = bc_func(ya, yb, paramGuess, aux)
                if any(np.isnan(res)):
                    print(res)
                    raise RuntimeError("Nan in residue")
                r1 = np.linalg.norm(res)
                if self.verbose:
                    logging.debug('Residue: '+str(r1))

                if r1 > self.max_error:
                    raise RuntimeError('Error exceeded max_error')

                # Solution converged if BCs are satisfied to tolerance
                if r1 <= self.tolerance:
                    if self.verbose:
                        logging.info("Converged in "+str(n_iter)+" iterations.")
                    converged = True
                    break

                # Compute Jacobian of boundary conditions using numerical derviatives
                nBCs = len(res)
                J = self.bc_jac_multi(nBCs, phi_list, ya, yb, paramGuess, aux)
                # Compute correction vector

                if r0 is not None:
                    # if r1/r0 > 2:
                    #     logging.error('Residue increased more than 2x in one iteration!')
                    #     break
                    beta = (r0-r1)/(alpha*r0)
                    if beta < 0:
                        beta = 1
                if r1>1:
                    alpha = 1/(2*r1)
                else:
                    alpha = 1
                r0 = r1

                # No damping if error within one order of magnitude
                # of tolerance
                if r1 < 10*self.tolerance:
                    alpha, beta = 1, 1

                try:
                    dy0 = alpha*beta*np.linalg.solve(J,-res)
                except:
                    keyboard()
                    rank1 = np.linalg.matrix_rank(J)
                    rank2 = np.linalg.matrix_rank(np.c_[J,-res])
                    if rank1 == rank2:
                        # dy0 = alpha*beta*np.dot(np.linalg.pinv(J),-res)
                        dy0 = -alpha*beta*(np.linalg.inv(J @ J.T) @ J).T @ res
                        # dy0 = -alpha*beta*np.dot( np.linalg.inv(np.dot(J.T,J)), J.T  )
                    else:
                        # Re-raise exception if system is infeasible
                        raise
                # dy0 = -alpha*beta*np.dot(np.dot(np.linalg.inv(np.dot(J,J.T)),J).T,res)

                # Apply corrections to states and parameters (if any)
                d_ya = np.reshape(dy0[:nOdes*num_arcs], (nOdes, num_arcs), order='F')
                if nParams > 0:
                    dp = dy0[nOdes*num_arcs:]
                    paramGuess += dp
                    ya = ya + d_ya
                else:
                    ya = ya + d_ya

                n_iter += 1
                logging.debug('Iteration #'+str(n_iter))
        # except KeyboardInterrupt as ke:
        #     converged = False
        except Exception as e:
            logging.warn(e)
            import traceback
            traceback.print_exc()


        # Return initial guess if it failed to converge
        sol = solinit
        if converged:
            y_list = []
            x_list = []
            sol.arcs = []
            y0 = np.zeros(ya.shape[0])
            timestep_ctr = 0
            for arc_idx, tspan in enumerate(tspan_list):
                tt,yy = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-6, reltol=1e-4)
                y_list.append(yy.T)
                x_list.append(tt)
                sol.arcs.append((timestep_ctr, timestep_ctr+len(tt)-1))
                timestep_ctr += len(tt)

            # If problem converged, propagate solution to get full trajectory
            sol.x = np.hstack(x_list)
            sol.y = np.column_stack(y_list)
            sol.parameters = paramGuess

        sol.converged = converged
        sol.aux = aux
        return sol
