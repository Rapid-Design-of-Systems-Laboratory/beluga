import abc


class BaseAlgorithm(object):
    """
    Object representing an algorithm that solves boundary valued problems.

    This object serves as a base class for other algorithms.
    """
    # Define class as abstract class
    __metaclass__ = abc.ABCMeta

    # Define common interface for algorithm classes
    def __init__(self, *args, **kwargs):

        self.derivative_function = None
        self.quadrature_function = None
        self.boundarycondition_function = None
        self.initial_cost_function = None
        self.path_cost_function = None
        self.terminal_cost_function = None
        self.inequality_constraint_function = None

        self.derivative_function_jac = None
        self.boundarycondition_function_jac = None

        if len(args) > 0:
            self.derivative_function = args[0]

        if len(args) > 1:
            self.quadrature_function = args[1]

        if len(args) > 2:
            self.boundarycondition_function = args[2]

        self.bc_func_ms = None
        self.stm_ode_func = None

    def set_boundarycondition_function(self, boundarycondition_function):
        self.boundarycondition_function = boundarycondition_function
        self.bc_func_ms = None

    def set_boundarycondition_jacobian(self, boundarycondition_jacobian):
        self.boundarycondition_function_jac = boundarycondition_jacobian

    def set_derivative_function(self, derivative_function):
        self.derivative_function = derivative_function
        self.stm_ode_func = None

    def set_derivative_jacobian(self, derivative_jacobian):
        self.derivative_function_jac = derivative_jacobian

    def set_quadrature_function(self, quadrature_function):
        self.quadrature_function = quadrature_function

    def set_initial_cost_function(self, initial_cost):
        self.initial_cost_function = initial_cost

    def set_path_cost_function(self, path_cost):
        self.path_cost_function = path_cost

    def set_terminal_cost_function(self, terminal_cost):
        self.terminal_cost_function = terminal_cost

    def set_inequality_constraint_function(self, inequality_constraint):
        self.inequality_constraint_function = inequality_constraint

    @abc.abstractmethod
    def solve(self, solinit, **kwargs):
        raise NotImplementedError()

    def close(self):
        pass

class BVPResult(dict):
    """ Represents the BVP solver result.

    :param dict:
    :return:
    """

    def __repr__(self):
        if self.keys():
            m = max(map(len, list(self.keys()))) + 1
            return '\n'.join([k.rjust(m) + ': ' + repr(v)
                              for k, v in sorted(self.items())])
        else:
            return self.__class__.__name__ + "()"
