import beluga
import logging

ocp = beluga.OCP()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h', 'v', 'm') \
   .state('v', 'u - g', 'm/s') \

# Define controls
ocp.control('u', 'm/s**2')

# Define constants
ocp.constant('g', 1.625, 'm/s^2')
ocp.constant('epsilon1', 1, 'm/s**2')

ocp.constant('h_0', 20, 'm')
ocp.constant('v_0', -2.5, 'm/s')
ocp.constant('h_f', 0, 'm')
ocp.constant('v_f', 0, 'm/s')

ocp.constant('u_lower', -1, 'm/s**2')
ocp.constant('u_upper', 5, 'm/s**2')

# Define costs
ocp.path_cost('u', 'm/s**2')

# Define constraints
ocp.constraints() \
    .initial_constraint('h - h_0', 'm') \
    .initial_constraint('v - v_0', 'm/s') \
    .initial_constraint('t', 's') \
    .terminal_constraint('h - h_f', 'm') \
    .terminal_constraint('v - v_f', 'm/s')

ocp.path_constraint('u', 'newton', lower='u_lower', upper='u_upper', activator='epsilon1', method='utm')

ocp.scale(m='h', s='h/v')

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator('auto',
                                     start=[20, -2.5],          # Starting values for states in order
                                     costate_guess=-0.1,
                                     control_guess=[0],
                                     use_control_guess=True)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('h_f', 0) \
    .const('v_f', 0)

continuation_steps.add_step('bisection') \
    .num_cases(10) \
    .const('u_lower', 0) \
    .const('u_upper', 4)

continuation_steps.add_step('bisection') \
    .num_cases(30, 'log') \
    .const('epsilon1', 1e-5)

sol_set = beluga.solve(ocp=ocp,
                       method='indirect',
                       optim_options={'analytical_jacobian': True, 'control_method': 'icrm'},
                       bvp_algorithm=bvp_solver,
                       steps=continuation_steps,
                       guess_generator=guess_maker)
