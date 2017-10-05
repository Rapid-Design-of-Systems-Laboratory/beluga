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
ocp.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
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
                start=[80000,0,5000,-90*pi/180],
                direction='forward',
                costate_guess = -0.1
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .terminal('h', 0)

continuation_steps.add_step('bisection') \
                .num_cases(41)  \
                .terminal('theta', 10*pi/180)

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

# import numpy as np
# import beluga.bvpsol as bvpsol
# import beluga.bvpsol.algorithms as algorithms
# import beluga.optim.Problem
# from beluga.optim.problem import *
# from beluga.continuation import *
# from math import *
#
# import functools
#
# def get_problem():
#     # Figure out way to implement caching automatically
#     #@functools.lru_cache(maxsize=None)
#
#     def CLfunction(alfa):
#         return 1.5658*alfa
#
#     def CDfunction(alfa):
#         return 1.6537*alfa**2 + 0.0612
#     #
#     # from beluga.utils import keyboard
#     # keyboard()
#
#     """A simple planar hypersonic problem example."""
#
#     # Rename this and/or move to optim package?
#     problem = beluga.optim.Problem('planarHypersonic')
#     # problem = beluga.optim.Problem()
#
#
#     # Define independent variables
#     problem.independent('t', 's')
#
#     # Define quantities used in the problem
#     problem.quantity('rho','rho0*exp(-h/H)')
#     problem.quantity('Cl','(1.5658*alfa + -0.0000)')
#     problem.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
#     problem.quantity('D','0.5*rho*v^2*Cd*Aref')
#     problem.quantity('L','0.5*rho*v^2*Cl*Aref')
#     problem.quantity('r','re+h')
#
#     # Define equations of motion
#     problem.state('h','v*sin(gam)','m')   \
#            .state('theta','v*cos(gam)/r','rad')  \
#            .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
#            .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')
#
#     # Define controls
#     problem.control('alfa','rad')
#
#     # Define costs
#     problem.cost['terminal'] = Expression('-v^2','m^2/s^2')
#
#     # Define constraints
#     problem.constraints().initial('h-h_0','m') \
#                         .initial('theta-theta_0','rad') \
#                         .initial('v-v_0','m/s') \
#                         .terminal('h-h_f','m')  \
#                         .terminal('theta-theta_f','rad')
#
#     # Define constants
#     problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
#     problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
#     problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m
#
#     problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
#     problem.constant('re',6378000,'m') # Radius of planet, m
#     problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
#
#     problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=2)
#     # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100000, verbose = True, cached = False)
#
#     problem.scale.unit('m','h')         \
#                    .unit('s','h/v')     \
#                    .unit('kg','mass')   \
#                    .unit('rad',1)
#
#     problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180],costate_guess=-0.1)
#     #problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14])
#     # Figure out nicer way of representing this. Done?
#
#     problem.steps.add_step().num_cases(11) \
#                             .terminal('h', 0)
#
#     problem.steps.add_step().num_cases(41)  \
#                             .terminal('theta', 10*pi/180)
#     # #
#     # problem.steps.add_step()
#     #                 .num_cases(3)
#     #                 .terminal('x', 40.0)
#     #                 .terminal('y',-40.0)
#     # )
#     return problem
#
# if __name__ == '__main__':
#     import beluga.Beluga as Beluga
#     problem = get_problem()
#     sol = Beluga.run(problem)
