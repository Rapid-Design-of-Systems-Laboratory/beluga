from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.t, sol.y[:,0])
plt.ylabel('Altitude [m]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,1]*180/np.pi)
plt.ylabel('Longitude [deg]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,2]*180/np.pi)
plt.ylabel('Latitude [deg]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,3])
plt.ylabel('Velocity [m/s]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,4]*180/np.pi)
plt.ylabel('Flight Path Angle [deg]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:,5]*180/np.pi)
plt.ylabel('Heading [deg]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u[:,0]*180/np.pi)
plt.ylabel('Angle of Attack [deg]')
plt.xlabel('Time [s]')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u[:,1]*180/np.pi)
plt.ylabel('Bank Angle [deg]')
plt.xlabel('Time [s]')
plt.grid(True)
plt.show()
