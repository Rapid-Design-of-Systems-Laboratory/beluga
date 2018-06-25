from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('xbar*V*tfreal','ybar*V*tfreal')                    \
#                 .xlabel('x(t)').ylabel('y(t)')      \
#                 .title('Trajectory')
plots.add_plot().line('e','n',label='traj1')                    \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory') \
                .postprocess(lambda a,b,c: plt.axis('equal'))

plots.add_plot().line('t','psi*180/3.14')                    \
                .xlabel('t (s)').ylabel('psi (deg)')      \
                .title('Heading')

plots.add_plot().line('t','gam*180/3.14',label='FPA')                    \
                .line('t','bank*180/3.14',label='Bank angle')                    \
                .xlabel('t [s]').ylabel('Control [deg]')      \
                .title('Control history')

# plots.add_plot().line('t','sqrt((xbar - xbar2)**2 + (ybar - ybar2)**2)*(V*tfreal)')                    \
#                 .xlabel('t').ylabel('Separation (m)')      \
#                 .title('Separation')


plots.render()
