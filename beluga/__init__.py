from beluga.utils.logging_helper import root
from .beluga import solve, add_logger
from .numeric import bvp_solvers
from .continuation import guess_generator, GuessGenerator
from .continuation import ContinuationList as init_continuation
from functools import partial
from .numeric.compilation import LocalCompiler
from .symbolic import Problem
from .numeric.bvp_solvers import bvp_algorithm
import numpy
from beluga.release import __version__, __splash__

import logging
logging.beluga = partial(logging.log, logging.DEBUG + 5)

# modules = glob.glob(os.path.dirname(__file__)+"/*.py")
# __all__ = [os.path.basename(f)[:-3] for f in modules]

DTYPE = numpy.float64
