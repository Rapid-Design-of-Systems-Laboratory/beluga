from beluga.utils import load
import matplotlib.pyplot as plt

data = load('indirect_data.beluga')
sol_set = data['solutions']
sol_indirect = sol_set[-1][-1]

# data = load('direct_data.blg')
# sol_set = data['solutions']
# sol_direct = sol_set[-1][-1]

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.y[:, 0], color='b', linewidth=2, label='Indirect')
plt.plot(sol_indirect.t, -sol_indirect.y[:, 0], color='b', linewidth=2)
# plt.plot(sol_direct.t, sol_direct.y[:, 0], color='r', label='Direct')
# plt.plot(sol_direct.t, -sol_direct.y[:, 0], color='r')
plt.xlabel('$x$ [m]')
plt.ylabel('$r$ [m]')
plt.title('Vehicle Shape')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_indirect.t, sol_indirect.u[:, 0], color='b', label='Indirect')
# plt.plot(sol_direct.t, sol_direct.u[:, 0], color='r', label='Direct')
plt.xlabel('$x$ [m]')
plt.ylabel('$u$ [m/s]')
plt.legend()
plt.grid(True)
plt.show()
