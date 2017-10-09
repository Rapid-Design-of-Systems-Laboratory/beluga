"""Brachistochrone example."""

ocp = beluga.OCP('brachisto')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('x', 'v*cos(theta)', 'm')   \
   .state('y', '-v*sin(theta)','m')   \
   .state('v', 'g*sin(theta)','m/s')

# Define controls
ocp.control('theta','rad')

# Define constants
ocp.constant('g',9.81,'m/s^2')
ocp.constant('xlim',1.0,'m')

# Define costs
ocp.path_cost('1','s')

# Define constraints
ocp.constraints() \
    .initial('x-x_0','m')    \
    .initial('y-y_0','m')    \
    .initial('v-v_0','m/s')  \
    .terminal('x-x_f','m')   \
    .terminal('y-y_f','m') \
    .path('constraint1','y + x','>',-1.0,'m')
    # .path('constraint2','y + 0.75*x','>',-2,'m')  #\


ocp.scale(m='x', s='x/v', kg=1, rad=1, nd=1)
# ocp.scale(m=1, s=1, kg=1, rad=1)


bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                    derivative_method='fd',
                    tolerance=1e-4,
                    max_iterations=100,
                    verbose = True,
                    max_error=50
)

guess_maker = beluga.guess_generator('auto',
                start=[0,0,1],          # Starting values for states in order
                direction='forward',
                costate_guess = 0.1,
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(6) \
                .terminal('x', 10) \
                .terminal('y',-10)

continuation_steps.add_step('bisection').num_cases(41,spacing='log') \
                 .const('eps_constraint1', 1e-4)


beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)


# """Brachistochrone example."""
#
# import numpy as np
#
# import beluga.Beluga as Beluga
# import beluga.bvpsol as bvpsol
# import beluga.bvpsol.algorithms as algorithms
# import beluga.optim.Problem
# from beluga.optim.problem import *
# from beluga.continuation import *
#
# def get_problem():
#     """Brachistochrone example."""
#
#     # Rename this and/or move to optim package?
#     problem = beluga.optim.Problem('boundedBrachistochrone')
#
#     # Define independent variables
#     problem.independent('t', 's')
#
#     # Define equations of motion
#     problem.state('x', 'v*cos(theta)','m')   \
#            .state('y', '-v*sin(theta)','m')   \
#            .state('v', 'g*sin(theta)','m/s')
#     # Define controls
#     problem.control('theta','rad')
#
#     # Define costs
#     problem.cost['path'] = Expression('1','s')
#
#
#     # Define constraints
#     problem.constraints('default',0) \
#                         .initial('x-x_0','m')    \
#                         .initial('y-y_0','m')    \
#                         .initial('v-v_0','m/s')  \
#                         .terminal('x-x_f','m')   \
#                         .terminal('y-y_f','m')   \
#                         .path('constraint1','y + 1.5*x','>',-0.5,'m')\
#                         .path('constraint2','y + 0.75*x','>',-2,'m')  #\
#                         # .path('constraint1','y + x','>',-1,'m')  #\
#                         # .path('constraint2','y - 0.5*x','>',-2,'m')
#                         # y + x > h0 -- above the line y= -x + h0
#
#     # Define constants
#     problem.constant('g','9.81','m/s^2')
#
#     # Scaling poptions
#     problem.scale.unit('m','x')     \
#                    .unit('s','x/v')\
#                    .unit('kg',1)   \
#                    .unit('rad',1)
#
#     # problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False, number_arcs=2)
#     problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False)
#     # problem.bvp_solver = algorithms.BroydenShooting(tolerance=1e-4, max_iterations=1000)
#
#     # Can be array or function handle
#     # TODO: implement an "initial guess" class subclassing Solution
#     problem.guess.setup('auto',
#                     start=[0,0,1],          # Starting values for states in order
#                     direction='forward',
#                     costate_guess = 0.1
#                     )
#
#     # Figure out nicer way of representing this. Done?
#     problem.steps.add_step().num_cases(41) \
#                     .terminal('x', 5) \
#                     .terminal('y',-5)
#
#     # TODO: Automate addition of epsilon continuation
#     problem.steps.add_step('bisection').num_cases(41,spacing='log') \
#                      .const('eps_constraint1', 1e-6) #\
#                     #  .const('eps_constraint2', 1e-6)
#
#     return problem
#
# if __name__ == '__main__':
#     Beluga.run(get_problem())
