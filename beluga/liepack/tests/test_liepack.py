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

    G.set_data(exp(x*rot).data)

    # Use case tests
    AdG = Adjoint(G)

    assert (AdG(y).get_vector() - np.array([0, np.cos(rot), np.sin(rot)]) < tol).all()
    assert (AdG(z).get_vector() - np.array([0, -np.sin(rot), np.cos(rot)]) < tol).all()
    n1 = np.linalg.norm(y.get_vector())
    n2 = np.linalg.norm(z.get_vector())
    rot = np.pi/4
    G.set_data(exp(x * rot).data)
    assert (Adjoint(G,y).data - (y+z).data/(np.sqrt(n1**2 + n2**2)) < tol).all()


def test_Commutator():
    x = so(3)
    y = so(3)
    z = so(3)

    x.set_vector([1,0,0])
    y.set_vector([0,1,0])
    z.set_vector([0,0,1])

    # Use case tests
    assert Commutator(x, y) == z
    assert Commutator(y, x) == -z
    assert Commutator(x, None)(y) == z
    assert Commutator(None, y)(x) == z
    assert Commutator(None, None)(y,x) == -z

    adjoint = Commutator(x)
    assert adjoint(y) == z
    assert adjoint(z) == -y

    # Lie algebra identities
    A = uniform(-1,1)
    B = uniform(-1,1)
    assert Commutator(x + y, z) == (Commutator(x, z) + Commutator(y, z))
    assert Commutator(x,x) == 0
    assert Commutator(x,y) == -Commutator(y, x)
    assert Commutator(x, Commutator(y, z)) + Commutator(y, Commutator(z, x)) + Commutator(z, Commutator(x, y)) == 0
    assert Commutator(A*x + B*y, z) == A*Commutator(x,z) + B*Commutator(y,z)
    assert Commutator(z, A*x + B*y) == Commutator(z, x)*A + Commutator(z,y)*B

    x.random()
    y.random()
    z.random()
    assert ((Commutator(x, Commutator(y, z)) + Commutator(y, Commutator(z, x)) + Commutator(z, Commutator(x, y))).data < tol).all()

def test_exp():
    x = so(3)
    M = SO(3)

    x.set_vector([1, 0, 0])
    rot = np.pi/4

    assert isinstance(exp(x), LieGroup)

    M.set_data(exp(x*rot).data)

    assert M.data[0, 0] == 1
    assert M.data[1, 0] == 0
    assert M.data[2, 0] == 0
    assert M.data[0, 1] == 0
    assert M.data[1, 1] - np.cos(rot) < tol
    assert M.data[2, 1] - np.sin(rot) < tol
    assert M.data[0, 2] == 0
    assert M.data[1, 2] - -np.sin(rot) < tol
    assert M.data[2, 2] - np.cos(rot) < tol
