class DynamicSystem(object):
    """Represents a class of dynamic systems with its own states, dynamic equations, constants and constraints"""
    #
    __ctr = 0
    
    def __init__(self):
        _constraints = ConstraintSet()
        
    def state(self,var,eqn,unit):
        pass
    def const(self,var,val,unit):
        pass
        
    def constraints():
        """Returns ConstraintSet object that can be used to add constraints
        """
        return self._constraints
        pass
        
    def count(self,num):
        pass
    pass