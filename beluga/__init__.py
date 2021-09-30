from numpy import float64

from .beluga import solve
from .continuation import guess_generator, GuessGenerator, ContinuationList as init_continuation
from .data_classes.symbolic_problem import SymbolicProblem as Problem
from .release import __version__, __splash__
from .solvers import bvp_solvers
from .solvers.bvp_solvers import bvp_algorithm
from .utils.logging import logger, add_logger, make_a_splash

DTYPE = float64
