import beluga
import logging

ocp = beluga.OCP()

# Define independent variables
ocp.independent('t', '1')

# Define equations of motion
ocp.state('y1', 'y2', 'm') \
   .state('y2', '-y1 + y2*(gam - p*y2**2) + m*u', 'm')

# Define controls
ocp.control('u', 'm')

# Define constants
ocp.constant('gam', 1.4, '1')
ocp.constant('p', 0.14, '1/m**2')
ocp.constant('m', 4, '1')
ocp.constant('y1_0', -5, 'm')
ocp.constant('y2_0', -5, 'm')
ocp.constant('y1_f', 0, 'm')
ocp.constant('y2_f', 0, 'm')
ocp.constant('t_f', 4.5, '1')

ocp.constant('epsilon1', 1e3, 'm**2')
ocp.constant('path_min', -10, 'm')
ocp.constant('path_max', 10, 'm')

# Define costs
ocp.path_cost('(u**2 + y1**2)', 'm**2')

# Define constraints
ocp.initial_constraint('y1 - y1_0', 'm')
ocp.initial_constraint('y2 - y2_0', 'm')
ocp.initial_constraint('t', '1')
ocp.terminal_constraint('t - t_f', '1')

ocp.path_constraint('u + y1/6', 'm', lower='path_min', upper='path_max', activator='epsilon1', method='utm')

ocp.scale(m='y1')

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[-5, -5],
    costate_guess=-0.1,
    control_guess=[1],
    use_control_guess=True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .const('y1_f', 0) \
                .const('y2_f', 0) \
                .const('t_f', 4.5)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('path_min', -1) \
                .const('path_max', 0)

continuation_steps.add_step('bisection') \
                .num_cases(100, 'log') \
                .const('epsilon1', 1e-5)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'icrm', 'analytical_jacobian': True},
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    initial_helper=True
)
