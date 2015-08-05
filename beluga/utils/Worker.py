from .propagators import *
from beluga.utils.joblib import Parallel, delayed
from beluga.utils.joblib import pool
import os
from beluga.utils import Propagator
from beluga.utils import keyboard

import numpy as np

try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

# TODO: Create py test for worker class
# TODO: Give worker class all functionality of the framework.
class Worker(object):
    def __init__(self, mode = 'MPI', propagator = Propagator()):
        self.process_count = os.cpu_count()
        self.mode = mode
        self.Propagator = propagator

        if self.mode == 'HOST':
            # Do nothing?
            self.rank = 0
        elif self.mode == 'MPI':
            self.comm = MPI.COMM_WORLD
            self.rank = self.comm.Get_rank()
            if self.rank == 0:
                self.mode = 'HOST'
        elif self.mode == 'TCP':
            raise Exception('TCP mode not yet implemented. Start worker process in MPI mode.')
        elif self.mode == 'DUAL':
            raise Exception('DUAL mode not yet implemented. Start worker process in MPI mode.')

        self.startworker()

    def startworker(self):
        self.started = 1
        if self.mode == 'MPI':
            print('Worker process started. Rank: ' + str(self.rank))
            while self.started:
                data = self.comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=MPI.Status())
                print('Received ' + str(data) + ' from ' + str(status.Get_source()) + ' with ' + str(status.Get_tag()))
                print('Closing ' + str(self.rank))
                self.started = 0
                self.stopworker()
        else:
            self.comm.send(10,dest=1,tag=2)

    def solve(self, problem, *args, **kwargs):
        # Generic solve method.
        return None

    def stopworker(self):
        return None