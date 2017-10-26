from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
import functools as ft

output_dir = './plots/'
def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig);
    tikz_save(f'{output_dir}/brachisto_{suffix}.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')

mpbvp_ds = Dill('../../mpbvp/boundedBrachistochrone/data.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='ICRM Solution', sol=-1, step=-1, style={'lw': 2.0})               \
                .line('x','y',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .line('x','y',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0})\
                .line('x','-1.0-x',label='x + y + 1 = 0',step=-1,sol=-1, style={'lw': 2.0, 'ls':'dashed'}) \
                .xlabel('$x(t)$ [m]').ylabel('$y(t)$ [m]')      \
                .postprocess(ft.partial(save_pic, suffix='icrm_xy'))

plots.add_plot().line('t','theta*180/3.14',label='ICRM Solution', style={'lw': 2.0})                    \
                .line('t','theta*180/3.14',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .line('t','theta*180/3.14',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0})\
                .xlabel('$t$ [s]').ylabel('$\\theta$ [deg]')      \
                .postprocess(ft.partial(save_pic, suffix='icrm_theta'))

plots.add_plot().line('t','lamX', label='$\\lambda_x(t)$ ICRM ', style={'lw': 2.0})                    \
                .line('t','lamX', label='$\\lambda_x(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .line('t','lamX', label='$\\lambda_x(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
                .xlabel('$t$ [s]').ylabel('$\\lambda_x(t)$') \
                .postprocess(ft.partial(save_pic, suffix='icrm_lamX'))
                # .line('t','lamY', label='$\\lambda_y(t)$ ICRM')                    \
                # .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1)\
                # .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1) \

plots.add_plot().line('t','lamY', label='$\\lambda_y(t)$ ICRM ', style={'lw': 2.0})                    \
                .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
                .xlabel('$t$ [s]').ylabel('$\\lambda_y(t)$') \
                .postprocess(ft.partial(save_pic, suffix='icrm_lamY'))

plots.render()
