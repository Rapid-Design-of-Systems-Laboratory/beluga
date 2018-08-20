from beluga.liepack.domain.liealgebras import *
from beluga.liepack.domain.liegroups import *

from beluga.utils import keyboard

from scipy.linalg import expm as scipyexpm
from scipy.linalg import inv as scipyinv
from beluga.utils import Bernoulli
from math import factorial
import numpy as np

def algebra2group(g):
    """
    Returns the Lie group corresponding to an input Lie algebra element.

    :param g: An element of Lie algebra :math:`\mathfrak{g}`.
    :return: :math:`\mathfrak{g}`'s group, :math:`G`.
    """
    if isinstance(g, rn):
        return RN
    if isinstance(g, so):
        return SO
    if isinstance(g, LieAlgebra):
        return LieGroup


def group2algebra(G):
    """
    Returns the Lie algebra corresponding to an input Lie group element.

    :param G: An element of Lie group :math:`G`.
    :return: :math:`G`'s algebra, :math:`\mathfrak{g}`.
    """
    if isinstance(G, RN):
        return rn
    if isinstance(G, SO):
        return so
    if isinstance(G, LieGroup):
        return LieAlgebra


class Adjoint(object):
    r"""
    Adjoint map of a Lie group, :math:`g \in G`, on Lie algebra element :math:`h \in \mathfrak{g}`.

    .. math::
        \begin{aligned}
            \text{Adjoint} : G \times \mathfrak{g} &\rightarrow \text{Aut}(\mathfrak{g}) \\
            (g, h) &\mapsto ghg^{-1}
        \end{aligned}

    :param G: A Lie group element.
    :param g: A Lie algebra element.
    :return: :math:`\text{Ad}_G(g)`
    """
    def __new__(cls, *args, **kwargs):
        obj = super(Adjoint, cls).__new__(cls)
        G, g = None, None

        if len(args) > 0:
            G = args[0]

        if len(args) > 1:
            g = args[1]

        obj._G = G
        obj._g = g

        if G is not None and g is not None:
            return cls.__call__(obj, *args, **kwargs)
        else:
            return obj

    def __call__(self, *args, **kwargs):
        k = 0
        if self._G is None:
            self._G = args[k]
            k += 1

        if self._g is None:
            self._g = args[k]
            k += 1

        if self._G.abelian is True:
            return LieAlgebra(self._g)
        else:
            return LieAlgebra(self._g, self._G.data)*self._g*LieAlgebra(self._g, scipyinv(self._G.data))


class Commutator(object):
    r"""
    Commutator of two Lie algebra elements, :math:`g, h \in \mathfrak{g}`.

    .. math::
        \begin{aligned}
            \text{Commutator} : \mathfrak{g} \times \mathfrak{g} &\rightarrow \mathfrak{g} \\
            [g, h] &\mapsto gh - hg
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

def dexpinv(g, h, order=5):
    r"""
    Inverse of the derivative of the exponential map.

    .. math::
        dexp^{-1} : \mathfrak{g} \rightarrow T\mathfrak{g}

    Evaluates the map by the following formula:

    .. math::
        dexp_g^{-1}(h) = h - \frac{1}{2}[g,h] + \frac{B_2}{2!}[g,[g,h]] + \cdots = \sum_{k=0}^{\text{order}} \frac{B_k}{k!}\text{ad}_g^k(h)

    where :math:`B_k` are the :math:`k`-th Bernioulli numbers.

    :param g: Element of a Lie algebra.
    :return:

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | order                  | 5               | > 0             |
    +------------------------+-----------------+-----------------+

    """
    if order < 2:
        return h

    k = 0
    stack = h
    out = h

    k = 1
    adjoint = Commutator(g)
    stack = adjoint(stack)
    out += -1/2*stack

    while k < order:
        k += 1
        stack = adjoint(stack)
        out += Bernoulli(k)/factorial(k)*stack

    return out


def exp(g):
    r"""
    Exponential map of a Lie algebra element to its Lie group.

    :param g:
    :return:
    """
    if isinstance(g, LieAlgebra):
        return g.group(g.get_shape, scipyexpm(g.data))
