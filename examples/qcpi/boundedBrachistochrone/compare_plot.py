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
    plt.tight_layout()
    plt.savefig(f'{output_dir}/boundedbrachisto_{suffix}.eps')

# mpbvp_ds = Dill('../../mpbvp/boundedBrachistochrone/data.dill')
icrm_ds = Dill('../../icrm/boundedBrachistochrone/data.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='QCPI', sol=-1, step=-1, style={'lw':0.0, 'marker':'o'})               \
                .line('x','y',label='ICRM + Shooting', datasource=icrm_ds, step=-1, sol=-1, style={'lw':2.0})\
                .line('x','-1.0-x',label='x + y = 1',step=-1,sol=-1,style={'lw':2.0, 'linestyle':'--'}) \
                .xlabel('$x(t)$ [m]').ylabel('$y(t)$ [m]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_xy'))

plots.add_plot().line('t','theta*180/3.14',label='QCPI Solution', style={'lw':0.0, 'marker':'o'})                    \
                .line('t','theta*180/3.14',label='ICRM + Shooting', datasource=icrm_ds, step=-1, sol=-1, style={'lw':2.0})\
                .xlabel('$t$ [s]').ylabel('$\\theta$ [deg]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_theta'))
plots.render()
