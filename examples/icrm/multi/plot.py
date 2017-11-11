import matplotlib
matplotlib.use('TkAgg')
import sys
import numpy as np
from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'data.dill'


def add_cylinder(r,f,p):
    ax = plt.gca()
    ax.set_zlabel('z(t)')
    # Cylinder
    x_center = -0.4
    y_center = 0.0
    radius = 0.1
    elevation = 0.0
    height = 0.1
    resolution = 20
    x = np.linspace(x_center-radius, x_center+radius, resolution)
    z = np.linspace(elevation, elevation+height, resolution)
    X, Z = np.meshgrid(x, z)

    Y = np.sqrt(radius**2 - (X - x_center)**2) + y_center # Pythagorean theorem

    ax.plot_surface(X, Y, Z, linewidth=0)
    ax.plot_surface(X, (2*y_center-Y), Z, linewidth=0)
    plt.axis('equal')


# plots = BelugaPlot('./data-3s3-202.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
plots = BelugaPlot(filename,default_sol=-1,default_step=-1, renderer='matplotlib')
#
# plots.add_plot().line('xbar','ybar',label='traj1')\
#                 .line('xbar2','ybar2',label='traj2')\
#                 .line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line3d('xbar','ybar','-zbar',label='traj1')\
                .line3d('xbar2','ybar2','-zbar2',label='traj2')\
                .xlabel('x(t)').ylabel('y(t)')\
                .postprocess(add_cylinder)

# plots.add_plot().line('t','xi11',label='xi11')\
#                 .line('t','xi21',label='xi21')\
#                 .line('t','xi31',label='xi31')
#                 .line('x2','y2',label='traj2')\
#                 .line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))

# plots.add_plot().line('t','z')\
#                 .xlabel('t (s)').ylabel('theta [deg]')\
#                 .title('Control history')
#
# plots.add_plot().line('t','z')\
#                 .line('t','z2')\
#                 .xlabel('t (s)').ylabel('theta [deg]')\
#                 .title('Control history')
#
# plots.add_plot().line('t','v2')\
#                 .xlabel('t (s)').ylabel('v2 [deg]')\
#                 .title('Control history')

#
# plots.add_plot().line('t','thr')\
#                 .xlabel('t (s)').ylabel('thr [nd]')\
#                 .title('Control history')
# plots.add_plot().line('t','sqrt((x - x2)**2 + (y - y2)**2)*(V*tfreal)')\
#                 .xlabel('t').ylabel('Separation (m)')\
#                 .title('Separation')


plots.render()
