from beluga.liepack.domain.liealgebras import *
from beluga.liepack.domain.liegroups import *
from beluga.liepack import *

from random import uniform

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
    assert ((Commutator(x, Commutator(y, z)) + Commutator(y, Commutator(z, x)) + Commutator(z, Commutator(x, y))).data < 1e-16).all()
