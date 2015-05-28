from optim import Hamiltonian, BoundaryConditions

class NecessaryConditions(object):
    """Defines necessary conditions of optimality."""
    
    def __init__(self):
        """Initializes all of the relevant necessary conditions."""
        self.costate = []
        self.ham = Hamiltonian()
        self.control = []
        self.aug_cost = {}
        self.bc = BoundaryConditions()

