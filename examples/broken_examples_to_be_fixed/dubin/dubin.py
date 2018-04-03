"""Ground vehicle path planning problem."""
from math import *
import beluga
import logging

ocp = beluga.OCP('dubin')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x','V*cos(theta)','m')   \
   .state('y','V*sin(theta)','m')  \
   .state('theta','-V/L*delta','rad')


# Define quantities used in the problem

# Define controls
ocp.control('delta','rad')

# Define constants
ocp.constant('L', 1.0, 'm')
ocp.constant('V', 1.0, 'm/s')
ocp.constant('rad2sec', 1.0, 's/(rad^2)')
ocp.constant('w1', 0.5, 'nd')
ocp.constant('steeringLim', 30*pi/180, 'rad')
# Define costs
ocp.path_cost('w1*delta**2 + (1)','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m') \
    .initial('y-y_0','m') \
    .initial('theta-theta_0','rad') \
    .terminal('x-x_f','m')  \
    .terminal('y-y_f','m') \
    .terminal('theta-theta_f','rad') \
    .path('steering','delta - steeringLim','<',0.0,'rad^2')
    # .path('gLoading','(D^2+L^2)/(mass*g0)','<',0.0,'m^2/s^2')


ocp.scale(m='x', s='x/V', rad=1, nd=1)


guess_maker = beluga.guess_generator('auto',
                start=[0,0,pi/4],
                direction='forward',
                time_integrate=1.0,
                costate_guess = 0.0
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(2) \
                .terminal('y', 1.0) \
                .terminal('x', 1.0) \
                .terminal('theta', pi/2)

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .terminal('y', 5.0) \
                .terminal('x', 5.0) \
                # .initial('theta', pi/2) \
                # .const('L', 3.02)

continuation_steps.add_step('activate_constraint', name='steering')

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .constraint('steering', 0.0, index=1)

# continuation_steps.add_step('bisection').num_cases(21) \
#                 .const('w1', 0.25)
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(11)  \
#                 .terminal('theta', 2*pi/180)
# # .initial('gam',-45*pi/180)\


bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=50,
                        verbose = True,
                        max_error=100
             )

beluga.setup_beluga(logging_level=logging.DEBUG)

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
