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
    def __init__(self, sol = 0, iteration = 0):
        self.sol_index = sol
        self.iter_index = iteration

    def xlabel(self, label):
        self.xlabel_str = label
        return self

    def ylabel(self, label):
        self.ylabel_str = label
        return self

    def x(self, expr):
        self.x_expr_str = expr
        return self

    def y(self, expr):
        self.y_expr_str = expr
        return self

    def preprocess(self, solution, problem_data):
        """
        Evaluates the expressions using the supplied data
        """
        sol = solution[self.sol_index][self.iter_index]

        self.x_data = np.empty_like(sol.x)
        self.y_data = np.empty_like(sol.x)
        self.x_data[:] = np.NaN
        self.y_data[:] = np.NaN

        # for timestep in range(len(sol.x)):
        var_names = [state for state in problem_data['state_list']]
        var_names += [var for aux in problem_data['aux_list'] for var in aux['vars']]
        var_names = sorted(var_names)

        variables  = [(state,np.array(sol.y[idx,:]))
                        for idx,state in enumerate(problem_data['state_list'])]
        # Add auxiliary variables and their values (hopefully they dont clash)
        variables += [(var,sol.aux[aux['type']][var])
                        for aux in problem_data['aux_list']
                        for var in aux['vars']]
        var_dict = dict(variables)

        var_values  = [np.array(sol.y[idx,:])
                for idx,state in enumerate(problem_data['state_list'])]
        var_values += [sol.aux[aux['type']][var]
                for aux in problem_data['aux_list']
                for var in aux['vars']]

        # Build environment to evaluate expressions
        self.x_data = ne.evaluate(self.x_expr_str,var_dict)
        self.y_data = ne.evaluate(self.y_expr_str,var_dict)

        print(self.x_data)
        print(self.y_data)

    def render(self, problem_data, solution):
        """
        Renders the plot using the given renderer
        """
        pass

if __name__ == '__main__':
    f = open('/Users/tantony/dev/mjgrant-beluga/examples/data.dill','rb')
    out = dill.load(f)
    f.close()
    p = Plot(0,4)
    p.x('v/1000')
    p.y('h/1000')
    p.preprocess(out['solution'],out['problem_data'])
