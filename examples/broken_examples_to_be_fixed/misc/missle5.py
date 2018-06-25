"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('xbar', 'cos(psi)', 'nd')   \
   .state('ybar', 'sin(psi)', 'nd')   \
   .state('psi', 'abar', 'nd')
ocp.control('abar','nd')

# ocp.state('xbar2', 'cos(psi2)', 'nd')   \
#    .state('ybar2', 'sin(psi2)', 'nd')   \
#    .state('psi2', 'abar2', 'nd')
# ocp.control('abar2','nd')

# Define constants
ocp.constant('V',300,'m/s')
ocp.constant('tfreal',50,'s')
ocp.constant('ylim',1.0,'nd')

ocp.constant('w1',0.75,'nd')
ocp.constant('w2',0.25,'nd')
# ocp.constant('w3',0.33,'nd')
# Define costs
ocp.path_cost('w1*abar^2 + w2*1','nd')

# Define constraints
ocp.constraints() \
    .initial('xbar-xbar_0','nd')    \
    .initial('ybar-ybar_0','nd')    \
    .initial('psi-psi_0','nd')  \
    .terminal('xbar-xbar_f','nd')   \
    .terminal('ybar-ybar_f','nd') \
    .terminal('psi - psi_f', 'nd')
# ocp.constraints() \
#     .initial('xbar2-xbar2_0','nd')    \
#     .initial('ybar2-ybar2_0','nd')    \
#     .initial('psi2-psi2_0','nd')  \
#     .terminal('xbar2-xbar2_f','nd')   \
#     .terminal('ybar2-ybar2_f','nd') \
#     .terminal('psi2 - psi2_f', 'nd') \

ocp.constraints() \
    .path('yupper','ybar','<','ylim','nd',start_eps=1e-5)

ocp.scale(m=1, s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-4,
                        max_iterations=30,
                        verbose = True,
                        derivative_method='fd',
                        max_error=100,
             )

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-4,
                    max_iterations=100,
                    verbose = True,
                    N = 41
)

guess_maker = beluga.guess_generator('auto',
                start=[-0.8,0,pi/6],          # Starting values for states in order
                direction='forward',
                costate_guess = [0.0, 0.0, 0.1]*1 + [0.0,0.0],
                control_guess = [-0.05, 0, 0],
                time_integrate=0.1
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(51) \
                .initial('xbar', -1.0) \
                .initial('ybar', 0.0) \
                .initial('psi', pi/6) \
                .terminal('xbar', 0.0)\
                .terminal('ybar', 0.0) \
                .terminal('psi', -pi/3) \
                # .initial('xbar2', -40) \
                # .initial('ybar2', -0.0) \
                # .initial('psi2', -pi/6) \
                # .terminal('xbar2', 0.0)\
                # .terminal('ybar2', -0.0) \
                # .terminal('psi2', +pi/3)

continuation_steps.add_step('bisection') \
                .num_cases(121) \
                .constant('ylim',0.15)
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(101, spacing='log') \
#                 .constant('eps_yupper',1e-6)

#
# import numpy as np
# import dill
# with open('./data4_2veh.dill','rb') as f:
#     data = dill.load(f)
#
# sol = data['solution'][-1][-1]
# # sol.y = np.r_[sol.y[:6], np.ones((sol.x.shape[0],1))*0.1, np.ones((sol.x.shape[0],1))*0.1 ]

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
