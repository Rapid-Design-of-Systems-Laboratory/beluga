from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
import functools as ft

import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'x-large'
mpl.rcParams['ytick.labelsize'] = 'x-large'

output_dir = './plots/'
def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig);
    # tikz_save(f'{output_dir}/brachisto_{suffix}.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/brachisto_{suffix}.eps')

def postprocess_ham(r,f,p):
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    save_pic(r,f,p,'qcpi_ham')

mpbvp_ds = Dill('../../brachistochrone/data.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot(mesh_size=None).line('x','y',label='QCPI', sol=-1, step=-1, style={'lw': 0.0, 'marker':'o'}) \
                .line('x','y',label='Multiple Shooting', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .xlabel('$x(t)$ [m]').ylabel('$y(t)$ [m]')      \
                .postprocess(ft.partial(save_pic, suffix='qcpi_xy'))

plots.add_plot(mesh_size=None).line('abs(t)','theta*180/3.14',label='QCPI', style={'lw': 0.0, 'marker':'o'}) \
                .line('abs(t)','theta*180/3.14',label='Multiple Shooting', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .xlabel('$t$ [s]').ylabel('$\\theta$ [deg]')      \
                .postprocess(ft.partial(save_pic, suffix='qcpi_theta'))

plots.add_plot(mesh_size=None)\
                .line('abs(t)','lamX',label='$\\lambda_x(t)$', style={'lw': 2.0})\
                .line('abs(t)','lamY',label='$\\lambda_y(t)$', style={'lw': 2.0})\
                .line('abs(t)','lamV',label='$\\lambda_v(t)$', style={'lw': 2.0})\
                .xlabel('$t$ [s]').ylabel('$\\lambda(t)$')      \
                .postprocess(ft.partial(save_pic, suffix='qcpi_lam'))

ham = 'lamX*v*cos(theta)+lamY*v*sin(theta)+lamV*g*sin(theta)+1.0'
plots.add_plot(mesh_size=None)\
                .line('abs(t)',ham,style={'lw': 2.0})\
                .xlabel('$t$ [s]').ylabel('$H(t)$ [s]')      \
                .postprocess(postprocess_ham)


# plots.add_plot().line('t','lamX', label='$\\lambda_x(t)$ ICRM ', style={'lw': 2.0})                    \
#                 .line('t','lamX', label='$\\lambda_x(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
#                 .line('t','lamX', label='$\\lambda_x(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
#                 .xlabel('$t$ (s)').ylabel('$\\lambda_x(t)$') \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_lamX'))
#                 # .line('t','lamY', label='$\\lambda_y(t)$ ICRM')                    \
#                 # .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1)\
#                 # .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1) \
#
# plots.add_plot().line('t','lamY', label='$\\lambda_y(t)$ ICRM ', style={'lw': 2.0})                    \
#                 .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
#                 .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
#                 .xlabel('$t$ (s)').ylabel('$\\lambda_y(t)$') \
#                 .postprocess(ft.partial(save_pic, suffix='icrm_lamY'))

plots.render()
