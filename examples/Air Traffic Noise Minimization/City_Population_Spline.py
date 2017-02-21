#==============================================================================#
# PROGRAM: City_Population_Spline.py
# Author: Justin Mansell (2016)
# Description: Create a 2D spline interpolation fit for sample population data.
#==============================================================================#
import numpy as np
from scipy import interpolate
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Load sample data
f = open('SampleCityData.txt', 'r')
pop_array = [[float(sector) for sector in line.split()] for line in f]
pop_array = np.array(pop_array)
f.close()

#Define the coordinates and population sample bins
sector_dx = 1.0 #Length of each sector along x direction [km]
sector_dy = 1.0 #Length of each sector along y direction [km]
den_array = pop_array / (sector_dx * sector_dy) #Convert to population density
Xcoords = np.linspace(0,1,len(den_array[:,0]))*len(den_array[:,0])*sector_dx+0.5*sector_dx
Ycoords = np.linspace(0,1,len(den_array[0,:]))*len(den_array[0,:])*sector_dy+0.5*sector_dy
den_array = den_array[::-1] #Flip data vertically so origin is at bottom left
#NOTE: the origin is located at the lower left corner of the data

#Perform the spline fit
#den_array=ndimage.gaussian_filter(den_array,sigma=0.5,order=0) #Smooth data (optional)
pop_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,den_array)
#Can now evaluate population density at any X,Y coordinate using pop_spl.ev(X,Y)

#Plot the population data
Xfine = np.linspace(Xcoords[0],Xcoords[-1],100)
Yfine = np.linspace(Ycoords[0],Ycoords[-1],100)
Yfine, Xfine = np.meshgrid(Xfine, Yfine)
spline_data = pop_spl.ev(Xfine,Yfine)

#Contour plot
plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
cplot = plt.contour(Yfine,Xfine,spline_data)
plt.title('City Population Density (People/sq.km)')
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.clabel(cplot, fmt = '%1.0f')
plt.savefig('ContourPlot.pdf')

#Surface plot
s_plot = plt.figure(2)
ax = s_plot.gca(projection='3d')
ax.plot_surface(Yfine, Xfine, spline_data, cmap = cm.coolwarm)
ax.set_zlabel('People/sq.km')
plt.title('City Population')
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.savefig('SurfacePlot.pdf')
plt.show()
