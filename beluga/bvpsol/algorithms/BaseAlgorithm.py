import abc
class BaseAlgorithm(object):
    # Define class as abstract class
    __metaclass__ = abc.ABCMeta

    # Define common interface for algorithm classes
    @abc.abstractmethod
    def solve(self,bvp):
        """Method to solve the bvp with given arguments"""
        raise NotImplementedError()

    def close(self):
        pass
