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
        plt.savefig(f'{output_dir}/icrm_app_{suffix}.{format}',rasterized=True, format='pdf',dpi=300)
    else:
        plt.savefig(f'{output_dir}/icrm_app_{suffix}.{format}')

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

    #
    # cb1 = mpl.colorbar.ColorbarBase(plt.gca(), cmap=cmap,
    #                                 norm=norm,
    #                                 orientation='vertical')
    cb.set_label(label)

one_path_ds = Dill('data-twoveh-s2-a.dill')
plots = BelugaPlot('data-twoveh-unc.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

scale = 300*50/1e3
Zone1 = np.array([-0.6, 0.0, 0.1])*scale
Zone2 = np.array([-0.2, 0.3, 0.2])*scale
Zone2b = np.array([-0.25, 0.225, 0.2])*scale

def add_vehicle_labels(r,f,p):
    y0 = np.array([0.0, 0.1])*scale
    x0 = np.ones_like(y0)*-0.8*scale

    for i,(x,y) in enumerate(zip(x0,y0),1):
        plt.text(x-0.45,y+0.125,'V-'+str(i),color='b')
        plt.plot(x,y,color='r', lw=0.0, marker='>', ms=4, mew=3)


plots.add_plot().line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',label='Vehicle 1 - Unconstrained',style={'color':'blue','lw':2.0, 'ls':'dashed'})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',label='Vehicle 2 - Unconstrained',style={'color':'green','lw':2.0, 'ls':'dashed'})\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=one_path_ds,label='Zone 1',style={'color':'red', 'ls':'--'})\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=one_path_ds,label='Zone 2',style={'color':'black', 'ls':'--'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(add_vehicle_labels)\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='s1_xy'))

plots.add_plot().line('t*tfreal','abar',datasource=one_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
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
                .postprocess(ft.partial(add_cylinder,params=Zone2,color='black',invert=True))\
                .postprocess(ft.partial(save_pic, suffix='s1_xyz', rasterized=True, format='pdf'))


# Terminal heading - vehicle 2
psi2f_path_ds = Dill('data-twoveh-s2-a-psi2-110.dill')
def add_psi2_psi1_v_plot(renderer, fig, plot):
    solution = psi2f_path_ds.get_solution()
    sol_set = solution[-1]
    V = sol_set[0].aux['const']['V']

    vbar = np.array([sol.y[8,0] for sol in sol_set])
    psi2f = np.array([sol.y[7,-1] for sol in sol_set])
    psi10 = np.array([sol.y[3,0] for sol in sol_set])

    ax = plt.gca()
    ax.plot(psi2f*180/pi, vbar*V, lw=2.0, color='b')
    ax.set_xlabel('$\\psi_2(T)$ [deg]')
    ax.set_ylabel('$v_2$ [m/s]', color='b')
    ax.tick_params('y', colors='b')

    ax2 = ax.twinx()
    ax2.plot(psi2f*180/pi, psi10*180/pi, lw=2.0, color='r')
    ax2.set_ylabel('$\\psi_1(0)$ [deg]', color='r')
    ax2.tick_params('y', colors='r')

#     plt.grid(True)
plots.add_plot(colormap=cmx.jet_r)\
                .line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=psi2f_path_ds,style={'lw':2.0},skip=5)\
                .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=psi2f_path_ds,style={'lw':2.0},skip=5)\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=psi2f_path_ds,label='Zone 1',style={'color':'red', 'ls':'--'})\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=psi2f_path_ds,label='Zone 2',style={'color':'black', 'ls':'--'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(add_vehicle_labels)\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(add_colorbar,label='$\\psi_2(T)$ [deg]',lb=-15, ub=-109,cmap=cmx.jet))\
                .postprocess(ft.partial(save_pic, suffix='s1_psi2f_xy'))

plots.add_plot(colormap=cmx.jet_r).line_series('t*tfreal','psi2*180/pi',datasource=psi2f_path_ds, skip=1)\
                .xlabel('$t$ [s]').ylabel('$\\psi_2(t)$ [deg]')\
                .postprocess(ft.partial(save_pic, suffix='s1_psi2f_psi2'))

plots.add_plot(colormap=cmx.jet_r).line_series('t*tfreal','abar2',datasource=psi2f_path_ds, skip=1)\
                .xlabel('$t$ [s]').ylabel('$\\bar{u}_2(t)$')\
                .postprocess(ft.partial(add_colorbar,label='$\\psi_2(T)$ [deg]',lb=-15, ub=-109,cmap=cmx.jet))\
                .postprocess(ft.partial(save_pic, suffix='s1_psi2f_u2'))


plots.add_plot().postprocess(add_psi2_psi1_v_plot) \
                .postprocess(ft.partial(save_pic, suffix='s1_psi2f_psi1_v'))

plots.add_plot(colormap=cmx.jet_r) \
                .line3d_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',datasource=psi2f_path_ds,style={'lw':2.0},skip=10)\
                .postprocess(ft.partial(add_cylinder,params=Zone1,color='red',opacity=0.20))\
                .postprocess(ft.partial(add_cylinder,params=Zone2,color='black',opacity=0.20,invert=True))\
                .postprocess(lambda r,f,p: plt.gca().view_init(elev=20, azim=-48))\
                .postprocess(ft.partial(add_colorbar3d,label='$\\psi_2(T)$ [deg]',lb=-15, ub=-109,cmap=cmx.jet,pos='bottom',orient='horizontal'))\
                .postprocess(ft.partial(save_pic, suffix='s1_psi2f_xyz', rasterized=True, format='pdf'))

# # Both constraints active
two_path_ds = Dill('data-twoveh-s2-b.dill')
plots.add_plot().line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=two_path_ds,label='Zone 1',style={'color':'red', 'ls':'--'})\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=two_path_ds,label='Zone 2',style={'color':'black', 'ls':'--'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(add_vehicle_labels)\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(save_pic, suffix='s2_xy'))

plots.add_plot(mesh_size=200).line('t*tfreal','abar',datasource=two_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('t*tfreal','abar2',datasource=two_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .xlabel('$t$ [s]').ylabel('$\\bar{u}(t)$')\
                .postprocess(ft.partial(save_pic, suffix='s2_u'))

plots.add_plot().line3d('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3','zbar*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',datasource=two_path_ds,label='Vehicle 2',style={'color':'green','lw':2.0})\
                .postprocess(ft.partial(add_cylinder,params=Zone1,color='red'))\
                .postprocess(ft.partial(add_cylinder,params=Zone2b,color='black',invert=True))\
                .postprocess(ft.partial(save_pic, suffix='s2_xyz', rasterized=True, format='pdf'))

two_path_middle_ds = Dill('data-twoveh-s2-yc02.dill')
Zone2c = np.array([-0.25, 0.2, 0.2])*scale
def add_zone2_plot(renderer, fig, plot):
    solution = two_path_middle_ds.get_solution()
    sol_set = solution[0]

    V = sol_set[0].aux['const']['V']
    tfreal = sol_set[0].aux['const']['tfreal']
    yc2 = np.array([sol.aux['const']['yc2'] for sol in sol_set])*V*tfreal

    vbar2 = np.array([sol.y[8,0] for sol in sol_set])*V

    ax = plt.gca()
    ax.plot(yc2/1e3, vbar2, lw=2.0, color='b')
    ax.set_xlabel('$y_{c2}$ [km]')
    ax.set_ylabel('$v_2$ [m/s]')
    # ax.tick_params('y', colors='b')

    # ax2 = ax.twinx()
    # ax2.plot(psi2f*180/pi, psi10*180/pi, lw=2.0, color='r')
    # ax2.set_ylabel('$\\psi_1(0)$ [deg]', color='r')
    # ax2.tick_params('y', colors='r')

    plt.grid(True)


plots.add_plot(colormap=cmx.jet_r).line_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=two_path_middle_ds,style={'lw':2.0},step=0,skip=5)\
                .line_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=two_path_middle_ds,style={'lw':2.0},step=0,skip=4)\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=two_path_middle_ds,label='Zone 1',style={'color':'red', 'ls':'--'})\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',datasource=two_path_middle_ds,label='Zone 2',style={'color':'black', 'ls':'--'})\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                .postprocess(add_vehicle_labels)\
                .postprocess(lambda r,f,p: plt.axis('equal'))\
                .postprocess(ft.partial(add_colorbar,label='$y_{c2}$ [km]',lb=4.5, ub=3.375,cmap=cmx.jet))\
                .postprocess(ft.partial(save_pic, suffix='s2_zone2_xy'))

plots.add_plot(colormap=cmx.jet_r) \
                .line3d_series('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3','zbar*V*tfreal/1e3',datasource=two_path_middle_ds,style={'lw':2.0},step=0,skip=5)\
                .line3d_series('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',datasource=two_path_middle_ds,style={'lw':2.0},step=0,skip=5)\
                .postprocess(ft.partial(add_cylinder,params=Zone1,color='red',opacity=0.20))\
                .postprocess(ft.partial(add_cylinder,params=Zone2c,color='black',opacity=0.20,invert=True))\
                .postprocess(lambda r,f,p: plt.gca().view_init(elev=20, azim=-48))\
                .postprocess(ft.partial(add_colorbar3d,label='$\\psi_2(T)$ [deg]',lb=-15, ub=-109,cmap=cmx.jet,pos='bottom',orient='horizontal'))\
                .postprocess(ft.partial(save_pic, suffix='s2_zone2_xyz', rasterized=True, format='pdf'))

plots.add_plot().postprocess(add_zone2_plot)\
                .postprocess(ft.partial(save_pic, suffix='s2_zone2_v'))


plots.add_plot(colormap=cmx.jet_r).line_series('t*tfreal','abar2',datasource=two_path_middle_ds,style={'lw':2.0}, step=0, skip=4)\
                .xlabel('$t$ [s]').ylabel('$\\bar{u}_2(t)$')\
                .postprocess(ft.partial(add_colorbar,label='$y_{c2}$ [km]',lb=4.5, ub=3.375,cmap=cmx.jet))\
                .postprocess(ft.partial(save_pic, suffix='s2_zone2_u2'))

plots.render()
