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
    def __init__(self, step = 0, sol = 0):
        self.step_index = step
        self.sol_index = sol
        self.plot_data = []
        self._title = self._xlabel = self._ylabel = None

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

    def line(self, x_expr, y_expr, legend=None, step = None, sol = None):
        """
        Adds a new line plot to the figure
        """
        self.plot_data.append({'x':x_expr, 'y':y_expr, 'legend':legend, 'step':step, 'sol':sol})
        return self

    def preprocess(self, solution, problem_data):
        """
        Evaluates the expressions using the supplied data
        """
        for line in self.plot_data:
            step_idx = line['step'] or self.step_index
            sol_idx = line['sol'] or self.sol_index

            sol = solution[step_idx][sol_idx]
            sol.prepare(problem_data)

            line['x_data'] = sol.evaluate(line['x'])
            line['y_data'] = sol.evaluate(line['y'])
