from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

bfr_diameter = 9

Hscale = 8.44e3

bfr_thrust0_sea = 1.993e6*31
bfr_thrust0_vac = 2.295e6*31
bfr_thrust1_sea = 1.993e6*7
bfr_thrust1_vac = 2.295e6*7

bfr_mass0 = 4400e3
bfr_mass0f = 1335e3
bfr_mass1 = 1335e3
bfr_mass1f = 85e3

bfr_massflow0 = -615.8468*31
bfr_massflow1 = -615.8468*7

data = load('data.beluga')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.y[:, 0]/1000, sol.y[:, 1]/1000)
plt.xlabel('Downrange [km]')
plt.ylabel('Altitude [km]')
plt.title('Time Optimal Launch of a BFR Trajectory')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:, 2]/1000, label='Horizontal Velocity')
plt.plot(sol.t, sol.y[:, 3]/1000, label='Vertical Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [km/s]')
plt.title('Velocities of a BFR')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.u*180/np.pi)
plt.xlabel('Time [s]')
plt.ylabel('Control [degrees]')
plt.title('BFR Steering Angle')
plt.grid(True)

plt.figure()
plt.plot(sol.t, sol.y[:, 4])
plt.plot([sol.t[0], sol.t[-1]], [bfr_mass0, bfr_mass0], linestyle='--', color='k')
plt.plot([sol.t[0], sol.t[-1]], [bfr_mass0f, bfr_mass0f], linestyle='--', color='k')
plt.plot([sol.t[0], sol.t[-1]], [bfr_mass1f, bfr_mass1f], linestyle='--', color='k')
plt.xlabel('Time [s]')
plt.ylabel('Mass [kg]')
plt.title('BFR Mass')
plt.grid(True)


engine0 = bfr_thrust0_sea*np.exp(-sol.y[:, 1]/Hscale) + bfr_thrust0_vac*(1-np.exp(-sol.y[:, 1]/Hscale))
engine1 = bfr_thrust1_sea*np.exp(-sol.y[:, 1]/Hscale) + bfr_thrust1_vac*(1-np.exp(-sol.y[:, 1]/Hscale))
stage_tol = sol.k[0]
Thrust = engine0/(1+np.exp((bfr_mass0f - sol.y[:, 4])/stage_tol)) \
         + engine1/(1+np.exp((sol.y[:, 4] - bfr_mass0f)/stage_tol))

plt.figure()
plt.plot(sol.t, Thrust/1e6)
plt.xlabel('Time [s]')
plt.ylabel('Thrust [MN]')
plt.title('BFR Thrust')
plt.grid(True)
plt.show()
