from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('y','x')                    \
                .xlabel('y (m)').ylabel('x (m)')      \
                .title('Boat Trajectory')       \

plots.add_plot().line('t','hdg*57.3')                    \
                .xlabel('time (s)').ylabel('hdg (rad)')      \
                .title('Boat Heading')

plots.render()
