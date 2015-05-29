
class Constraint(object):
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
        
    def make_aug_cost(self, ind = 1):
        """Return augmented cost expression."""
        return 'lagrange_' + self.type + '_' + str(ind) + '*(' + \
            self.expr + ')'