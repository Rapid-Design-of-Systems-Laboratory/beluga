if __name__ == "__main__":
    import numpy as np
    import beluga.Beluga as Beluga
    import beluga.bvpsol as bvpsol
    import beluga.bvpsol.algorithms as algorithms
    import beluga.optim.Problem
    from beluga.optim.problem import *
    from beluga.continuation import *

    import logging

    ''' Start Optimal Control Calculations '''

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('z03')

    # Define independent variables
    problem.independent('t', 's')


    # Define equations of motion
    problem.state('x', 'v*cos(a) + ep*k*cos(u)', 'm')   \
           .state('y', 'v*sin(a)', 'm') \
           .state('a', 'k*sin(u)', 'rad') \

    # Define controls
    problem.control('u', 'rad') \

    # Define costs
    problem.cost['path'] = Expression('1', '1')

    # Define constraints
    problem.constraints() \
        .initial('x-x_0', 'm') \
        .initial('y-y_0', 'm') \
        .initial('a-a_0', 'rad') \
 \
        .terminal('x-x_f', 'm') \
        .terminal('y-y_f', 'm') \
 \
    # Define constants
    problem.constant('k', 1, 'rad/s')

    problem.constant('v', 1, 'm/s')

    problem.constant('ep', 0.5, 'm/rad')

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd', tolerance=1e-6, max_iterations=1000, verbose=True, cached=False, number_arcs=16)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose=True, cached=False)

    problem.scale.unit('m', 1)       \
                 .unit('s', 1)     \
                 .unit('kg', 1)   \
                 .unit('rad', 1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    problem.guess.setup('auto', start=[0, 0, 0], costate_guess=[-0.1, -0.1, -0.001], time_integrate=0.1) # costate_guess=[0, 0, 0, 0, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14,0.00,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
    # Figure out nicer way of representing this. Done?

    # problem.steps.add_step().num_cases(10) \
    #     .const('ep', 0.05) \

    problem.steps.add_step().num_cases(10) \
        .terminal('x', 1.0) \
        .terminal('y', 0) \

    problem.steps.add_step().num_cases(10) \
        .terminal('x', 10.05) \
        .terminal('y', 0) \

    problem.steps.add_step().num_cases(10) \
        .terminal('y', 10) \

    problem.steps.add_step().num_cases(10) \
        .const('ep', 0.1) \

    problem.steps.add_step().num_cases(6) \
        .const('ep', 0.01)

    Beluga.run(problem, display_level=logging.DEBUG)

