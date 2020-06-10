"""
References
----------
.. [1] Vinh, Nguyen X., Adolf Busemann, and Robert D. Culp. "Hypersonic and planetary entry flight mechanics."
    NASA STI/Recon Technical Report A 81 (1980).
"""

from math import *

import beluga
import logging

import matplotlib.pyplot as plt

'''
Begin the planar portion of the solution process.
'''
ocp = beluga.OCP('planarHypersonic')

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
ocp.constant('rho0', 0.0001*1.2, 'kg/m^3')  # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp.constant('mass', 750/2.2046226, 'kg')  # Mass of vehicle, kg
ocp.constant('re', 6378000, 'm')  # Radius of planet, m
ocp.constant('Aref', pi*(24*.0254/2)**2, 'm^2')  # Reference area of vehicle, m^2
ocp.constant('h_0', 80000, 'm')
ocp.constant('v_0', 4000, 'm/s')
ocp.constant('gam_0', (-90)*pi/180, 'rad')
ocp.constant('h_f', 80000, 'm')
ocp.constant('theta_f', 0, 'rad')

# Define costs
ocp.terminal_cost('-v^2', 'm^2/s^2')

# Define constraints
ocp.constraints() \
    .initial('h-h_0', 'm') \
    .initial('theta', 'rad') \
    .initial('v-v_0', 'm/s') \
    .initial('gam-gam_0', 'rad') \
    .initial('t', 's') \
    .terminal('h-h_f', 'm')  \
    .terminal('theta-theta_f', 'rad')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[40000, 0, 2000, (-90)*pi/180],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0],
    use_control_guess=True)

continuation_steps = beluga.init_continuation()

# Start by flying straight towards the ground
continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .const('h_f', 0)

# Slowly turn up the density
continuation_steps.add_step('bisection') \
                .num_cases(3) \
                .const('rho0', 1.2)

# Move downrange out a tad
continuation_steps.add_step('bisection') \
                .num_cases(3) \
                .const('theta_f', 0.01*pi/180)

# Bring flight-path angle up slightly to activate the control
continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .const('gam_0', -80*pi/180) \
                .const('theta_f', 0.5*pi/180)

continuation_steps.add_step('bisection') \
                .num_cases(31) \
                .const('gam_0', -0*pi/180) \
                .const('theta_f', 3*pi/180)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

cont_planar = beluga.solve(ocp=ocp,
                           method='indirect',
                           optim_options={'control_method': 'icrm'},
                           bvp_algorithm=bvp_solver,
                           steps=continuation_steps,
                           guess_generator=guess_maker,
                           initial_helper=True)

sol = cont_planar[-1][-1]

'''
Begin the 3 dof portion of the solution process.
'''
ocp_2 = beluga.OCP('hypersonic3DOF')

# Define independent variables
ocp_2.independent('t', 's')

rho = 'rho0*exp(-h/H)'
Cl = '(1.5658*alpha + -0.0000)'
Cd = '(1.6537*alpha**2 + 0.0612)'
D = '(0.5*{}*v**2*{}*Aref)'.format(rho, Cd)
L = '(0.5*{}*v**2*{}*Aref)'.format(rho, Cl)
r = '(re+h)'

# Define equations of motion
ocp_2 \
    .state('h', 'v*sin(gam)', 'm') \
    .state('theta', 'v*cos(gam)*cos(psi)/({}*cos(phi))'.format(r), 'rad') \
    .state('phi', 'v*cos(gam)*sin(psi)/{}'.format(r), 'rad') \
    .state('v', '-{}/mass - mu*sin(gam)/{}**2'.format(D, r),  'm/s') \
    .state('gam', '{}*cos(bank)/(mass*v) - mu/(v*{}**2)*cos(gam) + v/{}*cos(gam)'.format(L, r, r),  'rad') \
    .state('psi', '{}*sin(bank)/(mass*cos(gam)*v) - v/{}*cos(gam)*cos(psi)*tan(phi)'.format(L, r),  'rad')

# Define controls
ocp_2.control('alpha', 'rad') \
   .control('bank', 'rad')

# Define costs
ocp_2.terminal_cost('-v^2', 'm^2/s^2')

# Define constraints
ocp_2.constraints() \
    .initial('h-h_0', 'm') \
    .initial('theta-theta_0', 'rad') \
    .initial('phi-phi_0', 'rad') \
    .initial('v-v_0', 'm/s') \
    .initial('gam-gam_0', 'rad') \
    .initial('psi-psi_0', 'rad') \
    .initial('t', 's') \
    .terminal('h-h_f', 'm') \
    .terminal('theta-theta_f', 'rad') \
    .terminal('phi-phi_f', 'rad')

# Define constants
ocp_2.constant('mu', 3.986e5*1e9, 'm**3/s**2')  # Gravitational parameter, m**3/s**2
ocp_2.constant('rho0', 1.2, 'kg/m**3')  # Sea-level atmospheric density, kg/m**3
ocp_2.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp_2.constant('mass', 750/2.2046226, 'kg')  # Mass of vehicle, kg
ocp_2.constant('re', 6378000, 'm')  # Radius of planet, m
ocp_2.constant('Aref', pi*(24*.0254/2)**2, 'm**2')  # Reference area of vehicle, m**2
ocp_2.constant('rn', 1/12*0.3048, 'm')  # Nose radius, m
ocp_2.constant('h_0', sol.y[0, 0], 'm')
ocp_2.constant('theta_0', sol.y[0, 1], 'rad')
ocp_2.constant('phi_0', 0, 'rad')
ocp_2.constant('v_0', sol.y[0, 2], 'm/s')
ocp_2.constant('gam_0', sol.y[0, 3], 'rad')
ocp_2.constant('psi_0', 0, 'rad')
ocp_2.constant('h_f', sol.y[-1, 0], 'm')
ocp_2.constant('theta_f', sol.y[-1, 1], 'rad')
ocp_2.constant('phi_f', 0, 'rad')

ocp_2.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver_2 = beluga.bvp_algorithm('Shooting', num_arcs=8)

guess_maker_2 = beluga.guess_generator(
    'auto',
    start=[sol.y[0, 0], sol.y[0, 1], 0, sol.y[0, 2], sol.y[0, 3], 0],
    direction='forward',
    costate_guess=[sol.dual[0, 0], sol.dual[0, 1], -0.01, sol.dual[0, 2], sol.dual[0, 3], -0.01],
    control_guess=[sol.u[0, 0], 0.0],
    use_control_guess=True,
    time_integrate=sol.t[-1],
)

continuation_steps_2 = beluga.init_continuation()

continuation_steps_2.add_step('bisection').num_cases(3) \
    .const('h_f', sol.y[-1, 0]) \
    .const('theta_f', sol.y[-1, 1]) \
    .const('phi_f', 0)

continuation_steps_2.add_step('bisection').num_cases(41) \
    .const('phi_f', 2*pi/180)

cont_3dof = beluga.solve(
    ocp=ocp_2,
    method='indirect',
    optim_options={'control_method': 'pmp'},
    bvp_algorithm=bvp_solver_2,
    steps=continuation_steps_2,
    guess_generator=guess_maker_2)

final_continuation = cont_3dof[-1]

plt.figure()
for trajectory in final_continuation:
    # Plot altitude vs velocity for the swept crossrange cases
    plt.plot(trajectory.y[:, 3], trajectory.y[:, 0])

plt.xlabel('Velocity [m/s]')
plt.ylabel('Altitude [m]')
plt.grid(True)
plt.show()
