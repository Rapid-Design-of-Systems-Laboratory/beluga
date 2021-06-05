"""
References
----------
.. [1] Vinh, Nguyen X., Adolf Busemann, and Robert D. Culp. "Hypersonic and planetary entry flight mechanics."
    NASA STI/Recon Technical Report A 81 (1980).
"""

from math import *

import beluga
import logging

ocp = beluga.SymbolicProblem()

# Define independent variables
ocp.independent('t', 's')


# Define equations of motion
ocp.state('h', 'v*sin(gam)', 'm')   \
   .state('theta', 'v*cos(gam)/r', 'rad')  \
   .state('v', '-D/mass - mu*sin(gam)/r**2', 'm/s') \
   .state('gam', 'L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)', 'rad')


# Define quantities used in the problem
ocp.quantity('rho', 'rho0*exp(-h/H)')
ocp.quantity('Cl', '(1.5658*alfa + -0.0000)')
ocp.quantity('Cd', '(1.6537*alfa^2 + 0.0612)')
ocp.quantity('D', '0.5*rho*v^2*Cd*Aref')
ocp.quantity('L', '0.5*rho*v^2*Cl*Aref')
ocp.quantity('r', 're+h')

# Define controls
ocp.control('alfa', 'rad')

# Define constants
ocp.constant('mu', 3.986e5*1e9, 'm^3/s^2')  # Gravitational parameter, m^3/s^2
ocp.constant('rho0', 1.2, 'kg/m^3')  # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp.constant('mass', 750/2.2046226, 'kg')  # Mass of vehicle, kg
ocp.constant('re', 6378000, 'm')  # rdius of planet, m
ocp.constant('Aref', pi*(24*.0254/2)**2, 'm^2')  # Reference area of vehicle, m^2
ocp.constant('h_0', 80000, 'm')
ocp.constant('v_0', 4000, 'm/s')
ocp.constant('gam_0', (-90)*pi/180, 'rad')
ocp.constant('h_f', 80000, 'm')
ocp.constant('theta_f', 0, 'rad')

# Define costs
ocp.terminal_cost('-v^2', 'm^2/s^2')

# Define constraints
ocp.initial_constraint('h-h_0', 'm')
ocp.initial_constraint('theta', 'rad')
ocp.initial_constraint('v-v_0', 'm/s')
ocp.initial_constraint('gam-gam_0', 'rad')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('h-h_f', 'm')
ocp.terminal_constraint('theta-theta_f', 'rad')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[40000, 0, 4000, (-90)*pi/180],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0]
)

continuation_steps = beluga.init_continuation()

# Start by flying straight towards the ground
continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .const('h_f', 0)

# # Slowly turn up the density
# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .const('rho0', 1.2)

# Move downrange out a tad
continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .const('theta_f', 0.01*pi/180)

# Bring flight-path angle up slightly to activate the control
continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .const('gam_0', -70*pi/180) \
                .const('theta_f', 0.5*pi/180)

# Move downrange down a bit
continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .const('theta_f', 1*pi/180)

beluga.add_logger(file_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'differential'},
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    initial_helper=True,
    autoscale=False
)
