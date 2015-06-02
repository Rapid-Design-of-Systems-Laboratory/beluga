from .Variable import Variable
class Constant(Variable):
    """Defines constant information."""

# Required so that subclassing works
# Symbol class only has a __new__ method and not __init__
    # @classmethod
    # def __new__(cls, var = '', val='', unit = ''):
    #     return Symbol.__new__(cls,var)

    def __init__(self, var = '', val='', unit = ''):
        """
        Input: var (string)
               unit (string)
               val (float)
        """
        self.var = var
        self.unit = unit
        self.val = val
        super().__init__(var,unit)
