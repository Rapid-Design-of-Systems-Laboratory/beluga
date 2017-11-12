import matplotlib
matplotlib.use('TkAgg')
from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
plots = BelugaPlot('./data-3d2v-rj024.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# data3.dill in 2815.9161 seconds (full traj with rj=0.15, eps=1e-6)

# plots.add_plot().line('x*V*tfreal','y*V*tfreal')                    \
#                 .xlabel('x(t)').ylabel('y(t)')      \
#                 .title('Trajectory')
# plots.add_plot().line3d('xbar','ybar','-zbar',label='traj1') \
#                 .line3d('xbar2','ybar2','-zbar2',label='traj2') \
#                 .xlabel('x(t)').ylabel('y(t)')      \
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line_series('t','ybar2')\


plots.add_plot().line_series('t','sqrt((xbar-xbar2)**2 + (ybar-ybar2)**2)')\
                .line('t','rj')

plots.add_plot().line('t','((xbar-xbar2)**2 + (ybar-ybar2)**2)/commLimit',label='Actual constraint val') \
                .xlabel('t').ylabel('Distance')
# S2C1 = '((xbar2--0.6)**2)'
# S2C2 = '((xbar2--0.2)**2)'
# u212 = f'( (1/(1+exp(-20*(0.05**2-{S2C1})/0.05**2)) + 1/(1+exp(-20*(0.05**2-{S2C2})/0.05**2))) )'
# # plots.add_plot().line('t','((xbar-xbar2)**2 + (ybar-ybar2)**2)/commLimit',label='constraint')
# plots.add_plot().line('xbar',f'{u212}',label='lim')

# plots.add_plot().line('t',u21,label='u21')
#
# plots.add_plot().line('t','-zbar',label='traj1') \
#                 .xlabel('t').ylabel('z(t)')      \
#                 .title('Trajectory') \

# .line('xc + rc*cos(2*3.14*t/tf)','yc + rc*sin(2*3.14*t/tf)')\
# plots.add_plot().line('t','psi*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('psi (deg)')      \
#                 .title('Heading')

# plots.add_plot().line('t','u')                    \
#                 .xlabel('t (s)').ylabel('u (rad/s)')      \
#                 .title('Control history')
#
# plots.add_plot().line('t','sqrt((x - x2)**2 + (y - y2)**2)*(V*tfreal)')                    \
#                 .xlabel('t').ylabel('Separation (m)')      \
#                 .title('Separation')


plots.render()
