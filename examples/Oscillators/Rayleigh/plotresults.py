from beluga.utils import load
import matplotlib.pyplot as plt

data = load('data.beluga')
sol_set = data['solutions']
traj = sol_set[-1][-1]

continuation = sol_set[-1]
L = len(continuation)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.y[:, 0], color=(1*(ind/L), 1*(L-ind)/L, 0))
    plt.plot(sol.t, sol.y[:, 1], color=(0, 1*(L-ind)/L, 1*(ind/L)))
plt.xlabel('Time [s]')
plt.ylabel('State Variables')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.y[:, 0], sol.y[:, 1], color=(0, 1*(L-ind)/L, 1*(ind/L)))
plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.u[:, 0], color=(0, 1*(L-ind)/L, 1*(ind/L)))

plt.plot(traj.t, -traj.y[:,0]/6, color='k', linestyle='--')
plt.plot(traj.t, -traj.y[:,0]/6 - 1, color='k', linestyle='--')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Control')

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.dual[:, 0], color=(1*(ind/L), 1*(L-ind)/L, 0), label=r'$\lambda_{y_1}$')
    plt.plot(sol.t, sol.dual[:, 1], color=(0, 1*(L-ind)/L, 1*(ind/L)), label=r'$\lambda_{y_2}$')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Costate Variables')

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.u[:, 0] + sol.y[:, 0]/6, color=(0, 1*(L-ind)/L, 1*(ind/L)))

plt.plot([traj.t[0], traj.t[-1]], [0, 0], color='k', linestyle='--')
plt.plot([traj.t[0], traj.t[-1]], [-1, -1], color='k', linestyle='--')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Path-constraint')
plt.show()
