from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

data = load('lowthrust_shooting_data.blg')
sol_set_shooting = data['solutions']
data = load('lowthrust_collocation_data.blg')
sol_set_collocation = data['solutions']

sol_c = sol_set_collocation[-1][-1]
sol_s = sol_set_shooting[-1][-1]

anom = np.linspace(0, 2*np.pi, num=1000)

plt.figure()
plt.plot(0, 0, marker='*')
plt.plot(np.cos(sol_s.y[:,1])*sol_s.y[:,0], np.sin(sol_s.y[:,1])*sol_s.y[:,0], color='b', linestyle='-', linewidth=2,
         label='Shooting')
plt.plot(np.cos(sol_c.y[:,1])*sol_c.y[:,0], np.sin(sol_c.y[:,1])*sol_c.y[:,0], color='r', linestyle='--', marker='.',
         label='Collocation')
plt.plot(np.cos(anom)*sol_s.y[0,0], np.sin(anom)*sol_s.y[0,0], color='k', linestyle='--')
plt.plot(np.cos(anom)*sol_s.y[-1,0], np.sin(anom)*sol_s.y[-1,0], color='k', linestyle='--')
plt.axis('equal')
plt.title('Low Thrust Orbit Raising')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_s.t, sol_s.y[:,0], color='b', linestyle='-', label='Radius')
plt.plot(sol_s.t, sol_s.y[:,1], color='r', linestyle='-', label='True Anomaly')
plt.plot(sol_s.t, sol_s.y[:,2], color='g', linestyle='-', label='Radial Velocity')
plt.plot(sol_s.t, sol_s.y[:,3], color='y', linestyle='-', label='Tangential Velocity')
plt.plot(sol_c.t, sol_c.y[:,0], color='b', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.y[:,1], color='r', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.y[:,2], color='g', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.y[:,3], color='y', linestyle='--', marker='.')
plt.xlabel('Time [nd]')
plt.ylabel('States [nd]')
plt.title('Low Thrust States')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_s.t, sol_s.dual[:,0], color='b', linestyle='-', label='Radius (costate)')
plt.plot(sol_s.t, sol_s.dual[:,1], color='r', linestyle='-', label='True Anomaly (costate)')
plt.plot(sol_s.t, sol_s.dual[:,2], color='g', linestyle='-', label='Radial Velocity (costate)')
plt.plot(sol_s.t, sol_s.dual[:,3], color='y', linestyle='-', label='Tangential Velocity (costate)')
plt.plot(sol_c.t, sol_c.dual[:,0], color='b', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.dual[:,1], color='r', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.dual[:,2], color='g', linestyle='--', marker='.')
plt.plot(sol_c.t, sol_c.dual[:,3], color='y', linestyle='--', marker='.')
plt.xlabel('Time [nd]')
plt.ylabel('Costates [nd]')
plt.title('High Thrust Costates')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_s.t, np.cos(sol_s.u), color='r', linestyle='-', label='Radial Thrust')
plt.plot(sol_s.t, np.sin(sol_s.u), color='b', linestyle='-', label='Tangential Thrust')
plt.plot(sol_c.t, np.cos(sol_c.u), color='r', linestyle='--', marker='.')
plt.plot(sol_c.t, np.sin(sol_c.u), color='b', linestyle='--', marker='.')
plt.xlabel('Time [nd]')
plt.ylabel('Control [nd]')
plt.title('Low Thrust Decomposed Control')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol_s.t, sol_s.u*180/np.pi, color='r', linestyle='-', label='Shooting')
plt.plot(sol_c.t, sol_c.u*180/np.pi, color='b', linestyle='--', marker='.', label='Collocation')
plt.xlabel('Time [nd]')
plt.ylabel('Control [degrees]')
plt.title('Low Thrust Control Angle')
plt.legend()
plt.grid(True)
plt.show()
