from beluga.bvpsol.algorithms.BaseAlgorithm import BaseAlgorithm
import numpy as np
import copy
from scipy.optimize import minimize
import logging
from beluga.utils import keyboard

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
        | number_of_nodes        | 40              | > 1             |
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
        number_of_nodes = kwargs.get('number_of_nodes', 40)
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
    
    def solve(self, deriv_func, quad_func, bc_func, solinit):
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
            raise ValueError('Initial guess must have at least 4 data points in collocation.')

        reconstruct = False
        if self.number_of_nodes != number_of_datapoints:
            new_t = np.linspace(sol.t[0], sol.t[-1], self.number_of_nodes)
            (new_y, new_q, new_u) = sol(new_t)
            sol.t = new_t
            sol.y = new_y
            sol.q = new_q
            sol.u = new_u
            if quad_func is not None:
                raise NotImplemented # TODO: Put reconstruction of q's in Trajectory()? Or leave in ivpsol?

        # Set up some required class functions for collocation
        self.eoms = deriv_func
        self.quadratures = quad_func
        self.path_cost = None # TODO: Assumed to be indirect. This class can handle direct with some work.
        self.terminal_cost = None # TODO: Assumed to be indirect.
        self.bcs = bc_func

        # self.constraint = {'type': 'eq', 'fun': self._collocation_constraint}
        self.constraint_midpoint = {'type': 'eq', 'fun': self._collocation_constraint_midpoint}
        self.constraint_boundary = {'type': 'eq', 'fun': self._collocation_constraint_boundary}

        # Set up initial guess and other info
        self.tspan = sol.t
        self.number_of_odes = sol.y.shape[1]

        # TODO: The following if-then structure is silly, but I can't resolve this until some optimlib corrections are made
        if sol.q is None:
            self.number_of_quads = 0
            sol.q = np.array([], dtype=np.float64)
        elif len(sol.q) == 0:
            self.number_of_quads = 0
            sol.q = np.array([], dtype=np.float64)
        else:
            self.number_of_quads = len(sol.q)
            raise NotImplementedError

        if sol.parameters is None:
            self.number_of_params = 0
            sol.parameters = np.array([], dtype=np.float64)
        else:
            self.number_of_params = len(sol.parameters)

        vectorized = self._wrap_params(sol.y, sol.q, sol.parameters)

        self.aux = sol.aux
        sol.converged = False

        if self.verbose:
            logging.info('Running collocation... ')

        xopt = minimize(self._collocation_cost, vectorized, args=(), method='SLSQP', jac=None, hess=None, hessp=None, bounds=None, constraints=[self.constraint_midpoint, self.constraint_boundary], tol=self.tolerance, callback=None, options=None)

        if self.verbose:
            logging.info(xopt['message'])

        if xopt['status'] == 0:
            sol.converged = True

        # Organize the output with the sol() structure
        sol.t = self.tspan
        sol.y, sol.q, sol.parameters = self._unwrap_params(xopt['x'])
        return sol

    def reconstruct(self, time, ivp):
        # TODO: Rewrite this trash. Use ivpsol(), this should already be done.
        if time < ivp.sol.x[0] or time > ivp.sol.x[-1]:
            raise ValueError

        if time == ivp.sol.x[0]:
            return ivp.sol.x[0], ivp.sol.y[0], ivp.sol.quads

        ind = 1
        t_high = ivp.sol.x[ind]
        tf = ivp.sol.x[-1]
        quads = ivp.sol.quads
        while t_high < time:
            if ivp.quadratures is not None:
                t0 = ivp.sol.x[ind-1]
                t1 = ivp.sol.x[ind]
                t12 = (t1 + t0) / 2
                p0 = ivp.sol.y[ind-1]
                p1 = ivp.sol.y[ind]
                try:
                    dp0 = np.squeeze(ivp.eoms(t0, p0, ivp.sol.params, ivp.sol.consts))
                except:
                    keyboard()
                dp1 = np.squeeze(ivp.eoms(t1, p1, ivp.sol.params, ivp.sol.consts))
                midpoint_predicted = 1 / 2 * (p0 + p1) + tf / (len(ivp.sol.x) - 1) / 8 * (dp0 - dp1)
                dt = ivp.sol.x[ind] - ivp.sol.x[ind-1]
                dquads = np.squeeze(ivp.quadratures(t0, p0, ivp.sol.params, ivp.sol.consts)) * dt
                dquads12 = np.squeeze(ivp.quadratures(t12, midpoint_predicted, ivp.sol.params, ivp.sol.consts)) * dt
                dquads1 = np.squeeze(ivp.quadratures(t1, p1, ivp.sol.params, ivp.sol.consts)) * dt
                C1, C2, C3, C4 = self._get_poly_coefficients_1_3(quads, dquads, dquads12, dquads1)
                quads = C1 + C2 + C3 + C4
            ind += 1
            t_high = ivp.sol.x[ind]

        dt = ivp.sol.x[ind] - ivp.sol.x[ind - 1]
        t_temp = (time - ivp.sol.x[ind - 1]) / dt
        p0 = np.array(ivp.sol.y[ind - 1])
        dp0 = np.squeeze(ivp.eoms(ivp.sol.x[ind - 1], ivp.sol.y[ind - 1], ivp.sol.params, ivp.sol.consts)) * dt
        p1 = np.array(ivp.sol.y[ind])
        dp1 = np.squeeze(ivp.eoms(ivp.sol.x[ind], ivp.sol.y[ind], ivp.sol.params, ivp.sol.consts)) * dt
        if ivp.quadratures is not None:
            t0 = ivp.sol.x[ind - 1]
            t1 = ivp.sol.x[ind]
            t12 = (t1 + t0) / 2
            midpoint_predicted = 1 / 2 * (p0 + p1) + tf / (len(ivp.sol.x) - 1) / 8 * (dp0 - dp1)
            dquads = np.squeeze(ivp.quadratures(t0, p0, ivp.sol.params, ivp.sol.consts)) * dt
            dquads12 = np.squeeze(ivp.quadratures(t12, midpoint_predicted, ivp.sol.params, ivp.sol.consts)) * dt
            dquads1 = np.squeeze(ivp.quadratures(t1, p1, ivp.sol.params, ivp.sol.consts)) * dt
            C1, C2, C3, C4 = self._get_poly_coefficients_1_3(quads, dquads, dquads12, dquads1)
            quadsf = C1 + C2*t_temp + C3*t_temp**2 + C4*t_temp**3
        else:
            quadsf = quads

        C1, C2, C3, C4 = self._get_poly_coefficients_2_2(p0, dp0, p1, dp1)
        y_new = C1 + C2*t_temp + C3*t_temp**2 + C4*t_temp**3
        return time, y_new, quadsf

    def _collocation_constraint_midpoint(self, vectorized):
        y, quads0, params = self._unwrap_params(vectorized)
        tf = self.tspan[-1]
        # dX = np.squeeze(self.eoms(self.tspan, X.T, params, self.aux)).T # TODO: Vectorized our code compiler so this line works
        dX = np.squeeze([self.eoms(ti, yi, params, self.aux) for ti,yi in zip(self.tspan, y)])
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
        midpoint_derivative_actual = np.squeeze([self.eoms(ti, yi, params, self.aux) for ti, yi in zip(t12, midpoint_predicted)]) # TODO: Vectorize, so this one works as well
        if len(midpoint_derivative_actual.shape) == 1:
            midpoint_derivative_actual = np.array([midpoint_derivative_actual]).T
        outvec = midpoint_derivative_predicted - midpoint_derivative_actual
        return outvec.flatten()

    def _collocation_constraint_boundary(self, vectorized):
        X, quads0, params = self._unwrap_params(vectorized)
        if len(quads0) == 0:
            return np.squeeze(self.bcs(self.tspan[0], X[0], [], self.tspan[-1], X[-1], [], params, self.aux))
        else:
            quadsf = self._integrate_quads(self.tspan, X, quads0, params, self.aux, quads=self.quadratures)
            return np.squeeze(self.bcs(self.tspan[0], X[0], self.tspan[-1], X[-1], quads0, quadsf, params, self.aux))

    def _collocation_cost(self, vectorized):
        X, quads0, params = self._unwrap_params(vectorized)
        return 0

        if self.path_cost is not None:
            path_cost = self.path_cost(self.tspan, X, params, self.consts)
            if path_cost is None:
                path_cost = 0
            else:
                path_cost = np.trapz(path_cost, x=self.tspan)
        else:
            path_cost = 0

        if self.terminal_cost is not None:
            terminal_cost = self.terminal_cost(self.tspan[-1], X[-1], params, self.consts)
            if terminal_cost is None:
                terminal_cost = 0
        else:
            terminal_cost = 0
        return path_cost + terminal_cost

    def _unwrap_params(self, vectorized):
        # TODO: This is hella inefficient
        if self.number_of_params + self.number_of_quads == 0:
            X = vectorized.reshape([self.number_of_nodes,self.number_of_odes])
            quads = np.array([])
            params = np.array([])
        else:
            quads = np.array([])
            params = np.array([])
            X = vectorized[0:-(self.number_of_params+self.number_of_quads)].reshape([self.number_of_nodes,self.number_of_odes])
            if self.number_of_params == 0:
                quads = vectorized[-self.number_of_quads:]
            elif self.number_of_quads == 0:
                params = np.array(vectorized[-self.number_of_params:])
            else:
                quads = vectorized[-(self.number_of_params+self.number_of_quads):-(self.number_of_params)]
                params = vectorized[-self.number_of_params:]

        return X, quads, params

    def _wrap_params(self, y, q, params):
        return np.concatenate((y.flatten(), q, params))

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