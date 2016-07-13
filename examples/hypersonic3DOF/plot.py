from beluga.visualization import BelugaPlot
# from beluga.visualization.renderers import ToyPlot

# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line_series('theta*re/1000','h/1000', step=-1, skip=18)                    \
                .xlabel('Downrange (km)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

# plots.add_plot().line('theta*re/1000','h/1000')                    \
#                 .xlabel('Downrange (km)').ylabel('h (km)')      \
#                 .title('Altitude vs. Downrange')
#
# plots.add_plot().line('t','alfa*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
#                 .title('Angle of attack vs. Time')

plots.add_plot().line_series('v/1000','h/1000')                    \
                .xlabel('v, km/s').ylabel('h, km')      \
                .title('Altitude vs. Velocity')

plots.add_plot().line('t','alfa*180/3.14159')                    \
                .xlabel('t, s').ylabel('alpha, deg')      \
                .title('Angle of attack vs. Time')

plots.add_plot().line('t','bank*180/3.14159')                    \
                .xlabel('t, s').ylabel('bank, deg')      \
                .title('Bank angle vs. Time')

plots.add_plot().line_series('theta*180/3.14159','phi*180/3.14159')                    \
                .xlabel('Latitude, deg').ylabel('Longitude, deg')      \
                .title('Ground Track')

# plots.add_plot().line('t','alfa*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
#                 .title('Angle of attack vs. Time')

plots.render()
#
