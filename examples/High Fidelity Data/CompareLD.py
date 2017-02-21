"""Compares lift and drag curves for various approximations"""
import numpy as np
import functools
from scipy import interpolate
import matplotlib.pyplot as plt

f = np.loadtxt('SphereConeTable.txt')
alfalist = []
CLdata = []
CDdata = []
for line in f:
    alfalist.append(line[0])
    CLdata.append(line[1])
    CDdata.append(line[2])
CLtck = interpolate.splrep(alfalist,CLdata) #(tck = knots,coefficients,order)
CDtck = interpolate.splrep(alfalist,CDdata)

def CLlookup(alfa, dc, rn, rc):
    if np.iscomplex(alfa)==True:
        deriv=interpolate.splev(np.real(alfa),CLtck,der=1)
        return deriv*1j*1e-30
    else:
        return interpolate.splev(alfa,CLtck,der=0)

def CDlookup(alfa, dc, rn, rc):
    if np.iscomplex(alfa)==True:
        deriv=interpolate.splev(np.real(alfa),CDtck,der=1)
        return deriv*1j*1e-30
    else:
        return interpolate.splev(alfa,CDtck,der=0)

def CLfunction(alfa, dc, rn, rc):
    CN = (1-(rn/rc)**2*np.cos(dc)**2)*np.cos(dc)**2*np.sin(2*alfa)
    CA = (1-np.sin(dc)**4)*(rn/rc)**2 + (2*np.sin(dc)**2*np.cos(alfa)**2+np.cos(dc)**2*np.sin(alfa)**2)*(1-(rn/rc)**2*np.cos(dc)**2)
    return CN*np.cos(alfa) - CA*np.sin(alfa)

def CDfunction(alfa, dc, rn, rc):
    CN = (1-(rn/rc)**2*np.cos(dc)**2)*np.cos(dc)**2*np.sin(2*alfa)
    CA = (1-np.sin(dc)**4)*(rn/rc)**2 + (2*np.sin(dc)**2*np.cos(alfa)**2+np.cos(dc)**2*np.sin(alfa)**2)*(1-(rn/rc)**2*np.cos(dc)**2)
    return CA*np.cos(alfa) + CN*np.sin(alfa)

def CLsimple(alfa, dc, rn, rc):
    return 1.1298*alfa

def CDsimple(alfa, dc, rn, rc):
    return 1.8102*alfa**2 + 0.3579

alfarng = np.linspace(0,-25,100)*np.pi/180
dc = 25 * np.pi/180
rc = 0.3
rn = 0.01

CD = []
CL = []
for alfa in alfarng:
    CD.append(CDlookup(alfa, dc, rn, rc))
    CL.append(CLlookup(alfa, dc, rn, rc))

plt.figure(1)
plot1, = plt.plot(alfarng*180/np.pi,CL,'k')
plot2, = plt.plot(alfarng*180/np.pi,CLfunction(alfarng, dc, rn, rc),'r--')
plot3, = plt.plot(alfarng*180/np.pi,CLsimple(alfarng, dc, rn, rc),'k:')
plt.xlabel('AoA (deg)')
plt.ylabel('C_L')
plt.legend(['Look up','Analytical','Linear'],loc='best')
plt.savefig('LiftCompare.png')

plt.figure(2)
plot1, = plt.plot(alfarng*180/np.pi,CD,'k')
plot2, = plt.plot(alfarng*180/np.pi,CDfunction(alfarng, dc, rn, rc),'r--')
plot3, = plt.plot(alfarng*180/np.pi,CDsimple(alfarng, dc, rn, rc),'k:')
plt.xlabel('AoA (deg)')
plt.ylabel('C_D')
plt.legend(['Look up','Analytical','Quadratic'],loc='best')
plt.savefig('DragCompare.png')

plt.show()
