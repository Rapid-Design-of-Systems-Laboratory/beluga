
class State(object):
    """Defines state information."""
    
    def __init__(self, indep_var = 't', var = 'x', process_eqn = '-x', unit = 'nd'):
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
        
    def make_costate(self):
        """Creates costate variable."""
        return 'lagrange_' + self.state_var