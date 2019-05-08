import beluga
import logging
import matplotlib.pyplot as plt
import numpy as np


atlasv_thrust0 = 5.84e6
atlasv_thrust1 = 4.152e6

atlasv_mass0 = 374406
atlasv_mass0f = 222972
atlasv_mass1 = 214664

atlasv_massflow0 = -1682.6
atlasv_massflow1 = -1252.9

"""
Step 1
"""

ocp = beluga.OCP('AtlasV')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v_x', 'm') \
   .state('y', 'v_y', 'm') \
   .state('v_x', 'Thrust/current_mass*cos(theta) - D/current_mass*v_x/sqrt(v_x**2 + v_y**2)', 'm/s') \
   .state('v_y', 'Thrust/current_mass*sin(theta) - D/current_mass*v_y/sqrt(v_x**2 + v_y**2) - g', 'm/s') \
   .state('mass', 'mass_flow*eps', 'kg')

# Define controls
ocp.control('theta', 'rad')

ocp.quantity('engine0', 'F0_sea*exp(-y/Hscale) + F0_vac*(1-exp(-y/Hscale))')
ocp.quantity('engine1', 'F1_sea*exp(-y/Hscale) + F1_vac*(1-exp(-y/Hscale))')
ocp.quantity('D', '1/2*rho_ref*exp(-y/Hscale)*CD*A*(v_x**2 + v_y**2)')

ocp.switch('Thrust', ['engine0', 'engine1'], [['mass_0f - mass'], ['mass - mass_0f']], 'rash')
ocp.switch('mass_flow', ['md0', 'md1'], [['mass_0f - mass'], ['mass - mass_0f']], 'rash')
ocp.switch('current_mass', ['mass', 'mass - drop_mass'], [['mass_0f - mass'], ['mass - mass_0f']], 'rash')
# [F0_sea*exp(-y/Hscale) + F0_vac*(1 - exp(-y/Hscale)), F1_sea*exp(-y/Hscale) + F1_vac*(1 - exp(-y/Hscale)), A*CD*rho_ref*(v_x**2 + v_y**2)*exp(-y/Hscale)/2, engine0/(exp((-mass + mass_0f)/rash) + 1) + engine1/(exp((mass - mass_0f)/rash) + 1), md0/(exp((-mass + mass_0f)/rash) + 1) + md1/(exp((mass - mass_0f)/rash) + 1), mass/(exp((-mass + mass_0f)/rash) + 1) + (-drop_mass + mass)/(exp((mass - mass_0f)/rash) + 1)]

# Define constants
ocp.constant('F0_sea', 2.1e6, 'newton')
ocp.constant('F0_vac', 2.1e6, 'newton')
ocp.constant('F1_sea', 2.1e6, 'newton')
ocp.constant('F1_vac', 2.1e6, 'newton')
ocp.constant('A', 7.069, 'm^2')
ocp.constant('mu', 3.986004e14, 'm^3/s^2')
ocp.constant('Re', 6378100, 'm')
ocp.constant('CD', 0.5, '1')
ocp.constant('rho_ref', 0, 'kg/m^3')
ocp.constant('Hscale', 8.44e3, 'm')
ocp.constant('g', 9.80665, 'm/s^2')
ocp.constant('md0', -807.6, 'kg/s')
ocp.constant('md1', -807.6, 'kg/s')
ocp.constant('eps', 0.000, '1')

ocp.constant('x_0', 0, 'm')
ocp.constant('y_0', 0, 'm')
ocp.constant('v_x_0', 0, 'm/s')
ocp.constant('v_y_0', 0.01, 'm/s')
ocp.constant('mass_0', 60880, 'kg')
ocp.constant('mass_0f', 0, 'kg')
ocp.constant('drop_mass', 2000, 'kg')

ocp.constant('rash', 100, '1')

ocp.constant('y_f', 1.5e5, 'm')
ocp.constant('v_y_f', 0, 'm/s')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp.constraints() \
    .initial('x - x_0', 'm')    \
    .initial('y - y_0', 'm') \
    .initial('v_x - v_x_0', 'm/s')  \
    .initial('v_y - v_y_0', 'm/s')  \
    .initial('mass - mass_0', 'kg') \
    .terminal('y - y_f', 'm') \
    .terminal('v_x - sqrt(mu/(y_f+Re))', 'm/s') \
    .terminal('v_y - v_y_f', 'm/s')

ocp.scale(m='y', s='y/v_x', kg='mass', newton='mass*v_x^2/y', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator('auto',
                start=[0, 0, 0, 0.01, 60880],          # Starting values for states in order
                costate_guess = -0.1,
                control_guess=[0],
                use_control_guess=False
)

beluga.add_logger(logging_level=logging.DEBUG)

sol_set = beluga.solve(ocp=ocp,
             method='indirect',
             bvp_algorithm=bvp_solver,
             steps=None,
             guess_generator=guess_maker, autoscale=True)

guess_maker = beluga.guess_generator('static', solinit=sol_set[-1][-1])

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('eps', 1) \
                .const('mass_0', atlasv_mass0) \
                .const('mass_0f', atlasv_mass0f) \
                .const('F0_sea', atlasv_thrust0) \
                .const('F0_vac', atlasv_thrust0) \
                .const('F1_sea', atlasv_thrust1) \
                .const('F1_vac', atlasv_thrust1) \
                .const('md0', atlasv_massflow0) \
                .const('md1', atlasv_massflow1) \
                .const('rash', 1)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('rho_ref', 1.225)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('rash', 1e-2)


sol_set = beluga.solve(ocp=ocp,
             method='indirect',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker, autoscale=True)

sol = sol_set[-1][-1]


plt.plot(sol.y[:,0]/1000, sol.y[:,1]/1000)
plt.xlabel('Downrange [km]')
plt.ylabel('Altitude [km]')
plt.title('Time Optimal Launch of a Atlas-V Trajectory')
plt.grid('on')
plt.show()

plt.plot(sol.t, sol.y[:,2]/1000, label='Horizontal Velocity')
plt.plot(sol.t, sol.y[:,3]/1000, label='Vertical Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [km/s]')
plt.title('Velocities of a Atlas-V')
plt.legend()
plt.grid('on')
plt.show()

plt.plot(sol.t, sol.u*180/np.pi)
plt.xlabel('Time [s]')
plt.ylabel('Control [degrees]')
plt.title('Atlas-V Steering Angle')
plt.grid('on')
plt.show()

plt.plot(sol.t, sol.y[:,4])
plt.plot([sol.t[0], sol.t[-1]], [atlasv_mass0, atlasv_mass0], linestyle='--', color='k')
plt.plot([sol.t[0], sol.t[-1]], [atlasv_mass0f, atlasv_mass0f], linestyle='--', color='k')
plt.xlabel('Time [s]')
plt.ylabel('Control [degrees]')
plt.title('Atlas-V Mass')
plt.grid('on')
plt.show()
