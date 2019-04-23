"""
References
----------
.. [1] Ping Chen and Sardar M.N. Islam. "Optimal Control Models in Finance."
    Kluwer Academic Publishers. DOI: 10.1007/b101888.
"""

import beluga
from beluga.bvpsol.Pseudospectral import linter
import numpy as np
import logging

import matplotlib.pyplot as plt

ocp_indirect = beluga.OCP('financial_oscillator_indirect')
ocp_direct = beluga.OCP('financial_oscillator_direct')

# Define independent variables
ocp_indirect.independent('tau', 'nd')
ocp_direct.independent('tau', 'nd')

# Define equations of motion
ocp_indirect.state('x1', 'T*x2', 'nd')
ocp_indirect.state('x2', '-T*x1 + T*2*sin(u) - T**2*B*x2', 'nd')
ocp_indirect.state('t', '1', 'nd')
ocp_direct.state('x1', 'T*x2', 'nd')
ocp_direct.state('x2', '-T*x1 + T*u - T**2*B*x2', 'nd')
ocp_direct.state('t', '1', 'nd')

# Define controls
ocp_indirect.control('u', 'rad')
ocp_direct.control('u', 'rad')

# Define constants
ocp_indirect.constant('T', 5, 'nd')
ocp_indirect.constant('B', 0.2, 'nd')
ocp_indirect.constant('x1_0', 3, 'nd')
ocp_indirect.constant('x2_0', 5, 'nd')
ocp_indirect.constant('epsilon1', 10, 'nd')
ocp_direct.constant('T', 5, 'nd')
ocp_direct.constant('B', 0.2, 'nd')
ocp_direct.constant('x1_0', 3, 'nd')
ocp_direct.constant('x2_0', 5, 'nd')
ocp_direct.constant('epsilon1', 10, 'nd')

# Define costs
ocp_indirect.path_cost('(x1 + 5*t - 5)**2 - epsilon1*cos(u)', 'nd')
ocp_direct.path_cost('abs(x1 + 5*t - 5)', 'nd')

# Define constraints
ocp_indirect.constraints().initial('x1 - x1_0', 'nd')
ocp_indirect.constraints().initial('x2 - x2_0', 'nd')
ocp_indirect.constraints().initial('t', 'nd')
ocp_indirect.constraints().terminal('t - 1', 'nd')
ocp_indirect.constraints().terminal('tau - 1', 'nd')
ocp_direct.constraints().initial('x1 - x1_0', 'nd')
ocp_direct.constraints().initial('x2 - x2_0', 'nd')
ocp_direct.constraints().initial('t', 'nd')
ocp_direct.constraints().path('u', 'rad', lower=-2, upper=2, activator=None)
ocp_direct.constraints().terminal('t - 1', 'nd')
ocp_direct.constraints().terminal('tau - 1', 'nd')

bvp_solver_direct = beluga.bvp_algorithm('Pseudospectral', number_of_nodes=60)
bvp_solver_indirect = beluga.bvp_algorithm('spbvp')

guess_maker_direct = beluga.guess_generator(
    'ones',
    start=[3, 5, 0],
    costate_guess=0,
    control_guess=[0],
    use_control_guess=True,
    time_integrate=0.1
)

guess_maker_indirect = beluga.guess_generator(
    'auto',
    start=[3, 5, 0],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0],
    use_control_guess=True,
    time_integrate=0.1
)


beluga.add_logger(logging_level=logging.DEBUG)

sol_set_direct = beluga.solve(
    ocp=ocp_direct,
    method='direct',
    bvp_algorithm=bvp_solver_direct,
    steps=None,
    guess_generator=guess_maker_direct,
    autoscale=False)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(60, 'log') \
    .const('epsilon1', 1e-6)

sol_set_indirect = beluga.solve(
    ocp=ocp_indirect,
    method='indirect',
    optim_options={'control_method': 'icrm'},
    bvp_algorithm=bvp_solver_indirect,
    steps=continuation_steps,
    guess_generator=guess_maker_indirect,
    autoscale=False
)

sol_direct = sol_set_direct[-1][-1]
sol_indirect = sol_set_indirect[-1][-1]

ts = np.linspace(sol_direct.t[0], sol_direct.t[-1], num=200)

plt.plot(sol_direct.t, sol_direct.y[:, 0], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.y[:, 0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:, 0], linestyle='-', color='b', label='indirect')
plt.xlabel('Time [nd]')
plt.ylabel('$x_1$ [nd]')
plt.grid('on')
plt.legend()
plt.show()

plt.plot(sol_direct.y[:,0], sol_direct.y[:, 1], linestyle='--', color='r', marker='o')
plt.plot(linter(sol_direct.t, sol_direct.y[:, 0], ts), linter(sol_direct.t, sol_direct.y[:, 1], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.y[:, 0], sol_indirect.y[:, 1], linestyle='-', color='b', label='indirect')
plt.title('State-Space')
plt.xlabel('$x_1$ [nd]')
plt.ylabel('$x_2$ [nd]')
plt.grid('on')
plt.legend()
plt.show()

plt.plot([0,1], [2,2], linestyle='--', color='k')
plt.plot([0,1], [-2,-2], linestyle='--', color='k')
plt.plot(sol_direct.t, 2*np.sin(sol_direct.u), linestyle='--', color='r', marker='o')
plt.plot(ts, 2*np.sin(linter(sol_direct.t, sol_direct.u[:, 0], ts)), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, 2*np.sin(sol_indirect.u), linestyle='-', color='b', label='indirect')
plt.title('Control')
plt.xlabel('Time [nd]')
plt.ylabel('$u$ [nd]')
plt.grid('on')
plt.legend()
plt.show()
