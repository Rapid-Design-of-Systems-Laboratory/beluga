import scipy.integrate
import numpy as np

from beluga.utils.ode45_old import ode45_old

def ode_wrap(func,*args):   # Required for odeint
    def func_wrapper(t,y):
        return func(y,t,*args)
    return func_wrapper

def split_tspan(tspan):
# def split_tspan(tspan, y0):
    # Detect duplicates in time array to find arc junctions
    [arc_end_idx] = np.where(np.diff(tspan) == 0)
    # np.add() required because of how np.split works
    arc_end_idx = np.add(arc_end_idx,1)

    if len(arc_end_idx) > 0:
        return np.split(tspan,arc_end_idx)
    else:
        return tspan

    # if len(arc_end_idx) > 0:
    #     return (np.split(tspan,arc_end_idx),
    #             np.split(y0,arc_end_idx,axis=1))
    # else:
    #     return ([tspan],[y0])

def ode45_multi(f,tspan,y0,*args,**kwargs):
    from beluga.utils.joblib import Parallel, delayed
    from beluga.utils import keyboard

    if isinstance(tspan,np.ndarray):
        tspan = [tspan]

    if isinstance(y0,np.ndarray):
        y0 = [y0]

    # Propagate multiple arcs in parallel utilizing all cores available
    t_and_y = Parallel(n_jobs=-1)(delayed(ode45_old)(f,t,y,*args,**kwargs)
        for (t,y) in zip(tspan,y0))
    # t1_y1 = [ode45_old(f,t,y,*args,**kwargs) for (t,y) in t_and_y]
    return list(zip(*t_and_y))

def ode45(f,tspan,y0,*args,**kwargs):
    """Implements interface similar to MATLAB's ode45 using scipy"""

    # return ode45_old(f,tspan,y0,*args,**kwargs)

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
