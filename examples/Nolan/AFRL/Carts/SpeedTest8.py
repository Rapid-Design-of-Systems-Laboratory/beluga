import numpy as np
from beluga.utils.math import *
from beluga.utils.tictoc import *

from numpy import pi

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
y_n = 100
theta_n = 0.1

p11_n = 1
p12_n = 1
p13_n = 1
p22_n = 1
p23_n = 1
p33_n = 1

lamX_N = 1
lamY_N = 1
lamTHETA_N = 1

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
for i in range(1000):
    fx = np.array([
        (tf)*(-lamP11_N*(-2*Dt*sigv**2*theta_s*sin(theta_n*theta_s)*cos(theta_n*theta_s) - 2*p13_n*p13_s*theta_s*v*cos(theta_n*theta_s))/p11_s - lamP12_N*(-Dt*sigv**2*theta_s*sin(theta_n*theta_s)**2 + Dt*sigv**2*theta_s*cos(theta_n*theta_s)**2 - p13_n*p13_s*theta_s*v*sin(theta_n*theta_s) - p13_n*p13_s*theta_s*v*cos(theta_n*theta_s))/p12_s + lamP13_N*p33_n*p33_s*theta_s*v*cos(theta_n*theta_s)/p13_s - lamP22_N*(2*Dt*sigv**2*theta_s*sin(theta_n*theta_s)*cos(theta_n*theta_s) - p13_n*p13_s*theta_s*v*sin(theta_n*theta_s) - p23_n*p23_s*theta_s*v*sin(theta_n*theta_s))/p22_s + lamP23_N*p33_n*p33_s*theta_s*v*sin(theta_n*theta_s)/p23_s + lamX_N*theta_s*v*sin(theta_n*theta_s)/x_s - lamY_N*theta_s*v*cos(theta_n*theta_s)/y_s),
        ])
tock = toc()
print(fx)
print('A:' + str(tock))

tic()
for i in range(1000):
    gx = np.array([
        (tf)*(-np.imag(-lamP11_N*(-Dt*sigv**2*cos(theta_s*(1.0e-50*1j + theta_n))**2 + 2*p13_n*p13_s*v*sin(theta_s*(1.0e-50*1j + theta_n)))/p11_s + lamP12_N*(Dt*sigv**2*sin(theta_s*(1.0e-50*1j + theta_n))*cos(theta_s*(1.0e-50*1j + theta_n)) - p13_n*p13_s*v*sin(theta_s*(1.0e-50*1j + theta_n)) + p13_n*p13_s*v*cos(theta_s*(1.0e-50*1j + theta_n)))/p12_s - lamP13_N*p33_n*p33_s*v*sin(theta_s*(1.0e-50*1j + theta_n))/p13_s + lamP22_N*(Dt*sigv**2*sin(theta_s*(1.0e-50*1j + theta_n))**2 + p13_n*p13_s*v*cos(theta_s*(1.0e-50*1j + theta_n)) + p23_n*p23_s*v*cos(theta_s*(1.0e-50*1j + theta_n)))/p22_s + lamP23_N*p33_n*p33_s*v*cos(theta_s*(1.0e-50*1j + theta_n))/p23_s + lamX_N*v*cos(theta_s*(1.0e-50*1j + theta_n))/x_s + sin(theta_s*(1.0e-50*1j + theta_n)))/1e-50),
        (tf)*(-np.imag(lamX_N * v * cos((theta_n+1e-50j) * theta_s) / x_s + Dt * lamP11_N * sigv ** 2 * cos((theta_n+1e-50j) * theta_s) ** 2 / p11_s - 2 * lamP11_N * p13_n * p13_s * v * sin((theta_n+1e-50j) * theta_s) / p11_s + Dt * lamP12_N * sigv ** 2 * sin((theta_n+1e-50j) * theta_s) * cos((theta_n+1e-50j) * theta_s) / p12_s + lamP12_N * p13_n * p13_s * v * cos((theta_n+1e-50j) * theta_s) / p12_s - lamP12_N * p13_n * p13_s * v * sin((theta_n+1e-50j) * theta_s) / p12_s - lamP13_N * p33_n * p33_s * v * sin((theta_n+1e-50j) * theta_s) / p13_s + Dt * lamP22_N * sigv ** 2 * sin((theta_n+1e-50j) * theta_s) ** 2 / p22_s + lamP22_N * p13_n * p13_s * v * cos((theta_n+1e-50j) * theta_s) / p22_s + lamP22_N * p23_n * p23_s * v * cos((theta_n+1e-50j) * theta_s) / p22_s + lamP23_N * p33_n * p33_s * v * cos((theta_n+1e-50j) * theta_s) / p23_s + sin((theta_n+1e-50j) * theta_s)))/1e-50])
tock = toc()
print(gx)
print('N:' + str(tock))

print(fx-gx)