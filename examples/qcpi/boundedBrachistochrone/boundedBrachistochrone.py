"""Brachistochrone example with path constraint."""

ocp = beluga.OCP('brachisto')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v*cos(theta)', 'm')   \
   .state('y', 'v*sin(theta)','m')   \
   .state('v', 'g*sin(theta)','m/s')

# Define controls
ocp.control('theta','rad')

# Define constants
ocp.constant('g',-9.81,'m/s^2')
ocp.constant('xlim',-1.0,'m')
# Define costs
ocp.path_cost('1','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m')    \
    .initial('y-y_0','m')    \
    .initial('v-v_0','m/s')  \
    .terminal('x-x_f','m')   \
    .terminal('y-y_f','m') \
    .path('constraint1','y + x','>','xlim','m',start_eps=1e-4)
    # .path('constraint2','y + 0.75*x','>',-2,'m')  #\


# ocp.scale(m='y', s='y/v', kg=1, rad=1, nd=1)
ocp.scale(m=25, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('QCPI',
                    tolerance=1e-4,
                    max_iterations=500,
                    verbose = True,
                    max_error=50,
                    N=41 # 21 -> 6, 31 -> 8+, 41-> 10 @ 1e-4/1e-4
)

guess_maker = beluga.guess_generator('auto',
                start=[0,0,1],          # Starting values for states in order
                direction='forward',
                costate_guess = 0.1,
                control_guess = [-3.14*60/180, 0.0, 0.0],
                use_control_guess = True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .terminal('x', 10) \
                .terminal('y',-10)


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
