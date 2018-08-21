from beluga.liepack.domain.liegroups import LieGroup
import copy
from scipy.linalg import expm
import numpy as np
from beluga.utils import keyboard

class HManifold(object):
    def __new__(cls, *args, **kwargs):
        obj = super(HManifold, cls).__new__(cls)
        obj.shape = None
        obj.data = None
        if len(args) > 0 and isinstance(args[0], HManifold):
            obj = copy.copy(args[0])
        if len(args) > 0 and isinstance(args[0], LieGroup):
            obj.shape = args[0]

        if len(args) > 1:
            obj.data = args[1]

        return obj

    def __init__(self, *args, **kwargs):
        if self.data is not None:
            self.setdata(np.array(self.data, dtype=np.float64))

    def __getitem__(self, item):
        return self.data[item]

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data

class HLie(HManifold):
    def __new__(cls, *args, **kwargs):
        obj = super(HLie, cls).__new__(cls, *args, **kwargs)
        return obj

    # def left(self, element, coord):
    #     if coord == 'exp':
    #         self.data = np.dot(expm(element.data), self.data)
    #     else:
    #         return NotImplementedError
    #
    # def right(self, element, coord):
    #     if coord == 'exp':
    #         self.data = np.dot(self.data, expm(element.data))
    #     else:
    #         return NotImplementedError
