"""Quasi-linear Chebyshev Picard Iteration method"""

from beluga.integrators.mcpi import mcpi, mcpi_init, cheby_eval, absdiff
from numba import njit, prange, jit
from .BaseAlgorithm import BaseAlgorithm
import pystache
import simplepipe as sp
import numpy as np
import functools as ft
import imp
from beluga.problem import BVP
import sys
# def create_odefn(problem_data, module):
#

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
    return module

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
    template_path = beluga.root()+'/optimlib/templates/'+problem_data['method']+'/qcpi/'+template_file
    with open(template_path) as f:
        tmpl = f.read()
        # Render the template using the data
        code = renderer.render(tmpl, problem_data)
        return code

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
        Compiled function
    """
    # For security
    module.__dict__.update({'__builtin__':{}})
    exec(code_string, module.__dict__)
    return getattr(module,function_name)

QCPICodeGen = sp.Workflow([
    # Create module for holding compiled code
    sp.Task(ft.partial(create_module), inputs='problem_data', outputs=('code_module')),

    # sp.Task(make_functions, inputs=('problem_data', 'code_module'), outputs=('code_module','compute_control_fn')),
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


pert_eom_bck = None
@ft.lru_cache(maxsize=16)
def make_pert_eom(nOdes, q, eom_fn):
    """Makes EOM that evaluates perturbed & unperturbed states at all time steps"""
    def pert_eom(t, X, dXdt, *args):
        for i in range(q+2):
            # Extract only relevant states
            X_ = X[:,i*nOdes:(i+1)*nOdes]
            dXdt_ = dXdt[:,i*nOdes:(i+1)*nOdes]
            # One timestep at a time
            for j in range(len(t)):
                eom_fn(t[j], X_[j,:], dXdt_[j,:], *args)

    global pert_eom_bck
    pert_eom_bck = pert_eom
    return njit(parallel=True)(pert_eom)

@ft.lru_cache(maxsize=16)
def make_mcpi_eom(eom_fn):
    """Makes EOM that evaluates perturbed & unperturbed states at all time steps"""

    # @njit(parallel=True)
    def mcpi_eom(t, X_, dXdt_, *args):
        # One timestep at a time
        for j in range(len(t)):
            eom_fn(t[j], X_[j,:], dXdt_[j,:], *args)

    return mcpi_eom


@ft.lru_cache(maxsize=16)
def make_bc_jac(bcfn, nOdes, step_size=1e-6):
    """Makes compiled BC jacobian function using forward difference"""

    @jit(parallel=True)
    def jac_fn(Yb, jac, *args):
        fx = bcfn(Yb, *args)
        steps = np.eye(nOdes)*step_size + Yb[:nOdes]
        for i in prange(nOdes):
            fxh = bcfn(steps[i], *args)
            jac[:,i] = (fxh - fx)/step_size

        return fx

    return jac_fn


@ft.lru_cache(maxsize=16)
def make_perf_idx(bc_left_fn, bc_right_fn):
    @jit(parallel=True)
    def perf_idx(x_t, A_t, alpha, *args):
        P = 0
        # MCPI gives reversed time history
        x_f = x_t[0,:] + alpha*A_t[0,:]
        x_0 = x_t[-1,:] + alpha*A_t[-1,:]

        f_vec = bc_left_fn(x_0, *args)
        g_vec = bc_right_fn(x_f, *args)
        P = P + f_vec.T @ f_vec + g_vec.T @ g_vec
        return P
    return perf_idx

class QCPI(BaseAlgorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, max_error=10, N=21, verbose=True):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.max_error = max_error
        self.N = N


    def preprocess(self, problem_data):
        """Code generation and compilation before running solver."""
        out_ws = QCPICodeGen({'problem_data': problem_data})
        print(out_ws['bc_func_code'])
        print(out_ws['deriv_func_code'])

        self.bvp = BVP(out_ws['deriv_func_fn'],
                       out_ws['bc_func_fn'], None) #out_ws['compute_control_fn'])#out_ws['compute_control_fn'])

        self.stm_ode_func = self.bvp.deriv_func
        self.module = out_ws['code_module']
        self.left_bc_mask = out_ws['code_module'].bc_free_mask
        self.num_dae_vars = out_ws['code_module'].num_dae_vars
        # self.left_bc_mask = problem_data['bc_free_mask']
        # print(self.left_bc_mask)
        self.bc_left_fn = out_ws['code_module'].bc_func_left
        self.bc_right_fn  = out_ws['code_module'].bc_func_right
        # self.deriv_func = njit(parallel=True)(out_ws['code_module'].deriv_func_mcpi)
        self.deriv_func = out_ws['code_module'].deriv_func_mcpi
        self.mcpi_eom = make_mcpi_eom(self.deriv_func)
        sys.modules['_beluga_'+problem_data['problem_name']] = out_ws['code_module']
        return out_ws['code_module']

    def solve(self,solinit):
        x  = solinit.x
        # Get initial states from the guess structure
        y0g = solinit.y[:,0]
        paramGuess = solinit.parameters

        deriv_func = self.bvp.deriv_func
        bc_func = self.bvp.bc_func

        aux = solinit.aux
        # Only the start and end times are required for ode45
        arcs = solinit.arcs

        ya = solinit.y[:,0]
        yb = solinit.y[:,-1]

        # Set initial values
        icvals= np.array(list(aux['initial'].values()))
        icval_slice = np.array(self.left_bc_mask[:-self.num_dae_vars])==0
        ya[:-self.num_dae_vars][icval_slice] = icvals[icval_slice]

        # Extract number of ODEs in the system to be solved
        nXandLam = y0g.shape[0]
        nParams = paramGuess.size
        nOdes = nXandLam + nParams

        ## Setup QCPI
        x_0 = np.concatenate((ya, paramGuess))

        res_left = self.bc_left_fn(x_0, aux)
        left_jac = np.zeros((len(res_left), nOdes))
        left_bc_jac_fn = make_bc_jac(self.bc_left_fn, nOdes)
        left_bc_jac_fn(x_0, left_jac, aux)

        x_pert = np.absolute(np.max(solinit.y, axis=1))*0.0001
        x_pert = np.append(x_pert, np.absolute(solinit.parameters)*0.0001)
        x_pert[x_pert < 10*self.tolerance] = 10*self.tolerance
        # Each row is one initial condition for particular solution
        # A_j0 = np.eye(nOdes)
        # A_j0[np.diag_indices(nOdes)] = self.left_bc_mask
        # A_j0 = np.unique(A_j0, axis=0)*.001   # Remove duplicates
        A_j0 = np.vstack((np.zeros(nOdes), x_pert*np.eye(nOdes, dtype=np.float64)))
        # A_j0 = np.vstack((np.zeros(nOdes), 0.01*np.eye(nOdes)))

        q = len(A_j0) - 1

        # Set up perturbed ICs
        xp_0 = np.hstack((x_0, A_j0.flat)) # Add perturbed ICs as extra states
        xp_0[nOdes:] = np.tile(xp_0[:nOdes], (q+1,)) + A_j0.flat  # Add perturbations to ICs
        xpm_0 = np.reshape(xp_0, (q+2, nOdes))  # Matrix 'view' of xp_0
        # tspan = x
        tspan = x[0], x[-1]
        t_short = [tspan[0], tspan[-1]]
        converged = False
        N = self.N
        max_iter = self.max_iterations

        # Setup MCPI
        w1 = (tspan[-1]-tspan[0])/2
        w2 = (tspan[-1]+tspan[0])/2
        tau, C_x, C_a = mcpi_init(N)      # tau is in reverse order (1 to -1)
        C_a = w1 * C_a.astype(np.float64)
        t_arr = tau*w1 + w2

        # Make functions
        pert_eom = make_pert_eom(nOdes, q, self.deriv_func)
        bc_jac_fn = make_bc_jac(self.bc_right_fn, nOdes)
        perf_idx_fn = make_perf_idx(self.bc_left_fn, self.bc_right_fn)

        const = tuple(aux['const'].values())

        _, x_guess2 = mcpi(pert_eom, tspan, xp_0, N=N, args=(const,))
        if np.isnan(x_guess2.flat).any():
            if solinit.extra is not None and not np.isnan(solinit.extra.flat).any():
                x_guess = solinit.extra.astype(np.float64)
            else:
                x_guess = np.tile(xp_0, (N+1, 1)).astype(np.float64)  # Each column -> time history of one state
        else:
            x_guess = np.flipud(x_guess2).astype(np.float64)

        x0_twice = 2*x_guess[-1]
        g_arr = np.empty_like(x_guess)

        res = self.bc_right_fn(x_0, aux)
        nBCs = len(res)
        psi_jac = np.zeros((nBCs, nOdes))

        alpha1 = 1
        alpha2 = 1
        r0 = None

        err1 = 1000
        err0 = 9999
        np.set_printoptions(precision=4, linewidth=160)
        for ctr in range(max_iter):
            pert_eom(t_arr, x_guess, g_arr, const)

            # if np.any(np.isnan(g_arr)):
            #     print('NaaaaaNaaaa')
            #     from beluga.utils import keyboard
            #     keyboard()
            #     break

            beta = (C_a @ g_arr)
            beta[0]+= x0_twice          # Compute Chebyshev coefficients of solution
            x_new = C_x @ beta          # Compute solution

            err1 = np.max(absdiff(x_new, x_guess))
            if np.isnan(err1):
                x_new = x_guess
                print('NaaaaaN')
                break
                from beluga.utils import keyboard
                keyboard()

            if err1 < 10*self.tolerance or abs(err0-err1)<self.tolerance:
                x_tf = x_new[0,:]       # x_new is reverse time history
                res = bc_jac_fn(x_tf[:nOdes], psi_jac, aux) # Compute residue and jacobian
                res_norm_0 = np.amax(np.abs((res)))
                # if ctr > -90:
                # print('Residue : '+str(res_norm_0))
                if res_norm_0 < self.tolerance:
                    converged = True
                    print('Converged in %d iterations.' % ctr)
                    break

                if np.isnan(res).any():
                    x_new = x_guess # Reset to old version in case of NaN
                    # from beluga.utils import keyboard
                    # keyboard()
                    print('NaaaaaN')
                    break
                # Convert perturbed terminal conditions to matrix
                # Num of rows = q+1, num of cols = num_states
                A_jf = np.reshape(x_tf[nOdes:], (q+1, nOdes))
                # Subtract unperturbed terminal state to get perturbations
                A_jf = (A_jf - x_tf[:nOdes]).T

                # lhs = np.vstack((np.ones((1,q+1)), psi_jac @ A_jf))
                # try:
                #     k_j = np.linalg.solve(lhs, np.hstack((1, -res)))
                # except:
                #     k_j, *_ = np.linalg.lstsq(lhs, np.hstack((1, -res)))

                x_t0 = x_new[-1,:]
                A0 = np.reshape(x_t0[nOdes:], (q+1, nOdes))
                A0 = (A0 - x_t0[:nOdes]).T
                res_left = left_bc_jac_fn(x_t0, left_jac, aux)
                lhs = np.vstack((np.ones((1,q+1)), psi_jac @ A_jf, left_jac @ A0))

                # First row is all ones, rows after = Jac @ perturbations at tf
                try:
                    k_j = np.linalg.solve(lhs, np.hstack((1, -res, -res_left)))
                except:
                    k_j, *_ = np.linalg.lstsq(lhs, np.hstack((1, -res, -res_left)))
                A_0 = k_j @ A_j0

                # stepsize calculation
                x_t = x_new[:,:nOdes]
                A_t = np.zeros_like(x_t)
                P0 = perf_idx_fn(x_t, A_t, 0.0, aux)
                if P0 < self.tolerance:
                    converged = True
                    print('Converged (w/ P0) in %d iterations.' % ctr)
                    break

                # Compute A for every time step
                for i in range(x_guess.shape[0]):
                    x_ti = x_new[i,:]
                    A_ji = np.reshape(x_ti[nOdes:], (q+1, nOdes))
                    # Subtract unperturbed x(t) to get perturbation at time t
                    A_ji = (A_ji.astype(np.float64) - x_ti[:nOdes].astype(np.float64))
                    A_ti = k_j @ A_ji
                    A_t[i,:] = k_j @ A_ji

                alpha = 2.0
                P = P0 + 1
                while P > P0 and alpha > self.tolerance:
                    alpha = alpha/2.0
                    P = perf_idx_fn(x_t, A_t, alpha, aux)

                xpm_0 += alpha * A_0   # Also adds to xp_0 as xpm_0 is a view
                x_new[:,:nOdes] += alpha * A_t

                x0_twice = 2*xp_0
                # x_new[-1] = xp_0
                # xpm_0 += alpha * A_t[-1]   # Also adds to xp_0 as xpm_0 is a view
                # x_new[:,:nOdes] += alpha * A_t
                x_new[-1,nOdes:] = xp_0[nOdes:]
                # x0_twice = 2*x_new[-1,:]

            x_guess = x_new
            err0 = err1

        # Return initial guess if it failed to converge
        sol = solinit
        if converged:
            if len(tspan) > 2:
                _, x_out = mcpi(self.mcpi_eom, tspan, x_new[-1, :nOdes], args=(const,))
            else:
                x_out = np.flipud(x_new)[:,:nOdes]
                tspan = t_arr[::-1]

            sol.x, sol.y = tspan, x_out[:,:nXandLam].T
            sol.parameters = x_out[0,nXandLam:]
            sol.arcs = [(0, len(sol.x)-1)]
            sol.arc_seq = (0,)
            sol.extra = x_new

        sol.converged = converged
        sol.aux = aux
        return sol
