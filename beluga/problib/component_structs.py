from beluga import LocalCompiler
from beluga.optimlib.special_functions import *
import sympy
from typing import Union, Callable, Collection, Iterable

import numpy as np

# default_tol = 1e-4
sym_zero = sympy.Integer(0)
sym_one = sympy.Integer(1)


class GenericStruct:
    def __init__(self, local_compiler: LocalCompiler = None):
        if not(hasattr(self, 'local_compiler') and local_compiler is None):
            self.local_compiler = local_compiler

    @staticmethod
    def _ensure_list(item):
        if isinstance(item, Iterable):
            return list(item)
        else:
            return [item]

    def _sympify_internal(self, expr: Union[str, Iterable]) -> sympy.Basic:
        if self.local_compiler is not None:
            return self.local_compiler.sympify(expr)
        else:
            return sympy.sympify(expr)

    def sympify_self(self):
        return self

    def subs_self(self, old, new):
        return self


class NamedStruct(GenericStruct):
    def __init__(self, name: str, local_compiler: LocalCompiler = None):
        # super(NamedParameter, self).__init__(local_compiler=local_compiler)
        GenericStruct.__init__(self, local_compiler=local_compiler)
        self.name = name

        if not hasattr(self, 'sym'):
            self.sym = sympy.Symbol(self.name)

            if self.local_compiler is not None:
                self.local_compiler.add_symbolic_local(self.name, local=self.sym)

    def __repr__(self):
        return self.name


class DimensionalStruct(GenericStruct):
    def __init__(self, units: str, local_compiler: LocalCompiler = None):
        GenericStruct.__init__(self, local_compiler=local_compiler)
        self.units = units

    def sympify_self(self):
        GenericStruct.sympify_self(self)
        self.units = self._sympify_internal(self.units)
        return self


class NamedDimensionalStruct(NamedStruct, DimensionalStruct):
    def __init__(self, name: str, units: Union[str, sympy.Basic], local_compiler: LocalCompiler = None):
        NamedStruct.__init__(self, name, local_compiler=local_compiler)
        DimensionalStruct.__init__(self, units)

    def sympify_self(self):
        NamedStruct.sympify_self(self)
        DimensionalStruct.sympify_self(self)
        return self


class Constant(NamedDimensionalStruct):
    def __init__(self, name: str, default_val: float, units: str, local_compiler: LocalCompiler = None):
        super(Constant, self).__init__(name, units, local_compiler=local_compiler)
        self.default_val = float(default_val)


class DynamicStruct(NamedDimensionalStruct):
    def __init__(self, name: str, eom: str, units: str, local_compiler: LocalCompiler = None):
        super(DynamicStruct, self).__init__(name, units, local_compiler=local_compiler)
        self.eom = eom

    def sympify_self(self):
        super(DynamicStruct, self).sympify_self()
        self.eom = self._sympify_internal(self.eom)
        return self

    def subs_self(self, old, new):
        if not hasattr(self.eom, 'subs_self'):
            self.sympify_self()
        self.eom = self.eom.subs(old, new)


class ExpressionStruct(GenericStruct):
    def __init__(self, expr: str, local_compiler: LocalCompiler = None):
        GenericStruct.__init__(self, local_compiler=local_compiler)
        self.expr = expr
        self.free_symbols = None

    def sympify_self(self):
        super(ExpressionStruct, self).sympify_self()
        self.expr = self._sympify_internal(self.expr)
        self.free_symbols = self.expr.free_symbols
        return self

    def __repr__(self):
        return self.expr.__repr__()

    def subs_self(self, old, new):
        if not hasattr(self.expr, 'subs_self'):
            self.sympify_self()
        self.expr = self.expr.subs(old, new)


class NamedExpressionStruct(NamedStruct, ExpressionStruct):
    def __init__(self, name: str, expr: str, local_compiler: LocalCompiler = None):
        NamedStruct.__init__(self, name, local_compiler=local_compiler)
        ExpressionStruct.__init__(self, expr)

    def sympify_self(self):
        NamedStruct.sympify_self(self)
        ExpressionStruct.sympify_self(self)
        return self


class DimensionalExpressionStruct(ExpressionStruct, DimensionalStruct):
    def __init__(self, expr: str, units: str, local_compiler: LocalCompiler = None):
        DimensionalStruct.__init__(self, units, local_compiler=local_compiler)
        ExpressionStruct.__init__(self, expr)

    def sympify_self(self):
        DimensionalStruct.sympify_self(self)
        ExpressionStruct.sympify_self(self)
        return self


class NamedDimensionalExpressionStruct(NamedStruct, DimensionalStruct, ExpressionStruct):
    def __init__(self, name: str, expr: str, units: str, local_compiler: LocalCompiler = None):
        NamedStruct.__init__(self, name, local_compiler=local_compiler)
        DimensionalStruct.__init__(self, units)
        ExpressionStruct.__init__(self, expr)

    def sympify_self(self):
        NamedStruct.sympify_self(self)
        DimensionalStruct.sympify_self(self)
        ExpressionStruct.sympify_self(self)
        return self


class CostStruct(DimensionalStruct):
    def __init__(self, initial: str = sym_zero, path: str = sym_zero, terminal: str = sym_zero, units: str = sym_one,
                 local_compiler: LocalCompiler = None):
        super(CostStruct, self).__init__(units, local_compiler=local_compiler)
        self.initial = initial
        self.path = path
        self.terminal = terminal

    def sympify_self(self):
        super(CostStruct, self).sympify_self()
        self.initial = self._sympify_internal(self.initial)
        self.path = self._sympify_internal(self.path)
        self.terminal = self._sympify_internal(self.terminal)

    def subs_self(self, old, new):
        if not (hasattr(self.initial, 'subs_self') and hasattr(self.path, 'subs_self') and hasattr(self.terminal, 'subs_self')):
            self.sympify_self()
        self.initial = self.initial.subs(old, new)
        self.path = self.path.subs(old, new)
        self.terminal = self.terminal.subs(old, new)


class CallableStruct(NamedDimensionalStruct):
    def __init__(self, name: str, units: str, arg_units: Collection, dim_consistent=False, local_compiler=None):
        super(CallableStruct, self).__init__(name, units, local_compiler=local_compiler)

        self.dim_consistent = dim_consistent
        self.arg_units = arg_units
        self.num_args = len(self.arg_units)

    def sympify_self(self):
        super(CallableStruct, self).sympify_self()
        self.arg_units = self._sympify_internal(self.arg_units)


class FunctionStruct(CallableStruct):
    def __init__(self, name: str, func: Callable, units: str, arg_units: Collection,
                 dim_consistent=False, local_compiler=None):

        self.num_args = len(arg_units)

        if not dim_consistent:
            raise NotImplementedError('Dimensionally inconsistant functions not yet implemented')
        else:
            self.func = jit_compile_func(func, self.num_args, array_inputs=False)
            self.sym = custom_functions.CustomFunctionGenerator(
                self.func, name=name, arg_len=self.num_args, local_compiler=local_compiler)

        super(FunctionStruct, self).__init__(name, units, arg_units, dim_consistent=dim_consistent,
                                             local_compiler=local_compiler)


class TableStruct(CallableStruct):
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

        super(TableStruct, self).__init__(name, units, arg_units, dim_consistent=dim_consistent,
                                          local_compiler=local_compiler)


# TODO Refine the switch class with metaclass like tables and custom functions
class SwitchStruct(NamedStruct):
    def __init__(self, name: str, functions: Collection, conditions: Collection, tol_param: str, local_compiler=None):
        super(SwitchStruct, self).__init__(name, local_compiler=local_compiler)
        self.functions = self._ensure_list(functions)
        self.conditions = self._ensure_list(conditions)
        self.tol_param = tol_param
        self.sym_func = None

    def sympify_self(self):
        super(SwitchStruct, self).sympify_self()

        self.functions = self._sympify_internal(self.functions)
        self.conditions = self._sympify_internal(self.conditions)
        self.tol_param = self._sympify_internal(self.tol_param)

        # Make switching function using RASHS
        self.sym_func = sympy.Integer(0)
        for function, conditions_for_function in zip(self.functions, self.conditions):
            rashs_mult = sympy.Integer(0)
            for condition in conditions_for_function:
                rashs_mult += 1/(1 + sympy.exp(condition / self.tol_param))
            self.sym_func += rashs_mult*function

        return self

    def subs_self(self, old, new):
        if self.sym_func is None:
            self.sympify_self()
        self.sym_func = self.sym_func.subs(old, new)


class SymmetryStruct(DimensionalStruct):
    def __init__(self, field: Iterable[str], units, remove=True, local_compiler=None):
        super(SymmetryStruct, self).__init__(units, local_compiler=local_compiler)
        self.field = field
        self.remove = remove

    def sympify_self(self):
        super(SymmetryStruct, self).sympify_self()
        self.field = self._sympify_internal(np.array(self.field))

    def subs_self(self, old, new):
        if not hasattr(self.field, 'subs_self'):
            self.sympify_self()
        self.field = self.field.subs(old, new)


class PathConstraintStruct(DimensionalExpressionStruct):
    def __init__(self, expr: str, units: str, lower: str, upper: str, activator: str, method: str = 'utm',
                 local_compiler: LocalCompiler = None):
        super(PathConstraintStruct, self).__init__(expr, units, local_compiler=local_compiler)
        self.lower = lower
        self.upper = upper
        self.activator = activator
        self.method = method

    def sympify_self(self):
        super(PathConstraintStruct, self).sympify_self()
        self.lower = self._sympify_internal(self.lower)
        self.upper = self._sympify_internal(self.upper)
        self.activator = self._sympify_internal(self.activator)

    def subs_self(self, old, new):
        if not (hasattr(self.expr, 'subs_self') and hasattr(self.lower, 'subs_self') and hasattr(self.upper, 'subs_self')):
            self.sympify_self()
        self.expr = self.expr.subs(old, new)
        self.lower = self.lower.subs(old, new)
        self.upper = self.upper.subs(old, new)


lc = LocalCompiler()
p = NamedDimensionalStruct('p', 'm', local_compiler=lc)
k = Constant('k', 1., '1/s', local_compiler=lc)
x = DynamicStruct('x', 'v', 'm', local_compiler=lc)
quant = NamedExpressionStruct('v', 'k*p', local_compiler=lc)


def simple_func(y):
    return y**3


f = FunctionStruct('f', simple_func, '1', ['1'], local_compiler=lc, dim_consistent=True)
a = sympy.Symbol('a')
fs = f.sym(a)

tab_x = np.linspace(-1, 1, 100)
tab_y = np.sin(tab_x)

tab = TableStruct('tab', '1d_spline', tab_y, tab_x, '1', ['1'], dim_consistent=True, local_compiler=lc)

s = SwitchStruct('mass_flow', ['md0', 'md1'], [['mass - mass_0f'], ['mass_0f - mass']], 'stage_tol',
                 local_compiler=lc)

p.sympify_self(), k.sympify_self(), x.sympify_self(), quant.sympify_self(), f.sympify_self(), tab.sympify_self(),
s.sympify_self()
