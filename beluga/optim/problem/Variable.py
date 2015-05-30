
class Variable(object):
    """Defines variable information."""

    def __init__(self, var = '', val = None, unit = ''):
        """
        Input: var (string)
               unit (string)
        """
        self.var = var
        self.unit = unit
        self.val = val
