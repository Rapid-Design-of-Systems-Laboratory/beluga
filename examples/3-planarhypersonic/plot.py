from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)
plots.add_plot().line('theta*re/1000','h/1000', step=-1)                    \
                .xlabel('Downrange (km)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line('t','alfa*180/pi')                    \
                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
                 .title('Angle of attack vs. Time')

plots.add_plot().line('theta*re/1000','h/1000')                    \
                .xlabel('Downrange (km)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line('v/1000','h/1000')                    \
                .xlabel('v (km/s)').ylabel('h (km)')      \
                .title('Altitude vs. Velocity')

plots.render()
