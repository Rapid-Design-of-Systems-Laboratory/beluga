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
        return obj

    @abc.abstractmethod
    def solve(self, deriv_func, quad_func, bc_func, solinit):
        raise NotImplementedError()

    def close(self):
        pass
