from beluga.bvpsol.Pseudospectral import linter
from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

data = load('direct_data.blg')
sol_set = data['solutions']
sol_direct = sol_set[-1][-1]

data = load('indirect_data.blg')
sol_set = data['solutions']
sol_indirect = sol_set[-1][-1]

ts = np.linspace(sol_direct.t[0], sol_direct.t[-1], num=200)

plt.figure()
plt.plot(sol_direct.t, sol_direct.y[:, 0], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.y[:, 0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:, 0], linestyle='-', color='b', label='indirect')
plt.plot([sol_direct.t[0], sol_direct.t[-1]], [sol_direct.const[-1]]*2, linestyle='--', color='k')
plt.title('Position')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_direct.t, sol_direct.y[:, 1], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.y[:, 1], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.y[:, 1], linestyle='-', color='b', label='indirect')
plt.title('Velocity')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_direct.t, sol_direct.u, linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.u[:, 0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.u, linestyle='-', color='b', label='indirect')
plt.title('Control')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_direct.t, sol_direct.dual[:, 0], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.dual[:, 0], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.dual[:, 0], linestyle='-', color='b', label='indirect')
plt.title('Position Costate')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_direct.t, sol_direct.dual[:, 1], linestyle='--', color='r', marker='o')
plt.plot(ts, linter(sol_direct.t, sol_direct.dual[:, 1], ts), linestyle='-', color='r', label='direct')
plt.plot(sol_indirect.t, sol_indirect.dual[:, 1], linestyle='-', color='b', label='indirect')
plt.title('Velocity Costate')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)
plt.show()
