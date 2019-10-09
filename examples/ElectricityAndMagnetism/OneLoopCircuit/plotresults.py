from beluga.utils import load
import matplotlib.pyplot as plt

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Current [A]', color=color)
ax1.plot(sol.t, sol.y[:,0], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Voltage [volts]', color=color)
ax2.plot(sol.t, sol.u[:,0], color=color)
ax2.plot([sol.t[0], sol.t[-1]], [sol.const[0]]*2, linestyle='--', color='k')
ax2.plot([sol.t[0], sol.t[-1]], [sol.const[1]]*2, linestyle='--', color='k', label='Min/Max Voltage')
ax2.tick_params(axis='y', labelcolor=color)

plt.legend()
plt.grid(True)
fig.tight_layout()
plt.show()
