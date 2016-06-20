from matplotlib import pyplot as plt
from beluga.visualization import BelugaPlot2 as Bp2

file = 'cart132partial'

sols_def = range(0, 23)
set_def = 5
cols = 'autumn_r'

plt.close('all')

f1, axarr = plt.subplots(3, 4)

Bp2().plot_cont_step(ax=axarr[0, 0], x='x_s*x_n', y='y_s*y_n', title='Trajectory',
                     xlabel='$x$', ylabel='$y$', file=file, axis=[0, 470, -470/2, 470/2], sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[0, 1], x='t', y='p11_s*p11_n', title='Variance in x',
                     xlabel='$t [s]$', ylabel='$p_{11} [m^2]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[0, 2], x='t', y='p12_s*p12_n', title='',
                     xlabel='$t [s]$', ylabel='$p_{12} [m^2]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[0, 3], x='t', y='p13_s*p13_n', title='',
                     xlabel='$t [s]$', ylabel='$p_{13} [m rad]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[1, 2], x='t', y='p22_s*p22_n', title='Variance in y',
                     xlabel='$t [s]$', ylabel='$p_{22} [m^2]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[1, 3], x='t', y='p23_s*p23_n', title='',
                     xlabel='$t [s]$', ylabel='$p_{23} [m rad]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[2, 3], x='t', y='p33_s*p33_n', title=r'Variance in $\theta$',
                     xlabel='$t [s]$', ylabel='$p_{33} [rad^2]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[1, 0], x='t', y='Dt*sigv**2*sin(theta_n*theta_s)**2 + p13_n*p13_s*v*cos(theta_n*theta_s) + p23_n*p23_s*v*cos(theta_n*theta_s)',
                     title='', xlabel='', ylabel='', file=file, colormap='winter_r', sols=sols_def, step=set_def,)

Bp2().plot_cont_step(ax=axarr[1, 0], x='t', y='p12_n*p12_s*(x_n*x_s - xb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) + p22_n*p22_s*(y_n*y_s - yb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))',
                     title='', xlabel='', ylabel='', file=file, colormap='summer_r', sols=sols_def, step=set_def,)

Bp2().plot_cont_step(ax=axarr[1, 0], x='t',
                     y='Dt*sigv**2*sin(theta_n*theta_s)**2 + p13_n*p13_s*v*cos(theta_n*theta_s) + p23_n*p23_s*v*cos(theta_n*theta_s) + p12_n*p12_s*(x_n*x_s - xb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2)) + p22_n*p22_s*(y_n*y_s - yb)*(-p12_n*p12_s*(x_n*x_s - xb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2) - p22_n*p22_s*(y_n*y_s - yb)/sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))/(Dt*sigr**2*sqrt((x_n*x_s - xb)**2 + (y_n*y_s - yb)**2))',
                     title=r'Components of $d p_{22}/{dt}$', xlabel='$t [s]$', ylabel=r'$[m^2]$', file=file, colormap='autumn_r', sols=sols_def, step=set_def,)

Bp2().plot_cont_step(ax=axarr[1, 1], x='t', y='sqrt((x_n*x_s-xb)**2+(y_n*y_s-yb)**2)', title=r'Measurment',
                     xlabel='$t [s]$', ylabel=r'$\rho [m]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[2, 0], x='t', y='u_max*sin(w)', title=r'Control Law',
                     xlabel='$t [s]$', ylabel=r'$d\theta/{dt} [rad/s]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[2, 1], x='t', y='theta_n*theta_s*180/3.141594', title=r'Control Law',
                     xlabel='$t [s]$', ylabel=r'$\theta [rad]$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr[2, 2], x='t', y='lamTHETA_N', title=r'Costate for $\theta$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{\theta}$', file=file, sols=sols_def, step=set_def, colormap=cols)

f1.subplots_adjust(hspace=0.35, wspace=0.35)
# f.tight_layout()

f2, axarr2 = plt.subplots(3, 4)

Bp2().plot_cont_step(ax=axarr2[0, 0], x='t', y='lamX_N', title=r'Costate for $x$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{x}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[1, 0], x='t', y='lamY_N', title=r'Costate for $y$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{y}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[2, 0], x='t', y='lamTHETA_N', title=r'Costate for $\theta$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{\theta}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[0, 1], x='t', y='lamP11_N', title=r'Costate for $p_{11}$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{p_{11}}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[0, 2], x='t', y='lamP12_N', title=r'Costate for $p_{12}$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{p_{12}}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[0, 3], x='t', y='lamP13_N', title=r'Costate for $p_{13}$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{p_{13}}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[1, 2], x='t', y='lamP22_N', title=r'Costate for $p_{22}$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{p_{12}}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[1, 3], x='t', y='lamP23_N', title=r'Costate for $p_{23}$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{p_{23}}$', file=file, sols=sols_def, step=set_def, colormap=cols)

Bp2().plot_cont_step(ax=axarr2[2, 3], x='t', y='lamP33_N', title=r'Costate for $p_{33}$',
                     xlabel='$t [s]$', ylabel=r'$\lambda_{p_{33}}$', file=file, sols=sols_def, step=set_def, colormap=cols)

f2.subplots_adjust(hspace=0.35, wspace=0.35)

plt.show()




