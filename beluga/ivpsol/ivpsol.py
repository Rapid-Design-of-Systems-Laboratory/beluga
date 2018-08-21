import numpy as np
from scipy.integrate import solve_ivp, simps
import scipy.interpolate
import copy

from beluga.ivpsol import RKMK, Flow
from beluga.liepack.domain.hspaces import HLie
from beluga.liepack.domain.liegroups import RN
from beluga.liepack.domain.liealgebras import rn
from beluga.liepack import exp
from beluga.liepack.field import VectorField

class Algorithm(object):
    """
    Object representing an algorithm that solves initial valued problems.

    This object serves as a base class for other algorithms.
    """

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)

        return obj


class Propagator(Algorithm):
    """
    Propagator of differential equations.
    """

    def __new__(cls, *args, **kwargs):
        """
        Creates a new Propagator object.

        :param args: Unused
        :param kwargs: Additional parameters accepted by the solver.
        :return: Propagator object.

        +------------------------+-----------------+--------------------+
        | Valid kwargs           | Default Value   | Valid Values       |
        +========================+=================+====================+
        | abstol                 | 1e-6            |  > 0               |
        +------------------------+-----------------+--------------------+
        | maxstep                | 0.1             |  > 0               |
        +------------------------+-----------------+--------------------+
        | reltol                 | 1e-6            |  > 0               |
        +------------------------+-----------------+--------------------+
        | program                | 'scipy'         |  {'scipy', 'lie'}  |
        +------------------------+-----------------+--------------------+
        | method                 | 'RKMK'          |  {'RKMK'}          |
        +------------------------+-----------------+--------------------+
        | stepper                | 'RK45'          |  see ivp methods   |
        +------------------------+-----------------+--------------------+
        | variable_step          | True            |  bool              |
        +------------------------+-----------------+--------------------+
        """

        obj = super().__new__(cls, *args, **kwargs)
        obj.abstol = kwargs.get('abstol', 1e-6)
        obj.maxstep = kwargs.get('maxstep', 0.1)
        obj.reltol = kwargs.get('reltol', 1e-6)
        obj.program = kwargs.get('program', 'scipy').lower()
        obj.method = kwargs.get('method', 'RKMK').upper()
        obj.stepper = kwargs.get('stepper', 'RK45').upper()
        obj.variable_step = kwargs.get('variable_step', True)
        return obj

    def __call__(self, eom_func, quad_func, tspan, y0, q0, *args, **kwargs):
        r"""
        Propagates the differential equations over a defined time interval.

        :param eom_func: Function representing the equations of motion.
        :param quad_func: Function representing the quadratures.
        :param tspan: Independent time interval.
        :param y0: Initial state position.
        :param q0: Initial quad position.
        :param args: Additional arguments required by EOM files.
        :param kwargs: Unused.
        :return: A full reconstructed trajectory, :math:`\gamma`.
        """
        y0 = np.array(y0, dtype=np.float64)

        if self.program == 'scipy':
            int_sol = solve_ivp(lambda t, y: eom_func(t, y, *args), [tspan[0], tspan[-1]], y0,
                                rtol=self.reltol, atol=self.abstol, max_step=self.maxstep)
            gamma = Trajectory(int_sol.t, int_sol.y.T)

        elif self.program == 'lie':
            dim = y0.shape[0]
            g = rn(dim)
            g.set_vector(y0)
            y = HLie(RN(dim), exp(g).data)
            vf = VectorField(y)
            vf.set_equationtype('general')

            def M2g(t, y):
                vec = y.data[:-1,-1]
                out = eom_func(t, vec, *args)
                g = rn(dim)
                g.set_vector(out)
                return g

            vf.set_M2g(M2g)
            if self.method == 'RKMK':
                ts = RKMK()
            else:
                raise NotImplementedError

            ts.setmethod(self.stepper)
            f = Flow(ts, vf, variablestep=self.variable_step)
            ti, yi = f(y, tspan[0], tspan[-1], self.maxstep)
            gamma = Trajectory(ti, np.vstack([_.data[:-1,-1] for _ in yi])) # Hardcoded assuming RN

        if quad_func is not None:
            gamma = reconstruct(quad_func, gamma, *args)

        return gamma


class Trajectory(object):
    r"""
    Class containing information for a trajectory.

    .. math::
        \gamma(t) : I \subset \mathbb{R} \rightarrow B
    """

    def __new__(cls, *args, **kwargs):
        r"""
        Creates a new Trajectory object.

        :param args: :math:`(t, y, q, u)`
        :param kwargs: Unused.
        :return: Trajectory object.
        """

        obj = super(Trajectory, cls).__new__(cls)
        obj.t = None
        obj.y = None
        obj.q = None
        obj.u = None

        interpolation_type = kwargs.get('interpolation_type', 'linear').lower()
        obj.interpolation_type = interpolation_type

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

    def __init__(self, *args, **kwargs):
        self.interpolate = None
        self.set_interpolate_function(self.interpolation_type)

    def __call__(self, t):
        r"""
        Mapping function for a trajectory.

        :param t: Time as :math:`t \in \mathbb{R}`
        :return: Returns position values :math:`(y, q, u) \in B`
        """

        t = np.array(t, dtype=np.float64)
        y_val = None
        q_val = None
        u_val = None

        if len(self.t) == 0:
            return None, None, None

        if len(self.y.shape) == 1:
            dim = 1
        else:
            dim = self.y.shape[1]

        # This builds the interpolation function on the most up to date data
        if dim == 1:
            f = self.interpolate(self.t, self.y.T)
            if t.shape == ():
                y_val = np.array([f(t)])
            else:
                y_val = f(t)

            y_val = y_val.T

        else:
            f = [self.interpolate(self.t, self.y.T[ii]) for ii in range(dim)]
            y_val = np.array([f[ii](t) for ii in range(dim)]).T

        return y_val, q_val, u_val

    def set_interpolate_function(self, func):
        """
        Sets the function used for interpolation.

        :param func: Function for interpolation or a string for SciPy's interp1d(kind=func).
        """
        if callable(func):
            self.interpolate = func
        elif isinstance(func, str):
            func = func.lower()
            self.interpolate = lambda t, y: scipy.interpolate.interp1d(t, y, kind=func)

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

    def __len__(self):
        if self.t is None:
            return 0
        else:
            return len(self.t)


def reconstruct(quadfun, gamma, *args):
    r"""
    Completely reconstructs a trajectory for all time in :math:`\gamma`.

    .. math::
        \begin{aligned}
            \text{reconstruct} : \gamma \in B/Q &\rightarrow \gamma \in B \\
            (g, \gamma) &\mapsto \int_{t_0}^{t} g \circ \gamma dt \; \forall \; t
        \end{aligned}

    :param quadfun: Equations of motion on the symmetry space.
    :param gamma: Trajectory in quotient space :math:`B/Q`.
    :param args: Additional arguments needed by quadfun.
    :return: :math:`\gamma` - Reconstructed trajectory in total space :math:`B`.
    """

    gamma = copy.copy(gamma)
    if gamma.q is None:
        q0 = 0
    else:
        q0 = gamma.q[0]

    l = len(gamma)
    temp_q = np.array([integrate_quads(quadfun, [gamma.t[0], gamma.t[0]], gamma, *args)])

    for ii in range(l-1):
        qf = integrate_quads(quadfun, [gamma.t[ii], gamma.t[ii+1]], gamma, *args)
        temp_q = np.vstack((temp_q, temp_q[-1] + qf))

    gamma.q = temp_q + q0
    return gamma


def integrate_quads(quadfun, tspan, gamma, *args):
    r"""
    Integrates quadratures over a trajectory base space. Only returns the terminal point.

    .. math::
        \begin{aligned}
            \text{integrate_quads} : \gamma \in B/Q &\rightarrow q_f \in B \\
            (g, \gamma) &\mapsto \int_{t_0}^{t_f} g \circ \gamma dt
        \end{aligned}

    :param quadfun: Equations of motion on the symmetry space.
    :param tspan: Time interval to integrate over.
    :param gamma: Trajectory in quotient space :math:`B/Q`.
    :param args: Additional arguments needed by quadfun.
    :return: Value of the quads at :math:`t_f`.
    """

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
