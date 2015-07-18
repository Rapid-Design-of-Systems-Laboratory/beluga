from beluga.visualization import BelugaPlot

plots = BelugaPlot('/Users/tantony/dev/mjgrant-beluga/examples/data.dill')

plots.add_plot().xlabel('v (km/s)')     \
                .ylabel('h (km)')       \
                .x('v/1000')            \
                .y('h/1000')            \
                .title('Altitude vs. Velocity')

plots.render()
