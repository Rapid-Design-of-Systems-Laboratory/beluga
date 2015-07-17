from beluga.plotting import Plot
class PlotList(list):
    """
    A collection class for storing plot objects
    """
    def add_plot(self, plot=None):
        if plot is None:
            plot = Plot()
        self.append(plot)
        return plot
