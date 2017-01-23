#===============================================================================
# PROGRAM: "Track_demo.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: Test of track planning on real terrain using graph search
#              continuation
#===============================================================================
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
import gdal

#Load Geotiff data
ds = gdal.Open('WL2.tif')
band = ds.GetRasterBand(1)
elevation = band.ReadAsArray()
elevation = np.flipud(elevation)
nrows, ncols = elevation.shape

#------------------------Create the terrain function---------------------------#
#Compute lat/lon extent of image
lon0, dlon, dlondlat, lat0, dlatdlon, dlat = ds.GetGeoTransform()
#NOTE: lat0,lon0 coordinates of the upper right corner
lats = np.linspace(lat0+dlat*nrows,lat0,nrows)
lons = np.linspace(lon0,lon0+dlon*ncols,ncols)
elevation = elevation.astype(np.float) #Convert to a floating point array (important for smoothing)

#Spline fit lat/lon image
print('Creating terrain function...')
elevation = ndimage.gaussian_filter(elevation,sigma=20,order=0) #Smooth terrain
geo_spl=interpolate.RectBivariateSpline(lats,lons,elevation,kx=3,ky=3,s=10)

def terrain(x,y):
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

print('Terrain function ready')
#------------------------------------------------------------------------------#

#----------------------------Beluga Problem------------------------------------#
def get_problem():
    """A simple test of optimal surface track planning."""

    problem = beluga.optim.Problem('Track_demo')
    problem.mode='analytical' #Other options: 'numerical', 'dae'

    #Define independent variables
    problem.independent('t', 's')

    # Define equations of motion
    problem.state('x','V*cos(hdg)','k')   \
           .state('y','V*sin(hdg)','k')  \

    # Define controls
    problem.control('hdg','rad')

    # Define cost functional
    problem.cost['path'] =  Expression('(1-w)+w*V*conv*elev*terrain(x,y)', 's')

    #Define constraints
    problem.constraints().initial('x-x_0','k') \
                         .initial('y-y_0','k') \
                         .terminal('x-x_f','k') \
                         .terminal('y-y_f','k')

    #Define constants
    problem.constant('w',0.9,'1') #Initial Terrain weighting factor
    problem.constant('conv',1,'s/k^2') #Integral conversion factor
    problem.constant('V',1,'k/s') #Vehicle speed
    problem.constant('elev',0.001,'k') #Units for the elevation

    #Unit scaling
    problem.scale.unit('k',1) \
                 .unit('s',1) \
                 .unit('rad',1)

    #Configure solver
    problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=50, verbose = True, cached = False, number_arcs=8)
    #problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=50, verbose = True, cached = False)

    #Initial Guess
    problem.guess.setup('auto',start=[16,10], costate_guess=[0.0,-0.1])

    #Add continuation steps
    problem.steps.add_step(strategy='HPA') \
                            .terminal('x', 180, 50) \
                            .terminal('y', 98, 50)

    return problem

if __name__ == '__main__':
    import beluga.Beluga as Beluga
    problem = get_problem()
    sol = Beluga.run(problem)

#NOTE: DEM is upside down. Try np.flipud
