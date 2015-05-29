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
        inst = cls(problem) # Create instance of Beluga class
        inst.solve()
        return inst
        
    def solve(self):
        nec_cond = NecessaryConditions.compute(self.problem)

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

        # Create problem dictionary
        # ONLY WORKS FOR ONE CONTROL
        # NEED TO ADD BOUNDARY CONDITIONS

        control_options = []
        
        for i in range(len(self.problem.control)):
            for j in range(len(nec_cond.ctrl_free)):  
                control_options.append([{'name':self.problem.control[i].var,'expr':nec_cond.ctrl_free[j]}])

        problem_data = {
        'aux_list': [
                {
                'type' : 'const',
                'vars': [self.problem.constant[i].var for i in range(len(self.problem.constant))]
                },
                {
                'type' : 'constraint',
                'vars': []
                }
         ],
         'state_list': 
             [self.problem.state[i].state_var for i in range(len(self.problem.state))] + 
             [nec_cond.costate[i] for i in range(len(nec_cond.costate))] + 
             ['tf']
         ,
         'deriv_list':
             ['tf*(' + self.problem.state[i].process_eqn + ')' for i in range(len(self.problem.state))] + 
             ['tf*(' + nec_cond.costate_rate[i] + ')' for i in range(len(nec_cond.costate_rate))] + 
             ['tf*0']
         ,
         'num_states': 2*len(self.problem.state) + 1,
         'left_bc_list':[
             "_ya[0] - _x0['x']", # x(0
             "_ya[1] - _x0['y']", # y(0)
             "_ya[2] - _x0['v']"         
         ],
         'right_bc_list':[
             "_yb[0] - _xf['x']", # x(tf)
             "_yb[1] - _xf['y']", # y(tf)
             "_yb[5] + 0.0",   # lamV(tf)
             "_H     - 0",     # H(tf)
         ],
         'control_options': control_options
             ,
         'control_list':[self.problem.control[i].var for i in range(len(self.problem.control))],
         'ham_expr':nec_cond.ham
        }
    #    problem.constraint[i].expr for i in range(len(problem.constraint))


        # Create problem functions by importing from templates
        problem_mod = imp.new_module('brachisto_prob')
        bvpsol.FunctionTemplate.compile('../bvpsol/templates/deriv_func.tmpl.py',problem_data,problem_mod)
        bvpsol.FunctionTemplate.compile('../bvpsol/templates/bc_func.tmpl.py',problem_data,problem_mod)
        bvpsol.FunctionTemplate.compile('../bvpsol/templates/compute_control.tmpl.py',problem_data,problem_mod)    



        solinit = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
        bvp = bvpsol.Problem(problem_mod.deriv_func,problem_mod.bc_func,
                                        states = ['x','y','v','lamX','lamY','lamV','tf'],
                                        initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                                        terminal_bc = {'x':0.1, 'y':-0.1}, 
                                        const = {'g':9.81},
                                        constraint = {}
                                        )

        # TODO: Start from specific step with restart capability later
        # Loop through all the continuation steps

        # TODO: Make class to store result from continuation set?
        self.out = []   # Array to store all solutions
        total_time = 0.0;
        for step_idx,step in enumerate(self.problem.steps):
        
            step.set_bvp(bvp)
            step.reset();

            print('\nRunning continuation step '+str(step_idx+1)+' : ')
            
            self.out.append([])
            if step_idx == 0:
                sol_last = solinit
            else:
                # Use the last solution from last continuation set 
                # as the starting point
                sol_last = self.out[step_idx-1][-1]

            while not step.complete():
                print('Starting iteration '+str(step.ctr+1)+'/'+str(step.num_cases))
                tic()
                bvp = step.next()
                sol = self.problem.bvp_solver.solve(bvp,sol_last)
    
                # Update solution for next iteration
                sol_last = sol
                self.out[step_idx].append(sol)
                
                elapsed_time = toc()
                total_time  += elapsed_time
                print('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases, elapsed_time))    
                plt.plot(sol.y[0,:], sol.y[1,:],'-')

            print('Done.\n')

        print('Continuation process completed in %0.4f seconds.\n' % total_time)
        ################################################################

        plt.title('Solution for Brachistochrone problem')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show(block=False)