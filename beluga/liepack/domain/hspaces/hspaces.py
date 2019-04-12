import copy
from scipy.linalg import expm
import numpy as np


class HManifold(np.ndarray):
    def __new__(cls, *args, **kwargs):
        if isinstance(args[0], HManifold):
            obj = copy.copy(args[0])
            return obj

        shape = sum([_.get_shape() for _ in args])
        obj = super(HManifold, cls).__new__(cls, (shape, shape), **kwargs)
        obj.actions = len(args)
        np.copyto(obj, np.zeros((shape, shape)))
        cls.set_data(obj, args)
        return obj

    def __repr__(self):
        if len(self.shape) == 0:
            return super(HManifold, self).__str__()
        else:
            return self.__class__.__name__ + '(' + str(self.shape[0]) + ', ' + super(HManifold, self).__str__() + ')'

    def set_data(self, Gset):
        ii = 0
        for G in Gset:
            np.copyto(self[ii:G.get_shape()+ii, ii:G.get_shape()+ii], G)
            ii += G.get_shape()

    def left(self, Gset):
        r"""
        Left action of a set of groups :math:`\{G_1, G_2, \cdots, G_i\}` on homogeneous space :math:`M`.

        .. math::
            \begin{aligned}
                \text{Left} : G_1 \times G_2 \times \cdots \times G_i M &\rightarrow M \\
                (G,M) &\mapsto GM
            \end{aligned}

        :param Gset: A list of Lie groups.
        """
        ii = 0
        for G in Gset:
            self[ii:G.get_shape()+ii, ii:G.get_shape()+ii] = np.dot(G, self[ii:G.get_shape()+ii, ii:G.get_shape()+ii])
            ii += G.get_shape()

    def right(self, Gset):
        r"""
        Right action of a set of groups :math:`\{G_1, G_2, \cdots, G_i\}` on homogeneous space :math:`M`.

        .. math::
            \begin{aligned}
                \text{Left} : G_1 \times G_2 \times \cdots \times G_i M &\rightarrow M \\
                (G,M) &\mapsto MG
            \end{aligned}

        :param Gset: A list of Lie groups.
        """
        ii = 0
        for G in Gset:
            self[ii:G.get_shape()+ii, ii:G.get_shape()+ii] = np.dot(self[ii:G.get_shape()+ii, ii:G.get_shape()+ii], G)
            ii += G.get_shape()
