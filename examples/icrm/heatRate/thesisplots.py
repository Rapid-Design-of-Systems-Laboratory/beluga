from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill, GPOPS
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from matplotlib2tikz import save as tikz_save
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker

import functools as ft
import numpy as np
from math import sqrt, pi
import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'x-large'
mpl.rcParams['ytick.labelsize'] = 'x-large'

output_dir = './plots/'
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')
def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig)
    plt.tight_layout()
    # tikz_save(f'{output_dir}/heatRate_{suffix}.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
    plt.savefig(f'{output_dir}/heatRate_{suffix}.eps')

def analytical_sol_xv(renderer, fig, p):

    save_pic(renderer,fig,p,'icrm_traj')

def analytical_sol_u(renderer, fig, p):

    save_pic(renderer,fig,p,'icrm_u')


def add_colorbar(r,f,p,lb,ub,label,cmap,pos='right',orient='vertical',sci_ticks=False):
    norm = mpl.colors.Normalize(vmin=lb, vmax=ub)

    fig = r._get_figure(f)
    # cax = fig.add_axes([0.125, 0.925, 0.775, 0.0725])

    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(pos, size="5%", pad=0.05)
    if sci_ticks:
        def fmt(x, pos):
            return '{:.0e}'.format(x)
            # a, b = '{:.0e}'.format(x).split('e')
            # b = int(b)
            # return r'${} \times 10^{{{}}}$'.format(a, b)
        formatter = ticker.FuncFormatter(fmt)
    else:
        formatter = None
    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, orientation=orient, format=formatter)
    cb.set_label(label)

plots = BelugaPlot('./data_fpa60.dill',default_sol=-1,default_step=-1)
mpbvp_ds = Dill('../../mpbvp/planarHypersonicWithHeatRate/data_1200.dill')
const_ds = Dill('./data_1200_5k_1deg_ep6.dill')
qdot_ds = Dill('./data_1200_ep4.dill')

# Remove \addlegendimage lines from tex file for dot plots

plots.add_plot(colormap=cmx.viridis_r).line_series('theta*re/1000','h/1000',step=1,skip=0,style={'lw':2.0}) \
                .xlabel('Downrange [km]').ylabel('$h$ [km]')\
                .postprocess(ft.partial(save_pic, suffix='evol1_htheta'))

plots.add_plot(colormap=cmx.viridis_r).line_series('t','gam*180/3.14159',step=1,skip=0,style={'lw':2.0}) \
                .xlabel('$t$ [s]').ylabel('$\\gamma$ [deg]')\
                .postprocess(ft.partial(save_pic, suffix='evol1_fpa'))

rho = 'rho0*exp(-h/H)'
Cl  = '(1.5658*alfa + -0.0000)'
Cd  = '(1.6537*alfa**2 + 0.0612)'

D   = '(0.5*'+rho+'*v**2*'+Cd+'*Aref)'
L   = '(0.5*'+rho+'*v**2*'+Cl+'*Aref)'
#
# plots.add_plot(colormap=cmx.jet_r).line_series('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000',datasource=mpbvp_ds,step=-1,skip=2) \
#                 .xlabel('$t$ [s]').ylabel('$\\dot{q}$ [W/cm$^2$]') \
#                 .postprocess(ft.partial(save_pic, suffix='mpbvp_evol_qdot')) \
#
# plots.add_plot(colormap=cmx.jet_r).line_series('v/1000','h/1000',datasource=mpbvp_ds,step=-1,skip=2) \
#                 .xlabel('$v$ [km/s]').ylabel('$h$ [km]') \
#                 .postprocess(ft.partial(save_pic, suffix='mpbvp_evol_hv'))
#
# # # Continuation on Qdotmax
# plots.add_plot(colormap=cmx.jet_r).line_series('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000',datasource=qdot_ds,step=-1,skip=0) \
#                 .xlabel('$t$ [s]').ylabel('$\\dot{q}$ [W/cm$^2$]') \
#                 .postprocess(ft.partial(add_colorbar, lb=1200, ub=2500, label='$\dot{Q}_{max}$ [W/cm$^2$]',cmap=cmx.jet)) \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_evol1_qdot'))
#
# plots.add_plot(colormap=cmx.jet_r).line_series('v/1000','h/1000',datasource=qdot_ds,step=-1,skip=0) \
#                 .xlabel('$v$ [km/s]').ylabel('$h$ [km]') \
#                 .postprocess(ft.partial(add_colorbar, lb=1200, ub=2500, label='$\dot{Q}_{max}$ [W/cm$^2$]',cmap=cmx.jet)) \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_evol1_hv'))
#
# Continuaton in epsilon
# plots.add_plot(colormap=cmx.jet_r).line_series('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000',datasource=const_ds,start=20, end=-1, step=-1,skip=0) \
#                 .xlabel('$t$ [s]').ylabel('$\\dot{q}$ [W/cm$^2$]') \
#                 .postprocess(ft.partial(add_colorbar, lb=1e-4, ub=1e-6, label='$\epsilon$',cmap=cmx.jet, sci_ticks=True)) \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_evol2_qdot'))
#
# plots.add_plot(colormap=cmx.jet_r).line_series('v/1000','h/1000',datasource=const_ds, start=20, end=-1, step=-1,skip=0) \
#                 .xlabel('$v$ [km/s]').ylabel('$h$ [km]') \
#                 .postprocess(ft.partial(add_colorbar, lb=1e-4, ub=1e-6, label='$\epsilon$',cmap=cmx.jet, sci_ticks=True)) \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_evol2_hv'))
#
# plots.add_plot()\
#                 .line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000', datasource=mpbvp_ds, label='MPBVP', style={'lw':2.5}) \
#                 .line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000', datasource=const_ds, label='ICRM', style={'lw':0.0,'marker':'o'}) \
#                 .xlabel('$t$ [s]').ylabel('$\\dot{q}$ [W/cm$^2$]') \
#                 .postprocess(ft.partial(save_pic, suffix='mpbvp_icrm_qdot'))
#
# plots.add_plot()\
#                 .line('v/1000','h/1000', datasource=mpbvp_ds, label='MPBVP', style={'lw':2.5}) \
#                 .line('v/1000','h/1000', datasource=const_ds, label='ICRM', style={'lw':0.0,'marker':'o'}) \
#                 .xlabel('$v$ [km/s]').ylabel('$h$ [km]') \
#                 .postprocess(ft.partial(save_pic, suffix='mpbvp_icrm_hv'))
#
# plots.add_plot().line('t','alfa*180/3.14', datasource=const_ds, style={'lw':2.0}) \
#                 .xlabel('$t$ [s]').ylabel('$\\alpha$ [deg]') \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_alpha'))
#
# # plots.add_plot().line('theta*180/3.14','h/1000')                    \
# #                 .xlabel('Downrange (km)').ylabel('h (km)')      \
# #                 .title('Altitude vs. Downrange')
# #
# # plots.add_plot().line('t','alfa*180/3.14')                    \
# #                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
# #                 .title('Angle of attack vs. Time')
# #
# #
# # plots.add_plot().line('t','lamV')                    \
# #                 .xlabel('t (s)').ylabel('lamV')      \
# #                 .title('lamV vs. Time')
#
# # rho = 'rho0*exp(-h/H)'
# # Cl  = '(1.5658*alfa + -0.0000)'
# # Cd  = '(1.6537*alfa**2 + 0.0612)'
# #
# # D   = '(0.5*'+rho+'*v**2*'+Cd+'*Aref)'
# # L   = '(0.5*'+rho+'*v**2*'+Cl+'*Aref)'
# #
# # plots.add_plot().line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000') \
# #                 .xlabel('t (s)').ylabel('Heat-rate')      \
# #                 .title('Heat-rate vs. Time')
# # #
# # # plots.add_plot().line('theta*re/1000','h/1000',label='Foo')       \
# # #                 .line('theta*re/1000','h/1000',label='Bar',step=1,sol=5)   \
# # #                 .xlabel('Downrange (km)')                   \
# # #                 .ylabel('h (km)')                           \
# # #                 .title('Altitude vs. Downrange')

plots.render()
