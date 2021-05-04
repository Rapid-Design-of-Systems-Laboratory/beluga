from beluga.utils.logging import root, init_logging, logger
from .beluga import solve, add_logger
from .numeric_solvers import bvp_solvers
from .continuation import guess_generator, GuessGenerator
from .continuation import ContinuationList as init_continuation
from .compilation import LocalCompiler
from .symbolic_manipulation import Problem
from beluga.numeric_solvers.bvp_solvers import bvp_algorithm
import numpy
from beluga.release import __version__, __splash__

DTYPE = numpy.float64
