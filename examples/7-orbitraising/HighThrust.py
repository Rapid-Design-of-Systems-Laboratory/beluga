import beluga
import logging
import matplotlib.pyplot as plt
import numpy as np

ocp = beluga.OCP('HighThrust_OrbitRaising')

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

beluga.add_logger(logging_level=logging.DEBUG)

sol_set_collocation = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver_collocation,
    steps=continuation_steps,
    guess_generator=guess_maker
)

sol_set_shooting = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver_shooting,
    steps=continuation_steps,
    guess_generator=guess_maker
)

sol_c = sol_set_collocation[-1][-1]
sol_s = sol_set_shooting[-1][-1]

anom = np.linspace(0, 2*np.pi, num=1000)
plt.plot(0, 0, marker='*')
plt.plot(np.cos(sol_s.y[:,1])*sol_s.y[:,0], np.sin(sol_s.y[:,1])*sol_s.y[:,0], color='b', linestyle='-', linewidth=2,
         label='Shooting')
plt.plot(np.cos(sol_c.y[:,1])*sol_c.y[:,0], np.sin(sol_c.y[:,1])*sol_c.y[:,0], color='r', linestyle='--', marker='.',
         label='Collocation')
plt.plot(np.cos(anom)*sol_s.y[0,0], np.sin(anom)*sol_s.y[0,0], color='k', linestyle='--')
plt.plot(np.cos(anom)*sol_s.y[-1,0], np.sin(anom)*sol_s.y[-1,0], color='k', linestyle='--')
plt.legend()
plt.axis('equal')
plt.grid('on')
plt.title('High Thrust Orbit Raising')
plt.show()

plt.plot(sol_s.t, sol_s.y[:,0], color='b', linestyle='-', label='Radius')
plt.plot(sol_s.t, sol_s.y[:,1], color='r', linestyle='-', label='True Anomaly')
plt.plot(sol_s.t, sol_s.y[:,2], color='g', linestyle='-', label='Radial Velocity')
plt.plot(sol_s.t, sol_s.y[:,3], color='y', linestyle='-', label='Tangential Velocity')
plt.plot(sol_c.t, sol_c.y[:,0], color='b', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.y[:,1], color='r', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.y[:,2], color='g', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.y[:,3], color='y', linestyle='--', marker='.')
plt.xlabel('Time [nd]')
plt.ylabel('States [nd]')
plt.title('High Thrust States')
plt.legend()
plt.show()

plt.plot(sol_s.t, sol_s.dual[:,0], color='b', linestyle='-', label='Radius (costate)')
plt.plot(sol_s.t, sol_s.dual[:,1], color='r', linestyle='-', label='True Anomaly (costate)')
plt.plot(sol_s.t, sol_s.dual[:,2], color='g', linestyle='-', label='Radial Velocity (costate)')
plt.plot(sol_s.t, sol_s.dual[:,3], color='y', linestyle='-', label='Tangential Velocity (costate)')
plt.plot(sol_c.t, sol_c.dual[:,0], color='b', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.dual[:,1], color='r', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.dual[:,2], color='g', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.dual[:,3], color='y', linestyle='--', marker='.')
plt.xlabel('Time [nd]')
plt.ylabel('Costates [nd]')
plt.title('High Thrust Costates')
plt.legend()
plt.show()

plt.plot(sol_s.t, np.cos(sol_s.u), color='r', linestyle='-', label='Radial Thrust')
plt.plot(sol_s.t, np.sin(sol_s.u), color='b', linestyle='-', label='Tangential Thrust')
plt.plot(sol_c.t, np.cos(sol_c.u), color='r', linestyle='--', marker='.')
plt.plot(sol_c.t, np.sin(sol_c.u), color='b', linestyle='--', marker='.')
plt.xlabel('Time [nd]')
plt.ylabel('Control [nd]')
plt.title('High Thrust Decomposed Control')
plt.legend()
plt.show()

plt.plot(sol_s.t, sol_s.u*180/np.pi, color='r', linestyle='-', label='Shooting')
plt.plot(sol_c.t, sol_c.u*180/np.pi, color='b', linestyle='--', marker='.', label='Collocation')
plt.xlabel('Time [nd]')
plt.ylabel('Control [degrees]')
plt.title('High Thrust Control Angle')
plt.legend()
plt.show()
