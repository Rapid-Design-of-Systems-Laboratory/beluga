"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.quantity('xbardot','cos(psi)*cos(gam)')
ocp.quantity('ybardot','sin(psi)*cos(gam)')
ocp.quantity('zbardot','-sin(gam)')
ocp.state('xbar', 'xbardot', 'nd')\
   .state('ybar', 'ybardot', 'nd')\
   .state('zbar', 'zbardot', 'nd')\
   .state('psi', '10*abar', 'nd')
ocp.control('abar','nd')
ocp.control('gam','nd')

ocp.quantity('xbar2dot','vbar2*cos(psi2)*cos(gam2)')
ocp.quantity('ybar2dot','vbar2*sin(psi2)*cos(gam2)')
ocp.quantity('zbar2dot','-vbar2*sin(gam2)')
ocp.state('xbar2', 'xbar2dot', 'nd')\
   .state('ybar2', 'ybar2dot', 'nd')\
   .state('zbar2', 'zbar2dot', 'nd')\
   .state('psi2', '10*abar2', 'nd')\
   .state('vbar2', '0', 'nd/s')

ocp.control('abar2','nd')
ocp.control('gam2','nd')

# Jammer location
ocp.constant('xc',-0.4,'nd')
ocp.constant('yc',0.0,'nd')
ocp.constant('rc',0.2,'nd')
ocp.constant('rj',0.16,'nd')
ocp.constant('rsep',10,'nd')

ocp.quantity('S2C','((xbar2-xc)**2 + (ybar2-yc)**2)')
ocp.quantity('u21','(1/(1+exp(-20*(rc**2-S2C)/rc**2)))')
ocp.quantity('S21','(xbar2-xbar)**2 + (ybar2-ybar)**2')
ocp.quantity('commLimit','u21*rj**2 + (1-u21)*rsep**2')
ocp.constraints().path('comm1','S21/commLimit','<',1,'nd',start_eps=1e-1)
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

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

# Define costs
# ocp.path_cost('abar^2 + abar2^2 + abar3^2 + abar4^2 + 0^2','nd')
ocp.path_cost('abar^2 + gam^2 + abar2^2 + gam2^2', 'nd')
# ocp.path_cost('1','nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')\
    .initial('ybar-ybar_0','nd')\
    .initial('zbar-zbar_0','nd')\
    .terminal('xbar-xbar_f','nd')\
    .terminal('ybar-ybar_f','nd') \
    .terminal('zbar-zbar_f','nd') \
    .terminal('psi - psi_f', 'nd') \
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
    .initial('zbar2-zbar2_0','nd')\
    .terminal('zbar2-zbar2_f','nd')

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
# 247(31) seconds for 5 vehicle with GPO constraint
# 106(14) seconds for 3 vehicle unconstrained (with u constraints)
# 75(10) seconds for 2 vehicle unconstrainted  (with u constraints)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)


# 1191 (45) - 5 vehicles with 4 path constraints
# 911 seconds for 5 v and one path constraint
# 247(31) seconds for 5 vehicle with GPO

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-3,
                    max_iterations=350,
                    verbose = True,
                    N=251
)
#
# guess_maker = beluga.guess_generator('auto',
#                 start=[-.8,0.,-.1,-pi/12]+[-.8,.1,-.1,0.]+[0.16,0.17,0.01],
#                 direction='forward',
#                 costate_guess = [0.0, 0.0, 0.0, -0.01]+[0.0,0.0,0.0,0.01]+[0.0,0.0,0.0],#+[0.1],#+[0,0]*2,
#                 control_guess = [+0.005, -0.1, -0.005, -0.1],#+[0.1,0.1],
#                 time_integrate=1.0
# )
#
# guess_maker = beluga.guess_generator('auto',
#                 start=[-.8,0.,-.1,-pi/12]+[-.8,.1,-.1,0.,1.],
#                 direction='forward',
#                 costate_guess = [0.0, 0.0, 0.0, -0.01]+[0.0,0.0,0.0,0.01,0.0]+[0.0],#+[0,0]*2,
#                 control_guess = [+0.005, -0.1, -0.005, -0.1]+[0.00,0.0],
#                 time_integrate=0.1
# )
#
# continuation_steps = beluga.init_continuation()
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(21) \
#                 .terminal('xbar', 0.0)\
#                 .terminal('ybar', 0.0) \
#                 .terminal('zbar', 0.0) \
#                 .terminal('psi', +15*pi/180) \
#                 .terminal('xbar2', 0.0)\
#                 .terminal('ybar2', 0.0) \
#                 .terminal('zbar2', 0.0) \
#                 .terminal('psi2', -30*pi/180) \
#                 # .initial('xbar2', -0.8) \
#                 # .initial('ybar2', 0.1) \
#                 # .terminal('xbar2', 0.0)\
#                 # .terminal('ybar2', 0.0) \
#                 # .terminal('psi2', -60*pi/180) \
#                 # .initial('xbar3', -0.8) \
#                 # .initial('ybar3', 0.2) \
#                 # .terminal('xbar3', 0.0)\
#                 # .terminal('ybar3', 0.0) \
#                 # .terminal('psi3', -pi/2)\
#                 # .initial('xbar4', -0.8) \
#                 # .initial('ybar4', 0.25) \
#                 # .terminal('xbar4', 0.0)\
#                 # .terminal('ybar4', 0.0) \
#                 # .terminal('psi4', -120*pi/180)\
#                 # .initial('xbar5', -0.8) \
#                 # .initial('ybar5', -0.1) \
#                 # .terminal('xbar5', 0.0)\
#                 # .terminal('ybar5', 0.0) \
#                 # .terminal('psi5', 30*pi/180)

# guess_maker = beluga.guess_generator('file',filename='data-3d2v-rj03.dill', iteration=-1, step=-1)
#
# continuation_steps = beluga.init_continuation()
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(5) \
#                 .const('rj',0.24)
#
#

guess_maker = beluga.guess_generator('file',filename='data-3d2v-rj024.dill', iteration=-1, step=-1)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(2) \
                .const('rj',0.15)


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data4.dill')

# beluga.solve(problem)
#     # from timeit import timeit
#
#     # print(timeit("get_problem()","from __main__ import get_problem",number=10))
#     beluga.run(get_problem())
