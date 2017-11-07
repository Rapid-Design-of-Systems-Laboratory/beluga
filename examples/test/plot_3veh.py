from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
plots = BelugaPlot('./data-3v-s15.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('xbar*V*tfreal','ybar*V*tfreal')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory')
plots.add_plot().line('xbar','ybar',label='traj1')\
                .line('xbar2','ybar2',label='traj2')\
                .line('xbar3','ybar3',label='traj3')\
                .line('xbar3','yc')\
                .xlabel('x(t)').ylabel('y(t)')\
                .title('Trajectory') \
                .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line('t','xi41')\
                .line('t','ybar/yc')

plots.add_plot().line('t','psi*180/3.14')\
                .line('t','psi2*180/3.14')\
                .line('t','psi3*180/3.14')\
                .xlabel('t (s)').ylabel('psi (deg)')\
                .title('Heading')

plots.add_plot().line('t','abar')\
                .line('t','abar2')\
                .line('t','abar3')\
                .xlabel('t (s)').ylabel('a (rad/s)')\
                .title('Control history')

# plots.add_plot().line('t','sqrt((xbar - xbar2)**2 + (ybar - ybar2)**2)*(V*tfreal)')\
#                 .xlabel('t').ylabel('Separation (m)')\
#                 .title('Separation')


plots.render()
