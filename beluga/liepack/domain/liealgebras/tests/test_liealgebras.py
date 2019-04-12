from beluga.liepack import commutator
from beluga.liepack.domain.liealgebras import *

from random import uniform

tol = 1e-15


def test_rn():
    x = rn(4)
    y = rn(4)
    z = rn(4)
    zero = rn(4)

    # Vector basis tests
    x.set_vector([1, 0, 0])
    y.set_vector([0, 1, 0])
    z.set_vector([0, 0, 1])
    zero.zero()
    a = 2
    b = 3

    # Algebra definitions
    assert ((x + y) * z == x * z + y * z).all()  # Right distributive
    assert (x * (y + z) == x * y + x * z).all()  # Left Distributive
    assert ((a * x) * (b * y) == (a * b) * (x * y)).all()  # Scalar multiplication

    # Lie algebra definitions
    assert (commutator(a * x + b * y, z) == a * commutator(x, z) + b * commutator(y, z)).all()  # Bilinearity
    assert (commutator(x, x) == zero).all()  # Alternativity
    assert (commutator(y, y) == zero).all()
    assert (commutator(z, z) == zero).all()
    assert (commutator(x, commutator(y, z)) + commutator(z, commutator(x, y)) + commutator(y, commutator(z, x)) == zero).all()  # Jacobi Identity
    assert (commutator(x, y) == -commutator(y, x)).all()  # Anticommutivity

    # rn specific (not simple)
    assert (commutator(x, y) == zero).all()
    assert (commutator(x, z) == zero).all()
    assert (commutator(y, z) == zero).all()

    # Random vector tests
    x.random()
    y.random()
    z.random()
    zero.zero()
    a = uniform(-1, 1)
    b = uniform(-1, 1)

    # Algebra definitions
    assert (((x + y) * z) - (x * z + y * z) < tol).all()  # Right distributive
    assert ((x * (y + z)) - (x * y + x * z) < tol).all()  # Left Distributive
    assert (((a * x) * (b * y)) - ((a * b) * (x * y)) < tol).all()  # Scalar multiplication

    # Lie algebra definitions
    assert ((commutator(a * x + b * y, z)) - (a * commutator(x, z) + b * commutator(y, z)) < tol).all()  # Bilinearity
    assert (commutator(x, x) == zero).all()  # Alternativity
    assert (commutator(y, y) == zero).all()
    assert (commutator(z, z) == zero).all()
    assert (commutator(x, commutator(y, z)) + commutator(z, commutator(x, y)) + commutator(y, commutator(z, x)) < tol).all()  # Jacobi Identity
    assert (commutator(x, y) == -commutator(y, x)).all()  # Anticommutivity


def test_so():
    x = so(3)
    y = so(3)
    z = so(3)
    zero = so(3)

    # Vector basis tests
    x.set_vector([1, 0,0])
    y.set_vector([0,1,0])
    z.set_vector([0,0,1])
    zero.zero()
    a = 2
    b = 3

    # Algebra definitions
    assert ((x + y) * z == x * z + y * z).all()  # Right distributive
    assert (x * (y + z) == x * y + x * z).all()  # Left Distributive
    assert ((a * x) * (b * y) == (a * b) * (x * y)).all()  # Scalar multiplication

    # Lie algebra definitions
    assert (commutator(a * x + b * y, z) == a * commutator(x, z) + b * commutator(y, z)).all()  # Bilinearity
    assert (commutator(x, x) == zero).all()  # Alternativity
    assert (commutator(y, y) == zero).all()
    assert (commutator(z, z) == zero).all()
    assert (commutator(x, commutator(y, z)) + commutator(z, commutator(x, y)) + commutator(y, commutator(z, x)) == zero).all()  # Jacobi Identity
    assert (commutator(x, y) == -commutator(y, x)).all()  # Anticommutivity

    # so specific (simple)
    assert (commutator(x, y) == z).all()
    assert (commutator(x, z) == -y).all()
    assert (commutator(y, z) == x).all()

    # Random vector tests
    x.random()
    y.random()
    z.random()
    zero.zero()
    a = uniform(-1,1)
    b = uniform(-1,1)

    # Algebra definitions
    assert (((x + y) * z) - (x * z + y * z) < tol).all()  # Right distributive
    assert ((x * (y + z)) - (x * y + x * z) < tol).all()  # Left Distributive
    assert (((a * x) * (b * y)) - ((a * b) * (x * y)) < tol).all()  # Scalar multiplication

    # Lie algebra definitions
    assert ((commutator(a * x + b * y, z)) - (a * commutator(x, z) + b * commutator(y, z)) < tol).all()  # Bilinearity
    assert (commutator(x, x) == zero).all()  # Alternativity
    assert (commutator(y, y) == zero).all()
    assert (commutator(z, z) == zero).all()
    assert (commutator(x, commutator(y, z)) + commutator(z, commutator(x, y)) + commutator(y, commutator(z, x)) < tol).all()  # Jacobi Identity
    assert (commutator(x, y) == -commutator(y, x)).all()  # Anticommutivity

def test_sp():
    x = sp(2)
    y = sp(2)
    z = sp(2)
    zero = sp(2)

    # Vector basis tests
    x.set_vector([1,0,0])
    y.set_vector([0,1,0])
    z.set_vector([0,0,1])
    zero.zero()
    a = 2
    b = 3

    # Algebra definitions
    assert ((x + y)*z == x*z + y*z).all()  # Right distributive
    assert (x*(y + z) == x*y + x*z).all()  # Left Distributive
    assert ((a*x) * (b*y) == (a*b) * (x*y)).all()  #Scalar multiplication

    # Lie algebra definitions
    assert (commutator(a*x + b*y, z) == a*commutator(x,z) + b*commutator(y,z)).all()  # Bilinearity
    assert (commutator(x, x) == zero).all()  # Alternativity
    assert (commutator(y, y) == zero).all()
    assert (commutator(z, z) == zero).all()
    assert (commutator(x, commutator(y,z)) + commutator(z, commutator(x,y)) + commutator(y, commutator(z,x)) == zero).all()  # Jacobi Identity
    assert (commutator(x,y) == -commutator(y,x)).all()  # Anticommutivity

    # sp specific (simple)
    assert (commutator(x,y) == 2*y).all()
    assert (commutator(x,z) == -2*z).all()
    assert (commutator(y,z) == x).all()

    # Random vector tests
    x.random()
    y.random()
    z.random()
    zero.zero()
    a = uniform(-1,1)
    b = uniform(-1,1)

    # Algebra definitions
    assert (((x + y) * z) - (x * z + y * z) < tol).all()  # Right distributive
    assert ((x * (y + z)) - (x * y + x * z) < tol).all()   # Left Distributive
    assert (((a * x) * (b * y)) - ((a * b) * (x * y)) < tol).all()   # Scalar multiplication

    # Lie algebra definitions
    assert ((commutator(a * x + b * y, z)) - (a * commutator(x, z) + b * commutator(y, z)) < tol).all()   # Bilinearity
    assert (commutator(x, x) == zero).all()  # Alternativity
    assert (commutator(y, y) == zero).all()
    assert (commutator(z, z) == zero).all()
    assert (commutator(x, commutator(y, z)) + commutator(z, commutator(x, y)) + commutator(y, commutator(z, x)) < tol).all()  # Jacobi Identity
    assert (commutator(x, y) == -commutator(y, x)).all()  # Anticommutivity
