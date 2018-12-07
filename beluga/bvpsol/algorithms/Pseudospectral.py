from beluga.bvpsol.algorithms import BaseAlgorithm
from beluga.ivpsol import Trajectory
from scipy.optimize import minimize

import logging
import numpy as np
import sys
import copy

class Pseudospectral(BaseAlgorithm):
    def __new__(cls, *args, **kwargs):
        """
        Creates a new Pseudospectral object.

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

        obj = super(Pseudospectral, cls).__new__(cls, *args, **kwargs)

        cached = kwargs.get('cached', True)
        tolerance = kwargs.get('tolerance', 1e-4)
        max_error = kwargs.get('max_error', 100)
        max_iterations = kwargs.get('max_iterations', 100)
        number_of_nodes = kwargs.get('number_of_nodes', 10)
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
        num_eoms = sol.y.shape[1]
        num_controls = sol.u.shape[1]
        num_params = len(sol.dynamical_parameters)
        num_quads = 0

        t0 = sol.t[0]
        tf = sol.t[-1]

        if len(sol.t) < 4:
            raise ValueError

        if len(sol.t) != self.number_of_nodes:
            T = []
            Y = []
            Q = []
            U = []
            tau = lglnodes(self.number_of_nodes - 1)
            tspan = (tau*(tf-t0) + tf+t0)/2
            y = np.column_stack([linter(sol.t, sol.y[:, ii],tspan) for ii in range(num_eoms)])
            if num_quads > 0:
                q = np.column_stack([linter(sol.t, sol.q[:, ii], tspan) for ii in range(num_quads)])
            else:
                q = np.array([])

            u = np.column_stack([linter(sol.t, sol.u[:, ii], tspan) for ii in range(num_controls)])
            sol.t = tspan
            sol.y = y
            sol.q = q
            sol.u = u

        tau = lglnodes(self.number_of_nodes - 1)
        weights = lglweights(tau)
        D = lglD(tau)

        Xinit = np.hstack([sol.y[:,ii][:] for ii in range(num_eoms)] + [sol.u[:,ii] for ii in range(num_controls)] + [sol.dynamical_parameters])
        arrrgs = (self.derivative_function, self.boundarycondition_function, self.path_cost_function, self.inequality_constraint_function, num_eoms, num_controls, weights, D, tf, t0, self.number_of_nodes, sol.aux)
        constraints = [{'type': 'eq', 'fun': _eq_constraints, 'args': arrrgs}]
        if self.inequality_constraint_function is not None:
            constraints.append({'type': 'ineq', 'fun': _ineq_constraints, 'args':arrrgs})

        iprint = 1
        xopt = minimize(_cost, Xinit, args=arrrgs, method='SLSQP', tol=1e-8, constraints=constraints, options={'ftol':1e-8,'disp':True, 'iprint':iprint})

        X = xopt['x']
        states = [X[(ii) * self.number_of_nodes:(ii + 1) * self.number_of_nodes] for ii in range(num_eoms)]
        ni = (num_eoms) * self.number_of_nodes
        controls = [X[ni + ii * self.number_of_nodes:ni + (ii + 1) * self.number_of_nodes] for ii in range(num_controls)]
        y = np.vstack(states).T
        u = np.vstack(controls).T
        sol.y = y
        sol.u = u
        sol.t = (tau*(tf-t0) + (tf+t0))/2
        sol.converged = True

        return sol

def lpoly(n,x):
    if n == 0:
        return np.ones_like(x), np.zeros_like(x)
    if n == 1:
        return np.array(x), np.ones_like(x)

    first_polynomial = np.ones_like(x)
    first_pd = np.zeros_like(x)
    poly = x
    pd = np.ones_like(x)
    for ii in range(1,n): #TODO: MAKE FASTERRRR
        n_poly = ((2*(ii+1)-1)*x*poly - ii*first_polynomial)/(ii+1)
        n_pd = first_pd + (2*ii+1)*poly
        first_polynomial = copy.copy(poly)
        poly = copy.copy(n_poly)
        first_pd = pd
        pd = n_pd
    return n_poly, n_pd

def lglnodes(n):
    theta = (4*np.arange(1,n+1)-1)*np.pi/(4*n+2)
    sigma = -(1-(n-1)/(8*n**3)-(39-28/np.sin(theta)**2)/(384*n**4))*np.cos(theta)
    eps = sys.float_info.epsilon
    ze = (sigma[:-1] + sigma[1:])/2
    ze1 = ze+eps*10+1
    while max(abs(ze1-ze)) >= eps*10:
        ze1 = ze
        y, dy = lpoly(n, ze)
        ze = ze-(1-ze*ze)*dy/(2*ze*dy - n*(n+1)*y)
    return np.hstack((-1, ze, 1))

def lglweights(T):
    n = len(T)-1
    y, dy = lpoly(n, T[1:-1])
    return np.hstack((2/(n*(n+1)), 2/(n*(n+1)*y**2), 2/(n*(n+1))))

def lglD(T):
    n = len(T) - 1

    if n+1 == 0:
        return np.array([])

    y, dy = lpoly(n, T)
    D = (1/((T/y)*np.array([y]).T - (1/y)*np.array([T*y]).T + np.eye(n+1)) - np.eye(n+1)).T
    D[0,0] = -n*(n+1)/4
    D[-1,-1] = n*(n+1)/4
    return D

def _cost(X, eom, bc, path, ineq, num_eoms, num_controls, weights, D, tf, t0, n, aux):
    X = copy.deepcopy(X)
    states = [X[(ii) * n:(ii + 1) * n] for ii in range(num_eoms)]
    ni = (num_eoms) * n
    controls = [X[ni + ii * n:ni + (ii + 1) * n] for ii in range(num_controls)]
    ni = (num_eoms + num_controls) * n
    params = X[ni:]
    y = np.column_stack(states)
    u = np.column_stack(controls)
    L = np.hstack([path([], y[ii], u[ii], params, aux) for ii in range(n)])
    c = (tf - t0) / 4 * np.inner(weights, L)
    return c

def _eq_constraints(X, eom, bc, path, ineq, num_eoms, num_controls, weights, D, tf, t0, n, aux):
    states = [X[(ii) * n:(ii + 1) * n] for ii in range(num_eoms)]
    ni = (num_eoms) * n
    controls = [X[ni + ii * n:ni + (ii + 1) * n] for ii in range(num_controls)]
    ni = (num_eoms + num_controls) * n
    params = X[ni:]
    y = np.column_stack(states)
    u = np.column_stack(controls)
    yd = np.vstack([eom([], y[ii], u[ii], params, aux) for ii in range(n)])
    F = (tf - t0) / 2 * yd

    c0 = bc(t0, y[0], [], u[0], tf, y[-1], [], u[-1], params, [], aux)
    c1 = np.dot(D, y) - F
    c1 = np.hstack([c1[:, ii][:] for ii in range(num_eoms)])
    return np.hstack((c0, c1))


def _ineq_constraints(X, eom, bc, path, ineq, num_eoms, num_controls, weights, D, tf, t0, n, aux):
    states = [X[(ii) * n:(ii + 1) * n] for ii in range(num_eoms)]
    ni = (num_eoms) * n
    controls = [X[ni + ii * n:ni + (ii + 1) * n] for ii in range(num_controls)]
    ni = (num_eoms + num_controls) * n
    params = X[ni:]
    y = np.vstack(states).T
    u = np.vstack(controls).T
    cp = np.hstack([ineq([], y[ii], u[ii], params, aux) for ii in range(n)])
    return -cp


def linter(x,y,xi):
    n = len(x) - 1
    ni = len(xi)
    L = np.ones((n+1,ni))
    for k in range(n+1):
        for kk in range(k):
            L[kk,:] = L[kk,:]*(xi - x[k])/(x[kk]-x[k])

        for kk in np.arange(k, n):
            L[kk+1,:] = L[kk+1,:]*(xi - x[k])/(x[kk+1]-x[k])

    return np.dot(y,L)
