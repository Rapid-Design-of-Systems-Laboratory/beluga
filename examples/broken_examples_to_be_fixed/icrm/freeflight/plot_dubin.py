from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data_dubin.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y')                    \
                .xlabel('x [m]').ylabel('y [m]')      \
                .title('Trajectory')

plots.add_plot().line('t','delta')                    \
                .xlabel('t (s)').ylabel('delta (m/s)')      \
                .title('Control history')

plots.render()
