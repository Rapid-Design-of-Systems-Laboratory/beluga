from math import pi
ocp = beluga.OCP('nofly_n')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)*cos(gam)', 'nd')\
   .state('ybar', 'sin(psi)*cos(gam)', 'nd')\
   .state('zbar', '-sin(gam)', 'nd')\
   .state('psi', '20*abar', 'nd')
ocp.control('abar','nd')
ocp.control('gam','nd')

import numpy as np
n = 5

path_cost = 'abar^2 + gam^2'
y0_pos = np.array([-0.05, 0.1, 0.15, -0.1,-0.15,-0.2]) #np.linspace(-0.3, 0.3, n+1)
yf_pos = np.array([0.0, 0.0, 0.0, -0.05,-0.05,-0.05])
psi_vec = np.array([+15*pi/180, -15*pi/180, -30*pi/180, 30*pi/180, 45*pi/180]) #np.linspace(45*pi/180, -45*pi/180, n+1)

# psi_vec = np.linspace(15*pi/180, -15*pi/180, n+1)
# y_pos = np.linspace(0.0, 0.2, n+1)
guess_start = [-0.8,y0_pos[0],-.1,0.]
for i in range(2,n+1):
    ocp.state(f'xbar{i}', f'vbar{i}*cos(psi{i})*cos(gam{i})', 'nd')\
       .state(f'ybar{i}', f'vbar{i}*sin(psi{i})*cos(gam{i})', 'nd')\
       .state(f'zbar{i}', f'-vbar{i}*sin(gam{i})', 'nd')\
       .state(f'psi{i}', f'20*abar{i}', 'nd')\
       .state(f'vbar{i}', '0', 'nd/s')
    ocp.control(f'abar{i}','nd')
    ocp.control(f'gam{i}','nd')

    ocp.constraints() \
        .initial(f'xbar{i}-xbar{i}_0','nd')\
        .initial(f'ybar{i}-ybar{i}_0','nd')\
        .initial(f'zbar{i}-zbar{i}_0','nd')\
        .terminal(f'xbar{i}-xbar{i}_f','nd')\
        .terminal(f'ybar{i}-ybar{i}_f','nd')\
        .terminal(f'zbar{i}-zbar{i}_f','nd')\
        .terminal(f'psi{i} - psi{i}_f', 'nd')

    ocp.constraints()\
        .path(f'zone1{i}',f'sqrt((xbar{i}-xc)**2 + (ybar{i}-yc)**2)/rc','>',1,'nd',start_eps=1e-4)\
        .path(f'u{i}',f'abar{i}','<>',1,'nd',start_eps=1e-3)
        # .path(f'zone2{i}',f'ybar{i}','<',0.30,'nd',start_eps=1e-4)\

    path_cost = path_cost + f' + abar{i}^2 + gam{i}^2'
    guess_start = guess_start + [-0.8,y0_pos[i-1],-.1,0.,1.]

# ocp.constraints().path(f'dist1','sqrt((xbar-xbar4)**2 + (ybar-ybar4)**2 + (zbar-zbar4)**2)','>',1,'nd',start_eps=1e-4)
ocp.constant('xc',-0.6,'nd')
ocp.constant('yc',0.0,'nd')
ocp.constant('rc',0.1,'nd')

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')

# Define costs
ocp.path_cost(path_cost,'nd')
# ocp.path_cost('abar^2 + gam^2 + abar2^2 + gam2^2', 'nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')\
    .initial('ybar-ybar_0','nd')\
    .initial('zbar-zbar_0','nd')\
    .terminal('xbar-xbar_f','nd')\
    .terminal('ybar-ybar_f','nd')\
    .terminal('zbar-zbar_f','nd')\
    .terminal('psi - psi_f', 'nd') \


ocp.constraints()\
    .path(f'zone10',f'sqrt((xbar-xc)**2 + (ybar-yc)**2)/rc','>',1,'nd',start_eps=1e-4)\
    .path('u1','abar','<>',1,'nd',start_eps=1e-3)
    # .path(f'zone21',f'ybar','<',0.30,'nd',start_eps=1e-4)\

ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

# bvp_solver = beluga.bvp_algorithm('MultipleShooting',
#                         tolerance=1e-3,
#                         max_iterations=200,
#                         verbose = True,
#                         derivative_method='fd',
#                         max_error=20,
#              )
#

bvp_solver = beluga.bvp_algorithm('qcpi',
                        tolerance=1e-6,
                        max_iterations=200,
                        verbose = True,
                        max_error=20,
                        N=31
             )

guess_maker = beluga.guess_generator('auto',
                start=guess_start,
                direction='forward',
                costate_guess = [0., 0., 0.,0.]+[0.,0.,0.,0.,0.]*(n-1)+[0.]*n,
                control_guess = [0.00, .0]*n+[0.0,0.0]*n*2,
                time_integrate=.05,
                # use_control_guess=True,
)

# 1848 seconds with 4 vehicles, N = 101
# 2540.27 seconds with 5 vehicles, N = 101
continuation_steps = beluga.init_continuation()

step1 = continuation_steps.add_step('bisection') \
                .num_cases(21)

step1.terminal('xbar', -0.6)\
    .terminal('ybar', -0.25) \
    .terminal('zbar', 0.) \
    .terminal('psi', psi_vec[0]) \

step2 = continuation_steps.add_step('bisection') \
                .num_cases(51)\
                .terminal('xbar',0.0)\
                .terminal('ybar',yf_pos[0])

for i in range(2,n+1):
    y_sign = y0_pos[i-1]/abs(y0_pos[i-1])
    step1.terminal(f'xbar{i}', -0.6)\
        .terminal(f'ybar{i}', y_sign*0.25) \
        .terminal(f'zbar{i}', 0) \
        .terminal(f'psi{i}', psi_vec[i-1]) \

    step2.terminal(f'xbar{i}', 0.)\
        .terminal(f'ybar{i}', yf_pos[i-1]) \

# # Test for decreasing all eps to 1e-5 with N = 150
# continuation_steps.add_step('bisection') \
#                 .num_cases(111) \
#                 .const('eps_zone10',1e-5)\
#                 .const('eps_zone12',1e-5) \
#                 .const('eps_zone13',1e-5) \
#                 .const('eps_zone14',1e-5) \
#                 .const('eps_zone15',1e-5)

# eps to 1e-6 with N=80
# guess_maker = beluga.guess_generator('file',filename='data-5v-eps5-all-2hrs.dill', iteration=-1, step=-1)

# tol = 1e-6
# 31 - 1e-4
# 81 - 1e-5
# 151 - 1e-6
# continuation_steps.add_step('bisection') \
#                 .num_cases(201) \
#                 .const('eps_zone10',1e-6)\
#                 .const('eps_zone12',1e-6) \
#                 .const('eps_zone13',1e-6) \
#                 .const('eps_zone14',1e-6) \
#                 .const('eps_zone15',1e-6)

guess_maker = beluga.guess_generator('file',filename='data-5v-eps5-all-2hrs.dill', iteration=-1, step=-1)

continuation_steps.add_step('bisection') \
                .num_cases(201) \
                .const('eps_zone10',1e-6)\
                .const('eps_zone12',1e-6) \
                .const('eps_zone13',1e-6) \
                .const('eps_zone14',1e-6) \
                .const('eps_zone15',1e-6)


#
# guess_maker = beluga.guess_generator('file',filename='data-qcpi-ulim-5v.dill', iteration=-1, step=-1)
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .terminal('psi3',-120*pi/180)\

# guess_maker = beluga.guess_generator('file',filename='data-5v-nominal.dill', iteration=-1, step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .terminal('psi3',-189*pi/180)\
#
# guess_maker = beluga.guess_generator('file',filename='data-qcpi-5v-psi3-179.dill', iteration=-1, step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .terminal('psi5',179*pi/180)\

# guess_maker = beluga.guess_generator('file',filename='data-5v-nominal.dill', iteration=-1, step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .constant('yc',0.15)\

# guess_maker = beluga.guess_generator('file',filename='data-5v-nominal.dill', iteration=-1, step=-1)
# continuation_steps.add_step('bisection', num_divisions=3) \
#                 .num_cases(41) \
#                 .constant('rc',0.16)\

# guess_maker = beluga.guess_generator('file',filename='data-qcpi-5v-psi3-179-psi5-120.dill', iteration=-1, step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .terminal('psi5',179*pi/180)\

# Test for decreasing eps with N = 1001
# guess_maker = beluga.guess_generator('file',filename='data-5v-nominal.dill', iteration=-1, step=-1)
# continuation_steps.add_step('bisection') \
#                 .num_cases(41) \
#                 .const('eps_zone10',1e-4)\

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data.dill')
