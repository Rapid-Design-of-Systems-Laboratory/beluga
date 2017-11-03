"""Ground vehicle path planning problem."""
import beluga
from math import *

ocp = beluga.OCP('dubin')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x','v*cos(theta)','m')   \
   .state('y','v*sin(theta)','m')  \
   .state('v','(a+1)/2','m/s') \
   .state('theta','-v/L*delta','rad')
# ocp.state('x1','v1*cos(theta1)','m')   \
#    .state('y1','v1*sin(theta1)','m')  \
#    .state('theta1','-V/L*delta1','rad')\
#    .state('v1','(a1+1)/2','m/s')


# Define quantities used in the problem

# Define controls
ocp.control('a','m/s^2')
ocp.control('delta','rad')
# ocp.control('delta1','rad')
# ocp.control('a1','m/s^2')

# Define constants
ocp.constant('L', 1.0, 'm')
ocp.constant('V', 1.0, 'm/s')
ocp.constant('steeringLim', 40*pi/180, 'rad')
# Define costs
ocp.path_cost('1','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m') \
    .initial('y-y_0','m') \
    .initial('theta-theta_0','rad') \
    .terminal('x-x_f','m')  \
    .terminal('y-y_f','m') \
    .terminal('theta-theta_f','rad') \
    .path('steering','delta','<>','steeringLim','rad', start_eps=1) \
    .path('accLimit','a','<>',1.0,'m/s^2',start_eps=1)

# ocp.scale(m='x', s='x/V', rad=1, nd=1)
ocp.scale(m=1, s=1, rad=1, nd=1)

guess_maker = beluga.guess_generator('auto',
                start=[0,0,0.1, pi/4],
                direction='forward',
                time_integrate=1.0,
                costate_guess = -0.01,
                control_guess = [0.1, 0.0, 0.1, 0.1, 0.1, 0.1],
                use_control_guess=False
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .terminal('y', 5.0) \
                .terminal('x', 5.0) \
                .terminal('theta', pi/4)

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .terminal('y1', 0.0) \
                .terminal('x1', 5.0) \
                .terminal('theta', -pi/4)

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .terminal('y', 5.0) \
#                 .terminal('x', 5.0) \
#                 .terminal('theta', pi/4)
#

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .constant('eps_steering', 1.0)

# continuation_steps.add_step('activate_constraint', name='steering')


bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                derivative_method='fd',
                tolerance=1e-4,
                max_iterations=250,
                verbose = True,
                max_error=100
             )


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data_dubin.dill')
