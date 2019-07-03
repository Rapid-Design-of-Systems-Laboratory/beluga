import beluga
import logging
import matplotlib.pyplot as plt

ocp = beluga.OCP('MoonLander')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h', 'v', 'm') \
   .state('v', 'u - g', 'm/s') \

# Define controls
ocp.control('u', 'newton')

# Define constants
ocp.constant('g', 1.625, 'm/s^2')
ocp.constant('epsilon1', 1, 'newton^2')

ocp.constant('h_0', 20, 'm')
ocp.constant('v_0', -2.5, 'm/s')
ocp.constant('h_f', 0, 'm')
ocp.constant('v_f', 0, 'm/s')

ocp.constant('u_lower', -1, 'newton')
ocp.constant('u_upper', 5, 'newton')

# Define costs
ocp.path_cost('u', 'newton')

# Define constraints
ocp.constraints() \
    .initial('h - h_0', 'm')    \
    .initial('v - v_0', 'm/2') \
    .path('u', 'm', lower='u_lower', upper='u_upper', activator='epsilon1', method='utm') \
    .terminal('h - h_f', 'm')  \
    .terminal('v - v_f', 'm/s')

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator('auto',
                                     start=[20, -2.5],          # Starting values for states in order
                                     costate_guess = -0.1,
                                     control_guess=[0],
                                     use_control_guess=False)

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
    .num_cases(20, 'log') \
    .const('epsilon1', 1e-5)

sol_set = beluga.solve(ocp=ocp,
                       method='indirect',
                       optim_options={'analytical_jacobian': True, 'control_method': 'icrm'},
                       bvp_algorithm=bvp_solver,
                       steps=continuation_steps,
                       guess_generator=guess_maker, autoscale=False)

sol = sol_set[-1][-1]

plt.plot(sol.t, sol.y[:,0], label='Altitude')
plt.plot(sol.t, sol.y[:,1], label='Velocity')
plt.xlabel('Time [s]')
plt.ylabel('States [nd]')
plt.title('Moon Lander States')
plt.grid('on')
plt.legend()
plt.show()

plt.plot(sol.t, sol.u)
plt.plot([sol.t[0], sol.t[-1]], [0, 0], color='k', linestyle='--')
plt.plot([sol.t[0], sol.t[-1]], [4, 4], color='k', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('Thrust [nd]')
plt.title('Bounded Control History')
plt.grid('on')
plt.show()

plt.plot(sol.t, sol.dual[:,0], label='Altitude (costate)')
plt.plot(sol.t, sol.dual[:,1], label='Velocity (costate)')
plt.xlabel('Time [s]')
plt.ylabel('Costates [nd]')
plt.title('Moon Lander Costates')
plt.grid('on')
plt.legend()
plt.show()
