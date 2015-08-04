from .propagators import *
from beluga.utils.joblib import Parallel, delayed
from beluga.utils.joblib import pool
import os
from beluga.utils import keyboard

import numpy as np

try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

# TODO: Create py test for worker class
class Worker(object):
    def __init__(self):
        self.process_count = os.cpu_count()

        # Same number of threads as processes until I can figure out how to get past the GIL lock
        self.threads = self.process_count

    def startworker(self):
        if HPCSUPPORTED == 1:
            self.comm = MPI.COMM_WORLD
            self.rank = self.comm.Get_rank()
            print('HPC SUPPORTED: ' + str(HPCSUPPORTED) + ' Rank: ' + str(self.rank))
        return None

    def stopworker(self):
        if HPCSUPPORTED == 1:
            print('HPC SUPPORTED: ' + str(HPCSUPPORTED))

        return None