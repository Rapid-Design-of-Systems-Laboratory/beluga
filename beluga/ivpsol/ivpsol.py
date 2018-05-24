import numpy as np
from scipy.optimize import minimize
import scipy.integrate
import time
from .ivp import sol
import copy
from beluga.utils import keyboard
from scipy.integrate import simps


class Algorithm(object):
    '''
    Object representing an algorithm that solves initial valued problems.

    This object serves as a base class for other algorithms.
    '''
    def __new__(cls, ivp=None):
        obj = super(Algorithm, cls).__new__(cls)

        if ivp is not None:
            return cls.__call__(obj, ivp)
        else:
            return obj

    def _reconstruct_quads(self, quadfun, x, y, quads0, *args):
        '''
        Reconstructs full quadratures over a trajectory base space.

        :param quadfun:
        :param x:
        :param y:
        :param quads0:
        :param args:
        :return:
        '''
        # TODO: This loop, in combination with _integrate_quads loop, is really slow
        out = quads0
        for ii in range(len(x)-1):
            ind = ii+2
            out = np.hstack((out, integrate_quads(quadfun, x[0:ind], y.T[0:ind].T, quads0, *args)))
        return out


class Propagator(Algorithm):
    '''
    Propagator of differential equations
    '''

    def __call__(self, ivp, tspan, y0, q0, *args, **kwargs):
        '''
        Propagates the differential equations over a defined time interval.

        :param ivp: Initial value problem (will be deprecated)
        :param tspan: Independent time interval.
        :param y0: Initial state position.
        :param q0: Initial quad position.
        :param args: Additional arguments required by EOM files.
        :param kwargs: Additional parameters accepted by the solver.
        :return: A full reconstructed trajectory.
        '''
        # Create a deep copy to prevent corrupting original data
        # TODO: Break up ivp() into something smarter.
        problem_copy = copy.deepcopy(ivp)
        eomfun = problem_copy.equations_of_motion
        quadfun = problem_copy.quadratures

        abstol = kwargs.get('abstol', 1e-5)
        reltol = kwargs.get('reltol', 1e-3)
        maxstep = kwargs.get('maxstep', 0.1)

        int_sol = scipy.integrate.solve_ivp(lambda t, y: eomfun(t, y, *args), tspan, y0, rtol=reltol, atol=abstol, max_step=maxstep)

        solout = sol()
        solout.x = int_sol.t
        solout.y = int_sol.y

        if quadfun is not None:
            solout.quads = self._reconstruct_quads(quadfun, solout.x, solout.y, q0, *args)

        return solout

class trajectory(object):
    '''
    Class containing information for a trajectory. A trajectory
    is a curve on a manifold that is also an integral curve
    of a vector field.

    .. math::
        \\gamma(t) : I \\subset \\mathbb{R} \\rightarrow B
    '''
    def __new__(cls, *args, **kwargs):
        obj = super(trajectory, cls).__new__(cls)
        obj.t = None
        obj.y = None
        obj.q = None
        obj.u = None

        l = len(args)
        if l >= 1:
            obj.t = args[0]

        if l >= 2:
            obj.y = args[1]

        if l >= 3:
            obj.q = args[2]

        if l >= 4:
            obj.u = args[3]

        return obj

    def __call__(self, t):
        '''

        :param t: Time input.
        :return: Returns position values :math:`(y, q, u) \\in B`
        '''

        y_val = None
        q_val = None
        u_val = None

        if len(self.t) == 0:
            return None

        if len(self.y.shape) == 1:
            dim = 1
        else:
            dim = self.y.shape[1]
        # keyboard()
        if dim == 1:
            y_val = np.array([np.interp(t, self.t, self.y)])
        else:
            y_val = np.array([np.interp(t, self.t, self.y.T[ii]) for ii in range(dim)])

        return y_val, q_val, u_val

    def __getitem__(self, item):
        t_val = None
        y_val = None
        q_val = None
        u_val = None
        if self.t is not None:
            t_val = self.t[item]

        if self.y is not None:
            y_val = self.y[item]

        if self.q is not None:
            q_val = self.q[item]

        if self.u is not None:
            u_val = self.u[item]

        return t_val, y_val, q_val, u_val

def reconstruct(quadfun, gamma, *args):
    '''
    Completely reconstructs a trajectory for all time in :math:`\\gamma`.

    .. math::
        \\begin{aligned}
            \\text{reconstruct} : \\gamma \\in B/Q &\\rightarrow \\gamma \\in B \\\\
            (g, \\gamma) &\\mapsto \\int_{t_0}^{t} g \\circ \\gamma dt \\; \\forall \\; t
        \\end{aligned}

    :param quadfun: Equations of motion on the symmetry space.
    :param gamma: Trajectory in quotient space :math:`B/Q`.
    :param args: Additional arguments needed by quadfun.
    :return: :math:`\\gamma` - Reconstructed trajectory in total space :math:`B`.
    '''
    gamma = copy.copy(gamma)
    if gamma.q is None:
        q0 = 0
    else:
        q0 = gamma.q[0]

    l = len(gamma)
    temp_q = integrate_quads(quadfun, [gamma.t[0], gamma.t[0]], gamma, *args)

    for ii in range(l-1):
        qf = integrate_quads(quadfun, [gamma.t[ii], gamma.t[ii+1]], gamma, *args)
        temp_q = np.vstack((temp_q, temp_q[-1] + qf))

    gamma.q = temp_q + q0
    return gamma

def integrate_quads(quadfun, tspan, gamma, *args):
    '''
    Integrates quadratures over a trajectory base space. Only returns the terminal point.

    .. math::
        \\begin{aligned}
            \\text{integrate_quads} : \\gamma \\in B/Q &\\rightarrow q_f \\in B \\\\
            (g, \\gamma) &\\mapsto \\int_{t_0}^{t_f} g \\circ \\gamma dt
        \\end{aligned}

    :param quadfun: Equations of motion on the symmetry space.
    :param tspan: Time interval to integrate over.
    :param gamma: Trajectory in quotient space :math:`B/Q`.
    :param args: Additional arguments needed by quadfun.
    :return: Value of the quads at :math:`t_f`.
    '''

    if tspan[0] < gamma.t[0]:
        raise Exception('Time span out of integration bounds.')

    if tspan[-1] > gamma.t[-1]:
        raise Exception('Time span out of integration bounds.')

    l = len(gamma.t)
    x_set_temp = np.arange(0,l,1)

    ind0 = int(np.ceil(np.interp(tspan[0], gamma.t, x_set_temp)))
    indf = int(np.ceil(np.interp(tspan[-1], gamma.t, x_set_temp)))

    if tspan[0] != gamma.t[ind0]:
        x_interp = np.array([tspan[0]])
    else:
        x_interp = np.array([])

    x_interp = np.hstack((x_interp, gamma.t[ind0:indf]))

    if tspan[-1] != gamma.t[indf-1]:
        x_interp = np.hstack((x_interp, tspan[-1]))

    y0, q0, u0 = gamma(x_interp[0])

    # Evaluate the quad function over every point in the given interval
    dq = np.array([quadfun(time, gamma(time)[0], *args) for time in x_interp])

    # Integrate the quad func using numerical quadrature
    qf_m0 = simps(dq.T, x=x_interp)

    # Add the initial state to get the final state.
    if q0 is None:
        q0 = 0

    qf = qf_m0 + q0

    return qf
