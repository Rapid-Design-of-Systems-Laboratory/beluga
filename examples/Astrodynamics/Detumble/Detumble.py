import beluga
import logging

w0 = [0.6, 0.2, 0.3]

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('w1', '((I2 - I3)*w2*w3 + u1)/I1', 'rad/s')
ocp.state('w2', '((I3 - I1)*w3*w1 + u2)/I2', 'rad/s')
ocp.state('w3', '((I1 - I2)*w1*w2 + u3)/I3', 'rad/s')

# Define controls
ocp.control('u1', 'rad/s**2')
ocp.control('u2', 'rad/s**2')
ocp.control('u3', 'rad/s**2')

# Define constants
ocp.constant('I1', 10, 'kg*m**2')
ocp.constant('I2', 20, 'kg*m**2')
ocp.constant('I3', 15, 'kg*m**2')

ocp.constant('q0_0', 1, 'rad')
ocp.constant('q1_0', 0, 'rad')
ocp.constant('q2_0', 0, 'rad')
ocp.constant('q3_0', 0, 'rad')

ocp.constant('w1_0', w0[0], 'rad/s')
ocp.constant('w2_0', w0[1], 'rad/s')
ocp.constant('w3_0', w0[2], 'rad/s')

ocp.constant('w1_f', 0, 'rad/s')
ocp.constant('w2_f', 0, 'rad/s')
ocp.constant('w3_f', 0, 'rad/s')

ocp.constant('h1_0', 0, 'rad/s')
ocp.constant('h2_0', 0, 'rad/s')
ocp.constant('h3_0', 0, 'rad/s')

ocp.constant('epsilon1', 1, '1')
ocp.constant('u_min', -1, 'rad**2/s**4')
ocp.constant('u_max', 1, 'rad**2/s**4')

# Define costs
ocp.path_cost('1', 's')

# Define constraints
ocp.initial_constraint('t', 's')
ocp.initial_constraint('w1 - w1_0', 'rad/s')
ocp.initial_constraint('w2 - w2_0', 'rad/s')
ocp.initial_constraint('w3 - w3_0', 'rad/s')
ocp.terminal_constraint('w1 - w1_f', 'rad/s')
ocp.terminal_constraint('w2 - w2_f', 'rad/s')
ocp.terminal_constraint('w3 - w3_f', 'rad/s')

ocp.path_constraint('u1', 'rad/s**2', lower='u_min', upper='u_max', activator='epsilon1', method='utm')
ocp.path_constraint('u2', 'rad/s**2', lower='u_min', upper='u_max', activator='epsilon1', method='utm')
ocp.path_constraint('u3', 'rad/s**2', lower='u_min', upper='u_max', activator='epsilon1', method='utm')

ocp.scale(rad=1, kg=1, s=1, m=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[w0[0], w0[1], w0[2]],
    direction='forward',
    costate_guess=0.1,
    control_guess=[-0.1, -0.1, -0.1]
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .const('w1_f', 0) \
                .const('w2_f', 0) \
                .const('w3_f', 0)

continuation_steps.add_step('bisection') \
                .num_cases(160, 'log') \
                .const('epsilon1', 1e-6)


beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'differential', 'analytical_jacobian': False},
    bvp_algo=bvp_solver,
    steps=continuation_steps,
    guess_gen=guess_maker,
    initial_helper=True
)
