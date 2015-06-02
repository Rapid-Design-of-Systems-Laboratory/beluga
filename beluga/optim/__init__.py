#from .BoundaryConditions import BoundaryConditions
#from .Hamiltonian import Hamiltonian
from .Problem import Problem
from .Guess import Guess
from .NecessaryConditions import NecessaryConditions

# __all__ = ['BoundaryConditions','Hamiltonian','NecessaryConditions']
# __all__ = ['NecessaryConditions']
import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
