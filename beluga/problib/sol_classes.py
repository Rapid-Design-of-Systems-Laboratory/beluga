import numpy as np


class BaseSol:
    def __init__(self, t, y, p, k):
        self.sol_type = 'Base'
        self.t = t
        self.y = y
        self.p = p
        self.k = k

    def __repr__(self):
        repr_str = self.sol_type + ' Solution\n'
        attr = self.__dict__
        for key in attr.keys():
            if not key == 'sol_type':
                repr_str += '{}:\n'.format(key)
                repr_str += attr[key].__repr__() + '\n'

        return repr_str


class OCPSol(BaseSol):
    def __init__(self, t, y, u, p, k):
        BaseSol.__init__(self, t, y, p, k)
        self.sol_type = 'OCP'
        self.u = u


class BVPSol(BaseSol):
    def __init__(self, t, y, p, nu, k):
        BaseSol.__init__(self, t, y, p, k)
        self.sol_type = 'BVP'
        self.nu = nu


class SolSet:
    def __init__(self, prob):

        self.prob = prob
        self.solutions = []
        self.mappings = []
