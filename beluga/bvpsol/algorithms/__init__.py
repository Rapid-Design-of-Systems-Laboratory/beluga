from .SingleShooting import SingleShooting
from .MultipleShooting_Thomas import MultipleShooting_Thomas

# from ScikitsBVPSolver import ScikitsBVPSolver
# __all__ = ['SingleShooting']
import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
