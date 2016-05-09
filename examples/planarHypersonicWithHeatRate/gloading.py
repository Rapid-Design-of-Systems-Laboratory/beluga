import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *

import functools

def get_problem():
    """A simple planar hypersonic problem example with Gloading constraint."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('planarHypersonicWithGloading')

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
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/r','rad')  \
           .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
           .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')

    # Define controls
    # problem.control('alfaDot','rad/s')
    problem.control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .terminal('h-h_f','m')  \
                        .terminal('theta-theta_f','rad') \
                        .initial('gam-gam_0','rad')
    # Define constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
    problem.constant('rn',1/12*0.3048,'m') # Nose radius, m
    problem.constant('k',1.74153e-4,'sqrt(kg)/m')   # Sutton-Graves constant
    problem.constant('g0',9.80665,'m/s^2')   # Sutton-Graves constant
    problem.constant('alfaRateMax',20*pi/180,'rad/s')
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-6, max_iterations=10000, verbose = True, cached = False, number_arcs=2)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100000, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)\
                   .unit('nd',100**2)

    # Smoothed path constraint
    c1 = '( (D^2 + L^2)/(mass^2*g0^2) )' # Non dimensional
    h1_1 = '(psi1)';              # xi11dot = ue1
    # problem.constant('eps1',1e-4,'m^2/s^2')   # The smoothing 'penalty' factor
    problem.constant('eps1',1,'m^2/s^2')   # The smoothing 'penalty' factor
    problem.constant('gMax',300**2,'nd')  # The constraint limit
    problem.control('ue1','1/s')    # The extra control
    # problem.quantity ('psi1','(2*gMax/(1+ exp((2/gMax)*ue1)))')
    problem.quantity ('psi1','(gMax - exp(-ue1))')
    problem.constraints('default',0).equality(c1+' - '+h1_1,'nd')

    problem.cost['path'] = Expression('eps1*(ue1^2)','m^2/s^2')

    problem.guess.setup('auto',start=[20000,0,2000,-85*pi/180])
    # problem.guess.setup('file',filename='fpa.dill',step=-1, iteration=-1)


    problem.steps.add_step().num_cases(21).initial('h',0)
    problem.steps.add_step().num_cases(101).initial('gam',-70*pi/180)\
                            .terminal('theta', 0.3*pi/180)
    problem.steps.add_step().num_cases(21)  \
                             .terminal('theta', 4*pi/180)
    problem.steps.add_step().num_cases(21)  \
                            .const('gMax',50**2)
    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
