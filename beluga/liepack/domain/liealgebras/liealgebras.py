import abc
import copy
import numpy as np

from random import uniform


class LieAlgebra(np.ndarray):
    """
    This serves as the default superclass on which all Lie algebras are constructed from.
    """
    abelian = False  # Default to assuming all Lie algebras are nonabelian.

    def __new__(cls, *args, **kwargs):
        if len(args) == 0:
            raise TypeError("Required input 'shape' (pos 1) or 'LieAlgebra' (pos 1) not found")

        if isinstance(args[0], LieAlgebra):
            obj = copy.copy(args[0])
            return obj

        if isinstance(args[0], int):
            obj = super(LieAlgebra, cls).__new__(cls, (args[0], args[0]), **kwargs)
        else:
            raise ValueError("Input 'shape' (pos 1) must be of 'int' type")

        if len(args) > 1:
            if isinstance(args[1], np.ndarray):
                np.copyto(obj, args[1])
            elif isinstance(args[1], list):
                for ii in range(len(args[1])):
                    for jj in range(len(args[1])):
                        obj[ii, jj] = args[1][ii][jj]
        else:
            np.copyto(obj, np.zeros(obj.shape))

        return obj

    def __eq__(self, other):
        return super(LieAlgebra, self).__eq__(other).view(np.ndarray)

    def __ge__(self, other):
        return super(LieAlgebra, self).__ge__(other).view(np.ndarray)

    def __gt__(self, other):
        return super(LieAlgebra, self).__gt__(other).view(np.ndarray)

    def __le__(self, other):
        return super(LieAlgebra, self).__le__(other).view(np.ndarray)

    def __lt__(self, other):
        return super(LieAlgebra, self).__lt__(other).view(np.ndarray)

    def __ne__(self, other):
        return super(LieAlgebra, self).__ne__(other).view(np.ndarray)

    def __repr__(self):
        if len(self.shape) == 0:
            return super(LieAlgebra, self).__str__()
        else:
            return self.__class__.__name__ + '(' + str(self.shape[0]) + ', ' + super(LieAlgebra, self).__str__() + ')'

    def basis(self):
        """
        Returns a basis for the Lie algebra.

        :return: List of basis elements.
        """
        d = self.get_dimension()
        basis = [LieAlgebra(self) for _ in range(d)]
        z = np.zeros(d)
        for ii in range(d):
            z[ii] = 1
            basis[ii].set_vector(z)
            z[ii] = 0
        return basis

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
        return int(self.shape[0])

    @abc.abstractmethod
    def get_vector(self):
        r"""
        Take's a Lie algebra's matrix representation and returns its vector representation.

        :return: vector A :math:`1 \times n`-dimensional vector.
        """
        raise NotImplementedError

    def killing_form(self):
        r"""
        Returns the Killing form for the Lie algebra.

        :return: Killing form.
        """
        from beluga.liepack import killing
        basis = self.basis()
        L = len(basis)
        mat = np.zeros((L, L))
        for ii in range(L):
            for jj in range(L):
                mat[ii, jj] = killing(basis[ii], basis[jj])

        return mat

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
        v = [uniform(0, 1) for _ in range(self.get_dimension())]
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
        n = self.get_shape()
        return int(n-1)

    def get_vector(self):
        return np.array(self[:-1, -1])

    def set_vector(self, vector):
        vector = np.array(vector, dtype=np.float64)
        n = self.get_dimension()
        vlen = n
        if vlen != len(vector):
            raise ValueError

        mat = np.zeros((n+1, n+1))
        for i in range(n):
            mat[i, -1] = vector[i]

        np.copyto(self, mat)


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
        n = self.get_shape()
        return int(n*(n-1)/2)

    def get_vector(self):
        n = self.get_shape()
        vlen = int(n*(n-1)/2)
        vector = np.zeros(vlen)

        k = 0
        for i in range(n-1, 0, -1):
            for j in range(n, i, -1):
                vector[k] = (self[i-1, j-1])/(-1)**(i+j)
                k += 1

        return vector

    def set_vector(self, vector):
        vector = np.array(vector, dtype=np.float64)
        n = self.shape[0]
        vlen = int(n*(n-1)/2)
        if vlen != len(vector):
            raise ValueError

        mat = np.zeros((n, n))
        k = 0
        for i in range(n-1, 0, -1):
            for j in range(n, i, -1):
                mat[i-1, j-1] = (-1)**(i+j)*vector[k]
                k += 1

        np.copyto(self, mat - mat.T)


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

        if cls.get_shape(obj) is not None and cls.get_shape(obj) % 2 != 0:
            raise ValueError('Symplectic Lie algebra must have an even dimension.')

        return obj

    def get_dimension(self):
        shape = self.get_shape()
        return int(shape * (shape + 1)/2)

    def get_vector(self):
        d = self.get_shape()
        s = int(d/2)
        k = 0
        out = np.zeros(self.get_dimension())
        A = self[:s, :s]
        B = self[:s, s:2*s]
        C = self[s:2*s, :s]
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
        A = np.zeros((s, s))
        B = np.zeros((s, s))
        C = np.zeros((s, s))
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

        np.copyto(self, np.vstack((top, bot)))
