import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *
import functools
from PIL import Image
from scipy import interpolate
import scipy.ndimage as ndimage
import gdal

def get_problem():
    """A test of dynamic continuation on aircraft noise minimization"""

    problem = beluga.optim.Problem('AircraftNoise3DOF')
    problem.mode='analytical' #Other options: 'numerical', 'dae'

    #Define independent variables
    problem.independent('t', 's')

    #Problem quantities
    problem.quantity('bank','bankmax*sin(banktrig)')    \
           .quantity('alfa','alfamax*sin(alfatrig)')    \
           .quantity('D','C1*v^2+C2/(v^2)')   \
           .quantity('L','mass*g')    \
           .quantity('T','1560*sin(Ttrignew)+1860')   \
           .quantity('Ft','T*cos(alfa) - D')    \
           .quantity('Fn','T*sin(alfa) + L')

    #Define equations of motion
    problem.state('x','v*cos(gam)*cos(psii)','m')    \
           .state('y','v*cos(gam)*sin(psii)','m')   \
           .state('z','v*sin(gam)','m') \
           .state('v','Ft/mass - g*sin(gam)','m/s') \
           .state('psii','Fn*sin(bank)/(mass*cos(gam)*v)','rad')    \
           .state('gam','Fn*cos(bank)/(mass*v) - g*cos(gam)/v','rad')

    # Define controls
    problem.control('banktrig','rad') \
           .control('alfatrig','rad')   \
           .control('Ttrignew','kg*m/s^2')

    # Define cost functional
    problem.cost['path'] =  Expression('T^5.2 * cos(gam)/(v*(z+50)^2.5)', 'nd')

    #Define constraints
    problem.constraints().initial('x-x_0','m') \
                         .initial('y-y_0','m') \
                         .initial('z-z_0','m') \
                         .initial('v-v_0','m/s') \
                         .initial('psii-psii_0','rad') \
                         .initial('gam-gam_0','rad') \
                         .terminal('x-x_f','m') \
                         .terminal('y-y_f','m') \
                         .terminal('z-z_f','m') \
                         .terminal('v-v_f','m/s') \
                         .terminal('psii-psii_f','rad') \
                         .terminal('gam-gam_f','rad')

    #Define constants
    problem.constant('mu',3.986e5*1e9,'m^3/s^2') #Gravitational parameter
    problem.constant('rho0',1.2,'kg/m^3') #Sea level atmospheric density
    problem.constant('H',7500,'m') #Atmospheric scale height
    problem.constant('re',6378000,'m') #Radius of Earth
    problem.constant('Aref',112,'m^2')
    problem.constant('bankmax',60*np.pi/180,'rad')
    problem.constant('alfamax',15*np.pi/180,'rad')
    problem.constant('Tmax',3420,'kg*m/s^2')
    problem.constant('Tmin',300,'kg*m/s^2')
    problem.constant('g',9.81,'m/s^2')
    problem.constant('mass',7180/9.81,'kg')
    problem.constant('C1',0.226,'kg/m')
    problem.constant('C2',5.2e6,'kg*m^3/s^4')

    #Unit scaling
    problem.scale.unit('m',1) \
                 .unit('s',1) \
                 .unit('kg',1) \
                 .unit('nd',1) \
                 .unit('rad',1)

    #Configure solver
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=50, verbose = True, cached = False, number_arcs=8)
    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=50, verbose = True, cached = False)

    #Initial Guess
    problem.guess.setup('auto',start=[0,0,1197,124,0*np.pi/180,0*np.pi/180])

    #Add continuation steps
    problem.steps.add_step(strategy='manual').num_cases(20) \
                            .terminal('x', 5400) \
                            .terminal('y', 4600) \
                            .terminal('z', 0) \
                            .terminal('v', 77.5) \
                            .terminal('psii', 45*np.pi/180) \
                            .terminal('gam', 0)

    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
