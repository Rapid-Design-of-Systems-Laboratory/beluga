from beluga.visualization.elements import PlotList
from beluga.visualization.renderers import *

class BelugaPlot:
    """
    Manages the plotting framework
    """
    def __init__(self, filename='data.dill', renderer = None):
        """
        Initializes plotting framework with given data file
        """
        self._plots = PlotList()
        self._plotconfig = {}
        self.global_settings = {}
        # TODO: Get default renderer information from global configuration
        if renderer is None:
            self.renderer = MatPlotLibRenderer()
        else:
            self.renderer = renderer

    def add_plot(self, plot=None):
        """
        Adds a new plot
            (alias for add_plot() in PlotList)
        """
        return self._plots.add_plot(plot)

    def plotconfig(varname,value=None):
        """
        Adds/updates settings affecting all plots
        """
        if isinstance(varname, dict):
            self._plotconfig.update(varname)
        else:
            self._plotconfig[varname] = value
        return self

    def render(self):
        pass
