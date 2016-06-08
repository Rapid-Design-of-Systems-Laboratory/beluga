from matplotlib import pyplot as plt
from beluga.visualization import BelugaPlot2 as BP2

plt.close('all')

out = BP2.load_dill('cart120')

x = BP2.retrieve('x_s*x_n', out, step=-1, sol=-1)
y = BP2.retrieve('y_s*y_n', out, step=-1, sol=-1)

plt.plot(x, y, color='red', label='Trajectory')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory')

plt.legend()

BP2().plot_cont_step(x='x_s*x_n', y='y_s*y_n', file='cart120', sols=range(0,39,2), axis='tight')

BP2().ez_plot_dill(x='x_s*x_n', y='y_s*y_n', file='cart120', step=-1, sol=-1, axis='equal', title='Trajectory', xlabel=r'$x$', ylabel=r'$y$', color='red')

BP2().ez_plot_dill(x='t', y='u_max*sin(w)', file='cart120', step=0, sol=0, title='Control Law', ylabel=r'$\dot{\theta}$')

ax1 = plt.subplot(2,1,1)
BP2().plot_cont_step(x='x_s*x_n', y='y_s*y_n', file='cart120', sols=range(0,30,2), ax=ax1)

ax2 = plt.subplot(2,1,2)
BP2().ez_plot_dill(x='x_s*x_n', y='y_s*y_n', file='cart120', step=-1, sol=-1, ax=ax2, title='Trajectory', xlabel=r'$x$', ylabel=r'$y$', color='red')

# f1, axarr = plt.subplots(3, 4)
#
# BP2().plot_cont_step(ax=axarr[0, 0], x='x_s*x_n', y='y_s*y_n', title='Trajectory',
#                      xlabel='$x$', ylabel='$y$', file='cart120', axis=[0, 250, -125, 125])
#
# BP2().plot_cont_step(ax=axarr[0, 1], x='t', y='p11_s*p11_n', title='Variance in x',
#                      xlabel='$t [s]$', ylabel='$p_{11} [m^2]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[0, 2], x='t', y='p12_s*p12_n', title='',
#                      xlabel='$t [s]$', ylabel='$p_{12} [m^2]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[0, 3], x='t', y='p13_s*p13_n', title='',
#                      xlabel='$t [s]$', ylabel='$p_{13} [m rad]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[1, 2], x='t', y='p22_s*p22_n', title='Variance in y',
#                      xlabel='$t [s]$', ylabel='$p_{12} [m^2]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[1, 3], x='t', y='p23_s*p23_n', title='',
#                      xlabel='$t [s]$', ylabel='$p_{23} [m rad]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[2, 3], x='t', y='p33_s*p33_n', title=r'Variance in $\theta$',
#                      xlabel='$t [s]$', ylabel='$p_{33} [rad^2]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[1, 0], x='t', y='Dt*sigv**2*sin(theta_n*theta_s)**2 + p13_n*p13_s*v*cos(theta_n*theta_s) + p23_n*p23_s*v*cos(theta_n*theta_s)',
#                      title='', xlabel='', ylabel='', file='cart120', colormap='winter_r')
#
# BP2().plot_cont_step(ax=axarr[1, 0], x='t', y='p12_n*p12_s*(x_n*x_s - xb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) + p22_n*p22_s*(y_n*y_s - yb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))',
#                      title='', xlabel='', ylabel='', file='cart120', colormap='summer_r')
#
# BP2().plot_cont_step(ax=axarr[1, 0], x='t',
#                      y='Dt*sigv**2*sin(theta_n*theta_s)**2 + p13_n*p13_s*v*cos(theta_n*theta_s) + p23_n*p23_s*v*cos(theta_n*theta_s) + p12_n*p12_s*(x_n*x_s - xb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) + p22_n*p22_s*(y_n*y_s - yb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))',
#                      title=r'Components of $d p_{22}/{dt}$', xlabel='$t [s]$', ylabel=r'$[m^2]$', file='cart120', colormap='autumn_r')
#
# BP2().plot_cont_step(ax=axarr[1, 1], x='t', y='sqrt((x_n*x_s-xb)**2+(y_n*y_s-yb)**2)', title=r'Measurment',
#                      xlabel='$t [s]$', ylabel=r'$\rho [m]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[2, 0], x='t', y='u_max*sin(w)', title=r'Control Law',
#                      xlabel='$t [s]$', ylabel=r'$d\theta/{dt} [rad/s]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[2, 1], x='t', y='theta_n*theta_s*180/3.141594', title=r'Control Law',
#                      xlabel='$t [s]$', ylabel=r'$\theta [rad]$', file='cart120')
#
# BP2().plot_cont_step(ax=axarr[2, 2], x='t', y='lamTHETA_N', title=r'Costate for $\theta$',
#                      xlabel='$t [s]$', ylabel=r'$\lambda_{\theta}$', file='cart120')
#
# f1.subplots_adjust(hspace=0.35, wspace=0.35)
# f.tight_layout()

plt.show()




