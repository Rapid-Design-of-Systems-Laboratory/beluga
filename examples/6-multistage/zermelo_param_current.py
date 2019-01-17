import beluga
import logging

ocp = beluga.OCP('zermelos_problem')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'V*cos(theta)', 'm')   \
   .state('y', 'V*sin(theta) - cur', 'm') \
   # .state('cur', '0', 'm/s')

# Define controls
ocp.control('theta', 'rad')

# Define constants
ocp.constant('V', 10, 'm/s')
ocp.constant('x_f', 0, 'm')
ocp.constant('y_f', 0, 'm')

ocp.parameter('cur', 'm/s')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.constraints() \
    .initial('x', 'm') \
    .initial('y', 'm') \
    .terminal('x-x_f', 'm') \
    .terminal('y-y_f', 'm')

ocp.scale(m='x', s='x/V', rad=1)

bvp_solver = beluga.bvp_algorithm(
    'Shooting',
    derivative_method='fd',
    tolerance=1e-4
)

guess_maker = beluga.guess_generator(
    'auto',
    start=[0, 0],
    quad_guess=[-0.01],
    costate_guess=[-0.01, -0.01],
    param_guess=[0],
    control_guess=[0],
    use_control_guess=True,
    direction='forward'
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .const('x_f', 10)

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .const('y_f', 10)

beluga.add_logger(logging_level=logging.DEBUG)

sol = beluga.solve(
    ocp,
    method='icrm',
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker)
