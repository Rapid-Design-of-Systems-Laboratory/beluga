#==================================================================================
# PROGRAM: "surftest_noinc.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: Preliminary test of a track path optimization using a user-defined
#              terrain elevation profile as well as user-defined bridge and tunnel
#              cost functions.
#==================================================================================

#Import Necessary Modules
import numpy as np
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *
import functools

def get_problem():

    #User Defined Terrain Elevation
    #def terr( x_pos, y_pos ):
        #Defines terrain elevation [m] as a function of x and y positions [m]
    #    elev=100.0*(np.sin(0.5*(x_pos/1000.0)))**2.0 #User defined elevation map
    #    return elev

    #User Defined Tunnel Cost
    #def tunnel(depth):
        #Defines additional cost for placing a 1 meter length of track a non-zero
        #depth below the ground.
    #    TunnelCost=(50e3)/(1+np.exp(-(depth-5))) #Tunneling Cost (2016 USD)
    #    return TunnelCost

    #def bridge(height):
        #Defines additional cost for placing a 1 meter length of track a non-zero
        #heigh above the ground.
    #    BridgeCost=10e3*(height/10)**2 #Bridge Cost (2016 USD)
    #    return BridgeCost

    """A simple test of optimal surface track planning."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('surftest_noinc')

    #Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x','V*cos(hdg)','m')   \
           .state('y','V*sin(hdg)','m')  \
           .state('V','amax*sin(thrA) + eps*(cos(thrA)+cos(hdgA))','m/s') \
           .state('hdg','cmax/V*sin(hdgA)','rad')

    # Define controls
    #problem.control('thrA','rad') \
    #       .control('hdgA','rad')
    problem.control('hdgA','rad')

    # Define Cost Functional
    problem.cost['path'] = Expression('1','s')

    #problem.cost['path'] =  Expression('TimeToUSD+trk*V', 'USD')

    #+ \
    #'(50e3)/(1.0+exp(-1.0*(z-0.0*(sin(0.5*(x/1000.0)))**2.0-5.0)))+'+ \
    #'10e3*((0.0*(sin(0.5*(x/1000.0)))**2.0-z)/10.0)**2.0','USD')

    #Define constraints
    problem.constraints().initial('x-x_0','m') \
                         .initial('y-y_0','m') \
                         .initial('V-V_0','m/s') \
                         .initial('hdg-hdg_0','rad') \
                         .terminal('x-x_f','m') \
                         .terminal('y-y_f','m')
                         #.terminal('V-V_f','m/s')
                         #.initial('hdg-hdg_0','rad') \

    #Define constants
    problem.constant('g',9.81,'m/s^2') #Acceleration due to gravity
    problem.constant('trk',1,'USD/m') #Basic cost of 1 m of track on ground (10k per m)
    problem.constant('amax',1.0,'m/s^2') #Maximum thrust acceleration of vehicle
    problem.constant('cmax',1.0,'m/s^2') #Maximum allowed centripetal acceleration
    problem.constant('eps',10,'m/s^2') #Error constant
    problem.constant('TimeToUSD',1,'USD/s') #Time is Money!!
    problem.constant('thrA',0,'rad')

    #Unit scaling
    problem.scale.unit('m','x') \
                 .unit('s','x/V') \
                 .unit('rad',1) \
                 .unit('USD',1)

    #Configure solver
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=2)

    #Initial Guess
    problem.guess.setup('auto',start=[0.0,0.0,1.0,pi/4-0.2], costate_guess=-0.1) #City A

    #Add Continuation Steps
    problem.steps.add_step().num_cases(10) \
                            .terminal('x', 10) \
                            .terminal('y', 0)

    problem.steps.add_step().num_cases(10) \
                            .const('eps', 0.2)

    #problem.steps.add_step().num_cases(10) \
    #                        .terminal('y', 2*pi*1000) \
    #                        .terminal('z', 0.0) \
    #                        .terminal('inc', 0.0)
                                                    #^ City B
    return problem


if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
