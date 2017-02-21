#===============================================================================
# Plots optimal route through Geotiff terrain
#===============================================================================
import gdal
import dill
from math import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy import interpolate
import scipy.ndimage as ndimage
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Load trajectory data
f = open('data.dill','rb')
out=dill.load(f)
f.close()
xsol=out['solution'][-1][-1].y[0,:]
ysol=out['solution'][-1][-1].y[1,:]
lamXsol=out['solution'][-1][-1].y[2,:]
lamYsol=out['solution'][-1][-1].y[3,:]
tf=out['solution'][-1][-1].y[4,-1]
tsol=out['solution'][-1][-1].x*tf

#Load Geotiff data
ds = gdal.Open('WL2.tif')
band = ds.GetRasterBand(1)
elevation = band.ReadAsArray()
elevation = np.flipud(elevation)
nrows, ncols = elevation.shape

#Compute lat/lon extent of image
lon0, dlon, dlondlat, lat0, dlatdlon, dlat = ds.GetGeoTransform()
#NOTE: lat0,lon0 coordinates of the upper right corner
lats = np.linspace(lat0+dlat*nrows,lat0,nrows)
lons = np.linspace(lon0,lon0+dlon*ncols,ncols)
elevation = elevation.astype(np.float) #Convert to a floating point array (important for smoothing)

#Spline fit lat/lon image
print('Generating terrain function...')
elevation = ndimage.gaussian_filter(elevation,sigma=20,order=0) #Smooth terrain
geo_spl=interpolate.RectBivariateSpline(lats,lons,elevation,kx=3,ky=3,s=10)

def terrain(x,y):
    #Computes the elevation a point (x,y) in km as measured from the lower left
    #corner.
    lat = x/111+lats[0]
    lon = y/(111*np.sin(lat*np.pi/180.0))+lons[0]
    if hasattr(x,'__len__') or hasattr(y,'__len__'):
        return geo_spl.ev(lat,lon)
    elif np.iscomplex(x)==True:
        xderiv=geo_spl.ev(np.real(lat),lon,dx=1) / (111) #[m/km]
        return xderiv*1j*1e-30
    elif np.iscomplex(y)==True:
        yderiv=geo_spl.ev(lat,np.real(lon),dy=1) / (111*np.sin(lat*np.pi/180.0)) #[m/km]
        return yderiv*1j*1e-30
    else:
        return geo_spl.ev(lat,lon) #[m]
print('Terrain function ready')


#Generate lists of X,Y coordinates
Xcoords = np.linspace(0,(lats[-1]-lats[0])*111,floor(len(lats)/2)) #[km]
Ycoords = np.linspace(0,(lons[-1]-lons[0])*111*np.sin(lats[-1]*np.pi/180.0),floor(len(lons)/2)) #[km]

#Plot
Y,X = np.meshgrid(Ycoords, Xcoords)
#X = np.flipud(X)
terrData=terrain(X,Y) #Create the elevation data based on the spline fit
plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,terrData)
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.plot(ysol,xsol,'r') #Plot optimal path
plt.scatter([ysol[0],ysol[-1]],[xsol[0],xsol[-1]],75,'r')


#Plot control
hdg = []
{hdg.append(np.arctan2(-lamYsol[i],-lamXsol[i])*180/np.pi) for i in range(0,len(lamXsol))}

plt.figure(2)
plt.xlabel('Time (s)')
plt.ylabel('Heading (deg)')
plt.plot(-tsol*10,np.array(hdg)+180)
plt.show()

#NOTE: not sure why loading the trajectory data re-runs the terrain function in
#      Track_demo.
#TODO: take heading from the solution vector rather than recomputing it from the costates
