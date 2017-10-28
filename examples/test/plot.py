from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('xbar*V*tfreal','ybar*V*tfreal')                    \
#                 .xlabel('x(t)').ylabel('y(t)')      \
#                 .title('Trajectory')
plots.add_plot().line('xbar','ybar')                    \
                .line('xbar2','ybar2')                    \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

plots.add_plot().line('t','psi*180/3.14')                    \
                .line('t','psi2*180/3.14')                    \
                .xlabel('t (s)').ylabel('psi (deg)')      \
                .title('Heading')

plots.add_plot().line('t','abar*V/tfreal')                    \
                .line('t','abar2*V/tfreal')                    \
                .xlabel('t (s)').ylabel('a (rad/s)')      \
                .title('Control history')
plots.render()
