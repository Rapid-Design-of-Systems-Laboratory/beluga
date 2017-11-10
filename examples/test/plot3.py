from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('x*V*tfreal','y*V*tfreal')                    \
#                 .xlabel('x(t)').ylabel('y(t)')      \
#                 .title('Trajectory')
plots.add_plot().line('xbar','ybar',label='traj1') \
                .line('xbar2','ybar2',label='traj2') \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory') \
                .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line('t','sqrt((xbar-xbar2)**2 + (ybar-ybar2)**2)',label='Actual S21') \
                .line('t','sqrt((xbar-xc)**2 + (ybar-yc)**2)',label='Actual S1C') \
                .line('t','sqrt((xbar2-xc)**2 + (ybar2-yc)**2)',label='Actual S2C') \
                .line('t','rj',label='rj')\
                .xlabel('t').ylabel('Distance')

plots.add_plot().line('t','((xbar-xbar2)**2 + (ybar-ybar2)**2)/commLimit',label='constraint')

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
