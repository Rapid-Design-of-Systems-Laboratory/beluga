import scipy.integrate
import numpy as np

from beluga.utils.ode45_old import ode45_old

def ode_wrap(func,*args):   # Required for odeint
    def func_wrapper(t,y):
        return func(y,t,*args)
    return func_wrapper

def ode45(f,tspan,y0,*args,**kwargs):
    """Implements interface similar to MATLAB's ode45 using scipy"""

    return ode45_old(f,tspan,y0,*args,**kwargs)

    if len(tspan) == 2:
        # TODO: Change hardcoding?
        tspan = np.linspace(tspan[0],tspan[1],200)
    t0 = tspan[0]
    t1 = tspan[1]
    yy = scipy.integrate.odeint(ode_wrap(f,*args),y0,tspan)
    return (tspan,yy)

    tt = tspan[0]
    yy = np.array([y0])

    from beluga.utils import keyboard

    r = scipy.integrate.ode(f).set_integrator('lsoda')
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
