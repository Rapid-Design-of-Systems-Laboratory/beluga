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
img=Image.open('terrain_test2.jpg')
img=np.array(img)
img=np.asfarray(img)/255.0 #Scale to unity scale (and convert to float - important)
img=ndimage.gaussian_filter(img,sigma=5,order=0) #Smooth image
Xcoords=np.linspace(0,10,len(img[:,0])) #North Coordinates
Ycoords=Xcoords[0:len(img[0,:])] #East Coordinates
terr_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,img,kx=3,ky=3,s=10)

#Load data
f = open('data.dill','rb')
out=dill.load(f)
f.close()
solution_set = out['solution'][-1]
guess_set = out['guesses'][-1]
xsol=out['solution'][-1][-1].y[0,:]
ysol=out['solution'][-1][-1].y[1,:]
lamXsol=out['solution'][-1][-1].y[2,:]
lamYsol=out['solution'][-1][-1].y[3,:]
tf=out['solution'][-1][-1].y[4,0]
tsol=out['solution'][-1][-1].x*tf

#Plot contour plot
Xcoords=np.linspace(0,10,len(img[:,0]))
Ycoords=Xcoords[0:len(img[0,:])]
Y,X = np.meshgrid(Ycoords, Xcoords)
terrData=terr_spl.ev(X,Y) #Create the elevation data based on the spline fit
plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,terrData)
plt.xlabel('East (km)')
plt.ylabel('North (km)')

#Plot continuation steps
ax = plt.axes()
for ind,sol in enumerate(solution_set[:-1]):
    if sol.converged:
        ypt = sol.y[1,-1]
        xpt = sol.y[0,-1]
        plt.plot(sol.y[1,:],sol.y[0,:],'r--')
        plt.scatter(sol.y[1,-1],sol.y[0,-1],marker='o',edgecolors='r',facecolors='None')
    elif not sol.converged:
        ypt = sol.aux['terminal']['y']
        xpt = sol.aux['terminal']['x']
        plt.scatter(sol.aux['terminal']['y'],sol.aux['terminal']['x'],\
        marker='o',edgecolors='k',facecolors='None')
        plt.scatter(sol.aux['terminal']['y'],sol.aux['terminal']['x'],50,\
        marker='x',color='r')

    #Draw arrow
    dx = xpt-guess_set[ind].y[0,-1]
    dy = ypt-guess_set[ind].y[1,-1]
    ax.arrow(guess_set[ind].y[1,-1],guess_set[ind].y[0,-1],dy,dx)

#Plot final solution
plt.plot(ysol,xsol,'r')
dx = xsol[-1]-guess_set[ind+1].y[0,-1]
dy = ysol[-1]-guess_set[ind+1].y[1,-1]
ax.arrow(guess_set[ind+1].y[1,-1],guess_set[ind+1].y[0,-1],dy,dx)
plt.scatter([ysol[0],ysol[-1]],[xsol[0],xsol[-1]],75,'r')


#Plot control
hdg = []
{hdg.append(np.arctan2(-lamYsol[i],-lamXsol[i])*180/np.pi) for i in range(0,len(lamXsol))}

plt.figure(2)
plt.xlabel('Time (s)')
plt.ylabel('Heading (deg)')
plt.plot(tsol,hdg)

#Plot surface
zsol=[]
for i in range(0,len(xsol)):
        zsol.append(terr_spl.ev(xsol[i],ysol[i]))
s_plot=plt.figure(3)
ax = s_plot.gca(projection='3d')
ax.plot_surface(Y, X, terrData,cmap=cm.terrain)
ax.plot(ysol,xsol,zsol,'r')
plt.show()
#Plot Track Path
#plt.figure(2)
#plt.plot(xsol,ysol,'r')
#plt.show()
