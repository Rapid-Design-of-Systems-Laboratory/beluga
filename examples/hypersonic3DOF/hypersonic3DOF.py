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
    problem = beluga.optim.Problem('hypersonci3DOF')

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
    problem.state('h','v*sin(gam)','m')                                     \
           .state('theta','v*cos(gam)*cos(psi)/('+r+'*cos(phi))','rad')    \
           .state('phi','v*cos(gam)*sin(psi)/'+r,'rad')                    \
           .state('v','-'+D+'/mass - mu*sin(gam)/'+r+'^2','m/s')            \
           .state('gam',L+'*cos(bank)/(mass*v) - mu/(v*'+r+'^2)*cos(gam) + v/'+r+'*cos(gam)','rad')                                         \
           .state('psi',L+'*sin(bank)/(mass*cos(gam)*v) - v/'+r+'*cos(gam)*cos(psi)*tan(phi)','rad')

    # Define controls
    problem.control('bank','rad') \
           .control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m')              \
                         .initial('theta-theta_0','rad')     \
                         .initial('phi-phi_0','rad')         \
                         .initial('v-v_0','m/s')             \
                         .terminal('h-h_f','m')              \
                         .terminal('theta-theta_f','rad')    \
                         .terminal('phi-phi_f','rad')

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

    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False)
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=4000, verbose = True, cached = False, number_arcs=4)

    problem.guess.setup('auto',start=[80000,0,0,5000,(-90+10)*pi/180,0])

    problem.steps.add_step().num_cases(11)           \
                            .terminal('h',0)
    #
    # problem.steps.add_step().num_cases(11)          \
    #                         .initial('h',80000)

    problem.steps.add_step().num_cases(41)          \
                            .terminal('theta',5*pi/180) \
                            .terminal('phi',2*pi/180)

    # problem.steps.add_step().num_cases(10)              \
    #                         .terminal('theta',5*pi/180) \
    #                         .terminal('phi',5*pi/180)

    return problem

if __name__ == '__main__':
    problem = get_problem()
    # Default solver is a forward-difference Single Shooting solver with 1e-4 tolerance
    Beluga.run(problem)
