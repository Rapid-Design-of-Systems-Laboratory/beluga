from beluga.visualization import BelugaPlot

plots = BelugaPlot('/Users/tantony/dev/beluga/examples/data.dill',default_sol=1,default_iter=20)

plots.add_plot().x('t','t (s)')                  \
                .y('h/1000','h (km)')            \
                .title('Altitude vs. Time')

plots.add_plot().x('theta*re/1000','Downrange (km)')                  \
                .y('h/1000','h (km)')            \
                .title('Altitude vs. Downrange')

plots.add_plot().x('v/1000','v (km/s)')          \
                .y('h/1000','h (km)')            \
                .title('Altitude vs. Velocity')

plots.render()
