from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('y','x')                    \
                .xlabel('y (m)').ylabel('x (m)')      \
                .title('Track Path Trajectory')

plots.add_plot().line('t','hdg')                    \
                .xlabel('time (s)').ylabel('hdg (rad)')      \
                .title('Track Heading')

plots.add_plot().line('t','V')                    \
                .xlabel('time (s)').ylabel('V (m/s)')      \
                .title('Velocity')

plots.add_plot().line('t','hdgA')                    \
                .xlabel('time (s)').ylabel('hdgA (rad)')      \
                .title('Heading Argument')

plots.render()