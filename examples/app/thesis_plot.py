import matplotlib as mpl
mpl.use('TkAgg')

from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill

import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable

from math import pi
import functools as ft
import numpy as np

output_dir = './plots/'
fontP = FontProperties()
fontP.set_size('small')

def save_pic(renderer, fig, p, suffix, tight=True, rasterized=False, dpi=300, format='eps'):
    fh = renderer._get_figure(fig)
    if tight:
        plt.tight_layout()
    if rasterized:
        # plt.gca().set_rasterized(True)
        plt.savefig(f'{output_dir}/app_{suffix}.{format}',rasterized=True, format='pdf',dpi=300)
    else:
        plt.savefig(f'{output_dir}/app_{suffix}.{format}')

def add_cylinder(r,f,p, params,color='k',opacity=0.4,invert=False):
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

    ax.plot_wireframe(X, Y, Z, linewidth=2.0,alpha=opacity,color=color)
    ax.plot_wireframe(X, (2*y_center-Y), Z, linewidth=2.0,alpha=opacity,color=color)
    # plt.axis('equal')

def add_colorbar3d(r,f,p,lb,ub,label,cmap,pos='right',orient='vertical'):
    norm = mpl.colors.Normalize(vmin=lb, vmax=ub)

    fig = r._get_figure(f)
    m = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
    m.set_array([])
    clb = plt.colorbar(m)
    clb.ax.set_ylabel(label)

def add_colorbar(r,f,p,lb,ub,label,cmap,pos='right',orient='vertical'):
    norm = mpl.colors.Normalize(vmin=lb, vmax=ub)

    fig = r._get_figure(f)
    # cax = fig.add_axes([0.125, 0.925, 0.775, 0.0725])

    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(pos, size="5%", pad=0.05)

    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, orientation=orient)
    cb.set_label(label)

# plots = BelugaPlot('data-qcpi-ulim-5v.dill',default_sol=-1,default_step=0, renderer='matplotlib')
plots = BelugaPlot('data-5v-nominal.dill',default_sol=-1,default_step=-1, renderer='matplotlib')


ds_psi3 = Dill('data-5v-psi3-189.dill')

V = 300
scale = V*50/1e3
Zone1 = np.array([-0.6, 0.0, 0.1])*scale
Zone2 = np.array([-0.2, 0.3, 0.2])*scale
Zone2b = np.array([-0.25, 0.225, 0.2])*scale
#
# plots.add_plot(colormap=cmx.Set1_r)\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 1',style={'lw':2.0})\
#                 .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 2',style={'lw':2.0})\
#                 .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 3',style={'lw':2.0})\
#                 .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 4',style={'lw':2.0})\
#                 .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 5',style={'lw':2.0})\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',label='No-Fly Zone',style={'color':'red'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='nominal_step1_xy'))
#
# plots.add_plot(colormap=cmx.Set1_r)\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',label='Vehicle 1',style={'lw':2.0})\
#                 .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',label='Vehicle 2',style={'lw':2.0})\
#                 .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',label='Vehicle 3',style={'lw':2.0})\
#                 .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',label='Vehicle 4',style={'lw':2.0})\
#                 .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',label='Vehicle 5',style={'lw':2.0})\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',label='No-Fly Zone',style={'color':'red'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='nominal_sol_xy'))

# Yc stuff
ds_yc = Dill('data-5v-yc-015.dill')

def v_yc_plot(r,f,p):
    out = ds_yc.get_solution()
    sol_set = out[-1]
    # from beluga.utils import keyboard
    # keyboard()
    v2 = np.array([sol.y[8,0] for sol in sol_set])*V
    v3 = np.array([sol.y[13,0] for sol in sol_set])*V
    v4 = np.array([sol.y[18,0] for sol in sol_set])*V
    v5 = np.array([sol.y[23,0] for sol in sol_set])*V
    yc = np.array([sol.aux['const']['yc'] for sol in sol_set])*scale
    v1 = np.ones_like(yc)*V

    plt.plot(yc, v1, label='$v_1$')
    plt.plot(yc, v2, label='$v_2$')
    plt.plot(yc, v3, label='$v_3$')
    plt.plot(yc, v4, label='$v_4$')
    plt.plot(yc, v5, label='$v_5$')
    plt.xlabel('$y_c$ [km]')
    plt.ylabel('$v$ [m/s]')
    plt.legend()
    plt.grid(True)

#
# plots.add_plot(colormap=cmx.viridis)\
#                 .line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_yc, label='No-Fly Zone',style={'color':'red'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(add_colorbar, lb=0.0, ub=2.25, label='$y_c$ [km]',cmap=cmx.viridis))\
#                 .postprocess(ft.partial(save_pic, suffix='yc_evol_xy'))
#
# plots.add_plot(colormap=cmx.Set1_r)\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_yc, label='Vehicle 1',style={'lw':2.0})\
#                 .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 2',style={'lw':2.0})\
#                 .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 3',style={'lw':2.0})\
#                 .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 4',style={'lw':2.0})\
#                 .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 5',style={'lw':2.0})\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_yc, label='No-Fly Zone',style={'color':'red'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='yc_xy'))
#
plots.add_plot().postprocess(v_yc_plot)\
                .postprocess(ft.partial(save_pic, suffix='yc_v'))

# # Psi3 stuff
# plots.add_plot(colormap=cmx.viridis)\
#                 .line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_psi3,style={'lw':2.0}, skip=5)\
#                 .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_psi3,style={'lw':2.0}, skip=5)\
#                 .line_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_psi3,style={'lw':2.0}, skip=5)\
#                 .line_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_psi3,style={'lw':2.0}, skip=5)\
#                 .line_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_psi3,style={'lw':2.0}, skip=5)\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_psi3, label='No-Fly Zone',style={'color':'red'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(add_colorbar, lb=15, ub=189, label='$\psi_3(T)$ [deg]',cmap=cmx.viridis))\
#                 .postprocess(ft.partial(save_pic, suffix='psi3_evol_xy'))

plots.render()
