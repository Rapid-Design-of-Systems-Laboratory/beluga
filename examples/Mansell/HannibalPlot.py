import dill
from math import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy import interpolate
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

#Load data
f = open('data.dill','rb')
out=dill.load(f)
f.close()
xsol=out['solution'][-1][-1].y[0,:]
ysol=out['solution'][-1][-1].y[1,:]

#Plot contour plot
Xcoords=np.linspace(0,10,len(img[:,0]))
Ycoords=Xcoords[0:len(img[0,:])]
plt.figure(1)
#plt.axis([0,10,0,10])
plt.contour(Ycoords,Xcoords,img)
plt.plot(ysol,xsol,'r')
plt.scatter([ysol[0],ysol[-1]],[xsol[0],xsol[-1]],75,'r')

#Plot surface 
zsol=[]
for i in range(0,len(xsol)):
        zsol.append(terr_spl.ev(xsol[i],ysol[i]))
s_plot=plt.figure(2)
ax = s_plot.gca(projection='3d')
Y,X = np.meshgrid(Ycoords, Xcoords)
ax.plot_surface(Y, X, img,cmap=cm.terrain)
ax.plot(ysol,xsol,zsol,'r')
plt.show()
#Plot Track Path
#plt.figure(2)
#plt.plot(xsol,ysol,'r')
#plt.show()


