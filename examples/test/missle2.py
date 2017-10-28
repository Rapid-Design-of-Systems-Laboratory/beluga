"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'cos(psi)', 'm')   \
   .state('y', 'sin(psi)', 'm')   \
   .state('psi', 'a/V', 'rad')


# Define controls
ocp.control('a','m/s^2')

# Define constants
ocp.constant('V',30,'m/s')
ocp.constant('tfreal',5,'s')

# Define costs
ocp.path_cost('a^2','m^2/s^4')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m')    \
    .initial('y-y_0','m')    \
    .initial('psi-psi_0','rad')  \
    .terminal('x-x_f','m')   \
    .terminal('y-y_f','m') \
    .terminal('psi - psi_f', 'rad') \
    .independent('tf - tfreal', 'nd')

ocp.scale(m='x', s='tfreal', kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-4,
                        max_iterations=30,
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
                start=[6.0,0,0],          # Starting values for states in order
                direction='forward',
                costate_guess = 0.0,
                control_guess = [0.0001],
                time_integrate=1.0
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(41) \
                .initial('x', 12000) \
                .initial('y', 0.0) \
                .terminal('x', 0.0)\
                .terminal('y', 0.0) \
                .terminal('psi', 0.0)

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .terminal('psi', -pi/3)

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .initial('psi', 30*pi/180)
beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

# beluga.solve(problem)
#     # from timeit import timeit
#
#     # print(timeit("get_problem()","from __main__ import get_problem",number=10))
#     beluga.run(get_problem())
