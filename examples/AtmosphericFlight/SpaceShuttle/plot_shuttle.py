import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.gridspec import GridSpec
from beluga.utils import load

rad2deg = 180/3.141592653589793

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 8
rcParams['mathtext.fontset'] = 'stix'

data = load('space_shuttle.beluga')
sol = data['solutions'][-1][-1]

t = sol.t

h = sol.y[:, 0]/1000
theta = sol.y[:, 1]*rad2deg
phi = sol.y[:, 2]*rad2deg
v = sol.y[:, 3]/1000
gam = sol.y[:, 4]*rad2deg
psi = sol.y[:, 5]*rad2deg

alpha = sol.u[:, 0]*rad2deg
bank = sol.u[:, 1]*rad2deg

fig = plt.figure(figsize=(6.5, 5))
fig.suptitle('Space Shuttle Maximum Crossrange', fontsize=10)

gs = GridSpec(4, 2, figure=fig)

ax11 = fig.add_subplot(gs[:2, 0], projection='3d')
ax11.plot(theta, phi, h)
ax11.set_title('Trajectory')
ax11.set_xlabel(r'Downrange $\theta$ [deg]')
ax11.set_ylabel(r'Crossrange $\phi$ [deg]')
ax11.set_zlabel(r'Altitude $h$ [kft]')

ax12 = fig.add_subplot(gs[:2, 1])
ax12.plot(v, h)
ax12.set_title('h-v Diagram')
ax12.set_xlabel(r'Velocity $v$ [kft/s]')
ax12.set_ylabel(r'Altitude $h$ [kft]')

ax21 = fig.add_subplot(gs[2, 0])
ax21.plot(t, gam, label='FPA')
ax21.set_title('Flight Path Angle')
ax21.set_xlabel(r'Time $t$ [s]')
ax21.set_ylabel(r'FPA $\gamma$ [deg]')

ax22 = fig.add_subplot(gs[2, 1])
ax22.plot(t, psi, label='Heading')
ax22.set_title('Heading Angle')
ax22.set_xlabel(r'Time $t$ [s]')
ax22.set_ylabel(r'Heading $\psi$ [deg]')

ax23 = fig.add_subplot(gs[3, 0])
ax23.plot(t, alpha, label='AoA')
ax23.set_title('Angle of Attack')
ax23.set_xlabel(r'Time $t$ [s]')
ax23.set_ylabel(r'AoA $\alpha$ [deg]')

ax24 = fig.add_subplot(gs[3, 1])
ax24.plot(t, bank, label='Bank')
ax24.set_title('Bank Angle')
ax24.set_xlabel(r'Time $t$ [s]')
ax24.set_ylabel(r'Bank $\beta$ [deg]')

fig.subplots_adjust(0.12, 0.09, 0.95, 0.9, 0.51, 1)

plt.show()
