import abc
import dill
import logging

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


class Dill(BaseDataSource):
    valid_exts = ['dill']
    def __init__(self, filename = 'data.dill'):
        """
        Initializes the data source with supplied filename
        """
        self.is_loaded = False
        self.filename = filename

    def reset(self):
        self.is_loaded = False
        self._data = None

    def load(self):
        """
        Loads solution data using dill if not already loaded
        """
        if not self.is_loaded:
            with open(self.filename,'rb') as f:
                logging.info("Loading datafile "+self.filename+"...")
                self._data = dill.load(f)
                if 'solution' not in self._data:
                    self.is_loaded = False
                    logging.error("Solution missing in data file :"+self.filename)
                    raise RuntimeError("Solution missing in data file :"+self.filename)
                if 'problem_data' not in self._data:
                    self.is_loaded = False
                    logging.error("Problem data missing in data file :"+self.filename)
                    raise RuntimeError("Problem data missing in data file :"+self.filename)

                logging.info("Loaded "+str(len(self._data['solution']))+" solution sets from "+self.filename)
                self.is_loaded = True

    def get_problem(self):
        """
        Return problem data
        """
        # Lazy load data
        if not self.is_loaded:
            self.load()
            # logging.error("Data source should be loaded before being used")
            # raise RuntimeError("Data source should be loaded before being used")
        return self._data['problem_data']


    def get_solution(self):
        """
        Returns solution array
        """
        # Lazy load data
        if not self.is_loaded:
            self.load()
            # logging.error("Data source should be loaded before being used")
            # raise RuntimeError("Data source should be loaded before being used")
        return self._data['solution']

from scipy.io import loadmat
from beluga.bvpsol import Solution
import numpy as np
class GPOPS(BaseDataSource):
    valid_exts = ['mat']
    def __init__(self, filename = 'data.mat', states=None, controls=None, const=None):
        """
        Initializes the data source with supplied filename
        """
        if states is None or controls is None:
            raise ValueError('Please specify both state and control variable names')

        self.is_loaded = False
        self.filename = filename
        states = tuple(states)
        costates = tuple('lam'+x.upper() for x in states)
        self._const = const
        self.problem_data = {'state_list':states+costates,
                             'control_list':controls,
                             'quantity_vars':{}}
    def reset(self):
        self.is_loaded = False
        self._data = None

    def load(self):
        """
        Loads solution data using dill if not already loaded
        """
        if not self.is_loaded:
            logging.info("Loading datafile "+self.filename+"...")
            out = loadmat(self.filename)

            if 'output' in out:
                out = out['output']['result'][0][0][0][0]
            soldata = out['solution']['phase'][0][0][0][0]

            # if 'solution' not in self._data:
            #     self.is_loaded = False
            #     logging.error("Solution missing in data file :"+self.filename)
            #     raise RuntimeError("Solution missing in data file :"+self.filename)
            # if 'problem_data' not in self._data:
            #     self.is_loaded = False
            #     logging.error("Problem data missing in data file :"+self.filename)
            #     raise RuntimeError("Problem data missing in data file :"+self.filename)
            #
            _sol = Solution()

            tf = max(soldata['time'])
            _sol.x = soldata['time'][:,0]/tf
            _sol.y = np.r_[soldata['state'].T,soldata['costate'].T,np.ones_like(soldata['time']).T*tf]
            _sol.u = soldata['control'].T

            if 'tf' not in self.problem_data['state_list']:
                self.problem_data['state_list'] = tuple(self.problem_data['state_list']) + ('tf',)

            _sol.arcs = ((0, len(_sol.x)-1),)

            if self._const is not None:
                _sol.aux = {'const':self._const}

            self._sol = [[_sol]]
            logging.info('Loaded solution from data file')

            self.is_loaded = True

    def get_problem(self):
        """
        Return problem data
        """
        # Lazy load data
        if not self.is_loaded:
            self.load()
            # logging.error("Data source should be loaded before being used")
            # raise RuntimeError("Data source should be loaded before being used")
        return self.problem_data


    def get_solution(self):
        """
        Returns solution array
        """
        # Lazy load data
        if not self.is_loaded:
            self.load()
            # logging.error("Data source should be loaded before being used")
            # raise RuntimeError("Data source should be loaded before being used")
        return self._sol
