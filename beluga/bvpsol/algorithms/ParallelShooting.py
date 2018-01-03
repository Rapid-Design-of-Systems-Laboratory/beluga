# from autodiff import Function, Gradient
import sys
import os
import numpy as np

import beluga
from .. import Solution
from beluga.utils import keyboard, timeout
# from beluga.integrators import ode45
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
    module.__dict__.update({'__builtin__':{}})
    exec(code_string, module.__dict__)
    return getattr(module,function_name,None)

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

import odespy

def make_wrapper(odefn):
    def wrapped(_X,_t,_p,_const,arc_idx):
        return odefn(_t, _X, _p, _const, arc_idx)
    return wrapped

@ft.lru_cache(maxsize=16)
def make_integrator(odefn, abstol=1e-6, reltol=1e-4):
    def ode45(tspan, y0, args=()):
        solver = odespy.RKF45(make_wrapper(odefn), atol=abstol, rtol=reltol, f_args=args)
        # solver._parameters['f_args'] = args
        solver.set_initial_condition(y0)
        u, t = solver.solve(tspan)
        return u
    return ode45

@ft.lru_cache(maxsize=16)
def make_stm_ode(odefn, nOdes, step_size=1e-4):
    """Makes multi-arc STM ODE function"""

    steps_mat = np.eye(nOdes)*step_size
    # @numba.njit
    def jac_fn(_, Ya, _p, _const, arc_idx):
        """
        Flat array - [X0, phi0]
        """
        YIc = Ya[:nOdes]
        fx = np.array(odefn(0, YIc, _p, _const, arc_idx))
        phi = Ya[nOdes:].reshape((nOdes, nOdes))
        F = np.empty((nOdes, nOdes))
        steps = steps_mat + YIc
        for k in range(nOdes):
            fxh = np.array(odefn(0, steps[k], _p, _const, arc_idx))
            F[:,k] = (fxh - fx)/step_size

        phidot = (F@phi)
        return np.hstack((fx, phidot.reshape(nOdes**2)))

    return jac_fn

@ft.lru_cache(maxsize=16)
def make_bc_jac_fn(bcfn, nBCs, nOdes, nArcs, step_size=1e-6):
    phi_size = nBCs + nOdes*(nArcs-1)
    steps_mat = np.eye(nOdes)*step_size
    # @numba.njit
    def bc_jac(ya, yb, res, M, N, parameters, aux):
        steps_0 = steps_mat + ya
        steps_f = steps_mat + yb

        for k in numba.prange(nOdes):
            fxh = bcfn(steps_0[k][:,np.newaxis], yb, parameters, aux)
            M[:,k] = (fxh - res)/step_size

            fxh = bcfn(ya, steps_f[k][:,np.newaxis], parameters, aux)
            N[:,k] = (fxh - res)/step_size

    @numba.jit(looplift=True)
    def bc_jac_multi(G, ya, yb, parameters, aux):
        """
        G : 3-D array with STMs

        """
        ya = ya[:,np.newaxis]
        yb = yb[:,np.newaxis]
        p  = np.array(parameters)
        h = step_size

        M = np.empty((nBCs, nOdes))
        N = np.empty((nBCs, nOdes))
        P = np.empty((nBCs, p.size))
        res = bcfn(ya, yb, parameters, aux)
        bc_jac(ya, yb, res, M, N, parameters, aux)

#         steps_0 = steps_mat + ya
#         steps_f = steps_mat + yb
#         for k in numba.prange(nOdes):
#             fxh = bcfn(steps_0[k], yb)
#             M[:,k] = (fxh - res)/step_size

#             fxh = bcfn(ya, steps_f[k])
#             N[:,k] = (fxh - res)/step_size

        Zbc = np.zeros((nBCs, nOdes))
        Z = np.zeros((nOdes, nOdes))
        Zp = np.zeros((nOdes, p.size))

        I = np.eye(nOdes)
        Gm = G[-1,:,:]

        P = np.empty((nBCs, p.size))
        for i in range(p.size):
            p[i] = p[i] + h
            f = bc_func(ya,yb,p,aux)
            P[:,i] = (f-res)/h
            p[i] = p[i] - h

        block_rows = [np.hstack([M] + [Zbc]*(nArcs-2) + [N@Gm] + [P])]

        for k in range(nArcs-1):
            row = np.hstack([Z]*k + [-G[k,:,:]] + [I] + [Z]*(nArcs-k-2) + [Zp])
            block_rows.append(row)

        J = np.vstack(block_rows)

        return res, J

    return bc_jac_multi

tspan = np.linspace(0, 1, 2)
@numba.jit(looplift=True)
def propagate_stm(stmode45, Xstm0, nArcs, nOdes, xf, phi, args):
    for i in numba.prange(nArcs):
        yy = stmode45(tspan/nArcs, Xstm0[i,:], args=args)

        xf[i,:] = yy[-1,:nOdes]
        phi[i,:,:] = yy[-1,nOdes:].reshape((nOdes, nOdes))

class ParallelShooting(BaseAlgorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, max_error=10, verbose=True):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.max_error = max_error
        self.saved_code = True

    def preprocess(self, problem_data):
        """Code generation and compilation before running solver."""
        out_ws = PythonCodeGen({'problem_data': problem_data})
        logging.debug(out_ws['bc_func_code'])
        logging.debug(out_ws['deriv_func_code'])
        cache_exists = os.path.isfile('codecache.pkl')
        # if not self.cached or not cache_exists:
        deriv_func = numba.njit(parallel=True)(out_ws['code_module'].deriv_func_nojit)
        out_ws['deriv_func_fn'] = deriv_func
        out_ws['code_module'].deriv_func = deriv_func
        self.saved_code = False
        # else:
        #     bvp_data = self.load_code()
        #     print('deriv func',id(bvp_data['deriv_fn']))
        #     out_ws['deriv_func_fn'] = bvp_data['deriv_fn']
        #     out_ws['code_module'].deriv_func = bvp_data['deriv_fn']

        self.out_ws = out_ws
        # self.stm_ode_func = self.make_stmode(out_ws['deriv_func_fn'], problem_data['nOdes'])
        self.bvp = BVP(out_ws['deriv_func_fn'],
                       out_ws['bc_func_fn'], out_ws['compute_control_fn'])#out_ws['compute_control_fn'])

        # self.stm_ode_func = ft.partial(self._stmode_fd, odefn=self.bvp.deriv_func)
        # self.stm_ode_func = self.make_stmode(self.bvp.deriv_func, problem_data['nOdes'])
        # self.bc_jac_multi  = ft.partial(self.__bc_jac_multi, bc_func=self.bvp.bc_func)
        sys.modules['_beluga_'+problem_data['problem_name']] = out_ws['code_module']
        return out_ws['code_module']

    def solve(self,solinit):
        """Solve a two-point boundary value problem
            using the parallel shooting method

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
        nArcs = 4
        nOdes = y0g.shape[0]
        if solinit.parameters is None:
            nParams = 0
        else:
            nParams = solinit.parameters.size
        nBCs = self.out_ws['code_module'].num_bc
        paramGuess = solinit.parameters

        deriv_func = self.bvp.deriv_func
        bc_func = self.bvp.bc_func

        aux = solinit.aux
        const =[np.float64(_) for _ in aux['const'].values()]

        ode45 = make_integrator(deriv_func)
        bcjac = make_bc_jac_fn(bc_func, nBCs, nOdes, nArcs)
        stmode = make_stm_ode(deriv_func, nOdes)
        stmode45 = make_integrator(stmode)

        yy = ode45(np.linspace(0,1,nArcs+1), y0g, args=(paramGuess, const, 0))
        x_new = yy[:-1,:]

        stm0 = np.tile(np.eye(nOdes).flat,(nArcs,1))
        Xstm0 = np.hstack((x_new, stm0))

        alpha = 1
        beta = 1
        r0 = None
        ctr = 0
        x_guess = np.copy(x_new)
        converged = False

        G = np.empty((nArcs, nOdes, nOdes))
        xf = np.empty((nArcs, nOdes))
        for ctr in range(self.max_iterations):
            Xstm0[:,:nOdes] = x_guess
            propagate_stm(stmode45, Xstm0, nArcs, nOdes, xf, G, args=(paramGuess, const, 0))
            
            ya = x_guess[0,:]
            yb = xf[-1,:]
            res, J = bcjac(G, ya, yb, paramGuess, aux)
            err_vec = (x_guess[1:,:] - xf[:-1,:]).reshape((nArcs-1)*nOdes)
            res_vec = np.hstack((res, err_vec))

            r1 = max(abs(res_vec))
            if r1 < self.tolerance:
                print('Converged in '+str(ctr)+' iterations !')
                converged = True
                break
            if self.verbose:
                logging.debug('Residual: '+str(r1))

            if r0 is not None:
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
            if r1 < 1e-3:
                alpha, beta = 1, 1

            dx_guess = alpha*beta*np.linalg.solve(J, -res_vec)

            if nParams > 0:
                dp = dy0[-nParams:]
                paramGuess += dp
                x_guess = x_guess + dx_guess[:-nParams].reshape((nArcs, nOdes))
            else:
                x_guess = x_guess + dx_guess.reshape((nArcs, nOdes))



        sol = solinit
        if converged:
            tspan = np.linspace(0,1,100)
            x0 = x_guess[0,:]
            x_out = ode45(tspan, x0, args=(paramGuess, const, 0))

            sol.arcs = []
            # If problem converged, propagate solution to get full trajectory
            sol.x = tspan
            sol.y = x_out
            sol.parameters = paramGuess

        sol.converged = converged
        sol.aux = aux
        return sol
        # # Only the start and end times are required for ode45
        # arcs = solinit.arcs
        #
        # if arcs is None:
        #     arcs = [(0, len(solinit.x)-1)]
        #     solinit.arcs = arcs
        #
        # arc_seq = aux['arc_seq']
        # num_arcs = len(arc_seq)
        # if len(arcs) % 2 == 0:
        #     raise Exception('Number of arcs must be odd!')
        #
        # left_idx, right_idx = map(np.array, zip(*arcs))
        # ya = solinit.y[:,left_idx]
        # yb = solinit.y[:,right_idx]
        #
        # tmp = np.arange(num_arcs+1, dtype=np.float32)
        # tspan_list = [(a, b) for a, b in zip(tmp[:-1], tmp[1:])]
        # # Extract number of ODEs in the system to be solved
        # nOdes = y0g.shape[0]
        # if solinit.parameters is None:
        #     nParams = 0
        # else:
        #     nParams = solinit.parameters.size
        #
        # # Initial state of STM is an identity matrix
        # stm0 = np.eye(nOdes).reshape(nOdes*nOdes)
        # n_iter = 1            # Initialize iteraiton counter
        # converged = False   # Convergence flag
        #
        # # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley
        # # Global Convergence and Armijo's Rule, pg. 11
        # alpha = 1
        # beta = 1
        # r0 = None
        #
        # y0stm = np.zeros((len(stm0)+nOdes))
        # yb = np.zeros_like(ya)
        # try:
        #     while True:
        #         phi_list = []
        #         x_list = []
        #         y_list = []
        #         with timeout(seconds=5000):
        #             for arc_idx, tspan in enumerate(tspan_list):
        #                 y0stm[:nOdes] = ya[:,arc_idx]
        #                 y0stm[nOdes:] = stm0[:]
        #                 # print(arc_idx, tspan, ya[:,arc_idx])
        #                 # t,yy = ode45(self.stm_ode_func, tspan, y0stm, paramGuess, aux, arc_idx, abstol=1e-6, reltol=1e-4)
        #                 t,yy = ode45(self.stm_ode_func, tspan, y0stm, paramGuess, const, arc_idx, abstol=1e-8, reltol=1e-6)
        #                 y_list.append(yy[:,:nOdes].T)
        #                 x_list.append(t)
        #                 # tt,yy2 = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-8, reltol=1e-4)
        #                 # _,yy2 = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-8, reltol=1e-3)
        #                 yb[:,arc_idx] = yy[-1,:nOdes]
        #                 phi = np.reshape(yy[-1,nOdes:],(nOdes, nOdes)) # STM
        #                 phi_list.append(np.copy(phi))
        #         if n_iter == 1:
        #             if not self.saved_code:
        #                 self.save_code()
        #                 self.saved_code = True
        #
        #         # Iterate through arcs
        #         if n_iter>self.max_iterations:
        #             logging.warn("Maximum iterations exceeded!")
        #             break
        #
        #         res = bc_func(ya, yb, paramGuess, aux)
        #
        #         if any(np.isnan(res)):
        #             print(res)
        #             # from beluga.utils import keyboard
        #             # keyboard()
        #             raise RuntimeError("Nan in residual")
        #
        #         # r1 = np.linalg.norm(res)
        #         r1 = max(abs(res))
        #         # if r0 is not None and r1 > self.tolerance*10 and abs(r1-r0)<self.tolerance:
        #         #     raise RuntimeError('Not enough change in residual. Stopping ...')
        #         if self.verbose:
        #             logging.debug('Residue: '+str(r1))
        #
        #         if r1 > self.max_error:
        #             raise RuntimeError('Error exceeded max_error')
        #
        #         # Solution converged if BCs are satisfied to tolerance
        #         if r1 <= self.tolerance and n_iter > 1:
        #             if self.verbose:
        #                 logging.info("Converged in "+str(n_iter)+" iterations.")
        #             converged = True
        #             break
        #
        #         # Compute Jacobian of boundary conditions using numerical derviatives
        #         nBCs = len(res)
        #         J = self.bc_jac_multi(nBCs, phi_list, ya, yb, paramGuess, aux)
        #         # Compute correction vector
        #
        #         if r0 is not None:
        #             # if r1/r0 > 2:
        #             #     logging.error('Residue increased more than 2x in one iteration!')
        #             #     break
        #             beta = (r0-r1)/(alpha*r0)
        #             if beta < 0:
        #                 beta = 1
        #         if r1>1:
        #             alpha = 1/(2*r1)
        #         else:
        #             alpha = 1
        #         r0 = r1
        #
        #         # No damping if error within one order of magnitude
        #         # of tolerance
        #         if r1 < min(10*self.tolerance,1e-3):
        #             alpha, beta = 1, 1
        #
        #         try:
        #             dy0 = alpha*beta*np.linalg.solve(J,-res)
        #         except:
        #             dy0, *_ = np.linalg.lstsq(J, -res)
        #             dy0 = alpha*beta*dy0
        #
        #             # # keyboard()
        #             # rank1 = np.linalg.matrix_rank(J)
        #             # rank2 = np.linalg.matrix_rank(np.c_[J,-res])
        #             # if rank1 == rank2:
        #             #     # dy0 = alpha*beta*np.dot(np.linalg.pinv(J),-res)
        #             #     dy0 = -alpha*beta*(np.linalg.inv(J @ J.T) @ J).T @ res
        #             #     # dy0 = -alpha*beta*np.dot( np.linalg.inv(np.dot(J.T,J)), J.T  )
        #             # else:
        #             #     # Re-raise exception if system is infeasible
        #             #     raise
        #         # dy0 = -alpha*beta*np.dot(np.dot(np.linalg.inv(np.dot(J,J.T)),J).T,res)
        #
        #         # Apply corrections to states and parameters (if any)
        #         d_ya = np.reshape(dy0[:nOdes*num_arcs], (nOdes, num_arcs), order='F')
        #         if nParams > 0:
        #             dp = dy0[nOdes*num_arcs:]
        #             paramGuess += dp
        #             ya = ya + d_ya
        #         else:
        #             ya = ya + d_ya
        #
        #         n_iter += 1
        #         logging.debug('Iteration #'+str(n_iter))
        # # except KeyboardInterrupt as ke:
        # #     converged = False
        # except Exception as e:
        #     logging.warn(e)
        #     import traceback
        #     traceback.print_exc()
        #
        #
        # # Return initial guess if it failed to converge
        # sol = solinit
        # if converged:
        #     # y_list = []
        #     # x_list = []
        #     sol.arcs = []
        #     y0 = np.zeros(ya.shape[0])
        #     timestep_ctr = 0
        #     for arc_idx, tt in enumerate(x_list):
        #     #     tt,yy = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-8, reltol=1e-4)
        #     #     tt,yy = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, const, arc_idx, abstol=1e-8, reltol=1e-4)
        #     #     y_list.append(yy.T)
        #     #     x_list.append(tt)
        #         sol.arcs.append((timestep_ctr, timestep_ctr+len(tt)-1))
        #     #     timestep_ctr += len(tt)
        #
        #     # If problem converged, propagate solution to get full trajectory
        #     sol.x = np.hstack(x_list)
        #     sol.y = np.column_stack(y_list)
        #     sol.parameters = paramGuess
        #
        # sol.converged = converged
        # sol.aux = aux
        # return sol
