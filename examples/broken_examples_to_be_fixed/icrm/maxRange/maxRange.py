from math import *

ocp = beluga.OCP('maxRange')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h','v*sin(gam)','m')   \
   .state('theta','v*cos(gam)/r','rad')  \
   .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
   .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')


# Define quantities used in the problem
ocp.quantity('rho','rho0*exp(-h/H)')
# ocp.quantity('Cl','(1.5658*alfa + -0.0000)')
# ocp.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
ocp.quantity('Cl','(1.4428*alfa)')
ocp.quantity('Cd','(2.1877*alfa^2 + 0.0503)')

ocp.quantity('D','0.5*rho*v^2*Cd*Aref')
ocp.quantity('L','0.5*rho*v^2*Cl*Aref')
ocp.quantity('r','re+h')

# Define controls
ocp.control('alfa','rad')

# Define constants
ocp.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
ocp.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

ocp.constant('mass',203.21,'kg') # Mass of vehicle, kg
ocp.constant('re',6378000,'m') # Radius of planet, m
ocp.constant('Aref',0.1877,'m^2') # Reference area of vehicle, m^2

# Constants related to constraints
ocp.constant('alfaMax', 11*pi/180, 'rad')

# Define costs
ocp.terminal_cost('-theta^2','rad^2')

# Define constraints
ocp.constraints() \
    .initial('h-h_0','m') \
    .initial('theta-theta_0','rad') \
    .initial('v-v_0','m/s') \
    .initial('gam-gam_0','rad') \
    .terminal('h-h_f','m')  \
    .path('aoaLimit','alfa/alfaMax','<>',1,'nd',start_eps=1e-2) \

ocp.scale(m='h', s='h/v', kg='mass', rad=1, W=1, nd=1)

continuation_steps = beluga.init_continuation()
continuation_steps.add_step('bisection').num_cases(11) \
                        .initial('v', 1000) \
                        .terminal('h', 12000)
continuation_steps.add_step('bisection').num_cases(31) \
                        .initial('v', 2500)

continuation_steps.add_step('bisection').num_cases(5) \
                        .initial('h',20000)
continuation_steps.add_step('bisection').num_cases(51) \
                        .initial('v',3000)
# continuation_steps.add_step('bisection').num_cases(21,spacing='log') \
#                         .const('eps_aoaLimit',1e-3)

continuation_steps.add_step('bisection').num_cases(11) \
                        .initial('gam',5*pi/180)
continuation_steps.add_step('bisection').num_cases(51) \
                        .initial('v',3800)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=50,
                        verbose = True,
                        max_error=100
             )

guess_maker = beluga.guess_generator('auto',
    start=[15000,0,500,0*pi/180],
    costate_guess=-0.0000001,
    time_integrate=50
)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
