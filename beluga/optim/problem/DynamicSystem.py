class DynamicSystem(object):
    """Represents a class of dynamic systems with its own states, dynamic equations, constants and constraints"""
    #
    __ctr = 0

    def __init__(self):
        self.constraints = ConstraintSet()
        self.states = []
        self.controls = []
        self.constants = []

    def state(self,var,eqn,unit):
        self.states.append(State(var,eqn,unit))
        pass
    def constant(self,var,val,unit):
        self.states.append(Variable(var,val,unit))
        pass

    def constraints(self,selection=None):
        """Returns ConstraintSet object that can be used to add constraints
        """
        return self.constraints
        pass

    def count(self,num):
        pass
