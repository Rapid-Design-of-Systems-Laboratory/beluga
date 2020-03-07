"""Bryson-Denham problem"""
# TODO: Costate estimates seem to be off by a factor of -2. See Issue #143

import beluga
import logging

ocp = beluga.OCP()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v', 'm') \
   .state('v', 'u', 'm/s')

# Define controls
ocp.control('u', 'rad')

# Define constants
ocp.constant('x_0', 0, 'm')
ocp.constant('x_f', 0, 'm')
ocp.constant('v_0', 1, 'm')
ocp.constant('v_f', -1, 'm')
ocp.constant('epsilon1', 10, 'rad**2')
ocp.constant('x_max', 0.3, 'm')

# Define costs
ocp.path_cost('u**2', 'rad**2')

# Define constraints
ocp.constraints() \
    .initial_constraint('x - x_0', 'm') \
    .initial_constraint('v - v_0', 'm/s') \
    .initial_constraint('t', 's') \
    .terminal_constraint('x - x_f', 'm') \
    .terminal_constraint('v - v_f', 'm') \
    .terminal_constraint('t - 1', 's')

ocp.path_constraint('x', 'm', lower='-x_max', upper='x_max', activator='epsilon1', method='utm')

ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)

bvp_solver_indirect = beluga.bvp_algorithm('spbvp')

guess_maker_indirect = beluga.guess_generator(
    'auto',
    start=[0, 1],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[-2],
    use_control_guess=True,
    time_integrate=0.1
)


beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(3) \
    .const('x_0', 0) \
    .const('v_0', 1) \
    .const('x_f', 0) \
    .const('v_f', -1)

continuation_steps.add_step('bisection') \
                .num_cases(10, 'log') \
                .const('x_max', 0.1)

continuation_steps.add_step('bisection') \
                .num_cases(10, 'log') \
                .const('epsilon1', 1e-6)

sol_set_indirect = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'analytical_jacobian': True, 'control_method': 'icrm'},
    bvp_algorithm=bvp_solver_indirect,
    steps=continuation_steps,
    guess_generator=guess_maker_indirect,
    autoscale=False,
    save='indirect_data.blg')
