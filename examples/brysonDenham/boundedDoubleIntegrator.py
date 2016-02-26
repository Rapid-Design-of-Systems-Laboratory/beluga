import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *

def get_problem():
    """Constrained Double integrator problem ."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('brysonDenhamConstrained')

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
                        .terminal('v-v_f','m/s') \
                        .independent('tf - 1','s') # Fixed final time

    problem.scale.unit('m',1)     \
                   .unit('s',1)\
                   .unit('kg',1)   \
                   .unit('rad',1)   \
                   .unit('nd',1)

    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False)
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='csd',tolerance=1e-4, max_iterations=40, verbose = True, cached=False, number_arcs=2)


    # Smoothed path constraint
    c1   = '( x )'   # Constraint
    c1_1 = '( v )'   # First derivative
    c1_2 = '( u )'   # Second derivative
    h1_1 = '(psi1)';
    h1_2 = '(psi11*xi12)';              # xi11dot = xi12
    h1_3 = '(psi12*xi12^2 + psi11*ue1)';  # xi12dot = ue1

    problem.constant('eps1',1e-1,'nd')   # The smoothing 'penalty' factor
    problem.control('ue1','m/s')    # The extra control
    problem.constant('lim',0.20,'m')  # The constraint limit

    problem.quantity ('psi1','(lim - (2*lim/(1+exp((2/lim)*xi11))))') \
            .quantity('psi11','((4*exp((2*xi11)/lim))/(exp((2*xi11)/lim) + 1)**2)') \
            .quantity('psi12','( 8*exp(2*xi11/lim)/(lim*(exp(2*xi11/lim) + 1)**2) - 16*exp(4*xi11/lim)/(lim*(exp(2*xi11/lim) + 1)**3))') # \
            # .quantity('psi13','(16*exp(2*xi11/lim)/(lim**2*(exp(2*xi11/lim) + 1)**2) - 96*exp(4*xi11/lim)/(lim**2*(exp(2*xi11/lim) + 1)**3) + 96*exp(6*xi11/lim)/(lim**2*(exp(2*xi11/lim) + 1)**4))')

    problem.state('xi11','xi12','m')
    problem.state('xi12','ue1','m/s')
    # solve psi1 - c = 0 -> xi11_0
    # solve psi11*xi12 - c1 = 0 -> xi12_0
    problem.constraints('default',0).initial('xi11 - x_0','m') \
                                    .initial('xi12 - v_0','m/s') \
                                    .equality(c1_2+' - '+h1_3,'m/s')

    problem.cost['path'] = Expression('u^2 + eps1*(ue1^2)','m^2/s')

    problem.guess.setup('auto',
                    start=[0,0.1,0,0.1],          # Starting values for states in order
                    direction='forward',
                    costate_guess = -0.1,
                    time_integrate = 1      ## REQUIRED BECAUSE OF FIXED FINAL TIME
                    )

    # problem.steps.add_step().num_cases(11) \
    problem.steps.add_step('bisection', max_divisions=30).num_cases(51)   \
                            .terminal('x',0) \
                            .initial('v',1) \
                            .terminal('v', -1)
                            # .const('lim',0.20)
    #
    problem.steps.add_step('bisection').num_cases(11)      \
                            .const('lim',0.14)
    # #
    problem.steps.add_step('bisection').num_cases(11,spacing='log')      \
                            .const('eps1',1e-5)
    return problem

if __name__ == '__main__':
    Beluga.run(get_problem())
