from .ContinuationStep import ContinuationStep
from .ContinuationSolution import ContinuationSolution

class ContinuationSet(list):
    def add_step(self, step=None):
        if step is None:
            return ContinuationStep()
        else:
            self.append(step)
            return step