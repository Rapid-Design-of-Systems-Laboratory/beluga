# from abc import ABC, abstractmethod
class Strategy(object):
    # Compute necessary conditions (DAE or Analytic)
    # Generate BVP object (solver-specific). Maybe call method in solver?
    # Generate initial guess
    # Perform Continuation

    def __init__(self):
        self.__actions = []

    def add_action(self, func, *args, **kwargs):
        self.__actions.append((func, args, kwargs))

    def execute(self):
        for action in self.__actions:
            action[0](*action[1], **action[2])
