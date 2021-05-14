import numpy

from .beluga import solve
from .solvers import bvp_solvers
from .continuation import guess_generator, GuessGenerator
from .continuation import ContinuationList as init_continuation
from .data_classes.symbolic_problem import Problem
from .solvers.bvp_solvers import bvp_algorithm
from .release import __version__, __splash__
from .utils.logging import logger, add_logger, make_a_splash

DTYPE = numpy.float64
