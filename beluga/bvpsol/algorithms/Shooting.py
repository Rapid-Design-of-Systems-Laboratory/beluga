import numpy as np

import beluga
from beluga.utils import timeout, keyboard
from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Propagator
import copy
import numba

import logging
import itertools as it


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

    def __new__(cls, *args, **kwargs):
        """
        Creates a new Shooting object.

        :param args: Unused
        :param kwargs: Additional parameters accepted by the solver.
        :return: Shooting object.

        +------------------------+-----------------+-----------------+
        | Valid kwargs           | Default Value   | Valid Values    |
        +========================+=================+=================+
        | cached                 | True            | Bool            |
        +------------------------+-----------------+-----------------+
        | derivative_method      | 'fd'            | {'fd','csd'}    |
        +------------------------+-----------------+-----------------+
        | ivp_args               | {}              | see `ivpsol`    |
        +------------------------+-----------------+-----------------+
        | tolerance              | 1e-4            | > 0             |
        +------------------------+-----------------+-----------------+
        | max_error              | 100             | > 0             |
        +------------------------+-----------------+-----------------+
        | max_iterations         | 100             | > 0             |
        +------------------------+-----------------+-----------------+
        | use_numba              | False           | Bool            |
        +------------------------+-----------------+-----------------+
        | verbose                | False           | Bool            |
        +------------------------+-----------------+-----------------+
        """

        obj = super(Shooting, cls).__new__(cls, *args, **kwargs)

        cached = kwargs.get('cached', True)
        derivative_method = kwargs.get('derivative_method', 'fd')
        ivp_args = kwargs.get('ivp_args', dict())
        tolerance = kwargs.get('tolerance', 1e-4)
        max_error = kwargs.get('max_error', 100)
        max_iterations = kwargs.get('max_iterations', 100)
        use_numba = kwargs.get('use_numba', False)
        verbose = kwargs.get('verbose', False)

        obj.cached = cached
        obj.derivative_method = derivative_method
        obj.ivp_args = ivp_args
        obj.tolerance = tolerance
        obj.max_error = max_error
        obj.max_iterations = max_iterations
        obj.use_numba = use_numba
        obj.verbose = verbose
        return obj

    def __init__(self, *args, **kwargs):
        self.stm_ode_func = None
        self.saved_code = True

        if self.derivative_method not in ['fd']:
            raise ValueError("Invalid derivative method specified. Valid options are 'csd' and 'fd'.")

    def preprocess(self, problem_data, use_numba=False):
        obj = super().preprocess(problem_data, use_numba=use_numba)
        self.stm_ode_func = self.make_stmode(obj[0].deriv_func, problem_data['nOdes'])
        return obj

    def _bc_jac_multi(self, nBCs, phi_full_list, y_list, parameters, aux, bc_func, StepSize=1e-6):
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

    @staticmethod
    def make_stmode(odefn, nOdes, StepSize=1e-6):
        Xh = np.eye(nOdes)*StepSize

        # @numba.jit(looplift=True, nopython=True)
        def _stmode_fd(t, _X, p, const, arc_idx):
            """ Finite difference version of state transition matrix """
            nParams = p.size
            F = np.empty((nOdes, nOdes+nParams))
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

    def solve(self, deriv_func, bc_func, solinit):
        '''
        Solve a two-point boundary value problem using the shooting method

        :param deriv_func: The ODE function.
        :param bc_func: The boundary conditions function.
        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        '''

        # Instantly make a copy of sol and format inputs
        sol = copy.deepcopy(solinit)
        sol.x = np.array(sol.x, dtype=np.float64)
        sol.y = np.array(sol.y, dtype=np.float64)
        sol.parameters = np.array(sol.parameters, dtype=np.float64)

        # Extract some info from the guess structure
        y0g = sol.y[:,0]
        nOdes = y0g.shape[0]
        paramGuess = solinit.parameters

        # Make the state-transition ode matrix if it hasn't already been made
        if self.stm_ode_func is None:
            self.stm_ode_func = self.make_stmode(deriv_func, y0g.shape[0])

        if sol.arcs is None:
            sol.arcs = [(0, len(solinit.x)-1)]

        arc_seq = sol.aux['arc_seq']
        num_arcs = len(arc_seq)
        if len(sol.arcs) % 2 == 0:
            raise Exception('Number of arcs must be odd!')

        left_idx, right_idx = map(np.array, zip(*sol.arcs))
        ya = sol.y[:,left_idx]
        yb = sol.y[:,right_idx]

        tmp = np.arange(num_arcs+1, dtype=np.float32)*sol.x[-1]
        tspan_list = [(a, b) for a, b in zip(tmp[:-1], tmp[1:])]

        if solinit.parameters is None:
            nParams = 0
        else:
            nParams = solinit.parameters.size

        # Initial state of STM is an identity matrix with an additional column of zeros per parameter
        stm0 = np.hstack((np.eye(nOdes), np.zeros((nOdes,nParams)))).reshape(nOdes*(nOdes+nParams))
        n_iter = 1  # Initialize iteration counter
        converged = False  # Convergence flag

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley # TODO: Reference this in the docstring
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None
        prop = Propagator(**self.ivp_args)
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
                        sol_ivp = prop(self.stm_ode_func, None, tspan, y0stm, q0, paramGuess, sol.aux, arc_idx)
                        t = sol_ivp.t
                        yy = sol_ivp.y.T
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

                # Break cycle if it exceeds the max number of iterations
                if n_iter > self.max_iterations:
                    logging.warning("Maximum iterations exceeded!")
                    break

                # Determine the error vector
                res = bc_func(ya, yb, paramGuess, sol.aux)

                # Break cycle if there are any NaNs in our error vector
                if any(np.isnan(res)):
                    print(res)
                    raise RuntimeError("Nan in residual")

                r1 = max(abs(res))
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

                # Compute Jacobian of boundary conditions
                nBCs = len(res)
                J = self._bc_jac_multi(nBCs, phi_full_list, y_list, paramGuess, sol.aux, bc_func)

                # Compute correction vector
                if r0 is not None:
                    # if r1/r0 > 2:
                    #     logging.error('Residue increased more than 2x in one iteration!')
                    #     break
                    # beta = (r0-r1)/(alpha*r0)
                    beta = 1
                    if beta < 0:
                        beta = 1

                if r1 > 1:
                    alpha = 1/(2*r1)
                else:
                    alpha = 1

                r0 = r1

                # No damping if error within one order of magnitude of tolerance
                if r1 < min(10*self.tolerance,1e-3):
                    alpha, beta = 1, 1

                try:
                    dy0 = alpha*beta*np.linalg.solve(J, -res)
                except:
                    dy0, *_ = np.linalg.lstsq(J, -res)
                    dy0 = alpha*beta*dy0

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

        except Exception as e:
            logging.warning(e)
            import traceback
            traceback.print_exc()

        if converged:
            sol.arcs = []
            timestep_ctr = 0
            for arc_idx, tt in enumerate(x_list):
                sol.arcs.append((timestep_ctr, timestep_ctr+len(tt)-1))

            sol.x = np.hstack(x_list)
            sol.y = np.column_stack(y_list)
            sol.parameters = paramGuess

        else:
            # Return a copy of the original guess if the problem fails to converge
            sol = copy.deepcopy(solinit)

        sol.converged = converged
        sol.aux = solinit.aux  # TODO: I'm fairly certain this line isn't needed. But if I delete it, it crashes.
        return sol
