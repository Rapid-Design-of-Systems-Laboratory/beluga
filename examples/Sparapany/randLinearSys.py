if __name__ == '__main__':
    import numpy as np

    import beluga.Beluga as Beluga
    import beluga.bvpsol as bvpsol
    import beluga.bvpsol.algorithms as algorithms
    import beluga.optim.Problem
    from beluga.optim.problem import *
    from beluga.continuation import *
    from beluga.utils import keyboard
    from math import *

    import functools

    # Figure out way to implement caching automatically
    #@functools.lru_cache(maxsize=None)

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('randLinearSys')

    number_states = 3

    #np.random.seed(1300)
    D = -np.random.rand(number_states,1)-0.1
    D = np.diagflat(D)
    v = [np.random.rand(number_states,1)*2-1 for i in range(number_states)]
    v = [np.divide(v[i],np.linalg.norm(v[i],axis=0)) for i in range(number_states)]
    P = np.hstack(v)
    A = np.dot(np.dot(np.linalg.inv(P),D),P)

    # Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    for i in range(number_states):
        basestr = ''
        for j in range(number_states):
            # Define System
            problem.constant('A_'+str(i)+'_'+str(j),A[i][j],'nd') # Mass of vehicle, kg
            basestr += '+A_'+str(i)+'_'+str(j)+'*x'+str(j)

        # Define constraints
        if np.mod(i,2) == 1:
            problem.constraints().initial('x'+str(i)+'-x'+str(i)+'_0','nd')
        else:
            problem.constraints().terminal('x'+str(i)+'-x'+str(i)+'_f','nd')

        # Define States
        basestr += '+u'+str(i)+'**2'
        print(basestr)
        problem.state('x'+str(i),basestr,'nd')

        # Define Control
        problem.control('u'+str(i),'nd')

    # Define costs
    #problem.cost['terminal'] = Expression('-x0^2','nd^2')
    problem.cost['path'] = Expression('1','s')
    #problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=4)
    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False)

    problem.scale.unit('s',1)     \
                 .unit('nd',1)

    problem.guess.setup('auto',start=[0.0 for i in range(number_states)])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(50)
    #problem.steps[0].terminal('x1', 0.5)
    for i in range(number_states):
        if np.mod(i,2) == 1:
            problem.steps[0].initial('x'+str(i), 0.0)  # bvp4c takes 10 steps
        else:
            problem.steps[0].terminal('x'+str(i), 0.5)  # bvp4c takes 10 steps
    #
    # problem.steps.add_step()
    #                 .num_cases(3)
    #                 .terminal('x', 40.0)
    #                 .terminal('y',-40.0)
    # )

    # Default solver is a forward-difference Single Shooting solver with 1e-4 tolerance
    print('stophere')
    Beluga.run(problem)
    # beluga = Beluga.create(problem)
    # beluga.add_callback('before_control',mycode)
    #
