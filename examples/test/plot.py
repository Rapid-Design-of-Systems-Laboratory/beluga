from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('x*V*tfreal','y*V*tfreal')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory')
# .line('x2','y2',label='traj2')\
plots.add_plot().line('x','y',label='traj1')\
                .line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')\
                .xlabel('x(t)').ylabel('y(t)')\
                .title('Trajectory') \
                .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line('t','theta*180/pi')\
                .xlabel('t (s)').ylabel('theta [deg]')\
                .title('Control history')

# plots.add_plot().line('t','v2')\
#                 .xlabel('t (s)').ylabel('v2 [deg]')\
#                 .title('Control history')

#
# plots.add_plot().line('t','thr')\
#                 .xlabel('t (s)').ylabel('thr [nd]')\
#                 .title('Control history')
# plots.add_plot().line('t','sqrt((x - x2)**2 + (y - y2)**2)*(V*tfreal)')\
#                 .xlabel('t').ylabel('Separation (m)')\
#                 .title('Separation')


plots.render()
