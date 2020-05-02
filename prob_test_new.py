import beluga
import numpy as np
import logging

# prob = beluga.OCP()
# prob = OCP('Test OCP')
ocp = beluga.problib.Problem()

bfr_diameter = 9

Hscale = 8.44e3

bfr_thrust0_sea = 1.993e6*31
bfr_thrust0_vac = 2.295e6*31
bfr_thrust1_sea = 1.993e6*7
bfr_thrust1_vac = 2.295e6*7

bfr_mass0 = 4400e3
bfr_mass0f = 1335e3
bfr_mass1 = 1335e3
bfr_mass1f = 85e3

bfr_massflow0 = -615.8468*31
bfr_massflow1 = -615.8468*7

"""
Step 1
"""

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v_x', 'm') \
   .state('y', 'v_y', 'm') \
   .state('v_x', 'Thrust/mass*cos(theta) - D/mass*v_x/sqrt(v_x**2 + v_y**2)', 'm/s') \
   .state('v_y', 'Thrust/mass*sin(theta) - D/mass*v_y/sqrt(v_x**2 + v_y**2) - g', 'm/s') \
   .state('mass', 'mass_flow*eps', 'kg') \
   .state('theta', 'theta_dot', 'rad')

# Define controls
ocp.control('theta_dot', 'rad/s')

ocp.quantity('engine0', 'F0_sea*exp(-y/Hscale) + F0_vac*(1-exp(-y/Hscale))')
ocp.quantity('engine1', 'F1_sea*exp(-y/Hscale) + F1_vac*(1-exp(-y/Hscale))')
ocp.quantity('D', '1/2*rho_ref*exp(-y/Hscale)*CD*A*(v_x**2 + v_y**2)')

ocp.switch('Thrust', ['engine0', 'engine1'], [['mass_0f - mass'], ['mass - mass_0f']], 'stage_tol')
ocp.switch('mass_flow', ['md0', 'md1'], [['mass_0f - mass'], ['mass - mass_0f']], 'stage_tol')


# Define constants
ocp.constant('stage_tol', 100, '1')

ocp.constant('F0_sea', 2.1e6, 'newton')
ocp.constant('F0_vac', 2.1e6, 'newton')
ocp.constant('F1_sea', 2.1e6, 'newton')
ocp.constant('F1_vac', 2.1e6, 'newton')
ocp.constant('A', 7.069, 'm^2')
ocp.constant('mu', 3.986004e14, 'm^3/s^2')
ocp.constant('Re', 6378100, 'm')
ocp.constant('CD', 0.5, '1')
ocp.constant('rho_ref', 0, 'kg/m^3')
ocp.constant('Hscale', Hscale, 'm')
ocp.constant('g', 9.80665, 'm/s^2')
ocp.constant('md0', -807.6, 'kg/s')
ocp.constant('md1', -807.6, 'kg/s')
ocp.constant('eps', 0.000, '1')
ocp.constant('theta_max', 0.1, 'rad')

ocp.constant('x_0', 0, 'm')
ocp.constant('y_0', 0, 'm')
ocp.constant('v_x_0', 0, 'm/s')
ocp.constant('v_y_0', 0.01, 'm/s')
ocp.constant('mass_0', 60880, 'kg')
ocp.constant('mass_0f', 0, 'kg')
ocp.constant('drop_mass', 2000, 'kg')
ocp.constant('y_f', 1.5e5, 'm')
ocp.constant('v_y_f', 0, 'm/s')

# Define costs
ocp.path_cost('1', '1')

# Define constraints
ocp \
    .initial_constraint('x - x_0', 'm') \
    .initial_constraint('y - y_0', 'm') \
    .initial_constraint('v_x - v_x_0', 'm/s') \
    .initial_constraint('v_y - v_y_0', 'm/s') \
    .initial_constraint('mass - mass_0', 'kg') \
    .initial_constraint('t', 's') \
    .terminal_constraint('y - y_f', 'm') \
    .terminal_constraint('v_x - sqrt(mu/(y_f+Re))', 'm/s') \
    .terminal_constraint('v_y - v_y_f', 'm/s')

ocp.path_constraint('y', 'rad', '0', 'y_f*2', 'eps', method='utm')
ocp.path_constraint('theta_dot', 'rad/s', '-theta_max', 'theta_max', 'eps', method='epstrig')

ocp.scale(m='y', s='y/v_x', kg='mass', newton='mass*v_x^2/y', rad=1)

ocp.map_ocp_to_bvp(control_method='differential', analytical_jacobian=False)
ocp.compile_problem()

# ocp.sympify_self()
# ocp.apply_quantities()
# ocp.momentum_shift()
# ocp.epstrig()
# ocp.utm()
# ocp.rashs()
# ocp.dualize(method='traditional')
# ocp.algebraic_control_law()
# # ocp.differential_control_law()
# ocp.squash_to_bvp()
# ocp.normalize_time()
# ocp.compute_analytical_jacobians()

t = 0.1
y = np.ones(len(ocp.states))
u = np.ones(len(ocp.controls))
p = np.ones(len(ocp.parameters))
p_con = np.ones(len(ocp.constraint_parameters))
k = np.ones(len(ocp.constants))

# ocp.functional_problem.compile_problem(ocp)
