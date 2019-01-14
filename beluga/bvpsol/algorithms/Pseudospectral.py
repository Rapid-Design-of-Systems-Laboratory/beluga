from beluga.bvpsol.algorithms import BaseAlgorithm
from npnlp import minimize, kkt_multipliers
from beluga.ivpsol import Trajectory

import numba

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
        | closure                | False           | Bool            |
        +------------------------+-----------------+-----------------+
        | max_error              | 100             | > 0             |
        +------------------------+-----------------+-----------------+
        | max_iterations         | 100             | > 0             |
        +------------------------+-----------------+-----------------+
        | number_of_nodes        | 15              | >= 4            |
        +------------------------+-----------------+-----------------+
        | tolerance              | 1e-4            | > 0             |
        +------------------------+-----------------+-----------------+
        """

        obj = super(Pseudospectral, cls).__new__(cls, *args, **kwargs)

        closure = kwargs.get('closure', False)
        max_error = kwargs.get('max_error', 100)
        max_iterations = kwargs.get('max_iterations', 100)
        number_of_nodes = kwargs.get('number_of_nodes', 15)
        tolerance = kwargs.get('tolerance', 1e-4)

        obj.closure = closure
        obj.max_error = max_error
        obj.max_iterations = max_iterations
        obj.number_of_nodes = number_of_nodes
        obj.tolerance = tolerance
        return obj

    def solve(self, solinit, **kwargs):
        """
        Solve a two-point boundary value problem using the pseudospectral method.

        :param deriv_func: The ODE function.
        :param quad_func: The quad func.
        :param bc_func: The boundary conditions function.
        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        """
        sol = copy.deepcopy(solinit)
        num_eoms = sol.y.shape[1]
        if sol.u.size > 0:
            num_controls = sol.u.shape[1]
        else:
            num_controls = 0
        # num_controls=0

        # Default costs to return nothing if not defined
        def return_nil(*args, **kwargs):
            return np.array([])

        if self.initial_cost_function is None:
            self.initial_cost_function = return_nil

        if self.path_cost_function is None:
            self.path_cost_function = return_nil

        if self.terminal_cost_function is None:
            self.terminal_cost_function = return_nil

        if self.inequality_constraint_function is None:
            self.inequality_constraint_function = return_nil

        if num_controls > 0:
            num_bcs = len(self.boundarycondition_function(sol.t[0], sol.y[0], [], sol.u[0], sol.t[-1], sol.y[-1], [], sol.u[-1], sol.dynamical_parameters, sol.nondynamical_parameters, sol.aux))
        else:
            num_bcs = len(self.boundarycondition_function(sol.t[0], sol.y[0], [], sol.t[-1], sol.y[-1], [], sol.dynamical_parameters, sol.nondynamical_parameters, sol.aux))

        num_params = len(sol.dynamical_parameters)
        num_nondynamical_params = len(sol.nondynamical_parameters)
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

            if num_controls > 0:
                u = np.column_stack([linter(sol.t, sol.u[:, ii], tspan) for ii in range(num_controls)])
            else:
                u = np.array([])

            sol.t = tspan
            sol.y = y
            sol.q = q
            sol.u = u

        tau = lglnodes(self.number_of_nodes - 1)
        weights = lglweights(tau)
        D = lglD(tau)
        Xinit = _wrap_params(sol, num_eoms, num_controls, num_params, num_nondynamical_params, self.number_of_nodes)
        extra_data = {'derivative_function': self.derivative_function,
                      'boundarycondition_function': self.boundarycondition_function,
                      'pathcost_function': self.path_cost_function,
                      'terminalcost_function': self.terminal_cost_function,
                      'inequalityconstraint_function': self.inequality_constraint_function,
                      'num_eoms': num_eoms,
                      'num_controls': num_controls,
                      'num_parameters': num_params,
                      'num_nondynamical_parameters': num_nondynamical_params,
                      'weights': weights,
                      'D': D,
                      'nodes': self.number_of_nodes,
                      'aux': sol.aux,
                      'closure': self.closure,
                      'knots': 0,
                      't0': t0,
                      'tf': tf}

        kkt0 = kkt_multipliers()
        if not self.closure:
            kkt0.equality_nonlinear = np.zeros(num_eoms * self.number_of_nodes + num_bcs)
        else:
            kkt0.equality_nonlinear = np.zeros(num_eoms * self.number_of_nodes + num_bcs + 1)
            raise NotImplementedError('Closure conditions are not implemented.')


        xopt = minimize(lambda x: _cost(x, extra_data), x0=Xinit, kkt0=kkt0,
                        nonlconeq=lambda x, kkt: _eq_constraints(x, kkt, extra_data),
                        nonlconineq=lambda x, kkt: _ineq_constraints(x, kkt, extra_data),
                        method='sqp')
        X = xopt['x']
        y, u, params, nondynamical_params = _unwrap_params(X, num_eoms, num_controls, num_params, num_nondynamical_params, self.number_of_nodes)
        sol.y = y
        sol.u = u
        sol.dynamical_parameters = params
        sol.nondynamical_parameters = nondynamical_params
        sol.t = (tau*(tf-t0) + (tf+t0))/2
        sol.converged = True

        return sol

def _lagrange_to_costates(KKT, num_eoms, nodes, weights):
    out = np.column_stack([KKT.equality_nonlinear[(ii) * nodes:(ii + 1) * nodes]/weights for ii in range(num_eoms)])
    return out

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

def _cost(X, data):
    num_eoms = data['num_eoms']
    num_controls = data['num_controls']
    num_parameters = data['num_parameters']
    num_nondynamical_parameters = data['num_nondynamical_parameters']
    path = data['pathcost_function']
    aux = data['aux']
    weights = data['weights']
    n = data['nodes']
    t0 = data['t0']
    tf = data['tf']
    y, u, params, nondynamical_params = _unwrap_params(X, num_eoms, num_controls, num_parameters, num_nondynamical_parameters, n)
    if num_controls > 0:
        L = np.hstack([path([], y[ii], u[ii], params, aux) for ii in range(n)])
    else:
        return 0

    c = (tf - t0) / 4 * np.inner(weights, L)
    return c

def _eq_constraints(X, KKT, data):
    num_eoms = data['num_eoms']
    num_controls = data['num_controls']
    num_parameters = data['num_parameters']
    num_nondynamical_parameters = data['num_nondynamical_parameters']
    eom = data['derivative_function']
    path = data['pathcost_function']
    bc = data['boundarycondition_function']
    aux = data['aux']
    weights = data['weights']
    D = data['D']
    closure = data['closure']
    n = data['nodes']
    t0 = data['t0']
    tf = data['tf']
    y, u, params, nondynamical_params = _unwrap_params(X, num_eoms, num_controls, num_parameters, num_nondynamical_parameters, n)
    if num_controls > 0:
        yd = np.vstack([eom([], y[ii], u[ii], params, aux) for ii in range(n)])
    else:
        yd = np.vstack([eom([], y[ii], params, aux) for ii in range(n)])

    F = (tf - t0) / 2 * yd

    if num_controls > 0:
        c0 = bc(t0, y[0], [], u[0], tf, y[-1], [], u[-1], params, nondynamical_params, aux)
    else:
        c0 = bc(t0, y[0], [], tf, y[-1], [], params, nondynamical_params, aux)
    c1 = np.dot(D, y) - F
    c1 = np.hstack([c1[:, ii][:] for ii in range(num_eoms)])

    if closure and KKT is not None:
        l = _lagrange_to_costates(KKT, num_eoms, n, weights)
        p0 = path([], y[0], u[0], params, aux)
        pf = path([], y[-1], u[-1], params, aux)
        h0 = p0 + np.inner(l[0], eom([], y[0], u[0], params, aux))
        hf = pf + np.inner(l[-1], eom([], y[-1], u[-1], params, aux))

        out = np.hstack((c1, c0, h0-hf))
    else:
        out = np.hstack((c1, c0))

    return out

def _unwrap_params(X, num_eoms, num_controls, num_params, num_nondynamical_params, nodes):
    states = [X[(ii) * nodes:(ii + 1) * nodes] for ii in range(num_eoms)]
    ni = (num_eoms) * nodes
    controls = [X[ni + ii * nodes:ni + (ii + 1) * nodes] for ii in range(num_controls)]
    ni = (num_eoms + num_controls) * nodes
    params = X[ni:ni + num_params]
    ni = ni + num_params
    nondynamical_params = X[ni:]
    y = np.column_stack(states)
    if num_controls > 0:
        u = np.column_stack(controls)
    else:
        u = np.array([])

    return y, u, params, nondynamical_params

def _wrap_params(sol, num_eoms, num_controls, num_params, num_nondynamical_params, nodes):
    X = np.hstack([sol.y[:, ii][:] for ii in range(num_eoms)] + [sol.u[:, ii] for ii in range(num_controls)] +
                  [sol.dynamical_parameters] + [sol.nondynamical_parameters])
    return X

def _ineq_constraints(X, KKT, data):
    num_eoms = data['num_eoms']
    num_controls = data['num_controls']
    num_parameters = data['num_parameters']
    num_nondynamical_parameters = data['num_nondynamical_parameters']
    ineq = data['inequalityconstraint_function']
    aux = data['aux']
    weights = data['weights']
    n = data['nodes']
    y, u, params, nondynamical_params = _unwrap_params(X, num_eoms, num_controls, num_parameters, num_nondynamical_parameters, n)
    if num_controls > 0:
        cp = np.hstack([ineq([], y[ii], u[ii], params, aux) for ii in range(n)])
    else:
        cp = np.hstack([ineq([], y[ii], [], params, aux) for ii in range(n)])
    return cp


@numba.jit()
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
