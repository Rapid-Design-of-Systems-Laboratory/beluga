import time
from typing import Collection

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
                 lam_t=EMPTY_ARRAY, lam=EMPTY_ARRAY_2D, lam_u=EMPTY_ARRAY_2D, nu=EMPTY_ARRAY, cost=np.nan, aux=None,
                 interpolation_type='linear'):

        self.t = np.array(t)
        self.y = np.array(y)
        self.q = np.array(q)
        self.u = np.array(u)
        self.p = np.array(p)
        self.k = np.array(k)

        self.lam_t = np.array(lam_t)
        self.lam = np.array(lam)
        self.lam_u = np.array(lam_u)
        self.nu = np.array(nu)

        self.cost = cost

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

    def form_data_dict(self, use_arrays: bool = True, include_aux: bool = True) -> dict:
        # TODO Maybe automate this instead of hardcoding values
        items_to_export = ['t', 'y', 'q', 'u', 'p', 'k', 'lam_t', 'lam', 'lam_u', 'nu', 'cost']

        data = dict()
        for key in items_to_export:
            val = getattr(self, key)

            if isinstance(val, np.ndarray):
                if val.size == 0:
                    continue
                elif not use_arrays:
                    val = val.tolist()

            data[key] = val

        if include_aux:
            if not use_arrays:
                for key, val in self.aux.items():
                    if isinstance(val, np.ndarray):
                        self.aux[key] = val.tolist()

            data['aux'] = self.aux

        return data

    def save(self, file_name: str = None, file_format: str = 'json'):
        if file_name is None:
            file_name = time.strftime('sol_%m%d%y%H%m%S')

        if file_format == 'json':
            import json

            with open(file_name + '.json', 'w') as file:
                json.dump(self.form_data_dict(use_arrays=False), file, indent=4)

        elif file_format == 'csv':
            raise NotImplementedError('CSV format not yet implemented.')
            # import os
            # import csv
            #
            # if not os.path.exists(file_name):
            #     os.mkdir(file_name)
            #
            # for key, data in self.form_data_dict(use_arrays=False, include_aux=False).items():
            #     with open('{0}/{0}_{1}.csv'.format(file_name, key), 'w') as file:
            #         csv_writer = csv.writer(file)
            #         csv_writer.writerows(data)

        elif file_format == 'npz':
            np.savez(file_name, **self.form_data_dict())

        elif file_format == 'mat':
            from scipy.io import savemat
            savemat(file_name + '.mat', self.form_data_dict())

        else:
            raise NotImplementedError('Export format {} not implemented'.format(file_format))
