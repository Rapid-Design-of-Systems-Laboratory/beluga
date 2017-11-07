"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)', 'nd')   \
   .state('ybar', 'sin(psi)', 'nd')   \
   .state('psi', '10*abar', 'nd')
ocp.control('abar','nd')

ocp.state('xbar2', 'cos(psi2)', 'nd')   \
   .state('ybar2', 'sin(psi2)', 'nd')   \
   .state('psi2', '10*abar2', 'nd')
ocp.control('abar2','nd')

ocp.state('xbar3', 'cos(psi3)', 'nd')   \
   .state('ybar3', 'sin(psi3)', 'nd')   \
   .state('psi3', '10*abar3', 'nd')
ocp.control('abar3','nd')

ocp.state('xbar4', 'cos(psi4)', 'nd')   \
   .state('ybar4', 'sin(psi4)', 'nd')   \
   .state('psi4', '10*abar4', 'nd')
ocp.control('abar4','nd')

ocp.state('xbar5', 'cos(psi5)', 'nd')   \
   .state('ybar5', 'sin(psi5)', 'nd')   \
   .state('psi5', '10*abar5', 'nd')
ocp.control('abar5','nd')

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

# Define costs
ocp.path_cost('abar^2 + abar2^2 + abar3^2 + abar4^2 + abar5^2','nd')
# ocp.path_cost('1','nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')    \
    .initial('ybar-ybar_0','nd')    \
    .terminal('xbar-xbar_f','nd')   \
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd') \
    .independent('tf - 1', 'nd')

ocp.constraints() \
    .path('u1','abar','<>',1,'nd',start_eps=1e-3) \
    .path('u2','abar2','<>',1,'nd',start_eps=1e-3)\
    .path('u3','abar3','<>',1,'nd',start_eps=1e-3)\
    .path('u4','abar4','<>',1,'nd',start_eps=1e-3)\
    .path('u5','abar5','<>',1,'nd',start_eps=1e-3)

ocp.constraints() \
    .initial('xbar2-xbar2_0','nd')    \
    .initial('ybar2-ybar2_0','nd')    \
    .terminal('xbar2-xbar2_f','nd')   \
    .terminal('ybar2-ybar2_f','nd') \
    .terminal('psi2 - psi2_f', 'nd') \

ocp.constraints() \
    .initial('xbar3-xbar3_0','nd')    \
    .initial('ybar3-ybar3_0','nd')    \
    .terminal('xbar3-xbar3_f','nd')   \
    .terminal('ybar3-ybar3_f','nd') \
    .terminal('psi3 - psi3_f', 'nd') \

ocp.constraints() \
    .initial('xbar4-xbar4_0','nd')    \
    .initial('ybar4-ybar4_0','nd')    \
    .terminal('xbar4-xbar4_f','nd')   \
    .terminal('ybar4-ybar4_f','nd') \
    .terminal('psi4 - psi4_f', 'nd') \

ocp.constraints() \
    .initial('xbar5-xbar5_0','nd')    \
    .initial('ybar5-ybar5_0','nd')    \
    .terminal('xbar5-xbar5_f','nd')   \
    .terminal('ybar5-ybar5_f','nd') \
    .terminal('psi5 - psi5_f', 'nd') \

# 68 seconds for 3 vehicle with u constraints
# 114 seconds for 4 vehicles with u constraint
# 106(14) seconds for 3 vehicle unconstrained (with u constraints)
# 75(10) seconds for 2 vehicle unconstrainted  (with u constraints)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-4,
                        max_iterations=30,
                        verbose = True,
                        derivative_method='fd',
                        max_error=100,
             )

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-3,
                    max_iterations=500,
                    verbose = True,
)

guess_maker = beluga.guess_generator('auto',
                start=[-0.8,0,0.0,-0.8,0.1,0.0,-0.8,0.2,0.0, -0.8,-0.3,0.0, -0.8,-0.4,0.0],          # Starting values for states in order
                direction='forward',
                costate_guess = [0.0, 0.0, 0.1]*5,
                control_guess = [-0.05, -0.05, -0.5, -0.5, -0.5, 0,0,0,0,0, 0,0,0,0,0],
                time_integrate=1.0
)

# guess_maker = beluga.guess_generator('auto',
#                 start=[-0.8,0,0],
#                 direction='forward',
#                 costate_guess = [0.0, 0.0, 0.1],
#                 control_guess = [-0.05, 0.0, 0.0],
#                 time_integrate=1.0
# )
#
continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(5) \
                .initial('xbar', -0.8) \
                .initial('ybar', 0.0) \
                .terminal('xbar', 0.0)\
                .terminal('ybar', 0.0) \
                .terminal('psi', -30*pi/180) \
                .initial('xbar2', -0.8) \
                .initial('ybar2', 0.1) \
                .terminal('xbar2', 0.0)\
                .terminal('ybar2', 0.0) \
                .terminal('psi2', -60*pi/180) \
                .initial('xbar3', -0.8) \
                .initial('ybar3', 0.2) \
                .terminal('xbar3', 0.0)\
                .terminal('ybar3', 0.0) \
                .terminal('psi3', -pi/2)\
                .initial('xbar4', -0.8) \
                .initial('ybar4', 0.3) \
                .terminal('xbar4', 0.0)\
                .terminal('ybar4', 0.0) \
                .terminal('psi4', -120*pi/180)
                .initial('xbar5', -0.8) \
                .initial('ybar5', 0.3) \
                .terminal('xbar5', 0.0)\
                .terminal('ybar5', 0.0) \
                .terminal('psi5', -150*pi/180)
# continuation_steps.add_step('bisection') \
#                 .num_cases(21) \

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
