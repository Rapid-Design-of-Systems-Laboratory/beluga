from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y')                    \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

plots.add_plot().line('t','theta')                    \
                .xlabel('t (s)').ylabel('theta (degrees)')      \
                .title('Control history')
plots.render()
