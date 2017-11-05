from math import pi

ocp = beluga.OCP('zermelo1')
ocp.independent('t', 's')
ocp.state('x','V*cos(theta)','m')
ocp.state('y','V*sin(theta)+x','m')

ocp.control('theta','rad')

ocp.constant('V',10,'m/s')
ocp.path_cost('1','s')
ocp.constraints().initial('x-x_0','m')\
                .initial('y-y_0','m')\
                .terminal('x-x_f','m')\
                .terminal('y-y_f','m')

ocp.constraints().path('c1','y','>',-1,'nd',start_eps=1e-6)
ocp.constant('xc',5,'m')
ocp.constant('yc',10,'m')
ocp.constant('rc',0.1,'m')

ocp.scale(m=1, s=1, kg=1, rad=1,nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=100,
                        verbose = True,
                        max_error=400,
             )

guess_maker = beluga.guess_generator('auto',
                start=[0, 0],
                direction='forward',
                # costate_guess = -0.1,
                costate_guess = [-0.1,-0.1,0.0]
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection').num_cases(5)           \
                        .terminal('x',10) \
                        .terminal('y',0.0)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
