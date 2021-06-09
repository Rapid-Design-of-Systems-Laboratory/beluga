import beluga
import logging

ocp = beluga.Problem('hanging_chain')

ocp.independent('s', 'ft')

ocp.state('x', 'cos(theta)', 'ft')
ocp.state('y', 'sin(theta)', 'ft')

ocp.control('theta', 'rad')

ocp.constant('x_0', 0, 'ft')
ocp.constant('y_0', 0, 'ft')
ocp.constant('s_0', 0, 'ft')

ocp.constant('x_f', 1, 'ft')
ocp.constant('y_f', 0, 'ft')
ocp.constant('s_f', 1.1, 'ft')

ocp.path_cost('y', 'ft')

ocp.initial_constraint('x - x_0', 'ft')
ocp.initial_constraint('y - y_0', 'ft')
ocp.initial_constraint('s', 'ft')

ocp.terminal_constraint('x - x_f', 'ft')
ocp.terminal_constraint('y - y_f', 'ft')
ocp.terminal_constraint('s - s_f', 'ft')

ocp.scale(ft='s', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator('auto', start=[0, 0], costate_guess=-0.1, time_integrate=1.1,
                                     control_guess=[0], use_control_guess=True)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(6) \
                .const('x_f', 1) \
                .const('y_f', 0) \
                .const('s_f', 1.1)

continuation_steps.add_step('bisection') \
                .num_cases(6) \
                .const('x_f', 1) \
                .const('y_f', 0) \
                .const('s_f', 3)

beluga.add_logger(display_level=logging.INFO)

sol_set = beluga.solve(ocp=ocp, method='traditional', bvp_algorithm=bvp_solver, steps=continuation_steps,
                       guess_generator=guess_maker, autoscale=True, initial_helper=True, save_sols='chain.beluga')
