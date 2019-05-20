from beluga.bvpsol.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Trajectory
from ._bvp import *
import numpy as np
import copy


class spbvp(BaseAlgorithm):
    r"""
    Reduced dimensional sparse collocation for solving boundary value problems.

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | max_nodes              | 1000            | > 2             |
    +========================+=================+=================+

    """
    # def __new__(cls, *args, **kwargs):
    #     obj = super(spbvp, cls).__new__(cls, *args, **kwargs)
    #     obj.max_nodes = kwargs.get('max_nodes', 1000)
    #     return obj

    def __init__(self, *args, **kwargs):
        BaseAlgorithm.__init__(self, *args, **kwargs)
        self.max_nodes = kwargs.get('max_nodes', 1000)

    def solve(self, solinit, **kwargs):

        solinit = copy.deepcopy(solinit)
        nstates = solinit.y.shape[1]

        def return_nil(*args, **kwargs):
            return np.array([])

        if solinit.q.size > 0:
            nquads = solinit.q.shape[1]
        else:
            nquads = 0
            self.quadrature_function = return_nil

        ndyn = solinit.dynamical_parameters.size
        nnondyn = solinit.nondynamical_parameters.size

        def _fun(t, y, params=np.array([]), const=solinit.const):
            y = y.T
            dy = np.vstack([self.derivative_function(yi[:nstates], [], params, const) for yi in y])
            return dy.T

        def _quad(t, y, params=np.array([]), const=solinit.const):
            y = y.T
            dq = np.vstack([self.quadrature_function(yi[:nstates], [], params, const) for yi in y])
            return dq.T

        def _bc(ya, qa, yb, qb, params=np.array([]), const=solinit.const):
            return self.boundarycondition_function(ya, qa, [], yb, qb, [], params[:ndyn], params[ndyn:ndyn+nnondyn],
                                                   const)

        if nquads > 0:
            opt = solve_bvp(_fun, _quad, _bc, solinit.t, solinit.y.T, solinit.q.T,
                            np.hstack((solinit.dynamical_parameters, solinit.nondynamical_parameters)),
                            max_nodes=self.max_nodes)
        else:
            opt = solve_bvp(_fun, _quad, _bc, solinit.t, solinit.y.T, solinit.q.T,
                            np.hstack((solinit.dynamical_parameters, solinit.nondynamical_parameters)),
                            max_nodes=self.max_nodes)

        sol = Trajectory(solinit)
        sol.t = opt['x']
        sol.y = opt['y'].T
        sol.q = opt['q'].T
        sol.dual = np.zeros_like(sol.y)
        if opt['p'] is not None:
            sol.dynamical_parameters = opt['p'][:ndyn]
            sol.nondynamical_parameters = opt['p'][ndyn:ndyn+nnondyn]
        else:
            sol.dynamical_parameters = np.array([])
            sol.nondynamical_parameters = np.array([])

        sol.converged = opt['success']
        return sol
