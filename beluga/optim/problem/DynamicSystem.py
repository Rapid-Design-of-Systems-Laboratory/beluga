from beluga.optim.problem import Variable, State, Constant, ConstraintList
class DynamicSystem(object):
    """Represents a class of dynamic systems with its own states, dynamic equations, constants and constraints"""
    #
    # __ctr = {}

    def __init__(self,name='default'):
        self.constraints = ConstraintList()
        self.states = []
        self.controls = []
        self.name = name
        self.constants = []
        self.independent_var = None

    def independent(self,var,unit):
        self.independent_var = Variable(var,unit)
        return self

    def state(self,var,eqn,unit):
        self.states.append(State(var,eqn,unit))
        return self

    def control(self,var,unit):
        self.controls.append(Variable(var,unit))
        return self

    def constant(self,var,val,unit):
        self.constants.append(Constant(var,val,unit))
        return self

    def constraints(self,selection=None):
        """Returns ConstraintSet object that can be used to add constraints
        """
        return self.constraints
