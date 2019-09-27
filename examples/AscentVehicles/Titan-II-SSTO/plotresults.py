from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.y[:,0]/1000, sol.y[:,1]/1000)
plt.xlabel('Downrange [km]')
plt.ylabel('Altitude [km]')
plt.title('Time Optimal Launch of a Titan-II Trajectory')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,2]/1000, label='Horizontal Velocity')
plt.plot(sol.t, sol.y[:,3]/1000, label='Vertical Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [km/s]')
plt.title('Velocities of a Titan-II')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u*180/np.pi)
plt.xlabel('Time [s]')
plt.ylabel('Control [degrees]')
plt.title('Titan-II Steering Angle')
plt.grid(True)
plt.show()
