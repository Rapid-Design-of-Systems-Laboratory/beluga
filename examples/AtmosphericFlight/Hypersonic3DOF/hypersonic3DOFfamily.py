"""
References
----------
.. [1] Vinh, Nguyen X., Adolf Busemann, and Robert D. Culp. "Hypersonic and planetary entry flight mechanics."
    NASA STI/Recon Technical Report A 81 (1980).
"""

from math import pi
import beluga
import logging

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

rho = 'rho0*exp(-h/H)'
Cl = '(1.5658*alpha + -0.0000)'
Cd = '(1.6537*alpha**2 + 0.0612)'
D = '(0.5*{}*v**2*{}*Aref)'.format(rho, Cd)
L = '(0.5*{}*v**2*{}*Aref)'.format(rho, Cl)
r = '(re+h)'

# Define equations of motion
ocp \
    .state('h', 'v*sin(gam)', 'm') \
    .state('theta', 'v*cos(gam)*cos(psi)/({}*cos(phi))'.format(r), 'rad') \
    .state('phi', 'v*cos(gam)*sin(psi)/{}'.format(r), 'rad') \
    .state('v', '-{}/mass - mu*sin(gam)/{}**2'.format(D, r), 'm/s') \
    .state('gam', '{}*cos(bank)/(mass*v) - mu/(v*{}**2)*cos(gam) + v/{}*cos(gam)'.format(L, r, r), 'rad') \
    .state('psi', '{}*sin(bank)/(mass*cos(gam)*v) - v/{}*cos(gam)*cos(psi)*tan(phi)'.format(L, r), 'rad')

# Define controls
ocp.control('alpha', 'rad') \
    .control('bank', 'rad')

# Define costs
ocp.terminal_cost('-v', 'm/s')

# Define constraints
ocp \
    .initial_constraint('h-h_0', 'm') \
    .initial_constraint('theta-theta_0', 'rad') \
    .initial_constraint('phi', 'rad') \
    .initial_constraint('v-v_0', 'm/s') \
    .initial_constraint('gam-gam_0', 'rad') \
    .initial_constraint('psi-psi_0', 'rad') \
    .initial_constraint('t', 's') \
    .terminal_constraint('h-h_f', 'm') \
    .terminal_constraint('theta-theta_f', 'rad') \
    .terminal_constraint('phi-phi_f', 'rad')

# Define constants
ocp.constant('mu', 3.986e5 * 1e9, 'm**3/s**2')  # Gravitational parameter, m**3/s**2
ocp.constant('rho0', 1.2, 'kg/m**3')  # Sea-level atmospheric density, kg/m**3
ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp.constant('mass', 750 / 2.2046226, 'kg')  # Mass of vehicle, kg
ocp.constant('re', 6378000, 'm')  # Radius of planet, m
ocp.constant('Aref', pi * (24 * .0254 / 2) ** 2, 'm**2')  # Reference area of vehicle, m**2
ocp.constant('rn', 1 / 12 * 0.3048, 'm')  # Nose radius, m
ocp.constant('h_0', 40000, 'm')
ocp.constant('theta_0', 0, 'rad')
ocp.constant('v_0', 2000, 'm/s')
ocp.constant('gam_0', -(90 - 10) * pi / 180, 'rad')
ocp.constant('psi_0', 0, 'rad')
ocp.constant('h_f', 0, 'm')
ocp.constant('theta_f', 0, 'rad')
ocp.constant('phi_f', 0, 'rad')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

# bvp_solver = beluga.bvp_algorithm(
#     'Shooting',
#     derivative_method='fd',
#     tolerance=1e-4,
#     max_iterations=100,
#     max_error=400,
#     algorithm='SLSQP'
# )

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[40000, 0, 0, 2000, -(90 - 10) * pi / 180, 0],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0.0, 0.0],
    use_control_guess=True,
    time_integrate=0.5
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection').num_cases(21) \
    .const('h_f', 0) \
    .const('theta_f', 6945.9 / 6378000)
# Isn't h_f 0 a no-op?

continuation_steps.add_step('bisection').num_cases(3) \
    .const('theta_f', 2 ** -14 * pi / 180)

continuation_steps.add_step('bisection').num_cases(3) \
    .const('gam_0', -(90 - 10) * pi / 180) \
    .const('theta_f', 2 ** -13 * pi / 180)

continuation_steps.add_step('bisection').num_cases(3) \
    .const('phi_f', 2 ** -10 * pi / 180)

continuation_steps.add_step('productspace') \
    .num_subdivisions(6) \
    .const('theta_f', 2 ** -10 * pi / 180) \
    .const('phi_f', 2 ** -6 * pi / 180)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algo=bvp_solver,
    steps=continuation_steps,
    guess_gen=guess_maker,
    initial_helper=True
)
