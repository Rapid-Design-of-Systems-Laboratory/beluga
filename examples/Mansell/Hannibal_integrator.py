#===============================================================================
# Integrates EOM + costate equations to see how legit the trajectory is
#===============================================================================
import dill
from math import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy import interpolate
from scipy import integrate
import scipy.ndimage as ndimage
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Load image
img=Image.open('terrain_test.jpg')
img=np.array(img)
img=np.asfarray(img)/255.0 #Scale to unity scale (and convert to float - important)
img=ndimage.gaussian_filter(img,sigma=10,order=0) #Smooth image
Xcoords=np.linspace(0,10,len(img[:,0])) #North Coordinates
Ycoords=Xcoords[0:len(img[0,:])] #East Coordinates
terr_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,img,kx=3,ky=3)

#Global parameters
w = 0.99 #Weighting factor
gam = 1.0 #Conversion factor
V = 1.0 #Speed
elev = 100.0 #Elevation

#Terrain function
def terrain(x,y): #Functions must be defined outside of the get_problem()
    if np.iscomplex(x)==True:
        xderiv=(terr_spl.ev(np.real(x)+25e-2,y)-terr_spl.ev(np.real(x)-25e-2,y))/5e-1
        return xderiv*1j*1e-30
    elif np.iscomplex(y)==True:
        yderiv=(terr_spl.ev(x,np.real(y)+25e-2)-terr_spl.ev(x,np.real(y)-25e-2))/5e-1
        return yderiv*1j*1e-30
    else:
        return terr_spl.ev(x,y)

def terrainA(x,y):
    terr=(-0.3*np.exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*np.exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*np.exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+ \
    1.6*(np.cos(0.8*y))**2*(np.sin(0.796*x))**2)*0.21509729918970577/0.772319886055
    return terr

#Equations of motion (calculated manually)
def EOM(x_vect,t):
    global w, gam, V, elev
    hdg = np.arctan2(-x_vect[3],-x_vect[2])
    xdot = V*np.cos(hdg)
    ydot = V*np.sin(hdg)
    lam1dot = -w*gam*elev*np.imag(terrain(x_vect[0]+(1e-30)*1j,x_vect[1])/1e-30)
    lam2dot = -w*gam*elev*np.imag(terrain(x_vect[0],x_vect[1]+(1e-30)*1j)/1e-30)
    return np.array([xdot, ydot, lam1dot, lam2dot])

#Load data
f = open('data.dill','rb')
out=dill.load(f)
f.close()
xsol=out['solution'][-1][-1].y[0,:]
ysol=out['solution'][-1][-1].y[1,:]
lamX=out['solution'][-1][-1].y[2,:]
lamY=out['solution'][-1][-1].y[3,:]
tf = out['solution'][-1][-1].y[4,0]
tsol=(out['solution'][-1][-1].x)*tf

#Integrate!
x0 = np.array([xsol[0], ysol[0], lamX[0], lamY[0]])
sol=integrate.odeint(EOM,x0,tsol)
#print(sol)
xint = sol[:,0]
yint = sol[:,1]

#Plot contour plot
Xcoords=np.linspace(0,10,len(img[:,0]))
Ycoords=Xcoords[0:len(img[0,:])]
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,img)
plt.plot(ysol,xsol,'b')
plt.plot(yint,xint,'r')
plt.scatter([ysol[0],ysol[-1]],[xsol[0],xsol[-1]],75,'r')
plt.show()
