import copy
import itertools as it
import logging
import numpy as np

from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Propagator, integrate_quads, Trajectory, reconstruct
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

        obj.ivp_args = kwargs.get('ivp_args', dict())
        obj.tolerance = kwargs.get('tolerance', 1e-4)
        obj.max_error = kwargs.get('max_error', 100)
        obj.max_iterations = kwargs.get('max_iterations', 100)
        obj.num_arcs = kwargs.get('num_arcs', 1)
        obj.num_cpus = kwargs.get('num_cpus', 1)

        obj.pool = None
        obj.stm_ode_func = None
        obj.bc_func_ms = None

        return obj

    def __init__(self, *args, **kwargs):
        # Set up the boundary condition function
        if self.boundarycondition_function is not None:
            self.bc_func_ms = self._bc_func_multiple_shooting(bc_func=self.boundarycondition_function)

        if self.num_cpus > 1:
            self.pool = pool.Pool(processes=self.num_cpus)

    def _bc_jac_multi(self, t_list, phi_full_list, y_list, q_list, parameters, nondynamical_params, aux, quad_func, bc_func, StepSize=1e-6):
        parameters = np.array(parameters)
        h = StepSize
        t0 = t_list[0][0]
        tf = t_list[-1][-1]
        y0 = np.array([traj[0] for traj in y_list])[0]
        yf = np.array([traj[-1] for traj in y_list])[0]
        nquads = q_list[0].shape[1]

        if nquads > 0:
            q0 = q_list[0][0]
            qf = q_list[-1][-1]
        else:
            q0 = []
            qf = []
        nOdes = y0.shape[0]
        num_arcs = len(phi_full_list)

        fx = bc_func(t_list, y_list, q_list, parameters, nondynamical_params, aux)
        nBCs = len(fx)

        M = np.zeros((nBCs, nOdes))
        Q = np.zeros((nBCs, nquads))
        P1 = np.zeros((nBCs, parameters.size))
        P2 = np.zeros((nBCs, nondynamical_params.size))
        Ptemp = np.zeros((nBCs, parameters.size))
        J = np.zeros((nBCs, (nOdes)*num_arcs))
        dx = np.zeros((nOdes + parameters.size, num_arcs))

        for arc_idx, phi in zip(it.count(), phi_full_list):
            for ii in range(nOdes):
                dx[ii, arc_idx] = dx[ii, arc_idx] + h
                dy = np.dot(phi, dx)
                breakpoint()
                gamma = Trajectory(np.hstack(t_list), np.vstack(y_list) + dy[:,:,arc_idx])
                if nquads > 0:
                    gamma = reconstruct(quad_func, gamma, q0, parameters, aux)
                    f = bc_func(t0, gamma.y[0], gamma.q[0], tf, gamma.y[-1], gamma.q[-1], parameters, nondynamical_params, aux)
                else:
                    f = bc_func(t0, gamma.y[0], [], tf, gamma.y[-1], [], parameters, nondynamical_params, aux)
                M[:, ii] = (f-fx)/h
                dx[ii, arc_idx] = dx[ii, arc_idx] - h
            J_i = M
            J_slice = slice(nOdes*arc_idx, nOdes*(arc_idx+1))
            J[:,J_slice] = J_i

        dq = np.zeros(nquads)
        for ii in range(nquads):
            dq[ii] = dq[ii] + h
            f = bc_func(t0, y0, q0 + dq, tf, yf, qf + dq, parameters, nondynamical_params, aux)
            Q[:, ii] = (f-fx)/h
            dq[ii] = dq[ii] - h

        for arc_idx, phi in zip(it.count(), phi_full_list):
            for ii in range(parameters.size):
                parameters[ii] = parameters[ii] + h
                jj = ii + nOdes
                dx[jj, arc_idx] = dx[jj, arc_idx] + h
                dy = np.dot(phi, dx)
                gamma = Trajectory(np.hstack(t_list), np.vstack(y_list) + dy[:, :, arc_idx])
                if nquads > 0:
                    gamma = reconstruct(quad_func, gamma, q0, parameters, aux)
                    f = bc_func(t0, gamma.y[0], gamma.q[0], tf, gamma.y[-1], gamma.q[-1], parameters, nondynamical_params, aux)
                else:
                    f = bc_func(t0, gamma.y[0], [], tf, gamma.y[-1], [], parameters, nondynamical_params, aux)
                Ptemp[:, ii] = (f-fx)/h
                dx[jj, arc_idx] = dx[jj, arc_idx] - h
                parameters[ii] = parameters[ii] - h
            P1 += Ptemp
            Ptemp = np.zeros((nBCs, parameters.size))

        Ptemp = np.zeros((nBCs, nondynamical_params.size))
        for ii in range(nondynamical_params.size):
            nondynamical_params[ii] = nondynamical_params[ii] + h
            if nquads > 0:
                f = bc_func(t0, y_list[0][0,:], q_list[0][0,:], tf, y_list[-1][-1,:], q_list[-1][-1,:], parameters, nondynamical_params, aux)
            else:
                f = bc_func(t0, y_list[0][0,:], [], tf, y_list[-1][-1,:], [], parameters, nondynamical_params, aux)
            Ptemp[:, ii] = (f-fx)/h
            nondynamical_params[ii] = nondynamical_params[ii] - h
        P2 += Ptemp

        return np.hstack((J, Q, P1, P2))

    def _bc_func_multiple_shooting(self, bc_func=None):
        def _bc_func(t_list, y_list, q_list, paramGuess, nondynamical_parameters, aux):
            bc1 = np.array(bc_func(t_list[0][0], y_list[0][0], q_list[0][0], t_list[-1][-1], y_list[-1][-1], q_list[-1][-1], paramGuess, nondynamical_parameters, aux)).flatten()
            narcs = len(y_list)
            bc2 = np.array([y_list[ii][-1] - y_list[ii+1][0] for ii in range(narcs - 1)]).flatten()
            bc = np.hstack((bc1,bc2))
            return bc
        return _bc_func

    @staticmethod
    def make_stmode(odefn, nOdes, StepSize=1e-6):
        Xh = np.eye(nOdes)*StepSize

        def _stmode_fd(t, _X, p, aux):
            """ Finite difference version of state transition matrix """
            nParams = p.size
            F = np.empty((nOdes, nOdes+nParams))
            phi = _X[nOdes:].reshape((nOdes, nOdes+nParams))
            X = _X[0:nOdes]  # Just states

            # Compute Jacobian matrix, F using finite difference
            fx = np.squeeze([odefn(t, X, p, aux)])

            for i in range(nOdes):
                fxh = odefn(t, X + Xh[i, :], p, aux)
                F[:, i] = (fxh-fx)/StepSize

            for i in range(nParams):
                p[i] += StepSize
                fxh = odefn(t, X, p, aux)
                F[:, i+nOdes] = (fxh - fx).real / StepSize
                p[i] -= StepSize

            phiDot = np.dot(np.vstack((F, np.zeros((nParams, nParams + nOdes)))), np.vstack((phi, np.hstack((np.zeros((nParams, nOdes)), np.eye(nParams))))))[:nOdes, :]
            return np.hstack((fx, np.reshape(phiDot, (nOdes * (nOdes + nParams)))))

        return _stmode_fd

    def solve(self, solinit):
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
        sol.q = np.array(sol.q, dtype=np.float64)
        sol.dynamical_parameters = np.array(sol.dynamical_parameters, dtype=np.float64)
        sol.nondynamical_parameters = np.array(sol.nondynamical_parameters, dtype=np.float64)

        # Extract some info from the guess structure
        y0g = sol.y[0, :]
        if self.quadrature_function is None or all(np.isnan(sol.q)):
            q0g = np.array([])
        else:
            q0g = sol.q[0, :]

        nOdes = y0g.shape[0]
        nquads = q0g.shape[0]
        paramGuess = sol.dynamical_parameters
        nondynamical_parameter_guess = sol.nondynamical_parameters

        # Make the state-transition ode matrix
        if self.stm_ode_func is None:
            self.stm_ode_func = self.make_stmode(self.derivative_function, y0g.shape[0])

        # Set up the boundary condition function
        if self.bc_func_ms is None:
            self.bc_func_ms = self._bc_func_multiple_shooting(bc_func=self.boundarycondition_function)

        if sol.arcs is None:
            sol.arcs = [(0, len(solinit.t)-1)]

        # sol.set_interpolate_function('cubic')
        ya = None
        qa = None
        tspan_list = []
        t0 = sol.t[0]
        ti = np.linspace(sol.t[0], sol.t[-1], self.num_arcs+1)

        for ii in range(len(ti)-1):
            tspan_list.append((t0, ti[ii+1]))
            if ya is None:
                ya = np.array([sol(t0)[0]])
                qa = np.array([sol(t0)[1]])
            else:
                ya = np.vstack((ya, sol(t0)[0]))
                qa = np.vstack((qa, sol(t0)[1]))

            t0 = ti[ii+1]

        num_arcs = self.num_arcs

        if solinit.dynamical_parameters is None:
            nParams = 0
        else:
            nParams = solinit.dynamical_parameters.size

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
        qb = np.zeros_like(qa)
        try:
            while True:
                phi_list = []
                phi_full_list = []
                t_list = []
                y_list = []
                q_list = []
                for arc_idx, tspan in enumerate(tspan_list):
                    y0stm[:nOdes] = ya[arc_idx, :]
                    q0g = qa[arc_idx, :]
                    y0stm[nOdes:] = stm0[:]
                    sol_ivp = prop(self.stm_ode_func, self.quadrature_function, tspan, y0stm, q0g, paramGuess, sol.aux)
                    t = sol_ivp.t
                    yy = sol_ivp.y
                    qq = sol_ivp.q
                    if arc_idx > 0:
                        qq += q_list[-1][-1]
                    t_list.append(t)
                    y_list.append(yy[:, :nOdes])
                    if nquads > 0:
                        q_list.append(qq[:, :nquads])
                    yb[arc_idx, :] = yy[-1, :nOdes]
                    qb[arc_idx, :] = qq[-1, :nOdes]
                    qb[arc_idx, :] = qq[-1]
                    phi_full = np.reshape(yy[:, nOdes:], (len(t), nOdes, nOdes+nParams))
                    phi_full_list.append(np.copy(phi_full))

                # Break cycle if it exceeds the max number of iterations
                if n_iter > self.max_iterations:
                    logging.warning("Maximum iterations exceeded!")
                    break

                # Determine the error vector
                res = self.bc_func_ms(t_list, y_list, q_list, paramGuess, nondynamical_parameter_guess, sol.aux)
                # if nquads == 0:
                #     res = self.bc_func_ms(t_list[0][0], ya[0], [], t_list[-1][-1], yb[0], [], paramGuess, nondynamical_parameter_guess, sol.aux)
                # else:
                #     res = self.bc_func_ms(t_list[0][0], ya[0], qq[0], t_list[-1][-1], yb[0], qq[-1], paramGuess, nondynamical_parameter_guess, sol.aux)

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

                J = self._bc_jac_multi(t_list, phi_full_list, y_list, q_list, paramGuess, nondynamical_parameter_guess, sol.aux, self.quadrature_function, self.bc_func_ms)

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

                # Apply corrections to states, quads, and parameters
                d_ya = np.reshape(dy0[:nOdes * num_arcs], (num_arcs, nOdes), order='C')
                dq = dy0[nOdes * num_arcs:nOdes * num_arcs + nquads]
                dp1 = dy0[nOdes * num_arcs + nquads:nOdes * num_arcs + nquads + paramGuess.size]
                dp2 = dy0[nOdes * num_arcs + paramGuess.size + nquads:]
                ya = ya + d_ya
                qa += dq
                paramGuess += dp1
                nondynamical_parameter_guess += dp2
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
            if nquads > 0:
                sol.q = np.row_stack(q_list)
            sol.dynamical_parameters = paramGuess
            sol.nondynamical_parameters = nondynamical_parameter_guess

        else:
            # Return a copy of the original guess if the problem fails to converge
            sol = copy.deepcopy(solinit)

        sol.converged = converged
        return sol
