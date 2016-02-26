from .ManualStrategy import ManualStrategy
from .BisectionStrategy import BisectionStrategy

# __all__ = ["I will get rewritten"]
# # Don't modify the line above, or this line!
# import automodinit
# automodinit.automodinit(__name__, __file__, globals())
# del automodinit
# # Anything else you want can go after here, it won't get modified.

import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
