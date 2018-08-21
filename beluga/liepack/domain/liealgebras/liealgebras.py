import abc
import copy
import numpy as np

from random import uniform

from beluga.utils import keyboard

class LieAlgebra(object):
    """
    This serves as the default superclass on which all Lie algebras are constructed from.
    """
    abelian = False # Default to assuming all Lie algebras are nonabelian.

    def __new__(cls, *args, **kwargs):
        obj = super(LieAlgebra, cls).__new__(cls)

        if len(args) > 0:
            if isinstance(args[0], LieAlgebra):
                obj = copy.copy(args[0])
            elif isinstance(args[0], int):
                obj.shape = args[0]
                obj.data = None

        if len(args) >= 2:
            obj.data = args[1]
            obj.shape = obj.data.shape[0]

        return obj

    def __init__(self, *args, **kwargs):
        if self.data is None:
            self.zero()

    def __add__(self, other):
        if isinstance(other, int):
            newdata = self.data + other
        elif isinstance(other, float):
            newdata = self.data + other
        elif isinstance(other, LieAlgebra):
            newdata = self.data + other.data
        return LieAlgebra(self, newdata)

    def __eq__(self, other):
        class_condition = type(self) == type(other)
        if isinstance(other, int) or isinstance(other, float):
            class_condition = True
            data_condition = (self.data == other*np.ones((self.shape))).all()
        else:
            data_condition = (self.data == other.data).all()

        return class_condition and data_condition

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            data_condition = (self.data < other * np.ones((self.shape))).all()
        else:
            data_condition = (self.data < other.data).all()

        return data_condition

    def __mul__(self, other):
        if isinstance(other, int):
            newdata = self.data * other
        elif isinstance(other, float):
            newdata = self.data * other
        else:
            newdata = np.dot(self.data, other.data)

        return LieAlgebra(self, newdata)

    def __ne__(self, other):
        class_condition = type(self) == type(other)
        data_condition = (self.data == other.data).all()

        return not (class_condition and data_condition)

    def __neg__(self):
        return LieAlgebra(self, -self.data)

    __radd__ = __add__

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.shape) + ', ' + str(self.data) + ')'

    __rmul__ = __mul__

    def __sub__(self, other):
        return LieAlgebra(self, self.data - other.data)

    def __truediv__(self, other):
        if isinstance(other, int):
            newdata = self.data / other
        elif isinstance(other, float):
            newdata = self.data / other
        else:
            raise NotImplementedError

        return LieAlgebra(self, newdata)

    @abc.abstractmethod
    def get_dimension(self):
        """
        Returns the dimension of the Lie algebra.

        :return: Dimension.
        """
        raise NotImplementedError

    def get_shape(self):
        r"""
        Returns the shape of the Lie algebra.

        :return: Shape.
        """
        return self.shape

    @abc.abstractmethod
    def set_vector(self, vector):
        r"""
        Take's a vector and saves it to the Lie algebra's matrix representation.

        :param vector: A :math:`1 \times n`-dimensional vector.
        """
        raise NotImplementedError

    def random(self):
        r"""
        Initializes a random element in the Lie algebra.
        """
        v = [uniform(0,1) for _ in range(self.get_dimension())]
        self.set_vector(v)

    def zero(self):
        r"""
        Sets the Lie algebra to the zero element.
        """
        v = np.zeros(self.get_dimension())
        self.set_vector(v)

class rn(LieAlgebra):
    r"""
    Lie algebra :math:`\mathbb{R}^n`, or ":math:`rn`".

    For a Lie algebra element of the form :math:`(x,y,z,\cdots,w)`, matrix representation is of the form:

    .. math::
        \begin{bmatrix}
            0 & 0 & 0 & \cdots & 0 & x \\
            0 & 0 & 0 & \cdots & 0 & y \\
            0 & 0 & 0 & \cdots & 0 & z \\
            \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
            0 & 0 & 0 & \cdots & 0 & w \\
            0 & 0 & 0 & \cdots & 0 & 0
        \end{bmatrix}

    """
    abelian = True

    def get_dimension(self):
        n = self.shape
        return int(n)

    def get_vector(self):
        return np.array(self.data[:-1,-1])

    def set_vector(self, vector):
        vector = np.array(vector, dtype=np.float64)
        n = self.shape
        vlen = n
        if vlen != len(vector):
            raise ValueError

        mat = np.zeros((n+1,n+1))
        for i in range(n):
            mat[i, -1] = vector[i]

        self.data = mat


class so(LieAlgebra):
    r"""
    Lie algebra :math:`so(n)`.

    For a Lie algebra element of the form :math:`(x, y, z)`, the matrix representation is of the form:

    .. math::
        \begin{bmatrix}
            0 & -z & y \\
            z & 0 & -x \\
            -y & x & 0
        \end{bmatrix}
    """
    abelian = False

    def get_dimension(self):
        n = self.shape
        return int(n*(n-1)/2)

    def get_vector(self):
        n = self.shape
        vlen = int(n*(n-1)/2)
        vector = np.zeros(vlen)

        k = 0
        for i in range(n-1, 0, -1):
            for j in range(n, i, -1):
                vector[k] = self.data[i-1, j-1]/(-1)**(i+j)
                k += 1

        return vector

    def set_vector(self, vector):
        vector = np.array(vector, dtype=np.float64)
        n = self.shape
        vlen = int(n*(n-1)/2)
        if vlen != len(vector):
            raise ValueError

        mat = np.zeros((n,n))
        k = 0
        for i in range(n-1, 0, -1):
            for j in range(n, i, -1):
                mat[i-1,j-1] = (-1)**(i+j)*vector[k]
                k += 1

        self.data = mat - mat.T
