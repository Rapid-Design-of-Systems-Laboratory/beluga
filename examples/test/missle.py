"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)', 'nd')   \
   .state('ybar', 'sin(psi)', 'nd')   \
   .state('psi', 'abar', 'nd')


# Define controls
ocp.control('abar','nd')

# Define constants
ocp.constant('tfreal',50,'s')
ocp.constant('V',300,'m/s')

# Define costs
ocp.path_cost('abar^2','s')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')    \
    .initial('ybar-ybar_0','nd')    \
    .initial('psi-psi_0','nd')  \
    .terminal('xbar-xbar_f','nd')   \
    .terminal('ybar-ybar_f','nd') \
    .independent('tf - 1', 'nd')

ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-4,
                        max_iterations=200,
                        verbose = True,
                        derivative_method='fd',
                        max_error=100,
             )

# bvp_solver = beluga.bvp_algorithm('SingleShooting',
#                     derivative_method='fd',
#                     tolerance=1e-4,
#                     max_iterations=50,
#                     verbose = True,
# )

guess_maker = beluga.guess_generator('auto',
                start=[0,0,0],          # Starting values for states in order
                direction='reverse',
                costate_guess = [0.0, 0.0, 1.0],
                control_guess = [0.05],
                time_integrate=1.0
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .initial('xbar', -0.8) \
                .initial('ybar', 0.0) \
                .terminal('xbar', 0.0)\
                .terminal('ybar', 0.0) \
                .terminal('psi', 0.0)

# continuation_steps.add_step('bisection') \
#                 .num_cases(5) \
#                 .terminal('psi', -pi/3)
#
continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .initial('psi', 30*pi/180)
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
