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
   .state('psi2', '10*abar2/vbar2', 'nd')\
   .state('vbar2', '0', 'nd/s')

ocp.control('abar2','nd')
ocp.control('gam2','nd')

# Jammer location
ocp.constant('xc',-0.4,'nd')
ocp.constant('yc',0.,'nd')
ocp.constant('rc',.1,'nd')
#
# ocp.quantity('S2C','((xbar2-xc)**2 + (ybar2-yc)**2)')
# ocp.quantity('u21','(1/(1+exp(-20*(rc**2-S2C)/rc**2)))')
# ocp.quantity('S21','(xbar2-xbar)**2 + (ybar2-ybar)**2')
# ocp.quantity('commLimit','u21*rj**2 + (1-u21)*rsep**2')
ocp.constraints().path('u1','abar','<>',1,'nd',start_eps=1e-4)\
                 .path('u2','abar2','<>',1,'nd',start_eps=1e-4)\
                 # .path('comm1','S21/commLimit','<',1,'nd',start_eps=1e-4)

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

# Define costs
# ocp.path_cost('abar^2 + abar2^2 + abar3^2 + abar4^2 + 0^2','nd')
ocp.path_cost('abar^2 + gam^2 + abar2^2 + gam2^2', 'nd')
# ocp.path_cost('1','s')

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

ocp.constraints() \
    .initial('xbar2-xbar2_0','nd')\
    .initial('ybar2-ybar2_0','nd')\
    .terminal('xbar2-xbar2_f','nd')\
    .terminal('ybar2-ybar2_f','nd') \
    .terminal('psi2 - psi2_f', 'nd') \
    .initial('zbar2-zbar2_0','nd')\
    .terminal('zbar2-zbar2_f','nd')

# 1191 (45) - 5 vehicles with 4 path constraints
# 911 seconds for 5 v and one path constraint
# 247(31) seconds for 5 vehicle with GPOPS in background
# 68(14) seconds for 3 vehicle with u constraints
# 114(20) seconds for 4 vehicles with u constraint
# 106(14) seconds for 3 vehicle unconstrained (with u constraints)
# 75(10) seconds for 2 vehicle unconstrainted  (with u constraints)
ocp.scale(m=1, s=1, kg=1, rad=1, nd='xbar')

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-3,
                        max_iterations=50,
                        verbose = True,
                        derivative_method='fd',
                        max_error=100,
             )

guess_maker = beluga.guess_generator('auto',
                start=[-.8,0.,-.1,-pi/12]+[-.8,.1,-.1,0.,1.],
                direction='forward',
                costate_guess = [0., 0., 0., -0.]+[0.,0.,0.,0.,0.1],#+[0.]
                control_guess = [+0.0, -.1, -0.0, -.1]+[0.1,0.1,0.1,0.1],
                time_integrate=.1
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .terminal('xbar', 0.)\
                .terminal('ybar', 0.) \
                .terminal('zbar', 0.) \
                .terminal('psi', +15*pi/180) \
                .terminal('xbar2', 0.)\
                .terminal('ybar2', 0.) \
                .terminal('zbar2', 0.) \
                .terminal('psi2', -15*pi/180) \


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data.dill')

# beluga.solve(problem)
#     # from timeit import timeit
#
#     # print(timeit("get_problem()","from __main__ import get_problem",number=10))
#     beluga.run(get_problem())
