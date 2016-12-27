#==================================================================================
# PROGRAM: "Hannibal_HPAdemo.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: Preliminary test of a track path optimization using graph search
#              continuation.
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
from PIL import Image
from scipy import interpolate
import scipy.ndimage as ndimage

#Import terrain map and create the terrain function
img=Image.open('terrain_test2.jpg')
img=np.array(img) #Convert to array
img=np.asfarray(img)/255.0 #Scale to unity scale (and convert to float - important)
img=ndimage.gaussian_filter(img,sigma=5,order=0) #Smooth image
Xcoords=np.linspace(0,10,len(img[:,0])) #North Coordinates
Ycoords=Xcoords[0:len(img[0,:])] #East Coordinates
terr_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,img,kx=3,ky=3,s=10)
#xx,yy=np.meshgrid(Xcoords,Ycoords)
#terr_query=interpolate.interp2d(Xcoords,Ycoords,img,kind='linear')
#tck=interpolate.bisplrep(xx,yy,img)
#print(tck)

def terrain(x,y): #Functions must be defined outside of the get_problem()
    if np.iscomplex(x)==True:
        #xderiv=(terr_spl.ev(np.real(x)+25e-2,y)-terr_spl.ev(np.real(x)-25e-2,y))/5e-1
        xderiv=terr_spl.ev(np.real(x),y,dx=1)
        return xderiv*1j*1e-30
    elif np.iscomplex(y)==True:
        #yderiv=(terr_spl.ev(x,np.real(y)+25e-2)-terr_spl.ev(x,np.real(y)-25e-2))/5e-1
        yderiv=terr_spl.ev(x,np.real(y),dy=1)
        return yderiv*1j*1e-30
    else:
        return terr_spl.ev(x,y)
    #terr=(-0.3*np.exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*np.exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*np.exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+1.6*(np.cos(0.8*y))**2*(np.sin(0.796*x))**2)

def terrain1(x,y):
    terr=(-0.3*np.exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*np.exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*np.exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+ \
    1.6*(np.cos(0.8*y))**2*(np.sin(0.796*x))**2)*0.21509729918970577/0.772319886055
    return terr


#print(terrain1(4.0,4.0))
#print(terrain2(4.0,4.0))
#print(np.imag(terrain1(4.0+(1e-30)*1j,4.0))/1e-30)
#print(np.imag(terrain2(4.0+(1e-30)*1j,4.0))/1e-30)

#quit()

def get_problem():

    """A simple test of optimal surface track planning."""

    # Rename this and/or move to optim package?
    problem = beluga.optim.Problem('Hannibal_HPAdemo')
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
    problem.constant('w',0.9,'1') #Initial Terrain weighting factor
    problem.constant('conv',1,'s/m^2') #Integral conversion factor
    problem.constant('V',1,'m/s') #Vehicle speed
    problem.constant('elev',1,'m') #Initial Elevation

    #Unit scaling
    problem.scale.unit('m',1) \
                 .unit('s',1) \
                 .unit('rad',1)

    #Configure solver
    #problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached = False, number_arcs=8)
    problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=15, verbose = True, cached = False)

    #Initial Guess (Classic test example [4.9,0.4])
    problem.guess.setup('auto',start=[8.0,0.5], costate_guess=[0.0,-0.1]) #City A
    #problem.guess.setup('auto',start=[4.9,0.4], costate_guess=[0.1,-0.1]) #City A

    #Add Continuation Steps (Classic test example [7.2,8.5]) [8, 4.5]
    problem.steps.add_step(strategy='HPA') \
                            .terminal('x', 3.0, 10) \
                            .terminal('y', 9.5, 10) \

    #problem.steps.add_step(strategy='manual').num_cases(10) \
    #                        .terminal('x', 3.0) \
    #                        .terminal('y', 9.5) \

    #problem.steps.add_step().num_cases(30) \
    #                        .const('w',0.99) #Final Terrain weighting factor


    return problem


if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)
