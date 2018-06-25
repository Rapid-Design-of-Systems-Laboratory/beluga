"""Brachistochrone example."""
from math import pi
ocp = beluga.OCP('missle')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('n', 'V*cos(psi)*cos(gam)', 'm')   \
   .state('e', 'V*sin(psi)*cos(gam)', 'm')   \
   .state('d', '-V*sin(gam)', 'm') \
   .state('psi', 'g*tan(bank)/V', 'rad') \


# Define controls
ocp.control('gam','rad')
ocp.control('bank','rad')

# Define constants
ocp.constant('V',100,'m/s')
ocp.constant('g',-9.81,'m/s^2')
# ocp.constant('tfreal',50,'s')

# Define costs
ocp.path_cost('1','s')

# Define constraints
ocp.constraints() \
    .initial('n-n_0','m')    \
    .initial('e-e_0','m')    \
    .initial('d-d_0','m')    \
    .terminal('n-n_f','m')    \
    .terminal('e-e_f','m')    \
    .terminal('d-d_f','m')    \
    .path('bankLim','bank','<>',60*pi/180,'rad',start_eps=1e-5) \
    .path('gamLim','gam','<>',60*pi/180,'rad',start_eps=1e-5)\

ocp.scale(m='n', s='n/V', kg=1, rad=1, nd=1)
# ocp.scale(m='V', s=1, kg=1, rad=1, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        tolerance=1e-4,
                        max_iterations=30,
                        verbose = True,
                        derivative_method='fd',
                        max_error=100,
             )

bvp_solver = beluga.bvp_algorithm('qcpi',
                    tolerance=1e-4,
                    max_iterations=50,
                    verbose = True,
)

guess_maker = beluga.guess_generator('auto',
                start=[-1000,-1000,-1000,pi/4],          # Starting values for states in order
                direction='forward',
                costate_guess = 0.0,
                control_guess = 0.0,
                use_control_guess = True,
                time_integrate=0.1
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(10) \
                .terminal('n', 0.0)\
                .terminal('e', 0.0)\
                .terminal('psi',pi/4)\
                .terminal('d',-1000)

continuation_steps.add_step('bisection') \
                .num_cases(21) \
                .terminal('d',-900) \
                .initial('n',-5000) \
                .initial('e',-5000)

# continuation_steps.add_step('bisection') \
#                 .num_cases(5) \
#                 .constant('eps_bankLim',1e-4) \
#                 .constant('eps_gamLim',1e-4)
#
continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .initial('n',-10000) \
                .initial('e',-10000)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

# beluga.solve(problem)
#     # from timeit import timeit
#
#     # print(timeit("get_problem()","from __main__ import get_problem",number=10))
#     beluga.run(get_problem())
