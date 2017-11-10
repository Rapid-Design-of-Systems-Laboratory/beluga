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
                .line('t','sqrt(S21)',label='sqrt(S21)',style='o')\
                .line('t','sqrt(S1C)',label='sqrt(S1C)',style='o')\
                .line('t','sqrt(S2C)',label='sqrt(S2C)',style='o')\
                .line('t','0.2*t/t',label='rc')\
                .xlabel('t').ylabel('Distance')

u21 = '(1/(1+exp(-20*(rc**2-S2C)/rc**2)))'
commLim = f'{u21}*rj + (1-{u21})*rsep'
plots.add_plot().line('t',f'sqrt(S21)/commLimit',label='constraint')\
                .line('t',commLim,label='commLimit')\

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
