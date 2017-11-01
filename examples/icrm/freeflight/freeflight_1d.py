"""Free flight in one dimension."""

ocp = beluga.OCP('freeflight1d')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v', 'm')   \
   .state('v', 'a','m/s')

# Define controls
ocp.control('a','m/s^2')

# Define costs
ocp.path_cost('1','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m')    \
    .initial('v-v_0','m/s')  \
    .terminal('x-x_f','m')   \
    .terminal('v-v_f','m/s') \
    .path('accLimit','a','<>',1.0,'m/s^2',start_eps=2)


# ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)
ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                    derivative_method='fd',
                    tolerance=1e-5,
                    max_iterations=40,
                    verbose = True,
                    max_error=50
)

guess_maker = beluga.guess_generator('auto',
                start=[0,0.01],          # Starting values for states in order
                direction='forward',
                costate_guess = [-0.2, -0.4],
                control_guess = [1, 0, 0],
                time_integrate= 10.0,
                use_control_guess=True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .terminal('x', 1.0) \
                .terminal('v', 0) \
                .initial('v', 0.0)

continuation_steps.add_step('bisection').num_cases(6) \
                 .const('eps_accLimit', 1e-1)

continuation_steps.add_step('bisection').num_cases(21, spacing='log') \
                 .const('eps_accLimit', 1e-3)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
