from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('xbar*V*tfreal','ybar*V*tfreal')                    \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

plots.add_plot().line('t','abar*V/tfreal')                    \
                .xlabel('t (s)').ylabel('a (rad/s)')      \
                .title('Control history')
plots.render()
