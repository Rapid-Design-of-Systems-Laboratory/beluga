from beluga.liepack.domain.liealgebras import *
from beluga.liepack.domain.liegroups import *
from beluga.liepack import *

import numpy as np

from random import uniform

tol = 1e-14

def test_Adjoint():
    x = so(3)
    y = so(3)
    z = so(3)
    G = SO(3)

    x.set_vector([1, 0, 0])
    y.set_vector([0, 1, 0])
    z.set_vector([0, 0, 1])
    rot = uniform(0, 2*np.pi)

    np.copyto(G, exp(x*rot))

    # Use case tests
    def AdG(g):
        return Adjoint(G, g)

    assert (AdG(y).get_vector() - np.array([0, np.cos(rot), np.sin(rot)]) < tol).all()
    assert (AdG(z).get_vector() - np.array([0, -np.sin(rot), np.cos(rot)]) < tol).all()
    n1 = np.linalg.norm(y.get_vector())
    n2 = np.linalg.norm(z.get_vector())
    rot = np.pi/4
    np.copyto(G, exp(x*rot))
    assert (Adjoint(G,y) - (y+z)/(np.sqrt(n1**2 + n2**2)) < tol).all()


def test_commutator():
    x = so(3)
    y = so(3)
    z = so(3)

    x.set_vector([1,0,0])
    y.set_vector([0,1,0])
    z.set_vector([0,0,1])

    # Use case tests
    assert (commutator(x, y) == z).all()
    assert (commutator(y, x) == -z).all()

    # Lie algebra identities
    A = uniform(-1,1)
    B = uniform(-1,1)
    assert (commutator(x + y, z) == (commutator(x, z) + commutator(y, z))).all()
    assert (commutator(x,x) == 0).all()
    assert (commutator(x,y) == -commutator(y, x)).all()
    assert (commutator(x, commutator(y, z)) + commutator(y, commutator(z, x)) + commutator(z, commutator(x, y)) == 0).all()
    assert (commutator(A*x + B*y, z) == A*commutator(x,z) + B*commutator(y,z)).all()
    assert (commutator(z, A*x + B*y) == commutator(z, x)*A + commutator(z,y)*B).all()

    x.random()
    y.random()
    z.random()
    assert ((commutator(x, commutator(y, z)) + commutator(y, commutator(z, x)) + commutator(z, commutator(x, y))) < tol).all()

def test_exp():
    x = so(3)
    M = SO(3)

    x.set_vector([1, 0, 0])
    rot = np.pi/4

    assert isinstance(exp(x), LieGroup)

    np.copyto(M, exp(x*rot))

    assert M.data[0, 0] == 1
    assert M.data[1, 0] == 0
    assert M.data[2, 0] == 0
    assert M.data[0, 1] == 0
    assert M.data[1, 1] - np.cos(rot) < tol
    assert M.data[2, 1] - np.sin(rot) < tol
    assert M.data[0, 2] == 0
    assert M.data[1, 2] - -np.sin(rot) < tol
    assert M.data[2, 2] - np.cos(rot) < tol
