from ..liegroups import LieGroup
from scipy.linalg import expm
import numpy as np
from beluga.utils import keyboard

class HManifold(object):
    def __new__(cls, *args, **kwargs):
        obj = super(HManifold, cls).__new__(cls)
        if len(args) == 0:
            obj.shape = None
            obj.data = None
        elif len(args) == 1 and isinstance(args[0], LieGroup):
            obj.shape = args[0]
            obj.data = None
        elif len(args) == 2:
            obj.shape = args[0]
            obj.data = args[1]

        return obj

    def __init__(self, *args, **kwargs):
        if self.data is not None:
            self.setdata(np.array(self.data, dtype=np.float64))

    def __getitem__(self, item):
        return self.data[item]

    def left(self):
        raise NotImplementedError('Left and Right actions are only defined on a manifold of Lie-type.')

    def right(self):
        raise NotImplementedError('Left and Right actions are only defined on a manifold of Lie-type.')

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data

class HLie(HManifold):
    def __new__(cls, *args, **kwargs):
        obj = super(HLie, cls).__new__(cls, *args, **kwargs)
        return obj

    def left(self, element, coord):
        if len(element.shape) == 1:
            self.data = self.data + element
        elif coord == 'exp':
            self.data = np.dot(expm(element), self.data)
        else:
            return NotImplementedError

    def right(self, element, coord):
        if len(element.shape) == 1:
            self.data = element + self.data
        elif coord == 'exp':
            self.data = np.dot(self.data, expm(element))
        else:
            return NotImplementedError
