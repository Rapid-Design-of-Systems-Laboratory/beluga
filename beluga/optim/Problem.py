from beluga.optim.problem import Expression, Execute, ConstraintSet
from beluga.continuation import ContinuationSet
# from os import getcwd

class Problem(object):
    """Defines problem settings."""
    def __init__(self):
        """Initialize all relevant problem settings."""
        self.indep_var = []
        self.state = []
        self.control = []
        self.cost = {'init': Expression('0','nd'),
                     'term': Expression('0','nd'),
                     'path': Expression('0','nd')}
        self.constant = []
        self.quantity = []
        self.scale = []
        self.continuation = []
        self.execute = Execute();
        self.constraints = ConstraintSet()
        self.steps = ContinuationSet()
        self.system = [] # List of dynamic system

        # self.get_initial_guess = getcwd() + '/get_initial_guess.py'
        # self.data_folder = getcwd() + '/data'
    def system(self,name='default', count=1):
        self.system.append([])
