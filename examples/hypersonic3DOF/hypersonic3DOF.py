from math import pi
import dill
import numpy as np
# Figure out way to implement caching automatically
# @functools.lru_cache(maxsize=None)
# def CLfunction(alfa):
#     return 1.5658*alfa
#
# # @functools.lru_cache(maxsize=None)
# def CDfunction(alfa):
#     return 1.6537*alfa**2 + 0.0612
#
# Rename this and/or move to optim package?
ocp = beluga.OCP('hypersonic3DOF')

# Define independent variables
ocp.independent('t', 's')

rho = 'rho0*exp(-h/H)'
Cl  = '(1.5658*alfa + -0.0000)'
Cd  = '(1.6537*alfa^2 + 0.0612)'
# Cl = 'CLfunction(alfa)'
# Cd = 'CDfunction(alfa)'
D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
r   = '(re+h)'

# Define equations of motion
ocp.state('h','v*sin(gam)','m')                                     \
       .state('theta','v*cos(gam)*cos(psi)/('+r+'*cos(phi))','rad')    \
       .state('phi','v*cos(gam)*sin(psi)/'+r,'rad')                    \
       .state('v','-'+D+'/mass - mu*sin(gam)/'+r+'^2','m/s')            \
       .state('gam',L+'*cos(bank)/(mass*v) - mu/(v*'+r+'^2)*cos(gam) + v/'+r+'*cos(gam)','rad')                                         \
       .state('psi',L+'*sin(bank)/(mass*cos(gam)*v) - v/'+r+'*cos(gam)*cos(psi)*tan(phi)','rad')

# Define controls
ocp.control('bank','rad') \
       .control('alfa','rad')

# Define costs
ocp.terminal_cost('-v^2','m^2/s^2')

# Define constraints
ocp.constraints().initial('h-h_0','m')              \
                 .initial('theta-theta_0','rad')     \
                 .initial('phi-phi_0','rad')         \
                 .initial('v-v_0','m/s')             \
                 .terminal('h-h_f','m')              \
                 .terminal('theta-theta_f','rad')    \
                 .terminal('phi-phi_f','rad') \
                 .initial('psi-psi_0','rad')


# Define constants
ocp.constant('mu',3.986e5*1e9,'m^3/s^2') # Gravitational parameter, m^3/s^2
ocp.constant('rho0',1.2,'kg/m^3') # Sea-level atmospheric density, kg/m^3
ocp.constant('H',7500,'m') # Scale height for atmosphere of Earth, m
ocp.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
ocp.constant('re',6378000,'m') # Radius of planet, m
ocp.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
ocp.constant('rn',1/12*0.3048,'m') # Nose radius, m

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('MultipleShooting',
                        derivative_method='fd',
                        tolerance=1e-4,
                        max_iterations=100,
                        verbose = True,
                        max_error=100,
             )

with open('data-initial-guess-to-ground.dill','rb') as f:
        out = dill.load(f)

sol = out['solution'][-1][-1]
sol.aux['parameters'] = []# np.append(sol.aux['parameters'],'lagrange_initial_5')
sol.aux['constraint'] = {}
sol.arcs = None
sol.aux['arc_seq'] = (0,)
# keyboard()
# sol.aux['parameters'].append('lagrange_initial_5')
# sol.parameters = sol.parameters[0:3]
sol.y = np.r_[sol.y, sol.u]
sol.parameters = np.concatenate((sol.parameters[0:4],(0,),sol.parameters[4:]),axis=0)
sol.parameters = np.array([])
# sol.parameters.append(0.0)
guess_maker = beluga.guess_generator('static', solinit = sol)

# problem.guess.setup('file', filename='data-initial-guess-to-ground.dill', step=-1, iteration=-1)



#
# guess_maker = beluga.guess_generator('auto',
#                 start=[80000,0,0,5000,-(90+5)*pi/180, 0],
#                 direction='forward',
#                 costate_guess = -0.01,
#                 control_guess=[0.0,0.0],
#                 time_integrate=0.01,
# )

continuation_steps = beluga.init_continuation()

continuation_steps.add_step().num_cases(11)           \
                        .terminal('h',0)
#
# continuation_steps.add_step().num_cases(11)          \
#                         .initial('h',80000)

continuation_steps.add_step().num_cases(41)          \
                        .terminal('theta',5*pi/180) \
                        .terminal('phi',2*pi/180)

# continuation_steps.add_step().num_cases(10)              \
#                         .terminal('theta',5*pi/180) \
#                         .terminal('phi',5*pi/180)
beluga.solve(ocp,
             method='brysonho',
             bvp_algorithm=bvp_solver,
             steps=continuation_steps,
             guess_generator=guess_maker)
