from beluga.liepack import Commutator
from beluga.liepack.domain.liealgebras import *

from random import uniform

tol = 1e-15

def test_rn():
    x = rn(3)
    y = rn(3)
    z = rn(3)
    zero = rn(3)

    # Vector basis tests
    x.set_vector([1,0,0])
    y.set_vector([0,1,0])
    z.set_vector([0,0,1])
    zero.zero()
    a = 2
    b = 3

    # Algebra definitions
    assert (x + y)*z == x*z + y*z  # Right distributive
    assert x*(y + z) == x*y + x*z  # Left Distributive
    assert (a*x) * (b*y) == (a*b) * (x*y)  # Scalar multiplication

    # Lie algebra definitions
    assert Commutator(a*x + b*y, z) == a*Commutator(x,z) + b*Commutator(y,z)  # Bilinearity
    assert Commutator(x,x) == Commutator(y,y) == Commutator(z,z) == zero  # Alternativity
    assert Commutator(x, Commutator(y,z)) + Commutator(z, Commutator(x,y)) + Commutator(y, Commutator(z,x)) == zero  # Jacobi Identity
    assert Commutator(x,y) == -Commutator(y,x)  # Anticommutivity

    # rn specific (not simple)
    assert Commutator(x,y) == Commutator(x,z) == Commutator(y,z) == zero

    # Random vector tests
    x.random()
    y.random()
    z.random()
    zero.zero()
    a = uniform(-1,1)
    b = uniform(-1,1)

    # Algebra definitions
    assert (x + y) * z == x * z + y * z  # Right distributive
    assert x * (y + z) == x * y + x * z  # Left Distributive
    assert (a * x) * (b * y) == (a * b) * (x * y)  # Scalar multiplication

    # Lie algebra definitions
    assert Commutator(a * x + b * y, z) == a * Commutator(z, x) + b * Commutator(z, y)  # Bilinearity
    assert Commutator(x, x) == Commutator(y, y) == Commutator(z, z) == zero  # Alternativity
    assert Commutator(x, Commutator(y, z)) + Commutator(z, Commutator(x, y)) + Commutator(y, Commutator(z, x)) == zero  # Jacobi Identity
    assert Commutator(x, y) == -Commutator(y, x)  # Anticommutivity

    # rn specific (not simple)
    assert Commutator(x, y) == Commutator(x, z) == Commutator(y, z) == zero

def test_so():
    x = so(3)
    y = so(3)
    z = so(3)
    zero = so(3)

    # Vector basis tests
    x.set_vector([1,0,0])
    y.set_vector([0,1,0])
    z.set_vector([0,0,1])
    zero.zero()
    a = 2
    b = 3

    # Algebra definitions
    assert (x + y)*z == x*z + y*z  # Right distributive
    assert x*(y + z) == x*y + x*z  # Left Distributive
    assert (a*x) * (b*y) == (a*b) * (x*y)  #Scalar multiplication

    # Lie algebra definitions
    assert Commutator(a*x + b*y, z) == a*Commutator(x,z) + b*Commutator(y,z)  # Bilinearity
    assert Commutator(x,x) == Commutator(y,y) == Commutator(z,z) == zero  # Alternativity
    assert Commutator(x, Commutator(y,z)) + Commutator(z, Commutator(x,y)) + Commutator(y, Commutator(z,x)) == zero  # Jacobi Identity
    assert Commutator(x,y) == -Commutator(y,x)  # Anticommutivity

    # so specific (simple)
    assert Commutator(x,y) == z
    assert Commutator(x,z) == -y
    assert Commutator(y,z) == x

    # Random vector tests
    x.random()
    y.random()
    z.random()
    zero.zero()
    a = uniform(-1,1)
    b = uniform(-1,1)

    # Algebra definitions
    assert ((x + y) * z) - (x * z + y * z) < tol  # Right distributive
    assert (x * (y + z)) - (x * y + x * z) < tol  # Left Distributive
    assert ((a * x) * (b * y)) - ((a * b) * (x * y)) < tol  # Scalar multiplication

    # Lie algebra definitions
    assert (Commutator(a * x + b * y, z)) - (a * Commutator(x, z) + b * Commutator(y, z)) < tol  # Bilinearity
    assert Commutator(x, x) == Commutator(y, y) == Commutator(z, z) == zero  # Alternativity
    assert Commutator(x, Commutator(y, z)) + Commutator(z, Commutator(x, y)) + Commutator(y, Commutator(z, x)) < tol  # Jacobi Identity
    assert Commutator(x, y) == -Commutator(y, x)  # Anticommutivity
