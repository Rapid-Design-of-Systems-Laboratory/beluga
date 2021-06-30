import copy

import numpy as np
from liepack import exp
from liepack.domain.hspaces import HManifold
from liepack.domain.liealgebras import rn
from liepack.domain.liegroups import RN
from liepack.field import VectorField
from liepack.flow import RKMK, Flow
from scipy.integrate import solve_ivp, simps

import beluga
from beluga.data_classes.trajectory import Trajectory


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

        :param eom_func: FunctionComponent representing the equations of motion.
        :param quad_func: FunctionComponent representing the quadratures.
        :param tspan: Independent time interval.
        :param y0: Initial state position.
        :param q0: Initial quad position.
        :param args: Additional arguments required by EOM files.
        :param kwargs: Unused.
        :return: A full reconstructed trajectory, :math:`\gamma`.
        """
        y0 = np.array(y0, dtype=beluga.DTYPE)

        if self.program == 'scipy':
            if self.variable_step is True:
                int_sol = solve_ivp(lambda t, _y: eom_func(_y, *args), [tspan[0], tspan[-1]], y0,
                                    rtol=self.reltol, atol=self.abstol, max_step=self.maxstep, method=self.stepper)
            else:
                ti = np.arange(tspan[0], tspan[-1], self.maxstep)
                if ti[-1] != tspan[-1]:
                    ti = np.hstack((ti, tspan[-1]))
                int_sol = solve_ivp(lambda t, _y: eom_func(_y, *args), [tspan[0], tspan[-1]], y0,
                                    rtol=self.reltol, atol=self.abstol, method=self.stepper, t_eval=ti)
            gamma = Trajectory(t=int_sol.t, y=int_sol.y.T)

        elif self.program == 'lie':
            dim = y0.shape[0]
            g = rn(dim+1)
            g.set_vector(y0)
            y = HManifold(RN(dim+1, exp(g)))
            vf = VectorField(y)
            vf.set_equationtype('general')

            def m2g(_, _y):
                vec = _y[:-1, -1]
                out = eom_func(vec, *args)
                _g = rn(dim+1)
                _g.set_vector(out)
                return _g

            vf.set_M2g(m2g)
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

        if quad_func is not None and len(q0) != 0:
            if self.quick_reconstruct:
                qf = integrate_quads(quad_func, tspan, gamma, *args)
                gamma.q = np.vstack((q0, np.zeros((len(gamma.t)-2, len(q0))), qf+q0))
            else:
                gamma = reconstruct(quad_func, gamma, q0, *args)

        return gamma


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

    dq = np.array([quadfun(gamma_i[1], *args) for gamma_i in gamma])

    # Integrate the quad func using compilation quadrature
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

    # Integrate the quad func using compilation quadrature
    qf_m0 = simps(dq.T, x=t_interp)

    # Add the initial state to get the final state.
    if len(q0) == 0:
        q0 = 0

    qf = qf_m0 + q0
    return qf
