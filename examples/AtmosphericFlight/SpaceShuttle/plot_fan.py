import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.gridspec import GridSpec
from beluga.utils import load

rad2deg = 180/3.141592653589793

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12
rcParams['mathtext.fontset'] = 'stix'

sols = load('space_shuttle_xi.json')[-1]


fig = plt.figure(figsize=(6.5, 5))
# fig.suptitle('Space Shuttle Reachability', fontsize=10)

# gs = GridSpec(1, 1, figure=fig)

ax11 = fig.add_subplot(111, projection='3d')

footprint_theta = []
footprint_phi = []
footprint_h = []
for sol in sols[::5]:
    h = sol.y[:, 0]/1000
    theta = sol.y[:, 1]*rad2deg
    phi = sol.y[:, 2]*rad2deg

    ax11.plot(theta, phi, h, color='C0')
    ax11.plot(theta, -phi, h, color='C0')

    footprint_theta.append(theta[-1])
    footprint_phi.append(phi[-1])
    footprint_h.append(h[-1])

ax11.plot(np.array(footprint_theta), np.array(footprint_phi), np.array(footprint_h), color='C1')
ax11.plot(np.array(footprint_theta), -np.array(footprint_phi), np.array(footprint_h), color='C1')


ax11.set_title('Space Shuttle Reachability')
ax11.set_xlabel(r'Downrange $\theta$ [deg]')
ax11.set_ylabel(r'Crossrange $\phi$ [deg]')
ax11.set_zlabel(r'Altitude $h$ [kft]')

plt.show()
