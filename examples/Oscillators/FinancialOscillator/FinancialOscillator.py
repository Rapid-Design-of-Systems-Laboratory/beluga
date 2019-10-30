"""
References
----------
.. [1] Ping Chen and Sardar M.N. Islam. "Optimal Control Models in Finance."
    Kluwer Academic Publishers. DOI: 10.1007/b101888.
"""

import beluga
import numpy as np
import logging

ocp_indirect = beluga.OCP()

# Define independent variables
ocp_indirect.independent('t', 'nd')

# Define equations of motion
ocp_indirect.state('x1', 'T*x2', 'nd')
ocp_indirect.state('x2', '-T*x1 + T*u - T**2*B*x2', 'nd') # 2*sin(u)

# Define controls
ocp_indirect.control('u', 'rad')

# Define constants
ocp_indirect.constant('T', 5, 'nd')
ocp_indirect.constant('B', 0.2, 'nd')
ocp_indirect.constant('x1_0', 3, 'nd')
ocp_indirect.constant('x2_0', 5, 'nd')
ocp_indirect.constant('epsilon1', 10, 'nd')

# Define costs
ocp_indirect.path_cost('(x1 + 5*t - 5)**2', 'nd')

# Define constraints
ocp_indirect.constraints().initial('x1 - x1_0', 'nd')
ocp_indirect.constraints().initial('x2 - x2_0', 'nd')
ocp_indirect.constraints().initial('t', 'nd')
ocp_indirect.path_constraint('u', 'rad', lower='-2', upper='2', activator='epsilon1', method='epstrig')
ocp_indirect.constraints().terminal('t - 1', 'nd')

bvp_solver_indirect = beluga.bvp_algorithm('spbvp')

guess_maker_indirect = beluga.guess_generator(
    'auto',
    start=[3, 5],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0],
    use_control_guess=True,
    time_integrate=0.1
)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(40, 'log') \
    .const('epsilon1', 2e-4)

sol_set_indirect = beluga.solve(
    ocp=ocp_indirect,
    method='indirect',
    optim_options={'analytical_jacobian': True, 'control_method': 'icrm'},
    bvp_algorithm=bvp_solver_indirect,
    steps=continuation_steps,
    guess_generator=guess_maker_indirect,
    autoscale=False,
    save='indirect_data.blg')
