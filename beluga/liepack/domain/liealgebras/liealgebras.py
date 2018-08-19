from beluga.liepack.domain.liegroups import *
import copy
import numpy as np

from beluga.utils import keyboard

class LieAlgebra(object):
    abelian = False
    group = LieGroup

    def __new__(cls, *args, **kwargs):
        obj = super(LieAlgebra, cls).__new__(cls)

        if len(args) >= 1:
            if isinstance(args[0], LieAlgebra):
                obj = copy.copy(args[0])
            elif isinstance(args[0], int):
                obj.shape = args[0]
                obj.data = None

        if len(args) >= 2:
            obj.data = args[1]
            obj.shape = obj.data.shape[0]

        return obj

    def __add__(self, other):
        return LieAlgebra(self, self.data + other.data)

    def __sub__(self, other):
        return LieAlgebra(self, self.data - other.data)

    def __mul__(self, other):
        if isinstance(other, int):
            self.data = self.data * other
            return self
        elif isinstance(other, float):
            self.data = self.data * other
            return self
        else:
            return LieAlgebra(self, np.dot(self.data, other.data))

    __rmul__ = __mul__

    def get_data(self):
        return self.data

    def get_shape(self):
        return self.shape


class rn(LieAlgebra):
    abelian = True
    group = RN
    pass


class so(LieAlgebra):
    abelian = False
    group = SO

    def get_dimension(self):
        n = self.shape
        return n*(n-1)/2
