from math import pi

ocp = beluga.OCP('zermelo1')
ocp.independent('t', 's')
# ocp.state('x','(thr+1)/2*V*cos(theta)','m')
# ocp.state('y','(thr+1)/2*V*sin(theta)+x','m')

ocp.state('x','V*cos(theta)','m')
ocp.state('y','V*sin(theta)','m')
ocp.control('theta','rad')

# ocp.state('x2','v2*cos(theta2)','m')
# ocp.state('y2','v2*sin(theta2)+x2','m')
# ocp.state('v2','0','m/s')
# ocp.control('theta2','rad')

ocp.constant('V',10,'m/s')
ocp.path_cost('1','s')

ocp.constraints().initial('x-x_0','m')\
                .initial('y-y_0','m')\
                .terminal('x-x_f','m')\
                .terminal('y-y_f','m')

# ocp.constraints().initial('x2-x2_0','m')\
#                  .initial('y2-y2_0','m')\
#                  .terminal('x2-x2_f','m')\
#                  .terminal('y2-y2_f','m')

ocp.constraints().path('c1','sqrt((x-xc1)**2 + (y-yc1)**2)','>','rc1','m',start_eps=1e-1) \
                 .path('c2','sqrt((x-xc2)**2 + (y-yc2)**2)','>','rc2','m',start_eps=1e-1) \
                 .path('c3','sqrt((x-xc3)**2 + (y-yc3)**2)','>','rc3','m',start_eps=1e-1)
# ocp.constraints().path('c1','y','>',-1,'nd',start_eps=1e-6)
                # .path('thr1','thr','<>',1,'nd',start_eps=1e-6)

ocp.constant('xc1',1.0,'m') # 1
ocp.constant('yc1',6.0,'m') # 4
ocp.constant('rc1',1.0,'m')

ocp.constant('xc2',7.0,'m') # 7.5
ocp.constant('yc2',4.0,'m') # 3.5
ocp.constant('rc2',1.0,'m')

ocp.constant('xc3',6.0,'m') # 6
ocp.constant('yc3',9.0,'m') # 9
ocp.constant('rc3',1.0,'m')

ocp.scale(m=10, s=1, kg=1, rad=1,nd=1)

# bvp_solver = beluga.bvp_algorithm('MultipleShooting',
#                         derivative_method='fd',
#                         tolerance=1e-4,
#                         max_iterations=30,
#                         verbose = True,
#                         max_error=400,
#              )

bvp_solver = beluga.bvp_algorithm('qcpi',
                        tolerance=1e-4,
                        max_iterations=300,
                        verbose = True,
                        max_error=1000,
                        N=101
             )

guess_maker = beluga.guess_generator('auto',
                start=[0, 0],
                direction='forward',
                # costate_guess = 0.1,
                costate_guess = [-0.1,-0.1,0.0],
)
guess_maker = beluga.guess_generator('auto',
                start=[0, 0],
                direction='forward',
                # costate_guess = 0.1,
                costate_guess = [-0.1,-0.1,0.0,0.0,0.0],
                control_guess = [pi/4,0,0,0,0,0,0],
                use_control_guess=True
)
#
# guess_maker = beluga.guess_generator('auto',
#                 start=[0, 0, 0, 2, 10.0],
#                 direction='forward',
#                 costate_guess = -0.1,
#                 # costate_guess = [-0.1,-0.1,0.0]
# )

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection').num_cases(5)           \
                        .terminal('x',10.0) \
                        .terminal('y',10.0) \
# 500s

# continuation_steps.add_step('bisection').num_cases(11)           \
#                         .const('rc',1.5)


# guess_maker = beluga.guess_generator(mode='file', filename='data-guess.dill', step=-1, iteration=-1)
# continuation_steps.add_step('bisection').num_cases(31, spacing='log') \
#                         .const('yc',0.5) \
                        # .const('xc',5.0) \

# continuation_steps.add_step('bisection').num_cases(11)           \
#                         .terminal('y',15.0) \

# continuation_steps.add_step('bisection').num_cases(41) \
#                         .terminal('y',5) \

# guess_maker = beluga.guess_generator(mode='file', filename='data-3s.dill', step=-1, iteration=-1)
continuation_steps.add_step('bisection').num_cases(11)\
                        .const('xc1',1.75) \
                        .const('yc1',3.5) \
                        .const('xc2',5.75) \
                        .const('yc2',4.0) \
                        # .const('xc3',7.5) \
                        # .const('yc3',8.5)


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
