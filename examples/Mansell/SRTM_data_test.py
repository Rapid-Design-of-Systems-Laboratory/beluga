#==============================================================================#
# PROGRAM: SRTM_data_test.py
# Description: Tests method of accessing SRTM DEM data obtained using the module
# from: https://github.com/tkrajina/srtm.py
#==============================================================================#
import srtm
import numpy as np
import matplotlib.pyplot as plt
geo_elevation_data = srtm.get_data()
npoints = 500
y_east = np.linspace(-123,-113,2*npoints)
x_north = np.linspace(50,55,npoints)
dem = np.zeros((npoints,2*npoints))
for x_ind,x in enumerate(x_north):
    print(x)
    for y_ind,y in enumerate(y_east):
        dem[x_ind,y_ind] = geo_elevation_data.get_elevation(x,y)

#Plot
#plt.contour(y_east,x_north,dem)
#plt.show()

#Image
plt.imshow(dem)
plt.show()

print(dem[32,117])
#print(geo_elevation_data.get_elevation(49.5,-117))

#Problem: strange gap in data between 49 and 50 degrees latitude
#It appears that this data is actually missing from SRTM
#Data missing in some points, particularly in mountains (NaN)
