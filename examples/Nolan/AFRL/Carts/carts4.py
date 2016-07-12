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
        v1, v2, u_max = symbols('v1, v2, u_max')
        Dt, sigv, sigw, sigr = symbols('Dt, sigv, sigw, sigr')

        # Primary States
        x1, y1, theta1, x2, y2, theta2 = symbols('x1, y1, theta1, x2, y2, theta2')


        # Control
        w1, w2 = symbols('w1, w2')

        # Secondary States


        # Primary State Rates
        x1_dot = v1 * cos(theta1)
        y1_dot = v1 * sin(theta1)
        theta1_dot = u_max * sin(w1)
        x2_dot = v2 * cos(theta2)
        y2_dot = v2 * sin(theta2)
        theta2_dot = u_max * sin(w2)

        writeList = [x1_dot, y1_dot, theta1_dot, x2_dot, y2_dot, theta2_dot]

        # Covariance Calculations

        p11, p12, p13, p14, p15, p16, \
        p22, p23, p24, p25, p26, \
        p33, p34, p35, p36, \
        p44, p45, p46, \
        p55, p56, \
        p66 \
            = symbols('p11 p12 p13 p14 p15 p16 \
                       p22 p23 p24 p25 p26 \
                       p33 p34 p35 p36 \
                       p44 p45 p46 \
                       p55 p56  \
                       p66')

        P = Matrix([[p11, p12, p13, p14, p15, p16],
                    [p12, p22, p23, p24, p25, p26],
                    [p13, p23, p33, p34, p35, p36],
                    [p14, p24, p34, p44, p45, p46],
                    [p15, p25, p35, p45, p55, p56],
                    [p16, p26, p36, p46, p56, p66]])

        F = Matrix([[diff(x1_dot, x1), diff(x1_dot, y1), diff(x1_dot, theta1), diff(x1_dot, x2), diff(x1_dot, y2), diff(x1_dot, theta2)],
                    [diff(y1_dot, x1), diff(y1_dot, y1), diff(y1_dot, theta1), diff(y1_dot, x2), diff(y1_dot, y2), diff(y1_dot, theta2)],
                    [diff(theta1_dot, x1), diff(theta1_dot, y1), diff(theta1_dot, theta1), diff(theta1_dot, x2), diff(theta1_dot, y2), diff(theta1_dot, theta2)],
                    [diff(x2_dot, x1), diff(x2_dot, y1), diff(x2_dot, theta1), diff(x2_dot, x2), diff(x2_dot, y2), diff(x2_dot, theta2)],
                    [diff(y2_dot, x1), diff(y2_dot, y1), diff(y2_dot, theta1), diff(y2_dot, x2), diff(y2_dot, y2), diff(y2_dot, theta2)],
                    [diff(theta2_dot, x1), diff(theta2_dot, y1), diff(theta2_dot, theta1), diff(theta2_dot, x2), diff(theta2_dot, y2), diff(theta2_dot, theta2)]])

        G = Matrix([[cos(theta1), 0,           0, 0],
                    [sin(theta2), 0,           0, 0],
                    [          0, 1,           0, 0],
                    [          0, 0, cos(theta2), 0],
                    [          0, 0, sin(theta2), 0],
                    [          0, 0,           0, 1]])

        h = sqrt((x1 - x2)**2 + (y1 - y2)**2)

        H = Matrix([[diff(h, x1), diff(h, y1), diff(h, theta1), diff(h, x2), diff(h, y2), diff(h, theta2)]])

        Q = Dt*diag(sigv**2, sigw**2, sigv**2, sigw**2)

        R = Dt*diag(sigr**2)

        P_dot = (F*P + P*F.T - P*H.T*(R**-1)*H*P + G*Q*G.T)

        Dim = P_dot.shape

        for i in range(0, Dim[0]):
            for j in range(i, Dim[1]):
                # print(P_dot[i, j])
                writeList.append(P_dot[i, j])

        # h_new, theta_new, v_new, gam_new = symbols('h_new, theta_new, v_new, gam_new')
        # h_scale, theta_scale, v_scale, gam_scale = symbols('h_scale, theta_scale, v_scale, gam_scale')

        states = [x1, y1, theta1, x2, y2, theta2,
                  p11, p12, p13, p14, p15, p16,
                  p22, p23, p24, p25, p26,
                  p33, p34, p35, p36,
                  p44, p45, p46,
                  p55, p56,
                  p66]

        x1_s, y1_s, theta1_s, x2_s, y2_s, theta2_s, \
        p11_s, p12_s, p13_s, p14_s, p15_s, p16_s, \
        p22_s, p23_s, p24_s, p25_s, p26_s, \
        p33_s, p34_s, p35_s, p36_s, \
        p44_s, p45_s, p46_s, \
        p55_s, p56_s, \
        p66_s = \
        symbols('x1_s, y1_s, theta1_s, x2_s, y2_s, theta2_s,\
                     p11_s, p12_s, p13_s, p14_s, p15_s, p16_s, \
                     p22_s, p23_s, p24_s, p25_s, p26_s, \
                     p33_s, p34_s, p35_s, p36_s, \
                     p44_s, p45_s, p46_s, \
                     p55_s, p56_s, \
                     p66_s')

        scales = [x1_s, y1_s, theta1_s, x2_s, y2_s, theta2_s,
                  p11_s, p12_s, p13_s, p14_s, p15_s, p16_s,
                  p22_s, p23_s, p24_s, p25_s, p26_s,
                  p33_s, p34_s, p35_s, p36_s,
                  p44_s, p45_s, p46_s,
                  p55_s, p56_s,
                  p66_s]

        x1_n, y1_n, theta1_n, x2_n, y2_n, theta2_n, \
        p11_n, p12_n, p13_n, p14_n, p15_n, p16_n, \
        p22_n, p23_n, p24_n, p25_n, p26_n, \
        p33_n, p34_n, p35_n, p36_n, \
        p44_n, p45_n, p46_n, \
        p55_n, p56_n, \
        p66_n = \
            symbols('x1_n, y1_n, theta1_n, x2_n, y2_n, theta2_n,\
                         p11_n, p12_n, p13_n, p14_n, p15_n, p16_n, \
                         p22_n, p23_n, p24_n, p25_n, p26_n, \
                         p33_n, p34_n, p35_n, p36_n, \
                         p44_n, p45_n, p46_n, \
                         p55_n, p56_n, \
                         p66_n')

        states_new = [x1_n, y1_n, theta1_n, x2_n, y2_n, theta2_n,
                      p11_n, p12_n, p13_n, p14_n, p15_n, p16_n,
                      p22_n, p23_n, p24_n, p25_n, p26_n,
                      p33_n, p34_n, p35_n, p36_n,
                      p44_n, p45_n, p46_n,
                      p55_n, p56_n,
                      p66_n]

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
    problem.state('x1_n',  eqnsList[0]+'+ ep1/x1_s*cos(w1)', '1')   \
           .state('y1_n',  eqnsList[1], '1') \
           .state('theta1_n', eqnsList[2], '1') \
           .state('x2_n',  eqnsList[3]+'+ ep2/x2_s*cos(w2)', '1') \
           .state('y2_n',  eqnsList[4], '1') \
           .state('theta2_n',   eqnsList[5], '1') \
           .state('p11_n', eqnsList[6], '1') \
           .state('p12_n', eqnsList[7], '1') \
           .state('p13_n', eqnsList[8], '1') \
           .state('p14_n', eqnsList[9], '1') \
           .state('p15_n', eqnsList[10], '1') \
           .state('p16_n', eqnsList[11], '1') \
           .state('p22_n', eqnsList[12], '1') \
           .state('p23_n', eqnsList[13], '1') \
           .state('p24_n', eqnsList[14], '1') \
           .state('p25_n', eqnsList[15], '1') \
           .state('p26_n', eqnsList[16], '1') \
           .state('p33_n', eqnsList[17], '1') \
           .state('p34_n', eqnsList[18], '1') \
           .state('p35_n', eqnsList[19], '1') \
           .state('p36_n', eqnsList[20], '1') \
           .state('p44_n', eqnsList[21], '1') \
           .state('p45_n', eqnsList[22], '1') \
           .state('p46_n', eqnsList[23], '1') \
           .state('p55_n', eqnsList[24], '1') \
           .state('p56_n', eqnsList[25], '1') \
           .state('p66_n', eqnsList[26], '1')

    # Define controls
    problem.control('w1', '1') \
           .control('w2', '1')

    # Define costs
    # problem.cost['path'] = Expression('p11', 'm^2/s^2')
    # problem.cost['path'] = Expression('0.001', 's')
    problem.cost['terminal'] = Expression('p22_n + p55_n', 'rad')

    # Define constraints
    problem.constraints() \
        .initial('x1_n-x1_n_0', '1') \
        .initial('y1_n-y1_n_0', '1') \
        .initial('theta1_n-theta1_n_0', '1') \
 \
        .initial('x2_n-x2_n_0', '1') \
        .initial('y2_n-y2_n_0', '1') \
        .initial('theta1_n-theta1_n_0', '1') \
 \
        .initial('p11_n-p11_n_0', '1') \
        .initial('p12_n-p12_n_0', '1') \
        .initial('p13_n-p13_n_0', '1') \
        .initial('p14_n-p14_n_0', '1') \
        .initial('p15_n-p15_n_0', '1') \
        .initial('p16_n-p16_n_0', '1') \
        .initial('p22_n-p22_n_0', '1') \
        .initial('p23_n-p23_n_0', '1') \
        .initial('p24_n-p24_n_0', '1') \
        .initial('p24_n-p24_n_0', '1') \
        .initial('p25_n-p25_n_0', '1') \
        .initial('p26_n-p26_n_0', '1') \
        .initial('p33_n-p33_n_0', '1') \
        .initial('p34_n-p34_n_0', '1') \
        .initial('p35_n-p35_n_0', '1') \
        .initial('p36_n-p36_n_0', '1') \
        .initial('p44_n-p44_n_0', '1') \
        .initial('p45_n-p45_n_0', '1') \
        .initial('p46_n-p46_n_0', '1') \
        .initial('p55_n-p55_n_0', '1') \
        .initial('p56_n-p56_n_0', '1') \
        .initial('p66_n-p66_n_0', '1') \
 \
        .terminal('x1_n-x1_n_f', '1') \
        .terminal('y1_n-y1_n_f', '1') \
        .terminal('x1_n-x1_n_f', '1') \
        .terminal('y1_n-y1_n_f', '1') \
 \
        # Define constants
    problem.constant('Dt', 0.1, '1')
    problem.constant('sigv', 0.01, '1')
    problem.constant('sigw', 0.01, '1')
    problem.constant('sigr', 0.01, '1')

    problem.constant('u_max', 1, '1')

    problem.constant('v1', 30, '1')
    problem.constant('v2', 30, '1')

    problem.constant('x1_s',     100, '1')
    problem.constant('y1_s',     100, '1')
    problem.constant('theta1_s', 1, '1')
    problem.constant('x2_s',     100, '1')
    problem.constant('y2_s',     100, '1')
    problem.constant('theta2_s', 1, '1')

    problem.constant('p11_s', 1, '1')
    problem.constant('p12_s', 1, '1')
    problem.constant('p13_s', 1, '1')
    problem.constant('p14_s', 1, '1')
    problem.constant('p15_s', 1, '1')
    problem.constant('p16_s', 1, '1')

    problem.constant('p22_s', 1, '1')
    problem.constant('p23_s', 1, '1')
    problem.constant('p24_s', 1, '1')
    problem.constant('p25_s', 1, '1')
    problem.constant('p26_s', 1, '1')

    problem.constant('p33_s', 1, '1')
    problem.constant('p34_s', 1, '1')
    problem.constant('p35_s', 1, '1')
    problem.constant('p36_s', 1, '1')

    problem.constant('p44_s', 1, '1')
    problem.constant('p45_s', 1, '1')
    problem.constant('p46_s', 1, '1')

    problem.constant('p55_s', 1, '1')
    problem.constant('p56_s', 1, '1')

    problem.constant('p66_s', 1, '1')


    problem.constant('ep1', 1, '1')
    problem.constant('ep2', 1.5, '1')

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd', tolerance=1e-4, max_iterations=1000, verbose=True, cached=False, number_arcs=16)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose=True, cached=False)

    problem.scale.unit('m', 1)       \
                 .unit('s', 1)     \
                 .unit('kg', 1)   \
                 .unit('rad', 1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    problem.guess.setup('auto', start=[0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], time_integrate=0.1) # costate_guess=[0, 0, 0, 0, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14,0.00,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(40) \
        .terminal('x1_n', 40) \
        .terminal('x2_n', 40) \
        .terminal('y1_n', 0) \
        .terminal('y2_n', 6) \
 \
        # problem.steps.add_step().num_cases(15) \
    #     .terminal('theta_n', 5)

    # problem.steps.add_step().num_cases(21)  \
    #                         .terminal('theta', 10*pi/180)

    Beluga.run(problem, display_level=logging.DEBUG)

