import dill
from .elements import PlotList,Plot
from .renderers import *

class BelugaPlot:
    """
    Manages the plotting framework
    """
    def __init__(self, filename='data.dill', renderer = None, default_sol = -1, default_iter = -1):
        """
        Initializes plotting framework with given data file
        """
        self._plots = []
        self._figures = []
        self._plotconfig = {}
        self.global_settings = {}
        self.filename = filename
        self.default_sol_idx = default_sol
        self.default_iter_idx = default_iter

        # TODO: Get default renderer information from global configuration
        # TODO: Pass in extra renderer options here?
        if renderer is None:
            self.renderer = MatPlotLibRenderer()
        else:
            self.renderer = renderer

    def add_plot(self, solution = None, iteration = None):
        """
        Adds a new plot
            (alias for add_plot() in PlotList)
        """
        if solution is None:
            solution = self.default_sol_idx
        if iteration is None:
            iteration = self.default_iter_idx
        plot = Plot(solution,iteration)
        self._plots.append(plot)
        return plot

    def render(self,show=True):
        with open(self.filename,'rb') as f:
            out = dill.load(f)

        for plot in self._plots:
            plot.preprocess(out['solution'],out['problem_data'])
            fig = self.renderer.create_figure()
            self.renderer.render_plot(fig,plot)
            self._figures.append(fig)
        if show:
            self.show()

    def show(self):
        self.renderer.show_all()

    def plotconfig(varname,value=None):
        """
        Adds/updates settings affecting all plots
        """
        if isinstance(varname, dict):
            self._plotconfig.update(varname)
        else:
            self._plotconfig[varname] = value
        return self
