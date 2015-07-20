# from autodiff import Function, Gradient
import numpy as np

from .. import Solution
from beluga.utils.ode45 import ode45
from ..Algorithm import Algorithm
from math import *

from beluga.utils.joblib import Memory

class GACPI(Algorithm):
    """
    Class that implements the Generalized Adaptive Chebyshev-Picard Iteration
       method in Python
    """
    def solve(self,bvp):
        """Solves the given BVP"""

        pass
