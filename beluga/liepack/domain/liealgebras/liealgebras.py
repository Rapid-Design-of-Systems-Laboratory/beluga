import abc
import copy
import numpy as np

from random import uniform
from math import floor

from beluga.utils import keyboard

class LieAlgebra(object):
    """
    This serves as the default superclass on which all Lie algebras are constructed from.
    """
    abelian = False  # Default to assuming all Lie algebras are nonabelian.

    def __new__(cls, *args, **kwargs):
        obj = super(LieAlgebra, cls).__new__(cls)
        obj.shape = None
        obj.data = None

        if len(args) > 0:
            if isinstance(args[0], LieAlgebra):
                obj = copy.copy(args[0])
            elif isinstance(args[0], int):
                obj.shape = args[0]
                obj.data = None

        if len(args) > 1:
            obj.data = args[1]

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

    def basis(self):
        d = self.get_dimension()
        basis = [LieAlgebra(self) for _ in range(d)]
        z = np.zeros(d)
        for ii in range(d):
            z[ii] = 1
            basis[ii].set_vector(z)
            z[ii] = 0
        return basis

    @abc.abstractmethod
    def get_dimension(self) -> int:
        """
        Returns the dimension of the Lie algebra.

        :return: Dimension.
        """
        raise NotImplementedError

    def get_shape(self) -> int:
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

    def get_dimension(self) -> int:
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

    def get_dimension(self) -> int:
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


class sp(LieAlgebra):
    r"""
    Lie algebra :math:`sp(n)`.

    For a Lie algebra element of the form :math:`(x, y, z)`, the matrix representation is of the form:

    .. math::
        \begin{bmatrix}
            x & y \\
            z & -x
        \end{bmatrix}

    For higher dimensions, the matrix representation is of the form:

    .. math::
        \begin{bmatrix}
            A & B \\
            C & -A^T
        \end{bmatrix}

    where :math:`B` and :math:`C` are symmetric matrices.

    """
    abelian = False

    def __new__(cls, *args, **kwargs):
        obj = super(sp, cls).__new__(cls, *args, **kwargs)

        if obj.shape is not None and obj.shape % 2 != 0:
            raise ValueError('Symplectic Lie algebra must have an even dimension.')

        return obj

    def get_dimension(self) -> int:
        return int(self.shape * (self.shape + 1)/2)

    def get_vector(self):
        d = self.get_shape()
        s = int(d/2)
        k = 0
        out = np.zeros(self.get_dimension())
        A = self.data[:s,:s]
        B = self.data[:s, s:2*s]
        C = self.data[s:2*s, :s]
        for ii in range(s):
            for jj in range(s):
                out[k] = A[ii, jj]
                k += 1

        for ii in range(s):
            for jj in range(ii, s):
                out[k] = B[ii, jj]
                k += 1

        for ii in range(s):
            for jj in range(ii, s):
                out[k] = C[ii, jj]
                k += 1
        return out

    def set_vector(self, vector):
        d = self.get_shape()
        s = int(d/2)
        k = 0
        A = np.zeros((s,s))
        B = np.zeros((s,s))
        C = np.zeros((s,s))
        for ii in range(s):
            for jj in range(s):
                A[ii, jj] = vector[k]
                k += 1

        for ii in range(s):
            for jj in range(ii, s):
                B[ii, jj] = vector[k]
                k += 1
        B = B + B.T - np.diag(B.diagonal())

        for ii in range(s):
            for jj in range(ii, s):
                C[ii, jj] = vector[k]
                k += 1
        C = C + C.T - np.diag(C.diagonal())
        top = np.hstack((A, B))
        bot = np.hstack((C, -A.T))
        self.data = np.vstack((top, bot))
