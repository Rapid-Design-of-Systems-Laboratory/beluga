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

def add_vehicle_labels(r,f,p):
    y0 = np.array([-0.05, 0.1, 0.15, -0.1,-0.15])*scale
    yf = np.array([0.0, 0.0, 0.0, -0.05,-0.05])*scale
    x0 = np.ones_like(y0)*-0.8*scale

    for i,(x,y) in enumerate(zip(x0,y0),1):
        plt.text(x-0.45,y+0.05,str(i))

# plots = BelugaPlot('data-qcpi-ulim-5v.dill',default_sol=-1,default_step=0, renderer='matplotlib')
plots = BelugaPlot('data-5v-nominal.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

V = 300
scale = V*50/1e3
Zone1 = np.array([-0.6, 0.0, 0.1])*scale
Zone1a = np.array([-0.6, 0.15, 0.1])*scale

def add_circle(r,f,p,pos,rad):
    ax = plt.gca()
    ax.add_patch(Circle(pos, radius=rad, fill=False, hatch='/', color='r'))

#
# plots.add_plot()\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 1',style={'lw':2.0})\
#                 .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 2',style={'lw':2.0})\
#                 .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 3',style={'lw':2.0})\
#                 .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 4',style={'lw':2.0})\
#                 .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',step=0,sol=-1,label='Vehicle 5',style={'lw':2.0})\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',label='No-Fly Zone',style={'color':'k'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='nominal_step1_xy'))
#
# plots.add_plot()\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',label='Vehicle 1',style={'lw':2.0})\
#                 .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',label='Vehicle 2',style={'lw':2.0})\
#                 .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',label='Vehicle 3',style={'lw':2.0})\
#                 .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',label='Vehicle 4',style={'lw':2.0})\
#                 .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',label='Vehicle 5',style={'lw':2.0})\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',label='No-Fly Zone',style={'color':'k'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='nominal_sol_xy'))
#
# # Yc stuff
# ds_yc = Dill('data-5v-yc-015.dill')
#
# def v_yc_plot(r,f,p):
#     out = ds_yc.get_solution()
#     sol_set = out[-1]
#     # from beluga.utils import keyboard
#     # keyboard()
#     v2 = np.array([sol.y[8,0] for sol in sol_set])*V
#     v3 = np.array([sol.y[13,0] for sol in sol_set])*V
#     v4 = np.array([sol.y[18,0] for sol in sol_set])*V
#     v5 = np.array([sol.y[23,0] for sol in sol_set])*V
#     yc = np.array([sol.aux['const']['yc'] for sol in sol_set])*scale
#     v1 = np.ones_like(yc)*V
#
#     plt.plot(yc, v1, label='$v_1$')
#     plt.plot(yc, v2, label='$v_2$')
#     plt.plot(yc, v3, label='$v_3$')
#     plt.plot(yc, v4, label='$v_4$')
#     plt.plot(yc, v5, label='$v_5$')
#     plt.xlabel('$y_c$ [km]')
#     plt.ylabel('$v$ [m/s]')
#     plt.legend()
#     plt.grid(True)
#
#
# plots.add_plot(colormap=cmx.viridis)\
#                 .line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_yc, style={'lw':2.0}, skip=5)\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_yc, label='No-Fly Zone',style={'color':'k'})\
#                 .postprocess(add_vehicle_labels)\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(add_colorbar, lb=0.0, ub=2.25, label='$y_c$ [km]',cmap=cmx.viridis))\
#                 .postprocess(ft.partial(save_pic, suffix='yc_evol_xy'))
#
# plots.add_plot()\
#                 .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_yc, label='Vehicle 1',style={'lw':2.0})\
#                 .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 2',style={'lw':2.0})\
#                 .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 3',style={'lw':2.0})\
#                 .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 4',style={'lw':2.0})\
#                 .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_yc, label='Vehicle 5',style={'lw':2.0})\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_yc, label='No-Fly Zone',style={'color':'k'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='yc_xy'))
#
# plots.add_plot().postprocess(v_yc_plot)\
#                 .postprocess(ft.partial(save_pic, suffix='yc_v'))
#
# plots.add_plot()\
#                 .line('t*tfreal','abar', datasource=ds_yc, label='Vehicle 1',style={'lw':2.0})\
#                 .line('t*tfreal','abar2',datasource=ds_yc, label='Vehicle 2',style={'lw':2.0})\
#                 .line('t*tfreal','abar3',datasource=ds_yc, label='Vehicle 3',style={'lw':2.0})\
#                 .line('t*tfreal','abar4',datasource=ds_yc, label='Vehicle 4',style={'lw':2.0})\
#                 .line('t*tfreal','abar5',datasource=ds_yc, label='Vehicle 5',style={'lw':2.0})\
#                 .xlabel('$t$ [s]').ylabel('$\\bar{u}(t)$')\
#                 .postprocess(ft.partial(save_pic, suffix='yc_u'))
#
# plots.add_plot()\
#                 .line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3', 'zbar*V*tfreal/1e3', datasource=ds_yc, label='Vehicle 1',style={'lw':2.0})\
#                 .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3', datasource=ds_yc, label='Vehicle 2',style={'lw':2.0})\
#                 .line3d('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3','zbar3*V*tfreal/1e3', datasource=ds_yc, label='Vehicle 3',style={'lw':2.0})\
#                 .line3d('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3','zbar4*V*tfreal/1e3', datasource=ds_yc, label='Vehicle 4',style={'lw':2.0})\
#                 .line3d('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3','zbar5*V*tfreal/1e3', datasource=ds_yc, label='Vehicle 5',style={'lw':2.0})\
#                 .postprocess(ft.partial(add_cylinder,params=Zone1a, opacity=0.2, invert=True))\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.gca().view_init(azim=-5,elev=10))\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='yc_xyz',format='pdf'))

# # Psi3 stuff
# ds_psi3 = Dill('data-5v-psi3-189.dill')
ds_psi3 = Dill('data-qcpi-5v-psi3-179.dill')
#
# def v_psi3_plot(r,f,p):
#     out = ds_psi3.get_solution()
#     sol_set = out[-1]
#     # from beluga.utils import keyboard
#     # keyboard()
#     v2 = np.array([sol.y[8,0] for sol in sol_set])*V
#     v3 = np.array([sol.y[13,0] for sol in sol_set])*V
#     v4 = np.array([sol.y[18,0] for sol in sol_set])*V
#     v5 = np.array([sol.y[23,0] for sol in sol_set])*V
#     psi3T = np.array([sol.y[12,-1] for sol in sol_set])*180/pi
#     v1 = np.ones_like(psi3T)*V
#
#     plt.plot(psi3T, v1, label='$v_1$')
#     plt.plot(psi3T, v2, label='$v_2$')
#     plt.plot(psi3T, v3, label='$v_3$')
#     plt.plot(psi3T, v4, label='$v_4$')
#     plt.plot(psi3T, v5, label='$v_5$')
#     plt.xlabel('$\\psi_3(T)$ [deg]')
#     plt.ylabel('$v$ [m/s]')
#     plt.legend()
#     plt.grid(True)
#
# plots.add_plot(colormap=cmx.viridis)\
#                 .line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_psi3,style={'lw':1.5}, skip=5)\
#                 .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_psi3,style={'lw':1.5}, skip=5)\
#                 .line_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_psi3,style={'lw':1.5}, skip=5)\
#                 .line_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_psi3,style={'lw':1.5}, skip=5)\
#                 .line_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_psi3,style={'lw':1.5}, skip=5)\
#                 .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_psi3, label='No-Fly Zone',style={'color':'k'})\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(add_vehicle_labels)\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(add_colorbar, lb=15, ub=189, label='$\psi_3(T)$ [deg]',cmap=cmx.viridis))\
#                 .postprocess(ft.partial(save_pic, suffix='psi3_evol_xy'))
#
# plots.add_plot(colormap=cmx.viridis,mesh_size=400)\
#                 .line3d_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3', 'zbar*V*tfreal/1e3', datasource=ds_psi3, skip=5, style={'lw':1.5})\
#                 .line3d_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3', datasource=ds_psi3, skip=5, style={'lw':1.5})\
#                 .line3d_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3','zbar3*V*tfreal/1e3', datasource=ds_psi3, skip=5, style={'lw':1.5})\
#                 .line3d_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3','zbar4*V*tfreal/1e3', datasource=ds_psi3, skip=5, style={'lw':1.5})\
#                 .line3d_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3','zbar5*V*tfreal/1e3', datasource=ds_psi3, skip=5, style={'lw':1.5})\
#                 .postprocess(ft.partial(add_cylinder,params=Zone1, opacity=0.2, invert=True))\
#                 .postprocess(ft.partial(add_colorbar3d, lb=15, ub=189, label='$\psi_3(T)$ [deg]',cmap=cmx.viridis))\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.gca().view_init(azim=50,elev=20))\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='psi3_evol_xyz',format='pdf'))
# #
# # plots.add_plot().line_series('t*tfreal','gam3*180/pi',  datasource=ds_psi3,style={'lw':1.5}, skip=5)\
# #                 .xlabel('$t$ [s]').ylabel('$\\gamma_3(t)$ [deg]')\
# #                 .postprocess(ft.partial(save_pic, suffix='psi3_gam'))
#
# plots.add_plot().postprocess(v_psi3_plot)\
#                 .postprocess(ft.partial(save_pic, suffix='psi3_v'))
#
# plots.add_plot()\
#                 .line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3', 'zbar*V*tfreal/1e3', datasource=ds_psi3, label='Vehicle 1',style={'lw':2.0})\
#                 .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3', datasource=ds_psi3, label='Vehicle 2',style={'lw':2.0})\
#                 .line3d('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3','zbar3*V*tfreal/1e3', datasource=ds_psi3, label='Vehicle 3',style={'lw':2.0})\
#                 .line3d('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3','zbar4*V*tfreal/1e3', datasource=ds_psi3, label='Vehicle 4',style={'lw':2.0})\
#                 .line3d('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3','zbar5*V*tfreal/1e3', datasource=ds_psi3, label='Vehicle 5',style={'lw':2.0})\
#                 .postprocess(ft.partial(add_cylinder,params=Zone1, opacity=0.2, invert=True))\
#                 .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
#                 .postprocess(lambda r,f,p: plt.gca().view_init(azim=50,elev=20))\
#                 .postprocess(lambda r,f,p: plt.axis('equal'))\
#                 .postprocess(ft.partial(save_pic, suffix='psi3_xyz',format='pdf'))
# # Psi3 stuff
ds_psi5 = Dill('data-qcpi-5v-psi3-179-psi5-125.dill')
def v_psi5_plot(r,f,p):
    out = ds_psi5.get_solution()
    sol_set = out[-1]
    # from beluga.utils import keyboard
    # keyboard()
    v2 = np.array([sol.y[8,0] for sol in sol_set])*V
    v3 = np.array([sol.y[13,0] for sol in sol_set])*V
    v4 = np.array([sol.y[18,0] for sol in sol_set])*V
    v5 = np.array([sol.y[23,0] for sol in sol_set])*V
    psi5T = np.array([sol.y[22,-1] for sol in sol_set])*180/pi
    v1 = np.ones_like(psi5T)*V

    plt.plot(psi5T, v1, label='$v_1$')
    plt.plot(psi5T, v2, label='$v_2$')
    plt.plot(psi5T, v3, label='$v_3$')
    plt.plot(psi5T, v4, label='$v_4$')
    plt.plot(psi5T, v5, label='$v_5$')
    plt.xlabel('$\\psi_3(T)$ [deg]')
    plt.ylabel('$v$ [m/s]')
    plt.legend()
    plt.grid(True)

plots.add_plot(colormap=cmx.viridis)\
                .line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_psi5,style={'lw':1.5}, skip=5)\
                .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_psi5,style={'lw':1.5}, skip=5)\
                .line_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_psi5,style={'lw':1.5}, skip=5)\
                .line_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_psi5,style={'lw':1.5}, skip=5)\
                .line_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_psi5,style={'lw':1.5}, skip=5)\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_psi5, label='No-Fly Zone',style={'color':'k'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(add_vehicle_labels)\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(add_colorbar, lb=45, ub=125, label='$\psi_5(T)$ [deg]',cmap=cmx.viridis))\
                .postprocess(ft.partial(save_pic, suffix='psi5_evol_xy'))

plots.add_plot(colormap=cmx.viridis,mesh_size=400)\
                .line3d_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3', 'zbar*V*tfreal/1e3', datasource=ds_psi5, skip=5, style={'lw':1.5})\
                .line3d_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3', datasource=ds_psi5, skip=5, style={'lw':1.5})\
                .line3d_series('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3','zbar3*V*tfreal/1e3', datasource=ds_psi5, skip=5, style={'lw':1.5})\
                .line3d_series('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3','zbar4*V*tfreal/1e3', datasource=ds_psi5, skip=5, style={'lw':1.5})\
                .line3d_series('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3','zbar5*V*tfreal/1e3', datasource=ds_psi5, skip=5, style={'lw':1.5})\
                .postprocess(ft.partial(add_cylinder,params=Zone1, opacity=0.2, invert=True))\
                .postprocess(ft.partial(add_colorbar3d, lb=45, ub=125, label='$\psi_5(T)$ [deg]',cmap=cmx.viridis))\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(lambda r,f,p: plt.gca().view_init(azim=-25,elev=35))\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='psi5_evol_xyz',format='pdf'))

plots.add_plot()\
                .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',  datasource=ds_psi5, label='Vehicle 1',style={'lw':2.0})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=ds_psi5, label='Vehicle 2',style={'lw':2.0})\
                .line('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3',datasource=ds_psi5, label='Vehicle 3',style={'lw':2.0})\
                .line('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3',datasource=ds_psi5, label='Vehicle 4',style={'lw':2.0})\
                .line('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3',datasource=ds_psi5, label='Vehicle 5',style={'lw':2.0})\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=ds_psi5, label='No-Fly Zone',style={'color':'k'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='psi5_xy'))

plots.add_plot()\
                .line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3', 'zbar*V*tfreal/1e3', datasource=ds_psi5, label='Vehicle 1',style={'lw':2.0})\
                .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3', datasource=ds_psi5, label='Vehicle 2',style={'lw':2.0})\
                .line3d('xbar3*V*tfreal/1e3','ybar3*V*tfreal/1e3','zbar3*V*tfreal/1e3', datasource=ds_psi5, label='Vehicle 3',style={'lw':2.0})\
                .line3d('xbar4*V*tfreal/1e3','ybar4*V*tfreal/1e3','zbar4*V*tfreal/1e3', datasource=ds_psi5, label='Vehicle 4',style={'lw':2.0})\
                .line3d('xbar5*V*tfreal/1e3','ybar5*V*tfreal/1e3','zbar5*V*tfreal/1e3', datasource=ds_psi5, label='Vehicle 5',style={'lw':2.0})\
                .postprocess(ft.partial(add_cylinder,params=Zone1, opacity=0.2, invert=True))\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(lambda r,f,p: plt.gca().view_init(azim=-35,elev=30))\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='psi5_xyz',format='pdf'))


plots.add_plot(colormap=cmx.viridis).line_series('t*tfreal','gam5*180/pi',  datasource=ds_psi5,style={'lw':1.5})\
                .xlabel('$t$ [s]').ylabel('$\\gamma_5(t)$ [deg]')\
                .postprocess(ft.partial(add_colorbar, lb=45, ub=125, label='$\psi_5(T)$ [deg]',cmap=cmx.viridis))\
                .postprocess(ft.partial(save_pic, suffix='psi5_gam'))

plots.add_plot().postprocess(v_psi5_plot)\
                .postprocess(ft.partial(save_pic, suffix='psi5_v'))

plots.render()
