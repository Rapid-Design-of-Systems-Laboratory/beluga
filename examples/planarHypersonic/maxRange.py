import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from beluga.continuation.strategies import BisectionStrategy
from math import *

import functools

def get_problem():
    """A simple planar hypersonic maximum range problem."""

    problem = beluga.optim.Problem('planarHypersonic')

    # Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/r','rad')  \
           .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
           .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')

    problem.quantity('rho','rho0*exp(-h/H)') \
           .quantity('Cl','(1.4428*alfa)') \
           .quantity('Cd','(2.1877*alfa^2 + 0.0503)') \
           .quantity('D','(0.5*rho*v^2*Cd*Aref)') \
           .quantity('L','(0.5*rho*v^2*Cl*Aref)') \
           .quantity('r','(re+h)')

    # Define controls
    problem.control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-theta^2','rad^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .initial('gam-gam_0','rad') \
                        .terminal('h-h_f','m') \
                        .path('alfaLim','alfa/(alfaMax)','<',1,'rad') # Units a bit inaccurate but watever

    # Define constants
    problem.constant('alfaMax',11*pi/180,'rad')
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    problem.constant('mass',203.21,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',0.1877,'m^2') # Reference area of vehicle, m^2

    # problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-6, max_iterations=50, verbose = True, cached = False, number_arcs=2)
    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-6, max_iterations=20, max_error=100, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)

    # Need long integration time to avoid local min?
    problem.guess.setup('auto',start=[15000,0,500,0*pi/180],costate_guess=-0.00000001,time_integrate=10)

    # 41 101
    problem.steps.add_step('bisection').num_cases(21) \
                            .initial('v', 1000) \
                            .terminal('h', 12000)
    problem.steps.add_step('bisection').num_cases(41) \
                            .initial('v', 3800)
    # #
    # # problem.guess.setup('file',filename='phu_2k5_eps2.dill', step=-1, iteration=-1)
    # # problem.steps.add_step('bisection').num_cases(5) \
    # #                         .initial('h',20000)
    # # problem.steps.add_step('bisection').num_cases(51) \
    # #                         .initial('v',3000)
    # # problem.steps.add_step('bisection').num_cases(21,spacing='log') \
    # #                         .const('eps_alfaLim',1e-3)
    #
    # problem.guess.setup('file',filename='phu_2k5_eps2.dill', step=-1, iteration=-1)
    # problem.steps.add_step('bisection').num_cases(11) \
    #                         .initial('h',25000) \
    #                         .initial('gam',5*pi/180)
    # problem.steps.add_step('bisection').num_cases(51) \
    #                         .initial('v',3800)
    # problem.guess.setup('file',filename='phu_3k8_25k_eps2.dill', step=-1, iteration=-1)
    # problem.steps.add_step('bisection').num_cases(11) \
    #                                    .initial('h',22500)
    problem.steps.add_step('bisection').num_cases(41,spacing='log') \
                            .const('eps_alfaLim',1e-7)
    # problem.steps.add_step('bisection').num_cases(41) \
    #                         .initial('v', 3000)


    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
