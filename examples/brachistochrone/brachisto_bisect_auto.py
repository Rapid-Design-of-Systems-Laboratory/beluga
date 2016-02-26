import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *

def get_problem():
    """Brachistochrone example."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('brachisto')

    # Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x', 'v*cos(theta)','m')   \
           .state('y', '-v*sin(theta)','m')   \
           .state('v', 'g*sin(theta)','m/s')
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
    # problem.constraints().interior_point('(x-x1)^2+(y-y1)^2','m^2')

    # Define constants (change to have units as well)
    problem.constant('g','9.81','m/s^2')
    # problem.constant('x1','7.5','m')
    # problem.constant('y1','-15','m')

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # TODO: Implement this
    problem.quantity = [Value('tanAng','tan(theta)')]

    problem.scale.unit('m','x')     \
                   .unit('s','x/v')\
                   .unit('kg',1)   \
                   .unit('rad',1)

    # problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False, number_arcs=4)
    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=50, verbose = True, cached=False)
    # problem.bvp_solver = algorithms.BroydenShooting(tolerance=1e-4, max_iterations=1000)

    # Can be array or function handle
    # TODO: implement an "initial guess" class subclassing Solution
    # problem.guess = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
    # problem.guess.parameters = np.array([0.1,0.1,0.1,0.1,0.1])
    problem.guess.setup('auto',
                    start=[0,0,1],          # Starting values for states in order
                    direction='forward',
                    costate_guess = -0.1
                    )

    problem.steps.add_step('bisection', initial_num_cases=5) \
                    .terminal('x', 1000) \
                    .terminal('y',-1000)

    return problem

if __name__ == '__main__':
    Beluga.run(get_problem())
