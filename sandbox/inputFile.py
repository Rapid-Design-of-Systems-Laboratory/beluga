import sys, os, imp
sys.path.append(os.getcwd()+'/../')

from problem import *
from continuation import *

import bvpsol.algorithms
from Beluga import Beluga
"""Brachistochrone example."""
    
problem = Problem()

# Define independent variables
problem.indep_var = [Variable('t', 's')]

# Define equations of motion
problem.state = [State('t','x','v*cos(theta)','m'),
                 State('t','y','-v*sin(theta)','m'),
                 State('t','v','g*sin(theta)','m/s')]

# Define controls
problem.control = [Variable('theta','rad')]

# Define costs
problem.cost['path'] = Expression('1','s')

# Define constraints
problem.constraint = [Constraint('init','x-x_0','m'),
                      Constraint('init','y-y_0','m'),
                      Constraint('term','x-x_f','m'),
                      Constraint('term','y-y_f','m')]

# Define constants
problem.constant = [Value('g','9.81')]

# Define quantity
problem.quantity = [Value('tanAng','tan(theta)')]

problem.bvp_solver = bvpsol.algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)

problem.steps = []

# Figure out nicer way of representing this
ind = 0
problem.steps.append(ContinuationStep())
problem.steps[-1].num_cases = 2
problem.steps[-1].terminal('x',20.0)
problem.steps[-1].terminal('y',-20.0)

problem.steps.append(ContinuationStep())
problem.steps[-1].num_cases = 2
problem.steps[-1].terminal('x',40.0)
problem.steps[-1].terminal('y',-40.0)

Beluga.run(problem)