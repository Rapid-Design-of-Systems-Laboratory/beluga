import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *

import functools


def CLfunction(alfa):
    return 1.5658 * alfa

def CDfunction(alfa):
    return 1.6537 * alfa ** 2 + 0.0612

def get_problem():
    # Figure out way to implement caching automatically
    #@functools.lru_cache(maxsize=None)

    """A simple planar hypersonic problem example."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('planarHypersonic')
    # problem = beluga.optim.Problem()


    # Define independent variables
    problem.independent('t', 's')

    # Define quantities used in the problem
    problem.quantity('rho','rho0*exp(-h/H)')
    # problem.quantity('Cl','(1.5658*alfa + -0.0000)')
    # problem.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
    # problem.quantity('D','0.5*rho*v^2*CDfunction(alfa)*Aref')
    # problem.quantity('L','0.5*rho*v^2*CLfunction(alfa)*Aref')
    problem.quantity('r','re+h')

    # Define equations of motion
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/r','rad')  \
           .state('v','-(0.5*rho*v^2*CDfunction(alfa)*Aref)/mass - mu*sin(gam)/r**2','m/s') \
           .state('gam','(0.5*rho*v^2*CLfunction(alfa)*Aref)/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')

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
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2

    problem.mode = 'analytic'
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=2, max_error=200)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100000, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)

    problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180],costate_guess=-0.1)

    problem.steps.add_step().num_cases(11) \
                            .terminal('h', 0)

    problem.steps.add_step().num_cases(41)  \
                            .terminal('theta', 10*pi/180)

    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
