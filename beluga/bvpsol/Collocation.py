from beluga.bvpsol.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Trajectory
import numpy as np
import copy
from scipy.optimize import minimize as mini
from npnlp import minimize
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
        | number_of_nodes_max    | 100             | >= 4            |
        +------------------------+-----------------+-----------------+
        | number_of_nodes_min    | 30              | >= 4            |
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
        number_of_nodes_min = kwargs.get('number_of_nodes_min', 30)
        number_of_nodes_max = kwargs.get('number_of_nodes_max', 100)
        use_numba = kwargs.get('use_numba', False)
        verbose = kwargs.get('verbose', False)

        obj.cached = cached
        obj.tolerance = tolerance
        obj.max_error = max_error
        obj.max_iterations = max_iterations
        obj.number_of_nodes_min = number_of_nodes_min
        obj.number_of_nodes_max = number_of_nodes_max
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
        self.number_of_nodes = self.number_of_nodes_min
        number_of_datapoints = len(sol.t)
        if number_of_datapoints < 4:
            # Special case where polynomial interpolation fails. Use linear interpolation to get 4 nodes.
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
            if self.quadrature_function is not None and len(sol.q[0]) is not 0:
                raise NotImplemented # TODO: Put reconstruction of q's in Trajectory()? Or leave in ivpsol?
        else:
            self.number_of_nodes = number_of_datapoints

        # self.constraint = {'type': 'eq', 'fun': self._collocation_constraint}
        self.constraint_midpoint = {'type': 'eq', 'fun': self._collocation_constraint_midpoint}
        self.constraint_boundary = {'type': 'eq', 'fun': self._collocation_constraint_boundary}

        # Set up initial guess and other info
        meshing = True
        while meshing:
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

            # This is SciPy syntax
            xopt = mini(self._collocation_cost, vectorized, args=(), method='SLSQP', jac=None, hess=None, hessp=None, bounds=None, constraints=[self.constraint_midpoint, self.constraint_boundary], tol=self.tolerance, callback=None, options={'maxiter':self.max_iterations})
            # xopt = minimize(self._collocation_cost, vectorized, nonlconeq=lambda X, L: np.hstack((self._collocation_constraint_boundary(X), self._collocation_constraint_midpoint(X))), method='sqp')
            sol.t = self.tspan
            sol.y, sol.q, sol.u, sol.dynamical_parameters, sol.nondynamical_parameters = self._unwrap_params(xopt['x'])
            if len(sol.t) >= self.number_of_nodes_max:
                meshing = False
            else:
                dX = np.squeeze([self.derivative_function(yi, ui, sol.dynamical_parameters, self.const) for yi, ui in zip(sol.y, sol.u)])
                if len(dX.shape) == 1:
                    dX = np.array([dX]).T
                dp0 = dX[:-1]
                dp1 = dX[1:]
                p0 = sol.y[:-1]
                p1 = sol.y[1:]
                t0 = self.tspan[:-1]
                t1 = self.tspan[1:]
                u0 = sol.u[:-1]
                uf = sol.u[1:]
                u_midpoint = (u0 + uf) / 2
                midpoint_predicted = np.column_stack([1 / 2 * (p0[:, ii] + p1[:, ii]) + (t1 - t0) / 8 * (dp0[:, ii] - dp1[:, ii]) for ii in range(sol.y.shape[1])])
                midpoint_derivative_predicted = np.column_stack([-3 / 2 * (p0[:, ii] - p1[:, ii]) / (t1 - t0) - 1 / 4 * (dp0[:, ii] + dp1[:, ii]) for ii in range(sol.y.shape[1])])
                dp12 = np.squeeze([self.derivative_function(yi, ui, sol.dynamical_parameters, self.const) for yi, ui in zip(midpoint_predicted, u_midpoint)])  # TODO: Vectorize, so this one works as well
                u13 = (u0*2 + uf*1)/3
                u23 = (u0*1 + uf*2)/3
                c1 = np.zeros((len(sol.t) - 1, sol.y.shape[1]))
                c2 = np.zeros((len(sol.t) - 1, sol.y.shape[1]))
                c3 = np.zeros((len(sol.t) - 1, sol.y.shape[1]))
                c4 = np.zeros((len(sol.t) - 1, sol.y.shape[1]))
                for ii in range(len(sol.t) - 1):
                    c1[ii], c2[ii], c3[ii], c4[ii] = self._get_poly_coefficients_2_2(p0[ii], dp0[ii], p1[ii], dp1[ii], (t1 - t0)[ii])
                x13 = np.column_stack([c1[:, ii] + c2[:, ii] * ((1 / 3) * (t1 - t0)) + c3[:, ii] * ((1 / 3) * (t1 - t0)) ** 2 + c4[:, ii] * ((1 / 3) * (t1 - t0)) ** 3 for ii in range(sol.y.shape[1])])
                x23 = np.column_stack([c1[:, ii] + c2[:, ii] * ((2 / 3) * (t1 - t0)) + c3[:, ii] * ((2 / 3) * (t1 - t0)) ** 2 + c4[:, ii] * ((2 / 3) * (t1 - t0)) ** 3 for ii in range(sol.y.shape[1])])
                dx13 = np.squeeze([self.derivative_function(yi, ui, sol.dynamical_parameters, self.const) for yi, ui in zip(x13, u13)])
                dx23 = np.squeeze([self.derivative_function(yi, ui, sol.dynamical_parameters, self.const) for yi, ui in zip(x23, u23)])
                xd03 = np.column_stack([c2[:, ii] + 2*c3[:, ii] * ((0 / 3) * (t1 - t0)) + 3*c4[:, ii] * ((0 / 3) * (t1 - t0)) ** 2 for ii in range(sol.y.shape[1])])
                xd13 = np.column_stack([c2[:, ii] + 2*c3[:, ii] * ((1 / 3) * (t1 - t0)) + 3*c4[:, ii] * ((1 / 3) * (t1 - t0)) ** 2 for ii in range(sol.y.shape[1])])
                xd23 = np.column_stack([c2[:, ii] + 2*c3[:, ii] * ((2 / 3) * (t1 - t0)) + 3*c4[:, ii] * ((2 / 3) * (t1 - t0)) ** 2 for ii in range(sol.y.shape[1])])
                xd33 = np.column_stack([c2[:, ii] + 2*c3[:, ii] * ((3 / 3) * (t1 - t0)) + 3*c4[:, ii] * ((3 / 3) * (t1 - t0)) ** 2 for ii in range(sol.y.shape[1])])
                err = [(abs(dp0[ii,:]-xd03[ii,:]), abs(dx13[ii,:]-xd13[ii,:]), abs(dx23[ii,:]-xd23[ii,:]), abs(dp1[ii,:]-xd33[ii,:])) for ii in range(len(sol.t)-1)]
                err = np.array([max(1/6*e[0] + 4/6*e[1] + 1/6*e[2]) for e in err])
                n_lim = int(max(2, np.floor(len(sol.t)*0.15)))
                add_nodes = np.argsort(-err)[:n_lim]
                for ii in add_nodes:
                    if err[ii] > self.tolerance and self.number_of_nodes_max >= self.number_of_nodes + 2:
                        meshing = True
                        new_sol = copy.deepcopy(sol)
                        t1add = (sol.t[ii] * 2 + sol.t[ii + 1] * 1) / 3
                        t2add = (sol.t[ii] * 1 + sol.t[ii + 1] * 2) / 3
                        y1add, q1add, u1add = sol(t1add)
                        y2add, q2add, u2add = sol(t2add)
                        new_sol.t = np.hstack((new_sol.t, t1add))
                        new_sol.t = np.hstack((new_sol.t, t2add))
                        new_sol.y = np.vstack((new_sol.y, y1add))
                        new_sol.y = np.vstack((new_sol.y, y2add))
                        new_sol.q = np.vstack((new_sol.q, q1add))
                        new_sol.q = np.vstack((new_sol.q, q2add))
                        new_sol.u = np.vstack((new_sol.u, u1add))
                        new_sol.u = np.vstack((new_sol.u, u2add))
                        self.number_of_nodes += 2
                        mapping = np.argsort(new_sol.t)
                        sol.t = new_sol.t[mapping]
                        sol.y = new_sol.y[mapping]
                        if sol.q.size > 0:
                            sol.q = new_sol.q[mapping]
                        if sol.u.size > 0:
                            sol.u = new_sol.u[mapping]
                    else:
                        meshing = False


        logging.debug(xopt['message'])

        # if xopt['status'] == 0:
        #     sol.converged = True
        sol.converged = xopt['success']

        # Organize the output with the sol() structure
        return sol

    def _collocation_constraint_midpoint(self, vectorized):
        y, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        gamma = Trajectory(self.tspan, y, np.array([]), u)
        # dX = np.squeeze(self.derivative_function(self.tspan, X.T, params, self.aux)).T # TODO: Vectorized our code compiler so this line works
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
        midpoint_predicted = np.column_stack([1 / 2 * (p0[:, ii] + p1[:, ii]) + (t1 - t0) / 8 * (dp0[:, ii] - dp1[:, ii]) for ii in range(y.shape[1])])
        midpoint_derivative_predicted = np.column_stack([-3 / 2 * (p0[:,ii] - p1[:,ii]) / (t1-t0) - 1 / 4 * (dp0[:,ii] + dp1[:,ii]) for ii in range(y.shape[1])])
        midpoint_derivative_actual = np.squeeze([self.derivative_function(yi, ui, params, self.const) for yi, ui in zip(midpoint_predicted, u_midpoint)]) # TODO: Vectorize, so this one works as well
        if len(midpoint_derivative_actual.shape) == 1:
            midpoint_derivative_actual = np.array([midpoint_derivative_actual]).T
        outvec = midpoint_derivative_predicted - midpoint_derivative_actual
        d2 = outvec.shape[1]
        outvec = np.hstack([outvec[:,ii][:] for ii in range(d2)])
        return outvec

    def _collocation_constraint_boundary(self, vectorized):
        X, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        return self.boundarycondition_function(X[0], [], u[0], X[-1], [], u[-1], params, nondyn_params, self.const)

    def _collocation_cost(self, vectorized):
        X, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        if self.initial_cost_function is not None:
            c0 = self.initial_cost_function(X[0], u[0], params, self.const)
        else:
            c0 = 0

        if self.terminal_cost_function is not None:
            cf = self.terminal_cost_function(X[-1], u[-1], params, self.const)
        else:
            cf = 0

        y, quads0, u, params, nondyn_params = self._unwrap_params(vectorized)
        dX = np.squeeze([self.derivative_function(yi, ui, params, self.const) for yi, ui in zip(y, u)])
        if len(dX.shape) == 1:
            dX = np.array([dX]).T
        dp0 = dX[:-1]
        dp1 = dX[1:]
        p0 = y[:-1]
        p1 = y[1:]
        u0 = u[:-1]
        uf = u[1:]
        t0 = self.tspan[:-1]
        t1 = self.tspan[1:]
        u_midpoint = (u0 + uf) / 2
        midpoint_predicted = np.column_stack([1/2*(p0[:,ii]+p1[:,ii]) + (t1-t0)/8*(dp0[:,ii]-dp1[:,ii]) for ii in range(y.shape[1])])

        cpath = 0
        if self.path_cost_function is not None:
            for ii in range(len(midpoint_predicted)):
                wk = self.path_cost_function(y[ii], u[ii], params, self.const)
                wk12 = self.path_cost_function(midpoint_predicted[ii], u_midpoint[ii], params, self.const)
                wk1 = self.path_cost_function(y[ii+1], u[ii+1], params, self.const)
                cpath += (1/6*wk + 4/6*wk12 + 1/6*wk1)*(self.tspan[ii+1] - self.tspan[ii])

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
    def _get_poly_coefficients_2_2(p0, dp0, p1, dp1, h):
        C1 = p0
        C2 = dp0
        C3 = -3*p0/h**2 - 2*dp0/h + 3*p1/h**2 - dp1/h
        C4 = 2*p0/h**3 + dp0/h**2 - 2*p1/h**3 + dp1/h**2
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