import abc


class BaseAlgorithm(object):
    '''
    Object representing an algorithm that solves boundary valued problems.

    This object serves as a base class for other algorithms.
    '''
    # Define class as abstract class
    __metaclass__ = abc.ABCMeta

    # Define common interface for algorithm classes
    def __new__(cls, *args, **kwargs):
        obj = super(BaseAlgorithm, cls).__new__(cls)
        obj.derivative_function = None
        obj.quadrature_function = None
        obj.boundarycondition_function = None
        obj.initial_cost_function = None
        obj.path_cost_function = None
        obj.terminal_cost_function = None
        obj.inequality_constraint_function = None

        if len(args) > 0:
            obj.derivative_function = args[0]

        if len(args) > 1:
            obj.quadrature_function = args[1]

        if len(args) > 2:
            obj.boundarycondition_function = args[2]

        return obj

    def set_boundarycondition_function(self, boundarycondition_function):
        self.boundarycondition_function = boundarycondition_function
        self.bc_func_ms = None

    def set_derivative_function(self, derivative_function):
        self.derivative_function = derivative_function
        self.stm_ode_func = None

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
