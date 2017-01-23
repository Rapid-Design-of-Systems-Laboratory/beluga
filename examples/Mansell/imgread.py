import numpy as np

import beluga.Beluga as Beluga
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import beluga.optim.Problem
from beluga.optim.problem import *
from beluga.continuation import *
from math import *
from PIL import Image

#IMG Reading
from osgeo import gdal

#Image processing kit
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# This script will read a .img file and return the pixel values as an array.

#Load Image
im=Image.open('imgn45w114_13_thumb.jpg','r')
pix=im.load()

#Formulate Elevation Map
dim=im.size
X = np.mgrid[1:dim[0]+1]
Y = np.mgrid[1:dim[1]+1]
XX, YY = np.meshgrid(X,Y) #Create pixel meshgrid
ZZ = np.empty([dim[1],dim[0]]) #Create elevation grid
for ii in range(dim[0]):
    for jj in range(dim[1]):
        ZZ[jj,ii]=pix[ii,jj]

#Plot Image
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX,YY,ZZ, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()