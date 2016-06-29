import abc
#TODO: Identify data source based on file extension
class BaseDataSource(object):
    __metaclass__ = abc.ABCMeta
    valid_exts = []
    @abc.abstractmethod
    def reset(self):
        """
        Resets data source
        """
        
    @abc.abstractmethod
    def load(self):
        """
        Loads data into memory
        """

    @abc.abstractmethod
    def get_problem(self):
        """
        Returns problem information
        """

    @abc.abstractmethod
    def get_solution(self):
        """
        Returns the solution array
        """
