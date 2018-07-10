from .brysonho import *
from .optimlib import *
from .icrm import *
from .diffyg import *

# from .brysonho import ocp_to_bvp

methods = {'traditional': BrysonHo, 'icrm': ICRM, 'brysonho': BrysonHo}
