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

#Load Geotiff data
ds = gdal.Open('WL2.tif')
band = ds.GetRasterBand(1)
elevation = band.ReadAsArray()
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

def terrain1(x,y):
    #Computes the elevation a point (x,y) in km as measured from the lower left
    #corner.
    lat = np.real(x)/111+lats[0]
    lon = np.real(y)/(111*np.sin(lat*np.pi/180.0))+lons[0]
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

def terrain2(x,y):
    #Computes the elevation a point (x,y) in km as measured from the lower left
    #corner.
    lat = np.real(x)/111+lats[0]
    lon = np.real(y)/(111*np.sin(lat*np.pi/180.0))+lons[0]
    if hasattr(x,'__len__') or hasattr(y,'__len__'):
        return geo_spl.ev(lat,lon)
    elif np.iscomplex(x)==True:
        xderiv=(geo_spl.ev(lat+0.01,lon)-geo_spl.ev(lat,lon))/((0.01)*111)
        return xderiv*1j*1e-30
    elif np.iscomplex(y)==True:
        yderiv=(geo_spl.ev(lat,lon+0.01)-geo_spl.ev(lat,lon))/((0.01)*(111*np.sin(lat*np.pi/180.0))) #[m/km]
        return yderiv*1j*1e-30
    else:
        return geo_spl.ev(lat,lon) #[m]

print('Terrain function ready')

Xcoords = np.linspace(0,(lats[-1]-lats[0])*111,floor(len(lats)/2)) #[km]
Ycoords = np.linspace(0,(lons[-1]-lons[0])*111*np.sin(lats[-1]*np.pi/180.0),floor(len(lons)/2)) #[km]

levelset = 44
npoints = 1000

xr=np.linspace(0,Xcoords[-1],npoints)
yr=np.linspace(levelset,levelset,npoints)

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

Y,X = np.meshgrid(Ycoords, Xcoords)
X = np.flipud(X)
terrData=terrain1(X,Y) #Create the elevation data based on the spline fit
plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,terrData)
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.title('Real Terrain with Smoothing')
plt.plot([levelset,levelset],[0,Xcoords[-1]],'r--')
#plt.savefig('Plt1.pdf')
plt.figure(2)
plt.plot(xr,terr1_list,'r')
plt.plot(xr,terr2_list,'b')
plt.xlabel('North (km)')
plt.ylabel('Elevation')
#plt.savefig('Plt2.pdf')
plt.figure(3)
plt.plot(xr,terr1dx_list,'r')
plt.plot(xr,terr2dx_list,'b')
plt.xlabel('North (km)')
plt.ylabel('Tx')
#plt.savefig('Plt3.pdf')
plt.figure(4)
plt.plot(xr,terr1dy_list,'r')
plt.plot(xr,terr2dy_list,'b')
plt.xlabel('North (km)')
plt.ylabel('Ty')
#plt.savefig('Plt4.pdf')
plt.show()



#Test terrain function derivaties
#x_list = np.linspace(100,200,50)
#y_list = np.linspace(78.5944,78.5944,50)
#for i,x in enumerate(x_list):
#    lat = np.real(x)/111+lats[0]
#    lon = np.real(y_list[i])/(111*np.sin(lat*np.pi/180.0))+lons[0]
#    dx1 = (geo_spl.ev(lat+0.01,lon)-geo_spl.ev(lat,lon))/((0.01)*111)
#    dx2 = terrain(x+1j*1e-30,y_list[i])/(1j*1e-30)
#    print(x,y_list[i],dx1,np.real(dx2))
#quit()
