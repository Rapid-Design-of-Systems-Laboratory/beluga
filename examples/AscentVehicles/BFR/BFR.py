import beluga
import logging
import numpy as np

bfr_diameter = 9

Hscale = 8.44e3

bfr_thrust0_sea = 1.993e6*31
bfr_thrust0_vac = 2.295e6*31
bfr_thrust1_sea = 1.993e6*7
bfr_thrust1_vac = 2.295e6*7

bfr_mass0 = 4400e3
bfr_mass0f = 1335e3
bfr_mass1 = 1335e3
bfr_mass1f = 85e3

bfr_massflow0 = -615.8468*31
bfr_massflow1 = -615.8468*7

"""
Step 1
"""

ocp = beluga.Problem(name='BFR')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v_x', 'm')
ocp.state('y', 'v_y', 'm')
ocp.state('v_x', 'Thrust/mass*cos(theta) - D/mass*v_x/sqrt(v_x**2 + v_y**2)', 'm/s')
ocp.state('v_y', 'Thrust/mass*sin(theta) - D/mass*v_y/sqrt(v_x**2 + v_y**2) - g', 'm/s')
ocp.state('mass', 'mass_flow*eps', 'kg')

# Define controls
ocp.control('theta', 'rad')

ocp.quantity('engine0', 'F0_sea*exp(-y/Hscale) + F0_vac*(1-exp(-y/Hscale))')
ocp.quantity('engine1', 'F1_sea*exp(-y/Hscale) + F1_vac*(1-exp(-y/Hscale))')
ocp.quantity('D', '1/2*rho_ref*exp(-y/Hscale)*CD*A*(v_x**2 + v_y**2)')

ocp.switch('Thrust', ['engine0', 'engine1'], [['mass_0f - mass'], ['mass - mass_0f']], 'stage_tol')
ocp.switch('mass_flow', ['md0', 'md1'], [['mass_0f - mass'], ['mass - mass_0f']], 'stage_tol')


# Define constants
ocp.constant('stage_tol', 100, '1')

ocp.constant('F0_sea', 2.1e6, 'newton')
ocp.constant('F0_vac', 2.1e6, 'newton')
ocp.constant('F1_sea', 2.1e6, 'newton')
ocp.constant('F1_vac', 2.1e6, 'newton')
ocp.constant('A', 7.069, 'm^2')
ocp.constant('mu', 3.986004e14, 'm^3/s^2')
ocp.constant('Re', 6378100, 'm')
ocp.constant('CD', 0.5, '1')
ocp.constant('rho_ref', 0, 'kg/m^3')
ocp.constant('Hscale', Hscale, 'm')
ocp.constant('g', 9.80665, 'm/s^2')
ocp.constant('md0', -807.6, 'kg/s')
ocp.constant('md1', -807.6, 'kg/s')
ocp.constant('eps', 0.000, '1')

ocp.constant('x_0', 0, 'm')
ocp.constant('y_0', 0, 'm')
ocp.constant('v_x_0', 0, 'm/s')
ocp.constant('v_y_0', 0.01, 'm/s')
ocp.constant('mass_0', 60880, 'kg')
ocp.constant('mass_0f', 0, 'kg')
ocp.constant('drop_mass', 2000, 'kg')
ocp.constant('y_f', 1.5e5, 'm')
ocp.constant('v_y_f', 0, 'm/s')

# Define costs
ocp.path_cost('1', 's')

# Define constraints
ocp.initial_constraint('x - x_0', 'm')
ocp.initial_constraint('y - y_0', 'm')
ocp.initial_constraint('v_x - v_x_0', 'm/s')
ocp.initial_constraint('v_y - v_y_0', 'm/s')
ocp.initial_constraint('mass - mass_0', 'kg')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('y - y_f', 'm')
ocp.terminal_constraint('v_x - sqrt(mu/(y_f+Re))', 'm/s')
ocp.terminal_constraint('v_y - v_y_f', 'm/s')

ocp.scale(m='y', s='y/v_x', kg='mass', newton='mass*v_x**2/y', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[0., 0., 0., 0.01, 60880.],          # Starting values for states in order
    costate_guess=-0.1,
    control_guess=[0.001],
    use_control_guess=True
)

beluga.add_logger(file_level=logging.INFO, display_level=logging.DEBUG)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(60) \
                .const('A', np.pi*(bfr_diameter/2)**2) \
                .const('eps', 1) \
                .const('mass_0', bfr_mass0) \
                .const('mass_0f', bfr_mass0f) \
                .const('F0_sea', bfr_thrust0_sea) \
                .const('F0_vac', bfr_thrust0_vac) \
                .const('F1_sea', bfr_thrust1_sea) \
                .const('F1_vac', bfr_thrust1_vac) \
                .const('md0', bfr_massflow0) \
                .const('md1', bfr_massflow1) \
                .const('stage_tol', 10)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('rho_ref', 1.225)

continuation_steps.add_step('bisection') \
                .num_cases(20, 'log') \
                .const('stage_tol', 1e-3)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'algebraic', 'analytical_jacobian': False},
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    autoscale=True)
