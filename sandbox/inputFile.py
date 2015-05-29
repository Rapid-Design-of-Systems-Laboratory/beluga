import sys, os, imp
import numpy as np
sys.path.append(os.getcwd()+'/../')

from problem import *
from continuation import *

import bvpsol.algorithms

from Beluga import Beluga
"""Brachistochrone example."""

# Rename this and/or move to optim package?
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

# Define quantity (not implemented at present)
# Is this actually an Expression rather than a Value?
problem.quantity = [Value('tanAng','tan(theta)')]

problem.bvp_solver = bvpsol.algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)

# Can be array or function handle
# TODO: implement an "initial guess" class subclassing Solution
problem.guess = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])

problem.steps = ContinuationSet()

# Figure out nicer way of representing this. Done?
ind = 0
problem.steps.add_step(ContinuationStep().num_cases(2)
                .terminal('x', 20.0)
                .terminal('y',-20.0))

problem.steps.add_step().num_cases(2) \
                .terminal('x', 20.0)  \
                .terminal('y',-20.0)

problem.steps.add_step() \
                .num_cases(2) \
                .terminal('x', 40.0) \
                .terminal('y',-40.0)

Beluga.run(problem)