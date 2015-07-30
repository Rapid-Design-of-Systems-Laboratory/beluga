from .propagators import *
from beluga.utils.joblib import Parallel, delayed
from beluga.utils.joblib import pool
import os
from beluga.utils import keyboard

import numpy as np

try:
    import mpi4py
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

# TODO: Create py test for propagator class
class Propagator(object):
    def __init__(self, solver='ode45', process_count=-1):
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(solver)
        if not method:
             raise Exception("Method %s not implemented" % solver)
        self.solver = method
        self.poolinitialized = 0

        self.process_count = process_count
        if self.process_count == -1:
            self.process_count = os.cpu_count()
        elif self.process_count > os.cpu_count():
            self.process_count = os.cpu_count()

        # Same number of threads as processes until I can figure out how to get past the GIL lock
        self.threads = self.process_count

    def startpool(self):
        if self.poolinitialized == 0:
            self.pool = pool.Pool(processes=self.process_count)
            self.poolinitialized = True

        print('Number of processors OS: ' + str(os.cpu_count()))
        print('HPCSUPPORTED: ' + str(HPCSUPPORTED))
        raise('DONE')

    def closepool(self):
        self.poolinitialized = False
        self.pool.close()
        self.pool.terminate()

    # TODO: Figure out how to add processes to an already started pool
    def addprocess(self):
        if self.poolinitialized:
            return None

    def solve(self, f, tspan, y0, *args, **kwargs):
        # Solve can handle either tspan with list length 2, and numpy array y0 for a SINGLE arc
        # or a tspan list the same length as y0 list for MULTIPLE arcs


        # Check if y0 is a list or np array. If it's a list, use parallel processing. Need to find a better way of determining parallel computations!
        if isinstance(y0,np.ndarray):
            sol = self.solver(f, tspan, y0, *args, **kwargs)
        else:
            """if len(tspan) == 1 & len(y0) == 1:
                sol = self.solver(f, tspan[0], y0[0], *args, **kwargs)
            elif len(tspan) == 1 & len(y0) != 1:
                t_and_y = Parallel(n_jobs=self.threads,backend='threading')(delayed(self.solver)(f,tspan[0],y,*args,**kwargs) for y in y0)
                sol = t_and_y # FIX THIS
            elif isinstance(tspan, np.ndarray):
                sol = Parallel(n_jobs=self.threads,backend='threading')(delayed(self.solver)(f,tspan[0],y,*args,**kwargs) for y in y0)
            else:"""
            if self.poolinitialized:
                #multisol = self.pool.map_async(self.solver,[(f,t,y, args,kwargs) for (t,y) in zip(tspan,y0)])
                multisol = [self.pool.apply_async(self.solver,(f,t,y) + args,(kwargs)) for (t,y) in zip(tspan,y0)]
                #keyboard()
                t_and_y = [s.get() for s in multisol]
                sol = list(zip(*t_and_y))
            else:
                # If pool hasn't been initialized, use backend threading.
                t_and_y = Parallel(n_jobs=self.threads,backend='threading')(delayed(ode45)(f,t,y,*args,**kwargs) for (t,y) in zip(tspan,y0))
                sol = list(zip(*t_and_y))

        return sol

    # TODO: Figure out how to disable GIL and try using backend threading instead of a pool. This will reduce overhead. Apparently Cython can do this
    def __sendnogiljob(self, f, tspan, y0, *args, **kwagrs):
        return None