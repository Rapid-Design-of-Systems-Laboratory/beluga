from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

g_0 = 1.0

h_0 = 1.0
v_0 = 0.0
m_0 = 1.0

t_c = 3.5
h_c = 500
v_c = 620
m_c = 0.6

tar_m_f = m_0 * m_c
c = 0.5 * sqrt(g_0 * h_0)
d_c = 0.5 * v_c * m_0 / g_0
thrust_max = t_c * g_0 * m_0

sol_set = load('data.json')

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.t, sol.y[:, 0])
plt.xlabel('Time [s]')
plt.ylabel('Altitude [nd]')
plt.title('Altitude Profile')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:, 1])
plt.xlabel('Time [s]')
plt.ylabel('Velocity [nd]')
plt.title('Velocity Profile')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:, 2])
plt.xlabel('Time [s]')
plt.ylabel('Mass [nd]')
plt.title('Mass Profile')
plt.grid(True)

plt.figure()
# plt.plot(traj.t, thrust_max*(np.sin(traj.u[:, 0]) + 1)/2, label='Thrust')
plt.plot(sol.t, sol.u[:, 0], label='Thrust')
plt.plot(sol.t, 1 * d_c * sol.y[:, 1]**2 * np.exp(-h_c * (sol.y[:, 0] - h_0) / h_0), label='Drag')
plt.xlabel('Time [s]')
plt.ylabel('Force [nd]')
plt.title('Forces')
plt.legend()
plt.grid(True)
plt.show()
