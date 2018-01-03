import dill
import numpy as np
import numexpr as ne
import collections
from sympy import *
from sympy.utilities.lambdify import lambdify
from beluga.utils import keyboard

class Plot(object):
    """
    Represents a single plot with axes, labels, expressions to evaluate etc.
    """
    def __init__(self, step, sol, mesh_size, datasource, colormap=None):
        self.step_index = step
        self.sol_index = sol
        self.mesh_size = mesh_size
        self.datasource = datasource
        self.plot_data = []
        self._title = self._xlabel = self._ylabel = None
        self.postprocess_list = []
        self.colormap = colormap

    def xlabel(self, label):
        self._xlabel = label
        return self

    def ylabel(self, label):
        self._ylabel = label
        return self

    def step(self, _step):
        self.step_index = _step
        return self

    def solution(self, _sol):
        self.sol_index = _sol
        return self

    def title(self, title_txt):
        """
        Sets the title of the figure
        """
        self._title = title_txt
        return self

    def line(self, x_expr, y_expr, label=None, style=None, step = None, sol = None, datasource = None):
        """
        Adds a new line plot to the figure
        """
        if datasource is None:
            datasource = self.datasource
        if style is None:
            style = {}
        # TODO: Datatype sanity checks needed here
        self.plot_data.append({'type':'line', 'x':x_expr, 'y':y_expr, 'style':style, 'label':label, 'step':step, 'sol':sol, 'datasource': datasource})
        return self

    def line_series(self, x_expr, y_expr, label=None, style=None, step = None, start = 0, skip = 0, end = -1, datasource = None):
        if datasource is None:
            datasource = self.datasource
        if style is None:
            style = {}
        self.plot_data.append({'type':'line_series', 'x':x_expr, 'y':y_expr, 'style':style, 'label':label, 'step':step, 'start':start, 'skip':skip, 'end': end, 'datasource': datasource})
        return self

    def line3d(self, x_expr, y_expr, z_expr, label=None, style=None, step = None, sol = None, datasource = None):
        if datasource is None:
            datasource = self.datasource
        if style is None:
            style = {}
        # TODO: Datatype sanity checks needed here
        self.plot_data.append({'type':'line3d', 'x':x_expr, 'y':y_expr, 'z':z_expr, 'style':style, 'label':label, 'step':step, 'sol':sol, 'datasource': datasource})
        return self

    def line3d_series(self, x_expr, y_expr, z_expr, label=None, style=None, step = None, start = 0, skip = 0, end = -1, datasource = None):
        if datasource is None:
            datasource = self.datasource
        if style is None:
            style = {}
        self.plot_data.append({'type':'line3d_series', 'x':x_expr, 'y':y_expr, 'z':z_expr, 'style':style, 'label':label, 'step':step, 'start':start, 'skip':skip, 'end': end, 'datasource': datasource})
        return self

    def preprocess(self):
        """
        Evaluates the expressions using the supplied data
        """
        for line in self.plot_data:
            solution = line['datasource'].get_solution()
            problem_data  = line['datasource'].get_problem()

            step_idx = line['step'] if line['step'] is not None else self.step_index
            line['data'] = []
            if line['type'] == 'line' or line['type'] == 'line3d':
                sol_idx = line['sol'] if line['sol'] is not None else self.sol_index
                sol = solution[step_idx][sol_idx]

                sol.prepare(problem_data, mesh_size=self.mesh_size, overwrite=True)
                line['data'].append({'x_data': sol.evaluate(line['x']),
                                     'y_data': sol.evaluate(line['y']),
                                     'z_data': sol.evaluate(line.get('z','0'))})
            elif line['type'] == 'line_series' or line['type'] == 'line3d_series':
                sol_set = solution[step_idx]
                line['end'] = len(sol_set) if line['end'] == -1 else line['end']
                for ind in range(line['start'], line['end'], line['skip']+1):
                    sol = sol_set[ind]
                    sol.prepare(problem_data, mesh_size=self.mesh_size, overwrite=True)
                    # sol.prepare(problem_data)
                    line['data'].append({'x_data': sol.evaluate(line['x']),
                                         'y_data': sol.evaluate(line['y']),
                                         'z_data': sol.evaluate(line.get('z','0'))})
            else:
                raise ValueError('Invalid plot type specified')

    def postprocess(self, fn):
        self.postprocess_list.append(fn)
        return self

class PlotList(list):
    """
    A collection class for storing plot objects
    """
    def add_plot(self, plot=None):
        if plot is None:
            plot = Plot()
        self.append(plot)
        return plot
