from math import *
import beluga.bvpsol as bvpsol
import beluga.bvpsol.algorithms as algorithms
import numpy as np
import numpy.testing as npt
import pytest
import os

#TODO: Write test where the number of arcs is more than number of elements in guess
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

    # Checks basic algorithm
    solver_fd1  = algorithms.MultipleShooting(derivative_method='fd',cached=False,tolerance=1e-6,number_arcs=2)
    solver_csd1 = algorithms.MultipleShooting(derivative_method='csd',cached=False,tolerance=1e-6,number_arcs=2)

    # Check arc stitching as well as # arcs > # cpus. Include constraints later
    solver_fd3  = algorithms.MultipleShooting(derivative_method='fd',cached=False,tolerance=1e-6,number_arcs=2*os.cpu_count())
    solver_csd3 = algorithms.MultipleShooting(derivative_method='csd',cached=False,tolerance=1e-6,number_arcs=2*os.cpu_count())

    # Multiple shooting solves it if ithad only two points
    x = np.linspace(0,1,3)
    bad_y = np.array([[0,1,0],[0,1,2]])

    # Test that raises error
    bvp = bvpsol.BVP(odefn,bcfn)
    bvp.solution = bvpsol.Solution(x,bad_y,[pi/2])
    # with pytest.raises(np.linalg.linalg.LinAlgError):
    sol = solver_fd1.solve(bvp) #Fails
    assert not sol.converged

    y = np.array([[0,0.1],[0,2]])
    bvp.solution = bvpsol.Solution(x,y,[pi/2])

    sol_fd1 = solver_fd1.solve(bvp)
    sol_fd3 = solver_fd3.solve(bvp)
    sol_csd1 = solver_csd1.solve(bvp)
    sol_csd3 = solver_csd3.solve(bvp)

    # Computing analytic solutions
    A = 2
    B = 0
    x_fd1 = sol_fd1.parameters[0]*sol_fd1.x
    y_expected_fd1 = [  A*np.sin(x_fd1) + B*np.cos(x_fd1),
                        A*np.cos(x_fd1) - B*np.sin(x_fd1)]

    x_fd3 = sol_fd3.parameters[0]*sol_fd3.x
    y_expected_fd3 = [  A*np.sin(x_fd3) + B*np.cos(x_fd3),
                        A*np.cos(x_fd3) - B*np.sin(x_fd3)]
    x_csd1 = sol_csd1.parameters[0]*sol_csd1.x
    y_expected_csd1 = [  A*np.sin(x_csd1) + B*np.cos(x_csd1),
                         A*np.cos(x_csd1) - B*np.sin(x_csd1)]

    x_csd3 = sol_csd3.parameters[0]*sol_csd3.x
    y_expected_csd3 = [  A*np.sin(x_csd3) + B*np.cos(x_csd3),
                        A*np.cos(x_csd3) - B*np.sin(x_csd3)]

    # Test for Finite Difference solver
    npt.assert_almost_equal(sol_fd1.y,y_expected_fd1,decimal=5)
    npt.assert_almost_equal(sol_fd3.y,y_expected_fd3,decimal=5)

    # Test for Complex Step solver
    npt.assert_almost_equal(sol_csd1.y,y_expected_csd1,decimal=5)
    npt.assert_almost_equal(sol_csd3.y,y_expected_csd3,decimal=5)

if __name__ == '__main__':
    test_solve()
