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
    # Figure out way to implement caching automatically
    #@functools.lru_cache(maxsize=None)
    """A simple planar hypersonic problem example."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('planarHypersonic')
    # problem = beluga.optim.Problem()

    # Define independent variables
    problem.independent('t', 's')

    rho = 'rho0*exp(-h/H)'
    Cl  = '(1.4428*alfa)'
    Cd  = '(2.1877*alfa^2 + 0.0503)'

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
    problem.cost['terminal'] = Expression('-theta^2','rad^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .initial('gam-gam_0','rad') \
                        .terminal('h-h_f','m') \
                        .path('alfaLim','alfa','<',11*pi/180,'rad')

    # Define constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    problem.constant('mass',203.21,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',0.1877,'m^2') # Reference area of vehicle, m^2

    # problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100, verbose = True, cached = False, number_arcs=2)
    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-5, max_iterations=25, max_error=100, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]
    # Need long integration time to avoid local min?
    problem.guess.setup('auto',start=[15000,0,500,0*pi/180],costate_guess=-0.0000001,time_integrate=50)
    #problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step('bisection').num_cases(11) \
                            .initial('v', 1000) \
                            .terminal('h', 12000)
    #
    # problem.steps.add_step('bisection').num_cases(61) \
    #                     .terminal('h',8000)

    # problem.steps.add_step('bisection').num_cases(51) \
    #                         .terminal('h',10000)
    problem.steps.add_step('bisection').num_cases(31) \
                            .initial('v', 2500)
    problem.steps.add_step('bisection').num_cases(21,spacing='log') \
                            .const('eps_alfaLim',1e-3)



    # problem.steps.add_step('bisection').num_cases(21) \
    #                         .initial('theta',0) \
    #                         .terminal('theta', 10*pi/180)

    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
