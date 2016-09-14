#==================================================================================
# PROGRAM: "Hannibal.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: Preliminary test of a track path optimization using a user-defined
#              terrain elevation profile.
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
##from PIL import Image
##from scipy import interpolate
##import scipy.ndimage as ndimage

#Import terrain map and create the terrain function
##img=Image.open('terrain_test2.jpg')
##img=np.array(img) #Convert to array
#img=ndimage.gaussian_filter(img,sigma=10,order=0) #Smooth image
##img=np.asfarray(img)/255.0 #Scale to unity scale
##Ycoords=np.linspace(0,10,len(img[:,0]))
##Xcoords=Ycoords[0:len(img[0,:])]
##xx,yy=np.meshgrid(Xcoords,Ycoords)
##terr_query=interpolate.interp2d(Xcoords,Ycoords,img,kind='linear')
#tck=interpolate.bisplrep(xx,yy,img)
#print(tck)

def terrain(x,y): #Functions must be defined outside of the get_problem()
#    terr=terr_query(x,y)#interpolate.bisplev(x,y,tck)
    terr=(-0.3*np.exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*np.exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*np.exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+1.6*(np.cos(0.8*y))**2*(np.sin(0.796*x))**2)
    return terr

#print(terrain(4.9,0.4))
#print(np.imag(terrain(4.9+1e-30*1j,0.4))/1e-30)
#quit()

def get_problem():
    
    """A simple test of optimal surface track planning."""
    
    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('Hannibal_wfunctions')
    problem.mode='analytical' #Other options: 'numerical', 'dae'
    
    #Define independent variables
    problem.independent('t', 's')
    
    #~~~~~!!!
    #problem.quantity('terrain','(-0.3*exp(-0.5*((x-2.7)^2+1.5*(y-2.1)^2))+2.6*exp(-0.55*(0.87*(x-6.7)^2+(y-2.2)^2))+2.1*exp(-0.27*(0.2*(x-5.5)^2+(y-7.2)^2))+1.6*(cos(0.8*y))^2*(sin(0.796*x))^2)')
    
    # Define equations of motion
    problem.state('x','V*cos(hdg)','m')   \
           .state('y','V*sin(hdg)','m')  \
           
    # Define controls
    problem.control('hdg','rad')

    # Define Cost Functional
    problem.cost['path'] =  Expression('(1-w)+w*V*conv*elev*terrain(x,y)', 's')
    
    #Define constraints
    problem.constraints().initial('x-x_0','m') \
                         .initial('y-y_0','m') \
                         .terminal('x-x_f','m') \
                         .terminal('y-y_f','m')
    
    #Define constants
    problem.constant('w',0.0,'1') #Initial Terrain weighting factor
    problem.constant('conv',1,'s/m^2') #Integral conversion factor
    problem.constant('V',1,'m/s') #Vehicle speed
    problem.constant('elev',1,'m') #Initial Elevation
    
    #Unit scaling
    problem.scale.unit('m',1) \
                 .unit('s',1) \
                 .unit('rad',1)
    
    #Configure solver
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=4)
    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False)

    #Initial Guess
    problem.guess.setup('auto',start=[1.0,3], costate_guess=[0.1,-0.1]) #City A
     
    #Add Continuation Steps   
    problem.steps.add_step().num_cases(30) \
                            .terminal('x', 8.0) \
                            .terminal('y', 4.5) \

    problem.steps.add_step().num_cases(30) \
                            .const('w',0.6) #Final Terrain weighting factor

    
    return problem
    
    
if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
                            