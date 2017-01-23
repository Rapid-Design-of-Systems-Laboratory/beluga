import dill
from math import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy import interpolate
import scipy.ndimage as ndimage

#Load image
img=Image.open('terrain_test2.jpg')
img=np.array(img)
img=img/1.0 #Convert to float

#Create Interpolation
Ycoords=np.linspace(0,10,len(img[:,0]))
Xcoords=Ycoords[0:len(img[0,:])]
terr_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,img)
def terrain1(x,y): #Functions must be defined outside of the get_problem()
    if np.iscomplex(x)==True:
        xderiv=(terr_spl.ev(np.real(x)+5e-5,y)-terr_spl.ev(np.real(x)-5e-5,y))/1e-4
        return xderiv*1j*1e-30
    elif np.iscomplex(y)==True:
        yderiv=(terr_spl.ev(x,np.real(y)+5e-5)-terr_spl.ev(x,np.real(y)+5e-5))/1e-4
        return yderiv*1j*1e-30
    else:
        return terr_spl.ev(x,y)

#Define analytic terrain function
def terrain2(x,y):
    terr=(-0.3*np.exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*np.exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*np.exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+1.6*(np.cos(0.8*y))**2*(np.sin(0.796*x))**2)*0.21509729918970577/0.772319886055
    return terr

#Interpolated terrain function with smoothing
imgs=ndimage.gaussian_filter(img,sigma=10,order=0) #Smooth image
terr_spl2=interpolate.RectBivariateSpline(Xcoords,Ycoords,imgs)
def terrain3(x,y): #Functions must be defined outside of the get_problem()
    if np.iscomplex(x)==True:
        xderiv=(terr_spl2.ev(np.real(x)+5e-5,y)-terr_spl2.ev(np.real(x)-5e-5,y))/1e-4
        return xderiv*1j*1e-30
    elif np.iscomplex(y)==True:
        yderiv=(terr_spl2.ev(x,np.real(y)+5e-5)-terr_spl2.ev(x,np.real(y)+5e-5))/1e-4
        return yderiv*1j*1e-30
    else:
        return terr_spl2.ev(x,y)

#Generate data
img2=img*0.0
img3=img*0.0
img4=img*0.0
for i in range(0,len(img[0,:])):
    for j in range(0,len(img[:,0])):
        img2[i,j]=terrain2(Xcoords[i],Ycoords[j]) 
        img3[i,j]=terrain1(Xcoords[i],Ycoords[j])
        img4[i,j]=terrain3(Xcoords[i],Ycoords[j])

#Plot contour plot of raw data
plt.figure(1)
Ycoords=np.linspace(0,10,len(img[:,0]))
Xcoords=Ycoords[0:len(img[0,:])]
plt.axis([0,10,0,10])
plt.title('Raw Terrain Data')
plt.contour(Ycoords,Xcoords,img)

#PLot contour plot of analytic data
plt.figure(2)
plt.axis([0,10,0,10])
plt.title('Analytic Terrain Data')
plt.contour(Ycoords,Xcoords,img2)

#Plot contour plot of interpolated terrain data
plt.figure(3)
plt.axis([0,10,0,10])
plt.title('Interpolated Terrain Data')
plt.contour(Ycoords,Xcoords,img3)

#Plot smoothed image
plt.figure(4)
plt.axis([0,10,0,10])
plt.title('Smoothed Terrain Data')
plt.contour(Ycoords,Xcoords,imgs)

#Plot contour plot of interpolated and smoothed terrain data
plt.figure(5)
plt.axis([0,10,0,10])
plt.title('Smoothed and Interpolated Terrain Data')
plt.contour(Ycoords,Xcoords,img4)

plt.show()
        
