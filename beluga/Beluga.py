from math import *
from beluga.utils import *
from beluga.optim import *

import matplotlib.pyplot as plt
import numpy as np
import sys,os,imp,inspect,warnings

from beluga import BelugaConfig
from beluga.continuation import *
from beluga.bvpsol import algorithms
from beluga.utils.Worker import Worker

try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except:
    HPCSUPPORTED = 0

import dill

class Beluga(object):
    """!
    \brief     Main class of mission design tool.
    \details   This class contains all of the information associated with the
                mission design problem.
    \author    Michael Grant
    \author    Thomas Antony
    \version   0.1
    \date      06/30/15
    \pre       First create problem file.
    \copyright Coming.
    \bug       Probably exists.
    """
    # __metaclass__ = SingletonMetaClass
    version = '0.1'
    _THE_MAGIC_WORD = object()
    instance = None

    config = BelugaConfig().config # class variable globally accessible

    def __init__(self,problem,token,input_module=None):
        """!
        \brief     Initializes class of mission design tool.
        \details   Assigns problem data based on the input file.
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """
        self.problem = problem
        # self.input_module = input_module

        # # Ensure user does not create an object with the Beluga class
        # if token is not self._THE_MAGIC_WORD:
        #     raise ValueError("Don't construct directly, use create() or run()")

    @classmethod
    def run(cls,problem):
        """!
        \brief     Returns Beluga object.
        \details   Takes a problem statement, instantiates a solver object and begins
                    the solution process.
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        # Get reference to the input file module
        frm = inspect.stack()[1]
        input_module = (inspect.getmodule(frm[0]))

        # Get information about input file
        info = inspect.getframeinfo(frm[0])

        # Suppress warnings
        warnings.filterwarnings("ignore")

        # Include configuration file path
        sys.path.append(cls.config['root'])

        # TODO: Get default solver options from configuration or a defaults file
        if problem.bvp_solver is None:
            problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)

        # Set the cache directory to be in the current folder
        cache_dir = os.getcwd()+'/_cache'
        # cache_dir = os.path.dirname(info.filename)+'/_cache'
        try:
            os.mkdir(cache_dir)
        except:
            pass
        problem.bvp_solver.set_cache_dir(cache_dir)


        if isinstance(problem,Problem):
            # Create instance of Beluga class
            inst = cls(problem, cls._THE_MAGIC_WORD)
            inst.solve()
            return
            # return inst
        else:
            #TODO:Add functionality for when problem is specified by filename
            pass

    def solve(self):
        """!
        \brief     Returns Beluga object.
        \details   Starts the solution process.
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        # Initialize necessary conditions of optimality object
        print("Computing the necessary conditions of optimality")
        self.nec_cond = NecessaryConditions()

        # Create corresponding boundary value problem
        bvp = self.nec_cond.get_bvp(self.problem)

        # TODO: Implement other types of initial guess depending on data type
        #       Array: Automatic?
        #       Guess object: Directly use
        #       Function handle: Call function
        #       String: Load file?

        # The initial guess is automatically stored in the bvp object
        # solinit is just a reference to it
        solinit = self.problem.guess.generate(bvp)

        # includes costates
        state_names = self.nec_cond.problem_data['state_list']
        initial_states = solinit.y[:,0] # First column
        terminal_states = solinit.y[:,-1] # Last column
        initial_bc = dict(zip(state_names,initial_states))
        terminal_bc = dict(zip(state_names,terminal_states))
        bvp.solution.aux['initial'] = initial_bc
        bvp.solution.aux['terminal'] = terminal_bc

        tic()
        # TODO: Start from specific step for restart capability
        # TODO: Make class to store result from continuation set?
        self.out = {};
        self.out['problem_data'] = self.nec_cond.problem_data;
        self.out['solution'] = self.run_continuation_set(self.problem.steps, bvp)
        total_time = toc();

        print('Continuation process completed in %0.4f seconds.\n' % total_time)

        # Save data
        output = open('data.dill', 'wb')
        # dill.settings['recurse'] = True
        dill.dump(self.out, output) # Dill Beluga object only
        output.close()

        # plt.title('Solution for Brachistochrone problem')
        plt.xlabel('theta')
        plt.ylabel('h')
        plt.show(block=False)

    # TODO: Refactor how code deals with initial guess
    def run_continuation_set(self,steps,bvp_start):
        # Loop through all the continuation steps
        solution_set = []

        # Initialize main worker for multi processing
        # TODO: Implement the host worker in a nicer way
        if HPCSUPPORTED:
            # Start Host MPI process
            worker = Worker(mode='HOST')
            worker.startWorker()
            worker.Propagator.setSolver(solver='ode45')
        else:
            worker = None

        # Initialize scaling
        import sys, copy
        s = self.problem.scale
        s.initialize(self.problem,self.nec_cond.problem_data)

        for step_idx,step in enumerate(steps):
            # Assign BVP from last continuation set
            step.reset()
            print('\nRunning Continuation Step #'+str(step_idx+1)+' : ')

            solution_set.append(ContinuationSolution())
            if step_idx == 0:
                step.set_bvp(bvp_start)
            else:
                # Use the bvp & solution from last continuation set
                step.set_bvp(steps[step_idx-1].bvp)

            for bvp in step:
                print('Starting iteration '+str(step.ctr)+'/'+str(step.num_cases()))
                tic()

                s.compute_scaling(bvp)
                s.scale(bvp)

                # sol is just a reference to bvp.solution
                sol = self.problem.bvp_solver.solve(bvp,worker=worker)

                s.unscale(bvp)

                # Update solution for next iteration
                solution_set[step_idx].append(copy.deepcopy(bvp.solution))

                elapsed_time = toc()
                print('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                # plt.plot(sol.y[0,:], sol.y[1,:],'-')
                # plt.plot(sol_copy.y[2,:]/1000, sol_copy.y[0,:]/1000,'-')

            # plt.plot(sol.y[2,:]/1000, sol.y[0,:]/1000,'-')
            # plt.plot(sol.y[1,:]*180/pi, sol.y[0,:]/1000,'-')
            print(sol.y[:,0])
        return solution_set
