import cloudpickle as pickle
import copy
import logging
import numpy as np
from math import isclose
from ._shooting import *

from beluga.bvpsol.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Propagator, Trajectory, reconstruct
from scipy.sparse import coo_matrix, csc_matrix
from scipy.sparse.linalg import splu
from scipy.optimize.slsqp import approx_jacobian
from scipy.optimize import minimize, root, fsolve
scipy_minimize_algorithms = {'Nelder-Mead', 'Powell', 'CG', 'BFGS', 'Newton-CG', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP',
                             'trust-constr', 'dogleg', 'trust-ncg', 'trust-exact', 'trust-krylov'}
scipy_root_algorithms = {'hybr', 'lm', 'broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden',
                         'excitingmixing', 'krylov', 'df-sane'}


class Shooting(BaseAlgorithm):
    r"""
    Reduced dimensional shooting algorithm for solving boundary value problems.

    Given a system of ordinary differential equations, define the sensitivities as

    .. math::
        A(\tau) =
        \left[\frac{\partial \mathbf{f}}{\partial \mathbf{x}}, \frac{\partial \mathbf{f}}{\partial \mathbf{p}}\right]

    Then, the state-transition matrix is defined as the following set of first-order differential equations

    .. math::
        \begin{aligned}
            \Delta_0 &= \left[Id_M, \mathbf{0}\right] \\
            \dot{\Delta} &= A(\tau)\Delta
        \end{aligned}

    Sensitivities of the boundary conditions are

    .. math::
        \begin{aligned}
            M &= \frac{\mathrm{d} \mathbf{\Phi}}{\mathrm{d} \mathbf{x}_0} \\
            Q &= \frac{\partial \mathbf{\Phi}}{\partial \mathbf{q}_0}
            + \frac{\partial \mathbf{\Phi}}{\partial \mathbf{q}_f} \\
            P_1 &= \frac{\mathrm{d} \mathbf{\Phi}}{\mathrm{d} \mathbf{p}} \\
            P_2 &= \frac{\partial \mathbf{\Phi}}{\partial \mathbf{\lambda}}
        \end{aligned}

    The Jacobian matrix is then the concatenation of these sensitivities

    .. math::
        J = \left[M, Q, P_1, P_2 \right]

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | algorithm              | 'Armijo'        | See note below. |
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

    The shooting solver uses 3rd party root-solvers to find numerical solutions. In addition to `Armijo`,
    the SciPy solvers `scipy.optimize.root`, `scipy.optimize.minimize`, `scipy.optimize.fsolve` are available.

    """
    def __init__(self, *args, **kwargs):

        BaseAlgorithm.__init__(self, *args, **kwargs)

        self.algorithm = kwargs.get('algorithm', 'Armijo')
        self.ivp_args = kwargs.get('ivp_args', dict())
        self.tolerance = kwargs.get('tolerance', 1e-4)
        self.max_error = kwargs.get('max_error', 100)
        self.max_iterations = kwargs.get('max_iterations', 100)
        self.num_arcs = kwargs.get('num_arcs', 1)

        self.stm_ode_func = None
        self.bc_func_ms = None

        # Set up the boundary condition function
        if self.boundarycondition_function is not None:
            self.bc_func_ms = self._bc_func_multiple_shooting(bc_func=self.boundarycondition_function)

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
    def _unwrap_y0(xx, n_odes, n_quads, n_dynparams, n_arcs):
        y0 = np.reshape(xx[:n_odes * n_arcs], (n_arcs, n_odes), order='C')
        q0 = xx[n_odes * n_arcs:n_odes * n_arcs + n_quads]
        dparams = xx[n_odes * n_arcs + n_quads:n_odes * n_arcs + n_quads + n_dynparams]
        dnonparams = xx[n_odes * n_arcs + n_dynparams + n_quads:]
        return y0, q0, dparams, dnonparams

    @staticmethod
    def _make_gammas(derivative_function, quadrature_function, gamma_set, param_guess, sol, prop, pool, nquads):
        n_arcs = len(gamma_set)
        tspan = [None]*n_arcs
        y0g = [None]*n_arcs
        q0g = [None]*n_arcs
        u0g = [None]*n_arcs
        for ii in range(len(gamma_set)):
            _y0g, _q0g, _u0g = gamma_set[ii](gamma_set[ii].t[0])
            tspan[ii] = gamma_set[ii].t
            y0g[ii] = _y0g
            q0g[ii] = _q0g
            u0g[ii] = _u0g

        def preload(args):
            return prop(derivative_function, quadrature_function, args[0], args[1], args[2], args[3],
                        param_guess, sol.const)

        if pool is not None:
            gamma_set_new = pool.map(preload, zip(tspan, y0g, q0g))
        else:
            gamma_set_new = [preload([T, Y, Q, U]) for T, Y, Q, U in zip(tspan, y0g, q0g, u0g)]

        if n_arcs > 1 and nquads > 0:
            for ii in range(n_arcs-1):
                qdiff = gamma_set_new[ii].q[-1] - gamma_set_new[ii+1].q[0]
                gamma_set_new[ii+1].q += qdiff

        return gamma_set_new

    @staticmethod
    def _make_gammas_parallel(derivative_function, quadrature_function, gamma_set, param_guess, sol, prop, pool,
                              nquads):
        n_arcs = len(gamma_set)
        tspan = [None] * n_arcs
        y0g = [None] * n_arcs
        q0g = [None] * n_arcs
        for ii in range(len(gamma_set)):
            _y0g, _q0g, _u0g = gamma_set[ii](gamma_set[ii].t[0])
            tspan[ii] = gamma_set[ii].t
            y0g[ii] = _y0g
            q0g[ii] = _q0g

        def preload(args):
            return prop(pickle.loads(derivative_function), pickle.loads(quadrature_function), args[0], args[1], args[2],
                        param_guess, sol.const)

        if pool is not None:
            gamma_set_new = pool.map(preload, zip(tspan, y0g, q0g))
        else:
            gamma_set_new = [preload([T, Y, Q]) for T, Y, Q in zip(tspan, y0g, q0g)]

        if n_arcs > 1 and nquads > 0:
            for ii in range(n_arcs - 1):
                qdiff = gamma_set_new[ii].q[-1] - gamma_set_new[ii + 1].q[0]
                gamma_set_new[ii + 1].q += qdiff

        return gamma_set_new

    @staticmethod
    def _bc_jac(gamma, phi_full, parameters, nondynamical_params, aux, quad_func, bc_func, step_size=1e-6):
        gamma_orig = copy.deepcopy(gamma)
        h = step_size
        t0 = gamma_orig.t[0]
        y0, q0, u0 = gamma_orig(t0)

        n_odes = len(y0)
        n_quads = len(q0)
        num_arcs = len(gamma_orig)
        fx = np.asarray(bc_func(gamma_orig.y[0], [], [], gamma_orig.y[-1], [], [], parameters, nondynamical_params, aux))
        n_bcs = len(fx)

        m = np.zeros((n_bcs, n_odes))
        q = np.zeros((n_bcs, n_quads))
        p1 = np.zeros((n_bcs, parameters.size))
        p2 = np.zeros((n_bcs, nondynamical_params.size))

        dx = np.zeros((n_odes + parameters.size))
        gamma_orig = copy.deepcopy(gamma)
        for jj in range(n_odes):
            dx[jj] = dx[jj] + h
            dy = np.dot(phi_full, dx)
            p = Trajectory(gamma_orig.t, gamma_orig.y + dy)
            f = np.asarray(bc_func(p.y[0], [], [], p.y[-1], [], [], parameters, nondynamical_params, aux))
            m[:, jj] = (f-fx)/h
            dx[jj] = dx[jj] - h

        # dq = np.zeros(n_quads)
        # for ii in range(n_quads):
        #     dq[ii] = dq[ii] + h
        #     gamma_set_perturbed = [Trajectory(g.t, g.y, g.q + dq) for g in gamma_orig]
        #     f = bc_func(gamma_set_perturbed, parameters, nondynamical_params, aux)
        #     q[:, ii] = (f-fx)/h
        #     dq[ii] = dq[ii] - h

        for ii in range(parameters.size):
            raise NotImplementedError
            gamma_set_perturbed = copy.deepcopy(gamma_orig)
            parameters[ii] = parameters[ii] + h
            jj = ii + n_odes
            dx[jj] = dx[jj] + h
            for kk, phi in zip(range(len(gamma_orig)), phi_full_list):
                dy = np.dot(phi, dx)
                perturbed_trajectory = Trajectory(gamma_orig[kk].t, gamma_orig[kk].y + dy)
                if n_quads > 0:
                    if kk > 0:
                        perturbed_trajectory = reconstruct(quad_func, perturbed_trajectory,
                                                           gamma_set_perturbed[kk-1].q[-1], parameters, aux)
                    else:
                        perturbed_trajectory = reconstruct(quad_func, perturbed_trajectory, gamma_orig[kk].q[0],
                                                           parameters, aux)

                gamma_set_perturbed[kk] = perturbed_trajectory

            f = bc_func(gamma_set_perturbed, parameters, nondynamical_params, aux)
            p1[:, ii] += (f-fx)/h
            dx[jj] = dx[jj] - h
            parameters[ii] = parameters[ii] - h

        for ii in range(nondynamical_params.size):
            nondynamical_params[ii] = nondynamical_params[ii] + h
            f = bc_func(gamma_orig, parameters, nondynamical_params, aux)
            p2[:, ii] = (f-fx)/h
            nondynamical_params[ii] = nondynamical_params[ii] - h

        jac = np.hstack((m, q, p1, p2))
        return jac

    @staticmethod
    def _bc_func_multiple_shooting(bc_func=None):
        def _bc_func(gamma_set, param_guess, _, k, *args):
            t0 = gamma_set[0].t[0]
            y0, q0, u0 = gamma_set[0](t0)
            tf = gamma_set[-1].t[-1]
            yf, qf, uf = gamma_set[-1](tf)
            bc1 = np.asarray([gamma_set[ii].y[-1] - gamma_set[ii + 1].y[0] for ii in range(len(gamma_set) - 1)]).flatten()
            bc2 = np.asarray(bc_func(y0, q0, u0, yf, qf, uf, param_guess[:k], param_guess[k:], *args)).flatten()
            bc = np.hstack((bc1, bc2))
            return bc
        return _bc_func

    @staticmethod
    def make_stmode(odefn, n_odes, step_size=1e-6):
        xh = np.eye(n_odes)*step_size

        def _stmode_fd(_xx, u, p, aux):
            """ Finite difference version of state transition matrix """
            n_params = p.size
            ff = np.empty((n_odes, n_odes+n_params))
            phi = _xx[n_odes:].reshape((n_odes, n_odes+n_params))
            xx = _xx[0:n_odes]  # Just states

            # Compute Jacobian matrix, F using finite difference
            fx = np.squeeze([odefn(xx, u, p, aux)])

            for i in range(n_odes):
                fxh = odefn(xx + xh[i, :], u, p, aux)
                ff[:, i] = (fxh-fx) / step_size

            for i in range(n_params):
                p[i] += step_size
                fxh = odefn(xx, u, p, aux)
                ff[:, i+n_odes] = (fxh - fx) / step_size
                p[i] -= step_size

            phi_dot = np.dot(np.vstack((ff, np.zeros((n_params, n_params + n_odes)))),
                             np.vstack((phi, np.hstack((np.zeros((n_params, n_odes)), np.eye(n_params))))))[:n_odes, :]
            return np.hstack((fx, np.reshape(phi_dot, (n_odes * (n_odes + n_params)))))

        return _stmode_fd

    def solve(self, solinit, **kwargs):
        """
        Solve a two-point boundary value problem using the shooting method.

        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        """

        # Make a copy of sol and format inputs
        sol = copy.deepcopy(solinit)
        sol.t = np.array(sol.t, dtype=np.float64)
        sol.y = np.array(sol.y, dtype=np.float64)
        if np.issubdtype(sol.y.dtype, np.complexfloating):
            dtype = complex
        else:
            dtype = float
        sol.q = np.array(sol.q, dtype=np.float64)
        sol.dynamical_parameters = np.array(sol.dynamical_parameters, dtype=np.float64)
        sol.nondynamical_parameters = np.array(sol.nondynamical_parameters, dtype=np.float64)

        n = sol.y[0].shape[0]
        k = sol.dynamical_parameters.shape[0]
        sol.dynamical_parameters = np.hstack((sol.dynamical_parameters, sol.nondynamical_parameters))
        sol.nondynamical_parameters = np.empty((0,))

        fun_wrapped, bc_wrapped, fun_jac_wrapped, bc_jac_wrapped = wrap_functions(
            self.derivative_function, self.boundarycondition_function, None, None, sol.const, k, dtype)

        pool = kwargs.get('pool', None)

        if sol.u.size > 0:
            raise NotImplementedError('Shooting cannot directly handle control variables.')

        # Extract some info from the guess structure
        y0g = sol.y[0, :]
        if self.quadrature_function is None or np.isnan(sol.q).all():
            q0g = np.array([])
        else:
            q0g = sol.q[0, :]

        parameter_guess = sol.dynamical_parameters
        nondynamical_parameter_guess = sol.nondynamical_parameters

        # Get some info on the size of the problem
        n_odes = y0g.shape[0]
        n_quads = q0g.shape[0]
        n_dynparams = sol.dynamical_parameters.shape[0]
        # n_nondynparams = nondynamical_parameter_guess.shape[0]

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
        # stm0 = np.hstack((np.eye(n_odes), np.zeros((n_odes, n_dynparams)))).reshape(n_odes*(n_odes + n_dynparams))
        # y0stm = np.zeros((len(stm0) + n_odes))

        prop = Propagator(**self.ivp_args)

        converged = False  # Convergence flag
        n_iter = 0  # Initialize iteration counter
        err = -1

        # Set up the initial guess vector
        x_init = self._wrap_y0(gamma_set, parameter_guess, nondynamical_parameter_guess)

        def quad_wrap(t, xx, p, aux):
            return self.quadrature_function(t, xx[:n_odes], p, aux)

        # Pickle the functions for faster execution
        if pool is not None:
            pick_deriv = pickle.dumps(self.derivative_function)
            pick_quad = pickle.dumps(self.quadrature_function)
            pick_stm = pickle.dumps(self.stm_ode_func)
            pick_quad_stm = pickle.dumps(quad_wrap)
            _gamma_maker = self._make_gammas_parallel
        else:
            pick_deriv = self.derivative_function
            pick_quad = self.quadrature_function
            pick_stm = self.stm_ode_func
            pick_quad_stm = quad_wrap
            _gamma_maker = self._make_gammas

        # Set up the constraint function
        def _constraint_function(xx, deriv_func, quad_func, n_odes, n_quads, n_dynparams, n_arcs, aux):
            g = copy.deepcopy(gamma_set)
            _y, _q, _params, _nonparams = self._unwrap_y0(xx, n_odes, n_quads, n_dynparams, n_arcs)
            for ii in range(n_arcs):
                g[ii].y[0] = _y[ii]
                if n_quads > 0:
                    g[ii].q[0] = _q
            g = _gamma_maker(deriv_func, quad_func, g, _params, sol, prop, pool, n_quads)
            return self.bc_func_ms(g, _params, _nonparams, k, aux)

        def _constraint_function_wrapper(X):
            return _constraint_function(X, pick_deriv, pick_quad, n_odes, n_quads, n_dynparams, self.num_arcs,
                                        sol.const)

        # Set up the jacobian of the constraint function
        def _jacobian_function(xx, deriv_func, quad_func, n_odes, n_quads, n_dynparams, n_arcs):
            g = copy.deepcopy(gamma_set)
            _y, _q, _params, _nonparams = self._unwrap_y0(xx, n_odes, n_quads, n_dynparams, n_arcs)
            n_nondyn = _nonparams.shape[0]
            for ii in range(n_arcs):
                g[ii].y[0] = _y[ii]
                if n_quads > 0:
                    g[ii].q[0] = _q

            phi_full_list = []
            for ii in range(n_arcs):
                t0 = g[ii].t[0]
                _y0g, _q0g, _u0g = g[ii](t0)
                tf = g[ii].t[-1]
                _yfg, _qfg, _ufg = g[ii](tf)
                stm0 = np.hstack((np.eye(n_odes), np.zeros((n_odes, n_dynparams)))).reshape(
                    n_odes * (n_odes + n_dynparams))
                y0stm = np.zeros((len(stm0) + n_odes))
                stmf = np.hstack((np.eye(n_odes), np.zeros((n_odes, n_dynparams)))).reshape(
                    n_odes * (n_odes + n_dynparams))
                yfstm = np.zeros((len(stmf) + n_odes))
                y0stm[:n_odes] = _y0g
                y0stm[n_odes:] = stm0[:]
                yfstm[:n_odes] = _yfg
                yfstm[n_odes:] = stmf[:]
                g[ii].t = np.hstack((t0, tf))
                g[ii].y = np.vstack((y0stm, yfstm))
                g[ii].q = np.vstack((_q0g, _qfg))
                g[ii].u = np.vstack((_u0g, _ufg))

            gamma_set_new = _gamma_maker(deriv_func, quad_func, g, _params, sol, prop, pool, n_quads)
            for ii in range(len(gamma_set_new)):
                t_set = gamma_set_new[ii].t
                temp = gamma_set_new[ii].y
                y_set = temp[:, :n_odes]
                q_set = gamma_set_new[ii].q
                u_set = gamma_set_new[ii].u
                gamma_set_new[ii] = Trajectory(t_set, y_set, q_set, u_set)
                phi_temp = np.reshape(temp[:, n_odes:], (len(gamma_set_new[ii].t), n_odes, n_odes + n_dynparams))
                phi_full_list.append(np.copy(phi_temp))

            dbc_dya, dbc_dyb, dbc_dp = estimate_bc_jac(bc_wrapped, gamma_set_new[0].y[0], [], gamma_set_new[-1].y[-1],
                                                       [], _params, _nonparams)

            if dbc_dp is None:
                dbc_dp = np.empty((dbc_dya.shape[0],0))

            values = np.empty((0,))
            i_jac = np.empty((0,), dtype=int)
            j_jac = np.empty((0,), dtype=int)

            if n_arcs == 1:
                jac = np.hstack((dbc_dya, dbc_dp))
                _phi = np.vstack((phi_full_list[-1][-1], np.zeros((n_dynparams, n_odes + n_dynparams))))
                jac += np.dot(np.hstack((dbc_dyb, dbc_dp)), _phi)

                i_bc = np.repeat(np.arange(0, n_odes + n_dynparams), n_odes + n_dynparams)
                j_bc = np.tile(np.arange(n_odes + n_dynparams), n_odes + n_dynparams)
                values = np.hstack((values, jac.ravel()))
                i_jac = np.hstack((i_jac, i_bc))
                j_jac = np.hstack((j_jac, j_bc))
            else:
                p_jac = np.empty((0,n_dynparams))
                for ii in range(n_arcs-1):
                    jac = np.dot(np.eye(n_odes), phi_full_list[ii][-1])
                    i_bc = np.repeat(np.arange(n_odes*ii, n_odes*(ii+1)), n_odes)
                    j_bc = np.tile(np.arange(0, n_odes), n_odes) + n_odes * ii
                    values = np.hstack((values, jac[:,:n_odes].ravel()))
                    i_jac = np.hstack((i_jac, i_bc))
                    j_jac = np.hstack((j_jac, j_bc))

                    if n_dynparams > 0:
                        p_jac = np.vstack((p_jac, jac[:, n_odes:]))

                    jac = -np.eye(n_odes)
                    i_bc = np.repeat(np.arange(n_odes * ii, n_odes * (ii + 1)), n_odes)
                    j_bc = np.tile(np.arange(0, n_odes), n_odes) + n_odes * (ii + 1)
                    values = np.hstack((values, jac.ravel()))
                    i_jac = np.hstack((i_jac, i_bc))
                    j_jac = np.hstack((j_jac, j_bc))

                if n_dynparams > 0:
                    values = np.hstack((values, p_jac.ravel()))
                    i_p = np.repeat(np.arange(0, n_odes*(n_arcs-1)), n_dynparams)
                    j_p = np.tile(np.arange(0, n_dynparams), n_odes*(n_arcs-1)) + n_odes * n_arcs
                    i_jac = np.hstack((i_jac, i_p))
                    j_jac = np.hstack((j_jac, j_p))

                jac = dbc_dya
                i_bc = np.repeat(np.arange(0, n_odes + n_dynparams), n_odes) + n_odes*(n_arcs - 1)
                j_bc = np.tile(np.arange(n_odes), n_odes + n_dynparams)
                values = np.hstack((values, jac.ravel()))
                i_jac = np.hstack((i_jac, i_bc))
                j_jac = np.hstack((j_jac, j_bc))

                _phi = np.vstack((phi_full_list[-1][-1], np.zeros((n_dynparams, n_odes + n_dynparams))))
                jac = np.dot(np.hstack((dbc_dyb, dbc_dp)), _phi)
                jac[:, n_odes:] += dbc_dp
                i_bc = np.repeat(np.arange(0, n_odes + n_dynparams), n_odes + n_dynparams) + n_odes * (n_arcs - 1)
                j_bc = np.tile(np.arange(n_odes + n_dynparams), n_odes + n_dynparams) + n_odes * (n_arcs - 1)
                values = np.hstack((values, jac.ravel()))
                i_jac = np.hstack((i_jac, i_bc))
                j_jac = np.hstack((j_jac, j_bc))

            J = csc_matrix(coo_matrix((values, (i_jac, j_jac))))
            return J

        is_sparse = False
        if n_quads == 0 and self.algorithm.lower() == 'armijo':
            is_sparse = True
            def _jacobian_function_wrapper(X):
                return _jacobian_function(X, pick_stm, pick_quad_stm, n_odes, n_quads, n_dynparams, self.num_arcs)
        elif n_quads == 0:
            def _jacobian_function_wrapper(X):
                return _jacobian_function(X, pick_stm, pick_quad_stm, n_odes, n_quads, n_dynparams, self.num_arcs).toarray()
        else:
            def _jacobian_function_wrapper(X):
                return approx_jacobian(X, _constraint_function_wrapper, 1e-6)

        constraint = {'type': 'eq', 'fun': _constraint_function_wrapper, 'jac': _jacobian_function_wrapper}

        # Set up the cost function. This should just return 0 unless the specified method cannot handle constraints
        def cost(_): return 0

        """
        Run the root-solving process
        """
        if self.algorithm in scipy_minimize_algorithms:
            if not (self.algorithm == 'COBYLA' or self.algorithm == 'SLSQP' or self.algorithm == 'trust-constr'):
                def cost(x):
                    return np.linalg.norm(_constraint_function_wrapper(x)) ** 2

            opt = minimize(cost, x_init, method=self.algorithm, tol=self.tolerance, constraints=constraint,
                           options={'maxiter': self.max_iterations})

            x_init = opt.x
            n_iter = opt.nit
            converged = opt.success and isclose(opt.fun, 0, abs_tol=self.tolerance)

        elif self.algorithm in scipy_root_algorithms:
            opt = root(_constraint_function_wrapper, x_init, jac=_jacobian_function_wrapper, method=self.algorithm,
                       tol=self.tolerance, options={'maxiter': self.max_iterations})
            x_init = opt.x
            n_iter = -1
            converged = opt.success

        elif self.algorithm.lower() == 'fsolve':
            x = fsolve(_constraint_function_wrapper, x_init, fprime=_jacobian_function_wrapper, xtol=self.tolerance)
            x_init = x
            n_iter = -1
            converged = isclose(np.linalg.norm(_constraint_function_wrapper(x_init))**2, 0, abs_tol=self.tolerance)

        elif self.algorithm.lower() == 'armijo':

            while not converged and n_iter <= self.max_iterations and err < self.max_error:
                residual = _constraint_function_wrapper(x_init)

                if any(np.isnan(residual)):
                    raise RuntimeError("Nan in residual")

                err = np.linalg.norm(residual)
                jac = _jacobian_function_wrapper(x_init)
                try:
                    if is_sparse:
                        LU = splu(jac)
                        dy0 = LU.solve(-residual)
                    else:
                        dy0 = np.linalg.solve(jac, -residual)
                except np.linalg.LinAlgError as error:
                    logging.warning(error)
                    dy0, *_ = np.linalg.lstsq(jac, -residual)

                a = 1e-4
                reduct = 0.5
                ll = 1
                r_try = float('Inf')
                step = None

                while (r_try >= (1-a*ll) * err) and (r_try > self.tolerance) and ll > 0.05:
                    step = ll*dy0
                    res_try = _constraint_function_wrapper(x_init + step)
                    r_try = np.linalg.norm(res_try)
                    ll *= reduct

                x_init += step
                err = r_try
                n_iter += 1

                if err <= self.tolerance:
                    converged = True
                if is_sparse:
                    logging.debug('Step {}: Residual = {}; Jacobian condition = {}'.format(n_iter, err, np.linalg.cond(jac.toarray())))
                else:
                    logging.debug('Step {}: Residual = {}; Jacobian condition = {}'.format(n_iter, err, np.linalg.cond(jac)))
        elif self.algorithm.lower() == 'npnlp':
            from npnlp import minimize as mini
            opt = mini(cost, x_init, method='sqp', tol=self.tolerance,
                       nonlconeq=lambda x, l: _constraint_function_wrapper(x))
            x_init = opt['x']
            n_iter = opt['nit']
            converged = opt['success'] and isclose(opt['fval'], 0, abs_tol=self.tolerance)

        else:
            raise NotImplementedError('Method \'' + self.algorithm + '\' is not implemented.')

        """
        Post optimization checks and formatting
        """

        # Unwrap the solution from the solver to put in a readable format
        y, q, parameter_guess, nondynamical_parameter_guess = self._unwrap_y0(x_init, n_odes, n_quads, n_dynparams,
                                                                              self.num_arcs)
        for ii in range(self.num_arcs):
            gamma_set[ii].y[0] = y[ii]
            if n_quads > 0:
                gamma_set[ii].q[0] = q
        gamma_set = _gamma_maker(pick_deriv, pick_quad, gamma_set, parameter_guess, sol, prop, pool, n_quads)

        if n_iter > self.max_iterations:
            logging.warning('Max iterations exceeded.')

        if err > self.max_error:
            raise RuntimeError('Error exceeded max_error')

        if err < self.tolerance and converged:
            if n_iter == -1:
                logging.debug("Converged in an unknown number of iterations.")
            else:
                logging.debug("Converged in " + str(n_iter) + " iterations.")

        # Stitch the arcs together to make a single trajectory, removing the boundary points inbetween each arc
        t_out = gamma_set[0].t
        y_out = gamma_set[0].y
        q_out = gamma_set[0].q
        u_out = gamma_set[0].u

        for ii in range(self.num_arcs - 1):
            t_out = np.hstack((t_out, gamma_set[ii + 1].t[1:]))
            y_out = np.vstack((y_out, gamma_set[ii + 1].y[1:]))
            q_out = np.vstack((q_out, gamma_set[ii + 1].q[1:]))
            u_out = np.vstack((u_out, gamma_set[ii + 1].u[1:]))

        sol.t = t_out
        sol.y = y_out
        sol.q = q_out
        sol.u = u_out

        sol.dynamical_parameters = parameter_guess[:k]
        sol.nondynamical_parameters = parameter_guess[k:]
        sol.converged = converged
        return sol
