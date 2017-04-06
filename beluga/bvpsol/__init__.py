from .ode45 import ode45
from .Scaling import Scaling
from .Solution import Solution
from .bvpinit import bvpinit
from .BVP import BVP
# from .FunctionTemplate import FunctionTemplate
from .Algorithm import Algorithm


# __all__ = ['Algorithm','Solution','BVP','FunctionTemplate','bvpinit']
import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
