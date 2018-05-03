import scipy.integrate
import logging


def ode45(f, tspan, y0, *args, **kwargs):
    """Implements interface similar to MATLAB's ode45 using scipy"""

    abstol = kwargs.get('abstol', 1e-5)
    reltol = kwargs.get('reltol', 1e-3)
    maxstep = kwargs.get('maxstep', 0.1)

    sol = scipy.integrate.solve_ivp(lambda t, y: f(t, y, *args), tspan, y0, rtol=reltol, atol=abstol, max_step=maxstep)

    return sol.t, sol.y


def warning(err, string):
    logging.warning('warning: ' + err)
    logging.warning(string)


def error(err, string):
    logging.error('error: ' + err)
    logging.error(string)
    raise RuntimeError(string)  # Raise error to notify shooting solver
    # exit

# specify default arguments here:


def processOdeArgs(**kwargs):
    defaults = {'normcontrol': 'on',  # ('on','off')
                # index array describing components that should be nonnegative
                'nonnegative': None,
                # relative tolerance (can be array of same dimension as y0)
                'reltol': 1e-5,
                'abstol': 1e-5,			# absolute tolerance
                'outputsel': None,		# which components to save
                # save output every outputsave steps
                'outputsave': None,
                'initialstep': None,
                'maxstep': None,
                'mass': None,
                'stats': 'off'			# statistics
                }

    if len(kwargs) > 0:
        for i in kwargs:
            defaults[i.lower()] = kwargs[i]

    # accept True instead of 'on' for certain options
    opts = ['stats', 'normcontrol']
    for o in opts:
        if defaults[o]:
            defaults[o] = 'on'

    return defaults
