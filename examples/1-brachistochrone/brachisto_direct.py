"""Brachistochrone example."""
import beluga
from beluga.bvpsol import Solution
import numpy as np
import logging
from math import pi

ocp = beluga.OCP('brachisto')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('y1', 'y2', 'm') \
   .state('y2', 'u', 'm')

# Define controls
ocp.control('u','1')

# Define constants
ocp.constant('y2_0', 0.1, 'm')
ocp.constant('y2_f', -0.1, 'm')

# Define costs
ocp.path_cost('u', '1')

# Define constraints
ocp.constraints() \
    .initial('y1', 'm')    \
    .initial('y2-y2_0', 'm') \
    .path('y1-1/9', 'm') \
    .terminal('y1', 'm')   \
    .terminal('y2-y2_f', 'm')

bvp_solver = beluga.bvp_algorithm('Pseudospectral', number_of_nodes=30)
t = np.linspace(0,1,num=6)
y1 = np.linspace(0,0,num=6)
y2 = np.linspace(0,0,num=6)
y3 = np.linspace(0,1,num=6)
q = np.array([])
u = np.array([np.linspace(0,0,num=6)]).T
solinit = Solution(t=t, y=np.column_stack((y1,y2)), q=q, u=u)
solinit.dynamical_parameters = np.array([])
solinit.aux['const'] = {'y2_0':1, 'y2_f':-1}

guess_maker = beluga.guess_generator('static', solinit=solinit)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .const('y2_0', 1) \
                .const('y2_f',-1)

beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.DEBUG)

sol = beluga.solve(ocp,
             method='direct',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker, autoscale=False)

import matplotlib.pyplot as plt
ts = np.linspace(sol.t[0],sol.t[-1],num=500)
from beluga.bvpsol.algorithms.Pseudospectral import linter
plt.plot(sol.t, sol.y[:,0], marker='o')
plt.plot(ts, linter(sol.t, sol.y[:,0], ts))
plt.show()
