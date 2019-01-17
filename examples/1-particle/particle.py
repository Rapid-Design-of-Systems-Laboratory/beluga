"""Brachistochrone example."""
import beluga
from beluga.bvpsol.Solution import Solution
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

# Define costs
ocp.path_cost('u**2', '1')

# Define constraints
ocp.constraints() \
    .initial('x - x_0', 'm')    \
    .initial('v - v_0', 'm/s') \
    .terminal('x - x_f', 'm')   \
    .terminal('v - v_f', 'm')

ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('Pseudospectral')

solinit = Solution(t=np.linspace(0,1,num=10), y=np.zeros((10,2)), q=np.array([]), u=np.zeros((10,1)))
solinit.dynamical_parameters = np.array([])
solinit.aux['const'] = {'x_0':0, 'x_f':0, 'v_0':1, 'v_f':-1}

guess_maker = beluga.guess_generator('static', solinit=solinit)

beluga.add_logger(logging_level=logging.DEBUG)

sol = beluga.solve(ocp,
             method='direct',
             bvp_algorithm=bvp_solver,
             steps=None,
             guess_generator=guess_maker, autoscale=False)

import matplotlib.pyplot as plt
plt.plot(sol.t, sol.y[:,0])
plt.plot(sol.t, sol.y[:,1])
plt.show()
