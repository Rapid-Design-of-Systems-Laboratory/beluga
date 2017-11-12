from math import pi
ocp = beluga.OCP('twoveh_s2')

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
ocp.constant('xc',-0.6,'nd')
ocp.constant('yc',0.,'nd')
ocp.constant('rc',.1,'nd')

ocp.constant('xc2',-0.3,'nd')
ocp.constant('yc2',0.25,'nd')
ocp.constant('rc2',.125,'nd')

ocp.constraints().path('comm1','sqrt((xbar-xc)**2+(ybar-yc)**2)/rc','>',1,'nd',start_eps=1e-6)\
                 .path('comm2','sqrt((xbar2-xc)**2+(ybar2-yc)**2)/rc','>',1,'nd',start_eps=1e-6)\
                 .path('u1','abar','<>',1,'nd',start_eps=1e-6)\
                 .path('u2','abar2','<>',1,'nd',start_eps=1e-6)\
                 .path('comm3','sqrt((xbar2-xc2)**2+(ybar2-yc2)**2)/rc2','>',1,'nd',start_eps=1e-6)\

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
    .initial('ybar-ybarar2_0','nd')\
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
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

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
                costate_guess = [0., 0., 0., -0.0]+[0.,0.,0.,0.0,0.]+[0.,0.,0.],
                control_guess = [0.00, -.0, -0.00, -.0]+[0.0,0.0]*5,
                time_integrate=.1,
                use_control_guess=True,
)

continuation_steps = beluga.init_continuation()
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .terminal('xbar', -0.6)\
#                 .terminal('ybar', -.25) \
#                 .terminal('zbar', 0.) \
#                 .terminal('psi', +15*pi/180) \
#                 .terminal('xbar2', -.6)\
#                 .terminal('ybar2', .25) \
#                 .terminal('zbar2', 0.) \
#                 .terminal('psi2', -15*pi/180) \
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(21) \
#                 .terminal('xbar', 0.)\
#                 .terminal('ybar', 0.) \
#                 .terminal('xbar2', -0.25)\
#                 .terminal('ybar2', 0.)
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(5) \
#                 .terminal('xbar2', -0.0)

guess_maker = beluga.guess_generator('file',filename='data-twoveh-s2-a.dill',iteration=-1,step=-1)
continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .constant('yc2', 0.15)\
#
# # guess_maker = beluga.guess_generator('file',filename='data-twoveh-s2-b.dill',iteration=-1,step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(21) \
#                 .constant('xc',-0.3)
#
# guess_maker = beluga.guess_generator('file',filename='data-twoveh-s2-a.dill',iteration=-1,step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .terminal('psi2', -pi/2)

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
