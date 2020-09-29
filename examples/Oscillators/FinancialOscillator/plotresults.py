from beluga.utils import load
import matplotlib.pyplot as plt

data = load('indirect_data.beluga')
sol_set = data['solutions']
sol_indirect = sol_set[-1][-1]


plt.figure()
plt.plot(sol_indirect.t, sol_indirect.y[:, 0], linestyle='-', color='b', label='indirect')
plt.xlabel('Time [nd]')
plt.ylabel('$x_1$ [nd]')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(sol_indirect.y[:, 0], sol_indirect.y[:, 1], linestyle='-', color='b', label='indirect')
plt.title('State-Space')
plt.xlabel('$x_1$ [nd]')
plt.ylabel('$x_2$ [nd]')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot([0,1], [2,2], linestyle='--', color='k')
plt.plot([0,1], [-2,-2], linestyle='--', color='k')
plt.plot(sol_indirect.t, sol_indirect.u, linestyle='-', color='b', label='indirect')
plt.title('Control')
plt.xlabel('Time [nd]')
plt.ylabel('$u$ [nd]')
plt.grid(True)
plt.legend()
plt.show()

