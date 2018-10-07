from .helpers import root
from .beluga import bvp_algorithm, guess_generator
from .continuation import ContinuationList as init_continuation
from .beluga import solve, add_logger, set_output_file
from .problem import OCP
from .scaling import Scaling

import os
import glob

from beluga.release import __version__

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]