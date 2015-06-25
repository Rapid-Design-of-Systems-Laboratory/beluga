from .ode45 import ode45
from .keyboard import keyboard
from .Timer import Timer
from .tictoc import tic, toc
from .fix_carets import fix_carets
from .sympify2 import sympify2
from .ode45_old import ode45_old
from .ode45 import ode45_multi

from .static_var import static_var
from .SingletonMetaClass import SingletonMetaClass

__all__ = ['tic','toc']

import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ += ([ os.path.basename(f)[:-3] for f in modules])
