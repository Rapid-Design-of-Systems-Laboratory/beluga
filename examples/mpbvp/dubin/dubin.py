"""Ground vehicle path planning problem."""
from math import *

ocp = beluga.OCP('dubin')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x','V*cos(theta)','m')   \
   .state('y','V*sin(theta)','m')  \
   .state('theta','-V/L*(delta)','rad')


# Define quantities used in the problem

# Define controls
ocp.control('delta','rad')

# Define constants
ocp.constant('L', 1.0, 'm')
ocp.constant('V', 1.0, 'm/s')
ocp.constant('rad2sec', 1.0, 's/(rad^2)')

# Define costs
ocp.path_cost('0.01*delta**2*(rad2sec) + 1','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m') \
    .initial('y-y_0','m') \
    .initial('theta-theta_0','rad') \
    .terminal('x-x_f','m')  \
    .terminal('y-y_f','m')
    # .path('heatRate','(k*sqrt(rho0*exp(-h/H)/rn)*v^3)*Wsec3pkg - heatRateLimit','<',0.0,'W') \
    # .path('gLoading','(D^2+L^2)/(mass*g0)','<',0.0,'m^2/s^2')


ocp.scale(m='x**2+y**2', s=1, rad=1, nd=1)


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
                .terminal('x', 1.0)

continuation_steps.add_step('bisection') \
                .num_cases(31) \
                .terminal('y', 20.0) \
                .terminal('x', 20.0)

continuation_steps.add_step().num_cases(11) \
                .initial('theta', pi/2)
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

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
