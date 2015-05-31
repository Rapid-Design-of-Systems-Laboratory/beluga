
class State(object):
    """Defines state information."""

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

    # Allows comparison with strings
    # Probably needs to be made more robust
    def __eq__(self,other):
        return (self.state_var == other)

    def __ne__(self,other):
        return not self.__eq__(other)

    def make_costate(self):
        """Creates costate variable."""
        return 'lagrange_' + self.state_var
