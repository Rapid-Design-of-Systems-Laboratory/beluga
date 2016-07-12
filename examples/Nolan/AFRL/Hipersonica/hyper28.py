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

    from sympy import symbols, Matrix, Transpose, simplify, diff
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
        rho0, h_ref, A_ref, r_e, mass, mu = symbols('rho0, h_ref, A_ref, r_e, mass, mu')
        sig_h, sig_t, sig_v, sig_g, sig_r, sig_b, Dt = symbols('sig_h, sig_t, sig_v, sig_g, sig_r, sig_b Dt')
        theta_b = symbols('theta_b')

        # Primary States
        h, theta, v, gam = symbols('h, theta, v, gam')


        # Control
        a_trig, a_max, u, u_max = symbols('a_trig, a_max, u, u_max')

        # alpha = a_max*sin(a_trig)
        alpha = symbols('alpha')

        # Secondary States
        rho = rho0 * exp(-h/h_ref)
        Cl = 1.5658*alpha*180/pi + -0.00000
        Cd = 1.6537*(alpha*180/pi)**2 + 0.0612
        D = 0.5*rho*v**2*Cd*A_ref
        L = 0.5*rho*v**2*Cl*A_ref
        r = r_e + h

        # Primary State Rates
        h_dot = v*sin(gam)
        theta_dot = v*cos(gam)/r
        v_dot = -D/mass - mu*sin(gam)/r**2
        gam_dot = L/(mass*v) + (v/r - mu/(v*r**2))*cos(gam)

        alpha_dot = u_max*sin(u)

        writeList = [h_dot, theta_dot, v_dot, gam_dot, alpha_dot]

        # Covariance Calculations

        p11, p12, p13, p14, \
            p22, p23, p24,  \
            p33, p34,       \
            p44                    \
            = symbols('p11 p12 p13 p14 \
                       p22 p23 p24 \
                       p33 p34 \
                       p44')

        P = Matrix([[p11, p12, p13, p14],
                    [p12, p22, p23, p24],
                    [p13, p23, p33, p34],
                    [p14, p24, p34, p44]])

        F = Matrix([[diff(h_dot, h),     diff(theta_dot, h),     diff(v_dot, h),     diff(gam_dot, h)],
                    [diff(h_dot, theta), diff(theta_dot, theta), diff(v_dot, theta), diff(gam_dot, theta)],
                    [diff(h_dot, v),     diff(theta_dot, v),     diff(v_dot, v),     diff(gam_dot, v)],
                    [diff(h_dot, gam),   diff(theta_dot, gam),   diff(v_dot, gam),   diff(gam_dot, gam)]]).T

        G = Matrix([[0, 0],
                    [0, 0],
                    [1, 0],
                    [0, 1]])

        theta_r = theta - theta_b

        Rho = sqrt(
            r_e ** 2 + r ** 2 - 2 * r * r_e * cos(theta - theta_b))  # sqrt(2*r_e*(r_e + h)*(1 - cos(theta_r)) + h**2)

        H = Matrix([[diff(Rho, h), diff(Rho, theta), diff(Rho, v), diff(Rho, gam)]])

        Q = Dt * Matrix([[sig_v ** 2, 0],
                         [0, sig_g ** 2]])

        R = Dt * Matrix([[sig_r ** 2]])

        P_dot = (F*P + P*F.T - P*H.T*(R**-1)*H*P + G*Q*G.T)

        Dim = P_dot.shape

        for i in range(0, Dim[0]):
            for j in range(i, Dim[1]):
                # print(P_dot[i, j])
                writeList.append(P_dot[i, j])

        # h_new, theta_new, v_new, gam_new = symbols('h_new, theta_new, v_new, gam_new')
        # h_scale, theta_scale, v_scale, gam_scale = symbols('h_scale, theta_scale, v_scale, gam_scale')

        states = [h, theta, v, gam, a_trig,
                  p11, p12, p13, p14,
                  p22, p23, p24,
                  p33, p34,
                  p44]

        h_s, theta_s, v_s, gam_s, \
            p11_s, p12_s, p13_s, p14_s, \
            p22_s, p23_s, p24_s, \
            p33_s, p34_s, \
            p44_s = \
            symbols('h_s, theta_s, v_s, gam_s, \
                  p11_s, p12_s, p13_s, p14_s, \
                  p22_s, p23_s, p24_s, \
                  p33_s, p34_s, \
                  p44_s')

        scales = [h_s, theta_s, v_s, gam_s, 1,
                  p11_s, p12_s, p13_s, p14_s,
                  p22_s, p23_s, p24_s,
                  p33_s, p34_s,
                  p44_s]

        h_n, theta_n, v_n, gam_n, \
            p11_n, p12_n, p13_n, p14_n, \
            p22_n, p23_n, p24_n, \
            p33_n, p34_n, \
            p44_n = \
            symbols('h_n, theta_n, v_n, gam_n, \
                  p11_n, p12_n, p13_n, p14_n, \
                  p22_n, p23_n, p24_n, \
                  p33_n, p34_n, \
                  p44_n')

        states_new = [h_n, theta_n, v_n, gam_n, a_trig,
                  p11_n, p12_n, p13_n, p14_n,
                  p22_n, p23_n, p24_n,
                  p33_n, p34_n,
                  p44_n]

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
        alfa = symbols('alpha')
        with open("eqnsUnscaled.txt", "w") as my_file:
            for item in writeList:
                item = item.subs(a_max*sin(a_trig),alfa)
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
    problem = beluga.optim.Problem('hyperKalman7')
    # problem = beluga.optim.Problem()


    # Define independent variables
    problem.independent('t', 's')

    # rho = 'rho0*exp(-h/H)'
    # Cl  = '(1.5658*alfa + -0.0000)'
    # Cd  = '(1.6537*alfa^2 + 0.0612)'
    # Cl = 'CLfunctio0n(alfa)'
    # Cd = 'CDfunction(alfa)'

    # D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
    # L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
    # r   = '(re+h)'

    # Define equations of motion
    problem.state('h_n',     eqnsList[0], 'm')   \
           .state('theta_n', eqnsList[1], 'rad') \
           .state('v_n',     eqnsList[2]+'+ ep*u_max/v_s*cos(u)', 'm/s') \
           .state('gam_n',   eqnsList[3], 'rad') \
           .state('alpha',   eqnsList[4], 'rad') \
           .state('p11_n',   eqnsList[5], 'm**2') \
           .state('p12_n',   eqnsList[6], 'm') \
           .state('p13_n',   eqnsList[7], 'm**2/s') \
           .state('p14_n',   eqnsList[8], 'm') \
           .state('p22_n',   eqnsList[9], 'rad')\
           .state('p23_n',   eqnsList[10], 'rad*m/s') \
           .state('p24_n',   eqnsList[11], 'rad**2') \
           .state('p33_n',   eqnsList[12], 'm**2/s**2') \
           .state('p34_n',   eqnsList[13], 'm/s') \
           .state('p44_n',   eqnsList[14], 'rad**2') \


    # Define controls
    problem.control('u', 'rad')

    # Define costs
    # problem.cost['path'] = Expression('p11', 'm^2/s^2')
    # problem.cost['path'] = Expression('0.001', 's')
    problem.cost['terminal'] = Expression('p22_n', '1')

    # Define constraints
    problem.constraints() \
        .initial('h_n-h_n_0', 'm') \
        .initial('theta_n-theta_n_0', 'rad') \
        .initial('v_n-v_n_0', 'm/s') \
        .initial('gam_n-gam_n_0', 'rad') \
        .initial('p11_n-p11_n_0', 'm**2') \
        .initial('p12_n-p12_n_0', 'm') \
        .initial('p13_n-p13_n_0', 'm**2/s') \
        .initial('p14_n-p14_n_0', 'm') \
        .initial('p22_n-p22_n_0', 'rad^2') \
        .initial('p23_n-p23_n_0', 'rad*m/s') \
        .initial('p24_n-p24_n_0', 'rad**2') \
        .initial('p33_n-p33_n_0', 'm**2/s**2') \
        .initial('p34_n-p34_n_0', 'm/s') \
        .initial('p44_n-p44_n_0', 'rad**2') \
        .terminal('h_n-h_n_f', 'm') \
        .terminal('theta_n-theta_n_f', 'rad')

    # Define constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2')  # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3')  # Sea-level atmospheric density, kg/m^3
    problem.constant('h_ref', 7500, 'm')  # Scale height for atmosphere of Earth, m
    problem.constant('mass', 750/2.2046226, 'kg')  # Mass of vehicle, kg
    problem.constant('r_e', 6378000, 'm')  # Radius of planet, m
    problem.constant('A_ref', pi*(24*.0254/2)**2, 'm^2')  # Reference area of vehicle, m^2
    problem.constant('rn', 1/12*0.3048, 'm')  # Nose radius, m

    problem.constant('Dt', 0.1, 's')  # time step
    problem.constant('sig_v', 10.0, 'm/s**2')  # var in v
    problem.constant('sig_g', 0.1*pi/180, 'rad/s')  # var in gam
    problem.constant('sig_r', 100.0, 'm')  # var in range
    problem.constant('theta_b', -2*pi/180, 'rad')  # location of kalmanBeacon

    problem.constant('a_max', 10.0*pi/180, 'rad')
    problem.constant('u_max', 1*pi/180, 'rad/s')

    problem.constant('h_s', 1000, 'rad')
    problem.constant('theta_s', 1, 'rad')
    problem.constant('v_s', 1000, 'rad')
    problem.constant('gam_s', 1, 'rad')
    problem.constant('p11_s', 1e5, 'rad')
    problem.constant('p12_s', 1e-2, 'rad')
    problem.constant('p13_s', 1e2, 'rad')
    problem.constant('p14_s', 1e-1, 'rad')
    problem.constant('p22_s', 1e-10, 'rad')
    problem.constant('p23_s', 1e-5, 'rad')
    problem.constant('p24_s', 1e-8, 'rad')
    problem.constant('p33_s', 1e1, 'rad')
    problem.constant('p34_s', 1e-3, 'rad')
    problem.constant('p44_s', 1e-6, 'rad')

    problem.constant('ep', 40, 'rad')

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd', tolerance=1e-4, max_iterations=1000, verbose=True, cached=False, number_arcs=16)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose=True, cached=False)

    problem.scale.unit('m', 1)       \
                 .unit('s', 1)     \
                 .unit('kg', 1)   \
                 .unit('rad', 1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    problem.guess.setup('auto', start=[80, 0, 5, -89*pi/180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], costate_guess=[0, 0, 0, 0, 0.0001, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], time_integrate=2.5) # costate_guess=[0, 0, 0, 0, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14,0.00,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
    # Figure out nicer way of representing this. Done?


    problem.steps.add_step().num_cases(101) \
        .terminal('theta_n', 1*pi/180) \
        .terminal('h_n', 0)

    # problem.steps.add_step().num_cases(15) \
    #     .terminal('theta_n', 5)

    # problem.steps.add_step().num_cases(21)  \
    #                         .terminal('theta', 10*pi/180)

    Beluga.run(problem, display_level=logging.DEBUG)

