from ..ContinuationVariable import ContinuationVariable
from .ManualStrategy import ManualStrategy
import numpy as np
import logging

# Can be subclassed to allow automated stepping
class BisectionStrategy(ManualStrategy):
    """Defines one continuation step in continuation set"""
    # A unique short name to select this class
    name = 'bisection'

    def __init__(self, initial_num_cases = 5, max_divisions=10, num_divisions = 2, vars=[], bvp=None):
        super(BisectionStrategy, self).__init__(num_cases=initial_num_cases)
        self.last_bvp = None
        self.num_divisions = num_divisions
        self.max_divisions = max_divisions
        self.division_ctr = 0

    def next(self):
        """Generator class to create BVPs for the continuation step iterations

            last_converged: Specfies if the previous continuation step converged
        """
        # If it is the first step or if previous step converged
        # continue with usual behavior
        if self.ctr == 0 or self.last_bvp.solution.converged:
            # Reset division counter
            self.division_ctr = 0
            return super(BisectionStrategy, self).next()

        # If first step didn't converge, the process fails
        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work!!')
            raise RuntimeError('Initial guess does not converge.')
            return self.last_bvp

        if self.division_ctr > self.max_divisions:
            logging.error('Solution does not without exceeding max_divisions : '+str(self.max_divisions))
            raise RuntimeError('Exceeded max_divisions')

        # If previous step did not converge, move back a half step
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                # Set current value of each continuation variable
                # self.vars[var_type][var_name].value = bvp.solution.aux[var_type][var_name]
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
