"""Brachistochrone example."""
import beluga
import logging
from math import pi

ocp = beluga.OCP('brachisto')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v*cos(theta)', 'm') \
   .state('y', 'v*sin(theta)', 'm') \
   .state('v', 'g*sin(theta)', 'm/s')

# Define controls
ocp.control('theta','rad')

# Define constants
ocp.constant('g', -9.81, 'm/s^2')
ocp.constant('x_f', 0, 'm')
ocp.constant('y_f', 0, 'm')

ocp.constant_of_motion('c1', 'lamX', '1/m')
ocp.constant_of_motion('c2', 'lamY', '1/m')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.constraints() \
    .initial('x', 'm')    \
    .initial('y', 'm') \
    .initial('v', 'm/s')  \
    .terminal('x-x_f', 'm')   \
    .terminal('y-y_f', 'm')

ocp.scale(m='y', s='y/v', kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('Shooting')

guess_maker = beluga.guess_generator('auto',
                start=[0,0,0],          # Starting values for states in order
                direction='forward',
                costate_guess = -0.1,
                control_guess=[-pi/2],
                use_control_guess=True,
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .const('x_f', 10) \
                .const('y_f',-10)

beluga.add_logger(logging_level=logging.DEBUG)

sol = beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
