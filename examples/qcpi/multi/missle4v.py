"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)', 'nd')\
   .state('ybar', 'sin(psi)', 'nd')\
   .state('psi', '10*abar', 'nd')
ocp.control('abar','nd')

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

import numpy as np
n = 4
psi_vec = np.linspace(45*pi/180, 45*pi/180, n)
path_cost = 'abar^2'
guess_start = [-0.8,0,0.]

for i in range(2,n):
    ocp.state(f'xbar{i}', 'vbar{i}*cos(psi{i})', 'nd')\
       .state(f'ybar{i}', 'vbar{i}*sin(psi{i})', 'nd')\
       .state(f'psi{i}', '10*abar{i}', 'nd')\
       .state(f'vbar{i}', '0', 'nd/s')\
    ocp.control('abar{i}','nd')

    ocp.constraints() \
        .initial('xbar{i}-xbar{i}_0','nd')\
        .initial('ybar{i}-ybar{i}_0','nd')\
        .terminal('xbar{i}-xbar{i}_f','nd')\
        .terminal('ybar{i}-ybar{i}_f','nd')\
        .terminal('psi{i} - psi{i}_f', 'nd')

    path_cost = path_cost + f' + abar{i}^2'
    guess_start = guess_start + [-0.8,0.,0.,1.]

# Define costs
ocp.path_cost(path_cost,'nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')\
    .initial('ybar-ybar_0','nd')\
    .terminal('xbar-xbar_f','nd')\
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd') \
    # .independent('tf - 1', 'nd')

# 1191 (45) - 5 vehicles with 4 path constraints
# 911 seconds for 5 v and one path constraint
# 247(31) seconds for 5 vehicle with GPOPS in background
# 68(14) seconds for 3 vehicle with u constraints
# 114(20) seconds for 4 vehicles with u constraint
# 106(14) seconds for 3 vehicle unconstrained (with u constraints)
# 75(10) seconds for 2 vehicle unconstrainted  (with u constraints)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)
#
# bvp_solver = beluga.bvp_algorithm('MultipleShooting',
#                         tolerance=1e-3,
#                         max_iterations=30,
#                         verbose = True,
#                         derivative_method='fd',
#                         max_error=100,
#              )

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-3,
                    max_iterations=100,
                    verbose = True,
                    N=101
)

guess_maker = beluga.guess_generator('auto',
                start=[-0.8,0,0.0,-0.8,0.1,0.0,-0.8,0.2,0.0, -0.8,0.25,0.0],#, -0.8,-0.1,0.0],          # Starting values for states in order
                direction='forward',
                costate_guess = [0.0, 0.0, 0.01]*4+[0,0]*2,
                control_guess = [-0.005]*4+ [0,0]*2,#, 0,0,0,0,0, 0,0,0,0,0],
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
                .num_cases(11) \
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
                .initial('ybar4', 0.25) \
                .terminal('xbar4', 0.0)\
                .terminal('ybar4', 0.0) \
                .terminal('psi4', -120*pi/180)\
                # .initial('xbar5', -0.8) \
                # .initial('ybar5', -0.1) \
                # .terminal('xbar5', 0.0)\
                # .terminal('ybar5', 0.0) \
                # .terminal('psi5', 30*pi/180)
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
