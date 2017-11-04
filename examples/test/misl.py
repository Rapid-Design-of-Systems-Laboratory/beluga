"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'cos(psi)', 'nd')   \
   .state('y', 'sin(psi)', 'nd')   \
   .state('psi', 'u', 'rad')

# Define controls
ocp.control('u','rad/s')

# Define constants
ocp.constant('V',100,'m/s')

ocp.constant('xc', -5,'nd')
ocp.constant('yc', 10.0,'nd')
ocp.constant('rc', 2.0,'nd')

# Define costs
ocp.path_cost('u**2','rad^2/s^2')
# ocp.path_cost('1','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','nd')    \
    .initial('y-y_0','nd')    \
    .terminal('x-x_f','nd')   \
    .terminal('y-y_f','nd') \
    .path('control','u','<>',10,'rad/s',start_eps=1e-4) \
    # .path('keepOut1','(x-xc)**2/rc**2','>',1.0,'nd**2',start_eps=1e-6)\
    # .path('keepOut2','(y-yc)**2/rc**2','>',1.0,'nd**2',start_eps=1e-6)

# ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)
ocp.scale(m=1, s=1, kg=1, rad=1, nd='x')

# bvp_solver = beluga.bvp_algorithm('MultipleShooting',
#                         tolerance=1e-4,
#                         max_iterations=200,
#                         verbose = True,
#                         derivative_method='fd',
#                         max_error=100,
#  )
#
bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-4,
                    max_iterations=200,
                    verbose = True,
                    N = 61
)

guess_maker = beluga.guess_generator('auto',
                start=[-1.0,0,0],          # Starting values for states in order
                direction='forward',
                costate_guess = [0.0,0.0,0.1],#,0.0,0.0],
                control_guess = [-0.05,0,0],#,0,0],
                use_control_guess=True,
                time_integrate=0.1
)
# guess_maker = beluga.guess_generator('auto',
#                 start=[-10.0,0,0],          # Starting values for states in order
#                 direction='forward',
#                 costate_guess = [0.0,0.0,0.1,0.0,0.0,0.0,0.0],
#                 control_guess = [-0.05,0,0,0,0,0,0],
#                 use_control_guess=True,
#                 time_integrate=0.1
# )


continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .initial('x', -10.0) \
                .initial('y', 0.0) \
                .terminal('x', 0.0)\
                .terminal('y', 0.0) \

# continuation_steps.add_step('bisection') \
#                 .num_cases(5) \
#                 .initial('x', -2.0) \
#                 .initial('y', 0.0) \
#                 .terminal('x', 0.0)\
#                 .terminal('y', 0.0)

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .constant('yc',5.0)

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .constant('eps_keepOut1',1e-4)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

# beluga.solve(problem)
#     # from timeit import timeit
#
#     # print(timeit("get_problem()","from __main__ import get_problem",number=10))
#     beluga.run(get_problem())
