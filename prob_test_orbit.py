import beluga
import logging
import numpy as np

prob = beluga.problib.InputOCP()

# Define independent variables
prob.independent('t', 's')

# Define equations of motion
prob.state('r', 'v_r', 'L')
prob.state('theta', 'v_theta/r', 'rad')
prob.state('v_r', 'v_theta**2/r - mu/r**2 + Tf*cos(alpha)', 'L/s')
prob.state('v_theta', '-v_r*v_theta/r + Tf*sin(alpha)', 'L/s')
prob.state('m', 'mdot', 'M')

# Define quantities used in the problem
prob.quantity('Tf', 'T/m')

# Define controls
prob.control('alpha', 'rad')

# Define constants
prob.constant('mu', 1, 'L^3/s^2')
prob.constant('T', 0.005, 'M*L/s^2')
prob.constant('r_0', 1, 'L')
prob.constant('theta_0', 0, 'rad')
prob.constant('v_r_0', 0, 'L/s')
prob.constant('v_theta_0', 1, 'L/s')
prob.constant('m_0', 1, 'M')
prob.constant('v_r_f', 0, 'L/s')
prob.constant('t_f', 1, 's')
prob.constant('mdot', 0.0025, 'M/s')

prob.constant('alpha', 0, 'rad')


# Define costs
prob.terminal_cost('-r^2', 'L')

# Define constraints
prob.initial_constraint('r-r_0', 'L')
prob.initial_constraint('theta - theta_0', 'rad')
prob.initial_constraint('v_r - v_r_0', 'L/s')
prob.initial_constraint('v_theta - v_theta_0', 'L/s')
prob.initial_constraint('m - m_0', 'M')
prob.initial_constraint('t', 's')
prob.terminal_constraint('v_r - v_r_f', 'L/s')
prob.terminal_constraint('v_theta - sqrt(mu / r)', 'L/s')
prob.terminal_constraint('t - t_f', 's')

prob.scale(L='r', s='r/v_theta', M='m', rad=1)

sym_prob = prob.sympify_problem()
# lam_prob = sym_prob.lambdify_problem()

x_test = np.array([2, 0.0, 0.5, 0.1, 1])
p_test = np.array([])
k_test = np.array([1, 0.005, 1, 0, 0, 1, 1, 0, 1, 0.0025, 0])
q_test = np.array([])
nu_test = np.array([])

