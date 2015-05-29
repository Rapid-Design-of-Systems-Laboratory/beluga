from .ContinuationStep import ContinuationStep
from .ContinuationSolution import ContinuationSolution

class ContinuationSet(list):
    def add_step(self, step=None):
        if step is None:
            step = ContinuationStep()
        self.append(step)
        return step