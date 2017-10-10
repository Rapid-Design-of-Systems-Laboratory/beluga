import numpy as np
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import Expression
from beluga.utils import keyboard
from math import *
import dill
import scipy.optimize

def get_problem():
    """Planar hypersonic problem with simple path constraint."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('mountain')

    # Define independent variables
    problem.independent('t', 's')

    # Define quantities used in the problem
    problem.quantity('rho','rho0*exp(-h/H)')
    problem.quantity('Cl','(1.5658*alfa + -0.0000)')
    problem.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
    problem.quantity('D','0.5*rho*v^2*Cd*Aref')
    problem.quantity('L','0.5*rho*v^2*Cl*Aref')
    problem.quantity('r','re+h')

    # Define equations of motion
    problem.state('h','(v*sin(gam))','m')   \
           .state('theta','v*cos(gam)/r','rad')  \
           .state('v','(-D/mass - mu*sin(gam)/r**2)','m/s') \
           .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')

    # Define controls
    problem.control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')

    # Planetary constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m
    problem.constant('re',6378000,'m') # Radius of planet, m

    # Vehicle constants
    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2

    # Constants related to constraints
    problem.constant('rn',1/12*0.3048,'m') # Nose radius, m
    # problem.constant('k',1.74153e-4,'sqrt(kg)/m')   # Sutton-Graves constant
    problem.constant('k',1.74153e-4,'W*(s^3/(sqrt(kg)*m))') # Some units magic
    problem.quantity('qdot','k*sqrt(rho/rn)*v^3')   # Convectional heat rate
    problem.constant('qdotMax', 10000e4, 'W')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .initial('gam-gam_0','rad') \
                        .terminal('h-h_f','m')  \
                        .terminal('theta-theta_f','rad') \
                        .path('heatRate','(qdot/qdotMax)','<',1,'nd',start_eps=1e-2) \

    # problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=2, max_error=10)
    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd', timeout=5, tolerance=1e-5, max_iterations=20, verbose = True, cached = False, max_error=30)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)  \
                   .unit('nd',1) \
                   .unit('W',1)

    # problem.guess.setup('auto',start=[80000,0,4000,-90*pi/180],costate_guess=-0.1)
    #
    # problem.steps.add_step('bisection').num_cases(11) \
    #                         .terminal('h', 10000.0) \
    #
    # problem.steps.add_step('bisection').num_cases(31)  \
    #                         .initial('gam', -45*pi/180) \
    #                         .terminal('theta', 1*pi/180)
    #
    # problem.steps.add_step('bisection').num_cases(6)  \
    #                         .terminal('theta', 2*pi/180)

    # problem.guess.setup(mode='file', filename='data-skip-10000-eps2.dill', step=-1, iteration=-1)
    # problem.steps.add_step('bisection').num_cases(11)  \
    #                         .const('qdotMax', 1800e4)

    problem.guess.setup(mode='file', filename='data-skip-1800-eps2.dill', step=-1, iteration=-1)
    problem.steps.add_step('bisection').num_cases(41,spacing='log')  \
                            .const('eps_heatRate', 1e-4)

    problem.steps.add_step('bisection').num_cases(21)  \
                            .const('qdotMax', 1200e4)

    # problem.guess.setup(mode='file', filename='data-skip-10000-eps2.dill', step=-1, iteration=-1)
    #
    # problem.steps.add_step('bisection').num_cases(41, spacing='log')  \
    #                         .const('eps_heatRate', 1e-7) \

    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
