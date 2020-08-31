from beluga.numeric.ivp_solvers import Propagator
import numpy as np
from math import *


def compute_hamiltonian(X, p, aux, u):
    [x, y, v, lamX, lamY, lamV, tf] = X[:7]
    g = aux['const']['g']

    thetta = u[0]
    return lamX*v*cos(thetta) + g*lamV*sin(thetta) + lamY*v*sin(thetta) + 1


def compute_control(X, p, aux):
    [x, y, v, lamX, lamY, lamV, tf] = X[:7]
    g = aux['const']['g']

    thetta_saved = float('inf')
    ham_saved = float('inf')

    try:
        thetta = -acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except (ValueError, ZeroDivisionError):
        thetta = 0
    ham = compute_hamiltonian(X, p, aux, [thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta
    try:
        thetta = acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except (ValueError, ZeroDivisionError):
        thetta = 0
    ham = compute_hamiltonian(X, p, aux, [thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = -acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except (ValueError, ZeroDivisionError):
        thetta = 0
    ham = compute_hamiltonian(X, p, aux, [thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except (ValueError, ZeroDivisionError):
        thetta = 0
    ham = compute_hamiltonian(X, p, aux, [thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    if thetta_saved == float('inf'):
        thetta_saved = 0
    return thetta_saved


def brachisto_ode(_X, _p, aux):
    [x, y, v, lamX, lamY, lamV, tf] = _X[:7]
    g = aux['const']['g']

    thetta = compute_control(_X, _p, aux)
    xdot = tf*np.array([v*cos(thetta),
                        v*sin(thetta),
                        g*sin(thetta),
                        0,
                        0,
                        -(lamX*cos(thetta) + lamY*sin(thetta)),
                        0])
    return xdot


inputs = [np.array([0.0, 0.0, 1.0, -0.1, -0.1, -0.1, 0.1]),
          [np.array([0.0, 0.0, 1.0, -0.1, -0.1, -0.1, 0.1]), np.array([0.0, 0.0, 1.0, -0.1, -0.1, -0.1, 0.1])]
          ]

x_end = np.array([2.57442406e-02, -1.46160497e-01, 1.96663900e+00, -1.00000000e-01,
                  -1.00000000e-01, -1.08178965e-01, 1.00000000e-01])


def test_ode45_2():
    x0 = inputs[0]
    q0 = []
    tspan = np.array([0, 1.0])
    prop = Propagator()
    aux = {'const': {'g': -9.81}}
    solout = prop(brachisto_ode, None, tspan, x0, q0, [], aux)
    x1 = solout.y

    assert (x1[-1, :] - x_end < 1e-5).all()
