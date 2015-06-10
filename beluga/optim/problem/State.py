from sympy import Symbol
class State(object):
    """Defines state information."""

    # # Required so that subclassing works
    # # Symbol class only has a __new__ method and not __init__
    # def __new__(cls, var = '', eqn='', unit = ''):
    #     return Symbol.__new__(cls,var)

    def __init__(self, var = 'x', process_eqn = '-x', unit = 'nd', indep_var = 't'):
        """
            Input: independent variable (string)
                   variable name (string)
                   process equation (string)
                   unit (string)
        """
        self.indep_var = indep_var
        self.state_var = var
        self.unit = unit
        self.process_eqn = process_eqn
        self.sym = Symbol(var)

    # Allows comparison with strings
    # Probably needs to be made more robust
    def __eq__(self,other):
        return (self.state_var == other)

    def __ne__(self,other):
        return not self.__eq__(other)

    def __str__(self):
        """Returns a string representation of the state variable"""
        return self.state_var
    def __repr__(self):
        return self.state_var
        
    def add_prefix(self,prefix):
        """Adds a prefix to the name of the state variable"""
        self.state_var = prefix+self.state_var
        return self

    def make_costate(self):
        """Creates costate variable."""
        return 'lagrange_' + self.state_var
