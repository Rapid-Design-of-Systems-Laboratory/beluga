from sympy import Symbol
class Variable(object):
    """Defines variable information."""

    def __init__(self, var = '', unit = ''):
        """
        Input: var (string)
               unit (string)
        """
        self.var = var
        self.unit = unit
        self.sym = Symbol(var)
        # super().__init__(self)

    def __repr__(self):
        return self.var

    def __str__(self):
        return self.var
