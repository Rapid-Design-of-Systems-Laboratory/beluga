from .ContinuationVariable import ContinuationVariable
from .ContinuationStep import ContinuationStep
import numpy as np

# Can be subclassed to allow automated stepping
class ContinuationStepBisection(ContinuationStep):
    """Defines one continuation step in continuation set"""

    def __init__(self, initial_num_cases = 10, num_divisions = 2, vars=[], bvp=None):
        super(ContinuationStepBisection, self).__init__(num_cases=initial_num_cases)
        self.last_bvp = None
        self.num_divisions = num_divisions

    def num_cases(self,num_cases=None):
        if num_cases is not None:
            raise RuntimeError('Cannot set num_cases on automated continuation object')
        return super(ContinuationStepBisection, self).num_cases()

    def next(self):
        """Generator class to create BVPs for the continuation step iterations

            last_converged: Specfies if the previous continuation step converged
        """
        # If it is the first step or if previous step converged
        # continue with usual behavior
        if self.ctr == 0 or self.last_bvp.solution.converged:
            return super(ContinuationStepBisection, self).next()

        # If first step didn't converge, the process fails
        if self.ctr == 1:
            raise RuntimeError('Initial guess should converge for automated continuation to work!!')
            return self.last_bvp

        # If previous step did not converge, move back a half step
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                # Set current value of each continuation variable
                # self.vars[var_type][var_name].value = bvp.solution.aux[var_type][var_name]
                # insert new steps
                old_steps = self.vars[var_type][var_name].steps
                new_steps = np.linspace(old_steps[self.ctr-2],old_steps[self.ctr-1],self.num_divisions+1)

                # Insert new steps
                self.vars[var_type][var_name].steps = np.insert(self.vars[var_type][var_name].steps,
                                                                self.ctr-1,
                                                                new_steps[1:-1] # Ignore repeated elements
                                                                )
        self.ctr = self.ctr - 1
        return super(ContinuationStepBisection, self).next()
