import numpy as np
import scipy.interpolate

import beluga


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

        obj.aux = dict()

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

        t = np.array(t, dtype=beluga.DTYPE)
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

        :param func: FunctionComponent for interpolation or a string for SciPy's interp1d(kind=func).
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
