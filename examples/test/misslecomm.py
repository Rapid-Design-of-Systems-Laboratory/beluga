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
ocp.constant('xc1',-0.4,'nd')
ocp.constant('xc2',-0.2,'nd')
ocp.constant('rc',0.1,'nd')
ocp.constant('rj',0.5,'nd')
ocp.constant('rsep',10,'nd')

ocp.quantity('S2C1','((xbar2-xc1)**2)')
ocp.quantity('S2C2','((xbar2-xc2)**2)')
ocp.quantity('u21','(1/(1+exp(-10*(rc**2-S2C1)/rc**2)))')#' + 1/(1+exp(-10*(rc**2-S2C2)/rc**2)))')
ocp.quantity('commLimit','u21*rj**2 + (1-u21)*rsep**2')
ocp.constraints().path('comm1','((xbar-xbar2)**2+(ybar-ybar2)**2)/commLimit','<',1,'nd',start_eps=1e-1)
# ocp.quantity('S2C','((xbar2-xc)**2 + (ybar2-yc)**2)')
# ocp.quantity('u21','(1/(1+exp(-20*(rc**2-S2C)/rc**2)))')
# ocp.quantity('commLimit','u21*rj**2 + (1-u21)*rsep**2')
# ocp.constraints().path('comm1','((xbar-xbar2)**2 + (ybar-ybar2)**2)/commLimit','<',1,'nd',start_eps=1e-1)


# ocp.state('xbar3', 'cos(psi3)', 'nd')\
#    .state('ybar3', 'sin(psi3)', 'nd')\
#    .state('psi3', '10*abar3', 'nd')
# ocp.control('abar3','nd')
#
# ocp.state('xbar4', 'cos(psi4)', 'nd')\
#    .state('ybar4', 'sin(psi4)', 'nd')\
#    .state('psi4', '10*abar4', 'nd')
# ocp.control('abar4','nd')
#
# ocp.state('xbar5', 'cos(psi5)', 'nd')\
#    .state('ybar5', 'sin(psi5)', 'nd')\
#    .state('psi5', '10*abar5', 'nd')
# ocp.control('abar5','nd')


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
    # .initial('S1C - ((xbar_0-xc)**2 + (ybar_0 - yc)**2)','nd^2')\
    # .initial('S2C - ((xbar_0-xc)**2 + (ybar2_0 - yc)**2)','nd^2')\
    # .initial('S21 - ((xbar_0-xbar2_0)**2 + (ybar_0 - ybar2_0)**2)','nd^2')
    # .independent('tf - 1', 'nd')

# ocp.constraints() \
#     .path('l1','ybar1/0.5','<',1,'m',start_eps=1e-2)\
#     .path('l2','ybar2/0.5','<',1,'m',start_eps=1e-2)\
#     .path('l3','ybar3/0.5','<',1,'m',start_eps=1e-2)\
#     .path('l4','ybar4/0.5','<',1,'m',start_eps=1e-2)\
    # .path('l3','ybar3','<',0.3,'m',start_eps=1e-8)\
    # .path('l4','ybar4','<',0.3,'m',start_eps=1e-8)
#     .path('u1','abar','<>',1,'nd',start_eps=1e-6) \
#     .path('u2','abar2','<>',1,'nd',start_eps=1e-6)\
#     .path('u3','abar3','<>',1,'nd',start_eps=1e-6)\
#     .path('u4','abar4','<>',1,'nd',start_eps=1e-6)\
#     .path('u5','abar5','<>',1,'nd',start_eps=1e-6)

ocp.constraints() \
    .initial('xbar2-xbar2_0','nd')\
    .initial('ybar2-ybar2_0','nd')\
    .terminal('xbar2-xbar2_f','nd')\
    .terminal('ybar2-ybar2_f','nd') \
    .terminal('psi2 - psi2_f', 'nd') \

# ocp.constraints() \
#     .initial('xbar3-xbar3_0','nd')\
#     .initial('ybar3-ybar3_0','nd')\
#     .terminal('xbar3-xbar3_f','nd')\
#     .terminal('ybar3-ybar3_f','nd') \
#     .terminal('psi3 - psi3_f', 'nd') \
#
# ocp.constraints() \
#     .initial('xbar4-xbar4_0','nd')\
#     .initial('ybar4-ybar4_0','nd')\
#     .terminal('xbar4-xbar4_f','nd')\
#     .terminal('ybar4-ybar4_f','nd') \
#     .terminal('psi4 - psi4_f', 'nd') \
#
# ocp.constraints() \
#     .initial('xbar5-xbar5_0','nd')\
#     .initial('ybar5-ybar5_0','nd')\
#     .terminal('xbar5-xbar5_f','nd')\
#     .terminal('ybar5-ybar5_f','nd') \
#     .terminal('psi5 - psi5_f', 'nd') \

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
                    N=11
)
#
# guess_maker = beluga.guess_generator('auto',
#                 start=[-.8,0.,0]+[-.8,.1,0.0,1.0],
#                 direction='forward',
#                 costate_guess = [0.0, 0.0, -0.01]+[0.0,0.0,0.01,0.0],#+[0.01,0.01],#+[0,0]*2,
#                 control_guess = [+0.005, -0.005],#+[0.00,0.0],
#                 time_integrate=0.1
# )

guess_maker = beluga.guess_generator('auto',
                start=[-0.8,0.,-pi/12]+[-0.8,.0,pi/12,1.0],
                direction='forward',
                costate_guess = [0.0, 0.0, -0.01]+[0.0,0.0,0.01,0.0]+[0.01,0.01],#+[0,0]*2,
                control_guess = [+0.005, -0.005]+[0.0,0.0],
                time_integrate=0.1,
                use_control_guess=True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .terminal('xbar', 0.0)\
                .terminal('ybar', 0.0) \
                .terminal('psi', +30*pi/180) \
                .terminal('xbar2', 0.0)\
                .terminal('ybar2', 0.0) \
                .terminal('psi2', -60*pi/180) \
                # .initial('xbar2', -0.8) \
                # .initial('ybar2', 0.1) \
                # .terminal('xbar2', 0.0)\
                # .terminal('ybar2', 0.0) \
                # .terminal('psi2', -60*pi/180) \
                # .initial('xbar3', -0.8) \
                # .initial('ybar3', 0.2) \
                # .terminal('xbar3', 0.0)\
                # .terminal('ybar3', 0.0) \
                # .terminal('psi3', -pi/2)\
                # .initial('xbar4', -0.8) \
                # .initial('ybar4', 0.25) \
                # .terminal('xbar4', 0.0)\
                # .terminal('ybar4', 0.0) \
                # .terminal('psi4', -120*pi/180)\
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
             guess_generator=guess_maker,
             output_file='data2.dill')

# beluga.solve(problem)
#     # from timeit import timeit
#
#     # print(timeit("get_problem()","from __main__ import get_problem",number=10))
#     beluga.run(get_problem())
