from beluga.optim.problem import Expression, Execute, ConstraintList, DynamicSystem, DynamicSystemList, Guess
from beluga.continuation import ContinuationList
# from os import getcwd
from .Scaling import Scaling
import inspect
import re

class Problem(object):
    """Defines problem settings."""
    def __init__(self,name):
        """Initialize all relevant problem settings."""

        self.name = self._format_name(name)

        # Get module calling this function
        frm = inspect.stack()[1]
        self.input_module = (inspect.getmodule(frm[0]))
        
        self.parameters = []
        self.cost = {'initial': Expression('0','nd'),
                     'terminal': Expression('0','nd'),
                     'path': Expression('0','nd')}
        # self.constant = []
        self.quantity = []
        self.scale = Scaling()
        self.continuation = []
        self.execute = Execute();
        self._constraints = ConstraintList()
        self.steps = ContinuationList()
        self.guess = Guess()
        self.functions = {}

        self.systems = {} # List of dynamic system

        self.system()   # Create default dynamic system

        # self.get_initial_guess = getcwd() + '/get_initial_guess.py'
        # self.data_folder = getcwd() + '/data'


    def _format_name(self, name):
        """Validates that the name is in the right format
            Only alphabets, numbers and underscores allowed
            Should not start with a number or underscore
        """

        if re.match(r'[a-zA-Z]\w+',name):
            return name
        else:
            raise ValueError("""Invalid problem name specified.
            Only alphabets, numbers and underscores allowed
            Should start with an alphabet""")

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

    def indep_var(self,name='default',index=0):
        return self.systems[name][index].independent_var


    def function(self,name,handle):
        # from functools import *
        self.functions[name] = handle
        return self

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
