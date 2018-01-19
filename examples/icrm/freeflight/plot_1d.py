from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('t','x')                    \
                .xlabel('t').ylabel('x [m]')      \
                .title('Trajectory')

plots.add_plot().line('t','v')                    \
                .xlabel('t (s)').ylabel('v (m/s)')      \
                .title('Velocity history')

plots.add_plot().line('t','a')                    \
                .xlabel('t (s)').ylabel('a (m/s^2)')      \
                .title('Control history')

plots.render()
