"""
References
----------
.. [1] Aly, G. M. and Chan, W. C. "Application of a modified quasilinearization technique to totally singular optimal control problems."
    International Journal of Control 17.4 (1973): 809-815.
"""

import beluga
import logging

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x1', 'x2', 'm')
ocp.state('x2', 'u', 'm/s')
ocp.state('x3', '1/2*(x2**2 - x1**2)', '1')

# Define controls
ocp.control('u', 'm/s**2')

# Define constants
ocp.constant('x1_0', 0, 'm')
ocp.constant('x2_0', 1, 'm/s')
ocp.constant('x3_0', 0, '1')
ocp.constant('epsilon1', 10, '1/s')
ocp.constant('u_max', 1, 'm/s**2')

# Define costs
ocp.terminal_cost('x3', '1')

# Define constraints
ocp.initial_constraint('x1 - x1_0', 'm')
ocp.initial_constraint('x2 - x2_0', 'm/s')
ocp.initial_constraint('x3 - x3_0', '1')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('t - 3.1415/2', 's')

ocp.path_constraint('u', 'rad', lower='-u_max', upper='u_max', activator='epsilon1', method='utm')

ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)

bvp_solver_indirect = beluga.bvp_algorithm('spbvp')

guess_maker_indirect = beluga.guess_generator(
    'auto',
    start=[0, 0, 0],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0.0],
    use_control_guess=True,
    time_integrate=3.1415/2
)


beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(60, 'log') \
                .const('epsilon1', 1e-9)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'analytical_jacobian': True, 'control_method': 'differential'},
    bvp_algo=bvp_solver_indirect,
    steps=continuation_steps,
    guess_gen=guess_maker_indirect,
    autoscale=False,
    initial_helper=False)
