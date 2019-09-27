from beluga.utils import load
import matplotlib.pyplot as plt

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.y[:,0], sol.y[:,1])
plt.title('Trajectory')
plt.ylabel('Vertical Position [m]')
plt.xlabel('Horizontal Position [m]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,0])
plt.ylabel('Horizontal Position [m]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,1])
plt.ylabel('Vertical Position [m]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,2])
plt.ylabel('Horizontal Velocity [m/s]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,3])
plt.ylabel('Vertical Velocity [m/s]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u[:, 0])
plt.ylabel('Lift Coefficient')
plt.xlabel('Time [s]')
plt.grid(True)
plt.show()
