"""
Goddard Rocket Problem Example.
Comparison to Goddard example in for OpenGoddard
https://github.com/istellartech/OpenGoddard/blob/master/examples/04_Goddard_0knot.py
"""

import beluga
import logging
from math import pi, sqrt

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', '1')

# Define quantities used in the problem
ocp.quantity('drag', '1 * d_c * v**2 * exp(-h_c * (h - h_0) / h_0)')
ocp.quantity('g', 'g_0 * (h_0 / h)**2')

# Define equations of motion
ocp.state('h', 'v', 'm') \
   .state('v', '(thrust - drag)/m - g', 'm/s') \
   .state('m', '-thrust/c', 'kg')

# Define controls
ocp.control('thrust', '1')

# Define constants' numeric values
g_0 = 1.0

h_0 = 1.0
v_0 = 0.0
m_0 = 1.0

t_c = 3.5
h_c = 500
v_c = 620
m_c = 0.6

tar_m_f = m_0 * m_c
c = 0.5 * sqrt(g_0 * h_0)
d_c = 0.5 * v_c * m_0 / g_0
thrust_max = t_c * g_0 * m_0

# Define constants
ocp.constant('g_0', g_0, '1')  # Gravity at surface

ocp.constant('t_c', t_c, '1')      # Constant for computing max thrust
ocp.constant('h_c', h_c, '1')      # Constant for height
ocp.constant('v_c', v_c, '1')      # Constant for velocity
ocp.constant('m_c', m_c, '1')      # Terminal mass fraction

ocp.constant('c', c, '1')          # Thrust to fuel ratio
ocp.constant('d_c', d_c, '1')      # Drag scaling
ocp.constant('T_max', thrust_max, '1')  # Max thrust
ocp.constant('T_min', 0, '1')

# Define constants for BCs
ocp.constant('h_0', h_0, '1')
ocp.constant('v_0', v_0, '1')
ocp.constant('m_0', m_0, '1')

ocp.constant('v_f', v_0, '1')
ocp.constant('m_f', tar_m_f, '1')

# Define smoothing constant
ocp.constant('eps', 0.01, '1')

# Define costs
ocp.terminal_cost('-h', '1')

# Define constraints
ocp.initial_constraint('h - h_0', '1')
ocp.initial_constraint('v - v_0', '1')
ocp.initial_constraint('m - m_0', '1')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('v - v_f', '1')
ocp.terminal_constraint('m - m_f', '1')

ocp.path_constraint('thrust', '1', lower='T_min', upper='T_max', activator='eps', method='epstrig')

ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[h_0, v_0, m_0],    # Starting values for states in order
    costate_guess=-0.0001,
    control_guess=[pi/3],
    time_integrate=0.1,
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step() \
    .num_cases(3) \
    .const('v_f', 0)

continuation_steps.add_step() \
    .num_cases(3, spacing='log') \
    .const('m_f', tar_m_f)

continuation_steps.add_step() \
    .num_cases(10, spacing='log') \
    .const('eps', 0.000005)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'algebraic'},
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    autoscale=False,
    initial_helper=True,
)
