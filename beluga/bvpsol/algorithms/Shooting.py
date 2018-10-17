import copy
import itertools as it
import logging
import numpy as np

from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Propagator, integrate_quads, Trajectory, reconstruct
from beluga.bvpsol import Solution
import multiprocessing_on_dill as multiprocessing
import pathos
from multiprocessing import Pool
import copy
import dill


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

    """

    def __new__(cls, *args, **kwargs):
        obj = super(Shooting, cls).__new__(cls, *args, **kwargs)

        obj.ivp_args = kwargs.get('ivp_args', dict())
        obj.tolerance = kwargs.get('tolerance', 1e-4)
        obj.max_error = kwargs.get('max_error', 100)
        obj.max_iterations = kwargs.get('max_iterations', 100)
        obj.num_arcs = kwargs.get('num_arcs', 1)

        obj.stm_ode_func = None
        obj.bc_func_ms = None

        return obj

    def __init__(self, *args, **kwargs):
        # Set up the boundary condition function
        if self.boundarycondition_function is not None:
            self.bc_func_ms = self._bc_func_multiple_shooting(bc_func=self.boundarycondition_function)

    def _bc_jac_multi(self, gamma_set, phi_full_list, parameters, nondynamical_params, aux, quad_func, bc_func, StepSize=1e-6):
        h = StepSize
        t0 = gamma_set[0].t[0]
        y0, q0, u0 = gamma_set[0](t0)
        tf = gamma_set[-1].t[-1]
        yf, qf, uf = gamma_set[-1](tf)

        gamma_set_perturbed = copy.copy(gamma_set)

        nOdes = len(y0)
        nquads = len(q0)
        num_arcs = len(gamma_set)

        fx = bc_func(gamma_set, parameters, nondynamical_params, aux)
        nBCs = len(fx)

        M = np.zeros((nBCs, nOdes))
        Q = np.zeros((nBCs, nquads))
        P1 = np.zeros((nBCs, parameters.size))
        P2 = np.zeros((nBCs, nondynamical_params.size))
        Ptemp = np.zeros((nBCs, parameters.size))
        J = np.zeros((nBCs, (nOdes)*num_arcs))
        dx = np.zeros((nOdes + parameters.size))

        for ii, phi in zip(range(len(gamma_set)), phi_full_list):
            for jj in range(nOdes):
                dx[jj] = dx[jj] + h
                dy = np.dot(phi, dx)
                perturbed_trajectory = Trajectory(gamma_set[ii].t, gamma_set[ii].y + dy)
                if nquads > 0:
                    perturbed_trajectory = reconstruct(quad_func, perturbed_trajectory, gamma_set[ii].q[0], parameters, aux)

                gamma_set_perturbed[ii] = perturbed_trajectory
                f = bc_func(gamma_set_perturbed, parameters, nondynamical_params, aux)
                gamma_set_perturbed[ii] = copy.copy(gamma_set[ii])
                M[:, jj] = (f-fx)/h
                dx[jj] = dx[jj] - h
            J_i = M
            J_slice = slice(nOdes * ii, nOdes * (ii + 1))
            J[:, J_slice] = J_i

        dq = np.zeros(nquads)
        for ii in range(nquads):
            dq[ii] = dq[ii] + h
            gamma_set_perturbed = [Trajectory(g.t, g.y, g.q + dq) for g in gamma_set]
            f = bc_func(gamma_set_perturbed, parameters, nondynamical_params, aux)
            Q[:, ii] = (f-fx)/h
            dq[ii] = dq[ii] - h

        gamma_set_perturbed = copy.copy(gamma_set)
        for ii, phi in zip(range(len(gamma_set)), phi_full_list):
            for jj in range(parameters.size):
                parameters[jj] = parameters[jj] + h
                kk = jj + nOdes
                dx[kk] = dx[kk] + h
                dy = np.dot(phi, dx)
                perturbed_trajectory = Trajectory(gamma_set[ii].t, gamma_set[ii].y + dy)
                if nquads > 0:
                    perturbed_trajectory = reconstruct(quad_func, perturbed_trajectory, gamma_set[ii].q[0], parameters, aux)

                gamma_set_perturbed[ii] = perturbed_trajectory
                f = bc_func(gamma_set_perturbed, parameters, nondynamical_params, aux)
                gamma_set_perturbed[ii] = copy.copy(gamma_set[ii])
                Ptemp[:, jj] = (f-fx)/h
                dx[jj] = dx[jj] - h
                parameters[jj] = parameters[jj] - h
            P1 += Ptemp
            Ptemp = np.zeros((nBCs, parameters.size))

        Ptemp = np.zeros((nBCs, nondynamical_params.size))
        for ii in range(nondynamical_params.size):
            nondynamical_params[ii] = nondynamical_params[ii] + h
            f = bc_func(gamma_set, parameters, nondynamical_params, aux)
            Ptemp[:, ii] = (f-fx)/h
            nondynamical_params[ii] = nondynamical_params[ii] - h
        P2 += Ptemp

        return np.hstack((J, Q, P1, P2))

    def _bc_func_multiple_shooting(self, bc_func=None):
        def _bc_func(gamma_set, paramGuess, nondynamical_parameters, *args):
            t0 = gamma_set[0].t[0]
            y0, q0, u0 = gamma_set[0](t0)
            tf = gamma_set[-1].t[-1]
            yf, qf, uf = gamma_set[-1](tf)
            bc1 = np.array(bc_func(t0, y0, q0, tf, yf, qf, paramGuess, nondynamical_parameters, *args)).flatten()
            bc2 = np.array([gamma_set[ii].y[-1] - gamma_set[ii+1].y[0] for ii in range(len(gamma_set) - 1)]).flatten()
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

    def solve(self, solinit, **kwargs):
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

        pool = kwargs.get('pool', None)

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

        # Build each of the separate arcs for multiple shooting. Uses sol's interpolation style
        gamma_set = []
        t0 = sol.t[0]
        tf = sol.t[-1]
        tn = np.linspace(t0, tf, self.num_arcs+1)

        for trajectory_number in range(self.num_arcs):
            y0t, q0t, u0t = sol(tn[trajectory_number])
            yft, qft, uft = sol(tn[trajectory_number+1])
            t_set = np.hstack((tn[trajectory_number], tn[trajectory_number+1]))
            y_set = np.vstack((y0t, yft))
            q_set = np.vstack((q0t, qft))
            u_set = np.vstack((u0t, uft))
            gamma_set.append(Trajectory(t_set, y_set, q_set, u_set))

        if sol.dynamical_parameters is None:
            nParams = 0
        else:
            nParams = sol.dynamical_parameters.size

        # Initial state of STM is an identity matrix with an additional column of zeros per parameter
        stm0 = np.hstack((np.eye(nOdes), np.zeros((nOdes,nParams)))).reshape(nOdes*(nOdes+nParams))

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley # TODO: Reference this in the docstring
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None
        prop = Propagator(**self.ivp_args)
        y0stm = np.zeros((len(stm0)+nOdes))

        n_iter = 1  # Initialize iteration counter
        converged = False  # Convergence flag
        try:
            while True:
                phi_full_list = []
                tspan = []
                y0g = []
                q0g = []
                for ii in range(len(gamma_set)):
                    _y0g, _q0g, _u0g = gamma_set[ii](gamma_set[ii].t[0])
                    y0stm[:nOdes] = _y0g
                    y0stm[nOdes:] = stm0[:]
                    tspan.append(copy.copy(gamma_set[ii].t))
                    y0g.append(copy.copy(y0stm))
                    q0g.append(copy.copy(_q0g))

                def preload(args):
                    return prop(self.stm_ode_func, self.quadrature_function, args[0], args[1], args[2], paramGuess, sol.aux)

                if pool is not None:
                    gamma_set_new = pool.map(preload, zip(tspan, y0g, q0g))
                    # _results = [pool.apply_async(preload, [(T,Y,Q)]) for T,Y,Q in zip(tspan, y0g, q0g)]
                    # gamma_set_new = [result.get() for result in _results]
                else:
                    gamma_set_new = [preload([T, Y, Q]) for T,Y,Q in zip(tspan, y0g, q0g)]

                for ii in range(len(gamma_set_new)):
                    t_set = gamma_set_new[ii].t
                    y_set = gamma_set_new[ii].y[:, :nOdes]
                    q_set = gamma_set_new[ii].q
                    u_set = gamma_set_new[ii].u
                    gamma_set[ii] = Trajectory(t_set, y_set, q_set, u_set)
                    phi_temp = np.reshape(gamma_set_new[ii].y[:, nOdes:], (len(gamma_set_new[ii].t), nOdes, nOdes + nParams))
                    phi_full_list.append(np.copy(phi_temp))

                if ii > 0 and nquads > 0:
                    qdiff = gamma_set[ii-1].q[-1] - gamma_set[ii].q[0]
                    gamma_set[ii].q += qdiff



                # Break cycle if it exceeds the max number of iterations
                if n_iter > self.max_iterations:
                    logging.warning("Maximum iterations exceeded!")
                    break

                # Determine the error vector
                res = self.bc_func_ms(gamma_set, paramGuess, nondynamical_parameter_guess, sol.aux)

                # Break cycle if there are any NaNs in our error vector
                if any(np.isnan(res)):
                    print(res)
                    raise RuntimeError("Nan in residual")

                r1 = max(abs(res))
                r1 = np.linalg.norm(res)
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

                J = self._bc_jac_multi(gamma_set, phi_full_list, paramGuess, nondynamical_parameter_guess, sol.aux, self.quadrature_function, self.bc_func_ms)

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
                d_ya = np.reshape(dy0[:nOdes * self.num_arcs], (self.num_arcs, nOdes), order='C')
                dq = dy0[nOdes * self.num_arcs:nOdes * self.num_arcs + nquads]
                for ii in range(self.num_arcs):
                    gamma_set[ii].y[0] += d_ya[ii,:]
                    if nquads > 0:
                        gamma_set[ii].q[0] += dq

                dp1 = dy0[nOdes * self.num_arcs + nquads:nOdes * self.num_arcs + nquads + paramGuess.size]
                dp2 = dy0[nOdes * self.num_arcs + paramGuess.size + nquads:]
                paramGuess += dp1
                nondynamical_parameter_guess += dp2
                n_iter += 1
                logging.debug('Iteration #' + str(n_iter))

        except Exception as e:
            logging.warning(e)
            import traceback
            traceback.print_exc()

        if converged:
            sol.t = np.hstack([g.t for g in gamma_set])
            sol.y = np.vstack([g.y for g in gamma_set])
            sol.q = np.vstack([g.q for g in gamma_set])
            sol.dynamical_parameters = paramGuess
            sol.nondynamical_parameters = nondynamical_parameter_guess

        else:
            # Return a copy of the original guess if the problem fails to converge
            sol = copy.deepcopy(solinit)

        sol.converged = converged
        return sol
