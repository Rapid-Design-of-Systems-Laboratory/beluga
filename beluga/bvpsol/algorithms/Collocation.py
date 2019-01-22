from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Trajectory
import numpy as np
import copy
from npnlp import minimize
from scipy.optimize import minimize as mini
from scipy.integrate import simps
import logging

class Collocation(BaseAlgorithm):
    """
    Collocation algorithm for solving boundary value problems.
    """
    def __new__(cls, *args, **kwargs):
        """
        Creates a new Collocation object.

        :param args: Unused
        :param kwargs: Additional parameters accepted by the solver.
        :return: Collocation object.

        +------------------------+-----------------+-----------------+
        | Valid kwargs           | Default Value   | Valid Values    |
        +========================+=================+=================+
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
        
        obj = super(Collocation, cls).__new__(cls, *args, **kwargs)

        cached = kwargs.get('cached', True)
        tolerance = kwargs.get('tolerance', 1e-4)
        max_error = kwargs.get('max_error', 100)
        max_iterations = kwargs.get('max_iterations', 100)
        number_of_nodes = kwargs.get('number_of_nodes', 30)
        use_numba = kwargs.get('use_numba', False)
        verbose = kwargs.get('verbose', False)

        obj.cached = cached
        obj.tolerance = tolerance
        obj.max_error = max_error
        obj.max_iterations = max_iterations
        obj.number_of_nodes = number_of_nodes
        obj.use_numba = use_numba
        obj.verbose = verbose
        return obj
    
    def solve(self, solinit, **kwargs):
        """
        Solve a two-point boundary value problem using the collocation method.

        :param deriv_func: The ODE function.
        :param quad_func: The quad func.
        :param bc_func: The boundary conditions function.
        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        """
        sol = copy.deepcopy(solinit)
        sol.set_interpolate_function('cubic')
        number_of_datapoints = len(sol.t)
        if number_of_datapoints < 4:
            # Special cae where polynomial interpolation fails. Use linear interpolation to get 4 nodes.
            t_new = np.linspace(sol.t[0], sol.t[-1], num=4)
            y_new = np.column_stack([np.interp(t_new, sol.t, sol.y[:,ii]) for ii in range(sol.y.shape[1])])
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

        reconstruct = False
        if self.number_of_nodes != number_of_datapoints:
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
            if self.quadrature_function is not None and len(sol.q[0]) is not 0:
                raise NotImplemented # TODO: Put reconstruction of q's in Trajectory()? Or leave in ivpsol?

        # self.constraint = {'type': 'eq', 'fun': self._collocation_constraint}
        self.constraint_midpoint = {'type': 'eq', 'fun': self._collocation_constraint_midpoint}
        self.constraint_boundary = {'type': 'eq', 'fun': self._collocation_constraint_boundary}

        # Set up initial guess and other info
        self.tspan = sol.t
        self.number_of_odes = sol.y.shape[1]
        if sol.u.size > 0:
            self.number_of_controls = sol.u.shape[1]
        else:
            self.number_of_controls = 0

        # TODO: The following if-then structure is silly, but I can't resolve this until some optimlib corrections are made
        if sol.q.size == 0:
            self.number_of_quads = 0
            sol.q = np.array([], dtype=np.float64)
        elif len(sol.q) == 0:
            self.number_of_quads = 0
            sol.q = np.array([], dtype=np.float64)
        else:
            self.number_of_quads = len(sol.q)
            raise NotImplementedError

        if sol.dynamical_parameters is None:
            sol.dynamical_parameters = np.array([], dtype=np.float64)

        if sol.nondynamical_parameters is None:
            sol.nondynamical_parameters = np.array([], dtype=np.float64)

        self.number_of_dynamical_params = len(sol.dynamical_parameters)
        self.number_of_nondynamical_params = len(sol.nondynamical_parameters)

        vectorized = self._wrap_params(sol.y, sol.q, sol.u, sol.dynamical_parameters, sol.nondynamical_parameters)

        self.aux = sol.aux
        self.const = sol.const
        sol.converged = False

        if self.verbose:
            logging.info('Running collocation... ')
        # This is SciPy syntax
        xopt = mini(self._collocation_cost, vectorized, args=(), method='SLSQP', jac=None, hess=None, hessp=None, bounds=None, constraints=[self.constraint_midpoint, self.constraint_boundary], tol=self.tolerance, callback=None, options=None)
        # xopt = minimize(self._collocation_cost, vectorized, nonlconeq=lambda X, L: np.hstack((self._collocation_constraint_boundary(X), self._collocation_constraint_midpoint(X))), method='sqp')
        logging.debug(xopt['message'])
        # breakpoint()
        if xopt['status'] == 0:
            sol.converged = True
        # sol.converged = xopt['status']

        # Organize the output with the sol() structure
        sol.t = self.tspan
        sol.y, sol.q, sol.u, sol.dynamical_parameters, sol.nondynamical_parameters = self._unwrap_params(xopt['x'])
        return sol

    def _collocation_constraint_midpoint(self, vectorized):
        y, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        gamma = Trajectory(self.tspan, y, np.array([]), u)
        tf = gamma.t[-1]
        # dX = np.squeeze(self.derivative_function(self.tspan, X.T, params, self.aux)).T # TODO: Vectorized our code compiler so this line works
        dX = np.squeeze([self.derivative_function(yi, params, self.const) for yi,ui in zip(y, u)])
        if len(dX.shape) == 1:
            dX = np.array([dX]).T
        dp0 = dX[:-1]
        dp1 = dX[1:]
        p0 = y[:-1]
        p1 = y[1:]
        t0 = self.tspan[:-1]
        t1 = self.tspan[1:]
        t12 = (t0+t1)/2
        midpoint_predicted = 1 / 2 * (p0 + p1) + tf / (self.number_of_nodes - 1) / 8 * (dp0 - dp1)
        midpoint_derivative_predicted = -3 / 2 * (self.number_of_nodes - 1) / tf * (p0 - p1) - 1 / 4 * (dp0 + dp1)
        midpoint_derivative_actual = np.squeeze([self.derivative_function(yi, params, self.const) for yi, ui in zip(midpoint_predicted, u[:-1])]) # TODO: Vectorize, so this one works as well
        if len(midpoint_derivative_actual.shape) == 1:
            midpoint_derivative_actual = np.array([midpoint_derivative_actual]).T
        outvec = midpoint_derivative_predicted - midpoint_derivative_actual
        d2 = outvec.shape[1]
        outvec = np.hstack([outvec[:,ii][:] for ii in range(d2)])
        return outvec

    def _collocation_constraint_boundary(self, vectorized):
        X, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        return self.boundarycondition_function(X[0], [], X[-1], [], params, nondyn_params, self.const)
        # else:
        #     quadsf = self._integrate_quads(self.tspan, X, quads0, params, self.aux, quads=self.quadrature_function)
        #     return np.squeeze(self.boundarycondition_function(self.tspan[0], X[0], self.tspan[-1], X[-1], quads0, quadsf, params, nondyn_params, self.aux))

    def _collocation_cost(self, vectorized):
        X, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        if self.initial_cost_function is not None:
            c0 = self.initial_cost_function(X[0], [], u[0], params, self.const)
        else:
            c0 = 0

        if self.terminal_cost_function is not None:
            cf = self.terminal_cost_function(X[-1], [], u[-1], params, self.const)
        else:
            cf = 0

        if self.path_cost_function is not None:
            cpath = np.array([self.path_cost_function(yi, [], ui, params, self.const) for yi, ui in zip(X, u)])
            cpath = simps(cpath, x=self.tspan)
        else:
            cpath = 0
        return c0 + cpath + cf

    def _unwrap_params(self, vectorized):
        X = vectorized[:self.number_of_odes * self.number_of_nodes].reshape([self.number_of_nodes, self.number_of_odes])
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_odes * self.number_of_nodes))

        quads = vectorized[:self.number_of_quads]
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_quads))

        u = vectorized[:self.number_of_controls * self.number_of_nodes].reshape([self.number_of_nodes, self.number_of_controls])
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_controls * self.number_of_nodes))

        dynamical_params = vectorized[:self.number_of_dynamical_params]
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_dynamical_params))

        nondynamical_params = vectorized[:self.number_of_nondynamical_params]
        vectorized = np.delete(vectorized, np.arange(0, self.number_of_nondynamical_params))

        return X, quads, u, dynamical_params, nondynamical_params

    def _wrap_params(self, y, q, u, params, nondyn_params):
        return np.concatenate((y.flatten(), q.flatten(), u.flatten(), params, nondyn_params))

    @staticmethod
    def _get_poly_coefficients_1_3(p0, dquads0, dquads12, dquads1):
        C1 = p0
        C2 = dquads0
        C3 = -3/2*dquads0 + 2*dquads12 - 1/2*dquads1
        C4 = 2/3*dquads0 - 4/3*dquads12 + 2/3*dquads1
        return C1, C2, C3, C4

    @staticmethod
    def _get_poly_coefficients_2_2(p0, dp0, p1, dp1):
        C1 = p0
        C2 = dp0
        C3 = -3*p0 - 2*dp0 + 3*p1 - dp1
        C4 = 2*p0 + dp0 - 2*p1 + dp1
        return C1, C2, C3, C4

    @staticmethod
    def _collocation_midpoint_prediction(p0, dp0, p1, dp1, tf, N):
        return 1 / 2 * (p0 + p1) + tf / (N - 1) / 8 * (dp0 - dp1)

    @staticmethod
    def _collocation_midpoint_derivative(p0, dp0, p1, dp1, tf, N):
        return -3 / 2 * (N - 1) / tf * (p0 - p1) - 1 / 4 * (dp0 + dp1)

    @classmethod
    def _get_default_options(cls, options='default'):
        """ Default options structure for Collocation. """
        if options == 'default':
            return [1, 10]
        elif options == 'quiet':
            return [0, 10]