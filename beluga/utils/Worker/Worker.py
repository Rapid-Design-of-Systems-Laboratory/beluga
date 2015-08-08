from beluga.utils.propagators import *
from beluga.utils.joblib import Parallel, delayed
from beluga.utils.joblib import pool
import os
from beluga.utils import Propagator
from beluga.utils import keyboard

import numpy as np

import time
import socket
try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

# TODO: Create py test for worker class
# TODO: Add multithreading
# TODO: Add TCP support
# TODO: Give worker class all functionality of the framework.
class Worker(object):
    def __init__(self, mode='MPI', propagator=Propagator()):
        # Worker process runs on a single node. Use all available CPUs.
        # TODO: Take control and make use of GPUs as well
        self.process_count = os.cpu_count()
        self.mode = mode

        # Create propagator class. Propagator handles local pooling
        self.Propagator = propagator
        self.Propagator.startPool()

        # Get tags for commands between nodes.
        self.tagtocommand = self.getTags()
        self.commandtotag = self.getCommands()

        # Determine mode the worker process is started in.
            # HOST: This is the main process or head node. This is the same node that runs the main solution process.
            # MPI: Slave nodes. They will sit idle until some operation is sent by the HOST worker.
            # TCP: Slave nodes. Behaves similarly to MPI process, but will listen on a TCP port instead of MPI.
        if self.mode == 'HOST':
            self.rank = 0
            self.comm = MPI.COMM_WORLD
            self.rank = self.comm.Get_rank()
            self.send = self.sendMPI
        elif self.mode == 'MPI':
            self.comm = MPI.COMM_WORLD
            self.rank = self.comm.Get_rank()
            self.send = self.sendMPI
            if self.rank == 0:
                self.mode = 'HOST'
        elif self.mode == 'TCP':
            self.send = self.sendTCP
            raise Exception('TCP mode not yet implemented. Start worker process in MPI mode.')
        elif self.mode == 'DUAL':
            raise Exception('DUAL mode not yet implemented. Start worker process in MPI mode.')

        # Start with no jobs in queue
        self.tasklist = []

        # Default to not running on init
        self.started = 0

    def startWorker(self):
        self.wprint('Worker process started in ' + self.mode + ' mode. Rank: ' + str(self.rank))
        self.started = 1
        if self.mode == 'HOST':
            for i in range(10):
                self.comm.send(10,dest=1,tag=self.commandtotag['TEST'])
                self.wprint('Sent to 1')
                time.sleep(1)
                #self.comm.send(10,dest=1,tag=self.commandtotag['TEST'])
                #self.wprint('Sent to all')
                #time.sleep(1)
            for i in range(self.comm.size-1):
                self.comm.send(0,dest=i+1,tag=self.commandtotag['STOPWORKER'])
        elif self.mode == 'MPI':
            self.listenMPI()
        else:
            return None

    def listenMPI(self):
        # Listen over MPI
        if self.mode == 'HOST':
            data = self.comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
            return data
        elif self.mode == 'MPI':
            while self.started:
                # Receive some data from the head node
                status = MPI.Status()  # get MPI status object. Does this need to be inside the loop?
                data = self.comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)

                PID = os.fork()
                self.wprint('Forked')
                if PID == 0:
                    self.wprint('Child PID: ' + str(PID))
                    os._exit(0)
                else:
                    self.wprint('Parent PID: ' + str(os.getpid()) + ' Child PID: ' + str(PID))

                respond,data = self.parseInput(data,status.Get_source(),status.Get_tag(),status)
                if respond == 1:
                    # Respond to the node with some information
                    self.sendMPI(data,destination=status.Get_source(),tag=self.commandtotag['RESPONSE'])

    def listenTCP(self):
        # Probably listen on a TCP port or something.
        return None

    def sendMPI(self,data,destination=0,tag=0):
        if destination == 'BROADCAST':
            for i in range(self.comm.size):
                self.comm.send(data,dest=i,tag=tag)
                self.wprint('BROADCAST not yet implemented.')
        else:
            self.comm.send(data,dest=destination,tag=tag)

        return None

    def sendTCP(self):
        return None

    def parseInput(self,data,source,tag,status):
        command = self.tagtocommand[tag]
        responseRequired = 1

        if command == 'TEST':
            self.wprint('Received...')
            time.sleep(2)
            self.wprint('Processed')
        elif command == 'RESULT':
            # Result from a computation
            responseRequired = 0
        elif command == 'RESPONSE':
            # Result from a command
            responseRequired = 0
        elif command == 'STARTWORKER':
            self.startWorker()
        elif command == 'STOPWORKER':
            self.stopWorker()
        elif command == 'PARSEFAILED':
            # Resend command? IDK
            return None
        elif command == 'SETDERIVATIVE':
            self.deriv_func = data
        elif command == 'SETBCFUNC':
            self.bc_func = data
        elif command == 'PROPAGATE':
            t,y = self.Propagator.solve(data)
            self.send((t,y),destination=source,tag='RESULT')

        return responseRequired,data

    def solve(self, problem, *args, **kwargs):
        # Generic solve method.
        return None

    def stopWorker(self):
        self.wprint('Worker process closed. Rank: ' + str(self.rank))
        self.started = 0
        return None

    def getTags(self):
        # Known commands by the worker. Additional commands should be added to this list.
        commands = ['TEST','RESULT','RESPONSE','STARTWORKER','STOPWORKER','PARSEFAILED','SETDERIVATIVE','SETBCFUNC','PROPAGATE']
        return dict(enumerate(commands))

    def getCommands(self):
        # Inverts the command list
        taglist = self.getTags()
        return dict(zip(taglist.values(), taglist.keys()))

    def wprint(self,message):
        print('(Worker ' + str(self.rank) + ') ' + str(message))

# TODO: Implement a queue system
class WorkerTask(object):
    def __init__(self,data,source=0,destination=1,tag=0,command='PROPAGATE'):
        self.data = data
        self.source = source
        self.destination = destination
        self.tag = tag
        self.command = command