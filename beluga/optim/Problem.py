from beluga.optim.problem import Expression, Execute, ConstraintList, DynamicSystem, DynamicSystemList, Guess
from beluga.continuation import ContinuationList
# from os import getcwd

class Problem(object):
    """Defines problem settings."""
    def __init__(self):
        """Initialize all relevant problem settings."""
        # self.indep_var = []
        # self.states = []
        # self.controls = []
        self.parameters = []
        self.cost = {'initial': Expression('0','nd'),
                     'terminal': Expression('0','nd'),
                     'path': Expression('0','nd')}
        # self.constant = []
        self.quantity = []
        self.scale = []
        self.continuation = []
        self.execute = Execute();
        self._constraints = ConstraintList()
        self.steps = ContinuationList()
        self.guess = Guess()

        self.systems = {} # List of dynamic system

        self.system()   # Create default dynamic system

        # self.get_initial_guess = getcwd() + '/get_initial_guess.py'
        # self.data_folder = getcwd() + '/data'


    def system(self,name='default', count=1):
        """Create new DynamicSystem objcts with given name"""
        # Replaces existing systems with same name
        self.systems[name] = DynamicSystemList(
                    [DynamicSystem(name) for i in range(count)]
        )
        return self.systems[name]

    # The folowing are alias functions to access a single system
    # Possible way to generate these automatically?
    def constraints(self,name='default',index=0):
        return self.systems[name][index].constraints

    def states(self,name='default',index=0):
        return self.systems[name][index].states

    def controls(self,name='default',index=0):
        return self.systems[name][index].controls

    def constants(self,name='default',index=0):
        return self.systems[name][index].constants


    # Setter functions that allow chaining
    def state(self,var,eqn,unit,name='default',index=0):
        """Adds a state to given system"""
        return self.systems[name][index].state(var,eqn,unit)

    def constant(self,var,val,unit,name='default',index=0):
        """Adds a constant to given system"""
        return self.systems[name][index].constant(var,val,unit)

    def control(self,var,unit,name='default',index=0):
        """Adds a control variable to given system"""
        return self.systems[name][index].control(var,unit)

    # Allows setting independent variables for select systems
    def independent(self,var,unit,name='default',select=None):
        """Sets independent variable for specified systems"""
        if select is None:
            [s.independent(var,unit) for s in self.systems[name]]
        else:
            [self.systems[name][i].independent('name_'+var,unit) for i in select]
        return self
