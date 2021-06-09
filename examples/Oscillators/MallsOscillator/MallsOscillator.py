"""
References
----------
.. [1] Longuski, James M., José J. Guzmán, and John E. Prussing. Optimal control with aerospace applications.
    Springer New York, 2014.

.. [2] Mall, Kshitij, and Michael J. Grant. "Epsilon-trig regularization method for bang-bang optimal control problems."
    AIAA Atmospheric Flight Mechanics Conference. 2016.
"""

import beluga
import logging

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x1', 'x2', '1') \
   .state('x2', '-x1 + u', '1')

# Define controls
ocp.control('u', '1')

# Define constants
ocp.constant('x1_0', 1, '1')
ocp.constant('x2_0', 1, '1')
ocp.constant('x1_f', 0, '1')
ocp.constant('x2_f', 0, '1')
ocp.constant('epsilon1', 1, '1')
ocp.constant('u_max', 1, '1')
ocp.constant('u_min', -1, '1')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.initial_constraint('x1 - x1_0', '1')
ocp.initial_constraint('x2 - x2_0', '1')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('x1 - x1_f', '1')
ocp.terminal_constraint('x2 - x2_f', '1')

ocp.path_constraint('u', '1', lower='u_min', upper='u_max', activator='epsilon1', method='epstrig')

bvp_solver_indirect = beluga.bvp_algorithm('spbvp')

guess_maker_indirect = beluga.guess_generator(
    'auto',
    start=[0, 0],
    direction='forward',
    costate_guess=-0.5,
    control_guess=[-.6],
    use_control_guess=True,
    time_integrate=0.5
)

beluga.add_logger(file_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('x1_0', 1) \
    .const('x2_0', 1) \
    .const('x1_f', 0) \
    .const('x2_f', 0)

continuation_steps.add_step('bisection') \
                .num_cases(10, 'log') \
                .const('epsilon1', 5e-1)

continuation_steps.add_step('bisection') \
                .num_cases(10, 'log') \
                .const('epsilon1', 1e-3)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'analytical_jacobian': True, 'control_method': 'differential'},
    bvp_algorithm=bvp_solver_indirect,
    steps=continuation_steps,
    guess_generator=guess_maker_indirect,
    autoscale=False,
    initial_helper=True
)
