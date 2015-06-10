import sys, os, imp
sys.path.append(os.getcwd()+'/../')

problem_data = {
    'aux_list': [
            {
            'type' : 'const',
            'vars': ['g']
            },
            {
            'type' : 'constraint',
            'vars': []
            }
     ],
     'state_list': [
         'x','y','v','lamX','lamY','lamV','tf'
     ],
     'deriv_list':[
         'tf*v*cos(thetta)',
         'tf*v*sin(thetta)',
         'tf*g*sin(thetta)',
         'tf*0',
         'tf*0',
         '-tf*(lamX*cos(thetta) + lamY*sin(thetta))',
         'tf*0'
     ],
     'num_states': 7,
     'left_bc_list':[
         "x - _x0['x']", # x(0)
         "y - _x0['y']", # y(0)
         "v - _x0['v']"  # v(0)
     ],
     'right_bc_list':[
         "x - _xf['x']", # x(tf)
         "y - _xf['y']", # y(tf)
         "lamV + 0.0",      # lamV(tf)
         "_H     - 0",        # H(tf)
     ],
     'control_options':[
         [{'name':'thetta','expr':'-acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))'}],
         [{'name':'thetta','expr':' acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))'}],
         [{'name':'thetta','expr':'-acos( ((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))'}],
         [{'name':'thetta','expr':' acos( ((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))'}]
     ],
     'control_list':['thetta'],
     'ham_expr':'lamX*v*cos(thetta) + g*lamV*sin(thetta) + lamY*v*sin(thetta) + 1'
}
from bvpsol import FunctionTemplate
problem_mod = imp.new_module('brachisto_prob')  # Customize this

FunctionTemplate.compile('../bvpsol/templates/deriv_func.tmpl.py',problem_data,problem_mod)
FunctionTemplate.compile('../bvpsol/templates/bc_func.tmpl.py',problem_data,problem_mod)
FunctionTemplate.compile('../bvpsol/templates/compute_control.tmpl.py',problem_data,problem_mod)




########################################
#
#       Same as brachisto.py below
#
########################################

import bvpsol
import numpy as np
from math import *
from bvpsol.algorithms import SingleShooting#, ScikitsBVPSolver
import matplotlib.pyplot as plt
from utils import *

solinit = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])


solver = SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)
# solver = ScikitsBVPSolver(num_left_boundary_conditions = 3)

################################################################
#           Stuff in the input file                            #
################################################################
from continuation import *
def run_continuation():
    bvp = bvpsol.BVP(problem_mod.deriv_func,problem_mod.bc_func,
                                    initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                                    terminal_bc = {'x':0.1, 'y':-0.1},
                                    const = {'g':-9.81},
                                    constraint = {}
                    )

    # step1 will actually be loaded from an array of continuation steps
    step1 = ContinuationStep()
    # 10 seconds for 100 in 5 steps
    # 20 seconds for 100 in 25 steps
    # 3 seconds for 100 in 2 steps
    step1.num_cases = 2
    step1.terminal('x',100.0)
    step1.terminal('y',-100.0)

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
        # p.line(sol.y[0,:], sol.y[1,:], line_width=2, color=tuple(x*255 for x in RGB_tuples[step1.ctr-1]))

    print('Continuation process completed in %0.4f seconds.\n' % total_time)
    ###############################################################
    # show(p)   # For bokeh
    plt.title('Solution for Brachistochrone problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show(block=False)

run_continuation()
