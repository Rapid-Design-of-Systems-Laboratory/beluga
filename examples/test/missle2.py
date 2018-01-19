"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)', 'nd')   \
   .state('ybar', 'sin(psi)', 'nd')   \
   .state('psi', 'abar', 'nd')

ocp.state('xbar2', 'cos(psi2)', 'nd')   \
   .state('ybar2', 'sin(psi2)', 'nd')   \
   .state('psi2', 'abar2', 'nd')

# Define controls
ocp.control('abar','nd')
ocp.control('abar2','nd')

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

# Define costs
ocp.path_cost('abar^2 + abar2^2','nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')    \
    .initial('ybar-ybar_0','nd')    \
    .initial('psi-psi_0','nd')  \
    .terminal('xbar-xbar_f','nd')   \
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd') \
    .independent('tf - 1', 'nd')

ocp.constraints() \
    .initial('xbar2-xbar2_0','nd')    \
    .initial('ybar2-ybar2_0','nd')    \
    .initial('psi2-psi2_0','nd')  \
    .terminal('xbar2-xbar2_f','nd')   \
    .terminal('ybar2-ybar2_f','nd') \
    .terminal('psi2 - psi2_f', 'nd') \

ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-4,
                        max_iterations=30,
                        verbose = True,
                        derivative_method='fd',
                        max_error=100,
             )

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-4,
                    max_iterations=50,
                    verbose = True,
)

guess_maker = beluga.guess_generator('auto',
                start=[-0.8,0,pi/6, -0.8,0,pi/3],          # Starting values for states in order
                direction='forward',
                costate_guess = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1],
                control_guess = [-0.05, -0.05],
                time_integrate=1.0
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .initial('xbar', -0.8) \
                .initial('ybar', 0.0) \
                .initial('psi', pi/6) \
                .terminal('xbar', 0.0)\
                .terminal('ybar', 0.0) \
                .terminal('psi', -pi/3)

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .initial('xbar2', -0.8) \
                .initial('ybar2', 0.0) \
                .initial('psi2', pi/3) \
                .terminal('xbar2', 0.0)\
                .terminal('ybar2', 0.0) \
                .terminal('psi2', -pi/2)

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
