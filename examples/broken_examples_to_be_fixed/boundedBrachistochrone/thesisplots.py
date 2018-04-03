from beluga.visualization import BelugaPlot
from matplotlib2tikz import save as tikz_save
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cmx

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'x-large'
mpl.rcParams['ytick.labelsize'] = 'x-large'

plots = BelugaPlot('./data_mpbvp_sol.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

output_dir = './plots/'
def postprocess_xy_plot(renderer, fig, plot):
    """fig: Matplotlib figure number.
    plot: Plot object."""

    fh = renderer._get_figure(fig);
    ax = fh.gca()
    plt.axis('equal')
    bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="yellow", ec="b", lw=2, alpha=0.5)
    t = ax.text(4, -6, "Decreasing constraint violation", ha="center", va="center", rotation=45,
                size=14,
                weight=400,
                bbox=bbox_props)
    t.set_alpha(.4)

    # tikz_save(output_dir+'brachisto_mpbvp_xy.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
    plt.savefig(output_dir+'brachisto_mpbvp_xy.eps')

def postprocess_theta_plot(renderer, fig, plot):
    """fig: Matplotlib figure number.
    plot: Plot object."""

    fh = renderer._get_figure(fig);
    ax = fh.gca()
    bbox_props = dict(boxstyle="larrow,pad=0.2", fc="yellow", ec="b", lw=2, alpha=0.5)
    t = ax.text(0.5, -65, "Constraint violation $\\rightarrow$ 0", ha="center", va="center", rotation=-45,
                size=13,
                weight=400,
                bbox=bbox_props)
    t.set_alpha(.5)

    bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="yellow", ec="b", lw=2, alpha=0.5)
    t = ax.text(1.465, -33, "Constraint violation $\\rightarrow$ 0", ha="center", va="center", rotation=-45,
                size=13,
                weight=400,
                bbox=bbox_props)
    t.set_alpha(.5)
    # tikz_save(output_dir+'brachisto_mpbvp_theta.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
    plt.savefig(output_dir+'brachisto_mpbvp_theta.eps')


def add_colorbar(r,f,p,lb,ub,label,cmap,pos='right',orient='vertical'):
    norm = mpl.colors.Normalize(vmin=lb, vmax=ub)

    fig = r._get_figure(f)
    # cax = fig.add_axes([0.125, 0.925, 0.775, 0.0725])

    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(pos, size="5%", pad=0.05)

    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, orientation=orient)
    cb.set_label(label)


plots.add_plot(colormap=cmx.jet).line_series('x','y', step=2, start=0, style={'lw': 2.5}) \
                .line('x','-1.0-x',label='x + y + 1 = 0',step=-1,sol=-1, style={'ls':'--', 'color':'green', 'lw':2.0}) \
                .xlabel('$x(t)$ [m]').ylabel('$y(t)$ [m]')      \
                .postprocess(postprocess_xy_plot)

plots.add_plot(colormap=cmx.jet).line_series('t','-theta*180/3.14', step=2, start=0) \
                .xlabel('$t$ [s]').ylabel('$\\theta(t)$ [deg]')      \
                .postprocess(postprocess_theta_plot)

# plots.add_plot().line('t','lamX')                    \
#                 .xlabel('t (s)').ylabel('lamX')      \
#                 .title('lamX')

plots.render()
