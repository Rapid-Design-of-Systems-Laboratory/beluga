from beluga.liepack.domain.liegroups import *
import abc
import copy
import numpy as np

from random import uniform

from beluga.utils import keyboard

class LieAlgebra(object):
    """
    This serves as the default superclass on which all Lie algebras are constructed from.
    """

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

    def __eq__(self, other):
        class_condition = type(self) == type(other)
        if isinstance(other, int):
            class_condition = True
            data_condition = (self.data == other*np.ones((self.shape))).all()
        elif isinstance(other, float):
            class_condition = True
            data_condition = (self.data == other*np.ones((self.shape))).all()
        else:
            data_condition = (self.data == other.data).all()

        return class_condition and data_condition

    def __ne__(self, other):
        class_condition = type(self) == type(other)
        data_condition = (self.data == other.data).all()

        return not (class_condition and data_condition)

    def __neg__(self):
        return LieAlgebra(self, -self.data)

    def __sub__(self, other):
        return LieAlgebra(self, self.data - other.data)

    def __mul__(self, other):
        if isinstance(other, int):
            newdata = self.data * other
        elif isinstance(other, float):
            newdata = self.data * other
        else:
            newdata = np.dot(self.data, other.data)

        return LieAlgebra(self, newdata)

    __rmul__ = __mul__

    def get_data(self):
        return self.data

    @abc.abstractmethod
    def get_dimension(self):
        pass

    def get_shape(self):
        return self.shape

    def random(self):
        v = [uniform(0,1) for _ in range(self.get_dimension())]
        self.set_vector(v)

class rn(LieAlgebra):
    abelian = True
    group = RN
    pass

# dimension
# getdata
# getmatrix
# getnumberfield
# getshape
# getvector
# hasmatrix
# hasshape

class so(LieAlgebra):
    abelian = False
    group = SO

    def get_dimension(self):
        n = self.shape
        return int(n*(n-1)/2)

    def set_vector(self, vector):
        vector = np.array(vector, dtype=np.float64)
        n = self.shape
        vlen = n*(n-1)/2
        if vlen != len(vector):
            raise ValueError

        mat = np.zeros((n,n))
        k = 0
        for i in range(n-1, 0, -1):
            for j in range(n, i, -1):
                mat[i-1,j-1] = (-1)**(i+j)*vector[k]
                k += 1

        self.data = mat - mat.T
