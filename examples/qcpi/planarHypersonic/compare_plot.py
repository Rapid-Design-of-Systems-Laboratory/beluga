from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
import functools as ft
import matplotlib.cm as cmx
import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'x-large'
mpl.rcParams['ytick.labelsize'] = 'x-large'

output_dir = './plots/'
def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig);
    plt.tight_layout()
    plt.savefig(f'{output_dir}/planarHypersonic_{suffix}.eps')

# mpbvp_ds = Dill('../../mpbvp/boundedBrachistochrone/data.dill')
icrm_ds = Dill('../planarHypersonic/data_thesis.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('theta*re/1000','h/1000',label='QCPI', sol=-1, step=-1, style={'lw':0.0, 'marker':'o'})\
                .line('theta*re/1000','h/1000',label='Shooting', sol=-1, step=-1, style={'lw':2.0})\
                .xlabel('Downrange distance [km]').ylabel('$h$ [km]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_ht'))

plots.add_plot().line('t','alfa*180/3.14',label='QCPI', style={'lw':0.0, 'marker':'o'})\
                .line('t','alfa*180/3.14',label='Shooting', datasource=icrm_ds, step=-1, sol=-1, style={'lw':2.0})\
                .xlabel('$t$ [s]').ylabel('$\\theta$ [deg]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_alfa'))

plots.add_plot(colormap=cmx.viridis).line_series('theta*re/1000','h/1000',step=-1,skip=5,  style={'lw':1.5})\
                .xlabel('Downrange distance [km]').ylabel('$h$ [km]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_evol_ht'))

plots.add_plot(colormap=cmx.viridis).line_series('v/1000','h/1000',step=-1, skip=1, style={'lw':1.5})\
                .xlabel('$v(t)$ [km/s]').ylabel('$h(t)$ [km]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_evol_hv'))

plots.add_plot(colormap=cmx.viridis).line_series('t','alfa*180/pi',step=-1,skip=1,  style={'lw':1.5})\
                .ylabel('$\\alpha$ [deg]').xlabel('$t$ [s]') \
                .postprocess(ft.partial(save_pic,suffix='qcpi_evol_alfa'))

plots.render()
