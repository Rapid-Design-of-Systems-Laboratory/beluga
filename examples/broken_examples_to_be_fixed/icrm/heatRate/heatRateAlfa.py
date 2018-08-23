
"""Planar hypersonic problem with simple path constraint."""
from math import pi
# Rename this and/or move to optim package?
ocp = beluga.OCP('heatRateWithAlfaConstraint')

# Define independent variables
ocp.independent('t', 's')

# Define quantities used in the problem
ocp.quantity('rho','rho0*exp(-h/H)')
ocp.quantity('Cl','(1.5658*alfa + -0.0000)')
ocp.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
ocp.quantity('D','0.5*rho*v^2*Cd*Aref')
ocp.quantity('L','0.5*rho*v^2*Cl*Aref')
ocp.quantity('r','re+h')

# Define equations of motion
ocp.state('h','(v*sin(gam))','m')   \
       .state('theta','v*cos(gam)/r','rad')  \
       .state('v','(-D/mass - mu*sin(gam)/r**2)','m/s') \
       .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')

# Define controls

# Define controls
ocp.control('u','nd')

# Define costs
ocp.terminal_cost('-v^2','m^2/s^2')

# Planetary constants
ocp.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
ocp.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
ocp.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m
ocp.constant('re',6378000,'m') # Radius of planet, m

# Vehicle constants
ocp.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
ocp.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2

# Constants related to constraints
ocp.constant('rn',1/12*0.3048,'m') # Nose radius, m
# ocp.constant('k',1.74153e-4,'sqrt(kg)/m')   # Sutton-Graves constant
ocp.constant('k',1.74153e-4,'W*(s^3/(sqrt(kg)*m))') # Some units magic
ocp.quantity('qdot','k*sqrt(rho/rn)*v^3')   # Convectional heat rate
ocp.constant('qdotMax', 10000e4, 'W')
ocp.constant('alfaMax', 40*pi/180, 'rad')
ocp.quantity('alfa','alfaMax*u')
# Define constraints
ocp.constraints().initial('h-h_0','m') \
                    .initial('theta-theta_0','rad') \
                    .initial('v-v_0','m/s') \
                    .initial('gam-gam_0','rad') \
                    .terminal('h-h_f','m')  \
                    .terminal('theta-theta_f','rad') \
                    .path('heatRate','(qdot/qdotMax)','<',1,'nd',start_eps=1e-2) \
                    .path('alfaLim','u','<>',1, 'nd', start_eps=1e-2)

bvp_solver = beluga.bvp_algorithm('Shooting',
                    derivative_method='fd',
                    # number_arcs=2,
                    tolerance=1e-4,
                    max_iterations=50,
                    verbose = True,
                    max_error=50,
)

# bvp_solver = beluga.bvp_algorithm('qcpi',
#                     tolerance=1e-4,
#                     max_iterations=300,
#                     verbose = True,
#                     max_error=50,
#                     N=81
# )

# ocp.bvp_solver = algorithms.SingleShooting(derivative_method='fd', timeout=10, tolerance=1e-5, max_iterations=20, verbose = True, cached = False, max_error=30)

ocp.scale(m='h', s='h/v', kg='mass', rad=1, nd=1, W=1e7)


continuation_steps = beluga.init_continuation()
guess_maker = beluga.guess_generator('auto',
                start=[80e3,0.0,5e3,-pi/2+1*pi/180],
                direction='forward',
                costate_guess = -0.1,
                control_guess = 0.0,
                use_control_guess = True
)
continuation_steps.add_step('bisection').num_cases(21) \
                        .terminal('h', 16000.0) \
                        .terminal('theta',0.01*pi/180)

continuation_steps.add_step('bisection').num_cases(101)  \
                        .initial('gam', -60*pi/180) \
                        .terminal('theta', 0.5*pi/180)

continuation_steps.add_step('bisection').num_cases(11)  \
                        .terminal('theta', 1*pi/180)

continuation_steps.add_step('bisection').num_cases(11)  \
                        .const('alfaMax', 40*pi/180)
beluga.solve(ocp,
             method='icrm',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker,
             output_file='data-flydown.dill'
             )
#
# # ^^ Saved as data-flydown.dill
#
# guess_maker = beluga.guess_generator('file', filename='./data-flydown.dill', step=-1, iteration=-1)
#
# continuation_steps.add_step('bisection').num_cases(6)  \
#                         .const('eps_heatRate', 1e-4)
# continuation_steps.add_step('bisection').num_cases(81)  \
#                         .const('qdotMax', 1200e4)
# beluga.solve(ocp,
#              method='icrm',
#              bvp_algorithm=bvp_solver,
#              steps=continuation_steps,
#              guess_generator=guess_maker,
#              output_file='data-1k2-eps4-eps2.dill'
#              )
# # ^^ Saved as data-1k2-eps4-eps2.dill
#
# guess_maker = beluga.guess_generator('file', filename='./data-1k2-eps4-eps2.dill', step=-1, iteration=-1)
#
# continuation_steps.add_step('bisection').num_cases(31,spacing='log') \
#                         .const('eps_alfaLim', 1e-6)
# continuation_steps.add_step('bisection').num_cases(31)  \
#                         .const('alfaMax', 45*pi/180)
# continuation_steps.add_step('bisection').num_cases(41,spacing='log')  \
#                         .const('eps_heatRate', 1e-6)
# beluga.solve(ocp,
#              method='icrm',
#              bvp_algorithm=bvp_solver,
#              steps=continuation_steps,
#              guess_generator=guess_maker,
#              output_file='data-1k2-eps6-eps6.dill'
#              )
# # ^^ Saved as data-1k2-eps6-eps4.dill
#
# guess_maker = beluga.guess_generator('file', filename='./data-1k2-eps6-eps6.dill', step=-1, iteration=-1)
# continuation_steps.add_step('bisection').num_cases(101)  \
#                         .terminal('theta', 1*pi/180)
# beluga.solve(ocp,
#              method='icrm',
#              bvp_algorithm=bvp_solver,
#              steps=continuation_steps,
#              guess_generator=guess_maker,
#              output_file='data-1k2-1deg-eps6-eps6.dill'
#              )
# # # ^^ Saved as data-1k2-eps6-eps7.dill
