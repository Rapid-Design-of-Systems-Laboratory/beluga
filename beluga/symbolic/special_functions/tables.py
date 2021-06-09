import logging

import numpy as np
from numba import njit, float64, errors
from sympy import Function
from sympy.core.function import ArgumentIndexError

from beluga.compilation.compiler import add_function_local


# TODO Extend to N-dim tables
class SymTableGenerator(object):
    def __init__(self, table, order=None):

        self.table = table

        if order is None:
            self.order = 0
        else:
            self.order = order

    def __call__(self, *args):
        return SymTable(self.table, *args, order=self.order)


class SymTableMeta(Function):
    def __new__(cls, table, arg):
        obj = super(SymTableMeta, cls).__new__(cls, arg)
        obj.nargs = (1,)
        obj.order = 0
        obj.table = table
        return obj

    @property
    def _diff_wrt(self):
        return True

    def fdiff(self, argindex=1):
        if argindex == 1:
            return SymTable(self.table, self.args[0], order=self.order + 1)
        else:
            raise ArgumentIndexError(self, argindex)

    def __deepcopy__(self, memodict=None):
        return self


class SymTable(SymTableMeta):
    def __new__(cls, table, arg, order=0):
        name = cls.construct_name(str(table), str(arg), order)
        obj = type(name, (SymTableMeta,), {})(table, arg)
        obj.table_func = table.form_eval_function(order)

        add_function_local(name, obj.table_func)

        obj.order = order
        return obj

    @staticmethod
    def construct_name(table_name, arg_name, order):
        if order == 0:
            pre = ''
            post = ''
        elif order == 1:
            pre = 'd'
            post = '_d' + arg_name
        else:
            pre = 'd' + str(order)
            post = '_d' + arg_name + str(order)
        return pre + table_name + post


class TableSpline1D(object):
    def __init__(self, name, data_y, data_x):

        self.name = name
        self.data_x = data_x
        self.data_y = data_y

        h = self.data_x[1:] - self.data_x[:-1]
        b = (self.data_y[1:] - self.data_y[:-1])/h
        v = 2*(h[:-1] + h[1:])
        u = 6*(b[1:] - b[:-1])

        mat_coeff = np.diag(v) + np.diag(h[1:-1], k=1) + np.diag(h[1:-1], k=-1)
        z = np.linalg.solve(mat_coeff, u)
        z = np.concatenate((np.array([0]), z, np.array([0])))

        self.coeff = np.array([[z[i+1]/(6*h[i]), z[i]/(6*h[i]), data_y[i+1]/h[i] - z[i+1]*h[i]/6,
                                data_y[i]/h[i] - z[i]*h[i]/6] for i in range(0, len(z)-1)])

        self.interp = self.form_eval_function(0)

    def __call__(self, x):
        return self.interp(x)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def form_eval_function(self, order):
        data_x = self.data_x
        coeff_set = self.coeff

        if order == 0:
            def interp(x):
                i = np.searchsorted(data_x, x, side='right')
                coeff = coeff_set[i - 1]
                t0 = data_x[i - 1]
                t1 = data_x[i]
                return coeff[0] * (x - t0) ** 3 + coeff[1] * (t1 - x) ** 3 + coeff[2] * (x - t0) + coeff[3] * (t1 - x)

        elif order == 1:
            def interp(x):
                i = np.searchsorted(data_x, x, side='right')
                coeff = coeff_set[i - 1]
                t0 = data_x[i - 1]
                t1 = data_x[i]
                return 3*(coeff[0]*(x - t0)**2 - coeff[1] * (t1 - x)**2) + coeff[2] - coeff[3]

        elif order == 2:
            def interp(x):
                i = np.searchsorted(data_x, x, side='right')
                coeff = coeff_set[i - 1]
                t0 = data_x[i - 1]
                t1 = data_x[i]
                return 6*(coeff[0]*(x - t0) + coeff[1] * (t1 - x))

        elif order == 3:
            def interp(x):
                i = np.searchsorted(data_x, x, side='right')
                coeff = coeff_set[i - 1]
                return 6*(coeff[0] - coeff[1])

        else:
            def interp(_):
                return 0.

        try:
            jit_interp = njit(float64(float64,))(interp)
            return jit_interp

        except errors.NumbaError as e:
            logging.debug(e)
            logging.debug('Cannot Compile FunctionComponent TableComponent')
            return interp
