from .BelugaPlot import BelugaPlot
# from .BelugaPlot2 import BelugaPlot2

import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
