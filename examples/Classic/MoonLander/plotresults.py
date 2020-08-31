from beluga.utils import load
import matplotlib.pyplot as plt

data = load('data.beluga')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.t, sol.y[:,0], label='Altitude')
plt.plot(sol.t, sol.y[:,1], label='Velocity')
plt.xlabel('Time [s]')
plt.ylabel('States [nd]')
plt.title('Moon Lander States')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(sol.t, sol.u)
plt.plot([sol.t[0], sol.t[-1]], [0, 0], color='k', linestyle='--')
plt.plot([sol.t[0], sol.t[-1]], [4, 4], color='k', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('Thrust [nd]')
plt.title('Bounded Control History')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.dual[:,0], label='Altitude (costate)')
plt.plot(sol.t, sol.dual[:,1], label='Velocity (costate)')
plt.xlabel('Time [s]')
plt.ylabel('Costates [nd]')
plt.title('Moon Lander Costates')
plt.legend()
plt.grid(True)
plt.show()
