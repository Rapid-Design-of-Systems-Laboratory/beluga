"""Free flight in one dimension."""
from math import pi
ocp = beluga.OCP('freeflight1d')

# Define independent variables
ocp.independent('t', 's')

ocp.quantity('u1','(u1_+1)/2')
ocp.quantity('u2','(u2_+1)/2')
ocp.quantity('u3','(u3_+1)/2')
ocp.quantity('u4','(u4_+1)/2')

ocp.quantity('T1','u1-u2')
ocp.quantity('T2','u3-u4')

# Define equations of motion
ocp.state('x', 'vx', 'm')   \
   .state('y', 'vy', 'm')   \
   .state('theta', 'omega','rad') \
   .state('vx', '(T1+T2)*cos(theta)', 'm/s')   \
   .state('vy', '(T1+T2)*sin(theta)', 'm/s')   \
   .state('omega','a1*(T1) - a2*(T2)', 'rad/s')

# Define controls
ocp.control('u1_','m/s^2')
ocp.control('u2_','m/s^2')
ocp.control('u3_','m/s^2')
ocp.control('u4_','m/s^2')

ocp.constant('a1',0.2,'s/m')
ocp.constant('a2',0.2,'s/m')
ocp.constant('gamma',1.0,'s/m')

# Define costs
ocp.path_cost('u1 + u2 + u3 + u4','m/s^2')
# ocp.terminal_cost('gamma*(u1 + u2 + u3 + u4)','m/s^2')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m')    \
    .initial('y-y_0','m')  \
    .initial('theta-theta_0','rad')  \
    .initial('vx-vx_0','m/s')  \
    .initial('vy-vy_0','m/s')  \
    .initial('omega-omega_0','rad/s')  \
    .terminal('x-x_f','m')    \
    .terminal('y-y_f','m')  \
    .terminal('theta-theta_f','rad')  \
    .terminal('vx-vx_f','m/s')  \
    .terminal('vy-vy_f','m/s')  \
    .terminal('omega-omega_f','rad/s')  \
    .path('u1Limit','u1_','<>',1.0,'m/s^2',start_eps=1) \
    .path('u2Limit','u2_','<>',1.0,'m/s^2',start_eps=1) \
    .path('u3Limit','u3_','<>',1.0,'m/s^2',start_eps=1) \
    .path('u4Limit','u4_','<>',1.0,'m/s^2',start_eps=1)


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
                start=[-0.1, 0.0, 0.0, 0.01, 0.0, 0.0],          # Starting values for states in order
                direction='forward',
                costate_guess = -0.01,
                time_integrate= 1.0,
                control_guess = 0.0,
                use_control_guess=True
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .terminal('x', 0.0) \
                .terminal('y', 0.0) \
                .terminal('vx', 0.0) \
                .terminal('vy', 0.0) \
                .terminal('theta',0.0) \
                .terminal('omega', 0.0)

# continuation_steps.add_step('bisection').num_cases(6) \
#                  .const('eps_accLimit', 1e-1)
#
# continuation_steps.add_step('bisection').num_cases(21, spacing='log') \
#                  .const('eps_accLimit', 1e-3)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
