from beluga.bvpsol.BaseAlgorithm import BaseAlgorithm
from beluga.ivpsol import Trajectory
from ._bvp import *
import numpy as np
import copy


class spbvp(BaseAlgorithm):
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
            o1 = np.vstack([self.derivative_function(yi[:nstates], [], params, const) for yi in y])
            o2 = np.vstack([self.quadrature_function(yi[:nstates], [], params, const) for yi in y])
            return np.hstack((o1,o2)).T

        def _bc(ya, yb, params=np.array([]), const=solinit.const):
            return self.boundarycondition_function(ya[:nstates], ya[nstates:nstates+nquads], [], yb[:nstates], yb[nstates:nstates+nquads], [], params[:ndyn], params[ndyn:ndyn+nnondyn], const)

        if nquads > 0:
            opt = solve_bvp(_fun, _bc, solinit.t, np.hstack((solinit.y, solinit.q)).T, np.hstack((solinit.dynamical_parameters, solinit.nondynamical_parameters)))
        else:
            # breakpoint()
            opt = solve_bvp(_fun, _bc, solinit.t, solinit.y.T, np.hstack((solinit.dynamical_parameters, solinit.nondynamical_parameters)))

        sol = Trajectory(solinit)
        sol.t = opt['x']
        sol.y = opt['y'].T[:, :nstates]
        sol.q = opt['y'].T[:, nstates:nstates+nquads]
        sol.dual = np.zeros_like(sol.y)
        if opt['p'] is not None:
            sol.dynamical_parameters = opt['p'][:ndyn]
            sol.nondynamical_parameters = opt['p'][ndyn:ndyn+nnondyn]
        else:
            sol.dynamical_parameters = np.array([])
            sol.nondynamical_parameters = np.array([])

        if opt['status'] == 0:
            sol.converged = True
        else:
            sol.converged = False
        return sol