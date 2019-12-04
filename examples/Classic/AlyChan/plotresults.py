from beluga.utils import load
import matplotlib.pyplot as plt

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(sol.t, sol.y[:,0], color='b')
ax1.plot(sol.t, sol.y[:,1], color='b')
ax1.plot(sol.t, sol.y[:,2], color='b')
ax2.plot(sol.t, sol.u[:,0], color='r')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('$x$ [m]', color='b')
ax2.set_ylabel('$u$ [m/s^2]', color='r')

plt.show()
