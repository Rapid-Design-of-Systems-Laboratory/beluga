if __name__ == "__main__":
    import numpy as np
    import beluga.Beluga as Beluga
    import beluga.bvpsol as bvpsol
    import beluga.bvpsol.algorithms as algorithms
    import beluga.optim.Problem
    from beluga.optim.problem import *
    from beluga.continuation import *

    import logging

    # Import Libraries for Matrix Calculations

    from sympy import symbols, Matrix, Transpose, simplify, diff, diag
    from sympy import sin
    from sympy import cos, acos
    from sympy import sqrt
    from sympy import exp
    from sympy import atan

    from numpy import pi

    writeEqn = True
    simpList = False

    if writeEqn:
        writeList = []

        # Constants
        v, u_max = symbols('v, u_max')
        xb, yb = symbols('xb, yb')
        Dt, sigv, sigw, sigr = symbols('Dt, sigv, sigw, sigr')

        # Primary States
        x, y, theta = symbols('x, y, theta')

        # Control
        w = symbols('w')

        # Secondary States


        # Primary State Rates
        x_dot = v * cos(theta)
        y_dot = v * sin(theta)
        theta_dot = u_max * sin(w)

        writeList = [x_dot, y_dot, theta_dot]

        # Covariance Calculations

        p11, p12, \
        p22, \
            = symbols('p11 p12 \
                       p22')

        P = Matrix([[p11, p12],
                    [p12, p22]])

        F = Matrix([[diff(x_dot, x), diff(x_dot, y)],
                    [diff(y_dot, x), diff(y_dot, y)]])

        G = Matrix([[cos(theta)],
                    [sin(theta)]])

        h = sqrt((x - xb)**2 + (y - yb)**2)

        H = Matrix([[diff(h, x), diff(h, y)]])

        Q = Dt*diag(sigv**2)

        R = Dt*diag(sigr**2)

        P_dot = (F*P + P*F.T - P*H.T*(R**-1)*H*P + G*Q*G.T)

        Dim = P_dot.shape

        for i in range(0, Dim[0]):
            for j in range(i, Dim[1]):
                # print(P_dot[i, j])
                writeList.append(P_dot[i, j])

        # h_new, theta_new, v_new, gam_new = symbols('h_new, theta_new, v_new, gam_new')
        # h_scale, theta_scale, v_scale, gam_scale = symbols('h_scale, theta_scale, v_scale, gam_scale')

        states = [x, y, theta,
                  p11, p12,
                  p22]

        x_s, y_s, theta_s, \
        p11_s, p12_s, \
        p22_s = \
        symbols('x_s, y_s, theta_s, \
                     p11_s, p12_s, \
                     p22_s')

        scales = [x_s, y_s, theta_s,
                  p11_s, p12_s,
                  p22_s]

        x_n, y_n, theta_n, \
        p11_n, p12_n, \
        p22_n = symbols( \
            'x_n, y_n, theta_n, \
            p11_n, p12_n, \
            p22_n')

        states_new = [x_n, y_n, theta_n,
                      p11_n, p12_n,
                      p22_n]

        # print(writeList)

        Z1 = zip(writeList, scales)

        scaledList = []

        for item, Scale in Z1:
            # print(item)
            item = item/Scale
            Z2 = zip(states, states_new, scales)
            # print(item)
            # for state, new, scale in Z2:
            #     print(state)
            #     print(new)
            #     print(scale)
            for state, new, scale in Z2:
                # print(new)
                item = item.subs(state, scale*new)
            # print(item)
            scaledList.append(item)

        k = 1
        with open("eqns.txt", "w") as my_file:
            for item in scaledList:
                if simpList:
                    # print('* ' + str(item))
                    item = simplify(item)
                    # print('# ' + str(item))
                my_file.write(str(item) + "\n")
                # print(" Wrote " + str(k) + "/" + str(len(scaledList)))
                k += 1

        k = 1
        with open("eqnsUnscaled.txt", "w") as my_file:
            for item in writeList:
                my_file.write(str(item) + "\n")
                # print(" Wrote " + str(k) + "/" + str(len(writeList)))
                k += 1

    ''' Start Optimal Control Calculations '''

    # Read Covariance State Rates from File
    with open("eqns.txt", "r") as f:
        eqnsList = list(f)

    # for item in P_dot_eqns:
    #     print(item)

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('carts0')

    # Define independent variables
    problem.independent('t', 's')


    # Define equations of motion
    problem.state('x_n',  eqnsList[0]+'+ ep/x_s*cos(w)', '1')   \
           .state('y_n',  eqnsList[1], '1') \
           .state('theta_n', eqnsList[2], '1') \
           .state('p11_n', eqnsList[3], '1') \
           .state('p12_n', eqnsList[4], '1') \
           .state('p22_n', eqnsList[5], '1') \

    # Define controls
    problem.control('w', '1') \

    # Define costs
    # problem.cost['path'] = Expression('p11', 'm^2/s^2')
    problem.cost['path'] = Expression('k', 's')
    problem.cost['terminal'] = Expression('(1-k)*p22_n', 'rad')

    # Define constraints
    problem.constraints() \
        .initial('x_n-x_n_0', '1') \
        .initial('y_n-y_n_0', '1') \
 \
        .initial('p11_n-p11_n_0', '1') \
        .initial('p12_n-p12_n_0', '1') \
        .initial('p22_n-p22_n_0', '1') \
 \
        .terminal('x_n-x_n_f', '1') \
        .terminal('y_n-y_n_f', '1') \
 \
        # Define constants
    problem.constant('Dt', 0.1, '1')
    problem.constant('sigv', 0.01, '1')
    problem.constant('sigw', 0.01, '1')
    problem.constant('sigr', 0.01, '1')

    problem.constant('xb', 0, '1')
    problem.constant('yb', 600, '1')

    problem.constant('u_max', 1, '1')

    problem.constant('v', 30, '1')

    problem.constant('x_s',     100, '1')
    problem.constant('y_s',     100, '1')
    problem.constant('theta_s', 1, '1')

    problem.constant('p11_s', 10, '1')
    problem.constant('p12_s', 10, '1')

    problem.constant('p22_s', 10, '1')

    problem.constant('ep', 0.1, '1')

    problem.constant('k', 1, '1')

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd', tolerance=1e-4, max_iterations=1000, verbose=True, cached=False, number_arcs=16)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose=True, cached=False)

    problem.scale.unit('m', 1)       \
                 .unit('s', 1)     \
                 .unit('kg', 1)   \
                 .unit('rad', 1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    problem.guess.setup('auto', start=[0, 0, 0, 0, 0, 0], time_integrate=0.2) # costate_guess=[0, 0, 0, 0, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14,0.00,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(11) \
        .terminal('x_n', 40) \
        .terminal('y_n', 0) \

    problem.steps.add_step().num_cases(11) \
        .const('k', 0) \
 \
        # problem.steps.add_step().num_cases(15) \
    #     .terminal('theta_n', 5)

    # problem.steps.add_step().num_cases(21)  \
    #                         .terminal('theta', 10*pi/180)

    Beluga.run(problem, display_level=logging.DEBUG)

