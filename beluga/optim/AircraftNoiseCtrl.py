#Generates a dictionary of possible control solutions for the noise minimization
#problem. The output is meant to be passed directly into ctrl_sol on line 289
#of NecessaryConditions.py.
from sympy import *

def CtrlSols():
    """Passes possible control solutions to NecessaryConditions"""
    lamPSII = symbols('lamPSII')
    lamGAM = symbols('lamGAM')
    gam = symbols('gam')
    v = symbols('v')
    lamV = symbols('lamV')
    banktrig = symbols('banktrig')
    alfatrig = symbols('alfatrig')
    mass = symbols('mass')
    z = symbols('z')
    alfa = symbols('alfa')
    bank = symbols('bank')
    bankmax = symbols('bankmax')
    alfamax = symbols('alfamax')

    #Bank options
    banktrig_options = [-pi/2]
    banktrig_options.append(asin(1/bankmax * atan(lamPSII/(lamGAM*cos(gam)))))
    banktrig_options.append(asin(1/bankmax * (atan(lamPSII/(lamGAM*cos(gam)))+pi)))
    banktrig_options.append(pi/2)

    #AoA options
    alfatrig_options = [-pi/2]
    alfatrig_options.append(asin(1/alfamax * atan(lamPSII*sin(bank)/(v*lamV*cos(gam)) + lamGAM*cos(bank)/(v*lamV))))
    alfatrig_options.append(asin(1/alfamax * (atan(lamPSII*sin(bank)/(v*lamV*cos(gam)) + lamGAM*cos(bank)/(v*lamV))+pi)))
    alfatrig_options.append(pi/2)

    #Thrust options
    Ttrignew_options = [-pi/2]
    Ttrignew_options.append(asin((((v*(z+50)**2.5/(97.396*cos(gam))) * (-lamV*cos(alfa)/mass - lamPSII*sin(alfa)*sin(bank)/(mass*v*cos(gam)) - lamGAM*sin(alfa)*cos(bank)/(mass*v)))**(1/4.2) - 1860)/1560))
    Ttrignew_options.append(pi/2)

    #Create the control options
    ctrl_sol = []
    for i,bankctrl in enumerate(banktrig_options):
        for j,alfactrl in enumerate(alfatrig_options):
            for Tctrl in Ttrignew_options:
                Ttrignew = Tctrl.subs([(bank,bankmax*sin(bankctrl)),(alfa,alfamax*sin(alfatrig))])
                ctrl_sol.append({'banktrig':bankctrl, 'alfatrig':alfactrl.subs(bank,bankmax*sin(bankctrl)), 'Ttrignew':Ttrignew})

    return ctrl_sol
