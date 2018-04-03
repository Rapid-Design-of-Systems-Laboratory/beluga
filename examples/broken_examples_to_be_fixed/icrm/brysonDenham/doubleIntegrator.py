import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *

def get_problem():
    """Unconstrained Double integrator problem ."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('brysondenham')

    # Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x', 'v','m')   \
           .state('v', 'u','m/s')   \
    # Define controls
    problem.control('u','m/s')

    # Define costs
    problem.cost['path'] = Expression('u^2','m^2/s')

    # Define constraints
    problem.constraints('default',0) \
                        .initial('x-x_0','m')    \
                        .initial('v-v_0','m/s')  \
                        .terminal('x-x_f','m')   \
                        .terminal('v-v_f','m/s')

    problem.scale.unit('m','x')     \
                   .unit('s',1)\
                   .unit('kg',1)   \
                   .unit('rad',1)

    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False)
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=10000, verbose = True, cached=False, number_arcs=4)

    problem.guess.setup('auto',
                    start=[0,1],          # Starting values for states in order
                    direction='forward',
                    costate_guess = -0.1,
                    time_integrate = 1      ## REQUIRED BECAUSE OF FIXED FINAL TIME
                    )

    problem.steps.add_step().num_cases(5)   \
                            .terminal('x',0)

    problem.steps.add_step().num_cases(5)   \
                        .initial('v',1.0) \
                        .terminal('v', -1)

    return problem

if __name__ == '__main__':
    Beluga.run(get_problem())
