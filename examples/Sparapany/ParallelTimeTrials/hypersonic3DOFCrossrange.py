import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
import matlab.engine
from beluga.utils import keyboard
from beluga.optim.problem import *
from beluga.continuation import *
from math import *

"""Hypersonic 3DOF dynamics maximizing crossrange example."""
def get_problem(state,costate,param,time):
    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('hypersonci3DOFCrossrange')

    # Define independent variables
    problem.independent('t', 's')

    # Updated aero from Mike Bolender
    #x = 'v/a' # mach
    #y = '(9*sin(ang)+5)'

    Cl = '((14185132937801937*sin(alfa))/72057594037927936 - (5421779306486855*(v/a))/2305843009213693952 - (1574554238845453*(v/a)*(9*sin(alfa) + 5))/576460752303423488 - (1081832482396803*(v/a)*(9*sin(alfa) + 5)^2)/147573952589676412928 + (795005714371527*(v/a)^2*(9*sin(alfa) + 5))/4611686018427387904 - (2905380043335151*(v/a)^2)/18446744073709551616 + (7384633541699571*(9*sin(alfa) + 5)^2)/36893488147419103232 + (4723631850413463*(9*sin(alfa) + 5)^3)/4722366482869645213696 + 40090326007262905/288230376151711744)'
    Cd = '((7975570356452291*(v/a))/144115188075855872 - (939292000388127*sin(alfa))/144115188075855872 + (4181805097702493*(v/a)^2*(9*sin(alfa) + 5)^2)/295147905179352825856 + (5799269589896587*(v/a)*(9*sin(alfa) + 5))/2305843009213693952 - (3435815237005351*(v/a)*(9*sin(alfa) + 5)^2)/18446744073709551616 - (6565772557668597*(v/a)^2*(9*sin(alfa) + 5))/9223372036854775808 - (2327227566991187*(v/a)*(9*sin(alfa) + 5)^3)/1180591620717411303424 + (3879272510917453*(v/a)^3*(9*sin(alfa) + 5))/73786976294838206464 - (4630940327334427*(v/a)^2)/144115188075855872 + (3228336930707955*(v/a)^3)/576460752303423488 - (5752786461422987*(v/a)^4)/18446744073709551616 + (59645010131291*(9*sin(alfa) + 5)^2)/72057594037927936 + (1198177006620385*(9*sin(alfa) + 5)^3)/73786976294838206464 + (1971121512347433*(9*sin(alfa) + 5)^4)/302231454903657293676544 + 506236799411217/18014398509481984)'

    rho = 'rho0*exp(-(r-re)/H)'
    #Cl  = '(1.5658*sin(alfa) + -0.0000)'
    #Cd  = '(1.6537*sin(alfa)^2 + 0.0612)'
    # Cl = 'CLfunction(alfa)'
    # Cd = 'CDfunction(alfa)'
    D   = '(0.5*'+rho+'*v^2*'+Cd+'*Aref)'
    L   = '(0.5*'+rho+'*v^2*'+Cl+'*Aref)'
    #r   = '(re+h)'
    r = 'r'
    # Define equations of motion
    problem.state('r','v*sin(gam)','m')                                     \
           .state('lam','v*cos(gam)*sin(chi)/('+r+'*cos(phi))','rad')    \
           .state('phi','v*cos(gam)*cos(chi)/'+r,'rad')                    \
           .state('v','-'+D+'/mass - mu*sin(gam)/'+r+'^2','m/s')            \
           .state('gam',L+'*cos(bank)/(mass*v) - mu/(v*'+r+'^2)*cos(gam) + v/'+r+'*cos(gam)','rad')                                         \
           .state('chi',L+'*sin(bank)/(mass*cos(gam)*v) + v/'+r+'*cos(gam)*sin(chi)*tan(phi)','rad')

    # Define controls
    problem.control('bank','rad') \
           .control('alfa','rad')

    # Define costs
    problem.cost['terminal'] = Expression('-phi^2','rad')

    # Define constraints
    problem.constraints().initial('r-r_0','m')              \
                         .initial('lam-lam_0','rad')     \
                         .initial('phi-phi_0','rad')         \
                         .initial('v-v_0','m/s')             \
                         .initial('gam-gam_0','rad')        \
                         .initial('chi-chi_0','rad')      \
                         .terminal('r-r_f','m')              \
                         .terminal('lam-lam_f','rad')

    # Define constants
    problem.constant('mu',3.986e5*1e9,'m^3/s^2') # Gravitational parameter, m^3/s^2
    problem.constant('rho0',1.2,'kg/m^3') # Sea-level atmospheric density, kg/m^3
    problem.constant('H',7500,'m') # Scale height for atmosphere of Earth, m
    problem.constant('mass',750/2.2046226,'kg') # Mass of vehicle, kg
    problem.constant('re',6378000,'m') # Radius of planet, m
    problem.constant('Aref',pi*(24*.0254/2)**2,'m^2') # Reference area of vehicle, m^2
    #problem.constant('rn',1/12*0.3048,'m') # Nose radius, m
    problem.constant('a',330,'m/s') # Speed of sound approx
    #in.const.a = {330,'m/s'}; % speed of sound
    #in.const.rn = {1/12*0.3048,'m'}; % Nose radius
    #in.const.k = {1.74153e-4,'sqrt(kg)/m^2'}; % heat rate coefficient
    #in.const.gammaThermo = {1.4,'nd'};
    #in.const.RThermo = {287,'m^2/(s^2*K)'};

    problem.scale.unit('m','r')     \
                   .unit('s','r/v')\
                   .unit('kg','mass')   \
                   .unit('rad',1)

    # Define quantity (not implemented at present)
    # Is this actually an Expression rather than a Value?
    # problem.quantity = [Value('tanAng','tan(theta)')]

    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False)
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=4)
    #problem.guess.setup('auto',start=state,costate_guess=costate,time_integrate=time)
    problem.guess.setup('auto',start=[6378050,0,0,10,-80*pi/180,0])
    #costate_guess = [.8*1000,-.2*1000,-1.0*1000,-0.09*1000,0.005*1000,-0.05*1000]
    #problem.guess.setup('auto',start=[40000,-45*pi/180,0,2200,-80*pi/180,-90*pi/180],costate_guess=costate_guess,time_integrate=1)

    problem.steps.add_step().num_cases(20)           \
                            .terminal('r',6378000)

    problem.steps.add_step().num_cases(2)           \
                            .terminal('r',6378000)  \
                            .terminal('lam',-2.122494903350304)

    return problem

if __name__ == '__main__':
    # Starting MATLAB's engine
    mat = matlab.engine.start_matlab()

    # Initial Conditions for the NN
    r0 = 6420000
    v0 = 2315
    y0 = -0.0908
    ltf = 0.6587

    # Put the IC's into MATLAB's format
    inz = matlab.double([r0,v0,y0,ltf])

    # Call the NN in MATLAB
    N = mat.neuralfunclarge(mat.transpose(inz))

    # Retrieve and convert the MATLAB NN output
    outz = mat.double(N)
    np_array = np.array(outz._data.tolist())
    np_array = np_array.reshape(outz.size).transpose()
    np_array = np_array[0]

    # Order output into variables that make meaningful sense
    t0 = np_array[0]
    ph0 = np_array[1]
    ch0 = np_array[2]
    lr0 = np_array[3]
    #lr0 = np_array[3]*1.558117793705204e-07
    lt0 = np_array[4]
    lph0 = np_array[5]
    lv0 = np_array[6]
    #lv0 = np_array[6]*4.842615012106537e-04
    ly0 = np_array[7]
    lch0 = np_array[8]
    rf = np_array[9]
    tf = np_array[10]
    phf = np_array[11]
    vf = np_array[12]
    yf = np_array[13]
    chf = np_array[14]
    lrf = np_array[15]
    #lrf = np_array[15]*1.558117793705204e-07
    lphf = np_array[16]
    lvf = np_array[17]
    #lvf = np_array[17]*4.842615012106537e-04
    lyf = np_array[18]
    lchf = np_array[19]
    timef = np_array[20]

    r0 = 6420000
    t0 = -0.000002122494903*1e6
    ph0 = 0.000000580321976*1e6
    v0 = 2315
    y0 = -0.000000090792028*1e6
    ch0 = -0.000001570796327*1e6
    lr0 = 0.000000000000509
    lt0 = -0.000000735910258*1e6
    lph0 = -0.000001265248753*1e6
    lv0 = -0.000000000046979*1e6
    ly0 = 0.000000015947252*1e6
    lch0 = -0.000000063859246*1e6
    lrf = -0.000000000000646*1e6
    ltf = -0.000000735910258*1e6

    state = [r0,t0,ph0,v0,y0,ch0]
    costate = [lr0,lt0,lph0,lv0,ly0,lch0]
    param = [lr0,lt0,lph0,lv0,ly0,lch0,lrf,ltf]
    time = timef
    time = 0.1

    problem = get_problem(state=state,costate=costate,param=param,time=time)
    # Default solver is a forward-difference Single Shooting solver with 1e-4 tolerance
    Beluga.run(problem)
