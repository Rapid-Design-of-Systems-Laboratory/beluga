from .brysonho import BrysonHo
from .icrm import ICRM

from .optimlib import *

# from .brysonho import ocp_to_bvp

methods = {'traditional': BrysonHo, 'icrm': ICRM, 'brysonho': BrysonHo}
