from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('theta*180/3.14','h/1000')                    \
                .xlabel('theta (deg)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line('t','alfa*180/3.14')                    \
                .xlabel('t (s)').ylabel('alfa (degrees)')      \
                .title('Angle of attack vs. Time')
plots.render()
