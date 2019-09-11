import abc
import copy
import numpy as np
import logging
import inspect
import itertools
import functools
import sys


def gamma_norm(const1, const2):
    norm = sum(abs(const2 - const1))
    return norm


class ContinuationList(list):
    def __init__(self):

        list.__init__(self)

        # Create list of available strategies
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        self.strategy_list = {
            obj.strategy_name: obj
            for (name, obj) in clsmembers
            if hasattr(obj, 'strategy_name')
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


class ContinuationStrategy(abc.ABC):
    def __init__(self, *args, **kwargs):
        self.solution_reference = None
        self.gammas = []
        self.vars = {}
        self.ctr = None
        self.bvp = None

    def __str__(self):
        return str(self.vars)

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        return self.next()

    def __len__(self):
        return self.num_cases()

    def add_gamma(self, gamma):
        self.gammas.append(copy.deepcopy(gamma))

    def get_closest_gamma(self, const):
        norms = []
        for traj in self.gammas:
            if traj.converged is False:
                norms.append(9e99)
            else:
                norms.append(gamma_norm(traj.const, const))

        return np.argmin(norms)

    def init(self, gamma, bvp):
        self.bvp = bvp
        for var_name in self.var_iterator():
            if var_name not in self.bvp.raw['constants']:
                raise ValueError('Variable ' + var_name + ' not found in boundary value problem')
        gamma_in = copy.deepcopy(gamma)
        gamma_in.converged = False
        self.gammas = [gamma_in]

    def next(self, ignore_last_step=False):
        if len(self.gammas) is 0:
            raise ValueError('No boundary value problem associated with this object')

        if not ignore_last_step and len(self.gammas) is not 1 and not self.gammas[-1].converged:
            logging.error('The last step did not converge!')
            raise RuntimeError('Solution diverged! Stopping.')

        if self.ctr >= self.num_cases():
            raise StopIteration

        # Update auxiliary variables using previously calculated step sizes
        total_change = 0.0
        const0 = copy.deepcopy(self.gammas[-1].const)
        for var_name in self.vars:
            jj = self.bvp.raw['constants'].index(var_name)
            const0[jj] = self.vars[var_name].steps[self.ctr]
            total_change += abs(self.vars[var_name].steps[self.ctr])

        i = self.get_closest_gamma(const0)
        gamma_guess = copy.deepcopy(self.gammas[i])
        gamma_guess.const = const0
        self.ctr += 1
        logging.debug('CHOOSE\ttraj #' + str(i) + ' as guess.')
        return gamma_guess

    def var_iterator(self):
        for var_name in self.vars.keys():
            yield var_name

    def num_cases(self):
        pass


class ManualStrategy(ContinuationStrategy):
    """
    Class defining the manual continuation strategy.
    """
    # A unique short name to select this class
    strategy_name = 'manual'

    def __init__(self, num_cases=1, vars=None):  # TODO change vars to other variable name to avoid overwriting
        super(ManualStrategy, self).__init__()
        self._num_cases = num_cases
        self._spacing = 'linear'
        if vars is None:
            self.vars = {}
        else:
            self.vars = vars  # dictionary of values
        self.ctr = 0   # iteration counter
        self.last_sol = None

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

    # TODO: Change to store only stepsize and use yield
    def init(self, sol, bvp):
        super(ManualStrategy, self).init(sol, bvp)

        # Iterate through all types of variables
        for var_name in self.var_iterator():
            if var_name not in bvp.raw['constants']:
                raise ValueError('Variable ' + var_name + ' not found in boundary value problem')

            # Set current value of each continuation variable
            jj = bvp.raw['constants'].index(var_name)
            self.vars[var_name].value = sol.const[jj]
            # Calculate update steps for continuation process
            if self._spacing == 'linear':
                self.vars[var_name].steps = np.linspace(self.vars[var_name].value,
                                                                  self.vars[var_name].target,
                                                                  self._num_cases)
            elif self._spacing == 'log':
                self.vars[var_name].steps = np.logspace(np.log10(self.vars[var_name].value),
                                                                  np.log10(self.vars[var_name].target),
                                                                  self._num_cases)

    def set(self, name, target, param_type):
        """
        Sets the target value for the specified parameter
        """
        # Create continuation variable object
        self.vars[name] = ContinuationVariable(name, target)
        return self

    def num_cases(self, num_cases=None, spacing='linear'):
        if num_cases is None:
            return self._num_cases

        if self.ctr > 0:
            raise RuntimeError('Cannot set num_cases during iteration')

        self._num_cases = num_cases
        self.orig_num_cases = num_cases
        self._spacing = spacing
        return self


class BisectionStrategy(ManualStrategy):
    """
    Defines the bisection continuation strategy.
    """
    strategy_name = 'bisection'

    def __init__(self, initial_num_cases=5, max_divisions=10, num_divisions=2):
        super(BisectionStrategy, self).__init__(num_cases=initial_num_cases)
        self.last_sol = None
        self.num_divisions = num_divisions
        self.max_divisions = max_divisions
        self.division_ctr = 0
        self.orig_num_cases = initial_num_cases

    def __str__(self):
        return str(self.vars)

    def next(self, ignore_last_step=False):
        """Generator class to create BVPs for the continuation step iterations

        last_converged: Specfies if the previous continuation step converged
        """
        # If it is the first step or if previous step converged
        # continue with usual behavior
        if self.ctr == 0 or self.gammas[-1].converged:
            # Reset division counter
            self.division_ctr = 0
            return super(BisectionStrategy, self).next()

        # If first step didn't converge, the process fails
        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work.')
            raise RuntimeError('Initial guess does not converge.')
            # return self.gammas[-1]

        if self.division_ctr > self.max_divisions:
            logging.error('Solution does not without exceeding max_divisions : '+str(self.max_divisions))
            raise RuntimeError('Exceeded max_divisions')

        # If previous step did not converge, move back a half step
        for var_name in self.var_iterator():
            old_steps = self.vars[var_name].steps
            if self._spacing == 'linear':
                new_steps = np.linspace(old_steps[self.ctr-2], old_steps[self.ctr-1], self.num_divisions+1)
            elif self._spacing == 'log':
                new_steps = np.logspace(np.log10(old_steps[self.ctr-2]), np.log10(old_steps[self.ctr-1]),
                                        self.num_divisions+1)
            else:
                raise ValueError('Invalid spacing type')

            # Insert new steps
            self.vars[var_name].steps = np.insert(
                    self.vars[var_name].steps,
                    self.ctr-1,
                    new_steps[1:-1]  # Ignore first element as it is repeated
                )
        # Move the counter back
        self.ctr = self.ctr - 1
        # Increment total number of steps
        self._num_cases = self._num_cases + self.num_divisions-1

        logging.debug('Increasing number of cases to '+str(self._num_cases)+'\n')
        self.division_ctr = self.division_ctr + 1
        return super(BisectionStrategy, self).next(True)


class ProductStrategy(ContinuationStrategy):
    """
    Defines the bisection continuation strategy.
    """
    strategy_name = 'productspace'

    def __init__(self, num_subdivisions=1, sol=None):
        ContinuationStrategy.__init__(self)
        self.sol = sol
        self.sols = []
        self._num_cases = None
        self._num_subdivisions = num_subdivisions
        self.vars = {}  # dictionary of values
        self.ctr = 0  # iteration counter

        self.const = functools.partial(self.set, param_type='const')
        self.constant = self.const

        self.last_sol = None
        self.orig_num_cases = None

    def __str__(self):
        return str(self.vars)

    def next(self, ignore_last_step=False):
        if self.ctr == 0 or self.gammas[-1].converged:
            # Reset division counter
            self.division_ctr = 0
            return super(ProductStrategy, self).next(False)

        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work.')
            raise RuntimeError('Initial guess does not converge.')

        return super(ProductStrategy, self).next(True)

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_sol = None

    def set(self, name, target, param_type):
        """
        Sets the target value for the specified parameter
        """
        self.vars[name] = ContinuationVariable(name, target)
        return self

    def init(self, sol, bvp):
        super(ProductStrategy, self).init(sol, bvp)

        num_vars = len(self.vars)
        self.num_cases(self.num_subdivisions() ** num_vars)
        for var_name in self.vars.keys():
            jj = bvp.raw['constants'].index(var_name)
            self.vars[var_name].value = sol.const[jj]

        ls_set = [np.linspace(self.vars[var_name].value, self.vars[var_name].target,
                              self._num_subdivisions) for var_name in self.vars.keys()]
        for val in itertools.product(*ls_set):
            ii = 0
            for var_name in self.vars.keys():
                self.vars[var_name].steps.append(val[ii])
                ii += 1

    # def next(self, ignore_last_step=False):
    #     if len(self.gammas) == 0:
    #         raise ValueError('No boundary value problem associated with this object')
    #
    #     if not ignore_last_step and self.last_sol is not None and not self.last_sol.converged:
    #         logging.error('The last step did not converge!')
    #         raise RuntimeError('Solution diverged! Stopping.')
    #
    #     if self.ctr >= self._num_cases:
    #         raise StopIteration
    #
    #     # Update auxiliary variables using previously calculated step sizes
    #     total_change = 0.0
    #     for var_type in self.vars:
    #         for var_name in self.vars[var_type]:
    #             self.sol.aux[var_type][var_name] = self.vars[var_type][var_name].steps[self.ctr]
    #             total_change += abs(self.vars[var_type][var_name].steps[self.ctr])
    #
    #     self.ctr += 1
    #     # if self.ctr % self.num_subdivisions() == 1 and self.ctr != 1:
    #     #     aux = copy.deepcopy(self.sol.aux)
    #     #     self.sol = self.sols[-self.num_subdivisions()]
    #     #     self.sol.aux = aux
    #
    #     self.sols.append(copy.deepcopy(self.sol))
    #     self.last_sol = self.sol
    #     return copy.deepcopy(self.sol)

    def num_cases(self, num_cases=None):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self.orig_num_cases = num_cases
            return self

    def num_subdivisions(self, num_subdivisions=None):
        if num_subdivisions is None:
            return self._num_subdivisions
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')
            self._num_subdivisions = num_subdivisions
            return self
