from beluga.utils import load
import matplotlib.pyplot as plt

data = load('indirect_data.blg')
sol_set = data['solutions']
sol_indirect = sol_set[-1][-1]

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.y[:, 0], linestyle='-', color='b', label='indirect')
plt.plot([sol_indirect.t[0], sol_indirect.t[-1]], [sol_indirect.k[-1]]*2, linestyle='--', color='k')
plt.title('Position')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.y[:, 1], linestyle='-', color='b', label='indirect')
plt.title('Velocity')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.u, linestyle='-', color='b', label='indirect')
plt.title('Control')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.lam[:, 0], linestyle='-', color='b', label='indirect')
plt.title('Position Costate')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.lam[:, 1], linestyle='-', color='b', label='indirect')
plt.title('Velocity Costate')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)
plt.show()
