from beluga.bvpsol.algorithms import Shooting
from beluga.bvpsol import Solution
import numpy as np

tol = 1e-4

def test_Shooting_1():
    def odefun(t, X, p, const, arc):
        return np.hstack((X[1], -abs(X[0]), 0))*X[2]

    def bcfun(X0,Xf,p,aux):
        return np.hstack((X0[0], Xf[0]+2, Xf[2]-4))

    algo = Shooting()
    solinit = Solution()
    solinit.x = np.linspace(0,1,2)
    solinit.y = np.array([[0,1,4],[-2,1,4]]).T
    solinit.aux['const'] = {}
    solinit.aux['arc_seq'] = (0,)
    solinit.parameters = np.array([])
    out = algo.solve(odefun, bcfun, solinit)
    assert out.y.T[0][0] < tol
    assert out.y.T[0][1] - 2.06366927 < tol
    assert out.y.T[0][2] - 4 < tol
    assert out.y.T[-1][0] + 2 < tol
    assert out.y.T[-1][1] + 2.87568811 < tol
    assert out.y.T[-1][2] - 4 < tol
