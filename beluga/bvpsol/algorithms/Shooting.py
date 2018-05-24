# from autodiff import Function, Gradient
import numpy as np

import beluga
from beluga.utils import timeout, keyboard
from beluga.ivpsol.integrators import ode45
from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.problem import BVP
from beluga.ivpsol import Propagator, ivp
from beluga.ivpsol import sol as solivp
from sympy.utilities.lambdify import lambdastr
import numba
import sys


from math import *
import logging
import imp
import functools as ft
import itertools as it
import sympy as sym
import pystache

import simplepipe as sp

import pickle


class Shooting(BaseAlgorithm):
    """
    Shooting algorithm for solving boundary value problems.

    Given a system of ordinary differential equations :eq:`ordinarydifferentialequation`, define the sensitivities as

    .. math::
        A(t) = \\left[\\frac{\\partial \\mathbf{f}}{\\partial \\mathbf{x}}, \\frac{\\partial \\mathbf{f}}{\\partial \\mathbf{p}}\\right]

    Then, the state-transition matrix is defined as the following set of first-order differential equations

    .. math::
        \\begin{aligned}
            \\Delta_0 &= \\left[Id_M, \\mathbf{0}\\right] \\\\
            \\dot{\\Delta} &= A(t)\\Delta
        \\end{aligned}

    Sensitivities of the boundary conditions are

    .. math::
        \\begin{aligned}
            M &= \\frac{\\partial \mathbf{\\Phi}}{\\partial \\mathbf{x}_0} \\\\
            P &= \\frac{\\partial \mathbf{\\Phi}}{\\partial \\mathbf{p}} \\\\
            Q_0 &= \\frac{\\partial \mathbf{\\Phi}}{\\partial \\mathbf{q}_0} \\\\
            Q_f &= \\frac{\\partial \mathbf{\\Phi}}{\\partial \\mathbf{q}_f}
        \\end{aligned}

    The Jacobian matrix is then the concatenation of these sensitivities

    .. math::
        J = \\left[M, P, Q_0+Q_f \\right]
    """

    def __init__(self, tolerance=1e-6, max_iterations=100, max_error=10, derivative_method='fd', verbose=True, cached=True, use_numba=False):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.max_error = max_error
        self.derivative_method = derivative_method
        self.use_numba = use_numba
        self.cached = False
        self.saved_code = True
        if derivative_method not in ['fd']:
            raise ValueError("Invalid derivative method specified. Valid options are 'csd' and 'fd'.")

    @staticmethod
    def load_code():
        logging.info('Loading compiled code ...')
        with open('codecache.pkl', 'rb') as f:
            bvp_data = pickle.load(f)

        return bvp_data

    def save_code(self):
        logging.info('Saving compiled code ...')
        bvp_data = {'deriv_fn': self.out_ws['code_module'].deriv_func}
        with open('codecache.pkl', 'wb') as f:
            pickle.dump(bvp_data, f, pickle.HIGHEST_PROTOCOL)

    def deriv_func_ode45(self, _t, _X, _p, _aux):
        return self.out_ws['code_module'].deriv_func(_t, _X, _p, list(_aux['const'].values()),0)

    def preprocess(self, problem_data):
        """Code generation and compilation before running solver."""
        out_ws = PythonCodeGen({'problem_data': problem_data})
        logging.debug(out_ws['bc_func_code'])
        logging.debug(out_ws['deriv_func_code'])

        if self.use_numba:
            deriv_func = numba.njit(parallel=False, nopython=True)(out_ws['code_module'].deriv_func_nojit)
        else:
            deriv_func = out_ws['code_module'].deriv_func_nojit
        out_ws['deriv_func_fn'] = deriv_func
        out_ws['code_module'].deriv_func = deriv_func
        self.saved_code = False

        self.out_ws = out_ws
        # self.stm_ode_func = self.make_stmode(out_ws['deriv_func_fn'], problem_data['nOdes'])
        self.bvp = BVP(out_ws['deriv_func_fn'],
                       out_ws['bc_func_fn'], out_ws['compute_control_fn'])#out_ws['compute_control_fn'])

        # self.stm_ode_func = ft.partial(self._stmode_fd, odefn=self.bvp.deriv_func)
        self.stm_ode_func = self.make_stmode(self.bvp.deriv_func, problem_data['nOdes'])
        self.bc_jac_multi  = ft.partial(self.__bc_jac_multi, bc_func=self.bvp.bc_func)
        # self.bc_jac_multi = self.__bc_jac_multi
        sys.modules['_beluga_'+problem_data['problem_name']] = out_ws['code_module']
        return out_ws['code_module']

    def __bc_jac_multi(self, nBCs, phi_full_list, y_list, parameters, aux, bc_func, StepSize=1e-6):
        p  = np.array(parameters)
        nParams = p.size
        h = StepSize
        ya = np.array([traj.T[0] for traj in y_list]).T
        yb = np.array([traj.T[-1] for traj in y_list]).T
        nOdes = ya.shape[0]
        num_arcs = len(phi_full_list)
        fx = bc_func(ya,yb,p,aux)
        nBCs = len(fx)

        M = np.zeros((nBCs, nOdes))
        P = np.zeros((nBCs, p.size))
        J = np.zeros((nBCs, (nOdes)*num_arcs+p.size))
        dx = np.zeros((nOdes+nParams, num_arcs))

        for arc_idx, phi in zip(it.count(), phi_full_list):
            # Evaluate for all arcs
            for i in range(nOdes):
                dx[i, arc_idx] = dx[i, arc_idx] + h
                dyb = np.dot(phi[-1], dx[:])
                f = bc_func(ya + dx[:nOdes,:], yb + dyb, p, aux)
                M[:,i] = (f-fx)/h
                dx[i, arc_idx] = dx[i, arc_idx] - h

            J_i = M
            J_slice = slice(nOdes*arc_idx, nOdes*(arc_idx+1))
            J[:,J_slice] = J_i

        for i in range(p.size):
            p[i] = p[i] + h
            j = i + nOdes
            dx[j] = dx[j] + h
            dy = np.dot(phi[-1],dx[:])
            f = bc_func(ya, yb + dy, p, aux)
            P[:,i] = (f-fx)/h
            dx[j] = dx[j] - h
            p[i] = p[i] - h

        J[:,nOdes*num_arcs:] = P
        return J

    def make_stmode(self, odefn, nOdes, StepSize=1e-6):
        Xh = np.eye(nOdes)*StepSize

        # @numba.jit(looplift=True, nopython=True)
        def _stmode_fd(t, _X, p, const, arc_idx):
            """ Finite difference version of state transition matrix """
            nParams = p.size
            F = np.empty((nOdes, nOdes+nParams))
            # nrt_mstats(alloc=14082696, free=13545502, mi_alloc=9439609, mi_free=8940786)
            # nrt_mstats(alloc=14005954, free=13468760, mi_alloc=9362867, mi_free=8864044)
            phi = _X[nOdes:].reshape((nOdes, nOdes+nParams))
            X = _X[0:nOdes]  # Just states

            # Compute Jacobian matrix, F using finite difference
            fx = odefn(t, X, p, const, arc_idx)

            for i in numba.prange(nOdes):
                fxh = odefn(t, X + Xh[i, :], p, const, arc_idx)
                F[:, i] = (fxh-fx)/StepSize

            for i in numba.prange(nParams):
                p[i] += StepSize
                fxh = odefn(t, X, p, const, arc_idx)
                F[:, i+nOdes] = (fxh - fx) / StepSize
                p[i] -= StepSize

            phiDot = np.dot(np.vstack((F, np.zeros((nParams, nParams + nOdes)))),np.vstack((phi, np.hstack((np.zeros((nParams, nOdes)), np.eye(nParams))))))[:nOdes, :]
            return np.concatenate((fx, np.reshape(phiDot, (nOdes * (nOdes + nParams)))))

        def wrapper(t, _X, p, const, arc_idx):  # needed for scipy
            return _stmode_fd(t, _X, p, const, arc_idx)
        return wrapper

    def solve(self, solinit):
        """Solve a two-point boundary value problem
            using the shooting method

        Args:
            deriv_func: the ODE function
            bc_func: the boundary conditions function
            solinit: a "Solution" object containing the initial guess
        Returns:
            solution of TPBVP
        """
        x = solinit.x
        # Get initial states from the guess structure
        y0g = solinit.y[:,0]
        paramGuess = solinit.parameters

        deriv_func = self.bvp.deriv_func
        bc_func = self.bvp.bc_func

        aux = solinit.aux
        const =[np.float64(_) for _ in aux['const'].values()]
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
        stm0 = np.hstack((np.eye(nOdes), np.zeros((nOdes,nParams)))).reshape(nOdes*(nOdes+nParams))
        n_iter = 1            # Initialize iteraiton counter
        converged = False   # Convergence flag

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None
        prop = Propagator()
        ivp_problem = ivp()
        ivp_problem.equations_of_motion = self.stm_ode_func
        y0stm = np.zeros((len(stm0)+nOdes))
        yb = np.zeros_like(ya)
        try:
            while True:
                phi_list = []
                phi_full_list = []
                x_list = []
                y_list = []
                with timeout(seconds=5000):
                    for arc_idx, tspan in enumerate(tspan_list):
                        y0stm[:nOdes] = ya[:, arc_idx]
                        y0stm[nOdes:] = stm0[:]
                        q0 = []
                        sol = prop(ivp_problem, tspan, y0stm, q0, paramGuess, aux, arc_idx)
                        t = sol.t
                        yy = sol.y.T
                        y_list.append(yy[:nOdes, :])
                        x_list.append(t)
                        yb[:, arc_idx] = yy[:nOdes, -1]
                        phi_full = np.reshape(yy[nOdes:, :].T, (len(t), nOdes, nOdes+nParams))
                        phi_full_list.append(np.copy(phi_full))
                        phi = np.reshape(yy[nOdes:, -1].T, (nOdes, nOdes+nParams))  # STM
                        phi_list.append(np.copy(phi))
                if n_iter == 1:
                    if not self.saved_code:
                        self.save_code()
                        self.saved_code = True

                # Iterate through arcs
                if n_iter>self.max_iterations:
                    logging.warn("Maximum iterations exceeded!")
                    break

                res = bc_func(ya, yb, paramGuess, aux)

                if any(np.isnan(res)):
                    print(res)
                    raise RuntimeError("Nan in residual")

                # r1 = np.linalg.norm(res)
                r1 = max(abs(res))
                # if r0 is not None and r1 > self.tolerance*10 and abs(r1-r0)<self.tolerance:
                #     raise RuntimeError('Not enough change in residual. Stopping ...')
                if self.verbose:
                    logging.debug('Residue: '+str(r1))

                if r1 > self.max_error:
                    raise RuntimeError('Error exceeded max_error')

                # Solution converged if BCs are satisfied to tolerance
                if r1 <= self.tolerance and n_iter > 1:
                    if self.verbose:
                        logging.info("Converged in "+str(n_iter)+" iterations.")
                    converged = True
                    break

                # Compute Jacobian of boundary conditions using numerical derviatives
                nBCs = len(res)
                # keyboard()
                # J = self.bc_jac_multi(nBCs, phi_full_list, [ya,yb], paramGuess, aux)
                J = self.bc_jac_multi(nBCs, phi_full_list, y_list, paramGuess, aux)
                # Compute correction vector

                if r0 is not None:
                    # if r1/r0 > 2:
                    #     logging.error('Residue increased more than 2x in one iteration!')
                    #     break
                    # beta = (r0-r1)/(alpha*r0)
                    beta = 1
                    if beta < 0:
                        beta = 1
                if r1>1:
                    # alpha = 1./(5*r1)
                    # alpha = 0.5
                    alpha = 1/(2*r1)
                else:
                    alpha = 1
                r0 = r1

                # No damping if error within one order of magnitude
                # of tolerance
                if r1 < min(10*self.tolerance,1e-3):
                    alpha, beta = 1, 1

                try:
                    dy0 = alpha*beta*np.linalg.solve(J,-res)
                except:
                    dy0, *_ = np.linalg.lstsq(J, -res)
                    dy0 = alpha*beta*dy0

                    # # keyboard()
                    # rank1 = np.linalg.matrix_rank(J)
                    # rank2 = np.linalg.matrix_rank(np.c_[J,-res])
                    # if rank1 == rank2:
                    #     # dy0 = alpha*beta*np.dot(np.linalg.pinv(J),-res)
                    #     dy0 = -alpha*beta*(np.linalg.inv(J @ J.T) @ J).T @ res
                    #     # dy0 = -alpha*beta*np.dot( np.linalg.inv(np.dot(J.T,J)), J.T  )
                    # else:
                    #     # Re-raise exception if system is infeasible
                    #     raise
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
            # y_list = []
            # x_list = []
            sol.arcs = []
            y0 = np.zeros(ya.shape[0])
            timestep_ctr = 0
            for arc_idx, tt in enumerate(x_list):
            #     tt,yy = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, aux, arc_idx, abstol=1e-8, reltol=1e-4)
            #     tt,yy = ode45(deriv_func, tspan, ya[:,arc_idx], paramGuess, const, arc_idx, abstol=1e-8, reltol=1e-4)
            #     y_list.append(yy.T)
            #     x_list.append(tt)
                sol.arcs.append((timestep_ctr, timestep_ctr+len(tt)-1))
            #     timestep_ctr += len(tt)

            # If problem converged, propagate solution to get full trajectory
            sol.x = np.hstack(x_list)
            sol.y = np.column_stack(y_list)
            sol.parameters = paramGuess

        sol.converged = converged
        sol.aux = aux
        return sol


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
    module.__dict__.update({'__builtin__': {}})
    exec(code_string, module.__dict__)
    return getattr(module, function_name, None)


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