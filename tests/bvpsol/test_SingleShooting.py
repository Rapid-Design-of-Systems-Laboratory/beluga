from math import *
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import numpy as np
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

def brachisto_bc(ya,yb,p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = yb[:7]

    thetta = compute_control(1,yb,p,aux)
    H = compute_hamiltonian(1,yb,p,aux,[thetta])

    # x0 = aux['initial']
    # xf = aux['terminal']
    return np.array([
        ya[0] - aux['initial']['x'], # x(0
        ya[1] - aux['initial']['y'], # y(0)
        ya[2] - aux['initial']['v'], # v(0)
        yb[0] - aux['terminal']['x'], # x(tf)
        yb[1] - aux['terminal']['y'], # y(tf)
        yb[5] + 0.0,   # lamV(tf)
        H     - 0,     # H(tf)

    ])
def test_solve():
    solinit = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
    bvp = bvpsol.BVP(brachisto_ode,brachisto_bc,
                                    initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                                    terminal_bc = {'x':0.1, 'y':-0.1},
                                    const = {'g':-9.81},
                                    constraint = {}
                                    )
    solver_csd = algorithms.SingleShooting(derivative_method='csd',cached=False)
    solver_fd  = algorithms.SingleShooting(derivative_method='fd',cached=False)

    solver_csd.solve(bvp,solinit)
    solver_fd.solve(bvp,solinit)
    pass

def test_bcjac_csd():
    pass

def test_bcjac_fd():
    pass

def test_stmode_csd():
    pass

def test_stmode_fd():
    pass
