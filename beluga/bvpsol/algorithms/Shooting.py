import logging
import numpy as np

from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Propagator, Trajectory, reconstruct
from scipy.optimize import minimize
import copy


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
    | algorithm              | {'SLSQP'}       | see `scipy.optimize.minimize` |
    +------------------------+-----------------+-----------------+
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
    @staticmethod
    def _wrap_y0(gamma_set, parameters, nondynamical_parameters):
        n_odes = len(gamma_set[0].y[0])
        n_quads = len(gamma_set[0].q[0])
        n_dynparams = len(parameters)
        n_nondynparams = len(nondynamical_parameters)
        out = np.zeros(len(gamma_set) * n_odes + n_quads + n_dynparams + n_nondynparams)

        ii = 0
        for trajectory in gamma_set:
            for initial_pt in trajectory.y[0]:
                out[ii] = initial_pt
                ii += 1

        for initial_pt in gamma_set[0].q[0]:
            out[ii] = initial_pt
            ii += 1

        for initial_pt in parameters:
            out[ii] = initial_pt
            ii += 1

        for initial_pt in nondynamical_parameters:
            out[ii] = initial_pt
            ii += 1
        return out

    @staticmethod
    def _unwrap_y0(X, n_odes, n_quads, n_dynparams, n_arcs):
        y0 = np.reshape(X[:n_odes * n_arcs], (n_arcs, n_odes), order='C')
        q0 = X[n_odes * n_arcs:n_odes * n_arcs + n_quads]
        dparams = X[n_odes * n_arcs + n_quads:n_odes * n_arcs + n_quads + n_dynparams]
        dnonparams = X[n_odes * n_arcs + n_dynparams + n_quads:]
        return y0, q0, dparams, dnonparams

    def _propagate_gammas(self, gamma_set, paramGuess, sol, prop, pool, nOdes, nquads, nParams):
        tspan = []
        y0g = []
        q0g = []
        for ii in range(len(gamma_set)):
            _y0g, _q0g, _u0g = gamma_set[ii](gamma_set[ii].t[0])
            tspan.append(copy.copy(gamma_set[ii].t))
            y0g.append(copy.copy(_y0g))
            q0g.append(copy.copy(_q0g))

        def preload(args):
            return prop(self.derivative_function, self.quadrature_function, args[0], args[1], args[2], paramGuess, sol.aux)

        if pool is not None:
            gamma_set_new = pool.map(preload, zip(tspan, y0g, q0g))
        else:
            gamma_set_new = [preload([T, Y, Q]) for T, Y, Q in zip(tspan, y0g, q0g)]

        for ii in range(len(gamma_set_new)):
            t_set = gamma_set_new[ii].t
            y_set = gamma_set_new[ii].y
            q_set = gamma_set_new[ii].q
            u_set = gamma_set_new[ii].u
            gamma_set[ii] = Trajectory(t_set, y_set, q_set, u_set)

        if ii > 0 and nquads > 0:
            qdiff = gamma_set[ii - 1].q[-1] - gamma_set[ii].q[0]
            gamma_set[ii].q += qdiff
        return gamma_set

    def _propagate_gammas_and_stt(self, gamma_set, y0stm, stm0, paramGuess, sol, prop, pool, nOdes, nquads, nParams):
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
        else:
            gamma_set_new = [preload([T, Y, Q]) for T, Y, Q in zip(tspan, y0g, q0g)]

        for ii in range(len(gamma_set_new)):
            t_set = gamma_set_new[ii].t
            temp = gamma_set_new[ii].y
            y_set = temp[:, :nOdes]
            q_set = gamma_set_new[ii].q
            u_set = gamma_set_new[ii].u
            gamma_set_new[ii] = Trajectory(t_set, y_set, q_set, u_set)
            phi_temp = np.reshape(temp[:, nOdes:], (len(gamma_set_new[ii].t), nOdes, nOdes + nParams))
            phi_full_list.append(np.copy(phi_temp))

        if ii > 0 and nquads > 0:
            qdiff = gamma_set_new[ii - 1].q[-1] - gamma_set_new[ii].q[0]
            gamma_set_new[ii].q += qdiff
        return gamma_set_new, phi_full_list

    def __new__(cls, *args, **kwargs):
        obj = super(Shooting, cls).__new__(cls, *args, **kwargs)

        obj.algorithm = kwargs.get('algorithm', 'SLSQP')
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
                dx[kk] = dx[kk] - h
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

        parameter_guess = sol.dynamical_parameters
        nondynamical_parameter_guess = sol.nondynamical_parameters

        # Get some info on the size of the problem
        n_odes = y0g.shape[0]
        n_quads = q0g.shape[0]
        if sol.dynamical_parameters is None:
            n_dynparams = 0
        else:
            n_dynparams = sol.dynamical_parameters.shape[0]
        n_nondynparams = nondynamical_parameter_guess.shape[0]


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

        # Initial state of STM is an identity matrix with an additional column of zeros per parameter
        stm0 = np.hstack((np.eye(n_odes), np.zeros((n_odes, n_dynparams)))).reshape(n_odes*(n_odes + n_dynparams))

        prop = Propagator(**self.ivp_args)
        y0stm = np.zeros((len(stm0) + n_odes))

        converged = False  # Convergence flag
        n_iter = 0  # Initialize iteration counter
        err = -1

        bypass = True
        if bypass:
            # Set up the initial guess vector
            Xinit = self._wrap_y0(gamma_set, parameter_guess, nondynamical_parameter_guess)

            # Set up the constraint function
            def _constraint_function(X, n_odes, n_quads, n_dynparams, n_nondynparams, n_arcs, aux):
                g = copy.copy(gamma_set)
                _y, _q, _params, _nonparams = self._unwrap_y0(X, n_odes, n_quads, n_dynparams, n_arcs)
                for ii in range(n_arcs):
                    g[ii].y[0] = _y[ii]
                    if n_quads > 0:
                        g[ii].q[0] = _q
                g = self._propagate_gammas(g, _params, sol, prop, pool, n_odes, n_quads, n_dynparams)
                return self.bc_func_ms(g, _params, _nonparams, aux)
            _constraint_function_wrapper = lambda X: _constraint_function(X, n_odes, n_quads, n_dynparams, n_nondynparams, self.num_arcs, sol.aux)

            # Set up the jacobian of the constraint function
            def _jacobian_function(X, n_odes, n_quads, n_dynparams, n_nondynparams, n_arcs, aux):
                g = copy.deepcopy(gamma_set)
                _y, _q, _params, _nonparams = self._unwrap_y0(X, n_odes, n_quads, n_dynparams, n_arcs)
                for ii in range(self.num_arcs):
                    g[ii].y[0] = _y[ii]
                    if n_quads > 0:
                        g[ii].q[0] = _q

                g, phi_full_list = self._propagate_gammas_and_stt(g, y0stm, stm0, _params, sol, prop, pool, n_odes, n_quads, n_dynparams)
                J = self._bc_jac_multi(g, phi_full_list, _params, _nonparams, sol.aux, self.quadrature_function, self.bc_func_ms, StepSize=1e-6)
                return J
            _jacobian_function_wrapper = lambda X: _jacobian_function(X, n_odes, n_quads, n_dynparams, n_nondynparams, self.num_arcs, sol.aux)
            constraint = {'type': 'eq', 'fun': _constraint_function_wrapper, 'jac':_jacobian_function_wrapper}

            # Set up the cost function. This should just return 0 unless the specified method cannot handle constraints
            cost = lambda x: 0
            if not (self.algorithm == 'COBYLA' or self.algorithm == 'SLSQP' or self.algorithm == 'trust-constr'):
                cost = lambda x: np.linalg.norm(_constraint_function_wrapper(x)) ** 2

            # This runs the actual
            opt = minimize(cost, Xinit, method=self.algorithm, tol=self.tolerance, constraints=[constraint], options={'maxiter':self.max_iterations})

            # Unwrap the solution from the solver to put in a readable format
            y, q, parameter_guess, nondynamical_parameter_guess = self._unwrap_y0(opt.x, n_odes, n_quads, n_dynparams, self.num_arcs)
            for ii in range(self.num_arcs):
                gamma_set[ii].y[0] = y[ii]
                if n_quads > 0:
                    gamma_set[ii].q[0] = q
            gamma_set = self._propagate_gammas(gamma_set, parameter_guess, sol, prop, pool, n_odes, n_quads, n_dynparams)
            n_iter = opt.nit
            converged = opt.success

        while not converged and n_iter <= self.max_iterations and err < self.max_error:
            # Begin by propagating the full trajectory and STT
            gamma_set, phi_full_list = self._propagate_gammas_and_stt(gamma_set, y0stm, stm0, parameter_guess, sol, prop, pool, nOdes, nquads, nParams)

            # Determine the error vector
            residual = self.bc_func_ms(gamma_set, parameter_guess, nondynamical_parameter_guess, sol.aux)

            # Break cycle if there are any NaNs in our error vector
            if any(np.isnan(residual)):
                raise RuntimeError("Nan in residual")
            err = np.linalg.norm(residual)
            logging.debug('Residual: ' + str(err))

            nBCs = len(residual)

            J = self._bc_jac_multi(gamma_set, phi_full_list, parameter_guess, nondynamical_parameter_guess, sol.aux, self.quadrature_function, self.bc_func_ms)
            correction_vector = np.linalg.solve(J, -residual)

            def minfun(x):
                g = copy.deepcopy(gamma_set)
                dy0 = x*correction_vector
                _dy, _dq, _dparams, _dnonparams = self._dy0_to_corrections(dy0, nOdes, nquads, nParams, self.num_arcs)
                for ii in range(self.num_arcs):
                    g[ii].y[0] += _dy[ii]
                    if nquads > 0:
                        g[ii].q[0] += _dq
                _p1 = parameter_guess + _dparams
                _p2 = nondynamical_parameter_guess + _dnonparams
                g = self._propagate_gammas(g, _p1, sol, prop, pool, nOdes, nquads, nParams)
                return np.linalg.norm(self.bc_func_ms(g, _p1, _p2, sol.aux))**2

            opt = minimize(minfun, np.array([1]), args=(), method='Nelder-Mead', tol=1e-3)
            scale = opt.x
            # breakpoint()

            # # Compute correction vector
            # beta = 1
            # if err > 1:
            #     alpha = 1/(2*err)
            # else:
            #     alpha = 1

            # # No damping if error within one order of magnitude of tolerance
            # if err < min(10*self.tolerance, 1e-3):
            #     alpha, beta = 1, 1

            try:
                dy0 = scale*np.linalg.solve(J, -residual)
            except:
                dy0, *_ = np.linalg.lstsq(J, -residual)
                dy0 = scale*dy0

            # Apply corrections to states, quads, and parameters
            dy, dq, dparams, dnonparams = self._dy0_to_corrections(dy0, nOdes, nquads, nParams, self.num_arcs)
            for ii in range(self.num_arcs):
                gamma_set[ii].y[0] += dy[ii]
                if nquads > 0:
                    gamma_set[ii].q[0] += dq

            parameter_guess += dparams
            nondynamical_parameter_guess += dnonparams
            n_iter += 1
            logging.debug('Iteration #' + str(n_iter))

            # Solution converged if BCs are satisfied to tolerance
            if err <= self.tolerance:
                converged = True

        # Post loop checks
        if n_iter > self.max_iterations:
            logging.warning('Max iterations exceeded.')

        if err > self.max_error:
            raise RuntimeError('Error exceeded max_error')

        if err < self.tolerance:
            logging.info("Converged in " + str(n_iter) + " iterations.")

        sol.t = np.hstack([g.t for g in gamma_set])
        sol.y = np.vstack([g.y for g in gamma_set])
        sol.q = np.vstack([g.q for g in gamma_set])
        sol.dynamical_parameters = parameter_guess
        sol.nondynamical_parameters = nondynamical_parameter_guess
        sol.converged = converged
        return sol
