from beluga.bvpsol.algorithms import Shooting
from beluga.bvpsol import Solution
import numpy as np

tol = 1e-3

def test_Shooting_1():
    # Full 2PBVP test problem
    # This is the simplest BVP

    def odefun(t, X, p, const, arc):
        return (X[1], -abs(X[0]))

    def bcfun(t0, X0, q0, tf, Xf, qf, p, aux):
        return (X0[0], Xf[0]+2)

    algo = Shooting()
    solinit = Solution()
    solinit.t = np.linspace(0,4,2)
    solinit.y = np.array([[0,1],[0,1]])
    out = algo.solve(odefun, None, bcfun, solinit)
    assert out.y[0][0] < tol
    assert out.y[0][1] - 2.06641646 < tol
    assert out.y[-1][0] + 2 < tol
    assert out.y[-1][1] + 2.87588998 < tol
    assert out.t[-1] - 4 < tol
    assert abs(out.y[0][1] - solinit.y[0][1]) > tol
    assert abs(out.y[-1][0] - solinit.y[-1][0]) - 2 < tol

def test_Shooting_2():
    # Full 2PBVP test problem
    # This is calculating the 4th eigenvalue of Mathieu's Equation
    # This problem contains an adjustable parameter.

    def odefun(t, X, p, const, arc):
        return (X[1], -(p[0] - 2 * 5 * np.cos(2 * t)) * X[0])

    def bcfun(t0, X0, q0, tf, Xf, qf, p, aux):
        return (X0[1], Xf[1], X0[0] - 1)

    algo = Shooting()
    solinit = Solution()
    solinit.t = np.linspace(0, np.pi, 30)
    solinit.y = np.vstack((np.cos(4 * solinit.t), -4 * np.sin(4 * solinit.t))).T
    solinit.parameters = np.array([15])

    out = algo.solve(odefun, None, bcfun, solinit)
    assert abs(out.t[-1] - np.pi) < tol
    assert abs(out.y[0][0] - 1) < tol
    assert abs(out.y[0][1]) < tol
    assert abs(out.y[-1][0] - 1) < tol
    assert abs(out.y[-1][1]) < tol
    assert abs(out.parameters[0] - 17.09646175) < tol

def test_Shooting_3():
    # This problem contains a parameter, but it is not explicit in the BCs.
    # Since time is buried in the ODEs, this tests if the BVP solver calculates
    # sensitivities with respect to parameters.
    def odefun(t, X, p, const, arc):
        return 1 * p[0]

    def bcfun(t0, X0, q0, tf, Xf, qf, p, aux):
        return (X0[0] - 0, Xf[0] - 2)

    algo = Shooting()
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0], [0]])
    solinit.parameters = np.array([1])
    out = algo.solve(odefun, None, bcfun, solinit)
    assert abs(out.parameters - 2) < tol

def test_Shooting_4():
    # This problem contains a quad and tests if the bvp solver correctly
    # integrates the quadfun.

    def compute_control_reduced(t, X, params, consts):
        g = consts[0]
        lx = params[0]
        ly = params[1]
        v = X[0]
        lv = X[1]
        theta1 = 2 * np.arctan(
            (lx * v - np.sqrt(g ** 2 * lv ** 2 - 2 * g * lv * ly * v + lx ** 2 * v ** 2 + ly ** 2 * v ** 2)) / (
                        g * lv - ly * v))
        theta2 = 2 * np.arctan(
            (lx * v + np.sqrt(g ** 2 * lv ** 2 - 2 * g * lv * ly * v + lx ** 2 * v ** 2 + ly ** 2 * v ** 2)) / (
                        g * lv - ly * v))
        H1 = -g * lv * np.sin(theta1) + lx * v * np.cos(theta1) + ly * v * np.sin(theta1) + 1
        H2 = -g * lv * np.sin(theta2) + lx * v * np.cos(theta2) + ly * v * np.sin(theta2) + 1
        T = np.vstack((theta1, theta2))
        H = np.vstack((H1, H2))
        ind = np.argmin(H, axis=0)
        return T[ind][0]

    algo = Shooting()
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0], [0]])
    solinit.parameters = np.array([1])
    out = algo.solve(odefun, None, bcfun, solinit)
    assert abs(out.parameters - 2) < tol
