import beluga
import logging

ocp = beluga.OCP('zermelos_problem')

def drift_x(x, y):
    return 0

def drift_y(x, y):
    return ((x-5)**4 - 625)/625

ocp.custom_function('drift_x', drift_x)
ocp.custom_function('drift_y', drift_y)

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'V*cos(theta) + drift_x(x,y)', 'm')   \
   .state('y', 'V*sin(theta) + drift_y(x,y)', 'm')

# Define controls
ocp.control('theta', 'rad')

# Define constants
ocp.constant('V', 10, 'm/s')
ocp.constant('epsilon', 0.001, '1')
ocp.constant('x_f', 0, 'm')
ocp.constant('y_f', 0, 'm')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.constraints() \
    .initial('x', 'm') \
    .initial('y', 'm') \
    .terminal('x-x_f', 'm') \
    .terminal('y-y_f', 'm')

ocp.scale(m='x', s='x/V', rad=1)

bvp_solver = beluga.bvp_algorithm('Shooting',
                        derivative_method='fd',
                        tolerance=1e-4)

guess_maker = beluga.guess_generator('auto',
                start=[0, 0],
                control_guess=[0],
                use_control_guess = True,
                direction='forward'
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('x_f', 10)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('y_f', 10)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('epsilon', 1)

beluga.add_logger(logging_level=logging.DEBUG)

sol_set = beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

sol = sol_set[-1][-1]

import matplotlib.pyplot as plt
plt.plot(sol.y[:,0], sol.y[:,1])
plt.show()
