import copy
import numpy as np
# from .optimlib import *
# from beluga.problib import SymBVP


class BaseSolMap:
    def __init__(self, in_place=True):
        self.in_place = in_place

    def map_sol(self, sol):
        # Make copy of sol if mapping is not to be done in place
        if not self.in_place:
            sol = copy.deepcopy(sol)

        return sol

    def inv_map_sol(self, sol):
        # Make copy of sol if mapping is not to be done in place
        if not self.in_place:
            sol = copy.deepcopy(sol)

        return sol


class MomemtumShiftSolMap(BaseSolMap):
    def __init__(self, in_place=True):
        BaseSolMap.__init__(self, in_place=in_place)
        self.time_idx = -1

    def map_sol(self, sol):
        sol = BaseSolMap.map_sol(self, sol)

        # Append time to states
        if self.time_idx == -1:
            sol.y = np.row_stack((sol.y, sol.t))
        elif self.time_idx < 0:
            sol.y = np.insert(sol.y, self.time_idx + 1, sol.t, axis=0)
        else:
            sol.y = np.insert(sol.y, self.time_idx, sol.t, axis=0)

        # Implement normalized time
        t0, tf = sol.t[0], sol.t[-1]
        scale_factor = tf - t0
        sol.t = (sol.t - t0) / scale_factor

        return sol

    def inv_map_sol(self, sol):
        sol = BaseSolMap.inv_map_sol(self, sol)

        sol.t = sol.y[self.time_idx, :]
        sol.y = np.delete(sol.y, self.time_idx, axis=0)

        return sol


class ScaleTime(BaseSolMap):
    pass


class RASHS(BaseSolMap):
    pass


class EpsTrig(BaseSolMap):
    pass


class UTM(BaseSolMap):
    pass


class Dualize(BaseSolMap):
    pass


class PMP(BaseSolMap):
    pass


