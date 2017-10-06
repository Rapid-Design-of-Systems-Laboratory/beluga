from . import renderers, datasources
from .elements import PlotList,Plot
from .renderers import BaseRenderer
from .datasources import BaseDataSource
import dill, inspect, logging
import os
class BelugaPlot:
    """
    Manages the plotting framework
    """
    def __init__(self, filename = None, datasource='dill', renderer = 'matplotlib', default_step = -1, default_sol = -1, mesh_size=512):
        """
        Initializes plotting framework with given data file
        """
        self._plots = []
        self._figures = []
        self._plotconfig = {}
        self.global_settings = {}
        self.filename = filename
        self.default_step_idx = default_step
        self.default_sol_idx = default_sol
        self.mesh_size = mesh_size

        # Load datasource by filename unless one is specified directly
        if filename is not None:
            fname, file_ext = os.path.splitext(filename)
        else:
            file_ext = None

        # TODO: Get default datasource information from global configuration
        if isinstance(datasource, BaseDataSource):
            # Use custom renderer object
            self.datasource = datasource
        else:
            # Load renderer from the list of existing classes
            self.datasource = None
            for name, obj in inspect.getmembers(datasources):
                if inspect.isclass(obj) and issubclass(obj, BaseDataSource):
                    if (isinstance(datasource, str) and name.lower() == datasource.lower()) \
                        or file_ext in obj.valid_exts:
                        # Renderer initialized with its default settings
                        self.datasource = obj(filename)
            if self.datasource is None:
                raise ValueError('Datasource "'+datasource+'" not found')

        # TODO: Get default renderer information from global configuration
        if isinstance(renderer, BaseRenderer):
            # Use custom renderer object
            self.renderer = renderer
        else:
            # Load renderer from the list of existing classes
            self.renderer = None
            for name, obj in inspect.getmembers(renderers):
                if inspect.isclass(obj) and issubclass(obj, BaseRenderer):
                    if name.lower() == renderer.lower():
                        # Renderer initialized with its default settings
                        self.renderer = obj()
            if self.renderer is None:
                raise ValueError('Renderer "'+renderer+'" not found')

    def add_plot(self, step = None, sol = None, datasource = None):
        """
        Adds a new plot
            (alias for add_plot() in PlotList)
        """
        if step is None:
            step = self.default_step_idx
        if sol is None:
            sol = self.default_sol_idx
        if datasource is None:
            datasource = self.datasource

        plot = Plot(step, sol, self.mesh_size, datasource)
        self._plots.append(plot)
        return plot

    def render(self,show=True):
        for plot in self._plots:
            # plot.preprocess(out['solution'],out['problem_data'])
            plot.preprocess()
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
