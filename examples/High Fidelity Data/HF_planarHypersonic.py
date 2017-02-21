import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *
import functools
from scipy import interpolate

#Load look-up table
f = np.loadtxt('SphereConeTable.txt')
alfalist = []
CLdata = []
CDdata = []
for line in f:
    alfalist.append(line[0])
    CLdata.append(line[1])
    CDdata.append(line[2])
CLtck = interpolate.splrep(alfalist,CLdata) #(tck = knots,coefficients,order)
CDtck = interpolate.splrep(alfalist,CDdata)

def CLlookup(alfa, dc, rn, rc):
    if np.iscomplex(alfa)==True:
        deriv=interpolate.splev(np.real(alfa),CLtck,der=1)
        return deriv*1j*1e-30
    else:
        return interpolate.splev(alfa,CLtck,der=0)

def CDlookup(alfa, dc, rn, rc):
    if np.iscomplex(alfa)==True:
        deriv=interpolate.splev(np.real(alfa),CDtck,der=1)
        return deriv*1j*1e-30
    else:
        return interpolate.splev(alfa,CDtck,der=0)

def CLfunction(alfa, dc, rn, rc):
    CN = (1-(rn/rc)**2*np.cos(dc)**2)*np.cos(dc)**2*np.sin(2*alfa)
    CA = (1-np.sin(dc)**4)*(rn/rc)**2 + (2*np.sin(dc)**2*np.cos(alfa)**2+np.cos(dc)**2*np.sin(alfa)**2)*(1-(rn/rc)**2*np.cos(dc)**2)
    return CN*np.cos(alfa) - CA*np.sin(alfa)

def CDfunction(alfa, dc, rn, rc):
    CN = (1-(rn/rc)**2*np.cos(dc)**2)*np.cos(dc)**2*np.sin(2*alfa)
    CA = (1-np.sin(dc)**4)*(rn/rc)**2 + (2*np.sin(dc)**2*np.cos(alfa)**2+np.cos(dc)**2*np.sin(alfa)**2)*(1-(rn/rc)**2*np.cos(dc)**2)
    return CA*np.cos(alfa) + CN*np.sin(alfa)

#Do some tests
#alfatest = 15*np.pi/180 + 1j*1e-30
#dc = 25*np.pi/180
#rc = 0.3
#rn = 0.01
#print('Derivatives')
#print(np.imag(CLfunction(alfatest, dc, rn, rc))*1e30)
#print(np.imag(CLlookup(alfatest, dc, rn, rc))*1e30)
#print(np.imag(CDfunction(alfatest, dc, rn, rc))*1e30)
#print(np.imag(CDlookup(alfatest, dc, rn, rc))*1e30)
#print('Values')
#print(CLfunction(np.real(alfatest), dc, rn, rc))
#print(CLlookup(np.real(alfatest), dc, rn, rc))
#print(CDfunction(np.real(alfatest), dc, rn, rc))
#print(CDlookup(np.real(alfatest), dc, rn, rc))
#quit()
def get_problem():

    """A simple planar hypersonic problem example."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('HF_planarHypersonic')
    problem.mode = 'analytical'
    # problem = beluga.optim.Problem()


#    alfatest = 15*np.pi/180
#    dc = 25*np.pi/180
#    rc = 2.5
#    rn = 0.25
#    print(CLfunction(alfatest, dc, rn, rc))
#    quit()

    # Define independent variables
    problem.independent('t', 's')

    # Define quantities used in the problem
    problem.quantity('rho','rho0*exp(-h/H)')
#    problem.quantity('Cl','CLfunction(alfa, dc, rn, rc)')
#    problem.quantity('Cd','CDfunction(alfa, dc, rn, rc)')
#    problem.quantity('Cl','(1.5658*alfa + -0.0000)')
#    problem.quantity('Cd','(1.6537*alfa^2 + 0.0612)')
#    problem.quantity('D','0.5*rho*v^2*Cd*Aref')
#    problem.quantity('L','0.5*rho*v^2*Cl*Aref')
    problem.quantity('r','re+h')
#TODO: need to look through problem quantities to find custom functions
    # Define equations of motion
#    problem.state('h','v*sin(gam)','m')   \
#           .state('theta','v*cos(gam)/r','rad')  \
#           .state('v','-D/mass - mu*sin(gam)/r**2','m/s') \
#           .state('gam','L/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')
    problem.state('h','v*sin(gam)','m')   \
           .state('theta','v*cos(gam)/r','rad')  \
           .state('v','-0.5*rho*v^2*CDlookup(alfa, dc, rn, rc)*Aref/mass - mu*sin(gam)/r**2','m/s') \
           .state('gam','0.5*rho*v^2*CLlookup(alfa, dc, rn, rc)*Aref/(mass*v) + (v/r - mu/(v*r^2))*cos(gam)','rad')

    # Define controls
    problem.control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-v^2','m^2/s^2')

    # Define constraints
    problem.constraints().initial('h-h_0','m') \
                        .initial('theta-theta_0','rad') \
                        .initial('v-v_0','m/s') \
                        .terminal('h-h_f','m')  \
                        .terminal('theta-theta_f','rad')

    # Define constants
    problem.constant('mu', 3.986e5*1e9, 'm^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0', 1.2, 'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H', 7500, 'm') # Scale height for atmosphere of Earth, m

    problem.constant('dc',25*np.pi/180,'rad') #Vehicle cone angle
    problem.constant('rc',0.3,'m') #Vehicle cone base radius
    problem.constant('rn',0.01,'m') #Vehicle nose radius

    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',pi*(0.3)**2,'m^2') # Reference area of vehicle, m^2

    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=4, max_error=200)
    # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=100000, verbose = True, cached = False)

    problem.scale.unit('m','h')         \
                   .unit('s','h/v')     \
                   .unit('kg','mass')   \
                   .unit('rad',1)

    problem.guess.setup('auto',start=[80000,0,5000,-90*pi/180],costate_guess=-0.1)
    #problem.guess.setup('auto',start=[80000,3.38575809e-21,5000,7.98617365e-02],direction='forward',time_integrate=229.865209,costate_guess =[-1.37514494e+01,3.80852584e+06,-3.26290152e+03,-2.31984720e-14])
    # Figure out nicer way of representing this. Done?

    problem.steps.add_step().num_cases(10) \
                            .terminal('h', 0)

    problem.steps.add_step().num_cases(40)  \
                            .terminal('theta', 10*pi/180)
    # #
    # problem.steps.add_step()
    #                 .num_cases(3)
    #                 .terminal('x', 40.0)
    #                 .terminal('y',-40.0)
    # )
    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
