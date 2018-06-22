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
        plt.savefig(f'{output_dir}/bench_{suffix}.{format}',rasterized=True, format='pdf',dpi=300)
    else:
        plt.savefig(f'{output_dir}/bench_{suffix}.{format}')

plots = BelugaPlot('data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

scale = 15

plot1 = plots.add_plot(colormap=cmx.tab10).line(f'xbar*{scale}',f'ybar*{scale}',label='Vehicle 1',style={'lw':2.0})
plot2 = plots.add_plot(colormap=cmx.tab10).line('t*50','abar',label='$\\bar{u}_1(t)$',style={'lw':2.0})

n = 10
for i in range(2, n+1):
    plot1.line(f'xbar{i}*{scale}',f'ybar{i}*{scale}',label=f'Vehicle {i}',style={'lw':2.0})
    plot2.line(f't*50',f'abar{i}',label='$\\bar{u}_'+str(i)+'(t)$',style={'lw':2.0})

plot1.xlabel('$x$ [km]').ylabel('$y$ [km]')\
     .postprocess(lambda r,f,p: plt.legend(loc='lower right'))\
     .postprocess(lambda r,f,p: plt.axis('equal'))\
     .postprocess(ft.partial(save_pic, suffix='xy',format='pdf'))

plot2.xlabel('$t$ [sec]').ylabel('$\\bar{u}$(t)')\
     .postprocess(lambda r,f,p: plt.legend(loc='lower right'))\
     .postprocess(ft.partial(save_pic, suffix='u',format='pdf'))

plots.render()
