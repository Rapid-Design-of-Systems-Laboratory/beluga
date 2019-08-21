"""
References
----------
.. [1] Betts, John T. "Practical methods for optimal control and estimation using nonlinear programming."
    Vol. 19. Siam, 2010.
"""

import beluga
import logging
import numpy as np
import matplotlib.pyplot as plt

ocp = beluga.OCP('HangGlider')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'vx', 'm')   \
   .state('y', 'vy', 'm')  \
   .state('vx', '1/m*(-L*(Vy/vr) - D*(vx/vr))', 'm/s') \
   .state('vy', '1/m*(L*(vx/vr) - D*(Vy/vr) - W)', 'm/s')

# Define quantities used in the problem
ocp.quantity('vr', 'sqrt(vx**2 + Vy**2)')
ocp.quantity('CD', 'C0 + k*u**2')
ocp.quantity('D', '0.5*rho*(vx**2 + vy**2)*CD*Aref')
ocp.quantity('L', '0.5*rho*(vx**2 + vy**2)*u*Aref')
ocp.quantity('Vy', 'vy - um*(1-X)*exp(-X)')
ocp.quantity('X', '(x/R - um)**2')

# Define controls
ocp.control('u', 'rad')

# Define constants
ocp.constant('um', 0.1, '1')
ocp.constant('R', 100, '1')
ocp.constant('CLmin', 0, '1')
ocp.constant('CLmax', 1.4, '1')
ocp.constant('C0', 0.034, '1')
ocp.constant('k', 0.069662, '1')
ocp.constant('W', 100*9.80665, '1')
ocp.constant('m', 100, 'kg')
ocp.constant('rho', 1.3, 'kg/m^3')  # Sea-level atmospheric density, kg/m^3
ocp.constant('Aref', 14, 'm^2')  # Reference area of vehicle, m^2

ocp.constant('x_0', 0, 'm')
ocp.constant('y_0', 1000, 'm')
ocp.constant('vx_0', 13.227, 'm/s')
ocp.constant('vy_0', -1.287, 'm/s')
ocp.constant('y_f', 900, 'm')
ocp.constant('vx_f', 13.227, 'm/s')
ocp.constant('vy_f', -1.287, 'm/s')

ocp.constant('eps', 100, '1')

# Define costs
ocp.terminal_cost('-x', 'm')

# Define constraints
ocp.constraints() \
    .initial('x - x_0', 'm') \
    .initial('y - y_0', 'm') \
    .initial('vx - vx_0', 'm/s') \
    .initial('vy - vy_0', 'm/s') \
    .initial('t', 's') \
    .terminal('y - y_f', 'm') \
    .terminal('vx - vx_f', 'm/s') \
    .terminal('vy - vy_f', 'm/s') \
    .path('u', 'rad', lower='CLmin', upper='CLmax', activator='eps', method='epstrig')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[0, 905, 13.2275675, -1.28750052],
    direction='forward',
    control_guess=[0.9],
    use_control_guess=True,
    costate_guess=[-.1, -1, -1, 0],
    time_integrate=3,
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('y_f', 900) \
                .const('vx_f', 13.2275675) \
                .const('vy_f', -1.28750052)

continuation_steps.add_step('bisection') \
                .num_cases(20) \
                .const('y_0', 1000)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('um', 2.5)

continuation_steps.add_step('bisection') \
                .num_cases(5, 'log') \
                .const('eps', 8)

continuation_steps.add_step('bisection') \
                .num_cases(15, 'log') \
                .const('eps', 4)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'icrm'},
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    autoscale=False,
    initial_helper=True
)

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.y[:,0], sol.y[:,1])
plt.title('Trajectory')
plt.ylabel('Vertical Position [m]')
plt.xlabel('Horizontal Position [m]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,0])
plt.ylabel('Horizontal Position [m]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,1])
plt.ylabel('Vertical Position [m]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,2])
plt.ylabel('Horizontal Velocity [m/s]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,3])
plt.ylabel('Vertical Velocity [m/s]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u[:, 0])
plt.ylabel('Lift Coefficient')
plt.xlabel('Time [s]')
plt.grid(True)
plt.show()
