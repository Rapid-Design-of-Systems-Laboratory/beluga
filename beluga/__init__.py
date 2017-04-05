# Must be defined first!
#from .BelugaConfig import BelugaConfig
# from .Beluga import Beluga

# __all__ = ['BoundaryConditions','Hamiltonian','NecessaryConditions']
# __all__ = ['Beluga']

from .problem2 import OCP
from .Beluga import get_algorithm as bvp_algorithm
from .problem2 import Guess as initial_guess
from .continuation import ContinuationList as init_continuation
from .Beluga import solve

import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
