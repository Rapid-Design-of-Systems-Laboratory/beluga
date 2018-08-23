from math import pi
import beluga
import logging

# Rename this and/or move to optim package?
ocp = beluga.OCP('hypersonic3DOF')

# Define independent variables
ocp.independent('t', 's')

rho = 'rho0*exp(-h/H)'
Cl = '(1.5658*alpha + -0.0000)'
Cd = '(1.6537*alpha**2 + 0.0612)'
D = '(0.5*{}*v**2*{}*Aref)'.format(rho, Cd)
L = '(0.5*{}*v**2*{}*Aref)'.format(rho, Cl)
r = '(re+h)'

# Define equations of motion
ocp \
    .state('h', 'v*sin(gam)', 'm') \
    .state('theta', 'v*cos(gam)*cos(psi)/({}*cos(phi))'.format(r), 'rad') \
    .state('phi', 'v*cos(gam)*sin(psi)/{}'.format(r), 'rad') \
    .state('v', '-{}/mass - mu*sin(gam)/{}**2'.format(D,r), 'm/s') \
    .state('gam', '{}*cos(bank)/(mass*v) - mu/(v*{}**2)*cos(gam) + v/{}*cos(gam)'.format(L,r,r), 'rad') \
    .state('psi', '{}*sin(bank)/(mass*cos(gam)*v) - v/{}*cos(gam)*cos(psi)*tan(phi)'.format(L,r), 'rad')

# Define controls
ocp.control('alpha', 'rad') \
   .control('bank', 'rad')

# Define costs
ocp.terminal_cost('-v', 'm/s')

# Define constraints
ocp.constraints() \
    .initial('h-h_0', 'm') \
    .initial('theta-theta_0', 'rad') \
    .initial('phi-phi_0', 'rad') \
    .initial('v-v_0', 'm/s') \
    .initial('gam-gam_0', 'rad') \
    .initial('psi-psi_0', 'rad') \
    .terminal('h-h_f', 'm') \
    .terminal('theta-theta_f', 'rad') \
    .terminal('phi-phi_f', 'rad')

# Define constants
ocp.constant('mu', 3.986e5*1e9, 'm**3/s**2')  # Gravitational parameter, m**3/s**2
ocp.constant('rho0', 1.2, 'kg/m**3')  # Sea-level atmospheric density, kg/m**3
ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp.constant('mass', 750/2.2046226, 'kg')  # Mass of vehicle, kg
ocp.constant('re', 6378000, 'm')  # Radius of planet, m
ocp.constant('Aref', pi*(24*.0254/2)**2, 'm**2')  # Reference area of vehicle, m**2
ocp.constant('rn', 1/12*0.3048, 'm')  # Nose radius, m

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('Shooting',
                                  derivative_method='fd',
                                  tolerance=1e-4,
                                  max_iterations=100,
                                  verbose=True,
                                  max_error=400,
                                  )

guess_maker = beluga.guess_generator('auto',
                                     start=[40000, 0, 0, 2000, -(90-10)*pi/180, 0],
                                     direction='forward',
                                     costate_guess=-0.1,
                                     control_guess=[0.0, 0.0],
                                     use_control_guess=True,
                                     time_integrate=0.5,
                                     )


continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection').num_cases(21) \
    .terminal('h', 0) \
    .terminal('theta', 6945.9/6378000)

continuation_steps.add_step('bisection').num_cases(21) \
    .terminal('theta', 0.5*pi/180)

continuation_steps.add_step('bisection').num_cases(41) \
    .initial('gam', 0) \
    .terminal('theta', 3*pi/180)

continuation_steps.add_step('bisection').num_cases(41) \
    .terminal('phi', 2*pi/180)

beluga.setup_beluga(logging_level=logging.DEBUG)

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
