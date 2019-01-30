"""Brachistochrone example."""
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

# Define costs
ocp.path_cost('u**2', '1')

# Define constraints
ocp.constraints() \
    .initial('x - x_0', 'm')    \
    .initial('v - v_0', 'm/s')  \
    .path('x - x_limit', 'm')   \
    .terminal('x - x_f', 'm')   \
    .terminal('v - v_f', 'm')

ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('Pseudospectral', number_of_nodes=30)

solinit = Solution(t=np.linspace(0,1,num=10), y=np.zeros((10,2)), q=np.array([]), u=np.zeros((10,1)))
solinit.dynamical_parameters = np.array([])
solinit.aux['const'] = {'x_0':0, 'x_f':0, 'v_0':1, 'v_f':-1, 'x_limit':0.1}

guess_maker = beluga.guess_generator('static', solinit=solinit)

beluga.add_logger(logging_level=logging.DEBUG)

sol_set = beluga.solve(ocp,
             method='direct',
             bvp_algorithm=bvp_solver,
             steps=None,
             guess_generator=guess_maker, autoscale=False)

sol = sol_set[-1][-1]

import matplotlib.pyplot as plt
ts = np.linspace(sol.t[0], sol.t[-1], num=200)

plt.plot(sol.t, sol.y[:,0], linestyle='--', marker='o')
plt.plot(ts, linter(sol.t, sol.y[:,0], ts), linestyle='-')
plt.plot([sol.t[0], sol.t[-1]], [sol.aux['const']['x_limit']]*2, linestyle='--', color='k')
plt.title('Position')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.y[:,1], linestyle='--', marker='o')
plt.plot(ts, linter(sol.t, sol.y[:,1], ts), linestyle='-')
plt.title('Velocity')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.dual[:,0], linestyle='--', marker='o')
plt.plot(ts, linter(sol.t, sol.dual[:,0], ts), linestyle='-')
plt.title('Position Costate')
plt.xlabel('Time [s]')
plt.show()

plt.plot(sol.t, sol.dual[:,1], linestyle='--', marker='o')
plt.plot(ts, linter(sol.t, sol.dual[:,1], ts), linestyle='-')
plt.title('Velocity Costate')
plt.xlabel('Time [s]')
plt.show()
