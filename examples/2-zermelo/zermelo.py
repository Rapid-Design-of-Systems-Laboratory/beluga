from math import *

import beluga
import logging

ocp = beluga.OCP('zermelos_problem')

def drift_x(x, y):
    return 0

def drift_y(x, y):
    if (x < 0).all():
        return 0*x
    if (x > 10).all():
        return 0*x
    return ((x-5)**4 - 625)/625

ocp.custom_function('drift_x', drift_x)
ocp.custom_function('drift_y', drift_y)

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'V*cos(theta) + drift_x(x,y)', 'm')   \
   .state('y', 'V*sin(theta) + drift_y(x,y)', 'm')

# Define controls
ocp.control('theta', 'rad')

# Define constants
ocp.constant('V', 10, 'm/s')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.constraints() \
    .initial('x-x_0', 'm') \
    .initial('y-y_0', 'm') \
    .terminal('x-x_f', 'm') \
    .terminal('y-y_f', 'm')

ocp.scale(m='x', s='x/V', rad=1)

bvp_solver = beluga.bvp_algorithm('Shooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=100,
                        max_error=100
             )

guess_maker = beluga.guess_generator('auto',
                start=[0,0],
                control_guess=[0],
                use_control_guess = True,
                direction='forward'
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(20) \
                .terminal('x', 10) \
                .terminal('y', 0)

continuation_steps.add_step('bisection') \
                .num_cases(30) \
                .terminal('y', 10)

beluga.add_logger(logging_level=logging.DEBUG)

sol = beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

# This stuff is only used for plotting. Move to plot.py? Can't w/o Issue #96
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,10,10)
Y = np.linspace(0,10,10)
[XX,YY] = np.meshgrid(X, Y)
UU = drift_x(XX, YY)
VV = drift_y(XX, YY)

plt.plot(sol.y[:,0], sol.y[:,1])
plt.quiver(XX,YY,UU,VV)
plt.show()

plt.plot(sol.t, sol.u*180/np.pi)
plt.show()
