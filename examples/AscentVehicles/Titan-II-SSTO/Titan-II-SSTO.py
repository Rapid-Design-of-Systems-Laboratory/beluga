import beluga
import logging

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v_x', 'm') \
   .state('y', 'v_y', 'm') \
   .state('v_x', 'F/mass*cos(theta) - D/mass*v_x/sqrt(v_x**2 + v_y**2)', 'm/s') \
   .state('v_y', 'F/mass*sin(theta) - D/mass*v_y/sqrt(v_x**2 + v_y**2) - g', 'm/s') \
   .state('mass', 'md*eps', 'kg')

# Define controls
ocp.control('theta', 'rad')

ocp.quantity('D', '1/2*rho_ref*exp(-y/Hscale)*CD*A*(v_x**2 + v_y**2)')

# Define constants
ocp.constant('F', 2.1e6, 'newton')
ocp.constant('A', 7.069, 'm^2')
ocp.constant('mu', 3.986004e14, 'm^3/s^2')
ocp.constant('Re', 6378100, 'm')
ocp.constant('CD', 0.5, '1')
ocp.constant('rho_ref', 0, 'kg/m^3')
ocp.constant('Hscale', 8.44e3, 'm')
ocp.constant('g', 9.80665, 'm/s^2')
ocp.constant('md', -807.6, 'kg/s')
ocp.constant('eps', 0.000, '1')

ocp.constant('x_0', 0, 'm')
ocp.constant('y_0', 0, 'm')
ocp.constant('v_x_0', 0, 'm/s')
ocp.constant('v_y_0', 0.01, 'm/s')
ocp.constant('mass_0', 60880, 'kg')

ocp.constant('y_f', 1.8e5, 'm')
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

ocp.scale(m='y', s='y/v_x', kg='mass', newton='mass*v_x^2/y', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[0, 0, 0, 0.01, 60880],          # Starting values for states in order
    costate_guess=-0.1,
    control_guess=[0],
    use_control_guess=False
)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('eps', 1) \
                .const('mass_0', 1.1702e5)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('rho_ref', 1.225)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver,
    optim_options={'control_method': 'algebraic'},
    steps=continuation_steps,
    guess_generator=guess_maker,
    autoscale=True
)
