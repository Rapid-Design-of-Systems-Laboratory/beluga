"""Unconstrained planar hypersonic trajectory problem."""
from math import *
import beluga

ocp = beluga.OCP('planarHypersonic')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h','v*sin(gam)','m')   \
   .state('theta','v*cos(gam)/r','rad')  \
   .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
   .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')


# Define quantities used in the problem
ocp.quantity('rho', 'rho0*exp(-h/H)')
ocp.quantity('Cl', 'CL1*alfa + CL2*exp(CL3*M) + CL0')
ocp.quantity('Cd', 'CD1*alfa**2 + k*(CD2*exp(CD3*M) + CD0)')
ocp.quantity('D', '0.5*rho*v**2*Cd*Aref')
ocp.quantity('L', '0.5*rho*v**2*Cl*Aref')
ocp.quantity('r', 're+h')

# Define controls
ocp.control('alfa','rad')

# Define constants
ocp.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
ocp.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

ocp.constant('mass', 907.2, 'kg') # Mass of vehicle, kg
ocp.constant('re', 6378000, 'm') # Radius of planet, m
ocp.constant('Aref', 0.4839, 'm^2') # Reference area of vehicle, m^2

ocp.constant('M', 15, '1')

ocp.constant('CL1', 0.0513*180/3.14159, '1/rad')
ocp.constant('CL2', 0.2945, '1')
ocp.constant('CL3', -0.1028, '1')
ocp.constant('CL0', -0.2317, '1')

ocp.constant('CD1', 7.24e-4*180**2/3.14159**2, '1/rad')
ocp.constant('CD2', 0.406, '1')
ocp.constant('CD3', -0.323, '1')
ocp.constant('CD0', 0.024, '1')

ocp.constant('k', 1, '1')

# Define costs
ocp.terminal_cost('-v^2', 'm^2/s^2')

# Define constraints
ocp.constraints() \
    .initial('h-h_0','m') \
    .initial('theta-theta_0','rad') \
    .initial('v-v_0','m/s') \
    .initial('gam-gam_0', 'rad') \
    .terminal('h-h_f','m')  \
    .terminal('theta-theta_f','rad')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=100,
                        verbose = True,
                        max_error=100
             )

guess_maker = beluga.guess_generator('auto',
                start=[50000,0,4000,00*pi/180],
                direction='forward',
                costate_guess = -0.001,
                time_integrate=1
)

continuation_steps = beluga.init_continuation()

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .terminal('h', 0)
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(21)  \
#                 .terminal('theta', 5*pi/180)

continuation_steps.add_step('bisection') \
                .num_cases(41) \
                .terminal('theta', 200/6378)

continuation_steps.add_step('bisection') \
                .num_cases(41) \
                .terminal('theta', 1000/6378) \
                .terminal('h', 0)

# continuation_steps.add_step('bisection') \
#                 .num_cases(141) \
#                 .terminal('theta', 2000/6378) \

# continuation_steps.add_step('bisection') \
#                 .num_cases(11) \
#                 .const('rho0',1.2) \

continuation_steps.add_step('bisection') \
                .num_cases(51) \
                .const('k', 0.5) \

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
