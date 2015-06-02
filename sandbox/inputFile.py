import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *

"""Brachistochrone example."""

# Rename this and/or move to optim package?
problem = beluga.optim.Problem()

# Define independent variables
problem.independent('t', 's')

# Define equations of motion
problem.state('x','v*cos(theta)','m')   \
       .state('y','-v*sin(theta)','m')  \
       .state('v','g*sin(theta)','m/s')

# Define controls
problem.control('theta','rad')

# Define costs
problem.cost['path'] = Expression('1','s')

# Define constraints
problem.constraints('default',0) \
                    .initial('x-x_0','m')    \
                    .initial('y-y_0','m')    \
                    .initial('v-v_0','m/s')  \
                    .terminal('x-x_f','m')   \
                    .terminal('y-y_f','m')

# Define constants (change to have units as well)
problem.constant('g','9.81','m/s^2')

# Define quantity (not implemented at present)
# Is this actually an Expression rather than a Value?
problem.quantity = [Value('tanAng','tan(theta)')]

problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True)

# Can be array or function handle
# TODO: implement an "initial guess" class subclassing Solution
# problem.guess = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
# problem.guess.parameters = np.array([0.1,0.1,0.1,0.1,0.1])
problem.guess.setup('auto',
                start=[0,0,1],  # Starting values for states in order
                direction='forward',
                costate_guess = -0.1)

# Figure out nicer way of representing this. Done?
problem.steps = ContinuationList()   # Add a reset function?

problem.steps.add_step(ContinuationStep()
                .num_cases(10)
                .terminal('x', 20.0)
                .terminal('y',-20.0))
(
problem.steps.add_step().num_cases(2)
                 .terminal('x', 30.0)
                 .terminal('y',-30.0),

problem.steps.add_step()
                .num_cases(3)
                .terminal('x', 40.0)
                .terminal('y',-40.0)
)

Beluga.run(problem)
#
