from beluga.utils.propagators import *
from beluga.utils.joblib import Parallel, delayed
from beluga.utils.joblib import pool
import os
from beluga.utils import Propagator
import signal
from beluga.utils import keyboard

import numpy as np

import time
import socket
try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

# Known commands for networking. To create a new command, add the name here and add it's function in the 'parseInput' method.
COMMANDS = ['TEST','READY','TICKET','RESULT','RESPONSE','STARTWORKER','STOPWORKER','PARSEFAILED','SETDERIVATIVE','SETBCFUNC','PROPAGATE']

# TODO: Create py test for worker class
# TODO: Add TCP support
# TODO: Give worker class all functionality of the framework.
# TODO: Take control and make use of GPUs
class Worker(object):
    """!
    \brief     Main class of worker process.
    \details   This class handles everything related to multiple node processing.
    \author    Mike Sparapany
    \version   0.1
    \date      08/08/15
    """



    def __init__(self, mode='MPI', propagator=Propagator()):
        # Worker process runs on a single node. Use all available CPUs.
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
            self.data = {}
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
            self.listenMPI() # This will need to change to reflect other modes, fine for just MPI stuff
            PID = os.fork()
            if PID == 0:
                self.listenMPI()

        elif self.mode == 'MPI':
            self.listenMPI()
        else:
            return None

    def sendJob(self,command,*args,**kwargs):
        ticket = 50
        return ticket

    def getResult(self,ticket):
        return data

    def listenMPI(self):
        # Listen over MPI
        if self.mode == 'HOST':
            data = self.comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
            return data

        elif self.mode == 'MPI':
            signal.signal(signal.SIGCHLD, self.reaper)
            while self.started:
                # Receive some data from another node
                status = MPI.Status()  # get MPI status object. Does this need to be inside the loop?
                data = self.comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)

                # Fork the thread to handle calculations and communication concurrently
                PID = os.fork()
                self.wprint('Forked')
                if PID == 0:
                    # Child thread to handle processing.
                    responseRequired,responseData,responseType = self.handleInput(data,status.Get_source(),status.Get_tag(),status)
                    if responseRequired == 1:
                        # Respond to the node with some information
                        self.sendMPI(responseData,destination=status.Get_source(),tag=self.commandtotag[responseType])
                    os._exit(0)
                else:
                    self.wprint('Parent PID: ' + str(os.getpid()) + ' Child PID: ' + str(PID))



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

    def handleInput(self,data,source,tag,status):
        # Determine the command from the pinging node.
        command = self.tagtocommand[tag]

        # Default to not sending a response to the pinging node.
        responseRequired = 0

        if command == 'TEST':
            # Testing command for whatever. Change this to test out new commands or functions. Code breaking stuff
            # here shouldn't affect the overall solution process.
            self.wprint('Received...')
            time.sleep(2)
            self.wprint('Processed')

        elif command == 'READY':
            # Ready signal from another node. This tells us that another node has started and is ready for work. Only
            # the HOST node should receive ready signals.
            self.slave[data].isReady = 1

        elif command == 'TICKET':
            return None

        elif command == 'RESULT':
            # Result from a computation
            responseRequired = 0

        elif command == 'RESPONSE':
            # Result from a command
            responseRequired = 0

        elif command == 'STARTWORKER':
            # Command to start the worker.
            # TODO: If a worker hasn't started, how can it receive a signal? Figure out a better solution to this paradox
            self.startWorker()

        elif command == 'STOPWORKER':
            # Command to stop the worker, close the pool, and terminate the script.
            self.stopWorker()

        elif command == 'PARSEFAILED':
            # Resend command? IDK
            self.wprint('Something went wrong here')
            return None

        elif command == 'SETDERIVATIVE':
            # Sets derivative for propagation. Minimizes amount of network communication.
            self.deriv_func = data

        elif command == 'SETBCFUNC':
            # Sets boundary condition function. Minimizes amount of network communication.
            self.bc_func = data

        elif command == 'PROPAGATE':
            # Propagate differential equations based on initial state.
            t,y = self.Propagator.solve(data)
            self.send((t,y),destination=source,tag='RESULT')
            responseRequired = 0
            responseData = (t,y)
            responseType = 'RESULT'

        else:
            # Unknown command. Send a failed response
            responseRequired = 1
            responseData = None
            responseType = 'PARSEFAILED'
            self.wprint('Unknown tag: ' + str(tag))

        return responseRequired,responseData,responseType

    def solve(self, problem, *args, **kwargs):
        # Generic solve method.
        return None

    def stopWorker(self):
        self.wprint('Worker process closed. Rank: ' + str(self.rank))
        self.started = 0
        return None

    def getTags(self):
        # Known commands by the worker. Additional commands should be added to this list.
        return dict(enumerate(COMMANDS))

    def getCommands(self):
        # Inverts the command list
        taglist = self.getTags()
        return dict(zip(taglist.values(), taglist.keys()))

    def wprint(self,message):
        # Prints to the main window adding on which worker sent the message.
        print('(Worker ' + str(self.rank) + ') ' + str(message))

    def reaper(self, signum, frame):
        pid, status = os.wait()
        print(
            'Child {pid} terminated with status {status}'
            '\n'.format(pid=pid, status=status)
            )

    def getAWorker(self):
        return None

# TODO: Implement a queue system
class WorkerTask(object):
    def __init__(self,data,source=0,destination=1,tag=0,command='PROPAGATE'):
        self.data = data
        self.source = source
        self.destination = destination
        self.tag = tag
        self.command = command