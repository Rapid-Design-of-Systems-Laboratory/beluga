from sandbox.inputFile import inputs
from optim.necessary_conditions import compute_necessary_conditions
from utils import *
from bvpsol import FunctionTemplate
import matplotlib.pyplot as plt
import numpy as np
from math import *
from bvpsol.algorithms import SingleShooting#, ScikitsBVPSolver
import bvpsol as bs
from continuation import *

import sys, os, imp
sys.path.append(os.getcwd()+'/../')

# from optim import *

# from necessary_conditions import compute_necessary_conditions
# import pdb

def run_optim():
    
    # Read from input file
    problem = inputs()
    
    # Perform necessary conditions calculations
    nec_cond = compute_necessary_conditions(problem)
    
    
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
    for i in range(len(problem.control)):
        for j in range(len(nec_cond.ctrl_free)):  
            control_options.append([{'name':problem.control[i].var,'expr':nec_cond.ctrl_free[j]}])
    
    problem_data = {
    'aux_list': [
            {
            'type' : 'const',
            'vars': [problem.constant[i].var for i in range(len(problem.constant))]
            },
            {
            'type' : 'constraint',
            'vars': []
            }
     ],
     'state_list': 
         [problem.state[i].state_var for i in range(len(problem.state))] + 
         [nec_cond.costate[i] for i in range(len(nec_cond.costate))] + 
         ['tf']
     ,
     'deriv_list':
         ['tf*(' + problem.state[i].process_eqn + ')' for i in range(len(problem.state))] + 
         ['tf*(' + nec_cond.costate_rate[i] + ')' for i in range(len(nec_cond.costate_rate))] + 
         ['tf*0']
     ,
     'num_states': 2*len(problem.state) + 1,
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
     'control_list':[problem.control[i].var for i in range(len(problem.control))],
     'ham_expr':nec_cond.ham
    }
#    problem.constraint[i].expr for i in range(len(problem.constraint))
    
    
    # Create problem functions by importing from templates
    problem_mod = imp.new_module('brachisto_prob')
    FunctionTemplate.compile('../bvpsol/templates/deriv_func.tmpl.py',problem_data,problem_mod)
    FunctionTemplate.compile('../bvpsol/templates/bc_func.tmpl.py',problem_data,problem_mod)
    FunctionTemplate.compile('../bvpsol/templates/compute_control.tmpl.py',problem_data,problem_mod)    
    
    
    
    
    solinit = bs.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
    bvp = bs.Problem(problem_mod.deriv_func,problem_mod.bc_func,
                                    states = ['x','y','v','lamX','lamY','lamV','tf'],
                                    initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                                    terminal_bc = {'x':0.1, 'y':-0.1}, 
                                    const = {'g':9.81},
                                    constraint = {}
                                    )
    
    solver = SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)
    # solver = ScikitsBVPSolver(num_left_boundary_conditions = 3)
    
    
    # step1 will actually be loaded from an array of continuation steps
    step1 = ContinuationStep()
    # 10 seconds for 100 in 5 steps
    # 20 seconds for 100 in 25 steps
    # 3 seconds for 100 in 2 steps
    step1.num_cases = 2
    step1.terminal('x',20.0)
    step1.terminal('y',-20.0)
    
    step1.set_bvp(bvp)
    step1.reset();
    
    print('\nRunning continuation set 1:')
    sol_last = solinit
    total_time = 0.0;
    plt.clf()
    while not step1.complete():
        print('Starting iteration '+str(step1.ctr+1)+'/'+str(step1.num_cases))
        tic()
        bvp = step1.next()
        sol = solver.solve(bvp,sol_last)
        
        # Update solution for next iteration
        sol_last = sol
        elapsed_time = toc()
        total_time  += elapsed_time
        print('Iteration %d/%d converged in %0.4f seconds\n' % (step1.ctr, step1.num_cases, elapsed_time))
        
        plt.plot(sol.y[0,:], sol.y[1,:],'-')
    
    print('Continuation process completed in %0.4f seconds.\n' % total_time)
    ################################################################
    
    plt.title('Solution for Brachistochrone problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show(block=False)