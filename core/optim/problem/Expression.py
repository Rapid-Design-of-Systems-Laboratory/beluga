# from sympy import Expr
class Expression(object):
    """Defines expression information."""

    def __init__(self, expr = '', unit = ''):
        """
        Input: expr (string)
               unit (string)
        """
        self.expr = expr
        self.unit = unit
        # Not yet calling superclass yet


    # add expression operations for optimal control calculations
