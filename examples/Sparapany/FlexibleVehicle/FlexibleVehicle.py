import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *

"""Hypersonic 3DOF dynamics example."""
def get_problem():
    # Figure out way to implement caching automatically
    # @functools.lru_cache(maxsize=None)
    def CLfunction(alfa):
        return 1.5658*alfa

    # @functools.lru_cache(maxsize=None)
    def CDfunction(alfa):
        return 1.6537*alfa**2 + 0.0612

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('FlexibleVehicle')

    # Define independent variables
    problem.independent('t', 's')

    rho = 'rho0*exp(-h/H)'
    Cl  = '(1.5658*alfa + -0.0000)'
    Cd  = '(1.6537*alfa^2 + 0.0612)'
    # Cl = 'CLfunction(alfa)'
    # Cd = 'CDfunction(alfa)'
    D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
    L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
    r   = '(re+h)'

    # Define equations of motion
    problem.state('u','-0.002026562855097*u - 0.002368164948809*w + 0.032731665933238*q + 3.029883241338212*eta + 0.045901344828101*etad + -6.51591715238238e-05*p','m/s') \
           .state('w','9.44720390042629e-05*u - 0.799313716620718*w + 885.153743891408*q + 74.6746509565035*eta - 0.239979021960767*etad + -0.00940054017082900*p','m/s') \
           .state('q','8.24130363317209e-06*u - 0.533547286663736*w + 1.57366050889403*q + 449.977120308181*eta - 1.37337187086628*etad + 0.00549719742270432*p','rad/s')   \
           .state('eta','7.65124859500383e-17*u - 5.42448031087167e-15*w + 7.49400541622875e-14*q + 7.48823226084066e-12*eta + 0.999999999999670*etad + -1.30168635216370e-16*p','nd')  \
           .state('etad','6.94499786867138e-05*u + 5.55595738164967*w - 12.3805376450147*q - 10041.5218916472*eta - 5.20187210352674*etad + 0.0494446349920132*p','nd')    \
           .state('theta','q','rad')    \
           .state('x','u*cos(theta) + w*sin(theta)','m')   \
           .state('z','u*sin(theta) - w*cos(theta)','m')

    # Define controls
    problem.control('p','N')

    # Define costs
    problem.cost['path'] = Expression('1','s')

    # Define constraints
    problem.constraints().initial('u-u_0','m/s') \
                         .initial('w-w_0','m/s') \
                         .initial('q-q_0','rad/s') \
                         .initial('eta-eta_0','nd') \
                         .initial('etad-etad_0','nd') \
                         .initial('theta-theta_0','rad') \
                         .initial('x-x_0','m') \
                         .initial('z-z_0','m') \
                         .terminal('x-x_f','m') \
                         .terminal('z-z_f','m')

    problem.scale.unit('m','x')     \
                 .unit('s','x/u') \
                 .unit('rad',1)   \
                 .unit('nd',1)    \
                 .unit('N',1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False)
    #problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=4000, verbose = True, cached = False, number_arcs=4)

    problem.guess.setup('auto',start=[885,0,0,0,0,0,0,0])

    problem.steps.add_step().num_cases(10)  \
                            .terminal('x',1)

    problem.steps.add_step().num_cases(10)           \
                            .terminal('x',4330.127018922193)
    #
    problem.steps.add_step().num_cases(10)          \
                            .initial('z',2500)

    return problem

if __name__ == '__main__':
    problem = get_problem()
    # Default solver is a forward-difference Single Shooting solver with 1e-4 tolerance
    Beluga.run(problem)
