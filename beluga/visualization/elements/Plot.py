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
    def __init__(self, sol = 0, iter = 0):
        self.sol_index = sol
        self.iter_index = iter
        self.x_data = self.y_data = None
        self._title = self._xlabel = self._ylabel = None

    def xlabel(self, label):
        self._xlabel = label
        return self

    def ylabel(self, label):
        self._ylabel = label
        return self

    def solution(self, sol):
        self.sol_index = sol
        return self

    def iteration(self, iter):
        self.iter_index = iter
        return self

    def x(self, expr, label = None):
        self.x_expr = expr
        if label is not None:
            self._xlabel = label
        return self

    def y(self, expr, label = None):
        self.y_expr = expr
        if label is not None:
            self._ylabel = label
        return self

    def title(self, title_txt):
        self._title = title_txt
        return self

    def preprocess(self, solution, problem_data):
        """
        Evaluates the expressions using the supplied data
        """
        sol = solution[self.sol_index][self.iter_index]
        sol.prepare(problem_data)
        
        self.x_data = sol.evaluate(self.x_expr)
        self.y_data = sol.evaluate(self.y_expr)
