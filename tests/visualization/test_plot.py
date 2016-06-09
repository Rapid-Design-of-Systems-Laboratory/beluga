import dill, os, numpy as np, numpy.testing as npt
from math import *
from beluga.utils import ode45, keyboard
from beluga.visualization.elements import Plot

def test_plot():
    with open(os.path.join(os.path.dirname(__file__),'planar.dill'),'rb') as f:
        out = dill.load(f)

    sol = out['solution']

    mesh_size = len(sol[0][0].x)
    # Testing default behavior (retain mesh size)
    p = Plot(0, 0, mesh_size)
    p.line('v','h')
    p.xlabel('v (m/s)')
    p.ylabel('h (m)')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(p.plot_data[0]['data'][0]['x_data'],sol[0][0].y[2,:])
    npt.assert_equal(p.plot_data[0]['data'][0]['y_data'],sol[0][0].y[0,:])

    # Testing behavior with line series
    p = Plot(0, 0, mesh_size)
    p.line_series('v','h', skip=9)
    p.xlabel('v (m/s)')
    p.ylabel('h (m)')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(p.plot_data[0]['data'][0]['x_data'],sol[0][0].y[2,:])
    npt.assert_equal(p.plot_data[0]['data'][0]['y_data'],sol[0][0].y[0,:])
    npt.assert_equal(p.plot_data[0]['data'][1]['x_data'],sol[0][10].y[2,:])
    npt.assert_equal(p.plot_data[0]['data'][1]['y_data'],sol[0][10].y[0,:])

    p.line_series('v','h', start=1, skip=3)
    p.xlabel('v (m/s)')
    p.ylabel('h (m)')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(len(p.plot_data[1]['data']), 3)
    npt.assert_equal(p.plot_data[1]['data'][0]['x_data'],sol[0][1].y[2,:])
    npt.assert_equal(p.plot_data[1]['data'][0]['y_data'],sol[0][1].y[0,:])
    npt.assert_equal(p.plot_data[1]['data'][1]['x_data'],sol[0][5].y[2,:])
    npt.assert_equal(p.plot_data[1]['data'][1]['y_data'],sol[0][5].y[0,:])
    npt.assert_equal(p.plot_data[1]['data'][2]['x_data'],sol[0][9].y[2,:])
    npt.assert_equal(p.plot_data[1]['data'][2]['y_data'],sol[0][9].y[0,:])

    p.line_series('v','h', start=1, skip=3, end=7)
    p.xlabel('v (m/s)')
    p.ylabel('h (m)')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(len(p.plot_data[2]['data']), 2)
    npt.assert_equal(p.plot_data[2]['data'][0]['x_data'],sol[0][1].y[2,:])
    npt.assert_equal(p.plot_data[2]['data'][0]['y_data'],sol[0][1].y[0,:])
    npt.assert_equal(p.plot_data[2]['data'][1]['x_data'],sol[0][5].y[2,:])
    npt.assert_equal(p.plot_data[2]['data'][1]['y_data'],sol[0][5].y[0,:])

    # Testing behavior with solution selector options
    p = Plot(0,4, mesh_size)
    p.line('theta','gam')
    p.preprocess(out['solution'],out['problem_data'])
    npt.assert_equal(p.plot_data[0]['data'][0]['x_data'],sol[0][4].y[1,:])
    npt.assert_equal(p.plot_data[0]['data'][0]['y_data'],sol[0][4].y[3,:])

    # Testing expressions with variables and constants or with multiple variables
    p = Plot(0, 0, mesh_size)
    p.line('theta+v*gam','rho0*exp(-h/H)')
    p.preprocess(out['solution'],out['problem_data'])

    const = sol[0][0].aux['const']
    rho = const['rho0']*np.exp(-sol[0][0].y[0,:]/const['H'])
    xval = sol[0][0].y[1,:] + sol[0][0].y[2,:]*sol[0][0].y[3,:]

    npt.assert_equal(p.plot_data[0]['data'][0]['x_data'],xval)
    npt.assert_equal(p.plot_data[0]['data'][0]['y_data'],rho)
