import numpy as np


class BVPSol:
    def __init__(self, t: np.ndarray, y: np.ndarray, p: np.ndarray, k: np.ndarray, q: np.ndarray):
        self.sol_type = 'BVP'
        self.t = t
        self.y = y
        self.p = p
        self.k = k
        self.q = q

    def __repr__(self):
        repr_str = self.sol_type + ' Solution\n'
        attr = self.__dict__
        for key in attr.keys():
            if isinstance(attr[key], np.ndarray):
                repr_str += '{}:\n'.format(key)
                repr_str += attr[key].__repr__() + '\n'

        return repr_str


class OCPSol(BVPSol):
    def __init__(self, t: np.ndarray, y: np.ndarray, u: np.ndarray, p: np.ndarray, k: np.ndarray, q: np.ndarray):
        BVPSol.__init__(self, t, y, p, k, q)
        self.sol_type = 'OCP'
        self.u = u

        self.dual_info = None

    class DualInfo:
        def __init__(self, lam_t, lam, nu, mu):
            self.lam_t = lam_t
            self.lam = lam
            self.nu = nu
            self.mu = mu


class DualSol(OCPSol):
    def __init__(self, t: np.ndarray, y: np.ndarray, u: np.ndarray, p: np.ndarray, k: np.ndarray, q: np.ndarray,
                 lam_t: np.ndarray, lam: np.ndarray, nu: np.ndarray, mu: np.ndarray):
        OCPSol.__init__(self, t, y, u, p, k, q)
        self.sol_type = 'Dual'

        self.lam_t = lam_t
        self.lam = lam
        self.nu = nu
        self.mu = mu


class SolSet:
    def __init__(self, prob):

        self.prob = prob
        self.solutions = []
        
        self.forward_stack = []
        self.backward_stack = []
