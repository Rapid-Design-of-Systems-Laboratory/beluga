import sys, os
sys.path.append(os.getcwd()+'/../')

import numpy as np
from utils import ode45
import math

################################################################
# First example problem
def twoode(x,y, parameters,aux):
    return np.array([ y[1], -abs(y[0]) ]);

def twobc(ya,yb,parameters,aux):
    return np.array([ ya[0], yb[0] + 2 ]);

################################################################
# Second example
Q = 5.0
def function(X,Y,parameters, aux):
    LAMBDA = Y[2]
    return np.array([Y[1],
                        -(LAMBDA - 2.0*Q*np.cos(2.0*X))*Y[0],
                    0])

def boundary_conditions (Ya,Yb,parameters,aux):
    return np.array([Ya[1],
                       Ya[0] - 1.0,
                       Yb[1]])
def guess(X):
    return np.array([np.cos(4.0*X)   ,
                        -4.0*np.sin(4.0*X),
                        15.0])  # Converted LAMBDA parameter to state

################################################################

from bvpsol.algorithms import SingleShooting#, ScikitsBVPSolver

import bvpsol
# import matplotlib.pylab as pylab

shoot_fd  = SingleShooting(derivative_method='fd')
shoot_csd = SingleShooting(derivative_method='csd',tolerance=1e-10)

# #solinit = bvpsol.Solution(np.linspace(0,4,5),np.array([[0,-2],[2.669,4]]))
# # Initial guess is just the same vector
# solinit = bvpsol.bvpinit(np.linspace(0,4,5),[0,2.5])
# sol1 = shoot_fd.solve(twoode,twobc, solinit)
#
# pylab.figure()
# pylab.plot(sol1.x, sol1.y[0,:],'-')
# pylab.plot(sol1.x, sol1.y[1,:],'-')
# pylab.title('Solution for TWOODE example')
# pylab.xlabel('x')
# pylab.legend(['y1','y2'])
# pylab.draw()

# Use guess function to generate initial guess structure
solinit = bvpsol.bvpinit(np.linspace(0,math.pi,10), guess)
prob2 = bvpsol.BVP(function,boundary_conditions,
                                states = ['y1','y2','lambda'],
                                initial_bc = {'y1':1.0, 'y2':0.0,'lambda':0.0},
                                terminal_bc = {'y1':0.0},
                                const = {},
                                constraint = {}
                                )
#
# solv = ScikitsBVPSolver(num_left_boundary_conditions = 2)
# sol2 = solv.solve(prob2,solinit)
# print 'Lambda is '+str(sol2.y[2,-1])

sol2 = shoot_csd.solve(prob2,solinit)
print 'Lambda is '+str(sol2.y[2,-1])
#
# pylab.figure()
# pylab.plot(sol2.x, sol2.y[0,:],'-')
# pylab.plot(sol2.x, sol2.y[1,:],'-')
# pylab.title('Solution for MAT4BVP example (Mathieu\'s equation)')
# pylab.xlabel('x')
# pylab.legend(['y1','y2'])
# pylab.show()
