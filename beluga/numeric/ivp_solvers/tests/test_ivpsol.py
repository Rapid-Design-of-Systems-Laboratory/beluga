from beluga.numeric.ivp_solvers import Propagator, Trajectory, integrate_quads
import numpy as np
from math import *

tol = 1e-3


def test_propagator_1():
    k = [-0.5, -0.2]

    def odefn(x, p, const):
        return np.array([k[0]*x[0], k[1]*x[1]])

    y0 = np.array([10, -50])
    q0 = np.array([])
    tspan = np.array([0, 1.0])
    prop = Propagator()
    solout = prop(odefn, None, tspan, y0, q0, [], {})
    t1 = solout.t
    x1 = solout.y.T
    x1_expected = np.array([y*np.exp(k_*t1) for (y, k_) in zip(y0, k)])
    assert (x1 - x1_expected < 1e-5).all()


def test_propagator_2():
    def odefun(x, p, const):
        return -x[1], x[0]

    def quadfun(x, p, const):
        return x[0]

    y0 = np.array([1, 0])
    q0 = np.array([0])
    tspan = np.array([0, pi / 2])
    prop = Propagator()
    solout = prop(odefun, quadfun, tspan, y0, q0, [], [])

    assert solout.y.T[0, -1] < tol
    assert solout.y.T[1, -1] - 1 < tol
    assert ((solout.y[:, 1] - solout.q[:, 0]) < tol).all()


def test_Trajectory():
    t = np.array([0, 1, 2, 3])
    y1 = t ** 2

    gam = Trajectory(t, y1)
    y, q, u = gam(0.5)
    assert y == 0.5
    assert len(q) == 0
    assert len(u) == 0

    y, q, u = gam(0.25)
    assert y == 0.25
    assert len(q) == 0
    assert len(u) == 0

    gam.set_interpolate_function('cubic')

    y, q, u = gam(0.25)
    assert y - 0.0625 < 1e-4
    assert len(q) == 0
    assert len(u) == 0

    t, y, q, u = gam[0]
    assert t == 0
    assert y == 0
    assert len(q) == 0
    assert len(u) == 0


def test_integrate_quads():
    # Test a 1-dim x and 1-dim q
    t = np.linspace(0, 10, 100)
    y1 = np.sin(t)

    def quadfun(t, y):
        return y[0]

    gam = Trajectory(t, y1)
    assert integrate_quads(quadfun, np.array([0, 1 * np.pi]) + 0, gam) - 2 < 1e-3
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 0, gam) < 1e-3
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 1, gam) < 1e-3
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 2, gam) < 1e-3
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 3, gam) < 1e-3

    # Test a 2-dim x and 1-dim q
    t = np.linspace(0, 10, 100)
    y1 = np.sin(t)
    y2 = np.cos(t)

    def quadfun(t, y):
        return y[0]*y[1]

    gam = Trajectory(t, np.vstack((y1, y2)).T)
    assert integrate_quads(quadfun, np.array([0, 1 * np.pi]) + 0, gam) - np.pi/2 < 1e-3
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 0, gam) - np.pi < 1e-3

    # Test a 1-dim x and 2-dim q
    t = np.linspace(0, 10, 100)
    y1 = np.sin(t)

    def quadfun(t, y):
        return y[0], y[0]**2

    gam = Trajectory(t, y1)
    assert integrate_quads(quadfun, np.array([0, 1 * np.pi]) + 0, gam)[0] - 2 < 1e-3
    assert integrate_quads(quadfun, np.array([0, 1 * np.pi]) + 0, gam)[1] - np.pi/2 < 1e-3

    # Test a 2-dim x and 2-dim q
    t = np.linspace(0, 10, 100)
    y1 = np.sin(t)
    y2 = np.cos(t)

    def quadfun(t, y):
        return y[0], y[1]

    gam = Trajectory(t, np.vstack((y1, y2)).T)
    assert len(integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 2, gam)) == 2
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 2, gam)[0] < 1e-3
    assert integrate_quads(quadfun, np.array([0, 2 * np.pi]) + 2, gam)[1] < 1e-3
    assert integrate_quads(quadfun, np.array([0, 1 * np.pi]) + 0, gam)[0] - 2 < 1e-3
    assert integrate_quads(quadfun, np.array([0, 1 * np.pi]) + 0, gam)[1] < 1e-3
