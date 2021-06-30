import numpy as np
import scipy.interpolate

import beluga

EMPTY_ARRAY = np.array([])


class Trajectory:
    r"""
    Class containing information for a trajectory.

    .. math::
        \gamma(t) : I \subset \mathbb{R} \rightarrow B
    """
    def __init__(self, t=EMPTY_ARRAY, y=EMPTY_ARRAY, q=EMPTY_ARRAY, u=EMPTY_ARRAY, p=EMPTY_ARRAY, k=EMPTY_ARRAY,
                 lam_t=EMPTY_ARRAY, lam=EMPTY_ARRAY, lam_u=EMPTY_ARRAY, nu=EMPTY_ARRAY, aux=None,
                 interpolation_type='linear'):

        self.t = t
        self.y = y
        self.q = q
        self.u = u
        self.p = p
        self.k = k

        self.lam_t = lam_t
        self.lam = lam
        self.lam_u = lam_u
        self.nu = nu

        self.cost = np.nan

        self.converged = False

        if aux is None:
            self.aux = dict()
        else:
            self.aux = aux

        self.interpolation_type = interpolation_type
        self.interpolator = None
        self.set_interpolate_function(self.interpolation_type)

    def __getitem__(self, item):

        out = []
        for arr in [self.t, self.y, self.q, self.u]:
            if len(arr) > 0:
                out.append(arr[item])
            else:
                out.append(EMPTY_ARRAY)

        return tuple(out)

    def __len__(self):
        if self.t is None:
            return 0
        else:
            return len(self.t)

    def interpolate(self, t):
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
                f = self.interpolator(self.t, self.y.T[0])
            else:
                f = self.interpolator(self.t, self.y)

            if t.shape == ():
                y_val = np.array([f(t)])
            else:
                y_val = np.array(f(t))
            y_val = y_val.T

        else:
            f = [self.interpolator(self.t, self.y.T[ii]) for ii in range(ydim)]
            y_val = np.array([f[ii](t) for ii in range(ydim)]).T

        if qdim == 1:
            if qcolumn:
                f = self.interpolator(self.t, self.q.T[0])
            else:
                f = self.interpolator(self.t, self.q)
            if t.shape == ():
                q_val = np.array([f(t)])
            else:
                q_val = f(t)

            q_val = q_val.T

        else:
            f = [self.interpolator(self.t, self.q.T[ii]) for ii in range(qdim)]
            q_val = np.array([f[ii](t) for ii in range(qdim)]).T

        if udim == 1:
            if ucolumn:
                f = self.interpolator(self.t, self.u.T[0])
            else:
                f = self.interpolator(self.t, self.u)
            if t.shape == ():
                u_val = np.array([f(t)])
            else:
                u_val = f(t)

            u_val = u_val.T

        else:
            f = [self.interpolator(self.t, self.u.T[ii]) for ii in range(udim)]
            u_val = np.array([f[ii](t) for ii in range(udim)]).T

        return y_val, q_val, u_val

    def set_interpolate_function(self, func):
        """
        Sets the function used for interpolation.

        :param func: FunctionComponent for interpolation or a string for SciPy's interp1d(kind=func).
        """
        if callable(func):
            self.interpolator = func
        elif isinstance(func, str):
            func = func.lower()
            self.interpolator = lambda t, y: scipy.interpolate.interp1d(t, y, kind=func)
