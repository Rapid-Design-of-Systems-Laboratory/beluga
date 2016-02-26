from .strategies.ManualStrategy import ManualStrategy
from beluga.continuation import strategies
# from .ContinuationSolution import ContinuationSolution

import inspect
class ContinuationList(list):
    def __init__(self):
        # Create list of available strategies
        self.strategy_list = {obj.name: obj  for (name,obj) in inspect.getmembers(strategies) if inspect.isclass(obj)}

    def add_step(self, strategy='manual', *args, **kwargs):
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
