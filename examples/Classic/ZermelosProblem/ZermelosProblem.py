import beluga
import logging

ocp = beluga.Problem()


# def drift_x(x, y):
#     return 0.0


def drift_y(x):
    return ((x - 5.)**4 - 625)/625


# ocp.custom_function('drift_x', drift_x, 'm', ['m', 'm'])
ocp.custom_function('drift_y', drift_y, 'm', ['m'])

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'V*cos(theta)', 'm')   \
   .state('y', 'V*sin(theta) + drift_y(x)', 'm')

# Define controls
ocp.control('theta', 'rad')

# Define constants
ocp.constant('V', 10, 'm/s')
ocp.constant('x_f', 0, 'm')
ocp.constant('y_f', 0, 'm')
ocp.constant('y_f_width', 2, 'm')
ocp.constant('epsilon', 1e-2, '1')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.initial_constraint('x', 'm')
ocp.initial_constraint('y', 'm')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('x-x_f', 'm')
ocp.terminal_constraint('y-y_f', 'm', lower='-y_f_width', upper='y_f_width', activator='epsilon', method='utm')

ocp.scale(m='x', s='x/V', rad=1)

bvp_solver = beluga.bvp_algorithm('SPBVP')

guess_maker = beluga.guess_generator(
    'auto',
    start=[0, 0],
    control_guess=[0],
    use_control_guess=True,
    direction='forward'
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('x_f', 10)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('y_f', 0)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('y_f_width', 0.25)

continuation_steps.add_step('bisection') \
                .num_cases(20, 'log') \
                .const('epsilon', 1e-8)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

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
