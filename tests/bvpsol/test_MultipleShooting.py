from math import *
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import numpy as np
import numpy.testing as npt
import pytest

def test_solve():
    """Test solver using analytic solution of a BVP"""
    def odefn(t,X,p,aux):
        y = X[0]
        ydot = X[1]
        xf = p[0]
        # y'' + y(x) = 0
        return xf*np.array([
            ydot,
            -y
        ])

    def bcfn(ya,yb,p,aux):
        # y(0) = 0
        # y(pi/2) = 2
        return np.array([
                    ya[0] - 0,
                    yb[0] - 2,
                    p[0]  - pi/2])

    solver_fd  = algorithms.MultipleShooting(derivative_method='fd',cached=False,tolerance=1e-6,number_arcs=2)

    # TODO: Implement complex step derivative in multiple shooting algorithm
    #solver_csd = algorithms.MultipleShooting(derivative_method='csd',cached=False,tolerance=1e-6,number_arcs=2)

    x = np.linspace(0,1,2)
    bad_y = np.array([[0,0],[0,2]])

    # Test that raises error
    bvp = bvpsol.BVP(odefn,bcfn)
    # bvp.solution = bvpsol.Solution(x,bad_y,[pi/2])
    # with pytest.raises(np.linalg.linalg.LinAlgError):
    #     solver_fd.solve(bvp)

    y = np.array([[0,0.1],[0,2]])
    bvp.solution = bvpsol.Solution(x,y,[pi/2])

    sol = solver_fd.solve(bvp)

    # Computing analytic solutions
    A = 2
    B = 0
    x = sol.parameters[0]*sol.x
    y_expected = [  A*np.sin(x) + B*np.cos(x),
                    A*np.cos(x) - B*np.sin(x)]

    # Test for Finite Difference solver
    npt.assert_almost_equal(sol.y,y_expected,decimal=5)

    # Test for Complex Step solver
    #sol2 = solver_csd.solve(bvp,solinit)
    #npt.assert_almost_equal(sol2.y,y_expected,decimal=5)

if __name__ == '__main__':
    test_solve()
