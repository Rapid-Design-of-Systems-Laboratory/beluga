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
        '''
        Method to solve the bvp with given arguments

        :param deriv_func: The ODE function.
        :param quad_func: The quad func.
        :param bc_func: The boundary conditions function.
        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        '''
        raise NotImplementedError()

    def close(self):
        pass
