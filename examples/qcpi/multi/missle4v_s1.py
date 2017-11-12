"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)*cos(gam)', 'nd')\
   .state('ybar', 'sin(psi)*cos(gam)', 'nd')\
   .state('zbar', '-sin(gam)', 'nd')\
   .state('psi', '10*abar', 'nd')
ocp.control('abar','nd')
ocp.control('gam','nd')

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

ocp.constraints() \
    .initial('xbar-xbar_0','nd')\
    .initial('ybar-ybar_0','nd')\
    .terminal('xbar-xbar_f','nd')\
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd') \
    .path(f'zone11',f'sqrt((xbar-xc)**2+(ybar-yc)**2)/rc','>',1,'nd',start_eps=1e-6)

import numpy as np
n = 2

psi_vec = np.linspace(45*pi/180, -45*pi/180, n+1)
ocp.constant('xc',-0.4,'nd')
ocp.constant('yc',0.,'nd')
ocp.constant('rc',0.15,'nd')

path_cost = 'abar^2'
y_pos = np.linspace(-0.3, 0.3, n+1)
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
        .terminal(f'psi{i} - psi{i}_f', 'nd')\
        .path(f'zone1{i}',f'sqrt((xbar{i}-xc)**2+(ybar{i}-yc)**2)/rc','>',1,'nd',start_eps=1e-6)

    path_cost = path_cost + f' + abar{i}^2'
    guess_start = guess_start + [-0.8,y_pos[i-1],0.,1.]

# Define costs
ocp.path_cost(path_cost,'nd')

# Define constraints

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
                    N=41
)

guess_maker = beluga.guess_generator('auto',
                start=guess_start,
                direction='forward',
                costate_guess = [0.0, 0.0, 0.01]+[0.,0.,0.01,0.]*(n-1)+[0,0]*n,
                control_guess = [-0.005]*n+[0.0,0.0]*n,
                time_integrate=.1
)

continuation_steps = beluga.init_continuation()

step1 = continuation_steps.add_step('bisection') \
                .num_cases(11)\
                .terminal('xbar', -0.4)\
                .terminal('ybar', -.25) \
                .terminal('psi',psi_vec[0]) \

step2 = continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .terminal('xbar', 0.)\
                .terminal('ybar', 0.) \



for i in range(2,n+1):
    y_sign = y_pos[i-1]/abs(y_pos[i-1])
    step1.terminal(f'xbar{i}', 0.4)\
        .terminal(f'ybar{i}', y_sign*0.25) \
        .terminal(f'psi{i}', psi_vec[i-1]) \

    step2.terminal(f'xbar{i}', 0.)\
        .terminal(f'ybar{i}', 0.) \

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
