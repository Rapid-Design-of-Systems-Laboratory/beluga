from beluga import LocalCompiler, jit_compile_func
from beluga.optimlib.special_functions import *
# from beluga.optimlib import rashs_mult
import sympy
from math import sin
from typing import Callable, Collection, Iterable, List

import numpy as np

# default_tol = 1e-4


class GenericParameter:
    def __init__(self, name: str, local_compiler: LocalCompiler = None):
        self.name = name
        self.local_compiler = local_compiler

        if not hasattr(self, 'sym'):
            self.sym = sympy.Symbol(self.name)

            if self.local_compiler is not None:
                self.local_compiler.add_symbolic_local(self.name, local=self.sym)

    def __repr__(self):
        return self.name

    @staticmethod
    def _ensure_list(item):
        if isinstance(item, Iterable):
            return list(item)
        else:
            return [item]

    def _sympify_internal(self, expr: str):
        if self.local_compiler is not None:
            return self.local_compiler.sympify(expr)
        else:
            return sympy.sympify(expr)

    def sympify(self):
        return self


class DimensionalParameter(GenericParameter):
    def __init__(self, name: str, units: str, local_compiler: LocalCompiler = None):
        super(DimensionalParameter, self).__init__(name, local_compiler=local_compiler)
        self.units = units

    def sympify(self):
        super(DimensionalParameter, self).sympify()
        self.units = self._sympify_internal(self.units)
        return self


class Constant(DimensionalParameter):
    def __init__(self, name: str, default_val: float, units: str, local_compiler: LocalCompiler = None):
        super(Constant, self).__init__(name, units, local_compiler=local_compiler)
        self.default_val = float(default_val)


class DynamicParameter(DimensionalParameter):
    def __init__(self, name: str, eom: str, units: str, local_compiler: LocalCompiler = None):
        super(DynamicParameter, self).__init__(name, units, local_compiler=local_compiler)
        self.eom = eom

    def sympify(self):
        super(DynamicParameter, self).sympify()
        self.eom = self._sympify_internal(self.eom)
        return self


class Expression(GenericParameter):
    def __init__(self, name: str, expr: str, local_compiler: LocalCompiler = None):
        super(Expression, self).__init__(name, local_compiler=local_compiler)
        self.expr = expr
        self.free_symbols = None

    def sympify(self):
        self.expr = self._sympify_internal(self.expr)
        self.free_symbols = self.expr.free_symbols
        return self


class CallableParameter(DimensionalParameter):
    def __init__(self, name: str, units: str, arg_units: Collection, dim_consistent=False, local_compiler=None):
        super(CallableParameter, self).__init__(name, units, local_compiler=local_compiler)

        self.dim_consistent = dim_consistent
        self.arg_units = arg_units
        self.num_args = len(self.arg_units)

    def sympify(self):
        super(CallableParameter, self).sympify()
        self.arg_units = self._sympify_internal(self.arg_units)


class Function(CallableParameter):
    def __init__(self, name: str, func: Callable, units: str, arg_units: Collection,
                 dim_consistent=False, local_compiler=None):

        self.num_args = len(arg_units)

        if not dim_consistent:
            raise NotImplementedError('Dimensionally inconsistant functions not yet implemented')
        else:
            self.func = jit_compile_func(func, self.num_args, array_inputs=False)
            self.sym = custom_functions.CustomFunctionGenerator(
                self.func, name=name, arg_len=self.num_args, local_compiler=local_compiler)

        super(Function, self).__init__(name, units, arg_units, dim_consistent=dim_consistent,
                                       local_compiler=local_compiler)


class Table(CallableParameter):
    def __init__(self, name: str, table_type: str, data, arg_data, units: str, arg_units: Collection,
                 dim_consistent=False, local_compiler=None):

        self.table_type = table_type
        self.data = np.array(data, dtype=np.float)
        self.arg_data = np.array(arg_data, dtype=np.float)
        self.dim_consistent = dim_consistent

        # TODO Add checks for size of data, arg_data consistent with type
        if self.table_type.lower() == '1d_spline':
            self.table = tables.TableSpline1D(name, self.data, self.arg_data)
        else:
            raise NotImplementedError('{} is not a implemented table type'.format(self.table_type))

        if not self.dim_consistent:
            raise NotImplementedError('Dimensionally inconsistant tables not yet implemented')
        else:
            self.sym = tables.SymTableGenerator(self.table, local_compiler=local_compiler)

        super(Table, self).__init__(name, units, arg_units, dim_consistent=dim_consistent,
                                    local_compiler=local_compiler)


# TODO Refine the switch class with metaclass like tables and custom functions
class Switch(GenericParameter):
    def __init__(self, name: str, functions: Collection, conditions: Collection, tol_param: str, local_compiler=None):
        super(Switch, self).__init__(name, local_compiler=local_compiler)
        self.functions = self._ensure_list(functions)
        self.conditions = self._ensure_list(conditions)
        self.tol_param = tol_param
        self.sym_func = None

    def sympify(self):
        super(Switch, self).sympify()

        self.functions = self._sympify_internal(self.functions)
        self.conditions = self._sympify_internal(self.conditions)
        self.tol_param = self._sympify_internal(self.tol_param)

        # Make switching function using RASHS
        self.sym_func = sympy.Integer(0)
        for function, conditions_for_function in zip(self.functions, self.conditions):
            rashs_mult = sympy.Integer(0)
            for condition in conditions_for_function:
                rashs_mult += 1/(1 + sympy.exp(-condition / self.tol_param))
            self.sym_func += rashs_mult*function

        return self


class Symmetry(DimensionalParameter):
    def __init__(self, name, field, units, remove=True, local_compiler=None):
        super(Symmetry, self).__init__(name, units, local_compiler=local_compiler)
        self.field = field
        self.remove = remove

    def sympify(self):
        super(Symmetry, self).sympify()
        self.field = self._sympify_internal(self.field)


# lc = LocalCompiler()
# p = DimensionalParameter('p', 'm', local_compiler=lc)
# k = Constant('k', 1., '1/s', local_compiler=lc)
# x = DynamicParameter('x', 'v', 'm', local_compiler=lc)
# quant = Expression('v', 'k*p', local_compiler=lc)
#
#
# def simple_func(y):
#     return sin(y)
#
#
# f = Function('f', simple_func, '1', ['1'], local_compiler=lc, dim_consistent=True)
# a = sympy.Symbol('a')
# fs = f.sym(a)
#
# tab_x = np.linspace(-1, 1, 100)
# tab_y = np.sin(tab_x)
#
# tab = Table('tab', '1d_spline', tab_y, tab_x, '1', ['1'], dim_consistent=True, local_compiler=lc)
#
# s = Switch('mass_flow', ['md0', 'md1'], [['mass - mass_0f'], ['mass_0f - mass']], 'stage_tol', local_compiler=lc)
#
# p.sympify(), k.sympify(), x.sympify(), quant.sympify(), f.sympify(), tab.sympify(), s.sympify()
