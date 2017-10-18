"""Unconstrained planar hypersonic trajectory problem."""
from math import *

ocp = beluga.OCP('planarHypersonic')

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('h','v*sin(gam)','m')   \
   .state('theta','v*cos(gam)/r','rad')  \
   .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
   .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')


# Define quantities used in the problem
ocp.quantity('rho','rho0*exp(-h/H)')
ocp.quantity('Cl','(1.5658*alfa + -0.0000)')
ocp.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
ocp.quantity('D','0.5*rho*v^2*Cd*Aref')
ocp.quantity('L','0.5*rho*v^2*Cl*Aref')
ocp.quantity('r','re+h')

# Define controls
ocp.control('alfa','rad')

# Define constants
ocp.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
ocp.constant('rho0', 0.0001*1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

ocp.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
ocp.constant('re',6378000,'m') # Radius of planet, m
ocp.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2

# Define costs
ocp.terminal_cost('-v^2','m^2/s^2')

# Define constraints
ocp.constraints() \
    .initial('h-h_0','m') \
    .initial('theta-theta_0','rad') \
    .initial('v-v_0','m/s') \
    .terminal('h-h_f','m')  \
    .terminal('theta-theta_f','rad') \
    # .initial('gam - gam_0', 'rad')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)
# ocp.scale(m=80e3, s=1, kg=1, rad=1)

bvp_solver = beluga.bvp_algorithm('qcpi',
                        tolerance=1e-6,
                        max_iterations=500,
                        verbose = True,
                        N = 101,
             )

guess_maker = beluga.guess_generator('auto',
                start=[80e3,0.0,4000,-89*pi/180],
                direction='forward',
                costate_guess = -0.1,
                control_guess = -0.1,
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .terminal('h',10e3) \
                .terminal('theta',0.01*pi/180)

continuation_steps.add_step('bisection') \
                .num_cases(51) \
                .terminal('theta',5.0*pi/180) \
                # .initial('gam', -80*pi/180) \

continuation_steps.add_step('bisection') \
                .num_cases(101) \
                .const('rho0',1.2) \
# continuation_steps.add_step('bisection') \
#                 .num_cases(51) \
#                 .terminal('theta',0.15*pi/180)
#
# continuation_steps.add_step('bisection') \
#                 .num_cases(101) \
#                 .initial('gam',-60*pi/180) \
#                 .terminal('theta',0.5*pi/180)

beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
