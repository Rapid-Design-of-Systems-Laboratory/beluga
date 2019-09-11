from .helpers import root
from .beluga import bvp_algorithm, guess_generator, ocp2bvp, run_continuation_set, solve, add_logger, bvpsol
from .continuation import ContinuationList as init_continuation
from .problem import OCP
from .scaling import Scaling

import os
import glob

from beluga.release import __version__, __splash__

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]
