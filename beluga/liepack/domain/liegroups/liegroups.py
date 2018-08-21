import abc

from beluga.utils import keyboard

import numpy as np

class LieGroup(object):
    """
    This serves as the default superclass on which all Lie algebras are constructed from.
    """
    abelian = False

    def __new__(cls, *args, **kwargs):
        obj = super(LieGroup, cls).__new__(cls)
        if len(args) == 0:
            obj.field = 'R'
            obj.shape = None
            obj.data = None
        elif len(args) == 1 and isinstance(args[0], LieGroup):
            obj = args[0]
        elif len(args) == 1 and isinstance(args[0], int):
            obj.field = 'R'
            obj.shape = args[0]
            obj.data = None
        elif len(args) == 2:
            obj.field = 'R'
            obj.shape = args[0]
            obj.data = args[1]

        return obj

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

    def set_data(self, data):
        self.data = np.array(data, dtype=np.float64)


class RN(LieGroup):
    abelian = True
    pass


class SO(LieGroup):
    abelian = False
    pass
