import numpy as np
from scipy.integrate import solve_ivp, simps
import scipy.interpolate
import copy

from liepack.flow import RKMK, Flow
from liepack.domain.hspaces import HManifold
from liepack.domain.liegroups import RN
from liepack.domain.liealgebras import rn
from liepack import exp
from liepack.field import VectorField


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
        | quick_reconstruct      | False           |  bool              |
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
        obj.quick_reconstruct = kwargs.get('quick_reconstruct', False)
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
            if self.variable_step is True:
                int_sol = solve_ivp(lambda t, y: eom_func(y, *args), [tspan[0], tspan[-1]], y0,
                                    rtol=self.reltol, atol=self.abstol, max_step=self.maxstep, method=self.stepper)
            else:
                T = np.arange(tspan[0], tspan[-1], self.maxstep)
                if T[-1] != tspan[-1]:
                    T = np.hstack((T, tspan[-1]))
                int_sol = solve_ivp(lambda t, y: eom_func(y, *args), [tspan[0], tspan[-1]], y0,
                                    rtol=self.reltol, atol=self.abstol, method=self.stepper, t_eval=T)
            gamma = Trajectory(int_sol.t, int_sol.y.T)

        elif self.program == 'lie':
            dim = y0.shape[0]
            g = rn(dim+1)
            g.set_vector(y0)
            y = HManifold(RN(dim+1, exp(g)))
            vf = VectorField(y)
            vf.set_equationtype('general')

            def M2g(t, y):
                vec = y[:-1, -1]
                out = eom_func(vec, *args)
                g = rn(dim+1)
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
            gamma = Trajectory(ti, np.vstack([_[:-1, -1] for _ in yi]))  # Hardcoded assuming RN

        else:
            raise NotImplementedError

        if quad_func is not None and len(q0) is not 0:
            if self.quick_reconstruct:
                qf = integrate_quads(quad_func, tspan, gamma, *args)
                gamma.q = np.vstack((q0, np.zeros((len(gamma.t)-2, len(q0))), qf+q0))
            else:
                gamma = reconstruct(quad_func, gamma, q0, *args)

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

        if len(args) > 0 and isinstance(args[0], Trajectory):
            return args[0]

        obj.t = np.array([])
        obj.dual_t = np.array([])
        obj.y = np.array([])
        obj.dual = np.array([])
        obj.q = np.array([])
        obj.u = np.array([])
        obj.dual_u = np.array([])
        obj.dynamical_parameters = np.array([])
        obj.nondynamical_parameters = np.array([])
        obj.const = np.array([])
        obj.converged = False
        obj.cost = np.nan

        interpolation_type = kwargs.get('interpolation_type', 'linear').lower()
        obj.interpolation_type = interpolation_type

        arg_len = len(args)
        if arg_len >= 1:
            obj.t = args[0]

        if arg_len >= 2:
            obj.y = args[1]

        if arg_len >= 3:
            obj.q = args[2]

        if arg_len >= 4:
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
        y_val = np.array([])
        q_val = np.array([])
        u_val = np.array([])

        if len(self.t) == 0:
            return y_val, q_val, u_val

        ycolumn = False
        if len(self.y.shape) == 1:
            ydim = 1
        else:
            ycolumn = True
            ydim = self.y.shape[1]

        qcolumn = False
        if len(self.q.shape) == 1:
            if self.q.shape[0] == 0:
                qdim = 0
            else:
                qdim = 1
        else:
            qcolumn = True
            qdim = self.q.shape[1]

        ucolumn = False
        if len(self.u.shape) == 1:
            if self.u.shape[0] == 0:
                udim = 0
            else:
                udim = 1
        else:
            ucolumn = True
            udim = self.u.shape[1]

        # This builds the interpolation function on the most up to date data
        if ydim == 1:
            if ycolumn:
                f = self.interpolate(self.t, self.y.T[0])
            else:
                f = self.interpolate(self.t, self.y)

            if t.shape == ():
                y_val = np.array([f(t)])
            else:
                y_val = np.array(f(t))
            y_val = y_val.T

        else:
            f = [self.interpolate(self.t, self.y.T[ii]) for ii in range(ydim)]
            y_val = np.array([f[ii](t) for ii in range(ydim)]).T

        if qdim == 1:
            if qcolumn:
                f = self.interpolate(self.t, self.q.T[0])
            else:
                f = self.interpolate(self.t, self.q)
            if t.shape == ():
                q_val = np.array([f(t)])
            else:
                q_val = f(t)

            q_val = q_val.T

        else:
            f = [self.interpolate(self.t, self.q.T[ii]) for ii in range(qdim)]
            q_val = np.array([f[ii](t) for ii in range(qdim)]).T

        if udim == 1:
            if ucolumn:
                f = self.interpolate(self.t, self.u.T[0])
            else:
                f = self.interpolate(self.t, self.u)
            if t.shape == ():
                u_val = np.array([f(t)])
            else:
                u_val = f(t)

            u_val = u_val.T

        else:
            f = [self.interpolate(self.t, self.u.T[ii]) for ii in range(udim)]
            u_val = np.array([f[ii](t) for ii in range(udim)]).T

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
        t_val = np.array([])
        y_val = np.array([])
        q_val = np.array([])
        u_val = np.array([])
        if len(self.t) > 0:
            t_val = self.t[item]

        if len(self.y) > 0:
            y_val = self.y[item]

        if len(self.q) > 0:
            q_val = self.q[item]

        if len(self.u) > 0:
            u_val = self.u[item]

        return t_val, y_val, q_val, u_val

    def __len__(self):
        if self.t is None:
            return 0
        else:
            return len(self.t)


def reconstruct(quadfun, gamma, q0, *args):
    r"""
    Completely reconstructs a trajectory for all time in :math:`\gamma`.

    .. math::
        \begin{aligned}
            \text{reconstruct} : \gamma \in B/Q &\rightarrow \gamma \in B \\
            (g, \gamma) &\mapsto \int_{t_0}^{t} g \circ \gamma dt \; \forall \; t
        \end{aligned}

    :param quadfun: Equations of motion on the symmetry space.
    :param gamma: Trajectory in quotient space :math:`B/Q`.
    :param q0: Initial quad point.
    :param args: Additional arguments needed by quadfun.
    :return: :math:`\gamma` - Reconstructed trajectory in total space :math:`B`.
    """
    gamma = copy.copy(gamma)

    # gam_len = len(gamma)
    temp_q = np.zeros_like(q0)

    dq = np.array([quadfun(gamma(time)[0], *args) for time in gamma.t])

    # Integrate the quad func using numerical quadrature
    qf_m0 = np.vstack([temp_q] + [simps(dq[:ii+2].T, x=gamma.t[:ii+2]) for ii in range(len(gamma.t)-1)])

    # Add the initial state to get the final state.
    if len(q0) == 0:
        q0 = 0

    gamma.q = qf_m0 + q0
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

    t_len = len(gamma.t)
    x_set_temp = np.arange(0, t_len, 1)

    ind0 = int(np.ceil(np.interp(tspan[0], gamma.t, x_set_temp)))
    indf = int(np.ceil(np.interp(tspan[-1], gamma.t, x_set_temp)))

    if tspan[0] != gamma.t[ind0]:
        t_interp = np.array([tspan[0]])
    else:
        t_interp = np.array([])

    t_interp = np.hstack((t_interp, gamma.t[ind0:indf]))

    if tspan[-1] != gamma.t[indf-1]:
        t_interp = np.hstack((t_interp, tspan[-1]))

    y0, q0, u0 = gamma(t_interp[0])

    # Evaluate the quad function over every point in the given interval
    dq = np.array([quadfun(time, gamma(time)[0], *args) for time in t_interp])

    # Integrate the quad func using numerical quadrature
    qf_m0 = simps(dq.T, x=t_interp)

    # Add the initial state to get the final state.
    if len(q0) == 0:
        q0 = 0

    qf = qf_m0 + q0
    return qf
