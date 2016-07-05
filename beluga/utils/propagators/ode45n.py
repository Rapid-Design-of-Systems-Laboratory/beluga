import scipy.integrate
import numpy as np

def ode45n(f,tspan,y0,*args,**kwargs):
    """Implements interface similar to MATLAB's ode45 using scipy"""

    tt = tspan[0]
    yy = np.array([y0])

    from beluga.utils import keyboard

    r = scipy.integrate.ode(f).set_integrator('zvode', method='bdf')
    r.set_f_params(*args)   # Add extra arguments to be passed in
    r.set_initial_value(y0,tspan[0])

    if 'num_steps' in kwargs:
        num_steps = kwargs['num_steps']
    else:
        num_steps = 100 # HARDCODED num_steps


    tt = np.linspace(tspan[0],tspan[-1],num_steps)
    dt = tt[1]-tt[0]

    while r.successful() and r.t < tspan[-1]:
        r.integrate(r.t+dt)
        yy = np.vstack((yy,r.y))  # Add new timestep as row

    return (tt,yy)