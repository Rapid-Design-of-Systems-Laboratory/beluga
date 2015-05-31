from .Variable import Variable
class Constant(Variable):
    """Defines constant information."""

    def __init__(self, var = '', val='', unit = ''):
        """
        Input: var (string)
               unit (string)
               val (float)
        """
        self.var = var
        self.unit = unit
        self.val = val
