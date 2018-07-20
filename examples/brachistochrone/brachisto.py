"""Brachistochrone example."""
import beluga
import logging
from math import pi
import matplotlib.pyplot as plt

ocp = beluga.OCP('brachisto')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v*cos(theta)', 'm')   \
   .state('y', 'v*sin(theta)', 'm')   \
   .state('v', 'g*sin(theta)', 'm/s')

# Define controls
ocp.control('theta','rad')

# Define constants
ocp.constant('g', -9.81, 'm/s^2')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.constraints() \
    .initial('x-x_0', 'm')    \
    .initial('y-y_0', 'm') \
    .initial('v-v_0', 'm/s')  \
    .terminal('x-x_f', 'm')   \
    .terminal('y-y_f', 'm')

# Use the "adjoined method" to solve for the constraints. (Default is False)
# ocp.constraints().set_adjoined(True)

ocp.scale(m='y', s='y/v', kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('Shooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=200,
                        verbose = True,
                        max_error=100,
                        num_arcs=1,
                        num_cpus=1
             )

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
                .terminal('x', 10) \
                .terminal('y',-10)

beluga.setup_beluga(logging_level=logging.DEBUG)

sol = beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
