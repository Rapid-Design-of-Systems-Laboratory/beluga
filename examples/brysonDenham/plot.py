from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('t','x')                    \
                .xlabel('t (s)').ylabel('x(t)')      \
                .title('Position vs. Time')

plots.add_plot().line('t','v')                    \
                .xlabel('t (s)').ylabel('v(t)')      \
                .title('Velocity vs. Time')

plots.add_plot().line('t','u')                    \
                .xlabel('t (s)').ylabel('u(t)')      \
                .title('Control history')

plots.render()
