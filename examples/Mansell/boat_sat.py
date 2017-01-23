#==================================================================================
# PROGRAM: "boat_sat.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: simple path optimization for a boat with bounded control used
#              to demonstrate graph search continuation. Uses saturation fcns.
#==================================================================================

#Import Necessary Modules
import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *
import functools

def sat_func(u):
    cu = 1 #Upper asymptote
    cl = -1 #Lower asymptote
    s0 = 1 #smoothing factor
    return cu - (cu-cl)/(1+np.exp(4*s0/(cu-cl)*u))

def get_problem():

    """A simple example of graph search continuation"""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('boat_sat')

    #Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x','V*cos(hdg)','m')  \
           .state('y','V*sin(hdg)','m') \
           .state('hdg','k*(1-2/(1+exp(2*u)))','rad')

    # Define controls
    problem.control('u',1)
#    problem.control('hdgdot','rad/s')

    problem.mode = 'dae'

    # Define Cost Functional
    problem.cost['path'] =  Expression('1+eps*u^2', 's')

    #Define constraints
    problem.constraints().initial('x-x_0','m') \
                         .initial('y-y_0','m') \
                         .initial('hdg-hdg_0','rad') \
                         .terminal('x-x_f','m') \
                         .terminal('y-y_f','m')

    #Define constants
    problem.constant('cmax',1.0,'m/s^2') #Maximum allowed centripetal acceleration
    problem.constant('V',1,'m/s') #Velocity
    problem.constant('k',1,'rad/s')
    problem.constant('eps',1,1) #Error constant

    #Problem scaling
    problem.scale.unit('m',1) \
                 .unit('s',1) \
                 .unit('rad',1)

    #Configure solver
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False,number_arcs=16)
    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100, verbose = True, cached = False)

    #Initial Guess....................x0..y0..hdg0
    problem.guess.setup('auto',start=[0.0,0.0,0.0])

    #Add Continuation Steps
    #problem.steps.add_step().num_cases(2) \
    #                        .terminal('x', 3) \
    #                        .terminal('y', 0.1)
    problem.steps.add_step().num_cases(30) \
        .terminal('x', 3.0) \
        .terminal('y', 0)

    problem.steps.add_step().num_cases(30) \
        .terminal('x', 3.0) \
        .terminal('y', 3.0)

    return problem


if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
