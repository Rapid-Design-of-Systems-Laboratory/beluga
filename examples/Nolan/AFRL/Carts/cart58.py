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

        p11, p12, p13,\
            p22, p23, \
            p33 \
            = symbols('p11 p12 p13\
                       p22 p23 \
                       p33')

        P = Matrix([[p11, p12, p13],
                    [p12, p22, p23],
                    [p13, p13, p33]])

        F = Matrix([[diff(x_dot, x), diff(x_dot, y), diff(x_dot, theta)],
                    [diff(y_dot, x), diff(y_dot, y), diff(y_dot, theta)],
                    [diff(theta_dot, x), diff(theta_dot, y), diff(theta_dot, theta)],])

        G = Matrix([[cos(theta), 0],
                    [sin(theta), 0],
                    [0, 1]])

        h = sqrt((x - xb)**2 + (y - yb)**2)

        H = Matrix([[diff(h, x), diff(h, y), diff(h, theta)]])

        Q = Dt*diag(sigv**2, sigw**2)

        R = Dt*diag(sigr**2)

        P_dot = (F*P + P*F.T - P*H.T*(R**-1)*H*P + G*Q*G.T)

        Dim = P_dot.shape

        for i in range(0, Dim[0]):
            for j in range(i, Dim[1]):
                # print(P_dot[i, j])
                writeList.append(P_dot[i, j])

        PP = - P * H.T * (R ** -1) * H * P

        obj = PP[1, 1]

        # h_new, theta_new, v_new, gam_new = symbols('h_new, theta_new, v_new, gam_new')
        # h_scale, theta_scale, v_scale, gam_scale = symbols('h_scale, theta_scale, v_scale, gam_scale')

        states = [x, y, theta,
                  p11, p12, p13,
                  p22, p23,
                  p33]

        x_s, y_s, theta_s, \
        p11_s, p12_s, p13_s, \
        p22_s, p23_s, \
        p33_s = \
        symbols('x_s, y_s, theta_s, \
                p11_s, p12_s, p13_s, \
                p22_s, p23_s, \
                p33_s')

        scales = [x_s, y_s, theta_s,
                  p11_s, p12_s, p13_s,
                  p22_s, p23_s,
                  p33_s]

        x_n, y_n, theta_n, \
        p11_n, p12_n, p13_n, \
        p22_n, p23_n, \
        p33_n = \
            symbols('x_n, y_n, theta_n, \
                    p11_n, p12_n, p13_n, \
                    p22_n, p23_n, \
                    p33_n')

        states_new = [x_n, y_n, theta_n,
                      p11_n, p12_n, p13_n,
                      p22_n, p23_n,
                      p33_n]

        # print(writeList)

        Z1 = zip(writeList, scales)

        scaledList = []

        for item, Scale in Z1:
            # print(item)
            item = item/Scale
            # print(item)
            # for state, new, scale in Z2:
            #     print(state)
            #     print(new)
            #     print(scale)
            Z2 = zip(states, states_new, scales)
            for state, new, scale in Z2:
                # print(new)
                item = item.subs(state, scale*new)
            # print(item)
            scaledList.append(item)

        Z2 = zip(states, states_new, scales)
        for state, new, scale in Z2:
            # print(new)
            obj = obj.subs(state, scale * new)

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
    problem\
        .state('x_n',  eqnsList[0] + '+ ep*u_max*cos(w)', '1')   \
        .state('y_n',  eqnsList[1], '1') \
        .state('theta_n', eqnsList[2], '1') \
        .state('p11_n', eqnsList[3], '1') \
        .state('p12_n', eqnsList[4], '1') \
        .state('p13_n', eqnsList[5], '1') \
        .state('p22_n', eqnsList[6], '1') \
        .state('p23_n', eqnsList[7], '1') \
        .state('p33_n', eqnsList[8], '1') \

        # Define controls
    problem.control('w', '1') \

    # Define costs
    # problem.cost['path'] = Expression('p11', 'm^2/s^2')
    problem.cost['path'] = Expression(str(obj), 's')
    # problem.cost['terminal'] = Expression('p22_n', '1')

    # Define constraints
    problem.constraints() \
        .initial('x_n-x_n_0', '1') \
        .initial('y_n-y_n_0', '1') \
        .initial('theta_n-theta_n_0', '1') \
 \
        .initial('p11_n-p11_n_0', '1') \
        .initial('p12_n-p12_n_0', '1') \
        .initial('p13_n-p13_n_0', '1') \
        .initial('p22_n-p22_n_0', '1') \
        .initial('p23_n-p23_n_0', '1') \
        .initial('p33_n-p33_n_0', '1') \
 \
        .terminal('x_n-x_n_f', '1') \
        .terminal('y_n-y_n_f', '1') \
 \

        # Define constants
    problem.constant('Dt', 0.1, '1')
    problem.constant('sigv', 0.1, '1')
    problem.constant('sigw', 0.1, '1')
    problem.constant('sigr', 0.1, '1')

    problem.constant('xb', 5, '1')
    problem.constant('yb', 5, '1')

    problem.constant('u_max', 0.1, '1')

    problem.constant('v', 30, '1')

    problem.constant('x_s',     1, '1')
    problem.constant('y_s',     1, '1')
    problem.constant('theta_s', 1, '1')

    problem.constant('p11_s', 1e-3, '1')
    problem.constant('p12_s', 1e-3, '1')
    problem.constant('p13_s', 1e-3, '1')

    problem.constant('p22_s', 1e-1, '1')
    problem.constant('p23_s', 1e-2, '1')

    problem.constant('p33_s', 1e-3, '1')

    problem.constant('ep', 5, '1')

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd', tolerance=1e-4, max_iterations=1000, verbose=True, cached=False, number_arcs=16)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose=True, cached=False)

    problem.scale.unit('m', 1)       \
                 .unit('s', 1)     \
                 .unit('kg', 1)   \
                 .unit('rad', 1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]
    problem.guess.setup('auto', start=[0, 0, 0, 0, 0, 0, 0, 0, 0], time_integrate=1, costate_guess=[0, 0, 0.001, -0.0001, 0.0, 0.0, 0.001, 0.0, 0.])
    # problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14,0.00,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(5) \
        .terminal('x_n', 20) \
        .terminal('y_n', 0) \

    problem.steps.add_step().num_cases(20) \
        .terminal('x_n', 80) \

    problem.steps.add_step().num_cases(10) \
        .const('xb', 7) \
        .const('yb', 7) \


        # problem.steps.add_step().num_cases(20) \
    #     .terminal('x_n', 150) \
    #     .terminal('y_n', 0) \


        # problem.steps.add_step().num_cases(15) \
    #     .terminal('theta', 5)

    # problem.steps.add_step().num_cases(21)  \
    #                         .terminal('theta', 10*pi/180)

    Beluga.run(problem, display_level=logging.DEBUG)

