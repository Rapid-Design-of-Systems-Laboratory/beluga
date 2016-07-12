import beluga.Beluga as Beluga
from beluga.optimlib import Problem

def get_problem():
    """Brachistochrone example."""

    problem = Problem('brachisto')

    # Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x', 'v*cos(theta)')   \
           .state('y', '-v*sin(theta)','m')   \
           .state('v', 'g*sin(theta)','m/s')

    # Define controls
    problem.control('theta','rad')

    # Define constants
    problem.constant('g','9.81','m/s^2')

    # Define costs
    problem.path_cost('1','s')

    # Define constraints
    problem.constraints('default',0) \
                        .initial('x-x_0','m')    \
                        .initial('y-y_0','m')    \
                        .initial('v-v_0','m/s')  \
                        .terminal('x-x_f','m')   \
                        .terminal('y-y_f','m')

    # problem.bvp_solver = Beluga.algorithm('MultipleShooting',
    #                         derivative_method='fd',
    #                         tolerance=1e-4,
    #                         max_iterations=1000,
    #                         verbose = True,
    #                         cached=False,
    #                         number_arcs=4,
    #                         max_error=100
    #                      )

    problem.bvp_solver = Beluga.algorithm('SingleShooting',
                            derivative_method='fd',
                            tolerance=1e-4,
                            max_iterations=50,
                            verbose = True,
                         )
    problem.guess.setup('auto',
                    start=[0,0,1],          # Starting values for states in order
                    direction='forward',
                    costate_guess = -0.1
    )

    problem.continuation.add_step('bisection') \
                    .num_cases(51) \
                    .terminal('x', 5) \
                    .terminal('y',-5)

    return problem

if __name__ == '__main__':
    prob = get_problem()
    print(prob)

    # problem.scale.unit('m',1)     \
    #                .unit('s',1)\
    #                .unit('kg',1)   \
    #                .unit('rad',1)
    #

#
# if __name__ == '__main__':
#     Beluga.run(get_problem())

# def get_problem():
#     """Brachistochrone example."""
#
#     # Rename this and/or move to optim package?
#     problem = Beluga.problem('brachisto')
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
#     # Define constraints
#     problem.constraints('default',0) \
#                         .initial('x-x_0','m')    \
#                         .initial('y-y_0','m')    \
#                         .initial('v-v_0','m/s')  \
#                         .terminal('x-x_f','m')   \
#                         .terminal('y-y_f','m')
#
#     # Define constants
#     problem.constant('g','9.81','m/s^2')
#
#     # problem.quantity('gDown','g*sin(theta)')
#
#     problem.scale.unit('m',1)     \
#                    .unit('s',1)\
#                    .unit('kg',1)   \
#                    .unit('rad',1)
#
#     # problem.bvp_solver = Beluga.algorithm('MultipleShooting',derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False, number_arcs=4, max_error=100)
#     problem.bvp_solver = Beluga.algorithm('SingleShooting',derivative_method='fd',tolerance=1e-4, max_iterations=50, verbose = True, cached=False)
#
#     problem.guess.setup('auto',
#                     start=[0,0,1],          # Starting values for states in order
#                     direction='forward',
#                     costate_guess = -0.1
#                     )
#
#     return problem
#
# if __name__ == '__main__':
#     Beluga.run(get_problem())
