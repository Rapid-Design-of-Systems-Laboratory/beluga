from beluga.liepack.domain.liealgebras import LieAlgebra
from beluga.liepack.domain.liegroups import LieGroup

from beluga.utils import keyboard

from scipy.linalg import expm as scipyexpm
from scipy.linalg import inv as scipyinv
import numpy as np

def adjoint(g, G):
    if G.abelian is True:
        return LieAlgebra(g)
    else:
        d1 = g.get_data()
        d2 = G.get_data()
        return LieAlgebra(g, np.dot(np.dot(d2, d1), scipyinv(d2)))


def commutator(g,h):
    return g*h - h*g

def expm(g):
    if isinstance(g, LieAlgebra):
        return g.group(g.get_shape, scipyexpm(g.data))
