from beluga.plotting import PlotList

plots = PlotList()

plots.add_plot().xlabel('v (km/s)')     \
                .ylabel('h (km)')       \
                .x('v/1000')            \
                .y('h/1000')
