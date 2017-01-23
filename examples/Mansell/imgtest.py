import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from osgeo import gdal

# GDAL does not use python exceptions by default
gdal.UseExceptions()

#cwd = os.path.dirname(__file__)
#datadir = os.path.join(os.path.split(cwd)[0], 'data')


geo = gdal.Open('imgn45w114_13.img')

#drv = geo.GetDriver()
#print drv.GetMetadataItem('DMD_LONGNAME')
topo = geo.ReadAsArray()

print(topo[9375][2398])
#i, j = np.where(topo>0)
#topo = topo[min(i):max(i)+1, min(j):max(j)+1]
#topo[topo==0] = np.nan
#print topo.shape

fig = plt.figure(frameon=False)
plt.imshow(topo, cmap=cm.BrBG_r)
plt.axis('off')
cbar = plt.colorbar(shrink=0.75)
cbar.set_label('meters')
plt.show()