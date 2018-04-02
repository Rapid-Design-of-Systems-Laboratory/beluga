import numpy as np
import numpy.testing as npt
from math import *
from beluga.integrators import ode45
from beluga.utils import keyboard

def test_ode45_1():
    """Test ode45() against analytical solution"""
    k  = [-0.5, -0.2]
    def odefn(t,x,p,aux):
        return np.array([k[0]*x[0],k[1]*x[1]])

    y0 = np.array([10,-50])
    tspan = np.array([0, 1.0])
    [t1,x1] = ode45(odefn,tspan,y0,[],{})
    x1_expected = np.array([y*np.exp(k_*t1) for (y,k_) in zip(y0,k)]).T
    npt.assert_almost_equal(x1,x1_expected)
    assert (x1 - x1_expected < 1e-5).all()

def compute_hamiltonian(t,X,p,aux,u):
    [x,y,v,lamX,lamY,lamV,tf] = X[:7]
    g = aux['const']['g']

    thetta = u[0]
    return lamX*v*cos(thetta) + g*lamV*sin(thetta) + lamY*v*sin(thetta) + 1

def compute_control(t,X,p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = X[:7]
    g = aux['const']['g']

    thetta_saved = float('inf')
    ham_saved = float('inf')

    try:
        thetta = -acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta
    try:
        thetta = acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = -acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    if thetta_saved == float('inf'):
        thetta_saved = 0
    return thetta_saved
#
def brachisto_ode(t,_X,_p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = _X[:7]
    g = aux['const']['g']

    thetta = compute_control(t,_X,_p,aux)
    xdot = tf*np.array([v*cos(thetta),
                     v*sin(thetta),
                     g*sin(thetta),
                     0,
                     0,
                     -(lamX*cos(thetta) + lamY*sin(thetta)),
                     0])
    return xdot

inputs = [np.array([0.0,0.0,1.0,-0.1,-0.1,-0.1,0.1]),
          [np.array([0.0,0.0,1.0,-0.1,-0.1,-0.1,0.1]),np.array([0.0,0.0,1.0,-0.1,-0.1,-0.1,0.1])]
          ]

x_end = np.array([  2.57442406e-02,  -1.46160497e-01,   1.96663900e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.08178965e-01,
      1.00000000e-01])

def test_ode45_2():
    # from beluga.utils import ode45

    x0 = inputs[0]
    tspan = np.array([0, 1.0])
    aux = {'const':{'g':-9.81}}
    [t1,x1] = ode45(brachisto_ode,tspan,x0,[],aux)

    assert (x1[-1] - x_end < 1e-5).all()
