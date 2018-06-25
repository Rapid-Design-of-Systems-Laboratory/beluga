tol = 1e-3


def test_brachistochrone():
    from math import pi
    import beluga

    from beluga.ivpsol import Trajectory
    from beluga.bvpsol import Solution

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

    ocp.constraints().set_adjoined(False)

    ocp.scale(m='y', s='y/v', kg=1, rad=1)

    bvp_solver = beluga.bvp_algorithm('Shooting')

    guess_maker = beluga.guess_generator('auto', start=[0, 0, 0], direction='forward', costate_guess=-0.1, control_guess = [-pi/2], use_control_guess=True)

    continuation_steps = beluga.init_continuation()

    continuation_steps.add_step('bisection') \
        .num_cases(21) \
        .terminal('x', 10) \
        .terminal('y', -10)

    sol = beluga.solve(ocp, method='traditional', bvp_algorithm=bvp_solver, steps=continuation_steps, guess_generator=guess_maker)

    assert isinstance(sol, Trajectory)
    assert isinstance(sol, Solution)

    y0 = sol.y.T[0]
    yf = sol.y.T[-1]
    assert abs(y0[0] - 0) < tol
    assert abs(y0[1] - 0) < tol
    assert abs(y0[2] - 0) < tol
    assert abs(y0[3] + 0.0667) < tol
    assert abs(y0[4] - 0.0255) < tol
    assert abs(y0[5] + 0.1019) < tol
    assert abs(sol.t[-1] - 1.8433) < tol
    assert abs(yf[0] - 10) < tol
    assert abs(yf[1] + 10) < tol
    assert abs(yf[2] - 14.0071) < tol
    assert abs(yf[3] + 0.0667) < tol
    assert abs(yf[4] - 0.0255) < tol
    assert abs(yf[5] - 0) < tol
    assert abs(y0[3] - yf[3]) < tol
    assert abs(y0[4] - yf[4]) < tol

    sol = beluga.solve(ocp, method='icrm', bvp_algorithm=bvp_solver, steps=continuation_steps, guess_generator=guess_maker)

    y0 = sol.y.T[0]
    yf = sol.y.T[-1]
    assert abs(y0[0] - 0) < tol
    assert abs(y0[1] - 0) < tol
    assert abs(y0[2] - 0) < tol
    assert abs(y0[3] + 0.0667) < tol
    assert abs(y0[4] - 0.0255) < tol
    assert abs(y0[5] + 0.1019) < tol
    assert abs(sol.t[-1] - 1.8433) < tol
    assert abs(yf[0] - 10) < tol
    assert abs(yf[1] + 10) < tol
    assert abs(yf[2] - 14.0071) < tol
    assert abs(yf[3] + 0.0667) < tol
    assert abs(yf[4] - 0.0255) < tol
    assert abs(yf[5] - 0) < tol
    assert abs(y0[3] - yf[3]) < tol
    assert abs(y0[4] - yf[4]) < tol


def test_brachistochrone_adjoined():
    from math import pi
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

    ocp.constraints().set_adjoined(True)

    ocp.scale(m='y', s='y/v', kg=1, rad=1)

    bvp_solver = beluga.bvp_algorithm('Shooting')

    guess_maker = beluga.guess_generator('auto', start=[0, 0, 0], direction='forward', costate_guess=-0.1, control_guess = [-pi/2], use_control_guess=True)

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
    assert abs(sol.t[-1] - 1.8433) < tol
    assert abs(yf[0] - 10) < tol
    assert abs(yf[1] + 10) < tol
    assert abs(yf[2] - 14.0071) < tol
    assert abs(yf[3] + 0.0667) < tol
    assert abs(yf[4] - 0.0255) < tol
    assert abs(yf[5] - 0) < tol
    assert abs(y0[3] - yf[3]) < tol
    assert abs(y0[4] - yf[4]) < tol

    sol = beluga.solve(ocp, method='icrm', bvp_algorithm=bvp_solver, steps=continuation_steps, guess_generator=guess_maker)

    y0 = sol.y.T[0]
    yf = sol.y.T[-1]
    assert abs(y0[0] - 0) < tol
    assert abs(y0[1] - 0) < tol
    assert abs(y0[2] - 0) < tol
    assert abs(y0[3] + 0.0667) < tol
    assert abs(y0[4] - 0.0255) < tol
    assert abs(y0[5] + 0.1019) < tol
    assert abs(sol.t[-1] - 1.8433) < tol
    assert abs(yf[0] - 10) < tol
    assert abs(yf[1] + 10) < tol
    assert abs(yf[2] - 14.0071) < tol
    assert abs(yf[3] + 0.0667) < tol
    assert abs(yf[4] - 0.0255) < tol
    assert abs(yf[5] - 0) < tol
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

    ocp.constraints().set_adjoined(True)

    ocp.scale(m='h', s='h/v', kg='mass', rad=1)

    bvp_solver = beluga.bvp_algorithm('Shooting')

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

    y0e = [80000, 0, 4000, 0.0195, -16.8243, 1212433.8085, -2836.0620, 0]
    yfe = [0, 0.0873, 2691.4733, -0.9383, 546.4540, 1212433.8085, -5382.9467, 0.1840]
    tfe = 144.5677

    assert abs((y0[0] - y0e[0]) / y0e[0]) < tol
    assert abs((y0[1] - y0e[1])) < tol
    assert abs((y0[2] - y0e[2]) / y0e[2]) < tol
    assert abs((y0[3] - y0e[3]) / y0e[3]) < tol
    assert abs((y0[4] - y0e[4]) / y0e[4]) < tol
    assert abs((y0[5] - y0e[5]) / y0e[5]) < tol
    assert abs((y0[6] - y0e[6]) / y0e[6]) < tol
    assert abs((y0[7] - y0e[7])) < tol
    assert abs((sol.t[-1] - tfe) / tfe) < tol
    assert abs((yf[0] - yfe[0])) < tol
    assert abs((yf[1] - yfe[1]) / yfe[1]) < tol
    assert abs((yf[2] - yfe[2]) / yfe[2]) < tol
    assert abs((yf[3] - yfe[3]) / yfe[3]) < tol
    assert abs((yf[4] - yfe[4]) / yfe[4]) < tol
    assert abs((yf[5] - yfe[5]) / yfe[5]) < tol
    assert abs((yf[6] - yfe[6]) / yfe[6]) < tol
    assert abs((yf[7] - yfe[7]) / yfe[7]) < tol

