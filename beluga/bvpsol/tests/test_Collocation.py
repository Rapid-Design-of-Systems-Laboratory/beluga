from beluga.bvpsol.algorithms import Collocation
from beluga.bvpsol import Solution
import numpy as np

tol = 1e-3

def test_Collocation_1():
    # Full 2PBVP test problem
    # This is the simplest BVP

    def odefun(t, X, p, const):
        return (X[1], -abs(X[0]))

    def bcfun(t0, X0, q0, tf, Xf, qf, p, ndp, aux):
        return (X0[0], Xf[0]+2)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0,4,4)
    solinit.y = np.array([[0,1],[0,1],[0,1],[0,1]])
    out = algo.solve(solinit)
    assert out.y[0][0] < tol
    assert out.y[0][1] - 2.06641646 < tol
    assert out.y[-1][0] + 2 < tol
    assert out.y[-1][1] + 2.87588998 < tol
    assert out.t[-1] - 4 < tol
    assert abs(out.y[0][1] - solinit.y[0][1]) > tol
    assert abs(out.y[-1][0] - solinit.y[-1][0]) - 2 < tol

def test_Collocation_2():
    # Full 2PBVP test problem
    # This is calculating the 4th eigenvalue of Mathieu's Equation
    # This problem contains an adjustable parameter.

    def odefun(t, X, p, const):
        return (X[1], -(p[0] - 2 * 5 * np.cos(2 * t)) * X[0])

    def bcfun(t0, X0, q0, tf, Xf, qf, p, ndp, aux):
        return (X0[1], Xf[1], X0[0] - 1)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, np.pi, 30)
    solinit.y = np.vstack((np.cos(4 * solinit.t), -4 * np.sin(4 * solinit.t))).T
    solinit.dynamical_parameters = np.array([15])

    out = algo.solve(solinit)
    assert abs(out.t[-1] - np.pi) < tol
    assert abs(out.y[0][0] - 1) < tol
    assert abs(out.y[0][1]) < tol
    assert abs(out.y[-1][0] - 1) < tol
    assert abs(out.y[-1][1]) < tol
    assert abs(out.dynamical_parameters[0] - 17.09646175) < tol

def test_Collocation_3():
    # This problem contains a parameter, but it is not explicit in the BCs.
    # Since time is buried in the ODEs, this tests if the BVP solver calculates
    # sensitivities with respect to parameters.
    def odefun(t, X, p, const):
        return 1 * p[0]

    def bcfun(t0, X0, q0, tf, Xf, qf, p, ndp, aux):
        return (X0[0] - 0, Xf[0] - 2)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 4)
    solinit.y = np.array([[0], [0], [0], [0]])
    solinit.dynamical_parameters = np.array([1])
    out = algo.solve(solinit)
    assert abs(out.dynamical_parameters - 2) < tol
