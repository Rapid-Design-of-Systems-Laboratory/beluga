import matplotlib
matplotlib.use('TkAgg')
import matplotlib
import numpy as np
from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill

import matplotlib.pyplot as plt
import matplotlib.cm as cmx

output_dir = './plots/'
from matplotlib.font_manager import FontProperties
import functools as ft
fontP = FontProperties()
fontP.set_size('small')

def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/icrm_app_{suffix}.eps')

def add_cylinder(r,f,p, params,color='k',invert=False):
    ax = plt.gca()

    if invert:
        ax.invert_zaxis()
    ax.set_xlabel('$x(t)$ [km]')
    ax.set_ylabel('$y(t)$ [km]')
    ax.set_zlabel('$z(t)$ [km]')
    # Cylinder

    xc,yc,rc = params
    x_center = xc#-0.6*300*50/1e3
    y_center = yc#0.0*300*50/1e3
    radius = rc#0.1*300*50/1e3
    elevation = -0.1*300*50/1e3
    height = 0.1*300*50/1e3
    resolution = 20
    x = np.linspace(x_center-radius, x_center+radius, resolution)
    z = np.linspace(elevation, elevation+height, resolution)
    X, Z = np.meshgrid(x, z)

    Y = np.sqrt(radius**2 - (X - x_center)**2) + y_center # Pythagorean theorem

    ax.plot_wireframe(X, Y, Z, linewidth=1.0,alpha=0.4,color=color)
    ax.plot_wireframe(X, (2*y_center-Y), Z, linewidth=1.0,alpha=0.4,color=color)
    # plt.axis('equal')


one_path_ds = Dill('data-twoveh-s2-a.dill')
two_path_ds = Dill('data-twoveh-s2-b.dill')
plots = BelugaPlot('data-twoveh-unc.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

scale = 300*50/1e3
Zone1 = np.array([-0.6, 0.0, 0.1])*scale
Zone2 = np.array([-0.2, 0.25, 0.1])*scale

plots.add_plot().line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',label='Vehicle 1 - Unconstrained',style={'color':'blue','lw':2.0, 'ls':'dashed'})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',label='Vehicle 2 - Unconstrained',style={'color':'green','lw':2.0, 'ls':'dashed'})\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=one_path_ds,label='Zone 1',style={'color':'red'})\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=one_path_ds,label='Zone 2',style={'color':'yellow'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='s1_xy'))

plots.add_plot(mesh_size=200).line('t*tfreal','abar',datasource=one_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('t*tfreal','abar2',datasource=one_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .line('t*tfreal','abar',label='Vehicle 1 - Unconstrained',style={'color':'blue','lw':2.0, 'ls':'dashed'})\
                .line('t*tfreal','abar2',label='Vehicle 2 - Unconstrained',style={'color':'green','lw':2.0, 'ls':'dashed'})\
                .xlabel('$t$ [s]').ylabel('$\\bar{u}(t)$')\
                .postprocess(ft.partial(save_pic, suffix='s1_u'))

plots.add_plot().line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3','zbar*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3','zbar*V*tfreal/1e3',label='Vehicle 1 - Unconstrained',style={'color':'blue','lw':2.0, 'ls':'dashed'})\
                .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',label='Vehicle 2 - Unconstrained',style={'color':'green','lw':2.0, 'ls':'dashed'})\
                .postprocess(ft.partial(add_cylinder,params=Zone1,color='red'))\
                .postprocess(ft.partial(add_cylinder,params=Zone2,color='yellow',invert=True))\
                .postprocess(ft.partial(save_pic, suffix='s1_xyz'))
# .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=one_path_ds,label='Zone 1',style={'color':'red'})\
# .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=one_path_ds,label='Zone 2',style={'color':'yellow'})\

plots.add_plot().line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=two_path_ds,label='Zone 1',style={'color':'red'})\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=two_path_ds,label='Zone 2',style={'color':'yellow'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='s2_xy'))

plots.add_plot(mesh_size=200).line('t*tfreal','abar',datasource=two_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('t*tfreal','abar2',datasource=two_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .xlabel('$t$ [s]').ylabel('$\\bar{u}(t)$')\
                .postprocess(ft.partial(save_pic, suffix='s2_u'))

plots.add_plot().line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3','zbar*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .postprocess(ft.partial(add_cylinder,params=Zone1,color='red'))\
                .postprocess(ft.partial(add_cylinder,params=Zone2,color='yellow',invert=True))\
                .postprocess(ft.partial(save_pic, suffix='s2_xyz'))
plots.render()
