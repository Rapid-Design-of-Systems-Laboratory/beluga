from beluga.utils.logging import root, init_logging, logger
from .beluga import solve, add_logger
from .numeric import bvp_solvers
from .continuation import guess_generator, GuessGenerator
from .continuation import ContinuationList as init_continuation
from .numeric.compilation import LocalCompiler
from .symbolic import Problem
from .numeric.bvp_solvers import bvp_algorithm
import numpy
from beluga.release import __version__, __splash__

DTYPE = numpy.float64
