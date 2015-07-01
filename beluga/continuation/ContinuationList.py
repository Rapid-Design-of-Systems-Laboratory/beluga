from .ContinuationStep import ContinuationStep
# from .ContinuationSolution import ContinuationSolution

class ContinuationList(list):
    def add_step(self, step=None):
        if step is None:
            step = ContinuationStep()
        self.append(step)
        return step
