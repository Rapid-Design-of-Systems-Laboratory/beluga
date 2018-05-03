import numpy as np
from scipy.optimize import minimize
import time
from .ivp import sol
import copy
from beluga.utils import keyboard
from beluga.ivpsol.integrators.ode45 import ode45
from scipy.integrate import simps


class Algorithm(object):
    '''
    I'm an algorithm
    '''
    def __new__(cls, ivp=None, options='default'):
        obj = super(Algorithm, cls).__new__(cls)
        if isinstance(options, str):
            obj.options = cls._get_default_options(options)
        else:
            obj.options = options

        if ivp is not None:
            return cls.__call__(obj, ivp)
        else:
            return obj

    def _integrate_quads(self, x, y, quads0, params, consts, quads=None):
        if quads0.size == 0:
            return np.array([])

        if quads is not None:
            dquads = np.squeeze(quads(x,y.T,params,consts))
            quickquad = simps(dquads, x=x)
        else:
            dquads = np.squeeze([self.quadratures(x[ii], y[ii], params, consts) for ii in range(y.shape[0])])
            quickquad = simps(dquads.T, x=x)
        quadsf = quickquad + quads0
        return quadsf

    @classmethod
    def _get_default_options(cls, options='default'):
        return []


class Propagator(Algorithm):
    '''
    Propagator of differential equations
    '''

    def __call__(self, ivp, tspan, y0, *args, **kwargs):
        time0 = time.time()
        # Create a deep copy to prevent corrupting original data
        problem_copy = copy.deepcopy(ivp)
        solinit = problem_copy.sol
        eoms = problem_copy.eoms

        use_stopping_condition = False
        if 'stopping_condition' in kwargs and kwargs['stopping_condition'] is not None:
            use_stopping_condition = True

        if use_stopping_condition is True:
            T = np.array([tspan[0]])
            X = np.array([y0])
            stopping_condition = kwargs['stopping_condition']
            dt = 0.005*tspan[-1]
            while stopping_condition(T[-1],X[-1],params) == False:
                Tnew, Xnew = ode45(eoms, [T[-1],T[-1]+dt], X[-1], params, AbsTol=1e-6, RelTol=1e-6)
                T = np.hstack((T,Tnew[1:]))
                X = np.vstack((X,Xnew[1:]))
        else:
            # T, X = ode45(eoms, tspan, y0, params, args, AbsTol=1e-6, RelTol=1e-6)
            T, X = ode45(eoms, tspan, y0, *args, AbsTol=1e-6, RelTol=1e-6)
            # T, X = ode45(eoms, tspan, y0, params, AbsTol=1e-8, RelTol=1e-8)

        solout = sol()
        solout.x = T
        solout.y = X
        solout.quads = None  # TODO: Reconstruct these above
        solout.params = solinit.params

        return solout


class Collocation(Algorithm):

    '''
    Collocation solver of differential equations
    '''

    def __call__(self, ivp, options):
        if options is not None:
            self.options = options

        time0 = time.time()
        # Grab some options
        self.display_flag = bool(self.options[0])
        self.number_of_nodes = int(self.options[1])

        if self.number_of_nodes < 2:
            raise ValueError('Must have more than 1 node in collocation.')

        # Take the initial solution and convert to np arrays, assume linear interpolation if not enough points are given
        probout = copy.deepcopy(ivp)
        solinit = probout.sol

        reconstruct = False
        if len(solinit.x) < self.number_of_nodes:
            try:
                solinit.x = np.linspace(solinit.x[0], solinit.x[-1], self.number_of_nodes)
                solinit.y = np.zeros((self.number_of_nodes, len(solinit.y[0])))
            except:
                solinit.x = np.linspace(solinit.x[0], solinit.x[-1], self.number_of_nodes)
                solinit.y = np.zeros((self.number_of_nodes, len(solinit.y)))
                ivp.sol.y = np.concatenate((solinit.y,solinit.y))
            reconstruct = True

        if len(solinit.x) > self.number_of_nodes:
            solinit.x = np.linspace(solinit.x[0], solinit.x[-1], self.number_of_nodes)
            solinit.y = np.zeros((self.number_of_nodes, len(solinit.y[0])))
            reconstruct = True

        if reconstruct is True:
            for ii in range(self.number_of_nodes):
                x,y,quads = self.reconstruct(solinit.x[ii], ivp)
                solinit.y[ii] = y

        # Set up some required class functions for collocation
        self.eoms = ivp.eoms
        self.quadratures = ivp.quadratures
        self.path_cost = ivp.path_cost
        self.terminal_cost = ivp.terminal_cost
        self.bcs = ivp.boundary_conditions

        # self.constraint = {'type': 'eq', 'fun': self._collocation_constraint}
        self.constraint_midpoint = {'type': 'eq', 'fun': self._collocation_constraint_midpoint}
        self.constraint_boundary = {'type': 'eq', 'fun': self._collocation_constraint_boundary}

        # Set up initial guess and other info
        self.tspan = solinit.x
        self.number_of_odes = len(solinit.y[0])
        if solinit.quads is not None:
            self.number_of_quads = len(solinit.quads)
        else:
            self.number_of_quads = 0
            solinit.quads = []

        if solinit.params is None:
            self.number_of_params = 0
            solinit.params = []

        else:
            self.number_of_params = len(solinit.params)

        vectorized = self._wrap_params(solinit.y, solinit.quads, solinit.params)
        self.consts = solinit.consts

        if self.display_flag > 0:
            print('Running collocation... ')

        xopt = minimize(self._collocation_cost, vectorized, args=(), method='SLSQP', jac=None, hess=None, hessp=None, bounds=None, constraints=[self.constraint_midpoint, self.constraint_boundary], tol=None, callback=None, options=None)
        time1 = time.time()
        if self.display_flag > 0:
            print('Done')

        # Organize the output with the sol() structure
        solution = sol()
        solution.x = self.tspan
        solution.y, solution.quads, solution.params = self._unwrap_params(xopt['x'])
        solution.consts = ivp.sol.consts
        solution.xopt = xopt
        solution.time = time1-time0
        probout.sol = solution
        return probout

    def reconstruct(self, time, ivp):
        # TODO: Rewrite this trash
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
        X, quads0, params = self._unwrap_params(vectorized)
        tf = self.tspan[-1]
        # dX = np.array([self.eoms(self.tspan[ii], X[ii], params, self.consts) for ii in range(X.shape[0])])
        dX = np.squeeze(self.eoms(self.tspan, X.T, params, self.consts)).T
        # dX = self.pool.starmap(self.eoms, [self.tspan, X, params, self.consts])
        dp0 = dX[:-1]
        dp1 = dX[1:]
        p0 = X[:-1]
        p1 = X[1:]
        t0 = self.tspan[:-1]
        t1 = self.tspan[1:]
        t12 = (t0+t1)/2
        midpoint_predicted = 1 / 2 * (p0 + p1) + tf / (self.number_of_nodes - 1) / 8 * (dp0 - dp1)
        midpoint_derivative_predicted = -3 / 2 * (self.number_of_nodes - 1) / tf * (p0 - p1) - 1 / 4 * (dp0 + dp1)
        midpoint_derivative_actual = np.squeeze(self.eoms(t12, midpoint_predicted.T, params, self.consts)).T
        outvec = midpoint_derivative_predicted - midpoint_derivative_actual
        return outvec.flatten()

    def _collocation_constraint_boundary(self, vectorized):
        X, quads0, params = self._unwrap_params(vectorized)
        if len(quads0) == 0:
            try:
                return np.squeeze(self.bcs(self.tspan[0], X[0], self.tspan[-1], X[-1], [], [], params, self.consts))
            except:
                keyboard()
        else:
            quadsf = self._integrate_quads(self.tspan, X, quads0, params, self.consts, quads=self.quadratures)
            return np.squeeze(self.bcs(self.tspan[0], X[0], self.tspan[-1], X[-1], quads0, quadsf, params, self.consts))

    def _collocation_cost(self, vectorized):
        X, quads0, params = self._unwrap_params(vectorized)
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


    def _wrap_params(self, X, quads0, params):
        return np.concatenate((X.flatten(), quads0, params))

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
