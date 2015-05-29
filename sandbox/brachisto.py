# Use formatting strings to create code from templates
# Can embed code from separate strings
# Using cmath works with complex step
import sys, os
sys.path.append(os.getcwd()+'/../')

from math import *
from bvpsol.algorithms import SingleShooting#, ScikitsBVPSolver
import matplotlib.pyplot as plt

import numpy as np
import bvpsol
from utils import *

def compute_hamiltonian(t,X,p,aux,u):
    [x,y,v,lamX,lamY,lamV,tf] = X[:7]
    # g = aux['const'][0]
    g = aux['const']['g']
    
    thetta = u[0]
    return lamX*v*cos(thetta) + g*lamV*sin(thetta) + lamY*v*sin(thetta) + 1

def compute_control(t,X,p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = X[:7]
    # g = aux['const'][0]
    g = aux['const']['g']
    
    thetta_saved = float('inf')
    ham_saved = float('inf')
    
    try:
        thetta = -acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    # if abs(ham-ham_saved) > 1e-3 and ham < ham_saved:
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta
    try:
        thetta = acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    # if abs(ham-ham_saved) > 1e-3 and ham < ham_saved:
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = -acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    # if abs(ham-ham_saved) > 1e-3 and ham < ham_saved:
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    # if abs(ham-ham_saved) > 1e-3 and ham < ham_saved:
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta
        
    if thetta_saved == float('inf'):
        thetta_saved = 0
    return thetta_saved
    
def brachisto_ode(t,_X,_p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = _X[:7]
    g = aux['const']['g']
    # Define all states in dictionary
    # states = {}
    # for idx,state_var in enumerate(aux['states']):
    #     states[state_var] = _X[idx]
    # # globals().update(states)
    # vars().update(states)
    
    # print globals()
    # print states['tf']
    # print tf
    # Load constants and constraints into local namespace
    # for key in ['const','constraint']:
    #     var_dict = {}
    #     for idx,aux_var in enumerate(aux[key]):
    #         var_dict[aux[key+'_names'][idx]] = aux_var
    #     locals().update(var_dict)
    
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
        # ya[0] - x0[0], # x(0
        # ya[1] - x0[1], # y(0)
        # ya[2] - x0[2], # v(0)
        # yb[0] - xf[0], # x(tf)
        # yb[1] - xf[1], # y(tf)
        # yb[5] + 0.0,   # lamV(tf)
        # H     - 0,     # H(tf)
        ya[0] - aux['initial']['x'], # x(0
        ya[1] - aux['initial']['y'], # y(0)
        ya[2] - aux['initial']['v'], # v(0)
        yb[0] - aux['terminal']['x'], # x(tf)
        yb[1] - aux['terminal']['y'], # y(tf)
        yb[5] + 0.0,   # lamV(tf)
        H     - 0,     # H(tf)
        
    ])
################################################################
################################################################
################################################################

solinit = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
bvp = bvpsol.BVP(brachisto_ode,brachisto_bc,
                                states = ['x','y','v','lamX','lamY','lamV','tf'],
                                # const_names = ['g'],
                                # constraint_names = [],
                                initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                                terminal_bc = {'x':0.1, 'y':-0.1}, 
                                const = {'g':-9.81},
                                constraint = {}
                                # const = [-9.81],
                                # constraint = []
                                )

solver = SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)
# solver = ScikitsBVPSolver(num_left_boundary_conditions = 3)

################################################################
#           Stuff in the input file                            #
################################################################
from continuation import *

# step1 will actually be loaded from an array of continuation steps
step1 = ContinuationStep()
# 10 seconds for 100 in 5 steps
# 20 seconds for 100 in 25 steps
# 3 seconds for 100 in 2 steps
step1.num_cases = 2
step1.terminal('x',20.0)
step1.terminal('y',-20.0)

step1.set_bvp(bvp)
step1.reset();

print('\nRunning continuation set 1:')
sol_last = solinit
total_time = 0.0;
plt.clf()
while not step1.complete():
    print('Starting iteration '+str(step1.ctr+1)+'/'+str(step1.num_cases))
    tic()
    bvp = step1.next()
    sol = solver.solve(bvp,sol_last)
    
    # Update solution for next iteration
    sol_last = sol
    elapsed_time = toc()
    total_time  += elapsed_time
    print('Iteration %d/%d converged in %0.4f seconds\n' % (step1.ctr, step1.num_cases, elapsed_time))
    
    plt.plot(sol.y[0,:], sol.y[1,:],'-')

print('Continuation process completed in %0.4f seconds.\n' % total_time)
################################################################

plt.title('Solution for Brachistochrone problem')
plt.xlabel('x')
plt.ylabel('y')
plt.show(block=False)
