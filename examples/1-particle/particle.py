"""Bryson-Denham problem"""
# TODO: Costate estimates seem to be off by a factor of -2. See Issue #143

import beluga
from beluga.bvpsol.Solution import Solution
from beluga.bvpsol.algorithms.Pseudospectral import linter
import numpy as np
import logging

ocp = beluga.OCP('particle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v', 'm') \
   .state('v', 'u', 'm/s')

# Define controls
ocp.control('u', 'rad')

# Define constants
ocp.constant('x_0', 0, 'm')
ocp.constant('x_f', 0, 'm')
ocp.constant('v_0', 1, 'm')
ocp.constant('v_f', -1, 'm')
ocp.constant('x_limit', 0.1, 'm')

ocp.constant('path_width', 2, '1')
ocp.constant('epsilon1', 1, '1')

# Define costs
ocp.path_cost('u**2', '1')

# Define constraints
ocp.constraints() \
    .initial('x - x_0', 'm')    \
    .initial('v - v_0', 'm/s') \
    .path('x / path_width', 'm', lower=-0.1, upper=0.1, activator='epsilon1') \
    .terminal('x - x_f', 'm')   \
    .terminal('v - v_f', 'm')   \
    .terminal('t - 1', 's')

ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)

bvp_solver_direct = beluga.bvp_algorithm('Pseudospectral', number_of_nodes=30)
bvp_solver_indirect = beluga.bvp_algorithm('Collocation', number_of_nodes=30)

solinit = Solution(t=np.linspace(0,1,num=10), y=np.zeros((10,2)), q=np.array([]), u=np.zeros((10,1)))
solinit.dynamical_parameters = np.array([])
solinit.aux['const'] = {'x_0':0, 'x_f':0, 'v_0':1, 'v_f':-1, 'x_limit':0.1, 'path_width':1, 'epsilon1':1}

guess_maker_direct = beluga.guess_generator('static', solinit=solinit)
guess_maker_indirect = beluga.guess_generator('auto',
                start=[0, 1],          # Starting values for states in order
                direction='forward',
                costate_guess = -0.1,
                control_guess = [-2],
                use_control_guess=True,
)


beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.DEBUG)

sol_set_direct = beluga.solve(ocp,
             method='direct',
             bvp_algorithm=bvp_solver_direct,
             steps=None,
             guess_generator=guess_maker_direct, autoscale=False)


continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(5) \
    .const('x_0', 0) \
    .const('v_0', 1) \
    .const('x_f', 0) \
    .const('v_f', -1)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('path_width', 1)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('epsilon1', 1e-1)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('epsilon1', 1e-2)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('epsilon1', 1e-3)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('epsilon1', 1e-4)

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .const('epsilon1', 1e-5)


sol_set_indirect = beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver_indirect,
             steps=continuation_steps,
             guess_generator=guess_maker_indirect, autoscale=False)

sol_direct = sol_set_direct[-1][-1]
sol_indirect = sol_set_indirect[-1][-1]

import matplotlib.pyplot as plt
ts = np.linspace(sol_direct.t[0], sol_direct.t[-1], num=200)

plt.plot(sol_direct.t, sol_direct.y[:,0], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.y[:,0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:,0], linestyle='-', color='b', label='indirect')
plt.plot([sol_direct.t[0], sol_direct.t[-1]], [sol_direct.aux['const']['x_limit']]*2, linestyle='--', color='k')
plt.title('Position')
plt.xlabel('Time [s]')
plt.legend()
plt.show()

plt.plot(sol_direct.t, sol_direct.y[:,1], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.y[:,1], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:,1], linestyle='-', color='b', label='indirect')
plt.title('Velocity')
plt.xlabel('Time [s]')
plt.legend()
plt.show()

plt.plot(sol_direct.t, sol_direct.u, linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.u[:,0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.u, linestyle='-', color='b', label='indirect')
plt.title('Control')
plt.xlabel('Time [s]')
plt.legend()
plt.show()

plt.plot(sol_direct.t, sol_direct.dual[:,0], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.dual[:,0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:,2], linestyle='-', color='b', label='indirect')
plt.title('Position Costate')
plt.xlabel('Time [s]')
plt.legend()
plt.show()

plt.plot(sol_direct.t, sol_direct.dual[:,1], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.dual[:,1], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:,3], linestyle='-', color='b', label='indirect')
plt.title('Velocity Costate')
plt.xlabel('Time [s]')
plt.legend()
plt.show()
