import matplotlib as mpl
mpl.use('TkAgg')
import sys
import numpy as np
from beluga.visualization import BelugaPlot
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import functools as ft

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'data.dill'


def add_cylinder(r,f,p):
    ax = plt.gca()
    ax.set_zlabel('z(t) [km]')
    # Cylinder
    ax.invert_zaxis()

    x_center = -0.6*300*50/1e3
    y_center = 0.0*300*50/1e3
    radius = 0.1*300*50/1e3
    elevation = -0.1*300*50/1e3
    height = 0.1*300*50/1e3
    resolution = 20
    x = np.linspace(x_center-radius, x_center+radius, resolution)
    z = np.linspace(elevation, elevation+height, resolution)
    X, Z = np.meshgrid(x, z)

    Y = np.sqrt(radius**2 - (X - x_center)**2) + y_center # Pythagorean theorem

    ax.plot_surface(X, Y, Z, linewidth=0)
    ax.plot_surface(X, (2*y_center-Y), Z, linewidth=0)
    plt.axis('equal')

def add_cylinder2(r,f,p):
    ax = plt.gca()
    ax.set_zlabel('z(t) [km]')
    # Cylinder
    ax.invert_zaxis()

    x_center = -0.5
    z_center = -0.125
    radius = 0.1

    y0 = -0.2
    yf = 0.2
    resolution = 20
    x = np.linspace(x_center-radius, x_center+radius, resolution)
    y = np.linspace(y0, yf, resolution)
    X, Y = np.meshgrid(x, y)

    Z = np.sqrt(radius**2 - (X - x_center)**2) + z_center # Pythagorean theorem

    ax.plot_surface(X, Y, Z, linewidth=0)
    ax.plot_surface(X, Y, (2*z_center-Z), linewidth=0)
    plt.axis('equal')

def add_sphere(r,f,p):
    ax = plt.gca()
    xc = -0.6
    yc = 0.00
    zc = -0.15
    zc = -0.125
    rc = 0.075

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = rc*np.cos(u)*np.sin(v) + xc
    y = rc*np.sin(u)*np.sin(v) + yc
    z = rc*np.cos(v) + zc
    ax.plot_wireframe(x, y, z, color="r")
    ax.scatter([xc], [yc], [zc], color="g", s=100)
    plt.axis('equal')



def add_colorbar(r,f,p,lb,ub,label,cmap,pos='right',orient='vertical'):
    norm = mpl.colors.Normalize(vmin=lb, vmax=ub)

    fig = r._get_figure(f)
    # cax = fig.add_axes([0.125, 0.925, 0.775, 0.0725])

    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(pos, size="5%", pad=0.05)

    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, orientation=orient)

    #
    # cb1 = mpl.colorbar.ColorbarBase(plt.gca(), cmap=cmap,
    #                                 norm=norm,
    #                                 orientation='vertical')
    cb.set_label(label)

plots = BelugaPlot(filename,default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line3d('xbar','ybar','zbar',label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line3d('xbar2','ybar2','zbar2',label='Vehicle 2',style={'color':'green','lw':2.0})\
                .postprocess(add_cylinder2)

# plots.add_plot(colormap=cmx.viridis).line_series('xbar2','ybar2',style={'color':'red'})\
#                 .line_series('xbar','ybar')\
#                 .xlabel('x(t) [km]').ylabel('y(t) [km]')\
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))
#
plots.add_plot(colormap=cmx.viridis).line_series('xbar','zbar')\
                .line('rc*cos(2*pi*t/tf)+xc','rc*sin(2*pi*t/tf)+zc')\
                .postprocess(lambda r,f,p: plt.gca().invert_yaxis())
#
# plots.add_plot(colormap=cmx.viridis).line_series('xbar','ybar2-ybar')\
#                 .line_series('xbar','sqrt(minSeparation2)')\
#                 .postprocess(ft.partial(add_colorbar, lb=0.07, ub=0.05,label='yc',cmap=cmx.viridis_r))
#

# plots.add_plot(colormap=cmx.viridis).line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',label='Vehicle 2',style={'color':'red'})\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',label='Vehicle 1')\
#                 .xlabel('x(t) [km]').ylabel('y(t) [km]')\
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))
# .line('xc1*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','',label='c1')\
# .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',label='c2')\

# plots.add_plot().line('t','rc2')

# plots.add_plot(colormap=cmx.jet).line('t','psi2*180/pi',label='Vehicle 1',style='r')\
#                 .line('t','psi*180/pi')\
#                 .xlabel('t [s]').ylabel('x(t)')\
#                 .title('x') \

# plots.add_plot().line('xbar','ybar',label='traj1')\
#                 .line('xbar2','ybar2',label='traj2')\
#                 .line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))
#
# plots.add_plot().line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3','zbar*V*tfreal/1e3',label='traj1')\
#                 .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',label='traj2')\
#                 .xlabel('x(t) [km]').ylabel('y(t) [km]')\
#                 .postprocess(add_cylinder)

# # S1C =f'(xbar--0.3)'
# S2C =f'(xbar2--0.20)'
# # u1c =f'(1/(1+exp(-40*{S1C})))'
# u2c =f'(1/(1+exp(-10*{S2C})))'
# #
# S21 =f'(ybar2-ybar)'
# sLimit = f'({u2c}*0.05 + (1-{u2c})*1.0)'
# #
# plots.add_plot().line('xbar','distLimit')
#
# plots.add_plot().line('t','abar',label='xi11')\
#                 .line('t','abar2',label='xi21')\
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
