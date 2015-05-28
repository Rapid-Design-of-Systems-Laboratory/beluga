
class Execute(object):
    """Defines execution control settings."""
    
    def __init__(self):
        """Initialize various execution control variables."""
        self.necessary_conditions = True
        self.continuation = True
        self.verbose = True
        self.skip_unconverged_solutions = True