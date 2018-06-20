from math import pi
import beluga
ocp = beluga.OCP('jammer')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)*cos(gam)', 'nd')\
   .state('ybar', 'sin(psi)*cos(gam)', 'nd')\
   .state('zbar', '-sin(gam)', 'nd')\
   .state('psi', '10*abar', 'nd')
ocp.control('abar','nd')
ocp.control('gam','nd')

ocp.state('xbar2', 'vbar2*cos(psi2)*cos(gam2)', 'nd')\
   .state('ybar2', 'vbar2*sin(psi2)*cos(gam2)', 'nd')\
   .state('zbar2', '-vbar2*sin(gam2)', 'nd')\
   .state('psi2', '10*abar2', 'nd')\
   .state('vbar2', '0', 'nd/s')

ocp.control('abar2','nd')
ocp.control('gam2','nd')

ocp.constant('xc1',-0.1,'nd')
ocp.constant('slope',40,'nd')
ocp.constant('safeDist',0.02,'nd')
ocp.constant('unsafeDist',0.000001,'nd') # Near target
ocp.constant('ymax',0.2,'nd')


ocp.constant('xc',-0.6,'nd')
ocp.constant('yc',0.0,'nd')
ocp.constant('zc',-0.15,'nd')
ocp.constant('rc',0.05,'nd')

ocp.constraints().path('alt1','sqrt((xbar-xc)**2 + (zbar-zc)**2)/rc','>',1,'nd',start_eps=1e-6)\
                 .path('alt2','sqrt((xbar2-xc)**2 + (zbar2-zc)**2)/rc','>',1,'nd',start_eps=1e-6)

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
    .terminal('ybar-ybar_f','nd')\
    .terminal('zbar-zbar_f','nd')\
    .terminal('psi - psi_f', 'nd') \

ocp.constraints() \
    .initial('xbar2-xbar2_0','nd')\
    .initial('ybar2-ybar2_0','nd')\
    .initial('zbar2-zbar2_0','nd')\
    .terminal('xbar2-xbar2_f','nd')\
    .terminal('ybar2-ybar2_f','nd') \
    .terminal('zbar2-zbar2_f','nd')\
    .terminal('psi2 - psi2_f', 'nd') \

# 1191 (45) - 5 vehicles with 4 path constraints
# 911 seconds for 5 v and one path constraint
# 247(31) seconds for 5 vehicle with GPOPS in background
# 68(14) seconds for 3 vehicle with u constraints
# 114(20) seconds for 4 vehicles with u constraint
# 106(14) seconds for 3 vehicle unconstrained (with u constraints)
# 75(10) seconds for 2 vehicle unconstrainted  (with u constraints)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('Shooting',
                        tolerance=1e-3,
                        max_iterations=200,
                        verbose = True,
                        derivative_method='fd',
                        max_error=20,
             )


bvp_solver = beluga.bvp_algorithm('qcpi',
                        tolerance=1e-3,
                        max_iterations=300,
                        verbose = True,
                        max_error=20,
                        N=141
             )

guess_maker = beluga.guess_generator('auto',
                start=[-.8,0.,-.1,-pi/12.]+[-.8,.1,-.1,0.,1.],
                direction='forward',
                costate_guess = [0., 0., 0., -0.]+[0.,0.,0.,0.,0.]+[0.]*2,
                control_guess = [0.00, .01, -0.00, .01]+[0.0,0.0]*2,
                time_integrate=.1,
                use_control_guess=True,
)

continuation_steps = beluga.init_continuation()
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(101) \
#                 .terminal('xbar', -0.)\
#                 .terminal('ybar', .0) \
#                 .terminal('zbar', 0.) \
#                 .terminal('psi', +0*pi/180) \
#                 .terminal('xbar2', -0.)\
#                 .terminal('ybar2', .0) \
#                 .terminal('zbar2', 0.) \
#                 .terminal('psi2', -0*pi/180) \
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .terminal('psi',15*pi/180)\
#                 .terminal('psi2',-30*pi/180)

guess_maker = beluga.guess_generator('file',filename='data-zs-unc-qcpi.dill',iteration=-1,step=-1)

continuation_steps.add_step('bisection') \
                .num_cases(101) \
                .constant('zc',-0.125)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data.dill')
