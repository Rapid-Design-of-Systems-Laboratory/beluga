import matplotlib.pyplot as plt
import numpy as np
from math import *

def terrain(x,y): #Functions must be defined outside of the get_problem()
#    terr=terr_query(x,y)#interpolate.bisplev(x,y,tck)
    terr=(-0.3*exp(-0.5*((x-2.7)**2+1.5*(y-2.1)**2))+2.6*exp(-0.55*(0.87*(x-6.7)**2+(y-2.2)**2))+2.1*exp(-0.27*(0.2*(x-5.5)**2+(y-7.2)**2))+1.6*(cos(0.8*y))**2*(sin(0.796*x))**2)
    return terr
    
Ycoords=np.linspace(0,10,100)
Xcoords=Ycoords
z=np.zeros((100,100))
for i in range(100):
    for j in range(100):
        z[i,j]=terrain(Xcoords[i],Ycoords[j])
plt.contour(Ycoords,Xcoords,z)
plt.show()