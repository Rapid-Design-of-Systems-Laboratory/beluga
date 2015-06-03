from math import *
from beluga.utils import *
from beluga.optim import *

import matplotlib.pyplot as plt
import numpy as np
import sys,os,imp

from beluga import BelugaConfig
from beluga.continuation import *

import dill

class Beluga(object):
    version = '0.1'

    config = BelugaConfig().config # class variable globally accessible
    def __init__(self,problem):
        self.problem = problem

    @classmethod
    def run(cls,problem):
        """Takes a problem statement, instantiates a solver object and begins
        the solution process

        Returns:
            Beluga object
        """
        sys.path.append(cls.config['root'])
        if isinstance(problem,Problem):
            inst = cls(problem) # Create instance of Beluga class
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
        nec_cond = NecessaryConditions(self.problem)

        # Determine order that controls should be computed

    # 	% Determine control write order to function. Select expression with fewest control variables first.
    # 	controlsInExpression = zeros(1,oc.num.controls);
    # 	for ctrExpression = 1 : 1 : oc.num.controls
    # 	for ctrControl = 1 : 1 : oc.num.controls
    #
    # 		if ~isempty(strfind(char(oc.control.unconstrained.expression{ctrExpression}(1)),char(oc.control.var(ctrControl))))
    # 			controlsInExpression(ctrExpression) = controlsInExpression(ctrExpression) + 1;
    # 		end
    #
    # 	end
    # 	end
    #
    # 	% Sort controls starting with those with fewest appearances in control equations
    # 	[~,oc.control.unconstrained.writeOrder] = sort(controlsInExpression);

    #    keyboard()

        # TODO: Implement other types of initial guess depending on data type
        #       Array: Automatic?
        #       Guess object: Directly use
        #       Function handle: Call function
        #       String: Load file?
        bvp = nec_cond.get_bvp()
        # solinit = self.problem.guess
        solinit = self.problem.guess.generate(bvp)

        # includes costates
        state_names = nec_cond.problem_data['state_list']
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

        # Save data
        output = open('data.dill', 'wb')
        dill.dump(self, output) # Dill Beluga object only
        output.close()

    # TODO: Refactor how code deals with initial guess
    def run_continuation_set(self,steps,bvp,guess):
        # Loop through all the continuation steps
        solution_set = []
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
                # bvp = step.next()
                sol = self.problem.bvp_solver.solve(bvp, sol_last)

                # Update solution for next iteration
                sol_last = sol
                solution_set[step_idx].append(sol)

                elapsed_time = toc()
                # total_time  += elapsed_time
                print('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                plt.plot(sol.y[0,:], sol.y[1,:],'-')

            print('Done.')
        return solution_set
