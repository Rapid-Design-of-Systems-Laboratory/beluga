
class Expression(object):
    """Defines expression information."""
    
    def __init__(self, expr = '', unit = ''):
        """
        Input: expr (string)
               unit (string)
        """
        self.expr = expr
        self.unit = unit
        
        
    # add expression operations for optimal control calculations