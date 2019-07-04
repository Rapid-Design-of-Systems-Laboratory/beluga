from beluga.bvpsol.BaseAlgorithm import BaseAlgorithm
import numpy as np
import copy
from scipy.optimize import minimize
import logging


class Collocation(BaseAlgorithm):
    """
    Collocation algorithm for solving boundary-value problems.

    :param args: Unused
    :param kwargs: Additional parameters accepted by the solver.
    :return: Collocation object.

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | adaptive_mesh          | False           | Bool            |
    +------------------------+-----------------+-----------------+
    | cached                 | True            | Bool            |
    +------------------------+-----------------+-----------------+
    | tolerance              | 1e-4            | > 0             |
    +------------------------+-----------------+-----------------+
    | max_error              | 100             | > 0             |
    +------------------------+-----------------+-----------------+
    | max_iterations         | 100             | > 0             |
    +------------------------+-----------------+-----------------+
    | number_of_nodes        | 30              | >= 4            |
    +------------------------+-----------------+-----------------+
    | use_numba              | False           | Bool            |
    +------------------------+-----------------+-----------------+
    | verbose                | False           | Bool            |
    +------------------------+-----------------+-----------------+
    """

    def __init__(self, *args, **kwargs):

        BaseAlgorithm.__init__(self, *args, **kwargs)

        adaptive_mesh = kwargs.get('adaptive_mesh', False)
        cached = kwargs.get('cached', True)
        tolerance = kwargs.get('tolerance', 1e-4)
        max_error = kwargs.get('max_error', 100)
        max_iterations = kwargs.get('max_iterations', 100)
        number_of_nodes = kwargs.get('number_of_nodes', 30)
        use_numba = kwargs.get('use_numba', False)
        verbose = kwargs.get('verbose', False)

        self.adaptive_mesh = adaptive_mesh
        self.cached = cached
        self.tolerance = tolerance
        self.max_error = max_error
        self.max_iterations = max_iterations
        self.number_of_nodes = number_of_nodes
        self.use_numba = use_numba
        self.verbose = verbose

        self.constraint_midpoint = None
        self.constraint_boundary = None
        self.constraint_path = None

        self.number_of_dynamical_params = None
        self.number_of_nondynamical_params = None

        self.tspan = None
        self.number_of_odes = None
        self.number_of_controls = None

        self.const = None

        self.number_of_quads = None

    def solve(self, solinit, **kwargs):
        """
        Solve a two-point boundary value problem using the collocation method.

        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        """
        sol = copy.deepcopy(solinit)
        sol.set_interpolate_function('cubic')
        number_of_datapoints = len(sol.t)

        # Default costs and quads to return nothing if not defined
        def return_nil(*_, **__):
            return np.array([])

        if self.quadrature_function is None:
            self.quadrature_function = return_nil

        if number_of_datapoints < 4:
            # Special case where polynomial interpolation fails. Use linear interpolation to get 4 nodes.
            t_new = np.linspace(sol.t[0], sol.t[-1], num=4)
            y_new = np.column_stack([np.interp(t_new, sol.t, sol.y[:, ii]) for ii in range(sol.y.shape[1])])
            if sol.q.size > 0:
                q_new = np.column_stack([np.interp(t_new, sol.t, sol.q[:, ii]) for ii in range(sol.q.shape[1])])
            else:
                q_new = np.array([])

            if sol.u.size > 0:
                u_new = np.column_stack([np.interp(t_new, sol.t, sol.q[:, ii]) for ii in range(sol.q.shape[1])])
            else:
                u_new = np.array([])
            sol.t = t_new
            sol.y = y_new
            sol.q = q_new
            sol.u = u_new

        if self.number_of_nodes > number_of_datapoints:
            new_t = np.linspace(sol.t[0], sol.t[-1], self.number_of_nodes)
            new_y, new_q, new_u = sol(new_t[0])
            for ti in new_t[1:]:
                yy, qq, uu = sol(ti)
                new_y = np.vstack((new_y, yy))
                new_q = np.vstack((new_q, qq))
                new_u = np.vstack((new_u, uu))

            sol.t = new_t
            sol.y = new_y
            sol.q = new_q
            sol.u = new_u
        else:
            self.number_of_nodes = number_of_datapoints

        # self.constraint = {'type': 'eq', 'fun': self._collocation_constraint}
        self.constraint_midpoint = {'type': 'eq', 'fun': self._collocation_constraint_midpoint}
        self.constraint_boundary = {'type': 'eq', 'fun': self._collocation_constraint_boundary}
        self.constraint_path = {'type': 'ineq', 'fun': self._collocation_constraint_path}

        self.tspan = sol.t
        self.number_of_odes = sol.y.shape[1]
        if sol.u.size > 0:
            self.number_of_controls = sol.u.shape[1]
        else:
            self.number_of_controls = 0

        if sol.q.size == 0:
            self.number_of_quads = 0
            sol.q = np.array([]).reshape((self.number_of_nodes, 0))
        else:
            self.number_of_quads = sol.q.shape[1]

        if sol.dynamical_parameters is None:
            sol.dynamical_parameters = np.array([], dtype=np.float64)

        if sol.nondynamical_parameters is None:
            sol.nondynamical_parameters = np.array([], dtype=np.float64)

        self.number_of_dynamical_params = len(sol.dynamical_parameters)
        self.number_of_nondynamical_params = len(sol.nondynamical_parameters)

        vectorized = self._wrap_params(sol.y, sol.q, sol.u, sol.dynamical_parameters, sol.nondynamical_parameters)

        self.const = sol.const
        sol.converged = False

        # noinspection PyTypeChecker
        xopt = minimize(
            self._collocation_cost, vectorized, args=(), method='SLSQP', jac=None,
            hessp=None, bounds=None,
            constraints=[self.constraint_midpoint, self.constraint_boundary, self.constraint_path],
            tol=self.tolerance, callback=None, options={'maxiter': self.max_iterations})

        sol.t = self.tspan
        sol.y, q0, sol.u, sol.dynamical_parameters, sol.nondynamical_parameters = self._unwrap_params(xopt['x'])

        if self.number_of_quads > 0:
            sol.q = self._integrate(self.quadrature_function, self.derivative_function, sol.y, sol.u,
                                    sol.dynamical_parameters, self.const, self.tspan, q0)

        logging.debug(xopt['message'])

        if 'kkt' in xopt:
            sol.dual = self._kkt_to_dual(sol, xopt['kkt'][0])
        else:
            sol.dual = np.ones_like(sol.y)*np.nan

        sol.converged = xopt['success']

        return sol

    @staticmethod
    def _kkt_to_dual(sol, kkt):
        nodes = len(sol.t)
        dual = (kkt.reshape((nodes-1, sol.y.shape[1]), order='F').T/(sol.t[:-1]-sol.t[1:])).T
        dual = np.vstack((dual, np.zeros(sol.y.shape[1])))
        return dual

    def _collocation_constraint_path(self, vectorized):
        if self.inequality_constraint_function is None:
            return ()

        y, q0, u, params, nondynamical_params = self._unwrap_params(vectorized)
        if u.size > 0:
            cp = np.hstack([-self.inequality_constraint_function(y[ii], u[ii], params, self.const)
                            for ii in range(self.number_of_nodes)])
        else:
            cp = np.hstack([-self.inequality_constraint_function(y[ii], [], params, self.const)
                            for ii in range(self.number_of_nodes)])

        return cp

    def _collocation_constraint_midpoint(self, vectorized):
        y, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        # TODO: Vectorized our code compiler so this line works
        # dX1 = np.squeeze(self.derivative_function(y.T, u.T, params, self.const)).T
        dX = np.squeeze([self.derivative_function(yi, ui, params, self.const) for yi, ui in zip(y, u)])
        if len(dX.shape) == 1:
            dX = np.array([dX]).T
        dp0 = dX[:-1]
        dp1 = dX[1:]
        p0 = y[:-1]
        p1 = y[1:]
        t0 = self.tspan[:-1]
        t1 = self.tspan[1:]
        u0 = u[:-1]
        uf = u[1:]
        u_midpoint = (u0 + uf)/2
        midpoint_predicted = self._midpoint(p0, p1, dp0, dp1, t0, t1)
        midpoint_derivative_predicted = self._midpoint_derivative(p0, p1, dp0, dp1, t0, t1)
        # TODO: Vectorize, so this one works as well
        midpoint_derivative_actual = np.squeeze(
            [self.derivative_function(yi, ui, params, self.const) for yi, ui in zip(midpoint_predicted, u_midpoint)])
        if len(midpoint_derivative_actual.shape) == 1:
            midpoint_derivative_actual = np.array([midpoint_derivative_actual]).T
        outvec = midpoint_derivative_predicted - midpoint_derivative_actual
        d2 = outvec.shape[1]
        outvec = np.hstack([outvec[:, ii][:] for ii in range(d2)])
        return outvec

    def _collocation_constraint_boundary(self, vectorized):
        y, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        qf = self._integrate(self.quadrature_function, self.derivative_function,
                             y, u, params, self.const, self.tspan, quads0)[-1]
        return self.boundarycondition_function(y[0], quads0, u[0], y[-1], qf, u[-1], params, nondyn_params, self.const)

    def _collocation_cost(self, vectorized):
        y, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        if self.initial_cost_function is not None:
            c0 = self.initial_cost_function(y[0], u[0], params, self.const)
        else:
            c0 = 0

        if self.terminal_cost_function is not None:
            cf = self.terminal_cost_function(y[-1], u[-1], params, self.const)
        else:
            cf = 0

        cpath = 0
        if self.path_cost_function is not None:
            cpath = self._integrate(self.path_cost_function, self.derivative_function,
                                    y, u, params, self.const, self.tspan, 0)[-1]

        return c0 + cpath + cf

    def _unwrap_params(self, vectorized):
        X = vectorized[:self.number_of_odes * self.number_of_nodes].reshape([self.number_of_nodes, self.number_of_odes])
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_odes * self.number_of_nodes))

        quads = vectorized[:self.number_of_quads]
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_quads))

        u = vectorized[:self.number_of_controls * self.number_of_nodes].reshape([self.number_of_nodes,
                                                                                 self.number_of_controls])
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_controls * self.number_of_nodes))

        dynamical_params = vectorized[:self.number_of_dynamical_params]
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_dynamical_params))

        nondynamical_params = vectorized[:self.number_of_nondynamical_params]
        # vectorized = np.delete(vectorized, np.arange(0, self.number_of_nondynamical_params))

        return X, quads, u, dynamical_params, nondynamical_params

    @staticmethod
    def _wrap_params(y, q, u, params, nondyn_params):
        return np.concatenate((y.flatten(), q[0], u.flatten(), params, nondyn_params))

    @staticmethod
    def _get_poly_coefficients_1_3(p0, dquads0, dquads12, dquads1):
        C1 = p0
        C2 = dquads0
        C3 = -3/2*dquads0 + 2*dquads12 - 1/2*dquads1
        C4 = 2/3*dquads0 - 4/3*dquads12 + 2/3*dquads1
        return C1, C2, C3, C4

    @staticmethod
    def _get_poly_coefficients_2_2(p0, dp0, p1, dp1, h):
        C1 = p0
        C2 = dp0
        C3 = -3*p0/h**2 - 2*dp0/h + 3*p1/h**2 - dp1/h
        C4 = 2*p0/h**3 + dp0/h**2 - 2*p1/h**3 + dp1/h**2
        return C1, C2, C3, C4

    @classmethod
    def _get_default_options(cls, options='default'):
        """ Default options structure for Collocation. """
        if options == 'default':
            return [1, 10]
        elif options == 'quiet':
            return [0, 10]

    # TODO: Cythonize _midpoint, _midpoint_derivative, _integrate
    @staticmethod
    def _midpoint(p0, p1, dp0, dp1, t0, t1):
        return (1 / 2 * (p0 + p1).T + (t1 - t0) / 8 * (dp0 - dp1).T).T

    @staticmethod
    def _midpoint_derivative(p0, p1, dp0, dp1, t0, t1):
        return (-3 / 2 * (p0 - p1).T / (t1 - t0) - 1 / 4 * (dp0 + dp1).T).T

    def _integrate(self, fun, base, y, u, params, c, t, val0):
        val0 = np.array([val0])
        dX = np.squeeze([base(yi, ui, params, c) for yi, ui in zip(y, u)])
        if len(dX.shape) == 1:
            dX = np.array([dX]).T
        dp0 = dX[:-1]
        dp1 = dX[1:]
        p0 = y[:-1]
        p1 = y[1:]
        t0 = t[:-1]
        t1 = t[1:]
        u0 = u[:-1]
        uf = u[1:]
        u_midpoint = (u0 + uf) / 2
        y_midpoint = self._midpoint(p0, p1, dp0, dp1, t0, t1)
        for ii in range(len(t) - 1):
            c0 = fun(y[ii], u[ii], params, c)
            c_mid = fun(y_midpoint[ii], u_midpoint[ii], params, c)
            c1 = fun(y[ii + 1], u[ii + 1], params, c)
            val0 = np.vstack((val0, val0[-1] + (1 / 6 * c0 + 4 / 6 * c_mid + 1 / 6 * c1) * (t[ii + 1] - t[ii])))

        return val0
