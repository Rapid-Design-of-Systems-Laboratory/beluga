"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missilecom')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.quantity('xbardot','cos(psi)')
ocp.quantity('ybardot','sin(psi)')
ocp.state('xbar', 'xbardot', 'nd')\
   .state('ybar', 'ybardot', 'nd')\
   .state('psi', '10*abar', 'nd')
ocp.control('abar','nd')

ocp.quantity('xbar2dot','vbar2*cos(psi2)')
ocp.quantity('ybar2dot','vbar2*sin(psi2)')
ocp.state('xbar2', 'xbar2dot', 'nd')\
   .state('ybar2', 'ybar2dot', 'nd')\
   .state('psi2', '10*abar2', 'nd')\
   .state('vbar2', '0', 'nd/s')

ocp.control('abar2','nd')

# Jammer location
ocp.constant('xc',-0.6,'nd')
ocp.constant('yc',0.0,'nd')
ocp.constant('rc',0.2,'nd')
ocp.constant('rj',0.8,'nd')
ocp.constant('rsep',10,'nd')

ocp.quantity('S2C','((xbar2-xc)**2 + (ybar2-yc)**2)')
ocp.quantity('u21','(1/(1+exp(-20*(rc**2-S2C)/rc**2)))')
ocp.quantity('commLimit','u21*rj**2 + (1-u21)*rsep**2')
ocp.constraints().path('comm1','((xbar-xbar2)**2 + (ybar-ybar2)**2)/commLimit','<',1,'nd',start_eps=1e-1)

# Define costs
# ocp.path_cost('abar^2 + abar2^2 + abar3^2 + abar4^2 + 0^2','nd')
ocp.path_cost('abar^2 + abar2^2', 'nd')
# ocp.path_cost('1','nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')\
    .initial('ybar-ybar_0','nd')\
    .terminal('xbar-xbar_f','nd')\
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd') \

ocp.constraints() \
    .initial('xbar2-xbar2_0','nd')\
    .initial('ybar2-ybar2_0','nd')\
    .terminal('xbar2-xbar2_f','nd')\
    .terminal('ybar2-ybar2_f','nd') \
    .terminal('psi2 - psi2_f', 'nd') \

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
#                         max_iterations=50,
#                         verbose = True,
#                         derivative_method='fd',
#                         max_error=100,
#              )

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-3,
                    max_iterations=250,
                    verbose = True,
                    N=121,
)

guess_maker = beluga.guess_generator('file',filename='data-2d2v-rj08.dill', iteration=-1, step=-1)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(4) \
                .const('rj',0.15)\
                .const('xc',-0.4)

# 995 econds to go from 0.8 to 0.15

guess_maker = beluga.guess_generator('file',filename='data-2d2v-rj015.dill', iteration=-1, step=-1)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(4) \
                .const('rj',0.10)


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
