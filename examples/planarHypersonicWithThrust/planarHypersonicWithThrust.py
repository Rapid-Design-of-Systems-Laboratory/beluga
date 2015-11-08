import beluga.Beluga as Beluga
import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *

import functools

def get_problem():
    """A simple planar hypersonic problem example."""
    # Author: Joseph Williams

    problem = beluga.optim.Problem('planarHypersonicWithThrust')

    # Define independent variables
    problem.independent('t', 's')

    rho = 'rho0*exp(-h/H)'
    Cl  = '(0.496*alfa + 0.0049)'
    Cd  = '(0.4747*alfa^2 + 0.0096*alfa + 0.0007)'
    # T = 'ThrustFunction()'
    D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
    L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
    r   = '(re+h)'
    Ft  = '(T*cos(alfa) - '+D+')'
    Fn  = '(T*sin(alfa) + '+L+')'

    # Define equations of motion
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/'+r,'rad')  \
           .state('v',Ft+'/mass - mu*sin(gam)/'+r+'**2','m/s') \
           .state('gam',Fn+'/(mass*v) + (v/'+r+' - mu/(v*'+r+'^2))*cos(gam)','rad') \
           .state('mass','mdotf','kg')

    # Define controls
    problem.control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')
    # problem.cost['path'] = Expression('1','s')
    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .initial('mass-mass_0','kg') \
                        .terminal('h-h_f','m')  \
                        .terminal('theta-theta_f','rad')

    # Define constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    # problem.constant('T',2668932,'kg*m/s^2') # Constant Thrust of Vehcicle, kgm/s^2
#     problem.constant('mdotf',15.5*0.05,'kg/s') # Fuel Mass Flow Rate of Vehicle, kg
    problem.constant('T',0,'kg*m/s^2') # Constant Thrust of Vehcicle, kgm/s^2
    problem.constant('mdotf',0,'kg/s') # Fuel Mass Flow Rate of Vehicle, kg

    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',557.4,'m^2') # Reference area of vehicle, m^2
    problem.constant('rn',1/12*0.3048,'m') # Nose radius, m

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=4)
    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    # problem.guess.setup('auto',start=[1000,0,100,-90*pi/180,127005])
    problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180,127005])
    #problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(11) \
                            .terminal('h', 0) \
                            # .initial('h',60000)\
                            # .initial('v',5000)
                            #.terminal('theta', 10*pi/180)
    problem.steps.add_step().num_cases(11)  \
                            .terminal('theta', 10*pi/180)

    problem.steps.add_step().num_cases(5)  \
                            .const('T', 2668932) \
                            .const('mdotf', 15.5*0.05)

    #
    # problem.steps.add_step()
    #                 .num_cases(3)
    #                 .terminal('x', 40.0)
    #                 .terminal('y',-40.0)
    # )
    return problem

if __name__ == '__main__':
    problem = get_problem()
    # Default solver is a forward-difference Single Shooting solver with 1e-4 tolerance
    sol = Beluga.run(problem)
