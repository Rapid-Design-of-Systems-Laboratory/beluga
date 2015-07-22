import numpy as np
import numpy.testing as npt
from math import *
from beluga.utils.propagators import mcpi

def test_mcpi():
    """Test mcpi() against analytical solution"""
    k  = [-0.5, -0.2]
    def odefn(t,x,p,aux):
        return np.array([k[0]*x[0],k[1]*x[1]])

    y0 = np.array([10,-50])
    tspan = np.array([0, 1.0])
    [t1,x1] = mcpi(odefn,tspan,y0,5,[],{},tol=1e-5)
    x1_expected = np.array([y*np.exp(k_*t1) for (y,k_) in zip(y0,k)]).T
    npt.assert_almost_equal(x1,x1_expected,decimal=5)
