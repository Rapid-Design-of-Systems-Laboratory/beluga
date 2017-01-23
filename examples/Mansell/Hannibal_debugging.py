#==================================================================================
# Tests spline derivatives
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
import time
import random
import matplotlib.pyplot as plt

#Import terrain map and create the terrain function
img=Image.open('terrain_test2.jpg')
img=np.array(img) #Convert to array
img=ndimage.gaussian_filter(img,sigma=10,order=0) #Smooth image
img=np.asfarray(img)/255.0 #Scale to unity scale
Xcoords=np.linspace(0,10,len(img[:,0])) #North Coordinates
Ycoords=Xcoords[0:len(img[0,:])] #East Coordinates

terr_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,img,kx=3,ky=3,s=10)
#xx,yy=np.meshgrid(Xcoords,Ycoords)
#terr_query=interpolate.interp2d(Xcoords,Ycoords,img,kind='linear')
#tck=interpolate.bisplrep(xx,yy,img)
#print(tck)

def terrain1(x,y): #Functions must be defined outside of the get_problem()
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

#def terrain1(x,y): #Functions must be defined outside of the get_problem()
#    return (terr_spl.ev(x+1e-4,y)-terr_spl.ev(x,y))/1e-4 #Just do the derivative
    #if np.iscomplex(x)==True:
    #    return terr_spl.ev(np.real(x),y,dx=1)#*1j*1e-30
    #elif np.iscomplex(y)==True:
    #    return terr_spl.ev(x,np.real(y),dy=1)*1j*1e-30
    #else:
    #    return terr_spl.ev(x,y,dx=1)


def terrain2(x,y):
    terr=(-0.3*np.exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*np.exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*np.exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+ \
    1.6*(np.cos(0.8*y))**2*(np.sin(0.796*x))**2)*0.21509729918970577/0.772319886055
    return terr

levelset = 6.5
npoints = 1000

xr=np.linspace(levelset,levelset,npoints)
yr=np.linspace(0,10,npoints)

pe_list = []
terr1_list = []
terr2_list = []
terr1dx_list = []
terr1dy_list = []
terr2dx_list = []
terr2dy_list = []
for i in range(0,npoints):
    #print('(x,y) = ',xr[i],yr[i])
    terr1_list.append(terrain1(xr[i],yr[i]))
    terr2_list.append(terrain2(xr[i],yr[i]))
    terr1dx = np.imag(terrain1(xr[i]+(1e-30)*1j,yr[i])/1e-30)
    terr1dy = np.imag(terrain1(xr[i],yr[i]+(1e-30)*1j)/1e-30)
    #print('Terrain 1:',terr1)
    terr2dx = np.imag(terrain2(xr[i]+(1e-30)*1j,yr[i])/1e-30)
    terr2dy = np.imag(terrain2(xr[i],yr[i]+(1e-30)*1j)/1e-30)
    #print('Terrain 2:',terr2)
    #pe = abs((terr1 - terr2)/terr2 * 100.0)
    terr1dx_list.append(terr1dx)
    terr1dy_list.append(terr1dy)
    terr2dx_list.append(terr2dx)
    terr2dy_list.append(terr2dy)
    #pe_list.append(pe)
    #print('Percent Error:', pe)
    #print('Percent Error:', pe)
    #if abs(pe) > 10:
    #    print('Uh oh!')
    #    print('(x,y) = ',xr[i],yr[i])
    #    print('Terrain 1:',terr1)
    #    print('Terrain 2:',terr2)
    #    print('Percent Error:', pe)

#print('Average Percent Error:', np.mean(pe_list))
print('Running a time trial...')
random.seed()
xra=[]
yra=[]
for i in range(0,10000):
    xra.append(random.random()*Xcoords[-1])
    yra.append(random.random()*Ycoords[-1])


time1=time.clock()
for i in range(0,10000):
    test=np.imag(terrain1(xra[i]+(1e-30)*1j,yra[i])/1e-30)
time1=time.clock()-time1
print(time1)

time2=time.clock()
for i in range(0,10000):
    test=np.imag(terrain2(xra[i]+(1e-30)*1j,yra[i])/1e-30)
time2=time.clock()-time2
print(time2)

#print(terrain1(4.9,0.4))
#print(np.imag(terrain2(4.9+(1e-30)*1j,0.4))/1e-30)
#print(terrain1(4.9,0.4))
#print(terrain2(4.9,0.4))
#terr1 = np.imag(terrain1(4.9+(1e-30)*1j,0.4))/1e-30
#terr2 = np.imag(terrain2(4.9+(1e-30)*1j,0.4))/1e-30
#print(terr1)
#print(terr2)
#print((terr1 - terr2)/terr2 * 100.0)
plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,img)
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.title('Simulated Terrain with Smoothing')
plt.plot([0,10],[levelset,levelset],'r--')
plt.savefig('Plt1.pdf')
plt.figure(2)
plt.plot(yr,terr1_list,'r')
plt.plot(yr,terr2_list,'b')
plt.xlabel('East (km)')
plt.ylabel('Elevation')
plt.savefig('Plt2.pdf')
plt.figure(3)
plt.plot(yr,terr1dx_list,'r')
plt.plot(yr,terr2dx_list,'b')
plt.xlabel('East (km)')
plt.ylabel('Tx')
plt.savefig('Plt3.pdf')
plt.figure(4)
plt.plot(yr,terr1dy_list,'r')
plt.plot(yr,terr2dy_list,'b')
plt.xlabel('East (km)')
plt.ylabel('Ty')
plt.savefig('Plt4.pdf')
plt.show()
