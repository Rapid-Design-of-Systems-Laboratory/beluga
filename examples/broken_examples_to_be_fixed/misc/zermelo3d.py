from math import pi

ocp = beluga.OCP('zermelo3')
ocp.independent('t', 's')
# ocp.state('x','(thr+1)/2*V*cos(theta)','m')
# ocp.state('y','(thr+1)/2*V*sin(theta)+x','m')

ocp.state('x','V*cos(theta)*cos(gam)','m')
ocp.state('y','V*sin(theta)*cos(gam)','m')
ocp.state('z','-V*sin(gam)','m')

ocp.control('theta','rad')
ocp.control('gam','rad')

ocp.state('x2','v2*cos(theta2)*cos(gam2)','m')
ocp.state('y2','v2*sin(theta2)*cos(gam2)','m')
ocp.state('z2','-v2*sin(gam2)','m')
ocp.state('v2','0','m/s')

ocp.control('theta2','rad')
ocp.control('gam2','rad')

ocp.constant('V',10,'m/s')
ocp.path_cost('1','s')

ocp.constraints().initial('x-x_0','m')\
                .initial('y-y_0','m')\
                .initial('z-z_0','m')\
                .terminal('x-x_f','m')\
                .terminal('y-y_f','m') \
                .terminal('z-z_f','m')

ocp.constraints().initial('x2-x2_0','m')\
                 .initial('y2-y2_0','m')\
                 .terminal('x2-x2_f','m')\
                 .terminal('y2-y2_f','m')\
                 .initial('z2-z2_0','m')\
                 .terminal('z2-z2_f','m')

ocp.constraints().path('c1','sqrt((x-xc)**2 + (y-yc)**2)','>','rc','m',start_eps=1e-2)\
                 .path('c2','sqrt((x2-xc)**2 + (y2-yc)**2)','>','rc','m',start_eps=1e-2)
# ocp.constraints().path('c1','y','>',-1,'nd',start_eps=1e-6)
                # .path('thr1','thr','<>',1,'nd',start_eps=1e-6)

ocp.constant('xc',5,'m')
ocp.constant('yc',10,'m')
ocp.constant('rc',1.5,'m')
ocp.constant('r1',5.0,'m')

ocp.scale(m=10, s=1, kg=1, rad=1,nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-3,
                        max_iterations=2000,
                        verbose = True,
                        max_error=400,
             )

# bvp_solver = beluga.bvp_algorithm('qcpi',
#                         tolerance=1e-4,
#                         max_iterations=300,
#                         verbose = True,
#                         max_error=1000,
#                         N=121
#              )

guess_maker = beluga.guess_generator('auto',
                start=[0, 0, 0],
                direction='forward',
                costate_guess = 0.1,
                # costate_guess = [-0.1,-0.1,-0.1,0.0]
)

guess_maker = beluga.guess_generator('auto',
                start=[0, 0, 0, 0, 0, 0, 10.0],
                direction='forward',
                # costate_guess = -0.1,
                costate_guess = [-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,0.01,0.01],
                control_guess=[0.0]*8,
                use_control_guess=True
)

continuation_steps = beluga.init_continuation()
#
continuation_steps.add_step('bisection').num_cases(11)           \
                        .terminal('x',10) \
                        .terminal('y',0.0) \
                        .terminal('z',-10.0) \
                        .terminal('x2',10) \
                        .terminal('y2',0.0) \
                        .terminal('z2',-10.0)
#
# continuation_steps.add_step('bisection').num_cases(11)           \
#                         .const('rc',1.5)


# guess_maker = beluga.guess_generator(mode='file', filename='data-guess.dill', step=-1, iteration=-1)
continuation_steps.add_step('bisection').num_cases(31) \
                            .const('yc',0.5) \
                        # .const('xc',5.0) \


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
