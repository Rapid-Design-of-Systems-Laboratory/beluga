from beluga.liepack.domain.liegroups import *
import numpy as np

tol = 1e-15

def test_SP():
    G = SP(2)
    G.random()
    Ju = np.hstack((np.zeros(1), np.ones(1)))
    Jl = np.hstack((-np.ones(1), np.zeros(1)))
    J = np.vstack((Ju, Jl))
    J2 = G.data.T @ J @ G.data # Symplectic matrix satisfies G^T * J * G = J
    assert (J - J2 < tol).all()