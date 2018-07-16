from .helpers import root
from .beluga import bvp_algorithm, guess_generator
from .continuation import ContinuationList as init_continuation
from .beluga import setup_beluga, solve
from .problem import OCP

import os
import glob

__version__ = '0.2.0'

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]