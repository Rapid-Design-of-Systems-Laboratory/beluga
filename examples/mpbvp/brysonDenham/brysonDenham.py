
"""Constrained Double integrator problem ."""

# Rename this and/or move to optim package?
ocp = beluga.OCP('brysonDenhamConstrained')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v','m')   \
   .state('v', 'u','m/s')

# Define controls
ocp.control('u','m/s')

# Define costs
ocp.path_cost('u**2','m**2/s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m')    \
    .initial('v-v_0','m/s')  \
    .terminal('x-x_f','m')   \
    .terminal('v-v_f','m/s') \
    .path('xlim','x - 0.18','<',0.00,'m') \
    .independent('tf - 1','s') # Fixed final time (not working for multiarc)

ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

# ocp.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=30, verbose = True, cached=False)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                    derivative_method='fd',
                    tolerance=1e-3,
                    max_iterations=1000,
                    verbose = True,
                    max_error=200
)

guess_maker = beluga.guess_generator('auto',
                start=[0,.01],          # Starting values for states in order
                direction='forward',
                costate_guess = -0.1,
                time_integrate = 1      ## REQUIRED BECAUSE OF FIXED FINAL TIME
)

continuation_steps = beluga.init_continuation()
continuation_steps.add_step('bisection', max_divisions=30).num_cases(5)   \
                    .terminal('x',0) \
                    .initial('v',1) \
                    .terminal('v', -1)

continuation_steps.add_step('activate_constraint', name='xlim')

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .constraint('xlim', 0.0, index=1)

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker
)
