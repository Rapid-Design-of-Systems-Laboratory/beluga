#Super simple test
import numpy as np

def terr( x_pos, y_pos ):
    #Defines terrain elevation [m] as a function of x and y positions [m]
    elev = 100.0*(np.sin(0.5*(x_pos/1000.0)))**2.0 #User defined elevation map
    return elev
     
num=terr(5500,1500)
print num