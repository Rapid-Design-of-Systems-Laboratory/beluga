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
ocp.quantity('Cl','(Cl0*alfa)')
ocp.quantity('Cd','(Cd0*alfa^2 + Cd1)')
ocp.quantity('D','0.5*rho*v^2*Cd*Aref')
ocp.quantity('L','0.5*rho*v^2*Cl*Aref')
ocp.quantity('r','re+h')
ocp.quantity('qdot','k*sqrt(rho0*exp(-h/H)/rn)*v^3')
# Define controls
ocp.control('alfa','rad')

# Define constants
ocp.constant('Cl0', 1.5658, 'nd')
ocp.constant('Cd0', 1.6537, 'nd')
ocp.constant('Cd1', 0.0612, 'nd')

ocp.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
ocp.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

ocp.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
ocp.constant('re',6378000,'m') # Radius of planet, m
ocp.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2

ocp.constant('rn',1/12*0.3048,'m') # Nose radius, m
ocp.constant('k',1.74153e-4,'sqrt(kg)/m')   # Sutton-Graves constant
# ocp.constant('g0',9.80665,'m/s^2')

ocp.constant('Wsec3pkg',1,'W*s^3*kg^-1')
ocp.constant('heatRateLimit', 1200e4, 'W')

# Define costs
ocp.terminal_cost('-v^2','m^2/s^2')


# Define constraints
ocp.constraints() \
    .initial('h-h_0','m') \
    .initial('theta-theta_0','rad') \
    .initial('v-v_0','m/s') \
    .initial('gam-gam_0', 'rad') \
    .terminal('h-h_f','m')  \
    .terminal('theta-theta_f','rad') \
    .path('heatRate','(k*sqrt(rho0*exp(-h/H)/rn)*v^3)*Wsec3pkg - heatRateLimit','<',0.0,'W')

ocp.scale(m='h', s='h/v', kg='mass', rad=1, W=1e7, nd=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=50,
                        verbose = True,
                        max_error=100
             )

guess_maker = beluga.guess_generator('auto',
                start=[80000,0,5000,-90*pi/180],
                direction='forward',
                costate_guess = -0.1
)



continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .terminal('h', 0.0)

continuation_steps.add_step('bisection').num_cases(11) \
                .initial('gam',-60*pi/180)\
                .terminal('theta', 1.0*pi/180)

# continuation_steps.add_step('bisection') \
#                 .num_cases(11)  \
#                 .terminal('theta', 2*pi/180)

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .terminal('h', 15000)

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data_unc.dill')
