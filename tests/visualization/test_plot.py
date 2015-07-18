import dill, os, numpy as np, numpy.testing as npt
from math import *
from beluga.utils import ode45, keyboard
from beluga.visualization.elements import Plot

def test_plot():
    with open(os.path.join(os.path.dirname(__file__),'planar.dill'),'rb') as f:
        out = dill.load(f)

    sol = out['solution']

    # Testing default behavior
    p = Plot()
    p.x('v')
    p.y('h')
    p.xlabel('v (m/s)')
    p.ylabel('h (m)')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(p.x_data,sol[0][0].y[2,:])
    npt.assert_equal(p.y_data,sol[0][0].y[0,:])
    # sol[0][4].prepare(out['problem_data'])
    # print(sol[0][4].evaluate('amax(h)'))

    # Testing behavior with solution selector options
    p = Plot(0,4)
    p.x('theta')
    p.y('gam')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(p.x_data,sol[0][4].y[1,:])
    npt.assert_equal(p.y_data,sol[0][4].y[3,:])

    # Testing expressions with variables and constants or with multiple variables
    p = Plot()
    p.x('theta+v*gam')
    p.y('rho0*exp(-h/H)')
    p.preprocess(out['solution'],out['problem_data'])

    const = sol[0][0].aux['const']

    rho = const['rho0']*np.exp(-sol[0][0].y[0,:]/const['H'])
    xval = sol[0][0].y[1,:] + sol[0][0].y[2,:]*sol[0][0].y[3,:]

    npt.assert_equal(p.x_data,xval)
    npt.assert_equal(p.y_data,rho)
