from beluga.liepack.domain.liealgebras import LieAlgebra
from beluga.liepack.domain.liegroups import LieGroup

from beluga.utils import keyboard

from scipy.linalg import expm as scipyexpm
from scipy.linalg import inv as scipyinv
import numpy as np

def adjoint(g, G):
    """
    Adjoint map of a

    :param g:
    :param G:
    :return:
    """
    if G.abelian is True:
        return LieAlgebra(g)
    else:
        d1 = g.get_data()
        d2 = G.get_data()
        return LieAlgebra(g, np.dot(np.dot(d2, d1), scipyinv(d2)))


class Commutator(object):
    r"""
    Commutator of two Lie algebra elements, :math:`g, h \in \mathfrak{g}`.

    .. math::
        \begin{aligned}
            \mathfrak{g} \times \mathfrak{g} &\rightarrow \mathfrak{g} \\
            (g, h) &\mapsto [g,h] = gh - hg
        \end{aligned}

    :param g: Lie algebra element 1.
    :param h: Lie algebra element 2.
    :return: A new Lie alegbra element in :math:`\mathfrak{g}`.

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | anticommutator         | 1               | {1, -1}         |
    +------------------------+-----------------+-----------------+

    >>> from beluga.liepack.domain.liealgebras import so
    >>> from beluga.liepack import Commutator
    >>> x = so(3)
    >>> y = so(3)
    >>> z = so(3)
    >>> x.set_data([1,0,0])
    >>> y.set_data([0,1,0])
    >>> z.set_data([0,0,1])
    >>> Commutator(x,y) == z
    True
    """

    def __new__(cls, *args, **kwargs):
        obj = super(Commutator, cls).__new__(cls)
        obj.anticommutator = int(kwargs.get('anticommutator', 1))
        g, h = None, None

        if len(args) > 0:
            g = args[0]

        if len(args) > 1:
            h = args[1]

        obj._g = g
        obj._h = h
        if g is not None and h is not None:
            return cls.__call__(obj, *args, **kwargs)
        else:
            return obj

    def __call__(self, *args, **kwargs):
        k = 0
        if self._g is None:
            self._g = args[k]
            k += 1

        if self._h is None:
            self._h = args[k]
            k += 1

        return self._g*self._h - self.anticommutator*self._h*self._g

def expm(g):
    r"""
    Exponential map of Lie algebra elements to their Lie group.

    :param g:
    :return:
    """
    if isinstance(g, LieAlgebra):
        return g.group(g.get_shape, scipyexpm(g.data))
