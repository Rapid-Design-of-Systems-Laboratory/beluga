from .BaseAlgorithm import BaseAlgorithm
from .SingleShooting import SingleShooting
from .MultipleShooting import MultipleShooting
from .ParallelShooting import ParallelShooting
#from .MultipleShooting_mike import MultipleShooting_mike
from .QCPI import QCPI
# from .QCPI_Parallel import QCPI_Parallel
# from ScikitsBVPSolver import ScikitsBVPSolver
# __all__ = ['SingleShooting']
import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
