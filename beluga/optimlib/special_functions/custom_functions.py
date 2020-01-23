from sympy import Function
from sympy.core.function import ArgumentIndexError
from collections.abc import Iterable
import inspect
from beluga.utils.numerical_derivatives import gen_num_diff
from beluga.codegen.codegen import jit_compile_func
from numba import njit, float64, errors, targets
import logging


class CustomFunctionGenerator(object):
    def __init__(self, base_func, name=None, arg_len=None, func_dict=None, deriv_list=None, order=None,
                 num_deriv_type='c_diff'):

        if arg_len is None:
            self.arg_len = len(inspect.signature(base_func).parameters)
        else:
            self.arg_len = arg_len

        if order is None:
            self.order = tuple([0] * self.arg_len)
        else:
            self.order = order

        self.deriv_list = deriv_list
        self.func_dict = func_dict
        self.num_deriv_type = num_deriv_type

        if type(base_func) is targets.registry.CPUDispatcher:
            self.base_func = base_func
        else:
            self.base_func = jit_compile_func(base_func, self.arg_len, array_inputs=False)

        if name is None:
            self.name = 'Sym(' + self.base_func.__name__ + ')'
        else:
            self.name = name

    def __call__(self, *args):
        return CustomFunction(self.base_func, args, func_dict=self.func_dict, order=self.order,
                              deriv_method=self.num_deriv_type)

    def __repr__(self):
        return self.name


class CustomFunctionMeta(Function):
    def __new__(cls, base_func, arg_list):
        obj = super(CustomFunctionMeta, cls).__new__(cls, *arg_list)
        obj.nargs = (len(arg_list),)
        obj.arg_list = tuple(arg_list)
        if type(base_func) is targets.registry.CPUDispatcher:
            obj.base_func = base_func
        else:
            obj.base_func = jit_compile_func(base_func, len(arg_list), array_inputs=False)

        return obj

    @property
    def _diff_wrt(self):
        return True

    def fdiff(self, argindex=1):
        if argindex <= self.nargs[0]:
            order = list(self.order)
            order[argindex - 1] += 1
            return CustomFunction(self.base_func, self.arg_list, order=tuple(order), func_dict=self.func_dict)
        else:
            raise ArgumentIndexError(self, argindex)


class CustomFunction(Function):
    def __new__(cls, base_func, arg_list, func_dict=None, order=None, deriv_method='c_diff'):

        cls.check_args(arg_list, base_func)

        if order is None:
            order = ([0 for _ in range(len(arg_list))])

        name = cls.construct_name(base_func.__name__, arg_list, order)
        obj = type(name, (CustomFunctionMeta,), {})(base_func, arg_list)
        if sum(order) == 0:
            obj.eval_func = base_func
        else:
            obj.eval_func = gen_num_diff(base_func, order=order, method=deriv_method)
        obj.func_dict = func_dict
        if obj.func_dict is not None:
            if name not in obj.func_dict:
                obj.func_dict[name] = obj.eval_func
        obj.order = order
        return obj

    @staticmethod
    def check_args(arg_list, base_func):
        if not isinstance(arg_list, Iterable):
            arg_list = (arg_list,)
        if not len(arg_list) == len(inspect.signature(base_func).parameters):
            raise SyntaxError('Number of arguments not equal to number of arguments needed for function {}'
                              .format(base_func.__name__))

    @staticmethod
    def construct_name(func_name, arg_list, order):
        total_order = sum(order)

        post = '_'
        for arg_k, order_k in zip(arg_list, order):
            if order_k == 0:
                pass
            elif order_k == 1:
                post += 'd' + str(arg_k)
            else:
                post += 'd' + str(arg_k) + str(order_k)

        if total_order == 0:
            pre = ''
            post = ''
        elif total_order == 1:
            pre = 'd'
        else:
            pre = 'd' + str(total_order)

        return pre + func_name + post

