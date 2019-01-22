"""
"T#" test cases from https://archimede.dm.uniba.it/~bvpsolvers/testsetbvpsolvers/?page_id=27, [1]_.

References
----------
.. [1] Francesca Mazzia and Jeff R. Cash. A fortran test set for boundary value problem solvers.
    AIP Conference Proceedings. 1648(1):020009, 2015.
"""

EASY = [1]
MEDIUM = [1, 1e-1]
HARD = [1, 1e-1, 1e-2]
VHARD = [1, 1e-1, 1e-2, 1e-3]
tol = 1e-3

import pytest
from beluga.bvpsol.algorithms import Collocation
from beluga.bvpsol import Solution
import numpy as np
from scipy.special import erf

@pytest.mark.parametrize("const", HARD)
def test_T1(const):
    def odefun(X, p, const):
        return (X[1], X[0] / const[0])

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] - 1, Xf[0])

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (np.exp(-sol.t / np.sqrt(sol.const)) - np.exp((sol.t - 2) / np.sqrt(sol.const))) / (
                1 - np.exp(-2.e0 / np.sqrt(sol.const)))
    e2 = (1. / (sol.const ** (1 / 2) * np.exp(sol.t / sol.const ** (1 / 2))) + np.exp(
        (sol.t - 2) / sol.const ** (1 / 2)) / sol.const ** (1 / 2)) / (1 / np.exp(2 / sol.const ** (1 / 2)) - 1)
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", MEDIUM)
def test_T2(const):
    def odefun(X, p, const):
        return (X[1], X[1] / const[0])

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] - 1, Xf[0])

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.const)) / (1.e0 - np.exp(-1.e0 / sol.const))
    e2 = np.exp((sol.t - 1) / sol.const) / (sol.const * (1 / np.exp(1 / sol.const) - 1))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", HARD)
def test_T3(const):
    def odefun(X, p, const):
        return (2 * X[1], 2 * (-(2 + np.cos(np.pi * X[2])) * X[1] + X[0] - (1 + const[0] * np.pi * np.pi) * np.cos(
            np.pi * X[2]) - (2 + np.cos(np.pi * X[2])) * np.pi * np.sin(np.pi * X[2])) / const[0], 2)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] + 1, Xf[0] + 1, X0[2] + 1)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", EASY)
def test_T4(const):
    def odefun(X, p, const):
        return (2 * X[1], 2 * (((1 + const[0]) * X[0] - X[1]) / const[0]), 2)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] - 1 - np.exp(-2), Xf[0] - 1 - np.exp(-2 * (1 + const[0]) / const[0]), X0[2] + 1)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.exp(sol.y[:, 2] - 1) + np.exp(-((1 + sol.const[0]) * (1 + sol.y[:, 2]) / sol.const[0]))
    e2 = np.exp(sol.y[:, 2] - 1) - (sol.const[0] + 1) / (
                sol.const[0] * np.exp((sol.y[:, 2] + 1) * (sol.const[0] + 1) / sol.const[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", VHARD)
def test_T5(const):
    def odefun(X, p, const):
        return (2 * X[1], 2 * ((X[0] + X[2] * X[1] - (1 + const[0] * np.pi ** 2) * np.cos(np.pi * X[2]) + X[2] * np.pi * np.sin(np.pi * X[2])) / const[0]), 2)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] + 1, Xf[0] + 1, X0[2] + 1)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

def test_T6():
    # This is a "special" case not using the difficulty settings above.
    def odefun(X, p, const):
        return (2 * X[1], 2 * ((-X[2] * X[1] - const[0] * np.pi ** 2 * np.cos(np.pi * X[2]) - np.pi * X[2] * np.sin(
            np.pi * X[2])) / const[0]), 2)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] + 2, Xf[0], X0[2] + 1)

    algo = Collocation(odefun, None, bcfun, number_of_nodes=200)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([1])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2]) + erf(sol.y[:, 2] / np.sqrt(2 * sol.const[0])) / erf(1 / np.sqrt(2 * sol.const[0]))
    e2 = np.sqrt(2) / (np.sqrt(np.pi) * np.sqrt(sol.const[0]) * np.exp(sol.y[:, 2] ** 2 / (2 * sol.const[0])) * erf(
        np.sqrt(2) / (2 * np.sqrt(sol.const[0])))) - np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", VHARD)
def test_T7(const):
    def odefun(X, p, const):
        return (2 * X[1], 2 * ((-X[2] * X[1] + X[0] - (1.0e0 + const[0] * np.pi ** 2) * np.cos(np.pi * X[2]) - np.pi *
                                X[2] * np.sin(np.pi * X[2])) / const[0]), 2)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] + 1, Xf[0] - 1, X0[2] + 1)

    algo = Collocation(odefun, None, bcfun, number_of_nodes=70)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2]) + sol.y[:, 2] + (
                sol.y[:, 2] * erf(sol.y[:, 2] / np.sqrt(2.0e0 * sol.const[0])) + np.sqrt(
            2 * sol.const[0] / np.pi) * np.exp(-sol.y[:, 2] ** 2 / (2 * sol.const[0]))) / (
                     erf(1.0e0 / np.sqrt(2 * sol.const[0])) + np.sqrt(2.0e0 * sol.const[0] / np.pi) * np.exp(
                 -1 / (2 * sol.const[0])))
    e2 = erf((np.sqrt(2) * sol.y[:, 2]) / (2 * np.sqrt(sol.const[0]))) / (
                erf(np.sqrt(2) / (2 * np.sqrt(sol.const[0]))) + (np.sqrt(2) * np.sqrt(sol.const[0])) / (
                    np.sqrt(np.pi) * np.exp(1 / (2 * sol.const[0])))) - np.pi * np.sin(np.pi * sol.y[:, 2]) + 1
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", MEDIUM)
def test_T8(const):
    def odefun(X, p, const):
        return (X[1], (-X[1] / const[0]), 1)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] - 1, Xf[0] - 2, X0[2])

    algo = Collocation(odefun, None, bcfun, number_of_nodes=300)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1, 0, -1], [2, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (2 - np.exp(-1 / sol.const[0]) - np.exp(-sol.y[:, 2] / sol.const[0])) / (1 - np.exp(-1 / sol.const[0]))
    e2 = -1 / (sol.const[0] * np.exp(sol.y[:, 2] / sol.const[0]) * (1 / np.exp(1 / sol.const[0]) - 1))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

@pytest.mark.parametrize("const", HARD)
def test_T9(const):
    def odefun(X, p, const):
        return (2 * X[1], 2 * (-(4 * X[2] * X[1] + 2 * X[0]) / (const[0] + X[2] ** 2)), 2)

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0] - 1 / (1 + const[0]), Xf[0] - 1 / (1 + const[0]), X0[2] + 1)

    algo = Collocation(odefun, None, bcfun, number_of_nodes=300)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1 / (1 + const), 0, -1], [1 / (1 + const), 1, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = 1 / (sol.const[0] + sol.y[:, 2] ** 2)
    e2 = -(2 * sol.y[:, 2]) / (sol.y[:, 2] ** 2 + sol.const[0]) ** 2
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)

def test_Collocation_1():
    # Full 2PBVP test problem
    # This is the simplest BVP

    def odefun(X, p, const):
        return (X[1], -abs(X[0]))

    def bcfun(X0, q0, Xf, qf, p, ndp, const):
        return (X0[0], Xf[0]+2)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0,4,4)
    solinit.y = np.array([[0,1],[0,1],[0,1],[0,1]])
    solinit.const = np.array([])
    out = algo.solve(solinit)
    assert out.y[0][0] < tol
    assert out.y[0][1] - 2.06641646 < tol
    assert out.y[-1][0] + 2 < tol
    assert out.y[-1][1] + 2.87588998 < tol
    assert out.t[-1] - 4 < tol
    assert abs(out.y[0][1] - solinit.y[0][1]) > tol
    assert abs(out.y[-1][0] - solinit.y[-1][0]) - 2 < tol

# def test_Collocation_2():
#     # Full 2PBVP test problem
#     # This is calculating the 4th eigenvalue of Mathieu's Equation
#     # This problem contains an adjustable parameter.
#
#     def odefun(X, p, const):
#         return (p[0]*X[1], p[0]*(-(p[1] - 2 * 5 * np.cos(2 * X[2])) * X[0]), 0)
#
#     def bcfun(X0, q0, Xf, qf, p, ndp, const):
#         return (X0[1], Xf[1], X0[0] - 1, X0[2], Xf[2]-np.pi)
#
#     algo = Collocation(odefun, None, bcfun)
#     solinit = Solution()
#     solinit.t = np.linspace(0, np.pi, 30)
#     solinit.y = np.vstack((np.cos(4 * solinit.t), -4 * np.sin(4 * solinit.t), solinit.t)).T
#     solinit.dynamical_parameters = np.array([np.pi, 15])
#     solinit.const = np.array([])
#
#     out = algo.solve(solinit)
#     assert abs(out.y[-1][2] - np.pi) < tol
#     assert abs(out.y[0][0] - 1) < tol
#     assert abs(out.y[0][1]) < tol
#     assert abs(out.y[-1][0] - 1) < tol
#     assert abs(out.y[-1][1]) < tol
#     assert abs(out.dynamical_parameters[0] - 17.098740587333868) < tol

def test_Collocation_3():
    # This problem contains a parameter, but it is not explicit in the BCs.
    # Since time is buried in the ODEs, this tests if the BVP solver calculates
    # sensitivities with respect to parameters.
    def odefun(X, p, const):
        return 1 * p[0]

    def bcfun(X0, q0, Xf, qf, p, ndp, aux):
        return (X0[0] - 0, Xf[0] - 2)

    algo = Collocation(odefun, None, bcfun)
    solinit = Solution()
    solinit.t = np.linspace(0, 1, 4)
    solinit.y = np.array([[0], [0], [0], [0]])
    solinit.dynamical_parameters = np.array([1])
    solinit.const = np.array([])
    out = algo.solve(solinit)
    assert abs(out.dynamical_parameters - 2) < tol
