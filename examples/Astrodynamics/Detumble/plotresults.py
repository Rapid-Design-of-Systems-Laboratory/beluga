from beluga.utils import load
import matplotlib.pyplot as plt

sol_set = load('data.json')

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.t, sol.y[:, 0], color='b', label=r'$\omega_1$')
plt.plot(sol.t, sol.y[:, 1], color='r', label=r'$\omega_2$')
plt.plot(sol.t, sol.y[:, 2], color='g', label=r'$\omega_3$')
plt.title('Rotation Rates')
plt.ylabel('Angular Rates [rad/s]')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot([sol.t[0], sol.t[-1]], [1, 1], color='k', linestyle='--', linewidth=3)
plt.plot([sol.t[0], sol.t[-1]], [-1, -1], color='k', linestyle='--', linewidth=3)
plt.plot(sol.t, sol.u[:, 0], color='b', label='$u_1$')
plt.plot(sol.t, sol.u[:, 1], color='r', label='$u_2$')
plt.plot(sol.t, sol.u[:, 2], color='g', label='$u_3$')
plt.title('Control History')
plt.ylabel('Control [rad/s^2]')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)

plt.show()
