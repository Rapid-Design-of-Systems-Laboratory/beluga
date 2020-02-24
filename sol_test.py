import beluga
import logging
import numpy as np
import beluga.optimlib
import time

n = 11

t0 = 10.1
tf = 20.1

y0 = [0., 1., 2.]
yf = [1., 2., 3.]

u0 = [1.2, 2.2]
uf = [3.2, 4.2]

t = np.linspace(t0, tf, n)
y = np.array([np.linspace(y0, yf, n) for y0, yf in zip(y0, yf)])
u = np.array([np.linspace(u0, uf, n) for u0, uf in zip(u0, uf)])
p = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
k = np.array([0.7, 1.7, 2.7, 3.7])

ocp_sol = beluga.problib.OCPSol(t, y, u, p, k)

mom_map = beluga.optimlib.MomemtumShiftSolMap(in_place=False)
mom_sol = mom_map.map_sol(ocp_sol)
inv_mom_sol = mom_map.inv_map_sol(mom_sol)


