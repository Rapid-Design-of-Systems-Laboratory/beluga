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
    problem = beluga.optim.Problem('boundedBrachistochrone')

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
                        .terminal('y-y_f','m')   \
                        .path('y + x','>','h0','m')  # y + x + h0 > 0 -- above the line y= -x - h0

    # problem.constraints().interior_point('(x-x1)^2+(y-y1)^2','m^2')

    # Define constants (change to have units as well)
    problem.constant('g','9.81','m/s^2')
    problem.constant('h0',-6,'m')

    # Smoothed path constraint
    # c1 = '( y + x )'                            # Constraint
    # c1_1 = '( -v*sin(theta) + v*cos(theta) )'   # First derivative

    # # Saturation function and its first derivative
    # psi1   = '(2*h0/(1+exp((2/h0)*xi11)))'
    # psi1_1 = '(-(4*exp((2*xi11)/h0))/(exp((2*xi11)/h0) + 1)^2)'
    #
    # h1_2   = '(psi1_1 * ue1)'      # Function for equality constraint

    # problem.constant('h0','3','m')
    #
    # problem.state('xi11','ue1','m')
    # problem.control('ue1','m/s')
    # problem.constraints('default',0) \
    #                     .initial('xi11-(x_0+y_0)','m') \
    #                     .equality(c1_1+' - '+h1_2,'m/s')

    # problem.quantity('psi1','(-h0 + exp(xi11))') \
    #         .quantity('psi11','(exp(xi11)*xi12)')

    problem.cost['path'] = Expression('1 + eps1*ue1^2','s')
    problem.constant('eps1',1,'s^2/m^2')    # Units to make cost non-dimensional


    problem.scale.unit('m','x')     \
                   .unit('s','x/v')\
                   .unit('kg',1)   \
                   .unit('rad',1)

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False, number_arcs=4)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False)
    # problem.bvp_solver = algorithms.BroydenShooting(tolerance=1e-4, max_iterations=1000)

    # Can be array or function handle
    # TODO: implement an "initial guess" class subclassing Solution
    # problem.guess = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])
    # problem.guess.parameters = np.array([0.1,0.1,0.1,0.1,0.1])
    problem.guess.setup('auto',
                    start=[0,0,1],          # Starting values for states in order
                    direction='forward',
                    costate_guess = 0.1
                    )

    # Figure out nicer way of representing this. Done?
    problem.steps.add_step(ContinuationStep()
                    .num_cases(11)
                    .terminal('x', 5)
                    .terminal('y',-5)
                    )
    # (
    problem.steps.add_step('bisection').num_cases(21,spacing='log') \
                     .const('eps1', 1e-6)

    problem.steps.add_step('bisection').num_cases(41)\
                    .const('h0',-1)

    # problem.steps.add_step()
    #                 .num_cases(10)
    #                 .terminal('x', 1000.0)
    #                 .terminal('y',-1000.0)
    # )
    return problem

if __name__ == '__main__':
    Beluga.run(get_problem())
