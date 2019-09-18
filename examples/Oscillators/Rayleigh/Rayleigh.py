import beluga
import logging

ocp = beluga.OCP('Rayleigh')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('y1', 'y2', '1') \
   .state('y2', '-y1 + y2*(gam - p*y2**2) + m*u', '1')

# Define controls
ocp.control('u', '1')

# Define constants
ocp.constant('gam', 1.4, '1')
ocp.constant('p', 0.14, '1')
ocp.constant('m', 4, '1')
ocp.constant('y1_0', -5, '1')
ocp.constant('y2_0', -5, '1')
ocp.constant('y1_f', 0, '1')
ocp.constant('y2_f', 0, '1')
ocp.constant('t_f', 4.5, 's')

ocp.constant('epsilon1', 1e4, '1')
ocp.constant('path_min', -10, '1')
ocp.constant('path_max', 10, '1')

# Define costs
ocp.path_cost('(u**2 + y1**2)', '1')

# Define constraints
ocp.constraints() \
    .initial('y1 - y1_0', '1') \
    .initial('y2 - y2_0', '1') \
    .initial('t', 's') \
    .path('u + y1/6', '1', lower='path_min', upper='path_max', activator='epsilon1', method='utm') \
    .terminal('t - t_f', 's') \

ocp.scale(m='y', s='y/v', kg=1, rad=1, nd=1)

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
                .num_cases(30) \
                .const('y1_f', 0) \
                .const('y2_f', 0) \
                .const('t_f', 4.5)

continuation_steps.add_step('bisection') \
                .num_cases(40) \
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
    autoscale=False,
    initial_helper=True
)
