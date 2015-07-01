from sympy import Expr
from beluga.utils import sympify2

class Constraint(Expr):
    """Defines constraint information."""
    # NEED TO ADD PATH CONSTRAINT

    def __init__(self, type = '', expr = '', unit = '', preprocess=True):
        """
        Input: type (string)
               expr (string)
               unit (string)
        """
        self.type = type
        self.expr = expr
        self.unit = unit
        # super().__init__()

    def __str__(self):
        "Returns constraint expression when object is converted to a string"
        return self.expr

    def make_multiplier(self, ind = 1):
        return 'lagrange_' + self.type + '_' + str(ind)

    def make_aug_cost(self, ind = 1):
        """Return augmented cost expression."""

        return sympify2(self.make_multiplier(ind) + '*(' + self.expr + ')')
