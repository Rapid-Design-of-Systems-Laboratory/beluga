import numpy as np
import scipy.interpolate

import beluga

EMPTY_ARRAY = np.empty((0,))
EMPTY_ARRAY_2D = np.empty((0, 0))


class Trajectory:
    r"""
    Class containing information for a trajectory.

    .. math::
        \gamma(t) : I \subset \mathbb{R} \rightarrow B
    """
    def __init__(self,
                 t=EMPTY_ARRAY, y=EMPTY_ARRAY_2D, q=EMPTY_ARRAY_2D, u=EMPTY_ARRAY_2D, p=EMPTY_ARRAY, k=EMPTY_ARRAY,
                 lam_t=EMPTY_ARRAY, lam=EMPTY_ARRAY_2D, lam_u=EMPTY_ARRAY_2D, nu=EMPTY_ARRAY, aux=None,
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

        if len(self.t) == 0:
            return EMPTY_ARRAY_2D, EMPTY_ARRAY_2D, EMPTY_ARRAY_2D

        y_dim, q_dim, u_dim = self.y.shape[1], self.q.shape[1], self.u.shape[1]

        data_in = np.hstack([item for item in (self.y, self.q, self.u) if item.size > 0])

        data_out = self.interpolator(self.t, data_in)(t)

        # if len(data_out.shape) == 1:
        #     data_out = data_out[np.newaxis, :]

        y_val = data_out[..., :y_dim]
        q_val = data_out[..., y_dim:(y_dim + q_dim)]
        u_val = data_out[..., (y_dim + q_dim):(y_dim + q_dim + u_dim)]

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

            def _interpolator(_t, _y):
                return scipy.interpolate.interp1d(_t, _y, kind=func, axis=0, assume_sorted=True)

            self.interpolator = _interpolator
