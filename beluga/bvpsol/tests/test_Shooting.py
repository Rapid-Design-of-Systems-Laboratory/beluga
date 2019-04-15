"""
"T#" test cases from https://archimede.dm.uniba.it/~bvpsolvers/testsetbvpsolvers/?page_id=27, [1]_.

References
----------
.. [1] Francesca Mazzia and Jeff R. Cash. "A fortran test set for boundary value problem solvers."
    AIP Conference Proceedings. 1648(1):020009, 2015.
"""

import pytest
import itertools
from beluga.ivpsol import Trajectory
from beluga.bvpsol import Shooting
import numpy as np
import copy
from scipy.special import erf

# Test the shooting solver for each algorithm listed below
ALGORITHMS = ['Armijo', 'SLSQP']
EASY = [1]
MEDIUM = [1e-1]
HARD = [1e-2]
VHARD = [1e-3]
tol = 1e-3


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T1(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], X[0] / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
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


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T2(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], X[1] / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.const)) / (1.e0 - np.exp(-1.e0 / sol.const))
    e2 = np.exp((sol.t - 1) / sol.const) / (sol.const * (1 / np.exp(1 / sol.const) - 1))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T3(algorithm, const):
    def odefun(X, u, p, const):
        return (2 * X[1], 2 * (-(2 + np.cos(np.pi * X[2])) * X[1] + X[0] - (1 + const[0] * np.pi * np.pi) * np.cos(
            np.pi * X[2]) - (2 + np.cos(np.pi * X[2])) * np.pi * np.sin(np.pi * X[2])) / const[0], 2)

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1, Xf[0] + 1, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T4(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1], 2 * (((1 + const[0]) * X[0] - X[1]) / const[0]), 2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1 - np.exp(-2), Xf[0] - 1 - np.exp(-2 * (1 + const[0]) / const[0]), X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.exp(sol.y[:, 2] - 1) + np.exp(-((1 + sol.const[0]) * (1 + sol.y[:, 2]) / sol.const[0]))
    e2 = np.exp(sol.y[:, 2] - 1) - (sol.const[0] + 1) / (
                sol.const[0] * np.exp((sol.y[:, 2] + 1) * (sol.const[0] + 1) / sol.const[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T5(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1],\
               2 * ((X[0] + X[2] * X[1] - (1 + const[0] * np.pi ** 2) * np.cos(np.pi * X[2]) + X[2] * np.pi
                     * np.sin(np.pi * X[2])) / const[0]),\
               2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1, Xf[0] + 1, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T6(algorithm, const):
    def odefun(X, u, p, const):
        return (2 * X[1], 2 * ((-X[2] * X[1] - const[0] * np.pi ** 2 * np.cos(np.pi * X[2]) - np.pi * X[2] * np.sin(
            np.pi * X[2])) / const[0]), 2)

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 2, Xf[0], X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2]) + erf(sol.y[:, 2] / np.sqrt(2 * sol.const[0])) / erf(1 / np.sqrt(2 * sol.const[0]))
    e2 = np.sqrt(2) / (np.sqrt(np.pi) * np.sqrt(sol.const[0]) * np.exp(sol.y[:, 2] ** 2 / (2 * sol.const[0])) * erf(
        np.sqrt(2) / (2 * np.sqrt(sol.const[0])))) - np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T7(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1], 2 * ((-X[2] * X[1] + X[0] - (1.0e0 + const[0] * np.pi ** 2) * np.cos(np.pi * X[2]) - np.pi *
                               X[2] * np.sin(np.pi * X[2])) / const[0]), 2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1, Xf[0] - 1, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2]) + sol.y[:, 2] + (
                sol.y[:, 2] * erf(sol.y[:, 2] / np.sqrt(2.0e0 * sol.const[0]))
                + np.sqrt(2 * sol.const[0] / np.pi) * np.exp(-sol.y[:, 2] ** 2 / (2 * sol.const[0]))) / (
                     erf(1.0e0 / np.sqrt(2 * sol.const[0])) + np.sqrt(2.0e0 * sol.const[0] / np.pi)
                     * np.exp(-1 / (2 * sol.const[0])))
    e2 = erf((np.sqrt(2) * sol.y[:, 2]) / (2 * np.sqrt(sol.const[0]))) / (
                erf(np.sqrt(2) / (2 * np.sqrt(sol.const[0]))) + (np.sqrt(2) * np.sqrt(sol.const[0])) / (
                    np.sqrt(np.pi) * np.exp(1 / (2 * sol.const[0])))) - np.pi * np.sin(np.pi * sol.y[:, 2]) + 1
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T8(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (-X[1] / const[0]), 1

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] - 2, X0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1, 0, -1], [2, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (2 - np.exp(-1 / sol.const[0]) - np.exp(-sol.y[:, 2] / sol.const[0])) / (1 - np.exp(-1 / sol.const[0]))
    e2 = -1 / (sol.const[0] * np.exp(sol.y[:, 2] / sol.const[0]) * (1 / np.exp(1 / sol.const[0]) - 1))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T9(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1], 2 * (-(4 * X[2] * X[1] + 2 * X[0]) / (const[0] + X[2] ** 2)), 2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1 / (1 + const[0]), Xf[0] - 1 / (1 + const[0]), X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1 / (1 + const), 0, -1], [1 / (1 + const), 1, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = 1 / (sol.const[0] + sol.y[:, 2] ** 2)
    e2 = -(2 * sol.y[:, 2]) / (sol.y[:, 2] ** 2 + sol.const[0]) ** 2
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T10(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1], 2 * (-X[2] * X[1] / const[0]), 2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0] - 2, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, -1], [2, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = 1 + erf(sol.y[:, 2] / np.sqrt(2 * sol.const[0])) / erf(1 / np.sqrt(2 * sol.const[0]))
    e2 = np.sqrt(2) / (np.sqrt(np.pi) * np.sqrt(sol.const[0]) * np.exp(sol.y[:, 2] ** 2 / (2 * sol.const[0])) * erf(
        np.sqrt(2) / (2 * np.sqrt(sol.const[0]))))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T11(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1],\
               2 * ((X[0] - const[0] * np.pi ** 2 * np.cos(np.pi * X[2]) - np.cos(np.pi * X[2])) / const[0]),\
               2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1, Xf[0] + 1, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T12(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1],\
               2 * ((X[0] - const[0] * np.pi ** 2 * np.cos(np.pi * X[2]) - np.cos(np.pi * X[2])) / const[0]),\
               2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1, Xf[0], X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2]) + np.exp(-(1 - sol.y[:, 2]) / np.sqrt(sol.const[0]))
    e2 = np.exp((sol.y[:, 2] - 1) / np.sqrt(sol.const[0])) / np.sqrt(sol.const[0]) - np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T13(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1],\
               2 * ((X[0] - const[0] * np.pi ** 2 * np.cos(np.pi * X[2]) - np.cos(np.pi * X[2])) / const[0]),\
               2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0] + 1, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, -1], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.cos(np.pi * sol.y[:, 2]) + np.exp(-(1 + sol.y[:, 2]) / np.sqrt(sol.const[0]))
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2]) - 1 / (
                np.sqrt(sol.const[0]) * np.exp((sol.y[:, 2] + 1) / np.sqrt(sol.const[0])))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T14(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1],\
               2 * ((X[0] - const[0] * np.pi ** 2 * np.cos(np.pi * X[2]) - np.cos(np.pi * X[2])) / const[0]),\
               2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0], X0[2]+1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0, -1], [0, 0, 1]])
    sol.const = np.array([const])
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    e1 = np.cos(np.pi * sol.y[:, 2]) + np.exp(-(1 + sol.y[:, 2]) / np.sqrt(sol.const[0])) + np.exp(
        -(1 - sol.y[:, 2]) / np.sqrt(sol.const[0]))
    e2 = np.exp((sol.y[:, 2] - 1) / np.sqrt(sol.const[0])) / np.sqrt(sol.const[0]) - np.pi * np.sin(
        np.pi * sol.y[:, 2]) - 1 / (np.sqrt(sol.const[0]) * np.exp((sol.y[:, 2] + 1) / np.sqrt(sol.const[0])))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T15(algorithm, const):
    def odefun(X, u, p, const):
        return 2 * X[1], 2 * (X[2] * X[0] / const[0]), 2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] - 1, X0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1, 0, -1], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    assert sol.converged is True


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T16(algorithm, const):
    def odefun(X, u, p, const):
        return 1 * X[1], 1 * (-X[0] * np.pi ** 2 / (4 * const[0])), 1

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0] - np.sin(np.pi / (2 * np.sqrt(const[0]))), X0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.sin(np.pi * sol.y[:, 2] / (2 * np.sqrt(sol.const[0])))
    e2 = (np.pi * np.cos((np.pi * sol.y[:, 2]) / (2 * np.sqrt(sol.const[0])))) / (2 * np.sqrt(sol.const[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T17(algorithm, const):
    def odefun(X, u, p, const):
        return 0.2 * X[1], 0.2 * (-3 * const[0] * X[0] / (const[0] + X[2] ** 2) ** 2), 0.2

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 0.1 / np.sqrt(const[0] + 0.01), Xf[0] - 0.1 / np.sqrt(const[0] + 0.01), X0[2] + 0.1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = sol.y[:, 2]/np.sqrt(sol.const[0]+sol.y[:, 2]**2)
    e2 = 1/np.sqrt(sol.y[:, 2]**2 + sol.const[0]) - sol.y[:, 2]**2/(sol.y[:, 2]**2 + sol.const[0])**(3/2)
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T18(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (-X[1] / const[0]), 1

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] - np.exp(-1 / const[0]), X0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.exp(-sol.y[:, 2] / sol.const[0])
    e2 = -1 / (sol.const[0] * np.exp(sol.y[:, 2] / sol.const[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T19(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (-X[1] / const[0]), 1

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0], X0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T21(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (X[0] * (1 + X[0]) - np.exp(-2 * X[2] / np.sqrt(const[0]))) / const[0], 1

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] - np.exp(-1 / np.sqrt(const[0])), X0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.exp(-sol.y[:, 2] / np.sqrt(const))
    e2 = -np.exp(-sol.y[:, 2] / np.sqrt(const)) / np.sqrt(const)
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T22(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], -(X[1] + X[0] * X[0]) / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0] - 1 / 2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0], [0, 0]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, MEDIUM))
def test_T23(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], -(X[1] + X[0] * X[0]) / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0] - 1 / 2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0], [0, 0]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T24(algorithm, const):
    def odefun(X, u, p, const=None):
        Ax = 1 + X[2] ** 2
        Apx = 2 * X[2]
        y = 1.4
        return (X[1], (((1 + y) / 2 - const[0] * Apx) * X[0] * X[1] - X[1] / X[0] - (Apx / Ax) * (
                    1 - (y - 1) / 2 * X[0] ** 2)) / (const[0] * Ax * X[0]), 1)

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const=None):
        return X0[0] - 0.9129, Xf[0] - 0.375, X0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 1, 0], [0.1, 0.1, 1]])
    sol.const = np.array([const])
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T25(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], X[0] * (1 - X[1]) / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1 / 3, Xf[0] - 1 / 3

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=16)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[-1/3, 1], [1/3, 1]])
    sol.const = np.array([const])
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T26(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], X[0] * (1 - X[1]) / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] + 1/3

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=64)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 0], [-1/3, 0]])
    sol.const = np.array([const])
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T27(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], X[0] * (1 - X[1]) / const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] - 1 / 3

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 0], [1 / 3, 0]])
    sol.const = np.array([const])
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T28(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (X[0] - X[0]*X[1])/const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 1, Xf[0] - 3/2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=1)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 0], [3/2, 0]])
    sol.const = np.array([const])
    sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T29(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (X[0] - X[0]*X[1])/const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0] - 3/2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=1)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0], [3/2, 0]])
    sol.const = np.array([const])
    sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T30(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (X[0] - X[0]*X[1])/const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 7/6, Xf[0] - 3/2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=8)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[-7/6, 0], [3/2, 0]])
    sol.const = np.array([const])
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, HARD))
def test_T31(algorithm, const):
    def odefun(X, u, p, const):
        return np.sin(X[1]), X[2], -X[3]/const[0],\
               ((X[0]-1)*np.cos(X[1]) - X[2]/np.cos(X[1]) - const[0]*X[3]*np.tan(X[1]))/const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], X0[2], Xf[0], Xf[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=12)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0, 0, 0], [0, 0, 0, 0]])
    sol.const = np.array([const])
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T32(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], X[2], X[3], (X[1]*X[2] - X[0]*X[3])/const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], X0[1], Xf[0] - 1, Xf[1]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0, 0, 0], [1, 0, 0, 0]])
    sol.const = np.array([const])
    sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("algorithm, const", itertools.product(ALGORITHMS, VHARD))
def test_T33(algorithm, const):
    def odefun(X, u, p, const):
        return X[1], (X[0]*X[3] - X[2]*X[1])/const[0], X[3], X[4], X[5], (-X[2]*X[5] - X[0]*X[1])/const[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] + 1, X0[2], X0[3], Xf[0] - 1, Xf[2], Xf[3]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=12)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[-1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
    sol.const = np.array([const])
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.const = np.array([c])
        sol = algo.solve(sol)

    assert sol.converged


@pytest.mark.parametrize("const", MEDIUM)
def test_R2(const):
    def odefun(X, u, p, const):
        return X[0] / const[0]

    def quadfun(X, u, p, const):
        return X[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return q0[0] - 1, qf[0]

    algo = Shooting(odefun, quadfun, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1], [1]])
    solinit.q = np.array([[0], [0]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.const)) / (1.e0 - np.exp(-1.e0 / sol.const))
    e2 = np.exp((sol.t - 1) / sol.const) / (sol.const * (1 / np.exp(1 / sol.const) - 1))
    assert all(e1 - sol.q[:, 0] < tol)
    assert all(e2 - sol.y[:, 0] < tol)


@pytest.mark.parametrize("const", MEDIUM)
def test_R8(const):
    def odefun(X, u, p, const):
        return -X[0] / const[0]

    def quadfun(X, u, p, const):
        return X[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return q0[0] - 1, qf[0] - 2

    algo = Shooting(odefun, quadfun, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1], [1]])
    solinit.q = np.array([[0], [0]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.const)) / (1.e0 - np.exp(-1.e0 / sol.const))
    e2 = np.exp((sol.t - 1) / sol.const) / (sol.const * (1 / np.exp(1 / sol.const) - 1))
    assert all(e1 - sol.q[:, 0] < tol)
    assert all(e2 - sol.y[:, 0] < tol)


@pytest.mark.parametrize("const", MEDIUM)
def test_R18(const):
    def odefun(X, u, p, const):
        return -X[0] / const[0]

    def quadfun(X, u, p, const):
        return X[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return q0[0] - 1, qf[0] - np.exp(-1 / const[0])

    algo = Shooting(odefun, quadfun, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1], [1]])
    solinit.q = np.array([[0], [0]])
    solinit.const = np.array([const])
    sol = algo.solve(solinit)

    e1 = np.exp(-sol.t / sol.const[0])
    e2 = -1 / (sol.const[0] * np.exp(sol.t / sol.const[0]))
    assert all(e1 - sol.q[:, 0] < tol)
    assert all(e2 - sol.y[:, 0] < tol)


def test_Shooting_1():
    # Full 2PBVP test problem
    # This is the simplest BVP

    def odefun(X, u, p, const):
        return X[1], -abs(X[0])

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0], Xf[0]+2

    algo = Shooting(odefun, None, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 4, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.const = np.array([])
    out = algo.solve(solinit)
    assert out.y[0][0] < tol
    assert out.y[0][1] - 2.06641646 < tol
    assert out.y[-1][0] + 2 < tol
    assert out.y[-1][1] + 2.87588998 < tol
    assert out.t[-1] - 4 < tol
    assert abs(out.y[0][1] - solinit.y[0][1]) > tol
    assert abs(out.y[-1][0] - solinit.y[-1][0]) - 2 < tol


# def test_Shooting_2():
#     # Full 2PBVP test problem
#     # This is calculating the 4th eigenvalue of Mathieu's Equation
#     # This problem contains an adjustable parameter.
#
#     def odefun(X, p, const):
#         return (X[1], -(p[0] - 2 * 5 * np.cos(2 * t)) * X[0])
#
#     def bcfun(X0, q0, Xf, qf, p, ndp, const):
#         return (X0[1], Xf[1], X0[0] - 1)
#
#     algo = Shooting(odefun, None, bcfun)
#     solinit = Trajectory()
#     solinit.t = np.linspace(0, np.pi, 30)
#     solinit.y = np.vstack((np.cos(4 * solinit.t), -4 * np.sin(4 * solinit.t))).T
#     solinit.dynamical_parameters = np.array([15])
#     solinit.const = np.array([])
#
#     out = algo.solve(solinit)
#     assert abs(out.t[-1] - np.pi) < tol
#     assert abs(out.y[0][0] - 1) < tol
#     assert abs(out.y[0][1]) < tol
#     assert abs(out.y[-1][0] - 1) < tol
#     assert abs(out.y[-1][1]) < tol
#     assert abs(out.dynamical_parameters[0] - 17.09646175) < tol


def test_Shooting_3():
    # This problem contains a parameter, but it is not explicit in the BCs.
    # Since time is buried in the ODEs, this tests if the BVP solver calculates
    # sensitivities with respect to parameters.
    def odefun(X, u, p, const):
        return 1 * p[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
        return X0[0] - 0, Xf[0] - 2

    algo = Shooting(odefun, None, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0], [0]])
    solinit.dynamical_parameters = np.array([1])
    solinit.const = np.array([])
    out = algo.solve(solinit)
    assert abs(out.dynamical_parameters - 2) < tol


def test_Shooting_4():
    # This problem contains a quad and tests if the bvp solver correctly
    # integrates the quadfun. Also tests multiple shooting.

    def odefun(x, u, p, const):
        return -x[1], x[0]

    def quadfun(x, u, p, const):
        return x[0]

    def bcfun(X0, q0, u0, Xf, qf, uf, params, ndp, const):
        return X0[0], X0[1] - 1, qf[0] - 1.0

    algo = Shooting(odefun, quadfun, bcfun, num_arcs=4)
    solinit = Trajectory()
    solinit.t = np.linspace(0, np.pi / 2, 2)
    solinit.y = np.array([[1, 0], [1, 0]])
    solinit.q = np.array([[0], [0]])
    solinit.const = np.array([])
    out = algo.solve(solinit)
    assert (out.y[0, 0] - 0) < tol
    assert (out.y[0, 1] - 1) < tol
    assert (out.q[0, 0] - 2) < tol
    assert (out.q[-1, 0] - 1) < tol
