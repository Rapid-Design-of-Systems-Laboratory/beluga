import abc
class Algorithm(object):
    # Define class as abstract class
    __metaclass__ = abc.ABCMeta

    # Define common interface for algorithm classes
    @abc.abstractmethod
    def solve(self,bvp,guess):
        """Method to solve the bvp with given arguments"""
