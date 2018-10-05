from beluga.liepack.domain.liealgebras import *
from beluga.liepack.domain.liegroups import *
from beluga.liepack.domain.hspaces import *

from scipy.linalg import expm as scipyexpm
from scipy.special import bernoulli
from math import factorial
import numpy as np

def algebra2group(g):
    r"""
    Returns the Lie group corresponding to an input Lie algebra element.

    :param g: An element of Lie algebra :math:`\mathfrak{g}`.
    :return: :math:`\mathfrak{g}`'s group, :math:`G`.
    """
    if isinstance(g, rn):
        return RN
    if isinstance(g, so):
        return SO
    if isinstance(g, sp):
        return SP
    if isinstance(g, LieAlgebra):
        return LieGroup


def group2algebra(G):
    r"""
    Returns the Lie algebra corresponding to an input Lie group element.

    :param G: An element of Lie group :math:`G`.
    :return: :math:`G`'s algebra, :math:`\mathfrak{g}`.
    """
    if isinstance(G, RN):
        return rn
    if isinstance(G, SO):
        return so
    if isinstance(G, SP):
        return sp
    if isinstance(G, LieGroup):
        return LieAlgebra


def Adjoint(G, h):
    r"""
    Adjoint map of a Lie group, :math:`g \in G`, on Lie algebra element :math:`h \in \mathfrak{g}`.

    .. math::
        \begin{aligned}
            \text{Adjoint} : G &\rightarrow \mathfrak{Aut}(\mathfrak{g}) \\
            (g, h) &\mapsto ghg^{-1}
        \end{aligned}

    :param g: A Lie group element.
    :param h: A Lie algebra element.
    :return: :math:`\text{Ad}_g(h)`
    """
    g = group2algebra(G)
    return g(G.get_shape(), np.dot(np.dot(G, h), np.linalg.inv(G)))


def commutator(g, h, **kwargs):
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

    Examples:

    Construct the set of commutation relations in :math:`so(3)`.

    >>> from beluga.liepack.domain.liealgebras import so
    >>> from beluga.liepack import commutator
    >>> x = so(3)
    >>> y = so(3)
    >>> z = so(3)
    >>> x.set_vector([1,0,0])
    >>> y.set_vector([0,1,0])
    >>> z.set_vector([0,0,1])
    >>> Commutator(x,y) == z
    True
    """
    anticommutator = kwargs.get('anticommutator', 1)
    return np.dot(g,h) - anticommutator*np.dot(h,g)

def dexpinv(g, h, order=5):
    r"""
    Inverse of the derivative of the exponential map.

    .. math::
        dexp^{-1} : \mathfrak{g} \rightarrow T\mathfrak{g}

    Evaluates the map by the following formula:

    .. math::
        dexp_g^{-1}(h) = h - \frac{1}{2}[g,h] + \frac{B_2}{2!}[g,[g,h]] + \cdots = \sum_{k=0}^{\text{order}} \frac{B_k}{k!}\text{ad}_g^k(h)

    where :math:`B_k` are the :math:`k`-th Bernioulli numbers. The infinite series is truncated at `order`.

    :param g: Element of a Lie algebra.
    :return:

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | order                  | 5               | > 0             |
    +------------------------+-----------------+-----------------+

    """

    if g.abelian:
        return LieAlgebra(h)
    if order < 2:
        return h

    B = bernoulli(order)

    def adg(e):
        return commutator(g, e)

    k = 0
    stack = h
    out = B(k) * h

    k = 1
    stack = adg(stack)
    out += B(k) * stack
    k += 1

    while k < order:
        stack = adg(stack)
        out += B(k) / factorial(k) * stack
        k += 2

    return out


def exp(g):
    r"""
    Exponential map of a Lie algebra element to its Lie group.

    .. math::
        \begin{aligned}
            \text{exp} : \mathfrak{g} &\rightarrow G \\
            (g) &\mapsto Id_G + g + \frac{1}{2}g^2 + \cdots = \sum_{k=0}^{\infty} \frac{g^k}{k!}
        \end{aligned}

    :param g: Lie algebra element.
    :return: Lie group element, :math:`G`.
    """
    if isinstance(g, LieAlgebra):
        return algebra2group(g)(g.get_shape(), scipyexpm(g))
    else:
        return scipyexpm(g)


def killing(g,h):
    r"""
    Determine the Killing coefficient between two elements in a Lie algebra.

    :param g: Lie algebra element.
    :param h: Lie algebra element.
    :return: Killing coefficient.
    """
    if type(g) != type(h):
        raise TypeError("Lie algebra elements must be of the same type.")

    basis = g.basis()
    def adg(H): return commutator(g, H)
    def adh(G): return commutator(h, G)

    k = 0
    for ii in range(len(basis)):
        k += adg(adh(basis[ii])).get_vector()[ii]
    return k


def Left(G, M):
    r"""
    Left action of group :math:`G` on homogeneous space :math:`M`.

    .. math::
        \begin{aligned}
            \text{Left} : G \times M &\rightarrow M \\
            (G,M) &\mapsto GM
        \end{aligned}

    :param G: Lie group.
    :param M: Homogeneous space.
    :return: Homogeneous space.
    """
    if not isinstance(G, LieGroup):
        raise ValueError
    Mout = HManifold(M)
    Mout = np.dot(G, Mout.data)
    return Mout

def Right(G, M):
    if not isinstance(G, LieGroup):
        raise ValueError
    Mout = HManifold(M)
    Mout = np.dot(Mout.data, G)
    return Mout
