"""Free flight in one dimension."""

ocp = beluga.OCP('freeflight2d')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'vx', 'm')   \
   .state('y', 'vy','m/s') \
   .state('vx', 'a*u1','m/s') \
   .state('vy', 'a*u2','m/s') \
   # .state('theta', 'thetaDot', 'rad')

# Define controls
ocp.control('theta','rad')
ocp.control('a','m/s^2')

# Define costs
ocp.path_cost('1','s')

# Define constraints
ocp.constraints()              \
    .initial('x-x_0','m')      \
    .initial('y-y_0','m')      \
    .initial('vx-vx_0','m/s')  \
    .initial('vy-vy_0','m/s')  \
    .terminal('x-x_f','m')     \
    .terminal('y-y_f','m')     \
    .terminal('vx-vx_f','m/s') \
    .terminal('vy-vy_f','m/s') \
    .path('accLimit','a','<>',1.0,'m/s^2',start_eps=1)
    # .path('thetaLimit','thetaDot','<>',60*pi/180,'rad/s',start_eps=2)


# ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                    derivative_method='fd',
                    tolerance=1e-3,
                    max_iterations=1000,
                    verbose = True,
                    max_error=100
)

guess_maker = beluga.guess_generator('auto',
                start=[0.0, 0.0, 0.0, 0.0],          # Starting values for states in order
                direction='forward',
                costate_guess = [-0.1, -0.2, -0.1, -0.2],
                control_guess = [0.0, 1.0, 0.00, 0.00],
                time_integrate= .1,
                use_control_guess=True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(6) \
                .terminal('x', 1.0) \
                .terminal('y', 0.0) \
                .initial('vx', 0) \
                .initial('vy', 0) \
                .terminal('vx', 0) \
                .terminal('vy', 0)

continuation_steps.add_step('bisection').num_cases(6) \
                 .const('eps_accLimit', 1e-1)

# continuation_steps.add_step('bisection').num_cases(21, spacing='log') \
#                  .const('eps_accLimit', 1e-3)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data2d.dill')
