from math import *
from beluga.utils import *
from beluga.optim import *

import matplotlib.pyplot as plt
import numpy as np
import sys,os,imp,inspect,warnings

from beluga import BelugaConfig
from beluga.continuation import *

class Beluga(object):
    __metaclass__ = SingletonMetaClass
    version = '0.1'
    _THE_MAGIC_WORD = object()
    instance = None

    config = BelugaConfig().config # class variable globally accessible
    def __init__(self,problem,token,input_module=None):
        self.problem = problem
        self.input_module = input_module
        if token is not self._THE_MAGIC_WORD:
            raise ValueError("Don't construct directly, use create() or run()")

    @classmethod
    def run(cls,problem):
        """Takes a problem statement, instantiates a solver object and begins
        the solution process

        Returns:
            Beluga object
        """

        # Get reference to the input file module
        frm = inspect.stack()[1]
        input_module = (inspect.getmodule(frm[0]))

        # Suppress warnings

        warnings.filterwarnings("ignore")

        sys.path.append(cls.config['root'])
        if isinstance(problem,Problem):
            # Create instance of Beluga class
            inst = cls(problem, cls._THE_MAGIC_WORD,input_module = input_module)
            inst.solve()
            return inst
        else:
            #TODO:Add functionality for when problem is specified by filename
            pass

    def solve(self):
        """Starts the solution process

        Returns:
            Beluga object
        """
        self.nec_cond = NecessaryConditions(self.problem)

        # TODO: Implement other types of initial guess depending on data type
        #       Array: Automatic?
        #       Guess object: Directly use
        #       Function handle: Call function
        #       String: Load file?
        bvp = self.nec_cond.get_bvp()

        # solinit = self.problem.guess
        solinit = self.problem.guess.generate(bvp)

        # includes costates
        state_names = self.nec_cond.problem_data['state_list']
        initial_states = solinit.y[:,0] # First column
        terminal_states = solinit.y[:,-1] # Last column
        initial_bc = dict(zip(state_names,initial_states))
        terminal_bc = dict(zip(state_names,terminal_states))
        bvp.aux_vars['initial'] = initial_bc
        bvp.aux_vars['terminal'] = terminal_bc

        tic()
        # TODO: Start from specific step for restart capability
        # TODO: Make class to store result from continuation set?
        self.out = self.run_continuation_set(self.problem.steps, bvp, solinit)
        total_time = toc();

        print('Continuation process completed in %0.4f seconds.\n' % total_time)

        ################################################################
        # Save the whole "self" object at this point?
        #
        # plt.title('Solution for Brachistochrone problem')
        plt.xlabel('theta')
        plt.ylabel('h')
        plt.show(block=False)

    # TODO: Refactor how code deals with initial guess
    def run_continuation_set(self,steps,bvp,guess):
        # Loop through all the continuation steps
        solution_set = []

        # Initialize scaling
        import sys
        # from beluga.optim import Scaling
        # s = Scaling()
        # s.unit('m',80000)
        # s.unit('s',80000/6000)
        # s.unit('kg','mass')
        # s.unit('rad',1)
        s = self.problem.scale
        s.initialize(self.nec_cond)

        for step_idx,step in enumerate(steps):
            # Assign BVP from last continuation set
            step.reset();
            print('\nRunning Continuation Step #'+str(step_idx+1)+' : ')

            solution_set.append(ContinuationSolution())
            if step_idx == 0:
                step.set_bvp(bvp)
                sol_last = guess
            else:
                # Use the bvp & solution from last continuation set
                sol_last = solution_set[step_idx-1][-1]
                step.set_bvp(steps[step_idx-1].bvp)

            for bvp in step:
                print('Starting iteration '+str(step.ctr)+'/'+str(step.num_cases()))
                tic()

                import copy
                s.compute_scaling(bvp,sol_last)

                s.scale(bvp,sol_last)

                sol = self.problem.bvp_solver.solve(bvp, sol_last)

                # bvp_copy = copy.deepcopy(bvp)
                sol_copy = copy.deepcopy(sol)
                s.unscale(bvp,sol_copy)

                # Update solution for next iteration
                sol_last = sol_copy
                solution_set[step_idx].append(sol_copy)

                elapsed_time = toc()
                # total_time  += elapsed_time
                print('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                # plt.plot(sol.y[0,:], sol.y[1,:],'-')
                # plt.plot(sol_copy.y[2,:]/1000, sol_copy.y[0,:]/1000,'-')

            # plt.plot(sol_copy.y[2,:]/1000, sol_copy.y[0,:]/1000,'-')
            plt.plot(sol_copy.y[1,:]*180/pi, sol_copy.y[0,:]/1000,'-')
            print('Done.')
        return solution_set
