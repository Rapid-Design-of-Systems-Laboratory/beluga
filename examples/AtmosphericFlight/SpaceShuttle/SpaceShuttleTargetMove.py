"""
References
----------
.. [1] Betts, John T. "Practical methods for optimal control and estimation using nonlinear programming."
    Vol. 19. Siam, 2010.
"""

import beluga
import logging
import numpy as np

h_0 = 260000
h_f = 80000
v_0 = 25600
v_f = 2500
gam_0 = -1*np.pi/180
gam_f = -5*np.pi/180
psi_0 = np.pi/2

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h', 'v*sin(gam)', 'ft')
ocp.state('phi', 'v*cos(gam)*sin(psi)/(r*cos(theta))', 'rad')
ocp.state('theta', 'v*cos(gam)*cos(psi)/r', 'rad')
ocp.state('v', '-D/mass - mu*sin(gam)/r**2', 'ft/s')
ocp.state('gam', 'L*cos(bank)/(mass*v) - mu/(v*r**2)*cos(gam) + v/r*cos(gam)', 'rad')
ocp.state('psi', 'L*sin(bank)/(mass*cos(gam)*v) + v/r*cos(gam)*sin(psi)*tan(theta)', 'rad')

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
ocp.constant('mu', 0.14076539e17, 'ft**3/s**2')  # Gravitational parameter, ft**3/s**2
ocp.constant('rho0', 0.002378, 'slug/ft**3')  # Sea-level atmospheric density, slug/ft**3
ocp.constant('H', 23800, 'ft')  # Scale height for atmosphere of Earth, ft
ocp.constant('mass', 203000/32.174, 'slug')  # Mass of vehicle, slug
ocp.constant('re', 20902900, 'ft')  # Radius of planet, ft
ocp.constant('aref', 2690, 'ft**2')  # Reference area of vehicle, ft**2

ocp.constant('cl0', -0.20704, '1')
ocp.constant('cl1', 0.029244, '1')

ocp.constant('cd0', 0.07854, '1')
ocp.constant('cd1', -0.61592e-2, '1')
ocp.constant('cd2', 0.621408e-3, '1')
ocp.constant('cd3', -0.323, '1')

ocp.constant('h_0', h_0, 'ft')
ocp.constant('phi_0', 0, 'rad')
ocp.constant('theta_0', 0, 'rad')
ocp.constant('v_0', v_0, 'ft/s')
ocp.constant('gam_0', 0, 'rad')
ocp.constant('psi_0', 0, 'rad')
ocp.constant('h_f', h_f, 'ft')
ocp.constant('v_f', v_f, 'ft/s')
ocp.constant('gam_f', -5*np.pi/180, 'rad')

ocp.constant('pi', np.pi, 'rad')
ocp.constant('amax', 89*np.pi/180, 'rad')
ocp.constant('bmax', 89*np.pi/180, 'rad')
ocp.constant('eps', 1e-5, 'rad/s')
ocp.constant('xi', 0, 'rad')

# Define costs
ocp.terminal_cost('-theta*sin(xi) - phi*cos(xi)', 'rad')

# Define constraints
ocp.initial_constraint('h-h_0', 'ft')
ocp.initial_constraint('phi-phi_0', 'rad')
ocp.initial_constraint('theta-theta_0', 'rad')
ocp.initial_constraint('v-v_0', 'ft/s')
ocp.initial_constraint('gam-gam_0', 'rad')
ocp.initial_constraint('psi-psi_0', 'rad')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('h-h_f', 'ft')
ocp.terminal_constraint('v-v_f', 'ft/s')
ocp.terminal_constraint('gam-gam_f', 'rad')

ocp.path_constraint('alpha', 'rad', lower='-amax', upper='amax', activator='eps', method='utm')
ocp.path_constraint('bank', 'rad', lower='-bmax', upper='bmax', activator='eps', method='utm')

ocp.scale(ft='theta*re', s='theta*re/v', slug='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[(h_0-h_f)*0.5 + h_f, 1, 1, v_0*0.25, gam_0, psi_0],
    direction='forward',
    costate_guess=[-1.30487794e-07, -1.00000000e+00, 0, -5.71719036e-06, -7.16743700e-03, 0.],
    control_guess=[18./180*np.pi, 0],
    time_integrate=25
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(20) \
    .const('theta_0', 0) \
    .const('phi_0', 0) \

continuation_steps.add_step('bisection') \
    .num_cases(201) \
    .const('h_f', h_f) \
    .const('v_f', v_f)

continuation_steps.add_step('bisection') \
    .num_cases(101) \
    .const('gam_f', gam_f)

continuation_steps.add_step('bisection') \
    .num_cases(101) \
    .const('h_0', h_0) \
    .const('v_0', v_0)

continuation_steps.add_step('bisection') \
    .num_cases(91) \
    .const('xi', np.pi/2)

beluga.add_logger(file_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    optim_options={'control_method': 'differential', 'analytical_jacobian': False},
    initial_helper=True,
    save_sols='space_shuttle.beluga',
    autoscale=True
)
