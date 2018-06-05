from beluga.bvpsol.algorithms import Shooting
from beluga.bvpsol import Solution
import numpy as np

tol = 1e-3

def test_Shooting_1():
    # Full 2PBVP test problem
    # This is the simplest BVP

    def odefun(t, X, p, const, arc):
        return np.hstack((X[1], -abs(X[0])))

    def bcfun(X0,Xf,p,aux):
        return np.hstack((X0[0], Xf[0]+2))

    algo = Shooting()
    solinit = Solution()
    solinit.x = np.linspace(0,4,2)
    solinit.y = np.array([[0,1],[0,1]]).T
    out = algo.solve(odefun, bcfun, solinit)
    assert out.y.T[0][0] < tol
    assert out.y.T[0][1] - 2.06641646 < tol
    assert out.y.T[-1][0] + 2 < tol
    assert out.y.T[-1][1] + 2.87588998 < tol
    assert out.x[-1] - 4 < tol

def test_Shooting_2():
    # Full 2PBVP test problem
    # This is calculating the 4th eigenvalue of Mathieu's Equation
    # This problem contains an adjustable parameter.

    def odefun(t, X, p, const, arc):
        return np.hstack((X[1], -(p[0] - 2 * 5 * np.cos(2 * t)) * X[0]))

    def bcfun(X0, Xf, p, aux):
        return np.hstack((X0[1], Xf[1], X0[0] - 1))

    algo = Shooting()
    solinit = Solution()
    solinit.x = np.linspace(0, np.pi, 30)
    solinit.y = np.vstack((np.cos(4 * solinit.x), -4 * np.sin(4 * solinit.x)))
    solinit.parameters = np.array([15])

    out = algo.solve(odefun, bcfun, solinit)
    assert out.x[-1] - np.pi < tol
    assert out.y.T[0][0] - 1 < tol
    assert out.y.T[0][1] < tol
    assert out.y.T[-1][0] - 1 < tol
    assert out.y.T[-1][1] < tol
    assert out.parameters[0] - 17.09646175 < tol
