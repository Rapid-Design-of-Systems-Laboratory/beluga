import numpy as np
import sympy

from typing import Union, Callable, Collection, List, Iterable


from beluga.compilation.compiler import sympify, jit_compile_func, add_symbolic_local, add_function_local
from beluga.symbolic_manipulation.special_functions import custom_functions, tables

# default_tol = 1e-4
sym_zero = sympy.Integer(0)
sym_one = sympy.Integer(1)


class GenericStruct:
    def __init__(self):
        pass

    @staticmethod
    def _ensure_list(item):
        if isinstance(item, Iterable):
            return list(item)
        else:
            return [item]

    def sympify_self(self):
        return self

    def subs_self(self, old, new):
        return self


class NamedStruct(GenericStruct):
    def __init__(self, name: str):
        # super(NamedParameter, self).__init__(local_compiler=local_compiler)
        GenericStruct.__init__(self)
        self.name = name

        if not hasattr(self, 'sym'):
            self.sym = sympy.Symbol(self.name)

            add_symbolic_local(self.name, local=self.sym)

    def __repr__(self):
        return self.name


class DimensionalStruct(GenericStruct):
    def __init__(self, units: str):
        GenericStruct.__init__(self)
        self.units = units

    def sympify_self(self):
        GenericStruct.sympify_self(self)
        self.units = sympify(self.units)
        return self


class NamedDimensionalStruct(NamedStruct, DimensionalStruct):
    def __init__(self, name: str, units: Union[str, sympy.Basic]):
        NamedStruct.__init__(self, name)
        DimensionalStruct.__init__(self, units)

    def sympify_self(self):
        NamedStruct.sympify_self(self)
        DimensionalStruct.sympify_self(self)
        return self


class Constant(NamedDimensionalStruct):
    def __init__(self, name: str, default_val: float, units: str):
        super(Constant, self).__init__(name, units)
        self.default_val = float(default_val)


class DynamicStruct(NamedDimensionalStruct):
    def __init__(self, name: str, eom: str, units: str):
        super(DynamicStruct, self).__init__(name, units)
        self.eom = eom

    def sympify_self(self):
        super(DynamicStruct, self).sympify_self()
        self.eom = sympify(self.eom)
        return self

    def subs_self(self, old, new):
        if not hasattr(self.eom, 'subs_self'):
            self.sympify_self()
        self.eom = self.eom.subs(old, new)


class ExpressionStruct(GenericStruct):
    def __init__(self, expr: str):
        GenericStruct.__init__(self)
        self.expr = expr
        self.free_symbols = None

    def sympify_self(self):
        super(ExpressionStruct, self).sympify_self()
        self.expr = sympify(self.expr)
        self.free_symbols = self.expr.free_symbols
        return self

    def __repr__(self):
        return self.expr.__repr__()

    def subs_self(self, old, new):
        if not hasattr(self.expr, 'subs_self'):
            self.sympify_self()
        self.expr = self.expr.subs(old, new)


class NamedExpressionStruct(NamedStruct, ExpressionStruct):
    def __init__(self, name: str, expr: str):
        NamedStruct.__init__(self, name)
        ExpressionStruct.__init__(self, expr)

    def sympify_self(self):
        NamedStruct.sympify_self(self)
        ExpressionStruct.sympify_self(self)
        return self


class DimensionalExpressionStruct(ExpressionStruct, DimensionalStruct):
    def __init__(self, expr: str, units: str):
        DimensionalStruct.__init__(self, units)
        ExpressionStruct.__init__(self, expr)

    def sympify_self(self):
        DimensionalStruct.sympify_self(self)
        ExpressionStruct.sympify_self(self)
        return self


class NamedDimensionalExpressionStruct(NamedStruct, DimensionalStruct, ExpressionStruct):
    def __init__(self, name: str, expr: str, units: str):
        NamedStruct.__init__(self, name, )
        DimensionalStruct.__init__(self, units)
        ExpressionStruct.__init__(self, expr)

    def sympify_self(self):
        NamedStruct.sympify_self(self)
        DimensionalStruct.sympify_self(self)
        ExpressionStruct.sympify_self(self)
        return self


class CostStruct(DimensionalStruct):
    def __init__(self, initial: str = sym_zero, path: str = sym_zero, terminal: str = sym_zero,
                 units: Union[str, sympy.Basic] = None, path_units: Union[str, sympy.Basic] = None):
        super(CostStruct, self).__init__(units, )
        self.initial = initial
        self.path = path
        self.terminal = terminal
        self.path_units = path_units

    def sympify_self(self):
        super(CostStruct, self).sympify_self()
        self.initial = sympify(self.initial)
        self.path = sympify(self.path)
        self.terminal = sympify(self.terminal)
        self.path_units = sympify(self.path_units)

    def subs_self(self, old, new):
        if not (hasattr(self.initial, 'subs_self') and hasattr(self.path, 'subs_self')
                and hasattr(self.terminal, 'subs_self')):
            self.sympify_self()
        self.initial = self.initial.subs(old, new)
        self.path = self.path.subs(old, new)
        self.terminal = self.terminal.subs(old, new)

    # noinspection PyUnresolvedReferences
    def check_path_units(self, independent_units):
        independent_units = sympify(independent_units)
        self.sympify_self()

        if self.units is None and self.path_units is None:
            return self
        elif self.units is None:
            self.units = self.path_units * independent_units
        elif self.path_units is None:
            self.path_units = self.units / independent_units
        elif self.units != self.path_units * independent_units:
            self.path_units = self.units / independent_units
            raise RuntimeWarning('Path cost units do not match boundary cost units: Defaulting to boundary cost units')

        return self


class CallableStruct(NamedDimensionalStruct):
    def __init__(self, name: str, units: str, arg_units: Collection, dim_consistent=False):
        super(CallableStruct, self).__init__(name, units, )

        self.dim_consistent = dim_consistent
        self.arg_units = arg_units
        self.num_args = len(self.arg_units)

    def sympify_self(self):
        super(CallableStruct, self).sympify_self()
        self.arg_units = sympify(self.arg_units)


class FunctionStruct(CallableStruct):
    def __init__(self, name: str, func: Callable, units: str, arg_units: Collection,
                 dim_consistent=False):

        self.arg_types = ['scalar' for _ in arg_units]

        if not dim_consistent:
            raise NotImplementedError('Dimensionally inconsistant functions not yet implemented')
        else:
            self.func = jit_compile_func(func, self.arg_types)
            self.sym = custom_functions.CustomFunctionGenerator(
                self.func, name=name, arg_types=self.arg_types, )

        add_symbolic_local(name, self.sym)
        # local_compiler.add_function_local(name, self.func)

        super(FunctionStruct, self).__init__(name, units, arg_units, dim_consistent=dim_consistent)


class TableStruct(CallableStruct):
    def __init__(self, name: str, table_type: str, data, arg_data, units: str, arg_units: Collection,
                 dim_consistent=False):

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
            self.sym = tables.SymTableGenerator(self.table, )

        add_symbolic_local(name, self.sym)
        # local_compiler.add_function_local(name, self.table)

        super(TableStruct, self).__init__(name, units, arg_units, dim_consistent=dim_consistent)


# TODO Refine the switch class with metaclass like tables and custom functions
class SwitchStruct(NamedStruct):
    def __init__(self, name: str, functions: Collection, conditions: Collection, tol_param: str):
        super(SwitchStruct, self).__init__(name, )
        self.functions = self._ensure_list(functions)
        self.conditions = self._ensure_list(conditions)
        self.tol_param = tol_param
        self.sym_func = None

    def sympify_self(self):
        super(SwitchStruct, self).sympify_self()

        self.functions = sympify(self.functions)
        self.conditions = sympify(self.conditions)
        self.tol_param = sympify(self.tol_param)

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
    def __init__(self, field: Iterable[str], units, remove=True):
        super(SymmetryStruct, self).__init__(units, )
        self.field = field
        self.remove = remove

    def sympify_self(self):
        super(SymmetryStruct, self).sympify_self()
        self.field = sympify(np.array(self.field))

    def subs_self(self, old, new):
        if not hasattr(self.field, 'subs_self'):
            self.sympify_self()
        self.field = self.field.subs(old, new)


class ConstraintStruct(DimensionalExpressionStruct):
    def __init__(self, expr: str, units: str, lower: str, upper: str, activator: str, method: str = 'utm'):
        super(ConstraintStruct, self).__init__(expr, units)
        self.lower = lower
        self.upper = upper
        self.activator = activator
        self.method = method

    def sympify_self(self):
        super(ConstraintStruct, self).sympify_self()
        if self.lower is not None:
            self.lower = sympify(self.lower)
        if self.upper is not None:
            self.upper = sympify(self.upper)
        if self.activator is not None:
            self.activator = sympify(self.activator)

    def subs_self(self, old, new):
        self.sympify_self()
        self.expr = self.expr.subs(old, new)
        if self.lower is not None:
            self.lower = self.lower.subs(old, new)
        if self.upper is not None:
            self.upper = self.upper.subs(old, new)


def extract_syms(structs: Union[List[NamedStruct], NamedStruct]):
    if isinstance(structs, Iterable):
        return [struct.sym for struct in structs]
    elif hasattr(structs, 'sym'):
        return [structs.sym]
    else:
        raise RuntimeError('{} has no attribute "sym"'.format(structs))


def getattr_from_list(structs: Union[List[NamedStruct], NamedStruct], attr: str):
    if isinstance(structs, Iterable):
        return [getattr(struct, attr) for struct in structs]
    elif hasattr(structs, attr):
        return [getattr(structs, attr)]
    else:
        raise RuntimeError('{} has no attribute "{}"'.format(structs, attr))


def combine_component_lists(items):
    out = []
    if isinstance(items, Iterable):
        for item in items:
            out += combine_component_lists(item)
    else:
        out.append(items)

    return out
