import numpy as np
from beluga.utils.math import *
from beluga.utils.tictoc import *

tf = 1

Dt = 0.1
sigv = 0.1
sigw = 0.1
sigr = 0.1

w = 3.1415/2

xb = 5
yb = 5

u_max = 0.1

v = 30

x_n = 100
y_n = 1e-4
theta_n = 0.1

p11_n = 1e5
p12_n = 1e5
p13_n = 1e5
p22_n = 1e5
p23_n = 1e5
p33_n = 1e5

lamX_N = 50
lamY_N = -100
lamTHETA_N = 2

lamP11_N = 1
lamP12_N = 1
lamP13_N = 1
lamP22_N = 1
lamP23_N = 1
lamP33_N = 1

x_s = 1
y_s = 1
theta_s = 1

p11_s = 1e-3
p12_s = 1e-3
p13_s = 1e-3
p22_s = 1e-1
p23_s = 1e-2
p33_s = 1e-3

ep = 5

tic()
for i in range(100000):
    fx = np.array([(tf)*(ep*u_max*cos(w) + v*cos(theta_n*theta_s)/x_s),
        (tf)*(v*sin(theta_n*theta_s)/y_s),
        (tf)*(u_max*sin(w)/theta_s),
        (tf)*((Dt*sigv**2*cos(theta_n*theta_s)**2 - 2*p13_n*p13_s*v*sin(theta_n*theta_s) - p11_n*p11_s*(x_n*x_s - xb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p12_n*p12_s*(y_n*y_s - yb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p11_s),
        (tf)*((Dt*sigv**2*sin(theta_n*theta_s)*cos(theta_n*theta_s) - p13_n*p13_s*v*sin(theta_n*theta_s) + p13_n*p13_s*v*cos(theta_n*theta_s) - p12_n*p12_s*(x_n*x_s - xb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p22_n*p22_s*(y_n*y_s - yb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p12_s),
        (tf)*((-p33_n*p33_s*v*sin(theta_n*theta_s) - p13_n*p13_s*(x_n*x_s - xb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p23_n*p23_s*(y_n*y_s - yb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p13_s),
        (tf)*((Dt*sigv**2*sin(theta_n*theta_s)**2 + p13_n*p13_s*v*cos(theta_n*theta_s) + p23_n*p23_s*v*cos(theta_n*theta_s) - p12_n*p12_s*(x_n*x_s - xb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p22_n*p22_s*(y_n*y_s - yb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p22_s),
        (tf)*((p33_n*p33_s*v*cos(theta_n*theta_s) - p13_n*p13_s*(x_n*x_s - xb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p23_n*p23_s*(y_n*y_s - yb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p23_s),
        (tf)*((Dt*sigw**2 - p13_n*p13_s*(x_n*x_s - xb)*(p13_n*p13_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p13_n*p13_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p23_n*p23_s*(y_n*y_s - yb)*(p13_n*p13_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p13_n*p13_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p33_s),
        tf*0,
        ])
# print(fx)
print(toc())

tic()
for j in range(100000):
    gx = np.array([(tf)*(ep*u_max*cos(w) + v*cos(theta_n*theta_s)/x_s),
        (tf)*(v*sin(theta_n*theta_s)/y_s),
        (tf)*(u_max*sin(w)/theta_s),
        (tf)*((Dt*sigv**2*cos(theta_n*theta_s)**2 - 2*p13_n*p13_s*v*sin(theta_n*theta_s) - p11_n*p11_s*(x_n*x_s - xb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p12_n*p12_s*(y_n*y_s - yb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p11_s),
        (tf)*((Dt*sigv**2*sin(theta_n*theta_s)*cos(theta_n*theta_s) - p13_n*p13_s*v*sin(theta_n*theta_s) + p13_n*p13_s*v*cos(theta_n*theta_s) - p12_n*p12_s*(x_n*x_s - xb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p22_n*p22_s*(y_n*y_s - yb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p12_s),
        (tf)*((-p33_n*p33_s*v*sin(theta_n*theta_s) - p13_n*p13_s*(x_n*x_s - xb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p23_n*p23_s*(y_n*y_s - yb)*(p11_n*p11_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p12_n*p12_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p13_s),
        (tf)*((Dt*sigv**2*sin(theta_n*theta_s)**2 + p13_n*p13_s*v*cos(theta_n*theta_s) + p23_n*p23_s*v*cos(theta_n*theta_s) - p12_n*p12_s*(x_n*x_s - xb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p22_n*p22_s*(y_n*y_s - yb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p22_s),
        (tf)*((p33_n*p33_s*v*cos(theta_n*theta_s) - p13_n*p13_s*(x_n*x_s - xb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p23_n*p23_s*(y_n*y_s - yb)*(p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p23_s),
        (tf)*((Dt*sigw**2 - p13_n*p13_s*(x_n*x_s - xb)*(p13_n*p13_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p13_n*p13_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) - p23_n*p23_s*(y_n*y_s - yb)*(p13_n*p13_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) + p13_n*p13_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)))/p33_s),
        tf*0,
        ])
# print(fx)
print(toc())