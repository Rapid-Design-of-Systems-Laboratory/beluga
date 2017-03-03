import re, inspect
from sympy import Symbol, Expr
from beluga.utils import sympify2
from beluga.optim.problem import ConstraintList

class Variable(object):
    """
    Stores a symbolic expression
    """
    def __init__(self, var):
        self._sym = Symbol(var)

    def _sympy_(self):
        """
        Make class usable as a sympy object
        """
        return self._sym

    def __call__(self, *pargs, **kargs):
        self._sym.__call__(*pargs, **kwargs)

    def __getattr__(self, attr):
        return getattr(self._sym, attr)

    def __repr__(self):
        return str(self._sym)

class Expression(object):
    """
    Stores a symbolic expression
    """
    def __init__(self, expr):
        self._sym = sympify2(expr)

    def _sympy_(self):
        """
        Make class usable as a sympy object
        """
        return self._sym

    def __call__(self, *pargs, **kargs):
        self._sym.__call__(*pargs, **kwargs)

    def __getattr__(self, attr):
        return getattr(self._sym, attr)

    def __repr__(self):
        return str(self._sym)

class DimensionalExpression(object):
    """
    Expression with unit
    """
    def __init__(self, expr, unit):
        self.expr = Expression(expr)
        self.unit = unit

    def _sympy_(self):
        """
        Make class usable as a sympy object
        """
        return self.expr._sym

class DimensionalVariable(object):
    """
    Variable with unit
    """
    def __init__(self, var, unit):
        self.var = Variable(var)
        self.unit = unit

    def _sympy_(self):
        """
        Make class usable as a sympy object
        """
        return self.var._sym

class StateVariable(object):
    """
    Variable with unit and equation
    """
    def __init__(self, var, eom, unit):
        self.var = Variable(var)
        self.eom = Expression(eom)
        self.unit = unit

class KeyValue(object):
    """
    Variable paired with expression
    """
    def __init__(self, var, expr):
        self.var = Variable(var)
        self.expr = Expression(expr)

class DynamicSystemList(list):
    """Describes a list of dynamic systems"""
    def constraints(self,select=0):
        """Returns ConstraintList object for given system in the list"""
        return self[i].constraints()

    def state(self,var,eqn,unit):
        """Adds a state to all systems in the list"""
        [s.state(var,eqn,unit) for s in self]
        return self

    def constant(self,var,val,unit):
        """Adds a state to all systems in the list"""
        [s.constant(var,val,unit) for s in self]
        return self

    def control(self,var,unit):
        """Adds a control variable to all systems in the list"""
        [s.control(var,unit) for s in self]
        return self

    def independent(self,name,unit,select=None):
        """Sets independent variable for all/some systems in the list"""
        if select is None:
            [s.independent(var,unit) for s in self]
        else:
            [self[i].independent(var,unit) for i in select]
        return self

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
        # self.parameters = []
        self.independent_var = None

    # def parameter(self,var,val=None):
    #     self.parameters.append(Constant(var,val))
    #     return self
    def independent(self,var,unit):
        self.independent_var = DimensionalVariable(var,unit)
        return self

    def state(self,var,eqn,unit):
        self.states.append(StateVariable(var,eqn,unit))
        return self

    def control(self,var,unit):
        self.controls.append(DimensionalVariable(var,unit))
        return self

    def constant(self,var,val,unit):
        self.constants.append(Constant(var,val,unit))
        return self

    def constraints(self,selection=None):
        """Returns ConstraintSet object that can be used to add constraints
        """
        return self.constraints

class Problem(object):
    """Defines problem settings."""
    def __init__(self,name):
        """Initialize all relevant problem settings."""

        self.name = self._format_name(name)

        # Get module calling this function
        frm = inspect.stack()[1]
        self.input_module = (inspect.getmodule(frm[0]))

        self.parameters = []
        self.cost = {'initial': DimensionalExpression('0','nd'),
                     'terminal': DimensionalExpression('0','nd'),
                     'path': DimensionalExpression('0','nd')}
        # self.constant = []
        self.quantity_list = []
        # self.scale = Scaling()
        self.continuation = []
        # self.execute = Execute()
        # self._constraints = ConstraintList()
        # self.steps = ContinuationList()
        # self.guess = Guess()
        self.functions = {}

        self.bvp_solver = None
        self.output_file = 'data.dill'

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

    def quantity(self, var=None, expr=None):
        if var is None and expr is None:
            return self.quantity_list
        else:
            self.quantity_list.append(KeyValue(var,expr))
            return self

    # Allows setting independent variables for select systems
    def independent(self,var,unit,name='default',select=None):
        """Sets independent variable for specified systems"""
        if select is None:
            [s.independent(var,unit) for s in self.systems[name]]
        else:
            [self.systems[name][i].independent('name_'+var,unit) for i in select]
        return self
