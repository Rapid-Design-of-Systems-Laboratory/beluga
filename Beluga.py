from utils import *
from math import *
from optim import *
import bvpsol

import matplotlib.pyplot as plt
import numpy as np
import imp

from continuation import *
class Beluga(object):
    
    def __init__(self,problem):
        self.problem = problem

    @classmethod
    def run(cls,problem):
        """Takes a problem statement, instantiates a solver object and begins 
        the solution process
           
        Returns: 
            Beluga object
        """
        inst = cls(problem) # Create instance of Beluga class
        inst.solve()
        return inst
        
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
        solinit = self.problem.guess
        bvp.set_guess(solinit)
        
        tic()
        # TODO: Start from specific step for restart capability
        # TODO: Make class to store result from continuation set?
        self.out = self.run_continuation_set(self.problem.steps, bvp)
        total_time = toc();
        
        print('Continuation process completed in %0.4f seconds.\n' % total_time)

        ################################################################
        # Save the whole "self" object at this point?

        plt.title('Solution for Brachistochrone problem')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show(block=False)
        
    # TODO: Refactor how code deals with initial guess
    def run_continuation_set(self,steps,bvp):
        # Loop through all the continuation steps
        for step_idx,step in enumerate(steps):
            # Assign BVP from last continuation set
            step.reset();

            print('\nRunning continuation step '+str(step_idx+1)+' : ')
            solution_set = []
            solution_set.append(ContinuationSolution())
            if step_idx == 0:
                step.set_bvp(bvp)
                sol_last = bvp.guess
            else:
                # Use the bvp & solution from last continuation set
                sol_last = solution_set[step_idx-1][-1]
                step.set_bvp(steps[step_idx-1].bvp)
                
            while not step.complete():
                print('Starting iteration '+str(step.ctr+1)+'/'+str(step.num_cases()))
                tic()
                bvp.set_guess(sol_last)
                bvp = step.next()
                sol = self.problem.bvp_solver.solve(bvp)
    
                # Update solution for next iteration
                sol_last = sol
                solution_set[step_idx].append(sol)
                
                elapsed_time = toc()
                # total_time  += elapsed_time
                print('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))    
                plt.plot(sol.y[0,:], sol.y[1,:],'-')

            print('Done.\n')
        