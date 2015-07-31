from .propagators import *
from beluga.utils.joblib import Parallel, delayed
from beluga.utils.joblib import pool
import os
from beluga.utils import keyboard

import numpy as np

try:
    import mpi4py as mpi
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

# TODO: Create py test for propagator class
class Worker(object):
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

    def startworker(self):
        print('HPC SUPPORTED: ' + str(HPCSUPPORTED))
        commworld = mpi.COMM_WORLD
        keyboard()
        return None