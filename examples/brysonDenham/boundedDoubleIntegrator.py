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
                        .terminal('v-v_f','m/s')

    problem.scale.unit('m',1)     \
                   .unit('s',1)\
                   .unit('kg',1)   \
                   .unit('rad',1)   \
                   .unit('nd',1)

    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False)
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=10000, verbose = True, cached=False, number_arcs=2)


    # Smoothed path constraint
    c1 = '( x )'                            # Constraint
    c1_1 = '( v )'   # First derivative
    c1_2 = '( u )'   # Second derivative
    h1_1 = '(psi1)';
    h1_2 = '(psi11*xi12)';              # xi11dot = xi12
    h1_3 = '(psi12*xi12^2 + psi11*ue1)';  # xi12dot = ue1

    problem.constant('eps1',1e-1,'nd')   # The smoothing 'penalty' factor
    problem.control('ue1','m/s')    # The extra control
    problem.constant('lim',0.25,'m')  # The constraint limit

    problem.quantity = [Value('psi1','(2*lim/(1+exp((2/lim)*xi11)))'),
                        Value('psi11','(-(4*exp((2*xi11)/lim))/(exp((2*xi11)/lim) + 1)**2)'),
                        Value('psi12','((16*exp((4*xi11)/lim))/(lim*(exp((2*xi11)/lim) + 1)**3) - (8*exp((2*xi11)/lim))/(lim*(exp((2*xi11)/lim) + 1)**2))'),
                        Value('psi13','((96*exp((4*xi11)/lim))/(lim**2*(exp((2*xi11)/lim) + 1)**3) - (16*exp((2*xi11)/lim))/(lim**2*(exp((2*xi11)/lim) + 1)**2) - (96*exp((6*xi11)/lim))/(lim**2*(exp((2*xi11)/lim) + 1)**4))')
                       ]
    problem.state('xi11','xi12','m')
    problem.state('xi12','ue1','m')
    problem.constraints('default',0).initial('xi11 - xi11_0','m') \
                                    .initial('xi12 - xi12_0','m/s') \
                                    .equality(c1_2+' - '+h1_3,'m/s')

    problem.cost['path'] = Expression('u^2 + eps1*(ue1^2)','m^2/s')

    problem.guess.setup('auto',
                    start=[0,1,-.1,-.1],          # Starting values for states in order
                    direction='forward',
                    costate_guess = -0.1,
                    time_integrate = 1      ## REQUIRED BECAUSE OF FIXED FINAL TIME
                    )

    # problem.steps.add_step().num_cases(11) \

    problem.steps.add_step().num_cases(41)   \
                            .initial('xi11',0.0) \
                            .initial('xi12',-1.0) \
                            .terminal('x',0) \
                            .terminal('v', -1)
                            # .const('lim',0.10)

    # problem.steps.add_step().num_cases(41)      \

    problem.steps.add_step().num_cases(61)      \
                            .const('lim',0.13)

    problem.steps.add_step().num_cases(41,spacing='log')      \
                            .const('eps1',1e-3)
    return problem

if __name__ == '__main__':
    Beluga.run(get_problem())
