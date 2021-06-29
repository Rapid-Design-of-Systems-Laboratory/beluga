"""
"T#" test cases from https://archimede.dm.uniba.it/~bvpsolvers/testsetbvpsolvers/?page_id=27, [1]_.
"R#" test cases from https://doi.org/10.2514/6.2019-3666, [2]_.

References
----------
.. [1] Francesca Mazzia and Jeff R. Cash. "A fortran test set for boundary value problem solvers."
    AIP Conference Proceedings. 1648(1):020009, 2015.

.. [2] Michael J Sparapany and Michael J Grant. "Numerical Algorithms for Solving Boundary-Value Problemson Reduced
    Dimensional Manifolds." AIAA Aviation 2019 Forum. 2019.
"""

import copy
import itertools

import numpy as np
import pytest
from beluga.numeric.data_classes.Trajectory import Trajectory
from scipy.special import erf

from beluga.solvers.bvp_solvers import Shooting

# Test the shooting solver for each algorithm listed below
ALGORITHMS = ['Armijo', 'SLSQP']
EASY = [1]
MEDIUM = [1e-1]
HARD = [1e-2]
VHARD = [1e-3]
tol = 1e-3


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t1(algorithm, const):
    def odefun(y, _, k):
        return y[1], y[0] / k[0]

    def odejac(_, __, k):
        df_dy = np.array([[0, 1], [1 / k[0], 0]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = (np.exp(-sol.t / np.sqrt(sol.k)) - np.exp((sol.t - 2) / np.sqrt(sol.k))) / (
                1 - np.exp(-2.e0 / np.sqrt(sol.k)))
    e2 = (1. / (sol.k ** (1 / 2) * np.exp(sol.t / sol.k ** (1 / 2))) + np.exp(
            (sol.t - 2) / sol.k ** (1 / 2)) / sol.k ** (1 / 2)) / (1 / np.exp(2 / sol.k ** (1 / 2)) - 1)
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t2(algorithm, const):
    def odefun(y, _, k):
        return y[1], y[1] / k[0]

    def odejac(_, __, k):
        df_dy = np.array([[0, 1], [0, 1 / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.k)) / (1.e0 - np.exp(-1.e0 / sol.k))
    e2 = np.exp((sol.t - 1) / sol.k) / (sol.k * (1 / np.exp(1 / sol.k) - 1))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t3(algorithm, const):
    def odefun(y, _, k):
        return (2 * y[1], 2 * (-(2 + np.cos(np.pi * y[2])) * y[1] + y[0] - (1 + k[0] * np.pi * np.pi) * np.cos(
            np.pi * y[2]) - (2 + np.cos(np.pi * y[2])) * np.pi * np.sin(np.pi * y[2])) / k[0], 2)

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [2 / k[0], -(2 * np.cos(np.pi * y[2]) + 4)/k[0],
                           (2*np.pi**2 * np.sin(np.pi * y[2])**2 + 2 * np.pi*np.sin(np.pi*y[2])*(k[0]*np.pi**2 + 1)
                            - 2*np.pi**2*np.cos(np.pi*y[2])*(np.cos(np.pi*y[2]) + 2)
                            + 2*y[1]*np.pi*np.sin(np.pi*y[2]))/k[0]],
                          [0, 0, 0]], dtype=np.float)
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1, yf[0] + 1, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t4(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * (((1 + k[0]) * y[0] - y[1]) / k[0]), 2

    def odejac(_, __, k):
        df_dy = np.array([[0, 2, 0], [2 * (1 + k[0]) / k[0], 2 * (-1) / k[0], 0], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, k):
        return y0[0] - 1 - np.exp(-2), yf[0] - 1 - np.exp(-2 * (1 + k[0]) / k[0]), y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.exp(sol.y[:, 2] - 1) + np.exp(-((1 + sol.k[0]) * (1 + sol.y[:, 2]) / sol.k[0]))
    e2 = np.exp(sol.y[:, 2] - 1) - (sol.k[0] + 1) / (
            sol.k[0] * np.exp((sol.y[:, 2] + 1) * (sol.k[0] + 1) / sol.k[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t5(algorithm, const):
    def odefun(y, _, k):
        return (2 * y[1], 2 * ((y[0] + y[2] * y[1] - (1 + k[0] * np.pi ** 2) * np.cos(np.pi * y[2])
                                + y[2] * np.pi * np.sin(np.pi * y[2])) / k[0]), 2)

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0], [2 / k[0], 2 * y[2] / k[0],
                                      (2 * (y[1] + np.pi * np.sin(np.pi * y[2]) + np.pi * np.sin(np.pi * y[2])
                                            * (k * np.pi ** 2 + 1) + np.pi * np.pi * y[2]
                                            * np.cos(np.pi * y[2]))) / k[0]], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1, yf[0] + 1, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t6(algorithm, const):
    def odefun(y, _, k):
        return (2 * y[1], 2 * ((-y[2] * y[1] - k[0] * np.pi ** 2 * np.cos(np.pi * y[2]) - np.pi * y[2] * np.sin(
            np.pi * y[2])) / k[0]), 2)

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [0, -2 * y[2] / k[0],
                           -(2 * (y[1] + np.pi * np.sin(np.pi * y[2]) - k[0] * np.pi ** 3 * np.sin(np.pi * y[2])
                                  + np.pi ** 2 * y[2] * np.cos(np.pi * y[2]))) / k[0]], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 2, yf[0], y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2]) + erf(sol.y[:, 2] / np.sqrt(2 * sol.k[0])) / erf(1 / np.sqrt(2 * sol.k[0]))
    e2 = np.sqrt(2) / (np.sqrt(np.pi) * np.sqrt(sol.k[0]) * np.exp(sol.y[:, 2] ** 2 / (2 * sol.k[0])) * erf(
        np.sqrt(2) / (2 * np.sqrt(sol.k[0])))) - np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t7(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * ((-y[2] * y[1] + y[0] - (1.0e0 + k[0] * np.pi ** 2) * np.cos(np.pi * y[2]) - np.pi *
                               y[2] * np.sin(np.pi * y[2])) / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [2 / k[0], -2 * y[2] / k[0],
                           -(2 * (y[1] + np.pi * np.sin(np.pi * y[2]) + np.pi ** 2 * y[2] * np.cos(np.pi * y[2])
                                  - np.pi * np.sin(np.pi * y[2]) * (k[0] * np.pi ** 2 + 1))) / k[0]],
                          [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1, yf[0] - 1, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [1, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2]) + sol.y[:, 2] + (
                sol.y[:, 2] * erf(sol.y[:, 2] / np.sqrt(2.0e0 * sol.k[0]))
                + np.sqrt(2 * sol.k[0] / np.pi) * np.exp(-sol.y[:, 2] ** 2 / (2 * sol.k[0]))) / (
                 erf(1.0e0 / np.sqrt(2 * sol.k[0])) + np.sqrt(2.0e0 * sol.k[0] / np.pi)
                 * np.exp(-1 / (2 * sol.k[0])))
    e2 = erf((np.sqrt(2) * sol.y[:, 2]) / (2 * np.sqrt(sol.k[0]))) / (
            erf(np.sqrt(2) / (2 * np.sqrt(sol.k[0]))) + (np.sqrt(2) * np.sqrt(sol.k[0])) / (
                    np.sqrt(np.pi) * np.exp(1 / (2 * sol.k[0])))) - np.pi * np.sin(np.pi * sol.y[:, 2]) + 1
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t8(algorithm, const):
    def odefun(y, _, k):
        return y[1], (-y[1] / k[0]), 1

    def odejac(_, __, k):
        df_dy = np.array([[0, 1, 0], [0, -1 / k[0], 0], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0] - 2, y0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1, 0, -1], [2, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = (2 - np.exp(-1 / sol.k[0]) - np.exp(-sol.y[:, 2] / sol.k[0])) / (1 - np.exp(-1 / sol.k[0]))
    e2 = -1 / (sol.k[0] * np.exp(sol.y[:, 2] / sol.k[0]) * (1 / np.exp(1 / sol.k[0]) - 1))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t9(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * (-(4 * y[2] * y[1] + 2 * y[0]) / (k[0] + y[2] ** 2)), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [-4 / (y[2] ** 2 + k[0]), -(8 * y[2]) / (y[2] ** 2 + k[0]),
                           (4 * y[2] * (2 * y[0] + 4 * y[1] * y[2])) / (y[2] ** 2 + k[0]) ** 2
                           - (8 * y[1]) / (y[2] ** 2 + k[0])], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, k):
        return y0[0] - 1 / (1 + k[0]), yf[0] - 1 / (1 + k[0]), y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=2)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0., 1., 2)
    # noinspection PyTypeChecker
    solinit.y = np.array([[1. / (1. + const), 0., -1.], [1. / (1. + const), 1., 1.]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = 1 / (sol.k[0] + sol.y[:, 2] ** 2)
    e2 = -(2 * sol.y[:, 2]) / (sol.y[:, 2] ** 2 + sol.k[0]) ** 2
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t10(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * (-y[2] * y[1] / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0], [0, 2 * (-y[2]) / k[0], 2 * (-y[1] / k[0])], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0] - 2, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, -1], [2, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = 1 + erf(sol.y[:, 2] / np.sqrt(2 * sol.k[0])) / erf(1 / np.sqrt(2 * sol.k[0]))
    e2 = np.sqrt(2) / (np.sqrt(np.pi) * np.sqrt(sol.k[0]) * np.exp(sol.y[:, 2] ** 2 / (2 * sol.k[0])) * erf(
        np.sqrt(2) / (2 * np.sqrt(sol.k[0]))))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t11(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * ((y[0] - k[0] * np.pi ** 2 * np.cos(np.pi * y[2]) - np.cos(np.pi * y[2])) / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [2 / k[0], 0, (2 * (np.pi * np.sin(np.pi * y[2])
                                              + k[0] * np.pi ** 3 * np.sin(np.pi * y[2]))) / k[0]], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1, yf[0] + 1, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [-1, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2])
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t12(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * ((y[0] - k[0] * np.pi ** 2 * np.cos(np.pi * y[2]) - np.cos(np.pi * y[2])) / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [2 / k[0], 0, (2 * (np.pi * np.sin(np.pi * y[2]) + k[0] * np.pi ** 3 * np.sin(np.pi * y[2])))
                           / k[0]], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1, yf[0], y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[-1, 0, -1], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2]) + np.exp(-(1 - sol.y[:, 2]) / np.sqrt(sol.k[0]))
    e2 = np.exp((sol.y[:, 2] - 1) / np.sqrt(sol.k[0])) / np.sqrt(sol.k[0]) - np.pi * np.sin(np.pi * sol.y[:, 2])
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t13(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * ((y[0] - k[0] * np.pi ** 2 * np.cos(np.pi * y[2]) - np.cos(np.pi * y[2])) / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [2 / k[0], 0, (2 * (np.pi * np.sin(np.pi * y[2]) + k[0] * np.pi ** 3 * np.sin(np.pi * y[2])))
                           / k[0]], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0] + 1, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=2)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, -1], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2]) + np.exp(-(1 + sol.y[:, 2]) / np.sqrt(sol.k[0]))
    e2 = -np.pi * np.sin(np.pi * sol.y[:, 2]) - 1 / (
            np.sqrt(sol.k[0]) * np.exp((sol.y[:, 2] + 1) / np.sqrt(sol.k[0])))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t14(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * ((y[0] - k[0] * np.pi ** 2 * np.cos(np.pi * y[2]) - np.cos(np.pi * y[2])) / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0],
                          [2 / k[0], 0, (2 * (np.pi * np.sin(np.pi * y[2]) + k[0] * np.pi ** 3 * np.sin(np.pi * y[2])))
                           / k[0]], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0], y0[2]+1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0, -1], [0, 0, 1]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    e1 = np.cos(np.pi * sol.y[:, 2]) + np.exp(-(1 + sol.y[:, 2]) / np.sqrt(sol.k[0])) + np.exp(
        -(1 - sol.y[:, 2]) / np.sqrt(sol.k[0]))
    e2 = np.exp((sol.y[:, 2] - 1) / np.sqrt(sol.k[0])) / np.sqrt(sol.k[0]) - np.pi * np.sin(
        np.pi * sol.y[:, 2]) - 1 / (np.sqrt(sol.k[0]) * np.exp((sol.y[:, 2] + 1) / np.sqrt(sol.k[0])))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t15(algorithm, const):
    def odefun(y, _, k):
        return 2 * y[1], 2 * (y[2] * y[0] / k[0]), 2

    def odejac(y, _, k):
        df_dy = np.array([[0, 2, 0], [2 * (y[2] / k[0]), 0, 2 * (y[0] / k[0])], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0] - 1, y0[2] + 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1, 0, -1], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    assert sol.converged is True


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t16(algorithm, const):
    def odefun(y, _, k):
        return 1 * y[1], 1 * (-y[0] * np.pi ** 2 / (4 * k[0])), 1

    def odejac(_, __, k):
        df_dy = np.array([[0, 1, 0], [-np.pi**2 / (4 * k[0]), 0, 0], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, k):
        return y0[0], yf[0] - np.sin(np.pi / (2 * np.sqrt(k[0]))), y0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.sin(np.pi * sol.y[:, 2] / (2 * np.sqrt(sol.k[0])))
    e2 = (np.pi * np.cos((np.pi * sol.y[:, 2]) / (2 * np.sqrt(sol.k[0])))) / (2 * np.sqrt(sol.k[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t17(algorithm, const):
    def odefun(y, _, k):
        return 0.2 * y[1], 0.2 * (-3 * k[0] * y[0] / (k[0] + y[2] ** 2) ** 2), 0.2

    def odejac(y, _, k):
        df_dy = np.array([[0, 0.2, 0],
                          [-(3 * k[0]) / (5 * (y[2] ** 2 + k[0]) ** 2), 0, (12 * k[0] * y[0] * y[2])
                           / (5 * (y[2] ** 2 + k[0]) ** 3)], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, k):
        return y0[0] + 0.1 / np.sqrt(k[0] + 0.01), yf[0] - 0.1 / np.sqrt(k[0] + 0.01), y0[2] + 0.1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = sol.y[:, 2]/np.sqrt(sol.k[0] + sol.y[:, 2] ** 2)
    e2 = 1 / np.sqrt(sol.y[:, 2] ** 2 + sol.k[0]) - sol.y[:, 2] ** 2 / (sol.y[:, 2] ** 2 + sol.k[0]) ** (3 / 2)
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t18(algorithm, const):
    def odefun(y, _, k):
        return y[1], (-y[1] / k[0]), 1

    def odejac(_, __, k):
        df_dy = np.array([[0, 1, 0], [0, -1 / k[0], 0], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, k):
        return y0[0] - 1, yf[0] - np.exp(-1 / k[0]), y0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.exp(-sol.y[:, 2] / sol.k[0])
    e2 = -1 / (sol.k[0] * np.exp(sol.y[:, 2] / sol.k[0]))
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t19(algorithm, const):
    def odefun(y, _, k):
        return y[1], (-y[1] / k[0]), 1

    def odejac(_, __, k):
        df_dy = np.array([[0, 1, 0], [0, -1 / k[0], 0], [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0], y0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t21(algorithm, const):
    def odefun(y, _, k):
        return y[1], (y[0] * (1 + y[0]) - np.exp(-2 * y[2] / np.sqrt(k[0]))) / k[0], 1

    def odejac(y, _, k):
        df_dy = np.array([[0, 1, 0],
                          [(2*y[0] + 1) / k[0], 0, (2 * np.exp(-(2 * y[2]) / np.sqrt(k[0]))) / k[0] ** (3 / 2)],
                          [0, 0, 0]])
        df_dp = np.empty((3, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, k):
        return y0[0] - 1, yf[0] - np.exp(-1 / np.sqrt(k[0])), y0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0, 0], [0, 0, 1]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.exp(-sol.y[:, 2] / np.sqrt(const))
    e2 = -np.exp(-sol.y[:, 2] / np.sqrt(const)) / np.sqrt(const)
    assert all(e1 - sol.y[:, 0] < tol)
    assert all(e2 - sol.y[:, 1] < tol)


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t22(algorithm, const):
    def odefun(y, _, k):
        return y[1], -(y[1] + y[0] * y[0]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [-(2*y[0]) / k[0], -1 / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0] - 1 / 2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0], [0, 0]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, MEDIUM))
def test_t23(algorithm, const):
    def odefun(y, _, k):
        return y[1], 1 / k[0] * np.sinh(y[0] / k[0])

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [np.cosh(y[0] / k[0]) / k[0] ** 2, 0]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0] - 1

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm)
    algo.set_derivative_jacobian(odejac)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0, 0], [1, 0]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t24(algorithm, const):
    def odefun(x, _, k):
        a_mat_x = 1 + x[2] ** 2
        a_mat_xp = 2 * x[2]
        y = 1.4
        return (x[1], (((1 + y) / 2 - k[0] * a_mat_xp) * x[0] * x[1] - x[1] / x[0] - (a_mat_xp / a_mat_x) * (
                1 - (y - 1) / 2 * x[0] ** 2)) / (k[0] * a_mat_x * x[0]), 1)

    def odejac(x, _, k):
        y = 1.4
        df_dy = np.array(
            [[0, 1, 0],
             [(x[1] * (y / 2 - 2 * k * x[2] + 1 / 2) + x[1] / x[0] ** 2
               + (4 * x[0] * x[2] * (y / 2 - 1 / 2)) / (x[2] ** 2 + 1)) / (k[0] * x[0] * (x[2] ** 2 + 1))
              - ((2 * x[2] * ((y / 2 - 1 / 2) * x[0] ** 2 - 1)) / (x[2] ** 2 + 1) - x[1] / x[0] + x[0] * x[1]
                 * (y / 2 - 2 * k[0] * x[2] + 1 / 2)) / (k[0] * x[0] ** 2 * (x[2] ** 2 + 1)),
              (x[0] * (y / 2 - 2 * k[0] * x[2] + 1 / 2) - 1 / x[0]) / (k[0] * x[0] * (x[2] ** 2 + 1)),
              -((4 * x[2] ** 2 * ((y / 2 - 1 / 2) * x[0] ** 2 - 1)) / (x[2] ** 2 + 1) ** 2
                - (2 * ((y / 2 - 1 / 2) * x[0] ** 2 - 1)) / (x[2] ** 2 + 1) + 2 * k[0] * x[0] * x[1])
              / (k[0] * x[0] * (x[2] ** 2 + 1))
              - (2 * x[2] * ((2 * x[2] * ((y / 2 - 1 / 2) * x[0] ** 2 - 1))
                             / (x[2] ** 2 + 1) - x[1] / x[0] + x[0] * x[1]
                             * (y / 2 - 2 * k[0] * x[2] + 1 / 2))) / (k[0] * x[0] * (x[2] ** 2 + 1) ** 2)],
             [0, 0, 0]])
        df_dp = np.empty((3, 0))

        return df_dy, df_dp

    def bcfun(x0, xf, _, __, ___):
        return x0[0] - 0.9129, xf[0] - 0.375, x0[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 1, 0], [0.1, 0.1, 1]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t25(algorithm, const):
    def odefun(y, _, k):
        return y[1], y[0] * (1 - y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [(1-y[1]) / k[0], -y[0] / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1 / 3, yf[0] - 1 / 3

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=16)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[-1/3, 1], [1/3, 1]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t26(algorithm, const):
    def odefun(y, _, k):
        return y[1], y[0] * (1 - y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [(1-y[1]) / k[0], -y[0] / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0] + 1/3

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=64)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 0], [-1/3, 0]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t27(algorithm, const):
    def odefun(y, _, k):
        return y[1], y[0] * (1 - y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [(1-y[1]) / k[0], -y[0] / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0] - 1 / 3

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 0], [1 / 3, 0]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const*10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t28(algorithm, const):
    def odefun(y, _, k):
        return y[1], (y[0] - y[0]*y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [(1-y[1]) / k[0], -y[0] / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 1, yf[0] - 3/2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=1)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[1, 0], [3/2, 0]])
    sol.k = np.array([const])
    sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t29(algorithm, const):
    def odefun(y, _, k):
        return y[1], (y[0] - y[0]*y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [(1-y[1]) / k[0], -y[0] / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0] - 3/2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=1)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0], [3/2, 0]])
    sol.k = np.array([const])
    sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t30(algorithm, const):
    def odefun(y, _, k):
        return y[1], (y[0] - y[0]*y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1], [(1-y[1]) / k[0], -y[0] / k[0]]])
        df_dp = np.empty((2, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 7/6, yf[0] - 3/2

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=8)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[-7/6, 0], [3/2, 0]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, HARD))
def test_t31(algorithm, const):
    def odefun(y, _, k):
        return np.sin(y[1]), y[2], -y[3] / k[0], \
               ((y[0]-1) * np.cos(y[1]) - y[2] / np.cos(y[1]) - k[0] * y[3] * np.tan(y[1])) / k[0]

    def odejac(y, _, k):
        df_dy = np.array(
            [[0, np.cos(y[1]), 0, 0], [0, 0, 1, 0], [0, 0, 0, -1 / k[0]],
             [np.cos(y[1]) / k[0], -(np.sin(y[1]) * (y[0] - 1) + k[0] * y[3] * (np.tan(y[1]) ** 2 + 1)
                                     + (y[2] * np.sin(y[1])) / np.cos(y[1]) ** 2) / k[0], -1 / (k[0] * np.cos(y[1])),
              -np.tan(y[1])]])
        df_dp = np.empty((4, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], y0[2], yf[0], yf[2]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=12)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0, 0, 0], [0, 0, 0, 0]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const * 10, const, 10)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t32(algorithm, const):
    def odefun(y, _, k):
        return y[1], y[2], y[3], (y[1]*y[2] - y[0]*y[3]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
                          [-y[3] / k[0], y[2] / k[0], y[1] / k[0], -y[0] / k[0]]])
        df_dp = np.empty((4, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0], y0[1], yf[0] - 1, yf[1]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=4)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[0, 0, 0, 0], [1, 0, 0, 0]])
    sol.k = np.array([const])
    sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("algorithm, k", itertools.product(ALGORITHMS, VHARD))
def test_t33(algorithm, const):
    def odefun(y, _, k):
        return y[1], (y[0]*y[3] - y[2]*y[1]) / k[0], y[3], y[4], y[5], (-y[2] * y[5] - y[0] * y[1]) / k[0]

    def odejac(y, _, k):
        df_dy = np.array(
            [[0, 1, 0, 0, 0, 0], [y[3] / k[0], -y[2] / k[0], -y[1] / k[0], y[0] / k[0], 0, 0], [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-y[1] / k[0], -y[0] / k[0], -y[5] / k[0], 0, 0, -y[2] / k[0]]])
        df_dp = np.empty((6, 0))
        return df_dy, df_dp

    def bcfun(y0, yf, _, __, ___):
        return y0[0] + 1, y0[2], y0[3], yf[0] - 1, yf[2], yf[3]

    algo = Shooting(odefun, None, bcfun, algorithm=algorithm, num_arcs=12)
    algo.set_derivative_jacobian(odejac)
    sol = Trajectory()
    sol.t = np.linspace(0, 1, 2)
    sol.y = np.array([[-1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
    sol.k = np.array([const])
    # noinspection PyTypeChecker
    cc = np.linspace(const * 10, const, 10, dtype=np.float)
    for c in cc:
        sol = copy.deepcopy(sol)
        sol.k = np.array([c])
        sol = algo.solve(sol)['traj']

    assert sol.converged


@pytest.mark.parametrize("k", MEDIUM)
def test_r2(const):
    def odefun(y, _, k):
        return y[0] / k[0]

    def quadfun(y, _, __):
        return y[0]

    def bcfun(_, q0, __, qf, ___, ____, _____):
        return q0[0] - 1, qf[0]

    algo = Shooting(odefun, quadfun, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1], [1]])
    solinit.q = np.array([[0], [0]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.k)) / (1.e0 - np.exp(-1.e0 / sol.k))
    e2 = np.exp((sol.t - 1) / sol.k) / (sol.k * (1 / np.exp(1 / sol.k) - 1))
    assert all(e1 - sol.q[:, 0] < tol)
    assert all(e2 - sol.y[:, 0] < tol)


@pytest.mark.parametrize("k", MEDIUM)
def test_r8(const):
    def odefun(y, _, k):
        return -y[0] / k[0]

    def quadfun(y, _, __):
        return y[0]

    def bcfun(_, q0, __, qf, ___, ____, _____):
        return q0[0] - 1, qf[0] - 2

    algo = Shooting(odefun, quadfun, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1], [1]])
    solinit.q = np.array([[0], [0]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = (1.e0 - np.exp((sol.t - 1.e0) / sol.k)) / (1.e0 - np.exp(-1.e0 / sol.k))
    e2 = np.exp((sol.t - 1) / sol.k) / (sol.k * (1 / np.exp(1 / sol.k) - 1))
    assert all(e1 - sol.q[:, 0] < tol)
    assert all(e2 - sol.y[:, 0] < tol)


@pytest.mark.parametrize("k", MEDIUM)
def test_r18(const):
    def odefun(y, _, k):
        return -y[0] / k[0]

    def quadfun(y, _, __):
        return y[0]

    def bcfun(_, q0, __, qf, ___, ____, k):
        return q0[0] - 1, qf[0] - np.exp(-1 / k[0])

    algo = Shooting(odefun, quadfun, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[1], [1]])
    solinit.q = np.array([[0], [0]])
    solinit.k = np.array([const])
    sol = algo.solve(solinit)['traj']

    e1 = np.exp(-sol.t / sol.k[0])
    e2 = -1 / (sol.k[0] * np.exp(sol.t / sol.k[0]))
    assert all(e1 - sol.q[:, 0] < tol)
    assert all(e2 - sol.y[:, 0] < tol)


def test_shooting_1():
    # Full 2PBVP test problem
    # This is the simplest BVP

    def odefun(y, _, __):
        return y[1], -abs(y[0])

    def bcfun(y0, yf, _, __, ___):
        return y0[0], yf[0] + 2

    algo = Shooting(odefun, None, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 4, 2)
    solinit.y = np.array([[0, 1], [0, 1]])
    solinit.k = np.array([])
    out = algo.solve(solinit)['traj']
    assert out.y[0][0] < tol
    assert out.y[0][1] - 2.06641646 < tol
    assert out.y[-1][0] + 2 < tol
    assert out.y[-1][1] + 2.87588998 < tol
    assert out.t[-1] - 4 < tol
    assert abs(out.y[0][1] - solinit.y[0][1]) > tol
    assert abs(out.y[-1][0] - solinit.y[-1][0]) - 2 < tol


# def test_shooting_2():
#     # Full 2PBVP test problem
#     # This is calculating the 4th eigenvalue of Mathieu's Equation
#     # This problem contains an adjustable parameter.
#
#     def odefun(y, p, k):
#         return (y[1], -(p[0] - 2 * 5 * np.cos(2 * t)) * y[0])
#
#     def bcfun(y0, q0, yf, qf, p, ndp, k):
#         return (y0[1], yf[1], y0[0] - 1)
#
#     algo = Shooting(odefun, None, bcfun)
#     solinit = Trajectory()
#     solinit.t = np.linspace(0, np.pi, 30)
#     solinit.y = np.vstack((np.cos(4 * solinit.t), -4 * np.sin(4 * solinit.t))).T
#     solinit.p = np.array([15])
#     solinit.k = np.array([])
#
#     out = algo.solve(solinit)['traj']
#     assert abs(out.t[-1] - np.pi) < tol
#     assert abs(out.y[0][0] - 1) < tol
#     assert abs(out.y[0][1]) < tol
#     assert abs(out.y[-1][0] - 1) < tol
#     assert abs(out.y[-1][1]) < tol
#     assert abs(out.p[0] - 17.09646175) < tol


def test_shooting_3():
    # This problem contains a parameter, but it is not explicit in the BCs.
    # Since time is buried in the ODEs, this tests if the BVP solver calculates
    # sensitivities with respect to parameters.
    def odefun(_, p, __):
        return 1 * p[0]

    def bcfun(y0, yf, _, __, ___):
        return y0[0] - 0, yf[0] - 2

    algo = Shooting(odefun, None, bcfun)
    solinit = Trajectory()
    solinit.t = np.linspace(0, 1, 2)
    solinit.y = np.array([[0], [0]])
    solinit.p = np.array([1])
    solinit.k = np.array([])
    out = algo.solve(solinit)['traj']
    assert abs(out.p - 2) < tol


def test_shooting_4():
    # This problem contains a quad and tests if the prob solver correctly
    # integrates the quadfun. Also tests multiple shooting.

    def odefun(x, _, __):
        return -x[1], x[0]

    def quadfun(x, _, __):
        return x[0]

    def bcfun(y0, _, __, qf, ___, ____, _____):
        return y0[0], y0[1] - 1, qf[0] - 1.0

    algo = Shooting(odefun, quadfun, bcfun, num_arcs=4)
    solinit = Trajectory()
    solinit.t = np.linspace(0, np.pi / 2, 2)
    solinit.y = np.array([[1, 0], [1, 0]])
    solinit.q = np.array([[0], [0]])
    solinit.k = np.array([])
    out = algo.solve(solinit)['traj']
    assert (out.y[0, 0] - 0) < tol
    assert (out.y[0, 1] - 1) < tol
    assert (out.q[0, 0] - 2) < tol
    assert (out.q[-1, 0] - 1) < tol
