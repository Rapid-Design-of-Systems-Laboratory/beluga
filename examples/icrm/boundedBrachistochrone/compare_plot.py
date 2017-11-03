from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill, GPOPS
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
import functools as ft

output_dir = './plots/'
def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig)
    plt.tight_layout()
    # tikz_save(f'{output_dir}/brachisto_{suffix}.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
    plt.savefig(f'{output_dir}/brachisto_{suffix}.eps')

def postprocess_lambda(renderer, fig, p):
    from matplotlib.font_manager import FontProperties
    fontP = FontProperties()
    fontP.set_size('small')
    fh = renderer._get_figure(fig)
    plt.ylim([-0.11, 0.10])
    plt.legend(loc='upper left',prop=fontP,ncol=2)
    plt.tight_layout()
    # Replace − with - in the output file
    save_pic(renderer, fig, p, 'icrm_costates')

def postprocess_gpops(renderer, fig, p):
    from matplotlib.font_manager import FontProperties
    fontP = FontProperties()
    fontP.set_size('small')
    fh = renderer._get_figure(fig)
    plt.ylim([-0.11, 0.05])
    plt.legend(loc='upper left',prop=fontP,ncol=2)
    plt.tight_layout()
    # Replace − with - in the output file
    save_pic(renderer, fig, p, 'gpops_costates')

mpbvp_ds = Dill('../../mpbvp/boundedBrachistochrone/data_mpbvp_sol.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
gpops_ds = GPOPS('./brachisto_eps5.mat',states=('x','y','v','xi','tf'),controls=('theta','ue1'))

plots.add_plot().line('x','y',label='ICRM Solution', sol=-1, step=-1, style={'lw': 2.0})               \
                .line('x','y',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .line('x','y',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0})\
                .line('x','-1.0-x',label='x + y + 1 = 0',step=-1,sol=-1, style={'lw': 2.0, 'ls':'dashed'}) \
                .xlabel('$x(t)$ [m]').ylabel('$y(t)$ [m]')      \
                .postprocess(ft.partial(save_pic, suffix='icrm_xy'))

plots.add_plot().line('t','theta*180/3.14',label='ICRM Solution', style={'lw': 2.0})\
                .line('t','-theta*180/3.14',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0})\
                .line('t','-theta*180/3.14',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0})\
                .xlabel('$t$ [s]').ylabel('$\\theta$ [deg]')      \
                .postprocess(ft.partial(save_pic, suffix='icrm_theta'))

plots.add_plot().line('t','lamX', label='$\\lambda_x(t)$ - ICRM ', style={'lw': 2.0}) \
                .line('t','lamX', label='$\\lambda_x(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1, style={'lw': 2.0,'ls':'--'})\
                .line('t','lamX', label='$\\lambda_x(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
                .line('t','lamY', label='$\\lambda_y(t)$ ICRM', style={'lw': 2.0}) \
                .line('t','lamY', label='$\\lambda_y(t)$ MPBVP', datasource=mpbvp_ds, step=-1, sol=-1,style={'lw':2.0,'ls':'--'})\
                .line('t','lamY', label='$\\lambda_y(t)$ Unconstrained', datasource=mpbvp_ds, step=0, sol=-1, style={'lw': 2.0}) \
                .xlabel('$t$ [s]').ylabel('$\\lambda_x(t)$') \
                .postprocess(postprocess_lambda)

plots.add_plot(mesh_size=None).line('t','lamX', label='$\\lambda_x$ ICRM')\
                .line('t','lamY', label='$\\lambda_y$ ICRM')\
                .line('t','lamV', label='$\\lambda_v$ ICRM')\
                .line('t','lamXI11', label='$\\lambda_{\\xi_1}$ ICRM')\
                .line('t','lamX',label='$\\lambda_x$ GPOPS',datasource=gpops_ds,style='o')\
                .line('t','lamY',label='$\\lambda_y$ GPOPS',datasource=gpops_ds,style='o')\
                .line('t','lamV',label='$\\lambda_v$ GPOPS',datasource=gpops_ds,style='o')\
                .line('t','lamXI',label='$\\lambda_{\\xi_1}$ GPOPS',datasource=gpops_ds,style='o')\
                .xlabel('t (s)').ylabel('$\\lambda(t)$')      \
                .postprocess(postprocess_gpops)


plots.render()
