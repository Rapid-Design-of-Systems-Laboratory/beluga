import abc
import copy

import numpy as np


class LieGroup(np.ndarray):
    """
    This serves as the default superclass on which all Lie groups are constructed from.
    """
    abelian = False

    def __new__(cls, *args, **kwargs):
        if len(args) == 0:
            raise TypeError("Required input 'shape' (pos 1) or 'LieGroup' (pos 1) not found")

        if isinstance(args[0], LieGroup):
            obj = copy.copy(args[0])
            return obj

        if isinstance(args[0], int):
            obj = super(LieGroup, cls).__new__(cls, (args[0], args[0]), **kwargs)
            shape = args[0]
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
            np.copyto(obj, np.eye(shape))

        return obj

    def __eq__(self, other):
        return super(LieGroup, self).__eq__(other).view(np.ndarray)

    def __ge__(self, other):
        return super(LieGroup, self).__ge__(other).view(np.ndarray)

    def __gt__(self, other):
        return super(LieGroup, self).__gt__(other).view(np.ndarray)

    def __le__(self, other):
        return super(LieGroup, self).__le__(other).view(np.ndarray)

    def __lt__(self, other):
        return super(LieGroup, self).__lt__(other).view(np.ndarray)

    def __ne__(self, other):
        return super(LieGroup, self).__ne__(other).view(np.ndarray)

    def __repr__(self):
        if len(self.shape) == 0:
            return super(LieGroup, self).__str__()
        else:
            return self.__class__.__name__ + '(' + str(self.shape[0]) + ', ' + super(LieGroup, self).__str__() + ')'

    @abc.abstractmethod
    def get_dimension(self):
        """
        Returns the dimension of the Lie group.

        :return: Dimension.
        """
        raise NotImplementedError

    def get_shape(self):
        r"""
        Returns the shape of the Lie group.

        :return: Shape.
        """
        return int(self.shape[0])

    def Identity(self):
        from beluga.liepack import group2algebra, exp
        g = group2algebra(self)(self.get_shape())
        np.copyto(self, exp(g))

    def random(self):
        from beluga.liepack import group2algebra, exp
        g = group2algebra(self)(self.get_shape())
        g.random()
        np.copyto(self, exp(g))


class RN(LieGroup):
    abelian = True


class SO(LieGroup):
    abelian = False


class SP(LieGroup):
    abelian = False
