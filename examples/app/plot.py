import matplotlib as mpl
mpl.use('MacOSX')
from beluga.visualization import BelugaPlot
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import sys
import functools as ft

def add_colorbar(r,f,p,lb,ub,label,cmap,pos='right',orient='vertical'):
    norm = mpl.colors.Normalize(vmin=lb, vmax=ub)

    fig = r._get_figure(f)
    # cax = fig.add_axes([0.125, 0.925, 0.775, 0.0725])

    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(pos, size="5%", pad=0.05)

    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, orientation=orient)
    cb.set_label(label)

if len(sys.argv) < 2:
    print('Usage: python plot.py <n>')
    sys.exit(1)
else:
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = 'data.dill'

# plots = BelugaPlot('./data-3v-s15.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
plots = BelugaPlot(filename,default_sol=-1,default_step=-1, renderer='matplotlib')

plot1 = plots.add_plot().line('xbar','ybar',label='traj1')
plot2 = plots.add_plot().line3d('xbar','ybar','zbar',label='traj1')
plot3 = plots.add_plot(colormap=cmx.viridis).line3d_series('xbar','ybar','zbar')
plot4 = plots.add_plot(colormap=cmx.viridis).line_series('t*tf','psi5*180/pi')\
             .xlabel('t').ylabel('psi5')
plot5 = plots.add_plot(colormap=cmx.viridis).line('t*tfreal','abar',label='$u_1$')

n = int(sys.argv[1])

for i in range(2, n+1):
    plot1.line(f'xbar{i}',f'ybar{i}',label=f'traj{i}')
    plot2.line3d(f'xbar{i}',f'ybar{i}',f'zbar{i}',label=f'traj{i}')
    plot3.line3d_series(f'xbar{i}',f'ybar{i}',f'zbar{i}')
    plot5.line('t*tfreal',f'abar{i}',label=f'$u_{i}$')
    # plot4.line_series(f't*tf',f'psi{i}')

plot1.line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')
plot1.postprocess(lambda r,f,p: plt.axis('equal'))
plot2.postprocess(lambda r,f,p: plt.gca().invert_zaxis())
plot4.postprocess(ft.partial(add_colorbar, lb=0.0, ub=0.05,label='$y_c$',cmap=cmx.viridis))

plots.render()

#                 .line3d('xbar2*V*tfreal/1e3','ybar2*V*tfreal/1e3','zbar2*V*tfreal/1e3',label='traj2')\
#                 .xlabel('x(t) [km]').ylabel('y(t) [km]')\
#                 .postprocess(add_cylinder)
