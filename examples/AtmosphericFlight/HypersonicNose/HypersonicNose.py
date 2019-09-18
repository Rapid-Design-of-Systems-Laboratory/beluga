"""
References
----------
.. [1] Buttazzo, Giuseppe, and Bernhard Kawohl. "On Newton’s problem of minimal resistance."
    The Mathematical Intelligencer 15.4 (1993): 7-12.
"""

import beluga
import logging
import matplotlib.pyplot as plt

ocp = beluga.OCP('hypersonic_nose')

# Define independent variables
ocp.independent('l', 'm')

# Define equations of motion
ocp.state('r', '-u', 'm')

# Define controls
ocp.control('u', 'm/s')

# Define constants
ocp.constant('r_0', 1, 'm')
ocp.constant('eps1', 1, '1')

# Define costs
ocp.path_cost('4*r*u**3/(1+u**2)', 'm')

# Define constraints
ocp.constraints() \
    .initial('r - r_0', 'm') \
    .initial('l - 0', 'm') \
    .path('u', 'm/s', lower='-5', upper='5', method='utm', activator='eps1') \
    .terminal('r', 'm') \
    .terminal('l - 2', 'm')

ocp.scale(m='x', rad=1)

guess_maker = beluga.guess_generator('ones',
                start=[1.0],          # Starting values for states in order
                costate_guess = 0.1,
                control_guess=[0.35],
                use_control_guess=True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10, 'log') \
                .const('eps1', 1e-1)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

bvp_solver = beluga.bvp_algorithm('spbvp')

beluga.solve(ocp=ocp,
             method='indirect',
             optim_options={'control_method': 'icrm'},
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             autoscale=False,
             save='indirect_data.blg')

bvp_solver = beluga.bvp_algorithm('Collocation', num_nodes=60)

beluga.solve(ocp=ocp,
             method='direct',
             bvp_algorithm=bvp_solver,
             steps=None,
             guess_generator=guess_maker,
             autoscale=False,
             save='direct_data.blg')
