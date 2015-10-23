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

# Known commands for networking. To create a new command, add the name here and add it's function in the 'handleInput' method.
COMMANDS = ['DO_NOTHING','TEST','PING','RESPONSE','WORKER_STATE','TICKET','RESULT','START_WORKER','STOP_WORKER','PARSE_FAILED',
            'SET_DERIVATIVE','SET_BCFUNC','PROPAGATE']

# TODO: Create py test for Worker class
# TODO: Add TCP support
# TODO: Give worker class all functionality of the framework.
# TODO: Take control and make use of GPUs
class Worker(object):
    """!
    \brief     Main class of worker process.
    \details   This class handles everything related to multiple processor and multiple node processing.
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
            self.data = {}
            if HPCSUPPORTED:
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
        self.tasklist = {}

        # Default to not running on init
        self.started = 0

        # Starting point for tickets
        self.tickmin = 0

    def startWorker(self):
        if HPCSUPPORTED:
            self.wprint('Worker process started in ' + self.mode + ' mode. Rank: ' + str(self.rank))
            self.started = 1
            if self.mode == 'HOST':
                PID = os.fork()
                if PID == 0:
                    # Child thread. Listens over network.
                    self.listenMPI() # This will need to change to reflect other modes, fine for just MPI stuff
                else:
                    # Parent thread. Head back to main process.
                    return None

            elif self.mode == 'MPI':
                self.listenMPI()
            else:
                return None
        else:
            self.wprint('Bypassing MPI support. Worker will only use local pool.')

    def stopWorker(self):
        self.wprint('Worker process closing... Rank: ' + str(self.rank))
        self.started = 0
        if HPCSUPPORTED == 0:
            self.Propagator.closePool()
        return None

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
                # TODO: Fix this garbled mess
                if self.tagtocommand[status.Get_tag()] is not 'STOP_WORKER':
                    PID = os.fork()
                else:
                    PID = 0

                if PID == 0:
                    # Child thread to handle processing.
                    responseDestination,responseData,responseType = self.handleInput(data,status.Get_source(),status.Get_tag(),status)
                    if responseDestination == -1:
                        # Respond to the node with some information
                        self.sendMPI(responseData,destination=status.Get_source(),tag=self.commandtotag[responseType])
                    elif responseDestination == -2:
                        # TODO: Implement scattered messages
                        # Respond to all nodes with some information
                        self.sendMPI(responseData,destination=status.Get_source(),tag=self.commandtotag[responseType])
                    elif responseDestination >= 0:
                        # Respond to all nodes with some information
                        self.sendMPI(responseData,destination=responseDestination,tag=self.commandtotag[responseType])

                    # Terminate child process
                    os._exit(0)
                else:
                    # Parent thread. Go back to listening
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
            # None - No response sent.
            # -1 - Response sent to source. "Return to Sender"
            # -2 - Response broadcasted to comm world.
            # 0+ - Response sent to specified rank.
        responseDestination = None

        # Data sent to other nodes. Default to nothing.
        responseData = None

        # Command sent with response message. Default to nothing.
        responseType = 'DO_NOTHING'

        if command == 'DO_NOTHING':
            # Okay...
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'TEST':
            # Testing command for whatever. Change this to test out new commands or functions. Code breaking stuff
            # here shouldn't affect the overall solution process. Use 'self.wprint()' to print to the command window.
            self.wprint('Received...')
            time.sleep(2)
            self.wprint('Processed')
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'WORKER_STATE':
            # State signal from another node. This tells us that another node has started and is ready for work.
                # 0 - Default. Worker node not started.
                # 1 - Worker node started, but busy with other computations.
                # 2 - Worker node started and free.

            # TODO: Implement how nodes keep track of each other.

            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'PING':
            # Generic ping command. Send response back.
            responseDestination = -1
            responseData = None
            responseType = 'RESPONSE'

        elif command == 'RESPONSE':
            # Response from a ping
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'TICKET':
            # Job ticket from another node. Probably don't need this as it will be handled locally.
            # TODO: Why did I write down that nodes are passing tickets to each other?
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'RESULT':
            # Result from a computation
            # TODO: Add data to corresponding ticket in queue
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'START_WORKER':
            # Command to start the worker.
            # TODO: If a worker hasn't started, how can it receive a signal? Figure out a better solution to this paradox
            self.startWorker()
            responseDestination = -2
            responseData = 2 # Tell every other worker this node has started
            responseType = 'WORKER_STATE'

        elif command == 'STOP_WORKER':
            # Command to stop the worker, close the pool, and terminate the script.
            self.stopWorker()
            responseDestination = None
            responseData = None # Tell every other worker this node one has closed
            responseType = 'DO_NOTHING'

        elif command == 'PARSE_FAILED':
            # Resend command? IDK
            self.wprint('Something went wrong here')
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'
            return None

        elif command == 'SET_DERIVATIVE':
            # Sets derivative for propagation. Minimizes amount of network communication.
            self.deriv_func = data
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'SET_BCFUNC':
            # Sets boundary condition function. Minimizes amount of network communication.
            self.bc_func = data
            responseDestination = None
            responseData = None
            responseType = 'DO_NOTHING'

        elif command == 'PROPAGATE':
            # Propagate differential equations based on initial state.
            t,y = self.Propagator.solve(data)
            # self.send((t,y),destination=source,tag='RESULT')
            responseDestination = -1
            responseData = (t,y)
            responseType = 'RESULT'

        else:
            # Unknown command. Send a failed response
            responseDestination = -1
            responseData = None
            responseType = 'PARSE_FAILED'
            self.wprint('Unknown tag: ' + str(tag))

        return responseDestination,responseData,responseType

    def solve_asynch(self, inputdata, command='PROPAGATE', *args, **kwargs):
        # Generic asynchronous solve method.
        # TODO: Make a more sophisticated system for choosing an open node.
        ticket = self.genTicket()
        newTask = WorkerTask(inputdata=inputdata,source=self.rank,destination=1,tag=self.commandtotag[command],command=command,ticket=ticket)
        self.tasklist[ticket] = newTask
        return ticket

    def solve_synch(self, problem, *args, **kwargs):
        # Generic synchronous solve method
        return None

    def getResult(self, ticket):
        task = self.tasklist[ticket]
        if task.outputdata == 'UNDEFINED':
            self.sendMPI(data='NONE',destination=task.destination,tag=self.commandtotag['PING'])


    def getTags(self):
        return dict(enumerate(COMMANDS))

    def getCommands(self):
        # Inverts the command list
        taglist = self.getTags()
        return dict(zip(taglist.values(), taglist.keys()))

    def genTicket(self):
        ticket = self.tickmin
        self.tickmin = self.tickmin + 1
        return ticket

    def wprint(self,message):
        # Prints to the main window adding on which worker sent the message.
        print('(Worker ' + str(self.rank) + ') ' + str(message))

    # TODO: Check for zombie threads. This should take care of it but they are zombies.
    def reaper(self, signum, frame):
        pid, status = os.wait()

    def getAWorker(self):
        return None

    def clearWorkerMemory(self):
        return None

# TODO: Implement a queue system
# TODO: See if we can just pass the tasks around
# Worker task object keeps track of jobs sent/received for easy data management and retrieval
class WorkerTask(object):
    def __init__(self,inputdata='UNDEFINED',source=0,destination=1,tag=0,command='PROPAGATE',ticket=0):
        self.inputdata = inputdata
        self.outputdata = 'UNDEFINED'
        self.source = source
        self.destination = destination
        self.tag = tag
        self.command = command
        self.ticket = ticket
        self.sent = 0

# Worker node object keeps track of connected nodes to the workers. Allows new jobs to be sent to free workers.
# TODO: Implement worker node object for dynamic tracking of connected nodes
class WorkerNode(object):
    def __init__(self):
        self.rank = 50