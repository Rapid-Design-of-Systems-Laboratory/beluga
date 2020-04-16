from .helpers import root
from .continuation import ContinuationList as init_continuation
from .codegen import *
from .problib import *
# from .problem import OCP
from .scaling import Scaling
from .problib.ocp_classes import InputOCP as OCP
from .problib.bvp_classes import InputBVP as BVP

import os
import glob

from beluga.release import __version__, __splash__

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]
