"""
References
----------
.. [1] Betts, John T. "Practical methods for optimal control and estimation using nonlinear programming."
    Vol. 19. Siam, 2010.
"""

from math import *

import beluga
import logging
import numpy as np
from matplotlib import pyplot as plt

h_0 = 79248
h_f = 24384
v_0 = 7802.88
v_f = 762
gam_f = -5*np.pi/180

ocp = beluga.OCP('SpaceShuttleMaxCrossrange')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h', 'v*sin(gam)', 'm') \
    .state('theta', 'v*cos(gam)*sin(psi)/(r*cos(phi))', 'rad') \
    .state('phi', 'v*cos(gam)*cos(psi)/r', 'rad') \
    .state('v', '-D/mass - mu*sin(gam)/r**2', 'm/s') \
    .state('gam', 'L*cos(bank)/(mass*v) - mu/(v*r**2)*cos(gam) + v/r*cos(gam)', 'rad') \
    .state('psi', 'L*sin(bank)/(mass*cos(gam)*v) + v/r*cos(gam)*sin(psi)*tan(phi)', 'rad')

# Define quantities used in the problem
ocp.quantity('rho', 'rho0*exp(-h/H)')
ocp.quantity('Cl', 'cl1 * alpha_star + cl0')
ocp.quantity('Cd', 'cd1 * alpha_star + cd2 * alpha_star**2 + cd0')
ocp.quantity('D', '0.5*rho*v**2*Cd*aref')
ocp.quantity('L', '0.5*rho*v**2*Cl*aref')
ocp.quantity('r', 're+h')
ocp.quantity('alpha_star', 'alpha*180/pi')

# Define controls
ocp.control('alpha', 'rad')
ocp.control('bank', 'rad')

# Define constants
ocp.constant('mu', 3.986e5*1e9, 'm**3/s**2')  # Gravitational parameter, m**3/s**2
ocp.constant('rho0', 1.2, 'kg/m**3')  # Sea-level atmospheric density, kg/m**3
ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp.constant('mass', 92079.2511, 'kg')  # Mass of vehicle, kg
ocp.constant('re', 6378000, 'm')  # Radius of planet, m
ocp.constant('aref', 249.9092, 'm**2')  # Reference area of vehicle, m**2

ocp.constant('cl0', -0.20704, '1')
ocp.constant('cl1', 0.029244, '1')

ocp.constant('cd0', 0.07854, '1')
ocp.constant('cd1', -0.61592e-2, '1')
ocp.constant('cd2', 0.621408e-3, '1')
ocp.constant('cd3', -0.323, '1')

ocp.constant('amax', 20 * pi / 180, 'rad')
ocp.constant('bmax', 89 * pi / 180, 'rad')
ocp.constant('eps', 0.00001, 'rad/s')

ocp.constant('h_0', 60000, 'm')
ocp.constant('phi_0', 0, 'rad')
ocp.constant('v_0', 4000, 'm/s')
ocp.constant('gam_0', 0, 'rad')
ocp.constant('h_f', 0, 'm')
ocp.constant('gam_f', -5*np.pi/180, 'rad')
ocp.constant('fpa', 1e-4, '1')

ocp.constant('psi_0', 0, 'rad')

ocp.constant('theta_0', 0, 'rad')
ocp.constant('phi_f', 0, 'rad')

# Define costs
ocp.terminal_cost('-phi**2 + fpa*(gam - gam_f)**2', 'rad**2')

# Define constraints
ocp.constraints() \
    .initial('h-h_0', 'm') \
    .initial('theta-theta_0', 'rad') \
    .initial('phi-phi_0', 'rad') \
    .initial('v-v_0', 'm/s') \
    .initial('gam-gam_0', 'rad') \
    .initial('psi-psi_0', 'rad') \
    .terminal('h-h_f', 'm') \
    .path('alpha', 'rad', lower='-amax', upper='amax', activator='eps', method='utm') \
    .path('bank', 'rad', lower='-bmax', upper='bmax', activator='eps', method='utm')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[0, 0, 100, 200, -80*pi/180, 0*pi/180],
    direction='reverse',
    costate_guess=-0.00001,
    time_integrate=0.1,
    control_guess=[0, 0]
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('v_0', 200) \
    .const('h_0', 1000) \
    .const('gam_f', gam_f)

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('phi_0', 0) \

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('amax', 89*pi/180)

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('gam_0', -1*np.pi/180)

continuation_steps.add_step('bisection') \
    .num_cases(80) \
    .const('h_0', h_0) \
    .const('v_0', v_0 - 1000)

continuation_steps.add_step('bisection') \
    .num_cases(20) \
    .const('psi_0', 90*pi/180)

continuation_steps.add_step('bisection') \
    .num_cases(30) \
    .const('fpa', 1) \
    .const('v_0', v_0) \
    .const('eps', 1e-5)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    optim_options={'control_method': 'icrm'},
)

sol = sol_set[-1][-1]

plt.plot(sol.t, sol.y[:,0])
plt.ylabel('Altitude [m]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.y[:,1]*180/np.pi)
plt.ylabel('Longitude [deg]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.y[:,2]*180/np.pi)
plt.ylabel('Latitude [deg]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.y[:,3])
plt.ylabel('Velocity [m/s]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.y[:,4]*180/np.pi)
plt.ylabel('Flight Path Angle [deg]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.y[:,5]*180/np.pi)
plt.ylabel('Heading [deg]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.u[:,0]*180/np.pi)
plt.ylabel('Angle of Attack [deg]')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.u[:,1]*180/np.pi)
plt.ylabel('Bank Angle [deg]')
plt.xlabel('Time [s]')
plt.show()
