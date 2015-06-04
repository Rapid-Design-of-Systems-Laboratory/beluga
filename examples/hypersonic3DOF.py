import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *

"""Brachistochrone example."""

# Rename this and/or move to optim package?
problem = beluga.optim.Problem()

# Define independent variables
problem.independent('t', 's')

rho = 'rho0*exp(-h/H)'
Cl  = '(1.5658*alfa + -0.0000)'
# Allow use of caret instead of **
Cd  = '(1.6537*alfa^2 + 0.0612)'
D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
r   = '(re+h)'
# Define equations of motion

problem.state('h','v*cos(theta)','m')   \
       .state('theta','-v*sin(theta)','rad')  \
       .state('phi','-v*sin(theta)','rad')  \
       .state('v','g*sin(theta)','m/s')
       .state('gam','g*sin(theta)','rad')
       .state('psi','g*sin(theta)','rad')

# Define controls
problem.control('alfa','rad')
       .control('bank','rad')

# Define costs
problem.cost['path'] = Expression('1','s')

# Define constraints
problem.constraints('default',0) \
                    .initial('x-x_0','m')    \
                    .initial('y-y_0','m')    \
                    .initial('v-v_0','m/s')  \
                    .terminal('x-x_f','m')   \
                    .terminal('y-y_f','m')

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

problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)

# Can be array or function handle
# TODO: implement an "initial guess" class subclassing Solution
problem.guess = bvpsol.bvpinit(np.linspace(0,1,2), [0,0,1,-0.1,-0.1,-0.1,0.1])

problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180])

problem.steps.add_step().num_cases(5) \
                        .terminal('h', 0))  # bvp4c takes 10 steps

problem.steps.add_step().num_cases(50)  \
                        .terminal('theta', 20*pi/180)
Beluga.run(problem)
#
