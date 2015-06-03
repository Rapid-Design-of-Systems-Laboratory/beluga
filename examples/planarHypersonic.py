import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
import math
"""A simple planar hypersonic problem example."""

# Rename this and/or move to optim package?
problem = beluga.optim.Problem()

# Define independent variables
problem.independent('t', 's')

rho = 'rho0*exp(-h/H)'
Cl  = '(1.5658*alfa + -0.0000)'
# Allow use of caret instead of **
Cd  = '(1.6537*alfa**2 + 0.0612)'
D   = '(0.5*'+rho+'*v**2*'+Cd+'*Aref)'
L   = '(0.5*'+rho+'*v**2*'+Cl+'*Aref)'
r   = '(re+h)'
# Define equations of motion
problem.state('h','v*sin(gam)','m')   \
       .state('theta','v*sin(gam)/'+r,'rad')  \
       .state('v','-'+D+'/mass - mu*sin(gam)/'+r+'**2','m/s')
       .state('gam',L+'/(mass*v) + (v/'+r+' - mu/(v*'+r+'**2))*cos(gam)','rad')

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

# Define constants (change to have units as well)
problem.constant('mu',3.986e5*1e9,'m^3/s^2') # Gravitational parameter, m^3/s^2
problem.constant('rho0',1.2,'kg/m^3') # Sea-level atmospheric density, kg/m^3
problem.constant('H',7500,'m') # Scale height for atmosphere of Earth, m
problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
problem.constant('re',6378000,'m') # Radius of planet, m
problem.constant('Aref',math.pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
problem.constant('rn',1/12*0.3048,'m') # Nose radius, m


# Define quantity (not implemented at present)
# Is this actually an Expression rather than a Value?
problem.quantity = [Value('tanAng','tan(theta)')]

problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)

# Can be array or function handle
# TODO: implement an "initial guess" class subclassing Solution
problem.guess = bvpsol.bvpinit(np.linspace(0,1,2), [80e3,0,6000,0,-0.1,-0.1,-0.1,-0.1,0.1])

# Figure out nicer way of representing this. Done?
problem.steps = ContinuationList()   # Add a reset function?

problem.steps.add_step(ContinuationStep()
                .num_cases(10)
                .terminal('h', 0.0)
                .terminal('theta',2*pi/180))
# (
# problem.steps.add_step().num_cases(2)
#                  .terminal('x', 30.0)
#                  .terminal('y',-30.0),
#
# problem.steps.add_step()
#                 .num_cases(3)
#                 .terminal('x', 40.0)
#                 .terminal('y',-40.0)
# )

Beluga.run(problem)
#
