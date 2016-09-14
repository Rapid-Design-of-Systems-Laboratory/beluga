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


#Load data
f = open('data.dill','rb')
out=dill.load(f)
f.close()
xsol=out['solution'][-1][-1].y[0,:]
ysol=out['solution'][-1][-1].y[1,:]

#Plot contour plot
Ycoords=np.linspace(0,10,len(img[:,0]))
Xcoords=Ycoords[0:len(img[0,:])]
plt.figure(1)
plt.scatter([0.4,8.5],[4.9,7.2],75,'r')
plt.axis([0,10,0,10])
plt.plot(ysol,xsol,'r')
plt.contour(Ycoords,Xcoords,img)
plt.show()

#Plot Track Path
#plt.figure(2)
#plt.plot(xsol,ysol,'r')
#plt.show()


