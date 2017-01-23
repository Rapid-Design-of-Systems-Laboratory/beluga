#==============================================================================#
# Tests the loading AND smoothing AND coordinate conversion of Geotiff elevation
# data. Download Geotiff elevation from:
# http://www.cgiar-csi.org/data/srtm-90m-digital-elevation-database-v4-1
#==============================================================================#
import gdal
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from math import *
import scipy.ndimage as ndimage

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
elevation = ndimage.gaussian_filter(elevation,sigma=20,order=0) #Smooth terrain
geo_spl=interpolate.RectBivariateSpline(lats,lons,elevation,kx=3,ky=3,s=10)
print(lats[0])
print(lons[0])
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

#Generate lists of X,Y coordinates
Xcoords = np.linspace(0,(lats[-1]-lats[0])*111,floor(len(lats)/2)) #[km]
Ycoords = np.linspace(0,(lons[-1]-lons[0])*111*np.sin(lats[-1]*np.pi/180.0),floor(len(lons)/2)) #[km]

#Plot
Y,X = np.meshgrid(Ycoords, Xcoords)
terrData=terrain(X,Y) #Create the elevation data based on the spline fit
plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,terrData)
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.show()


#NOTE: v is too computationally intensive. Suggest conversion inside terrain function
#Make a new elevation array in X and Y coordinates
#terr_arr = np.zeros((len(Xcoords),len(Ycoords)))
#for i,x in enumerate(Xcoords):
#    print(i,'out of',len(Xcoords))
#    for j,y in enumerate(Ycoords):
#        terr_arr[i,j] = geo_spl.ev(x/111+lats[0],y/(111*np.sin(lats[-1]*np.pi/180.0))+lons[0])

#Spline fit x/y image with smoothing
#terr_spl = interpolate.RectBivariateSpline(Xcoords,Ycoords,terr_arr,kx=3,ky=3,s=10)

#Plot
#Y,X = np.meshgrid(Ycoords, Xcoords)
#terrData=terr_spl.ev(X,Y) #Create the elevation data based on the spline fit
#plt.figure(1)
#plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
#plt.contour(Ycoords,Xcoords,terrData)
#plt.xlabel('East (km)')
#plt.ylabel('North (km)')
#plt.show()
