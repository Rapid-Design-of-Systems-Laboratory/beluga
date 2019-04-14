from beluga.optimlib import Manifold, FiberBundle


def test_Manifold():
    M = Manifold(['x', 'y'], 'test_manifold')
    assert M.dimension == 2

    x = M.base_coords
    dx = M.base_oneforms
    D_x = M.base_vectors

    f = x[0]**2 + x[1]**2
    df = M.exteriorderivative(f)
    assert df == 2*x[0]*dx[0] + 2*x[1]*dx[1]
