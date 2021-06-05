import inspect
from collections.abc import Iterable

from numba.core.registry import CPUDispatcher
from sympy import Function
from sympy.core.function import ArgumentIndexError

from beluga.compilation import jit_compile_func
from beluga.compilation.compiler import add_function_local
from beluga.utils.numerical_derivatives import gen_num_diff


class CustomFunctionGenerator(object):
    def __init__(self, base_func, name=None, arg_types=None, deriv_list=None, order=None,
                 num_deriv_type='c_diff'):

        if arg_types is None:
            self.arg_types = ['scalar' for _ in inspect.signature(base_func).parameters]
        else:
            self.arg_types = arg_types

        if order is None:
            self.order = tuple([0] * len(self.arg_types))
        else:
            self.order = order

        self.deriv_list = deriv_list
        self.num_deriv_type = num_deriv_type

        if type(base_func) is CPUDispatcher:
            self.base_func = base_func
        else:
            self.base_func = jit_compile_func(base_func, self.arg_types, complex_numbers=False)

        if name is None:
            self.name = 'Sym(' + self.base_func.__name__ + ')'
        else:
            self.name = name

    def __call__(self, *args):
        return CustomFunction(self.name, self.base_func, args, order=self.order, deriv_method=self.num_deriv_type)

    def __repr__(self):
        return self.name


class CustomFunctionMeta(Function):
    def __new__(cls, base_name, base_func, arg_list):
        obj = super(CustomFunctionMeta, cls).__new__(cls, *arg_list)
        obj.nargs = (len(arg_list),)
        obj.arg_list = tuple(arg_list)
        obj.base_name = base_name
        if type(base_func) is CPUDispatcher:
            obj.base_func = base_func
        else:
            obj.base_func = jit_compile_func(base_func, arg_list)

        return obj

    def __deepcopy__(self, memodict=None):
        return self

    @property
    def _diff_wrt(self):
        return True

    def fdiff(self, argindex=1):
        if argindex <= self.nargs[0]:
            order = list(self.order)
            order[argindex - 1] += 1
            return CustomFunction(self.base_name, self.base_func, self.arg_list, order=tuple(order))
        else:
            raise ArgumentIndexError(self, argindex)


class CustomFunction(Function):
    def __new__(cls, base_name, base_func, arg_list, order=None, deriv_method='c_diff'):

        cls.check_args(arg_list, base_func)

        if order is None:
            order = ([0 for _ in range(len(arg_list))])

        name = cls.construct_name(base_name, arg_list, order)
        obj = type(name, (CustomFunctionMeta,), {})(name, base_func, arg_list)
        if sum(order) == 0:
            obj.eval_func = base_func
        else:
            obj.eval_func = gen_num_diff(base_func, order=order, method=deriv_method)

        add_function_local(name, obj.eval_func)
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

