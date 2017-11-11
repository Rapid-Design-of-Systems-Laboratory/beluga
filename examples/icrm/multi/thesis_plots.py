import matplotlib
import numpy as np
from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill

import matplotlib.pyplot as plt
import matplotlib.cm as cmx

def add_cylinder(r,f,p, xc,yc,rc):
    ax = plt.gca()
    ax.set_zlabel('z(t) [km]')
    # Cylinder
    ax.invert_zaxis()

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

    ax.plot_surface(X, Y, Z, linewidth=0)
    ax.plot_surface(X, (2*y_center-Y), Z, linewidth=0)
    plt.axis('equal')

output_dir = './plots/'
from matplotlib.font_manager import FontProperties
import functools as ft
fontP = FontProperties()
fontP.set_size('small')
def save_pic(renderer, fig, p, suffix):
    fh = renderer._get_figure(fig)
    plt.tight_layout()
    # tikz_save(f'{output_dir}/freeflight_{suffix}.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
    plt.savefig(f'{output_dir}/icrm_app_{suffix}.eps')

one_path_ds = Dill('data-twoveh-s2-a.dill')

plots = BelugaPlot('data-twoveh-unc.dill',default_sol=-1,default_step=-1, renderer='matplotlib')


plots.add_plot().line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 1',style={'color':'blue','lw':2.0})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',datasource=one_path_ds,label='Vehicle 2',style={'color':'red','lw':2.0})\
                .line('xbar*V*tfreal/1e3','ybar*V*tfreal/1e3',label='Vehicle 1 - Unconstrained',style={'color':'blue','lw':2.0, 'ls':'dashed'})\
                .line('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3',label='Vehicle 2 - Unconstrained',style={'color':'red','lw':2.0, 'ls':'dashed'})\
                .line('xc*V*tfreal/1e3+rc*V*tfreal/1e3*cos(2*pi*t/tf)','yc*V*tfreal/1e3+rc*V*tfreal/1e3*sin(2*pi*t/tf)',label='Zone 1')\
                .line('xc2*V*tfreal/1e3+rc2*V*tfreal/1e3*cos(2*pi*t/tf)','yc2*V*tfreal/1e3+rc2*V*tfreal/1e3*sin(2*pi*t/tf)',label='Zone 2')\
                .xlabel('$x(t)$ [km]').ylabel('$y(t)$ [km]')\
                # .postprocess(ft.partial(save_pic, suffix='s1_xy'))

plots.render()
