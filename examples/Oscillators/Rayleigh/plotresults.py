from beluga.bvpsol.Pseudospectral import linter
from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.t, sol.y[:, 0], label='$y_1$')
plt.plot(sol.t, sol.y[:, 1], label='$y_2$')
plt.xlabel('Time [s]')
plt.ylabel('State Variables')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol.y[:, 0], sol.y[:, 1])
plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u[:, 0])
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Control')

plt.figure()
plt.plot(sol.t, sol.dual[:, 0], label='$\lambda_{y_1}$')
plt.plot(sol.t, sol.dual[:, 1], label='$\lambda_{y_2}$')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Costate Variables')
plt.legend()

plt.figure()
plt.plot(sol.t, sol.u[:,0] + sol.y[:,0]/6)
plt.plot([sol.t[0], sol.t[-1]], [0, 0], color='k', linestyle='--')
plt.plot([sol.t[0], sol.t[-1]], [-1, -1], color='k', linestyle='--')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Path-constraint')
plt.show()
