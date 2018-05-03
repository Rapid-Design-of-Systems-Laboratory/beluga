from beluga.ivpsol.ivpsol import Collocation
from beluga.ivpsol.ivp import ivp
import numpy as np


def test_Collocation():
    Col = Collocation()
    Col.number_of_odes = 3
    Col.number_of_nodes = 3
    Col.number_of_quads = 3
    Col.number_of_params = 2
    prob = ivp()
    prob.sol.x = np.array([0, 1])
    prob.sol.y = np.array([[1,2,3],[4,5,6],[7,8,9]])
    prob.sol.quads0 = np.array([10,11,12])
    prob.sol.params = np.array([13,14])
    prob.sol.consts = np.array([15])

    # Check wrapping and unwrapping
    vectorized = Col._wrap_params(prob.sol.y, prob.sol.quads0, prob.sol.params)
    assert np.array_equal(vectorized, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
    X,q,p = Col._unwrap_params(vectorized)
    assert np.array_equal(X, prob.sol.y)
    assert np.array_equal(q, prob.sol.quads0)
    assert np.array_equal(p, prob.sol.params)

    Col.number_of_quads = 0
    vectorized = Col._wrap_params(prob.sol.y, [], prob.sol.params)
    assert np.array_equal(vectorized, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14]))
    X, q, p = Col._unwrap_params(vectorized)
    assert np.array_equal(X, prob.sol.y)
    assert np.array_equal(q, np.array([]))
    assert np.array_equal(p, prob.sol.params)