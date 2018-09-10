import abc
import copy

from beluga.utils import keyboard

import numpy as np

class LieGroup(object):
    """
    This serves as the default superclass on which all Lie groups are constructed from.
    """
    abelian = False

    def __new__(cls, *args, **kwargs):
        obj = super(LieGroup, cls).__new__(cls)
        obj.field = 'R'
        obj.shape = None
        obj.data = None

        if len(args) >= 1 and isinstance(args[0], LieGroup):
            obj = copy.copy(args[0])
        if len(args) >= 1 and isinstance(args[0], int):
            obj.shape = args[0]

        if len(args) >= 2:
            obj.data = args[1]

        return obj

    def __init__(self, *args, **kwargs):
        if self.data is None:
            self.Identity()

    def __mul__(self, other):
        if isinstance(other, int):
            self.data = self.data * other
            return self
        elif isinstance(other, float):
            self.data = self.data * other
            return self
        elif isinstance(other, LieGroup):
            return LieGroup(self, np.dot(self.data, other.data))

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.shape) + ', ' + str(self.data) + ')'

    __rmul__ = __mul__

    @abc.abstractmethod
    def get_dimension(self):
        raise NotImplementedError

    def get_data(self):
        return self.data

    def Identity(self):
        from beluga.liepack import group2algebra, exp
        g = group2algebra(self)(self.shape)
        self.data = exp(g).data

    def random(self):
        from beluga.liepack import group2algebra, exp
        g = group2algebra(self)(self.shape)
        g.random()
        self.data = exp(g).data

    def set_data(self, data):
        self.data = np.array(data, dtype=np.float64)


class RN(LieGroup):
    abelian = True


class SO(LieGroup):
    abelian = False


class SP(LieGroup):
    abelian = False
