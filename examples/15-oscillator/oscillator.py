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

import matplotlib.pyplot as plt

ocp = beluga.OCP('oscillator')

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
ocp.constraints() \
    .initial('x1 - x1_0', '1') \
    .initial('x2 - x2_0', '1') \
    .initial('t', 's') \
    .path('u', '1', lower='u_min', upper='u_max', activator='epsilon1', method='epstrig') \
    .terminal('x1 - x1_f', '1')   \
    .terminal('x2 - x2_f', '1')

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

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('x1_0', 1) \
    .const('x2_0', 1) \
    .const('x1_f', 0) \
    .const('x2_f', 0)

continuation_steps.add_step('bisection') \
                .num_cases(5, 'log') \
                .const('epsilon1', 5e-1)

continuation_steps.add_step('bisection') \
                .num_cases(10, 'log') \
                .const('epsilon1', 1e-3)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'analytical_jacobian': True, 'control_method': 'icrm'},
    bvp_algorithm=bvp_solver_indirect,
    steps=continuation_steps,
    guess_generator=guess_maker_indirect,
    autoscale=False,
    initial_helper=True
)

continuation = sol_set[-1]
ind = 0
L = len(continuation)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.y[:, 0], sol.y[:, 1], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('Phase Plot')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.u[:, 0], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('Control History Plot')
plt.xlabel('Time [s]')
plt.ylabel('Control, $u$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.dual[:, 0], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('$\\lambda_{x1}$ History Plot')
plt.xlabel('Time [s]')
plt.ylabel('$\\lambda_{x1}$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.dual[:, 1], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('$\\lambda_{x2}$ History Plot')
plt.xlabel('Time [s]')
plt.ylabel('$\\lambda_{x2}$')
plt.grid(True)
plt.show()
