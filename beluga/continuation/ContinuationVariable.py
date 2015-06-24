import numpy as np
class ContinuationVariable(object):
    def __init__(self,name,target):
        self.name = name
        self.target = target
        self.value = np.nan
        self.index = np.nan # Index of state in BVP, obsolete
        self.steps = []
        
    def set_value(self, val):
        self.value = val