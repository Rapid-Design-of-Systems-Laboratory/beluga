from .Solution import Solution
from .BaseAlgorithm import BaseAlgorithm
from .Shooting import Shooting
from .Collocation import Collocation
from .Pseudospectral import Pseudospectral

# __all__ = ['Algorithm','Solution','BVP','FunctionTemplate','bvpinit']
import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
