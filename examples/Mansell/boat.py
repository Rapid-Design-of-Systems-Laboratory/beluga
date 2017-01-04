#==================================================================================
# PROGRAM: "boat.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: simple path optimization for a boat with bounded control used
#              to demonstrate graph search continuation.
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

def get_problem():

    """A simple example of graph search continuation"""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('boat')

    #Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x','V*cos(hdg)','m')  \
           .state('y','V*sin(hdg)','m') \
           .state('hdg','hdgdot','rad')
#           .state('hdg','cmax/V*sin(hdgA)','rad')

    # Define controls
#    problem.control('hdgA','rad')
    problem.control('hdgdot','rad/s')

    problem.mode = 'analytic'

    # Define Cost Functional
    problem.cost['path'] =  Expression('1', 's')

    #Define constraints
    problem.constraints().initial('x-x_0','m') \
                         .initial('y-y_0','m') \
                         .initial('hdg-hdg_0','rad') \
                         .terminal('x-x_f','m') \
                         .terminal('y-y_f','m') \
                         .path('hdgdotLim','hdgdot/hdgdmax','<',1,'rad')

    #Define constants
    problem.constant('cmax',1.0,'m/s^2') #Maximum allowed centripetal acceleration
    problem.constant('V',1,'m/s') #Velocity
    #problem.constant('eps',0.1,'m/rad') #Error constant
    #problem.constant('y_f',0.0,'m')
    problem.constant('hdgdmax',1,'rad/s')

    #Problem scaling
    problem.scale.unit('m',1) \
                 .unit('s',1) \
                 .unit('rad',1)

    #Configure solver
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False,number_arcs=4)

    #Initial Guess....................x0..y0..hdg0
    problem.guess.setup('auto',start=[0.0,0.0,0.0])

    #Add Continuation Steps
    problem.steps.add_step().num_cases(3) \
                            .terminal('x', 1) \
                            .terminal('y', 0.0)

    return problem


if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
