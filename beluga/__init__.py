from beluga.utils.logging_helper import root
from .beluga import bvp_algorithm, guess_generator, run_continuation_set, solve, add_logger
from .numeric import bvp_solvers
from .continuation import GuessGenerator
from .continuation import ContinuationList as init_continuation
# from .problem import OCP

from .numeric.compilation import LocalCompiler
from .symbolic import Problem


from beluga.release import __version__, __splash__

# modules = glob.glob(os.path.dirname(__file__)+"/*.py")
# __all__ = [os.path.basename(f)[:-3] for f in modules]

import numpy
DTYPE = numpy.float64

