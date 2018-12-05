"""Brachistochrone example."""
import beluga
from beluga.bvpsol import Solution
import numpy as np
import logging
from math import pi

ocp = beluga.OCP('brachisto')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'time_final*v*cos(theta)', 'm') \
   .state('y', 'time_final*v*sin(theta)', 'm') \
   .state('v', 'time_final*g*sin(theta)', 'm/s')

ocp.constant_of_motion('c1', 'lamX', 's/m')
ocp.constant_of_motion('c2', 'lamY', 's/m')

# Define controls
ocp.control('theta','rad')

ocp.parameter('time_final','s')

# Define constants
ocp.constant('g', -9.81, 'm/s^2')
ocp.constant('x_f', 0.1, 'm')
ocp.constant('y_f', 0.1, 'm')

# Define costs
# ocp.path_cost('1', '1')
ocp.terminal_cost('time_final','s')

# Define constraints
ocp.constraints() \
    .initial('x', 'm')    \
    .initial('y', 'm') \
    .initial('v', 'm/s')  \
    .terminal('x-x_f', 'm')   \
    .terminal('y-y_f', 'm')

ocp.scale(m='y', s='y/v', kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('Collocation')
solinit = Solution(t=np.linspace(0,1,num=4), y=np.array([[0.01,0,0],[0.033,0.033,0],[0.066,0.066,0],[0.1,0.1,0]]), q=np.array([]), u=np.array([[-pi/2],[-pi/2],[-pi/2],[-pi/2]]))
solinit.dynamical_parameters = np.array([1, 0.1])
solinit.aux['const'] = {'g': -9.81, 'x_f': 0.1, 'y_f': 0.1}

guess_maker = beluga.guess_generator('static', solinit=solinit)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .const('x_f', 10) \
                .const('y_f',-10)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.DEBUG)

sol = beluga.solve(ocp,
             method='direct',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker, autoscale=False)
