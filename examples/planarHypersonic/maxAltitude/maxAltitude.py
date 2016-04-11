import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *

import functools

def get_problem():
    # Figure out way to implement caching automatically
    #@functools.lru_cache(maxsize=None)
    # from beluga.utils import keyboard
    # keyboard()

    """A simple planar hypersonic problem example."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('planarHypersonic')
    # problem = beluga.optim.Problem()


    # Define independent variables
    problem.independent('t', 's')

    # rho = 'rho0*exp(-h/H)'
    # Cl  = '(1.5658*alfa + -0.0000)'
    # Cd  = '(1.6537*alfa^2 + 0.0612)'
    # D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
    # L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
    # r   = '(re+h)'
    problem.quantity('rho','rho0*exp(-h/H)')
    # problem.quantity('Cl','(Cl1*(w*alfa + (1-w)*alfaCtrl) + -0.0000)')
    # problem.quantity('Cd','(Cd2*(w*alfa + (1-w)*alfaCtrl)^2 + Cd0)')
    problem.quantity('Cl','(Cl1*(alfa) + -0.0000)')
    problem.quantity('Cd','(Cd2*(alfa)^2 + Cd0)')
    problem.quantity('qA','0.5*rho*v^2*Aref')
    # problem.quantity('D','0.5*rho*v^2*Cd*Aref')
    # problem.quantity('L','0.5*rho*v^2*Cl*Aref')
    problem.quantity('r','re+h')

    # Define equations of motion
    # problem.state('h','v*sin(gam) + eps * cos(alfaDotTrig)','m')   \
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/r','rad')  \
           .state('v','-qA*Cd/mass - mu*sin(gam)/r**2','m/s') \
           .state('gam','qA*Cl/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad') \
           .state('alfa','alfaDot','rad')
        #    .state('alfa','alfaRateMax*sin(alfaDotTrig)','rad')
    # problem.state('h','v*sin(gam)','m')   \
    #        .state('theta','v*cos(gam)/'+r,'rad')  \
    #        .state('v','-'+D+'/mass - mu*sin(gam)/'+r+'**2','m/s') \
    #        .state('gam',L+'/(mass*v) + (v/'+r+' - mu/(v*'+r+'^2))*cos(gam)','rad')

    # Define controls
    # problem.control('alfa','rad')
    problem.control('alfaDot','rad/s')
    # problem.control('alfaDotTrig','rad')
    # problem.control('alfaCtrl','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .terminal('h-h_f','m')  \
                        .terminal('theta-theta_f','rad') \
                        .path('h','<','hMax','m') \
                        .control('alfaDot','-alfaRateMax','alfaRateMax','rad/s')

    # Define constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    problem.constant('Cd2', 1.6537, 'nd')
    problem.constant('Cd0', 0.0612, 'nd')
    problem.constant('Cl1', 1.5658, 'nd')

    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
    problem.constant('rn',1/12*0.3048,'m') # Nose radius, m
    problem.constant('hMax', 85000, 'm')
    problem.constant('alfaRateMax', 10*pi/180, 'rad/s')

    # problem.constant('eps',10, 'm/s')
    # problem.constant('w',0, 'nd')
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=21, verbose = True, cached = False, number_arcs=2, max_error=100000)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='csd',tolerance=1e-4, max_iterations=100000, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1) \
                   .unit('nd',1)


    # import dill, numpy as np
    # f = open('alfa.dill','rb')
    # out = dill.load(f)
    # f.close()
    #
    # sol = out['solution'][-1][0]
    # alfaDot = np.append(np.arcsin(np.diff(sol.u)/(10*3.14/180)),0)
    # # Construct initial guess
    # sol.y = np.vstack((sol.y[:4,:], sol.u, sol.y[4:8,:], np.ones_like(sol.x)*100, sol.y[8,:]))
    # sol.u = np.vstack((alfaDot, sol.u))
    # problem.guess.setup('static', solinit=sol)

    #problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14])

    problem.guess.setup('auto',start=[80000,0.01,5000,-90*pi/180, 0*pi/180], costate_guess=0.1, time_integrate=0.1)
    # problem.guess.setup('auto',start=[80000,0.01,5000,-90*pi/180])
    problem.steps.add_step('bisection') \
                            .num_cases(11) \
                            .terminal('h', 0)
    problem.steps.add_step('bisection') \
                            .num_cases(31) \
                            .terminal('theta', 10*pi/180)
    #

    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
