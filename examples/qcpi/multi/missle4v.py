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
n = 25

psi_vec = np.linspace(45*pi/180, -45*pi/180, n+1)

path_cost = 'abar^2'
y_pos = np.linspace(-0.2, 0.2, n+1)
guess_start = [-0.8,y_pos[0],0]
for i in range(2,n+1):
    ocp.state(f'xbar{i}', f'vbar{i}*cos(psi{i})', 'nd')\
       .state(f'ybar{i}', f'vbar{i}*sin(psi{i})', 'nd')\
       .state(f'psi{i}', f'10*abar{i}', 'nd')\
       .state(f'vbar{i}', '0', 'nd/s')
    ocp.control(f'abar{i}','nd')

    ocp.constraints() \
        .initial(f'xbar{i}-xbar{i}_0','nd')\
        .initial(f'ybar{i}-ybar{i}_0','nd')\
        .terminal(f'xbar{i}-xbar{i}_f','nd')\
        .terminal(f'ybar{i}-ybar{i}_f','nd')\
        .terminal(f'psi{i} - psi{i}_f', 'nd')

    path_cost = path_cost + f' + abar{i}^2'
    guess_start = guess_start + [-0.8,y_pos[i-1],0.,1.]

# Define costs
ocp.path_cost(path_cost,'nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')\
    .initial('ybar-ybar_0','nd')\
    .terminal('xbar-xbar_f','nd')\
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd') \

# 1191 (45) - 5 vehicles with 4 path constraints
# 911 seconds for 5 v and one path constraint
# 247(31) seconds for 5 vehicle with GPOPS in background
# 68(14) seconds for 3 vehicle with u constraints
# 114(20) seconds for 4 vehicles with u constraint
# 106(14) seconds for 3 vehicle unconstrained (with u constraints)
# 75(10) seconds for 2 vehicle unconstrainted  (with u constraints)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-4,
                    max_iterations=100,
                    verbose = True,
                    N=21
)

guess_maker = beluga.guess_generator('auto',
                start=guess_start,
                direction='forward',
                costate_guess = [0.0, 0.0, 0.01]+[0.,0.,0.01,0.]*(n-1),#+[0,0]*2,
                control_guess = [-0.005]*n,#+ [0,0]*2,#, 0,0,0,0,0, 0,0,0,0,0],
                time_integrate=1.0
)

continuation_steps = beluga.init_continuation()

step = continuation_steps.add_step('bisection') \
                .num_cases(2)

step.terminal('xbar', 0.0)\
    .terminal('ybar', 0.0) \
    .terminal('psi', psi_vec[0]) \

for i in range(2,n+1):
    step.terminal(f'xbar{i}', 0.0)\
        .terminal(f'ybar{i}', 0.0) \
        .terminal(f'psi{i}', psi_vec[i-1]) \

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
