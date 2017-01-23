#==============================================================================#
# Tests the loading of tif elevation data
# Use python elevation to get data (must be in home directory for some reason)
# Then use this code to display the data
#==============================================================================#
import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open('WL2.tif')
band = ds.GetRasterBand(1)
elevation = band.ReadAsArray()

nrows, ncols = elevation.shape

# I'm making the assumption that the image isn't rotated/skewed/etc.
# This is not the correct method in general, but let's ignore that for now
# If dxdy or dydx aren't 0, then this will be incorrect
x0, dx, dxdy, y0, dydx, dy = ds.GetGeoTransform()

x1 = x0 + dx * ncols
y1 = y0 + dy * nrows

plt.imshow(elevation, cmap='gist_earth', extent=[x0, x1, y1, y0])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
