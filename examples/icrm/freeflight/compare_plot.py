from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill, GPOPS
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
import matplotlib.cm as cmx
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
    tikz_save(f'{output_dir}/freeflight_{suffix}.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')

def analytical_sol_xv(renderer, fig, p):
    fh = renderer._get_figure(fig)
    T = 2.0

    t_list = np.linspace(0,T,21)
    x_t = np.zeros_like(t_list)
    v_t = np.zeros_like(t_list)
    for i, t in enumerate(t_list):
        if t < T/2:
            x_t[i] = t**2/2
            v_t[i] = t
        else:
            x_t[i] = t*T - t**2/2 -T**2/4
            v_t[i] = T-t

    plt.plot(t_list, x_t, 'o', label='$x$ - Analytical')
    plt.plot(t_list, v_t, 'o', label='$v$ - Analytical')
    plt.legend(prop=fontP,loc='lower right')
    plt.ylim([-0.02, 1.2])
    plt.tight_layout()
    save_pic(renderer,fig,p,'icrm_traj')

def analytical_sol_u(renderer, fig, p):
    fh = renderer._get_figure(fig)
    T = 2.0
    t_list = np.linspace(0,T,21)
    u_list = np.ones_like(t_list)

    u_list[t_list > T/2] = -1.0
    plt.plot(t_list, u_list, 'o', label='$u$ - Analytical')
    plt.legend(prop=fontP,loc='center right')
    plt.tight_layout()
    save_pic(renderer,fig,p,'icrm_u')

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('t','x',label='$x$ [m] - ICRM', sol=-1, step=-1, style={'lw': 2.0})\
                .line('t','v',label='$v$ [m/s]- ICRM', step=-1, sol=-1, style={'lw': 2.0})\
                .xlabel('$t$ [s]') \
                .postprocess(analytical_sol_xv)

plots.add_plot().line('t','a',label='$u$ - ICRM', sol=-1, step=-1, style={'lw': 2.0})\
                .xlabel('$t$ [s]').ylabel('$u(t)$ [m/s$^2$] -- ICRM') \
                .postprocess(analytical_sol_u)

plots.add_plot(colormap=cmx.gnuplot).line_series('t','v',step=-1,skip=1)\
                .xlabel('$t$ [s]').ylabel('$v(t)$ [m/s]')\
                .postprocess(ft.partial(save_pic, suffix='icrm_evol'))

#
# plots.add_plot().line('t','theta*180/3.14',label='ICRM Solution', style={'lw': 2.0})\
#                 .line('t','theta*180/3.14',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
#                 .line('t','theta*180/3.14',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0})\
#                 .xlabel('$t$ [s]').ylabel('$\\theta$ [deg]')      \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_theta'))
#
# plots.add_plot().line('t','lamX', label='$\\lambda_x(t)$ - ICRM ', style={'lw': 2.0}) \
#                 .line('t','lamX', label='$\\lambda_x(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0,'ls':'--'})\
#                 .line('t','lamX', label='$\\lambda_x(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
#                 .line('t','lamY', label='$\\lambda_y(t)$ ICRM', style={'lw': 2.0}) \
#                 .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1,style={'lw':2.0,'ls':'--'})\
#                 .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
#                 .xlabel('$t$ [s]').ylabel('$\\lambda_x(t)$') \
#                 .postprocess(postprocess_lambda)
#
# plots.add_plot(mesh_size=None).line('t','lamX', label='$\\lambda_x$ ICRM')\
#                 .line('t','lamY', label='$\\lambda_y$ ICRM')\
#                 .line('t','lamV', label='$\\lambda_v$ ICRM')\
#                 .line('t','lamXI11', label='$\\lambda_{\\xi_1}$ ICRM')\
#                 .line('t','lamX',label='$\\lambda_x$ GPOPS',datasource=gpops_ds,style='o')\
#                 .line('t','lamY',label='$\\lambda_y$ GPOPS',datasource=gpops_ds,style='o')\
#                 .line('t','lamV',label='$\\lambda_v$ GPOPS',datasource=gpops_ds,style='o')\
#                 .line('t','lamXI',label='$\\lambda_{\\xi_1}$ GPOPS',datasource=gpops_ds,style='o')\
#                 .xlabel('t (s)').ylabel('$\\lambda(t)$')      \
#                 .postprocess(postprocess_gpops)


# plots.add_plot().line('t','lamY', label='$\\lambda_y(t)$ ICRM ', style={'lw': 2.0})\
#                 .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
#                 .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
#                 .xlabel('$t$ [s]').ylabel('$\\lambda_y(t)$') \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_lamY'))

plots.render()
