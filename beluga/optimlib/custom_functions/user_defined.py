import numpy as np
from sympy import Function
from sympy.core.function import ArgumentIndexError
from numba import njit, float64, errors
import logging


class CustomFunctionMeta(Function):
    def __new__(cls, cust_func, arg_list):
        obj = super(CustomFunctionMeta, cls).__new__(cls, arg_list)
        obj.nargs = (len(arg_list),)
        obj.order = [0 for _ in arg_list]
        obj.cust_func = cust_func
        obj.deriv_list = None
        obj.num_deriv_type = 'csd'
        return obj

    @property
    def _diff_wrt(self):
        return True

    def fdiff(self, argindex=1):
        if argindex == 1:
            return CustomFunction(self.table, self.args[0], order=self.order + 1)
        else:
            raise ArgumentIndexError(self, argindex)


class CustomFunction(CustomFunctionMeta):
    def __new__(cls, cust_func, arg, func_dict=None, order=None):
        name = cls.construct_name(str(table), str(arg), order)
        obj = type(name, (SymTableMeta,), {})(table, arg)
        obj.table_func = table.form_eval_function(order)
        if func_dict is not None:
            if name not in func_dict:
                func_dict[name] = obj.table_func
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


