# from autodiff import Function, Gradient

import numpy as np

from .. import Solution
from .BaseAlgorithm import BaseAlgorithm
from math import *
from beluga.utils import keyboard
# from joblib import Memory
from .Propagator import Propagator
from .Worker import Worker
import logging, sys, os


try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except ImportError:
    HPCSUPPORTED = 0

import beluga
from .. import Solution
from beluga.utils import keyboard
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

class MultipleShooting_mike(BaseAlgorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, max_error=100, derivative_method='fd', cache_dir = None,verbose=False,cached=True,number_arcs=-1):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.max_error = max_error
        self.derivative_method = derivative_method
        if derivative_method == 'csd':
            self.stm_ode_func = self.__stmode_csd
            self.bc_jac_func  = self.__bcjac_fd
        elif derivative_method == 'fd':
            self.stm_ode_func = self.__stmode_fd
            self.bc_jac_func  = self.__bcjac_fd
        else:
            raise ValueError("Invalid derivative method specified. Valid options are 'csd' and 'fd'.")
        self.cached = cached
        if cached and cache_dir is not None:
            self.set_cache_dir(cache_dir)
        self.number_arcs = number_arcs

        # TODO: Implement the host worker in a nicer way
        # Start Host MPI process
        # self.worker = Worker(mode='HOST')
        # self.worker.startWorker()
        # self.worker.Propagator.setSolver(solver='ode45')
        self.worker = None

    def preprocess(self, problem_data):
        """Code generation and compilation before running solver."""
        out_ws = PythonCodeGen({'problem_data': problem_data})
        print(out_ws['bc_func_code'])
        print(out_ws['deriv_func_code'])
        self.bvp = BVP(out_ws['deriv_func_fn'],
                       out_ws['bc_func_fn'], out_ws['compute_control_fn'])#out_ws['compute_control_fn'])

        self.stm_ode_func = ft.partial(self.__stmode_fd, odefn=self.bvp.deriv_func)
        self.bc_jac_func  = ft.partial(self.__bcjac_fd, bc_func=self.bvp.bc_func)
        return out_ws['code_module']

    def set_cache_dir(self,cache_dir):
        self.cache_dir = cache_dir
        # if self.cached and cache_dir is not None:
        #     memory = Memory(cachedir=cache_dir, mmap_mode='r', verbose=0)
        #     self.solve = memory.cache(self.solve)

    def __bcjac_csd(self, bc_func, ya, yb, phi, parameters, aux, StepSize=1e-50):
        ya = np.array(ya, dtype=complex)
        yb = np.array(yb, dtype=complex)
        # if parameters is not None:
        p  = np.array(parameters, dtype=complex)
        h = StepSize

        nOdes = ya[0].shape[0]
        nBCs = nOdes + nOdes*(self.number_arcs - 1)
        if parameters is not None:
            nBCs += parameters.size

        fx = bc_func(ya,yb,parameters,aux)

        M = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        N = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        J = [None for _ in range(self.number_arcs)]
        for arc in range(self.number_arcs):
            for i in range(nOdes):
                ya[arc][i] += h*1j
                f = bc_func(ya,yb,p,aux)
                M[arc][:,i] = np.imag(f)/h
                ya[arc][i] -= h*1j

                yb[arc][i] += h*1j
                f = bc_func(ya,yb,p,aux)
                N[arc][:,i] = np.imag(f)/h
                yb[arc][i] -= h*1j
            J[arc] = M[arc]+np.dot(N[arc],phi[arc])

        if parameters is not None:
            P = np.zeros((nBCs, p.size))
            for i in range(p.size):
                p[i] = p[i] + h*1j
                f = bc_func(ya,yb,p,aux)
                P[:,i] = np.imag(f)/h
                p[i] = p[i] - h*1j
            J.append(P)

        J = np.hstack(J)
        return J

    def __bcjac_fd(self, bc_func, ya, yb, phi, parameters, aux, StepSize=1e-6):
        # if parameters is not None:
        p  = np.array(parameters)
        h = StepSize

        nOdes = ya[0].shape[0]
        nBCs = nOdes + nOdes*(self.number_arcs - 1)
        if parameters is not None:
            nBCs += parameters.size

        fx = bc_func(ya,yb,parameters,aux)

        M = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        N = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        J = [None for _ in range(self.number_arcs)]
        for arc in range(self.number_arcs):
            for i in range(nOdes):
                ya[arc][i] += h
                f = bc_func(ya,yb,p,aux)
                M[arc][:,i] = (f-fx)/h
                ya[arc][i] -= h

                yb[arc][i] += h
                f = bc_func(ya,yb,p,aux)
                N[arc][:,i] = (f-fx)/h
                yb[arc][i] -= h
            J[arc] = M[arc]+np.dot(N[arc],phi[arc])

        if parameters is not None:
            P = np.zeros((nBCs, p.size))
            for i in range(p.size):
                p[i] = p[i] + h
                f = bc_func(ya,yb,p,aux)
                P[:,i] = (f-fx)/h
                p[i] = p[i] - h
            J.append(P)

        J = np.hstack(J)
        return J

    def __stmode_fd(self, x, y, odefn, parameters, aux, nOdes = 0, StepSize=1e-6):
        "Finite difference version of state transition matrix"
        N = y.shape[0]
        nOdes = int(0.5*(sqrt(4*N+1)-1))

        phi = y[nOdes:].reshape((nOdes, nOdes)) # Convert STM terms to matrix form
        Y = np.array(y[0:nOdes])  # Just states
        F = np.zeros((nOdes, nOdes))

        # Compute Jacobian matrix, F using finite difference
        fx = (odefn(x, Y, parameters, aux)).real
        for i in range(nOdes):
            Y[i] += StepSize
            F[:, i] = (odefn(x, Y, parameters, aux) - fx).real/StepSize
            Y[i] -= StepSize

        phiDot = np.dot(F, phi)
        return np.concatenate((fx, np.reshape(phiDot, (nOdes*nOdes))))

    def __stmode_csd(self, x, y, odefn, parameters, aux, StepSize=1e-100):
        "Complex step version of State Transition Matrix"
        N = y.shape[0]
        nOdes = int(0.5 * (sqrt(4 * N + 1) - 1))

        phi = y[nOdes:].reshape((nOdes, nOdes))  # Convert STM terms to matrix form
        Y = np.array(y[0:nOdes], dtype=complex)  # Just states
        F = np.zeros((nOdes, nOdes))

        # Compute Jacobian matrix, F using finite difference
        for i in range(nOdes):
            Y[i] += StepSize * 1.j
            F[:, i] = np.imag(odefn(x, Y, parameters, aux)) / StepSize
            Y[i] -= StepSize * 1.j

        # Phidot = F*Phi (matrix product)
        phiDot = np.dot(F, phi)
        return np.concatenate((odefn(x, y, parameters, aux), np.reshape(phiDot, (nOdes * nOdes))))

    # def __stmode_ad(self, x, y, odefn, parameters, aux, nOdes = 0, StepSize=1e-50):
    #     "Automatic differentiation version of State Transition Matrix"
    #     phi = y[nOdes:].reshape((nOdes, nOdes)) # Convert STM terms to matrix form
    #     # Y = np.array(y[0:nOdes],dtype=complex)  # Just states
    #     # F = np.zeros((nOdes,nOdes))
    #     # # Compute Jacobian matrix using complex step derivative
    #     # for i in range(nOdes):
    #     #     Y[i] = Y[i] + StepSize*1.j
    #     #     F[:,i] = np.imag(odefn(x, Y, parameters, aux))/StepSize
    #     #     Y[i] = Y[i] - StepSize*1.j
    #     f = Function(odefn)
    #     g = Gradient(odefn)
    #
    #     # Phidot = F*Phi (matrix product)
    #     # phiDot = np.real(np.dot(F,phi))
    #     phiDot = np.real(np.dot(g(x,y,paameters,aux),phi))
    #     # return np.concatenate( (odefn(x,y, parameters, aux), np.reshape(phiDot, (nOdes*nOdes) )) )
    #     return np.concatenate( f(x,y,parameters,aux), np.reshape(phiDot, (nOdes*nOdes) ))


    # @staticmethod
    # def ode_wrap(func,*args, **argd):
    #    def func_wrapper(x,y0):
    #        return func(x,y0,*args,**argd)
    #    return func_wrapper

    def get_bc(self,ya,yb,p,aux):
        f1 = self.bc_func(ya[0],yb[-1],p,aux)
        for i in range(self.number_arcs-1):
            nextbc = yb[i]-ya[i+1]
            f1 = np.concatenate((f1,nextbc)).astype(np.float64)
        return f1

    def solve(self,solinit):
        """Solve a two-point boundary value problem
            using the multiple shooting method

        Args:
            deriv_func: the ODE function
            bc_func: the boundary conditions function
            solinit: a "Solution" object containing the initial guess
        Returns:
            solution of TPBVP
        Raises:
        """
        guess = solinit
        if self.number_arcs == 1:
            # Single Shooting
            from .SingleShooting import SingleShooting
            Single = SingleShooting(self.tolerance, self.max_iterations, self.derivative_method, self.cache_dir, self.verbose, self.cached)
            return Single.solve(bvp)

        if self.worker is not None:
            ode45 = self.worker.Propagator
        else:
            # Start local pool
            ode45 = Propagator(solver='ode45',process_count=self.number_arcs)
            ode45.startPool()

        # Decrease time step if the number of arcs is greater than the number of indices
        if self.number_arcs >= len(guess.x):
            x,ynew = ode45.solve(self.bvp.deriv_func, np.linspace(guess.x[0],guess.x[-1],self.number_arcs+1), guess.y[:,0], guess.parameters, guess.aux, abstol=self.tolerance/10, reltol=1e-3)
            guess.y = np.transpose(ynew)
            guess.x = x

        solinit = guess
        x = solinit.x
        # Get initial states from the guess structure

        y0g = [solinit.y[:,np.floor(i/self.number_arcs*x.shape[0]).astype(np.int32)] for i in range(self.number_arcs)]
        paramGuess = solinit.parameters

        deriv_func = self.bvp.deriv_func
        self.bc_func =self. bvp.bc_func
        aux = solinit.aux
        # Only the start and end times are required for ode45
        t0 = x[0]
        tf = x[-1]
        t = x

        # Extract number of ODEs in the system to be solved
        nOdes = solinit.y.shape[0]

        # Initial state of STM is an identity matrix
        stm0 = np.eye(nOdes).reshape(nOdes*nOdes)

        if solinit.parameters is None:
            nParams = 0
        else:
            nParams = solinit.parameters.size

        iter = 1            # Initialize iteration counter
        converged = False   # Convergence flag

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None
        phiset = [np.eye(nOdes) for i in range(self.number_arcs)]
        tspanset = [np.empty(t.shape[0]) for i in range(self.number_arcs)]

        tspan = [t0,tf]

        try:
            while True:
                if iter>self.max_iterations:
                    logging.warn("Maximum iterations exceeded!")
                    break
                # keyboard
                y0set = [np.concatenate( (y0g[i], stm0) ) for i in range(self.number_arcs)]

                for i in range(self.number_arcs):
                    left = int(np.floor(i/self.number_arcs*t.shape[0]))
                    right = int(np.floor((i+1)/self.number_arcs*t.shape[0]))
                    if i == self.number_arcs-1:
                        right = t.shape[0] - 1
                    print(left,right,len(t))
                    tspanset[i] = [t[left],t[right]]
                    #tspanset[i] = np.linspace(t[left],t[right],np.ceil(5000/self.number_arcs))

                # Propagate STM and original system together
                tset,yySTM = ode45.solve(self.stm_ode_func, tspanset, y0set, deriv_func, paramGuess, aux, abstol=self.tolerance/10, reltol=1e-5)

                # Obtain just last timestep for use with correction
                yf = [yySTM[i][-1] for i in range(self.number_arcs)]
                # Extract states and STM from ode45 output
                yb = [yf[i][:nOdes] for i in range(self.number_arcs)]  # States
                phiset = [np.reshape(yf[i][nOdes:],(nOdes, nOdes)) for i in range(self.number_arcs)] # STM

                # y1 = yySTM[0][:, :nOdes]
                # for i in range(1, self.number_arcs):
                #     y1 = np.vstack((y1, (yySTM[i][1:, :nOdes])))
                #
                # for i in range(0,len(y1[:,3])):
                #     print('den = ' + str((-0.5 * 1 * y1[i,3] * cos(y1[i,7]) - 1 * y1[i,5] * sin(y1[i,7]))) + '  u =' + str(y1[i,7]) + '  lamX =' + str(y1[i,3]) + '  lamA =' + str(y1[i,5]))

                # Evaluate the boundary conditions
                res = self.get_bc(y0g, yb, paramGuess, aux)

                # Compute correction vector
                r1 = np.linalg.norm(res)
                if r1 > self.max_error:
                    logging.warn('Residue: '+str(r1) )
                    logging.warn('Residue exceeded max_error')
                    raise RuntimeError('Residue exceeded max_error')

                if self.verbose:
                    logging.debug('Residue: '+str(r1))

                # Solution converged if BCs are satisfied to tolerance
                if max(abs(res)) < self.tolerance:
                    if self.verbose:
                        logging.info("Converged in "+str(iter)+" iterations.")
                    converged = True
                    break
                # logging.debug(paramGuess)
                # Compute Jacobian of boundary conditions using numerical derviatives
                J   = self.bc_jac_func(self.get_bc, y0g, yb, phiset, paramGuess, aux).astype(np.float64)
                # if r0 is not None:
                #     beta = (r0-r1)/(alpha*r0)
                #     if beta < 0:
                #         beta = 1
                # if r1>1:
                #     alpha = 1/(2*r1)
                # else:
                #     alpha = 1
                alpha = 0.5
                beta = 1.0

                r0 = r1

                # No damping if error within one order of magnitude
                # of tolerance
                if r1 < 10*self.tolerance:
                    alpha, beta = 1, 1

                dy0 = alpha*beta*np.linalg.solve(J,-res)

                #dy0 = -alpha*beta*np.dot(np.transpose(np.dot(np.linalg.inv(np.dot(J,np.transpose(J))),J)),res)

                # dy0 = np.linalg.solve(J,-res)
                # if abs(r1 - 0.110277711594) < 1e-4:
                #     from beluga.utils import keyboard

                # Apply corrections to states and parameters (if any)

                if nParams > 0:
                    dp = dy0[(nOdes*self.number_arcs):]
                    dy0 = dy0[:(nOdes*self.number_arcs)]
                    paramGuess = paramGuess + dp
                    for i in range(self.number_arcs):
                        y0g[i] = y0g[i] + dy0[(i*nOdes):((i+1)*nOdes)]
                else:
                    y0g = y0g + dy0
                iter = iter+1
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warn(fname+'('+str(exc_tb.tb_lineno)+'): '+str(exc_type))

        # Now program stitches together solution from the multiple arcs instead of propagating from beginning.
        # This is important for sensitive problems because they can diverge from the actual solution if propagated in single arc.
        # Therefore, the initial guess for next step and data for plotting are much better.
        if converged:
            # x1, y1 = ode45.solve(deriv_func, [x[0],x[-1]], y0g[0], paramGuess, aux, abstol=1e-6, reltol=1e-6)
            # sol = Solution(x1,y1.T,paramGuess)
            x1 = tset[0]
            y1 = yySTM[0][:, :nOdes]
            for i in range(1, self.number_arcs):
                x1 = np.hstack((x1, tset[i][1:]))
                y1 = np.vstack((y1, (yySTM[i][1:, :nOdes])))
            sol = Solution(x1, y1.T, paramGuess)
        else:
            # Return initial guess if it failed to converge
            sol = solinit

        sol.converged = converged

        sol.aux = aux

        if self.worker is None:
            ode45.closePool()
        return sol
