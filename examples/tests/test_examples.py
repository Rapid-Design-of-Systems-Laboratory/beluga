tol = 1e-3


def test_brachistochrone():
    import beluga

    ocp = beluga.OCP('brachisto')

    # Define independent variables
    ocp.independent('t', 's')

    # Define equations of motion
    ocp.state('x', 'v*cos(theta)', 'm') \
        .state('y', 'v*sin(theta)', 'm') \
        .state('v', 'g*sin(theta)', 'm/s')

    # Define controls
    ocp.control('theta', 'rad')

    # Define constants
    ocp.constant('g', -9.81, 'm/s^2')

    # Define costs
    ocp.path_cost('1', 's')

    # Define constraints
    ocp.constraints() \
        .initial('x-x_0', 'm') \
        .initial('y-y_0', 'm') \
        .initial('v-v_0', 'm/s') \
        .terminal('x-x_f', 'm') \
        .terminal('y-y_f', 'm')

    ocp.scale(m='y', s='y/v', kg=1, rad=1)

    bvp_solver = beluga.bvp_algorithm('Shooting', derivative_method='fd', tolerance=1e-4, max_iterations=200, verbose=True, max_error=100)

    guess_maker = beluga.guess_generator('auto', start=[0, 0, 0], direction='forward', costate_guess=-0.1)

    continuation_steps = beluga.init_continuation()

    continuation_steps.add_step('bisection') \
        .num_cases(21) \
        .terminal('x', 10) \
        .terminal('y', -10)

    sol = beluga.solve(ocp, method='traditional', bvp_algorithm=bvp_solver, steps=continuation_steps, guess_generator=guess_maker)

    y0 = sol.y.T[0]
    yf = sol.y.T[-1]
    assert abs(y0[0] - 0) < tol
    assert abs(y0[1] - 0) < tol
    assert abs(y0[2] - 0) < tol
    assert abs(y0[3] + 0.0667) < tol
    assert abs(y0[4] - 0.0255) < tol
    assert abs(y0[5] + 0.1019) < tol
    assert abs(y0[6] - 1.8433) < tol # This is time. If this fails because time is no longer adjoined as an EOM, remove this line
    assert abs(yf[0] - 10) < tol
    assert abs(yf[1] + 10) < tol
    assert abs(yf[2] - 14.0071) < tol
    assert abs(yf[3] + 0.0667) < tol
    assert abs(yf[4] - 0.0255) < tol
    assert abs(yf[5] - 0) < tol
    assert abs(yf[6] - 1.8433) < tol # This is time. If this fails because time is no longer adjoined as an EOM, remove this line
    assert abs(y0[3] - yf[3]) < tol
    assert abs(y0[4] - yf[4]) < tol


def test_planarhypersonic():
    from math import pi
    import beluga

    ocp = beluga.OCP('planarHypersonic')

    # Define independent variables
    ocp.independent('t', 's')

    # Define equations of motion
    ocp.state('h', 'v*sin(gam)', 'm') \
        .state('theta', 'v*cos(gam)/r', 'rad') \
        .state('v', '-D/mass - mu*sin(gam)/r**2', 'm/s') \
        .state('gam', 'L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)', 'rad')

    # Define quantities used in the problem
    ocp.quantity('rho', 'rho0*exp(-h/H)')
    ocp.quantity('Cl', '(1.5658*alfa + -0.0000)')
    ocp.quantity('Cd', '(1.6537*alfa^2 + 0.0612)')
    ocp.quantity('D', '0.5*rho*v^2*Cd*Aref')
    ocp.quantity('L', '0.5*rho*v^2*Cl*Aref')
    ocp.quantity('r', 're+h')

    # Define controls
    ocp.control('alfa', 'rad')

    # Define constants
    ocp.constant('mu', 3.986e5 * 1e9, 'm^3/s^2')  # Gravitational parameter, m^3/s^2
    ocp.constant('rho0', 0.0001 * 1.2, 'kg/m^3')  # Sea-level atmospheric density, kg/m^3
    ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m

    ocp.constant('mass', 750 / 2.2046226, 'kg')  # Mass of vehicle, kg
    ocp.constant('re', 6378000, 'm')  # Radius of planet, m
    ocp.constant('Aref', pi * (24 * .0254 / 2) ** 2, 'm^2')  # Reference area of vehicle, m^2

    # Define costs
    ocp.terminal_cost('-v^2', 'm^2/s^2')

    # Define constraints
    ocp.constraints() \
        .initial('h-h_0', 'm') \
        .initial('theta-theta_0', 'rad') \
        .initial('v-v_0', 'm/s') \
        .terminal('h-h_f', 'm') \
        .terminal('theta-theta_f', 'rad')

    ocp.scale(m='h', s='h/v', kg='mass', rad=1)

    bvp_solver = beluga.bvp_algorithm('Shooting', derivative_method='fd', tolerance=1e-4, max_iterations=100, verbose=True, max_error=100)

    guess_maker = beluga.guess_generator('auto', start=[80000, 0, 4000, -90 * pi / 180], direction='forward', costate_guess=-0.1)

    continuation_steps = beluga.init_continuation()

    continuation_steps.add_step('bisection') \
        .num_cases(11) \
        .terminal('h', 0) \
        .terminal('theta', 0.01 * pi / 180)

    continuation_steps.add_step('bisection') \
        .num_cases(11) \
        .terminal('theta', 5.0 * pi / 180)

    continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .const('rho0', 1.2)

    sol = beluga.solve(ocp, method='traditional', bvp_algorithm=bvp_solver, steps=continuation_steps, guess_generator=guess_maker)

    y0 = sol.y.T[0]
    yf = sol.y.T[-1]
    assert abs(y0[0] - 80000) < tol
    assert abs(y0[1] - 0) < tol
    assert abs(y0[2] - 4000) < tol
    assert abs(y0[3] - 0.0195) < tol
    assert abs(y0[4] + 16.8243) < tol
    assert abs(y0[5] - 1306472.5796) < tol
    assert abs(y0[6] + 2834.2179) < tol
    assert abs(y0[7] - 0) < tol
    assert abs(y0[8] - 144.5677) < tol # This is time. If it fails because time is not an EOM, delete this line
    assert abs(yf[0] - 0) < tol
    assert abs(yf[1] - 0.0873) < tol
    assert abs(yf[2] - 2691.5778) < tol
    assert abs(yf[3] + 0.9383) < tol
    assert abs(yf[4] - 546.5061) < tol
    assert abs(yf[5] - 1306472.5796) < tol
    assert abs(yf[6] + 5383.1553) < tol
    assert abs(yf[7] - 0.3489) < tol
    assert abs(yf[8] - 144.5677) < tol # This is time. If it fails because time is not an EOM, delete this line
    assert abs(y0[5] - yf[5]) < tol
