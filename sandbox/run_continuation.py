import sys, os
sys.path.append(os.getcwd()+'/../')

import math
import numpy as np
import bvpsol as bs
import bvpsol.algorithms as algo
from utils import *

################################################################
# Second example
Q = 5.0
def function(X,Y,parameters,aux):
    LAMBDA = Y[2]
    return np.array([Y[1],
                        -(LAMBDA - 2.0*Q*np.cos(2.0*X))*Y[0],
                    0])

def boundary_conditions (Ya,Yb,parameters,aux):
    return np.array([Ya[1] - aux['initial']['y2'],
                     Ya[0] - aux['initial']['y1'],
                     Yb[1] - aux['terminal']['y2']])
def guess(X):
    return np.array([np.cos(4.0*X)   ,
                        -4.0*np.sin(4.0*X),
                        15.0])  # Converted LAMBDA parameter to state

################################################################

solinit = bs.bvpinit(np.linspace(0,math.pi,2), guess)

bvp = bs.Problem(function,boundary_conditions,
                                states = ['y1','y2'],
                                initial_bc = {'y1':1.0, 'y2':0.0},
                                terminal_bc = {'y2':0.0}, 
                                const = [], 
                                constraint = []
                                )



################################################################
#           Stuff in the input file                            #
################################################################
from continuation import *

# step1 will actually be loaded from an array of continuation steps
step1 = ContinuationStep()
step1.num_cases = 5
step1.initial('y1',2.0)


from numba.decorators import jit
@autojit
def run_continuation(step1,bvp):
    import matplotlib.pylab as pylab
    pylab.figure()
    solver = algo.SingleShooting(derivative_method='csd')
    ################################################################
    #            Actual code for runContinuation                   #
    ################################################################

    step1.set_bvp(bvp)
    step1.reset();

    print('\nRunning continuation set 1:')
    sol_last = solinit
    total_time = 0.0;
    while not step1.complete():
        print('Starting iteration '+str(step1.ctr+1)+'/'+str(step1.num_cases))
    
        tic()
    
        bvp = step1.next()
        sol = solver.solve(bvp,sol_last)
    
        # Update solution for next iteration
        sol_last = sol
        elapsed_time = toc()
        total_time  += elapsed_time
        print('Iteration %d/%d converged in %0.4f seconds\n' % (step1.ctr+1, step1.num_cases, elapsed_time))
    
        pylab.plot(sol.x, sol.y[0,:],'-')

    print('Continuation process completed in %0.4f seconds.\n' % total_time)
    
    
    ################################################################

    pylab.title('Solution for MAT4BVP example (Mathieu\'s equation)')
    pylab.xlabel('x')
    pylab.legend(['y(0)=1.0','y(0)=1.25','y(0)=1.50','y(0)=1.75','y(0)=2.0'])
    pylab.show()

run_continuation(step1,bvp)
# keyboard()