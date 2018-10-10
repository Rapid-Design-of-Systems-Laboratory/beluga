import numpy as np
import logging
import inspect
import functools
import sys


class ContinuationList(list):
    def __init__(self):
        # Create list of available strategies
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        self.strategy_list = {obj.strategy_name: obj
                                for (name,obj) in clsmembers
                                if hasattr(obj,'strategy_name')
                              }

    def add_step(self, strategy='manual', *args, **kwargs):
        """
        Adds a continuation step with specified strategy

        Returns the strategy object to further chain calls into it
        """
        # Create object if strategy is specified as a string
        if isinstance(strategy, str):
            if strategy in self.strategy_list:
                strategy_obj = self.strategy_list[strategy](*args, **kwargs)
            else:
                logging.error('Invalid strategy name')
                raise ValueError('Continuation strategy : '+strategy+' not found.')
        else:
            strategy_obj = strategy

        self.append(strategy_obj)
        return strategy_obj


class ContinuationVariable(object):
    """
    Class containing information for a continuation variable.
    """

    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.value = np.nan
        self.steps = []


# Can be subclassed to allow automated stepping
class ManualStrategy(object):
    """
    Class defining the manual continuation strategy.
    """
    # A unique short name to select this class
    strategy_name = 'manual'

    def __init__(self, num_cases = 1,vars=[], sol=None):
        self.sol = sol
        self._num_cases = num_cases
        self._spacing = 'linear'
        self.vars = {}  # dictionary of values
        self.ctr  = 0   # iteration counter
        self.last_sol = None

        self.terminal = functools.partial(self.set, param_type='terminal')
        self.initial = functools.partial(self.set, param_type='initial')
        self.const = functools.partial(self.set, param_type='const')
        self.orig_num_cases = num_cases
        self.constant = self.const

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_sol = None

    def clear(self):
        """Clears all the previously set continuation variables"""
        self.vars = {}
        self.reset()

    def constraint(self, name, target, index):
        """Continuation on constraint limit.

        index : Specify which constraint arc to use."""
        # sol.aux['constraints'][self.name]['limit'][1]
        self.set((name,index), target, param_type='constraint')

    def var_iterator(self):
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                yield var_type, var_name

    # TODO: Change to store only stepsize and use yield
    def init(self, sol, problem_data):
        self.sol = sol

        # Iterate through all types of variables
        for var_type, var_name in self.var_iterator():
        # for var_type in self.vars.keys():
        #     for var_name in self.vars[var_type].keys():
            # Look for the variable name from continuation in the BVP
            if var_name not in sol.aux[var_type].keys():
                raise ValueError('Variable '+var_name+' not found in boundary value problem')

            # Set current value of each continuation variable
            self.vars[var_type][var_name].value = sol.aux[var_type][var_name]
            # Calculate update steps for continuation process
            if self._spacing == 'linear':
                self.vars[var_type][var_name].steps = np.linspace(self.vars[var_type][var_name].value,
                                                                  self.vars[var_type][var_name].target,
                                                                  self._num_cases)
            elif self._spacing == 'log':
                self.vars[var_type][var_name].steps = np.logspace(np.log10(self.vars[var_type][var_name].value),
                                                                  np.log10(self.vars[var_type][var_name].target),
                                                                  self._num_cases)

    def set(self,name,target,param_type):
        """
        Sets the target value for the specified parameter
        """
        if param_type not in self.vars.keys():
            self.vars[param_type] = {}

        # Create continuation variable object
        self.vars[param_type][name] = ContinuationVariable(name,target)
        return self

    def num_cases(self,num_cases=None,spacing='linear'):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self.orig_num_cases = num_cases
            self._spacing   = spacing
            return self

        self.set('const', name, target)
        return self

    def __str__(self):
        return str(self.vars)

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        return self.next()

    def next(self, ignore_last_step = False):
        """Generator class to create BVPs for the continuation step iterations
        ignore_last_step: Should the non-convergence of previous step be ignored?
        """

        if self.sol is None:
            raise ValueError('No boundary value problem associated with this object')

        if not ignore_last_step and self.last_sol is not None and not self.last_sol.converged:
            logging.error('The last step did not converge!')
            raise RuntimeError('Solution diverged! Stopping.')

        if self.ctr >= self._num_cases:
            raise StopIteration

        # Update auxiliary variables using previously calculated step sizes
        total_change = 0.0
        for var_type in self.vars:
            for var_name in self.vars[var_type]:
                self.sol.aux[var_type][var_name] = self.vars[var_type][var_name].steps[self.ctr]
                total_change += abs(self.vars[var_type][var_name].steps[self.ctr])

        self.ctr += 1
        self.last_sol = self.sol
        return self.sol.aux


class BisectionStrategy(ManualStrategy):
    """
    Defines the bisection continuation strategy.
    """
    strategy_name = 'bisection'

    def __init__(self, initial_num_cases = 5, max_divisions=10, num_divisions = 2, vars=[], aux=None):
        super(BisectionStrategy, self).__init__(num_cases=initial_num_cases)
        self.last_sol = None
        self.num_divisions = num_divisions
        self.max_divisions = max_divisions
        self.division_ctr = 0
        self.orig_num_cases = initial_num_cases

    def __str__(self):
        return str(self.vars)

    def next(self):
        """Generator class to create BVPs for the continuation step iterations

            last_converged: Specfies if the previous continuation step converged
        """
        # If it is the first step or if previous step converged
        # continue with usual behavior
        if self.ctr == 0 or self.last_sol.converged:
            # Reset division counter
            self.division_ctr = 0
            return super(BisectionStrategy, self).next()

        # If first step didn't converge, the process fails
        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work!!')
            raise RuntimeError('Initial guess does not converge.')
            return self.last_sol

        if self.division_ctr > self.max_divisions:
            logging.error('Solution does not without exceeding max_divisions : '+str(self.max_divisions))
            raise RuntimeError('Exceeded max_divisions')

        # If previous step did not converge, move back a half step
        for var_type, var_name in self.var_iterator():
            # Set current value of each continuation variable
            # self.vars[var_type][var_name].value = aux[var_type][var_name]
            # insert new steps
            old_steps = self.vars[var_type][var_name].steps
            if self._spacing == 'linear':
                new_steps = np.linspace(old_steps[self.ctr-2],old_steps[self.ctr-1],self.num_divisions+1)
            elif self._spacing == 'log':
                new_steps = np.logspace(np.log10(old_steps[self.ctr-2]),np.log10(old_steps[self.ctr-1]),self.num_divisions+1)
            else:
                raise ValueError('Invalid spacing type')

            # Insert new steps
            self.vars[var_type][var_name].steps = np.insert(
                    self.vars[var_type][var_name].steps,
                    self.ctr-1,
                    new_steps[1:-1] # Ignore first element as it is repeated
                )
        # Move the counter back
        self.ctr = self.ctr - 1
        # Increment total number of steps
        self._num_cases = self._num_cases + self.num_divisions-1

        logging.info('Increasing number of cases to '+str(self._num_cases)+'\n')
        self.division_ctr = self.division_ctr + 1
        return super(BisectionStrategy, self).next(True)


class HPA_Variable(object):
    def __init__(self,name,target,Nnodes,spacing='linear',confined=False):
        self.name = name
        self.target = target
        self.spacing = spacing #spacing of the continuation parameter
        self.confined = confined #whether or not the search can venture beyond the limits of the grid
        self.nodes = Nnodes #number of nodes along this axis of the graph
        self.value = np.nan
        self.index = np.nan # Index of state in BVP, obsolete
        self.steps = []
