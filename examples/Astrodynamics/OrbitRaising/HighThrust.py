import beluga
import logging

ocp = beluga.OCP()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('r', 'v_r', 'L')   \
   .state('theta', 'v_theta/r', 'rad')  \
   .state('v_r', 'v_theta**2/r - mu/r**2 + Tf*cos(alpha)', 'L/s') \
   .state('v_theta', '-v_r*v_theta/r + Tf*sin(alpha)', 'L/s') \
   .state('m', 'mdot', 'M')

# Define quantities used in the problem
ocp.quantity('Tf', 'T/m')

# Define controls
ocp.control('alpha', 'rad')

# Define constants
ocp.constant('mu', 1, 'L^3/s^2')
ocp.constant('T', 0.1, 'M*L/s^2')
ocp.constant('r_0', 1, 'L')
ocp.constant('theta_0', 0, 'rad')
ocp.constant('v_r_0', 0, 'L/s')
ocp.constant('v_theta_0', 1, 'L/s')
ocp.constant('m_0', 1, 'M')
ocp.constant('v_r_f', 0, 'L/s')
ocp.constant('t_f', 1, 's')
ocp.constant('mdot', 0.05, 'M/s')


# Define costs
ocp.terminal_cost('-r^2', 'L')

# Define constraints
ocp.constraints() \
    .initial('r-r_0', 'L') \
    .initial('theta - theta_0', 'rad') \
    .initial('v_r - v_r_0', 'L/s') \
    .initial('v_theta - v_theta_0', 'L/s') \
    .initial('m - m_0', 'M') \
    .initial('t', 's') \
    .terminal('v_r - v_r_f', 'L/s')  \
    .terminal('v_theta - sqrt(mu / r)', 'L/s') \
    .terminal('t - t_f', 's')

ocp.scale(L='r', s='r/v_theta', M='m', rad=1)

bvp_solver_shooting = beluga.bvp_algorithm('Shooting', algorithm='Armijo')
bvp_solver_collocation = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[1, 0, 0, 1, 1],
    direction='forward',
    costate_guess=-0.1
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .const('v_r_f', 0) \
                .const('t_f', 4)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

sol_set_collocation = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver_collocation,
    steps=continuation_steps,
    guess_generator=guess_maker,
    save='highthrust_collocation_data.blg'
)

sol_set_shooting = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver_shooting,
    steps=continuation_steps,
    guess_generator=guess_maker,
    save='highthrust_shooting_data.blg'
)
