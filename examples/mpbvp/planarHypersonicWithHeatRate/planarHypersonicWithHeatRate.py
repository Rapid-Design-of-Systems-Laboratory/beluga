"""Planar hypersonic problem with heat rate constraint."""
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

ocp.constant('rn',1/12*0.3048,'m') # Nose radius, m
ocp.constant('k',1.74153e-4,'sqrt(kg)/m')   # Sutton-Graves constant
ocp.constant('g0',9.80665,'m/s^2')

ocp.constant('Wsec3pkg',1,'W*s^3*kg^-1')
ocp.constant('heatRateLimit', 5000e4, 'kgs^-3')

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
    .path('heatRate','(k*sqrt(rho/rn)*v^3 - heatRateLimit) * Wsec3pkg','<',0.0,'W')

ocp.scale(m='h', s='h/v', kg='mass', rad=1, W=10000)

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

continuation_steps.add_step().num_cases(61) \
                .initial('gam',-60*pi/180)\
                .terminal('theta', 1.0*pi/180)

continuation_steps.add_step('bisection') \
                .num_cases(41)  \
                .terminal('theta', 4*pi/180)

continuation_steps.add_step('activate_constraint', name='heatRate')

continuation_steps.add_step('bisection') \
                .num_cases(11) \
                .constraint('heatRate', 0.0, index=1)

beluga.solve(ocp,
             method='traditional',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)

#
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
#     """A simple planar hypersonic problem example."""
#
#     # Rename this and/or move to optim package?
#     problem = beluga.optim.Problem('planarHypersonicWithHeatRate')
#
#     # Define independent variables
#     problem.independent('t', 's')
#
#     rho = 'rho0*exp(-h/H)'
#     Cl  = '(1.5658*alfa + -0.0000)'
#     Cd  = '(1.6537*alfa^2 + 0.0612)'
#
#     D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
#     L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
#     r   = '(re+h)'
#
#     dvdt = '-'+D+'/mass - mu*sin(gam)/'+r+'**2'
#     # Define equations of motion
#     problem.state('h','v*sin(gam)','m')   \
#            .state('theta','v*cos(gam)/'+r,'rad')  \
#            .state('v',dvdt,'m/s') \
#            .state('gam',L+'/(mass*v) + (v/'+r+' - mu/(v*'+r+'^2))*cos(gam)','rad') \
#         #    .state('alfa','alfaDot','rad')
#     # Define controls
#     # problem.control('alfaDot','rad/s')
#     problem.control('alfa','rad')
#
#     # Define costs
#     problem.cost['terminal'] = Expression('-v^2','m^2/s^2')
#
#     # Define constraints
#     problem.constraints().initial('h-h_0','m') \
#                         .initial('theta-theta_0','rad') \
#                         .initial('v-v_0','m/s') \
#                         .initial('gam-gam_0','rad') \
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
#     problem.constant('rn',1/12*0.3048,'m') # Nose radius, m
#     problem.constant('k',1.74153e-4,'sqrt(kg)/m')   # Sutton-Graves constant
#     # problem.constant('g0',9.80665,'m/s^2')   # Sutton-Graves constant
#     problem.constant('alfaRateMax',20*pi/180,'rad/s')
#     problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=10000, verbose = True, cached = False, number_arcs=2)
#     # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100000, verbose = True, cached = False)
#
#     problem.scale.unit('m','h')         \
#                    .unit('s','h/v')     \
#                    .unit('kg','mass')   \
#                    .unit('rad',1)       \
#                    .unit('W',10000)
#
#     # Smoothed path constraint
#     c1 = '( qdot )' # Constraint (units W/m^2 = kg m^2 s^−3/m^2 = kgs^-3)
#     problem.quantity('dcdh','(-(k*rho0*v^3*exp(-h/H))/(2*H*rn*((rho0*exp(-h/H))/rn)^(1/2)))')
#     problem.quantity('dcdv','(3*k*v**2*((rho0*exp(-h/H))/rn)**(1/2))')
#     # dcdv = '(3*k*v**2*((rho0*exp(-h/H))/rn)**(1/2))'
#     # dcdh = '(-(k*rho0*v^3*exp(-h/H))/(2*H*rn*((rho0*exp(-h/H))/rn)^(1/2)))'
#     c1_1 = 'Wsec3pkg*(dcdh*(v*sin(gam)) + dcdv*'+dvdt+')'  # First derivative
#     h1_2 = '(psi11*ue1)';              # xi11dot = ue1
#     # problem.constant('eps1',1e-4,'m^2/s^2')   # The smoothing 'penalty' factor
#     problem.constant('eps1',1e-1,'m^2')   # The smoothing 'penalty' factor
#
#     problem.state('xi11','ue1','W')
#     problem.control('ue1','W/s')    # The extra control
#     problem.constant('lim',10000e4,'W')  # The constraint limit
#     problem.quantity ('psi1','(lim - exp(-xi11))') \
#             .quantity('psi11','(exp(-xi11)*ue1)') \
#             .quantity('qdot',' k*sqrt('+rho+'/rn)*v^3 * Wsec3pkg')
#     problem.constraints('default',0).initial('xi11 - xi11_0','W') \
#                                     .equality(c1_1+' - '+h1_2,'W/s')
#
#     problem.constant('Wsec3pkg',1,'W*s^3*kg^-1')
#     problem.constant('invW',1,'W^-1')
#     problem.constant('sec',1,'s')
#
#     # # Control constraint
#     # c2 = '(alfaDot)'
#     # h2 = '(psi2)'
#     # problem.quantity ('psi2','alfaRateMax - (2*alfaRateMax/(1+exp((2/alfaRateMax)*ue2)))')
#     # problem.control('ue2','rad/s^2')
#
#     # problem.constant('inverseSecondSquared',1,'1/s^2')
#     # problem.constraints('default',0).equality(c2+' - '+h2,'rad/s')
#
#     problem.cost['path'] = Expression('eps1*((ue1*invW)^2)','m^2/s^2')
#     # problem.cost['path'] = Expression('eps1*(inverseKgSecondSquared^2*ue1^2 + inverseSecondSquared*ue2^2)','m^2/s^2')
#
#     # problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180,722399.607]) # qdot(0) = 722399.607
#     problem.guess.setup('file',filename='fpa.dill',step=-1, iteration=-1)
#
#     problem.steps.add_step().num_cases(101) \
#                             .initial('xi11', 722399.607)
#     #
#     # problem.steps.add_step().num_cases(101).initial('gam',-70*pi/180)\
#     #                         .terminal('theta', 0.3*pi/180)
#     # problem.steps.add_step().num_cases(21)  \
#     #                          .terminal('theta', 4*pi/180)
#     return problem
#
# if __name__ == '__main__':
#     import beluga.Beluga as Beluga
#     problem = get_problem()
#     sol = Beluga.run(problem)
