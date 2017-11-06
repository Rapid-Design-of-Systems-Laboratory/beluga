from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('x*V*tfreal','y*V*tfreal')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory')

plots.add_plot().line('x','y',label='traj1')\
                .line('xc1+rc1*cos(2*pi*t/tf)','yc1+rc1*sin(2*pi*t/tf)')\
                .line('xc2+rc2*cos(2*pi*t/tf)','yc2+rc2*sin(2*pi*t/tf)')\
                .line('xc3+rc3*cos(2*pi*t/tf)','yc3+rc3*sin(2*pi*t/tf)')\
                .xlabel('x(t)').ylabel('y(t)')\
                .title('Trajectory') \
                .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line('t','xi11',label='xi11')\
                .line('t','xi21',label='xi21')\
                .line('t','xi31',label='xi31')
#                 .line('x2','y2',label='traj2')\
#                 .line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory') \
#                 .postprocess(lambda a,b,c: plt.axis('equal'))

# plots.add_plot().line('t','z')\
#                 .xlabel('t (s)').ylabel('theta [deg]')\
#                 .title('Control history')
#
# plots.add_plot().line('t','z')\
#                 .line('t','z2')\
#                 .xlabel('t (s)').ylabel('theta [deg]')\
#                 .title('Control history')
#
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
