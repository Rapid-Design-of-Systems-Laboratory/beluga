import copy
import itertools as it
import logging
import numpy as np

from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Propagator
from multiprocessing_on_dill import pool


class Shooting(BaseAlgorithm):
    r"""
    Shooting algorithm for solving boundary value problems.

    Given a system of ordinary differential equations :eq:`ordinarydifferentialequation`, define the sensitivities as

    .. math::
        A(t) = \left[\frac{\partial \mathbf{f}}{\partial \mathbf{x}}, \frac{\partial \mathbf{f}}{\partial \mathbf{p}}\right]

    Then, the state-transition matrix is defined as the following set of first-order differential equations

    .. math::
        \begin{aligned}
            \Delta_0 &= \left[Id_M, \mathbf{0}\right] \\
            \dot{\Delta} &= A(t)\Delta
        \end{aligned}

    Sensitivities of the boundary conditions are

    .. math::
        \begin{aligned}
            M &= \frac{\partial \mathbf{\Phi}}{\partial \mathbf{x}_0} \\
            P &= \frac{\partial \mathbf{\Phi}}{\partial \mathbf{p}} \\
            Q_0 &= \frac{\partial \mathbf{\Phi}}{\partial \mathbf{q}_0} \\
            Q_f &= \frac{\partial \mathbf{\Phi}}{\partial \mathbf{q}_f}
        \end{aligned}

    The Jacobian matrix is then the concatenation of these sensitivities

    .. math::
        J = \left[M, P, Q_0+Q_f \right]

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | ivp_args               | {}              | see `ivpsol`    |
    +------------------------+-----------------+-----------------+
    | tolerance              | 1e-4            | > 0             |
    +------------------------+-----------------+-----------------+
    | max_error              | 100             | > 0             |
    +------------------------+-----------------+-----------------+
    | max_iterations         | 100             | > 0             |
    +------------------------+-----------------+-----------------+
    | num_arcs               | 1               | > 0             |
    +------------------------+-----------------+-----------------+
    | num_cpus               | 1               | > 0             |
    +------------------------+-----------------+-----------------+

    """

    def __new__(cls, *args, **kwargs):
        obj = super(Shooting, cls).__new__(cls, *args, **kwargs)

        ivp_args = kwargs.get('ivp_args', dict())
        tolerance = kwargs.get('tolerance', 1e-4)
        max_error = kwargs.get('max_error', 100)
        max_iterations = kwargs.get('max_iterations', 100)
        num_arcs = kwargs.get('num_arcs', 1)
        num_cpus = kwargs.get('num_cpus', 1)

        obj.ivp_args = ivp_args
        obj.tolerance = tolerance
        obj.max_error = max_error
        obj.max_iterations = max_iterations
        obj.num_arcs = num_arcs
        obj.num_cpus = num_cpus

        obj.pool = None

        return obj

    def __init__(self, *args, **kwargs):
        self.stm_ode_func = None

        if self.num_cpus > 1:
            self.pool = pool.Pool(processes=self.num_cpus)

    def _bc_jac_multi(self, t_list, nBCs, phi_full_list, y_list, parameters, aux, bc_func, StepSize=1e-6):
        p  = np.array(parameters)
        nParams = p.size
        h = StepSize
        ya = np.array([traj[0] for traj in y_list]).T
        yb = np.array([traj[-1] for traj in y_list]).T
        nOdes = ya.shape[0]
        num_arcs = len(phi_full_list)
        fx = bc_func(t_list[0][0], ya, [], t_list[-1][-1], yb, [], p, aux)
        nBCs = len(fx)

        M = np.zeros((nBCs, nOdes))
        P = np.zeros((nBCs, p.size))
        Ptemp = np.zeros((nBCs, p.size))
        J = np.zeros((nBCs, (nOdes)*num_arcs+p.size))
        dx = np.zeros((nOdes+nParams, num_arcs))

        for arc_idx, phi in zip(it.count(), phi_full_list):
            # Evaluate for all arcs
            for i in range(nOdes):
                dx[i, arc_idx] = dx[i, arc_idx] + h
                dy = np.dot(phi[-1], dx)
                f = bc_func(t_list[0][0], ya + dx[:nOdes], [], t_list[-1][-1], yb + dy, [], p, aux)
                M[:,i] = (f-fx)/h
                dx[i, arc_idx] = dx[i, arc_idx] - h
            J_i = M
            J_slice = slice(nOdes*arc_idx, nOdes*(arc_idx+1))
            J[:,J_slice] = J_i

        for arc_idx, phi in zip(it.count(), phi_full_list):
            for i in range(p.size):
                p[i] = p[i] + h
                j = i + nOdes
                dx[j, arc_idx] = dx[j, arc_idx] + h
                dy = np.dot(phi[-1], dx)
                f = bc_func(t_list[0][0], ya, [], t_list[-1][-1], yb + dy, [], p, aux)
                Ptemp[:,i] = (f-fx)/h
                dx[j, arc_idx] = dx[j, arc_idx] - h
                p[i] = p[i] - h
            P += Ptemp
            Ptemp = np.zeros((nBCs, p.size))

        J_i = P
        J_slice = slice(nOdes * num_arcs, nOdes * num_arcs + nParams)
        J[:, J_slice] = J_i

        return J

    def _bc_func_multiple_shooting(self, bc_func=None):
        def _bc_func(t0, y0, q0, tf, yf, qf, paramGuess, aux):
            bc1 = np.array(bc_func(t0, y0, q0, tf, yf, qf, paramGuess, aux)).flatten()
            narcs = y0.shape[1]
            bc2 = np.array([y0[:, ii + 1] - yf[:, ii] for ii in range(narcs - 1)]).flatten()
            bc = np.hstack((bc1,bc2))
            return bc

        def wrapper(t0, y0, q0, tf, yf, qf, paramGuess, aux):
            return _bc_func(t0, y0, q0, tf, yf, qf, paramGuess, aux)

        return wrapper

    @staticmethod
    def make_stmode(odefn, nOdes, StepSize=1e-6):
        Xh = np.eye(nOdes)*StepSize

        def _stmode_fd(t, _X, p, const, arc_idx):
            """ Finite difference version of state transition matrix """
            nParams = p.size
            F = np.empty((nOdes, nOdes+nParams))
            phi = _X[nOdes:].reshape((nOdes, nOdes+nParams))
            X = _X[0:nOdes]  # Just states

            # Compute Jacobian matrix, F using finite difference
            fx = np.squeeze([odefn(t, X, p, const, arc_idx)])

            for i in range(nOdes):
                fxh = odefn(t, X + Xh[i, :], p, const, arc_idx)
                F[:, i] = (fxh-fx)/StepSize

            for i in range(nParams):
                p[i] += StepSize
                fxh = odefn(t, X, p, const, arc_idx)
                F[:, i+nOdes] = (fxh - fx).real / StepSize
                p[i] -= StepSize

            phiDot = np.dot(np.vstack((F, np.zeros((nParams, nParams + nOdes)))), np.vstack((phi, np.hstack((np.zeros((nParams, nOdes)), np.eye(nParams))))))[:nOdes, :]
            return np.hstack((fx, np.reshape(phiDot, (nOdes * (nOdes + nParams)))))

        def wrapper(t, _X, p, const, arc_idx):  # needed for scipy
            return _stmode_fd(t, _X, p, const, arc_idx)
        return wrapper

    def solve(self, deriv_func, quad_func, bc_func, solinit):
        """
        Solve a two-point boundary value problem using the shooting method.

        :param deriv_func: The ODE function.
        :param quad_func: The quad func.
        :param bc_func: The boundary conditions function.
        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        """

        # Make a copy of sol and format inputs
        sol = copy.deepcopy(solinit)
        sol.t = np.array(sol.t, dtype=np.float64)
        sol.y = np.array(sol.y, dtype=np.float64)
        sol.parameters = np.array(sol.parameters, dtype=np.float64)

        # Extract some info from the guess structure
        y0g = sol.y[0, :]
        nOdes = y0g.shape[0]
        paramGuess = sol.parameters

        # Make the state-transition ode matrix
        self.stm_ode_func = self.make_stmode(deriv_func, y0g.shape[0])

        # Set up the boundary condition function
        self.bc_func = self._bc_func_multiple_shooting(bc_func=bc_func)

        if sol.arcs is None:
            sol.arcs = [(0, len(solinit.t)-1)]

        arc_seq = sol.aux['arc_seq']
        num_arcs = len(arc_seq)
        # if len(sol.arcs) % 2 == 0:
        #     raise Exception('Number of arcs must be odd!')

        # TODO: These are specific to an old implementation of path constraints see I51
        left_idx, right_idx = map(np.array, zip(*sol.arcs))
        ya = sol.y[left_idx, :]
        yb = sol.y[right_idx, :]
        tmp = np.arange(num_arcs+1, dtype=np.float32)*sol.t[-1] # TODO: I51
        tspan_list = [(a, b) for a, b in zip(tmp[:-1], tmp[1:])] # TODO: I51

        # sol.set_interpolate_function('cubic')
        ya = None
        tspan_list = []
        t0 = sol.t[0]
        ti = np.linspace(sol.t[0], sol.t[-1], self.num_arcs+1)
        for ii in range(len(ti)-1):
            tspan_list.append((t0, ti[ii+1]))
            if ya is None:
                ya = np.array([sol(t0)[0]])
            else:
                ya = np.vstack((ya, sol(t0)[0]))
            t0 = ti[ii+1]

        num_arcs = self.num_arcs

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
                t_list = []
                y_list = []
                if self.pool is None:
                    for arc_idx, tspan in enumerate(tspan_list):
                        y0stm[:nOdes] = ya[arc_idx, :]
                        y0stm[nOdes:] = stm0[:]
                        q0 = []
                        sol_ivp = prop(self.stm_ode_func, None, tspan, y0stm, q0, paramGuess, sol.aux, 0) # TODO: arc_idx is hardcoded as 0 here, this'll change with path constraints. I51
                        t = sol_ivp.t
                        yy = sol_ivp.y
                        y_list.append(yy[:, :nOdes])
                        t_list.append(t)
                        yb[arc_idx, :] = yy[-1, :nOdes]
                        phi_full = np.reshape(yy[:, nOdes:], (len(t), nOdes, nOdes+nParams))
                        phi_full_list.append(np.copy(phi_full))
                else:
                    raise NotImplementedError
                    y0stm = [np.hstack((ya[arc_idx, :],stm0[:])) for arc_idx, tspan in enumerate(tspan_list)]
                    q0 = []
                    sol_set = [self.pool.apply_async(prop, args=(self.stm_ode_func, None, tspan, y0s, q0, paramGuess, sol.aux, 0)) for tspan, y0s in zip(tspan_list, y0stm)]
                    sol_ivp = [traj.get() for traj in sol_set]
                    t_list = [s.t for s in sol_ivp]
                    y_list = [s.y for s in sol_ivp]
                    yb = [s.y[-1] for s in sol_ivp]
                    keyboard() # TODO: Parallelize multiple shooting. This is as far as I got.
                    for arc_idx, tspan in enumerate(tspan_list):
                        y0stm[:nOdes] = ya[arc_idx, :]
                        y0stm[nOdes:] = stm0[:]
                        q0 = []
                        sol_ivp = prop(self.stm_ode_func, None, tspan, y0stm, q0, paramGuess, sol.aux, 0)
                        t = sol_ivp.t
                        yy = sol_ivp.y
                        y_list.append(yy[:, :nOdes])
                        t_list.append(t)
                        yb[arc_idx, :] = yy[-1, :nOdes]
                        phi_full = np.reshape(yy[:, nOdes:], (len(t), nOdes, nOdes+nParams))
                        phi_full_list.append(np.copy(phi_full))

                # Break cycle if it exceeds the max number of iterations
                if n_iter > self.max_iterations:
                    logging.warning("Maximum iterations exceeded!")
                    break

                # Determine the error vector
                res = self.bc_func(t_list[0][0], ya.T, [], t_list[-1][-1], yb.T, [], paramGuess, sol.aux)

                # Break cycle if there are any NaNs in our error vector
                if any(np.isnan(res)):
                    print(res)
                    raise RuntimeError("Nan in residual")

                r1 = max(abs(res))
                logging.debug('Residual: ' + str(r1))

                if r1 > self.max_error:
                    raise RuntimeError('Error exceeded max_error')

                # Solution converged if BCs are satisfied to tolerance
                if r1 <= self.tolerance and n_iter > 1:
                    logging.info("Converged in "+str(n_iter)+" iterations.")
                    converged = True
                    break

                # Compute Jacobian of boundary conditions
                nBCs = len(res)
                J = self._bc_jac_multi(t_list, nBCs, phi_full_list, y_list, paramGuess, sol.aux, self.bc_func)

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
                if r1 < min(10*self.tolerance, 1e-3):
                    alpha, beta = 1, 1

                try:
                    dy0 = alpha*beta*np.linalg.solve(J, -res)
                except:
                    dy0, *_ = np.linalg.lstsq(J, -res)
                    dy0 = alpha*beta*dy0

                # Apply corrections to states and parameters (if any)
                d_ya = np.reshape(dy0[:nOdes * num_arcs], (num_arcs, nOdes), order='C')

                if nParams > 0:
                    dp = dy0[nOdes * num_arcs:]
                    paramGuess += dp
                    ya = ya + d_ya
                else:
                    ya = ya + d_ya

                n_iter += 1
                logging.debug('Iteration #' + str(n_iter))

        except Exception as e:
            logging.warning(e)
            import traceback
            traceback.print_exc()

        if converged:
            sol.arcs = []
            timestep_ctr = 0
            for arc_idx, tt in enumerate(t_list):
                sol.arcs.append((timestep_ctr, timestep_ctr+len(tt)-1))

            sol.t = np.hstack(t_list)
            sol.y = np.row_stack(y_list)
            sol.parameters = paramGuess

        else:
            # Return a copy of the original guess if the problem fails to converge
            sol = copy.deepcopy(solinit)

        sol.converged = converged
        return sol
