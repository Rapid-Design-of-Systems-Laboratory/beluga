import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *
from mock import *

import pytest

@pytest.fixture(scope='session')
def problem_1():
    """A simple planar hypersonic problem example."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('planarHypersonic')
    # problem = beluga.optim.Problem()

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
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/'+r,'rad')  \
           .state('v','-'+D+'/mass - mu*sin(gam)/'+r+'**2','m/s') \
           .state('gam',L+'/(mass*v) + (v/'+r+' - mu/(v*'+r+'^2))*cos(gam)','rad')

    # Define controls
    problem.control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .terminal('h-h_f','m')  \
                        .terminal('theta-theta_f','rad')

    # Define constants
    problem.constant('mu',3.986e5*1e9,'m^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0',1.2,'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H',7500,'m') # Scale height for atmosphere of Earth, m


    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
    problem.constant('rn',1/12*0.3048,'m') # Nose radius, m

    problem.scale.unit('m','h')     \
                   .unit('s','h/v')\
                   .unit('kg','mass')   \
                   .unit('rad',1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(5) \
                            .terminal('h', 0)  # bvp4c takes 10 steps

    problem.steps.add_step().num_cases(21)  \
                            .terminal('theta', 10*pi/180)
    return problem

@pytest.fixture(scope='session')

def dummy_bvp_1():
    dummy_bvp = Mock(bvpsol.BVP)
    dummy_bvp.solution = bvpsol.Solution()
    dummy_bvp.solution.converged = True
    return dummy_bvp

@pytest.fixture(scope='session')
def scaled_problem_1_bvp():
    bvp = bvpsol.BVP(None,None)

    bvp.solution.aux = {'const': {'H': 0.09375, 're': 79.725, 'mu': 90099.286107092, 'rho0': 38407326093859.13, 'Aref': 4.560367311877479e-11, 'mass': 21.266199024571318, 'rn': 3.175e-07},
            'initial': {'h': 1.0, 'theta': 0.0, 'tf': 0.00029394967999999999, 'v': 21.262142554467147, 'lagrange_gam': 1.808314824025931e-06, 'lagrange_theta': 1.808314824025931e-06, 'gam': -1.5707963267948966, 'lagrange_h': 0.14466518592207447, 'lagrange_v': 0.00042524285108934293}, 'parameters': ['lagrange_initial_1', 'lagrange_initial_2', 'lagrange_initial_3', 'lagrange_terminal_1', 'lagrange_terminal_2'],
            'function': {},
            'terminal': {'h': 0.99374940380311361, 'theta': 3.4084523282394519e-14, 'tf': 0.00029394967999999999, 'v': 21.266199024571318, 'lagrange_gam': 1.8083800321018192e-06, 'lagrange_theta': 1.808314824025931e-06, 'gam': -1.5707963259187729, 'lagrange_h': 0.14466519241178213, 'lagrange_v': 0.00046776747646368021}, 'constraint': []}

    return bvp

@pytest.fixture(scope='session')
def scaled_problem_1_solinit():
    """Returns scaled version of the initial guess from problem_1"""

    sol_y = [[  1.00000000e+00,   9.99937500e-01,   9.99312493e-01,   9.98687474e-01,
                9.98062443e-01,   9.97437400e-01,   9.96812345e-01,   9.96187278e-01,
                9.95562199e-01,   9.94937109e-01,   9.94312006e-01,   9.93749404e-01],
             [  0.00000000e+00,   3.44282986e-18,   4.16124993e-16,   1.51500165e-15,
                3.29792926e-15,   5.76283267e-15,   8.90771179e-15,   1.27306329e-14,
                1.72297305e-14,   2.24032024e-14,   2.82493092e-14,   3.40845233e-14],
             [  9.99809253e-01,   9.99811160e-01,   9.99830235e-01,   9.99849309e-01,
                9.99868384e-01,   9.99887459e-01,   9.99906533e-01,   9.99925608e-01,
                9.99944683e-01,   9.99963758e-01,   9.99982833e-01,   1.00000000e+00],
             [ -1.57079633e+00,  -1.57079633e+00,  -1.57079633e+00,  -1.57079633e+00,
               -1.57079633e+00,  -1.57079633e+00,  -1.57079633e+00,  -1.57079633e+00,
               -1.57079633e+00,  -1.57079633e+00,  -1.57079633e+00,  -1.57079633e+00],
             [  3.19877933e-04,   3.19877934e-04,   3.19877935e-04,   3.19877937e-04,
                3.19877938e-04,   3.19877940e-04,   3.19877941e-04,   3.19877943e-04,
                3.19877944e-04,   3.19877945e-04,   3.19877947e-04,   3.19877948e-04],
             [  3.99847417e-09,   3.99847417e-09,   3.99847417e-09,   3.99847417e-09,
                3.99847417e-09,   3.99847417e-09,   3.99847417e-09,   3.99847417e-09,
                3.99847417e-09,   3.99847417e-09,   3.99847417e-09,   3.99847417e-09],
             [  1.99961851e-05,   2.00161814e-05,   2.02161447e-05,   2.04161081e-05,
                2.06160715e-05,   2.08160349e-05,   2.10159983e-05,   2.12159618e-05,
                2.14159253e-05,   2.16158888e-05,   2.18158523e-05,   2.19958196e-05],
             [  3.99847417e-09,   3.99847562e-09,   3.99849012e-09,   3.99850461e-09,
                3.99851907e-09,   3.99853352e-09,   3.99854794e-09,   3.99856235e-09,
                3.99857674e-09,   3.99859111e-09,   3.99860545e-09,   3.99861835e-09],
             [  6.25119240e-03,   6.25119240e-03,   6.25119240e-03,   6.25119240e-03,
                6.25119240e-03,   6.25119240e-03,   6.25119240e-03,   6.25119240e-03,
                6.25119240e-03,   6.25119240e-03,   6.25119240e-03,   6.25119240e-03]]
    sol_x = [ 0.0,    0.01,  0.11,  0.21,  0.31,  0.41,  0.51,  0.61,  0.71,  0.81,  0.91,  1.0  ]
    return bvpsol.Solution(sol_x, sol_y)

@pytest.fixture(scope = 'session')
def problem_brachistochrone():
    """!
    \brief     Classical Brachistochrone problem.
    \author    Michael Grant
    \version   0.1
    \date      06/30/15
    """

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('brachistochrone')

    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False, cached = False)

    # Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x','v*cos(theta)','m') \
           .state('y','v*sin(theta)','m') \
           .state('v','g*sin(theta)','m/s')

    # Define controls
    problem.control('theta','rad')

    # Define costs
    problem.cost['path'] = Expression('1','nd')

    # Define constraints
    problem.constraints().initial('x-x_0','m') \
                        .initial('y-y_0','m') \
                        .initial('v-v_0','m/s') \
                        .terminal('x-x_f','m')  \
                        .terminal('y-y_f','m')

    # Define constants
    problem.constant('g', 9.81, 'm/s^2') # local gravity acceleration

    problem.scale.unit('m', 'x')     \
                 .unit('s', 'x/v')   \
                 .unit('nd', 1)      \
                 .unit('rad', 1)

    problem.guess.setup('auto', start=[0,0,1], costate_guess = -0.1)

    problem.steps.add_step().num_cases(21) \
                            .terminal('x', 5) \
                            .terminal('y', 5)

    # problem.steps.add_step().num_cases(10)  \
    #                         .terminal('x', 5) \
    #                         .terminal('y', 5)

    return problem
