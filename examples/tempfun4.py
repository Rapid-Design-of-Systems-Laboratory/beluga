from beluga.bvpsol import spbvp, Shooting
from beluga.ivpsol import Trajectory
import numpy as np
import matplotlib.pyplot as plt

import time

const = 1e-1

# Travis original: 19 min 45 sec
# Travis built in: 10 min 35 sec

# Tests original: 574.07 seconds
# Tests built in Jacobian: 178.48 seconds

# This problem original 1e-1:
# Unreduced: 0.03403019905090332
# Reduced: 0.09608721733093262

# This built in Jac 1e-1:
# Unreduced: 0.04604029655456543
# Reduced: 0.10009169578552246

# N = 1: 0.04604983329772949
# N = 2: 0.029026269912719727
# N = 4: 0.08207488059997559
# N = 8: 0.07606768608093262
# N = 32: 0.1951766014099121
# N = 256: 3.5632269382476807

N = 4

# N = 1
# array([[1.00000000e+00, 0.00000000e+00],
#        [9.99999884e-01, 2.20255495e+03]])

# N = 2
# array([[  1.        ,   0.        ,   0.        ,   0.        ],
#        [  0.        ,   0.        ,   1.        ,  14.74134256],
#        [  1.        ,  14.74134259,  -1.        ,   0.        ],
#        [  0.        , 148.4134259 ,   0.        ,  -1.        ]])

# N = 3
# array([[ 1.        ,  0.        ,  0.        ,  0.        ,  0.        ,  0.        ],
#        [ 0.        ,  0.        ,  0.        ,  0.        ,  1.        ,  2.70316615],
#        [ 1.        ,  2.70316615, -1.        ,  0.        ,  0.        ,  0.        ],
#        [ 0.        , 28.03166151,  0.        , -1.        ,  0.        ,  0.        ],
#        [ 0.        ,  0.        ,  1.        ,  2.70316615, -1.        ,  0.        ],
#        [ 0.        ,  0.        ,  0.        , 28.03166151,  0.        , -1.        ]])

# matrix([[ 1.        ,  0.        ,  0.        ,  0.        ,  0.        , 0.        ],
#         [ 0.        ,  0.        ,  0.        ,  0.        ,  1.        , 2.70316615],
#         [ 1.        ,  2.70316615, -1.        ,  0.        ,  0.        , 0.        ],
#         [ 0.        , 28.03166149,  0.        , -1.        ,  0.        , 0.        ],
#         [ 0.        ,  0.        ,  1.        ,  2.70316615, -1.        , 0.        ],
#         [ 0.        ,  0.        ,  0.        , 28.0316615 ,  0.        , -1.        ]])

def odefun(X, u, p, const):
    return X[1], X[1] / const[0]

def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
    return X0[0] - 1, Xf[0]


algo = Shooting(odefun, None, bcfun, num_arcs=N)
solinit = Trajectory()
solinit.t = np.linspace(0, 1, 2)
solinit.y = np.array([[0, 1], [0, 1]])
solinit.const = np.array([const])
t0 = time.time()
sol1 = algo.solve(solinit)
t1 = time.time()
print('Unreduced: ' + str(t1-t0))

# def odefun(X, u, p, const):
#     return X[0] / const[0]
#
# def quadfun(X, u, p, const):
#     return X[0]
#
# def bcfun(X0, q0, u0, Xf, qf, uf, p, ndp, const):
#     return q0[0] - 1, qf[0]
#
# algo = Shooting(odefun, quadfun, bcfun)
# solinit = Trajectory()
# solinit.t = np.linspace(0, 1, 2)
# solinit.y = np.array([[1], [1]])
# solinit.q = np.array([[0], [9]])
# solinit.const = np.array([const])
# t0 = time.time()
# sol2 = algo.solve(solinit)
# t1 = time.time()
# print('Reduced: ' + str(t1-t0))
#
# plt.plot(sol1.t, sol1.y[:,1], color='b', linewidth=3)
# plt.plot(sol2.t, sol2.y[:,0], color='r')
# plt.title('base space')
# plt.show()
#
# plt.plot(sol1.t, sol1.y[:,0], color='b', linewidth=3)
# plt.plot(sol2.t, sol2.q[:,0], color='r')
# plt.title('q\'s')
# plt.show()
