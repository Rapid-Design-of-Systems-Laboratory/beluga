from .propagators import *
import os
from beluga.utils import keyboard
from multiprocessing_on_dill import pool
import dill

import numpy as np

# TODO: Create py test for propagator class
# TODO: Find a better worker-propagator relationship.
class Propagator(object):
    """!
    \brief     Main class of the propagator.
    \details   This class handles all propagation of differential equations in serial or parallel on a single node.
    \author    Mike Sparapany
    \version   0.1
    \date      08/08/15
    """
    def __init__(self, solver='ode45', process_count=-1):
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(solver)
        if not method:
             raise Exception("Method %s not implemented" % solver)
        self.solver = method
        self.poolinitialized = 0

        self.process_count = process_count
        # Set process count to be the same number as available cores
        if self.process_count == -1:
            self.process_count = os.cpu_count()
        elif self.process_count > os.cpu_count():
            self.process_count = os.cpu_count()

        self.poolinitialized = False

    def __call__(self, f, tspan, y0, *args, **kwargs):
        # Solve can handle either tspan with list length 2, and numpy array y0 for a SINGLE arc
        # or a tspan list the same length as y0 list for MULTIPLE arcs


        # Check if y0 is a list or np array. If it's a list, use parallel processing. Need to find a better way of determining parallel computations!
        if isinstance(y0,np.ndarray):
            sol = self.solver(f, tspan, y0, *args, **kwargs)
        else:
            if self.poolinitialized:
                multisol = [self.pool.apply_async(self.solver,(f,t,y) + args,(kwargs)) for (t,y) in zip(tspan,y0)]
                t_and_y = [s.get() for s in multisol]

                sol = list(zip(*t_and_y))
                return sol

            else:
                tout = []
                yout = []
                for i in range(len(y0)):
                    ttemp, ytemp = ode45(f,tspan[i], y0[i], *args, **kwargs)
                    tout.append(ttemp)
                    yout.append(ytemp)

                return tout, yout

    def startPool(self):
        if dill.__version__ == '0.2.5':
            if self.poolinitialized is False:
                self.pool = pool.Pool(processes=self.process_count)
                self.poolinitialized = True
        else:
            print('Could not start parallel pool. Running in single-core mode. Use dill version 0.2.5 for parallelization.')

    def closePool(self):
        if self.poolinitialized:
            self.poolinitialized = False
            self.pool.close()
            self.pool.terminate()

    def setSolver(self,solver='ode45'):
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(solver)
        if not method:
             raise Exception("Method %s not implemented" % solver)
        self.solver = method
