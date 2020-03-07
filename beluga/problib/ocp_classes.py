from .bvp_classes import BaseBVP, InputBVP, SymBVP, FuncBVP, default_tol
from collections import OrderedDict
from copy import copy
import sympy
import numpy as np

from beluga.codegen import jit_compile_func


class BaseOCP(BaseBVP):
    def __init__(self, name=None):
        BaseBVP.__init__(self, name=name)

        self.problem_type = 'BaseOCP'

        self.controls = []
        self.constraints = {'initial': [], 'path': [], 'terminal': []}
        self.cost = {'initial': 0., 'path': 0., 'terminal': 0., 'units': None, 'tol': None}

        self.constants_of_motion = []

    def generate_repr_data(self):
        display_dict = OrderedDict()
        display_dict['States'] = self.states
        display_dict['Parameters'] = self.parameters
        display_dict['Initial Cost'] = self.cost['initial']
        display_dict['Path Cost'] = self.cost['path']
        display_dict['Terminal Cost'] = self.cost['terminal']
        return display_dict

    def copy_problem_data(self, duplicate):
        BaseBVP.copy_problem_data(self, duplicate)
        duplicate.controls = self.copy_list_items(self.controls)
        duplicate.constraints['path'] = self.copy_list_items(self.constraints['path'])
        duplicate.cost = copy(self.cost)


class InputOCP(InputBVP, BaseOCP):
    def __init__(self, name=None):
        InputBVP.__init__(self, name=name)
        BaseOCP.__init__(self, name=name)

        self.problem_type = 'InputOCP'

    def control(self, name, units, tol=default_tol):
        self.controls.append({'name': name, 'sym': sympy.Symbol(name), 'units': units, 'tol': tol})
        self.local_compiler.add_symbolic_local(name, sympy.Symbol(name))
        return self

    def path_constraint(self, expr, units, lower, upper, activator, method='utm', tol=default_tol):
        self.constraints['path'].append({'expr': expr, 'units': units, 'lower': lower, 'upper': upper,
                                         'activator': activator, 'method': method, 'tol': tol})
        return self

    def constant_of_motion(self, name, expr, units):
        self.constants_of_motion.append({'name': name, 'expr': expr, 'units': units})
        return self

    def initial_cost(self, expr, units, tol=default_tol):
        self.cost['initial'] = expr
        # TODO Add units check
        self.cost['units'] = units
        self.cost['tol'] = tol
        return self

    def path_cost(self, expr, units, tol=default_tol):
        self.cost['path'] = expr
        # TODO Add units check
        self.cost['units'] = units + '*' + self.ind_var['units']
        self.cost['tol'] = tol
        return self

    def terminal_cost(self, expr, units, tol=default_tol):
        self.cost['terminal'] = expr
        # TODO Add units check
        self.cost['units'] = units
        self.cost['tol'] = tol
        return self

    # TODO Rename cost
    def set_cost(self, initial=None, path=None, terminal=None, units=None, tol=default_tol):
        if initial is not None:
            self.cost['initial'] = initial
        if path is not None:
            self.cost['path'] = path
        if terminal is not None:
            self.cost['terminal'] = terminal
        if units is not None:
            self.cost['units'] = units
        if tol is not None:
            self.cost['tol'] = tol

    def sympify_problem(self, sym_prob=None):

        if sym_prob is None:
            sym_prob = SymOCP()

        InputBVP.sympify_problem(self, sym_prob=sym_prob)
        return sym_prob


class SymOCP(BaseOCP, SymBVP):
    def __init__(self, name=None):
        BaseOCP.__init__(self, name=name)
        SymBVP.__init__(self, name=name)
        self.problem_type = 'SymOCP'

    def sympify_vars(self):
        SymBVP.sympify_vars(self)

        # Controls
        for control in self.controls:
            self.sympify_name(control)

        # Constants of Motion
        for constant_of_motion in self.constants_of_motion:
            self.sympify_name(constant_of_motion)

    def sympify_units(self):
        SymBVP.sympify_units(self)

        # Controls
        for control in self.controls:
            control['units'] = self.sympify(control['units'])

        # Path Constraints
        for constraint in self.constraints['path']:
            constraint['units'] = self.sympify(constraint['units'])

        # Cost
        self.cost['units'] = self.sympify(self.cost['units'])

    def sympify_exprs(self):
        SymBVP.sympify_exprs(self)

        # Path Constraints
        for constraint in self.constraints['path']:
            constraint['expr'] = self.sympify(constraint['expr'])
            constraint['lower'] = self.sympify(constraint['lower'])
            constraint['upper'] = self.sympify(constraint['upper'])
            constraint['activator'] = self.sympify(constraint['activator'])

        # Cost
        self.cost['initial'] = self.sympify(self.cost['initial'])
        self.cost['path'] = self.sympify(self.cost['path'])
        self.cost['terminal'] = self.sympify(self.cost['terminal'])

    def eps_trig(self):
        pass

    def utm(self):
        pass

    def dualize(self):
        pass


# TODO Finish fleshing out this class
class FuncOCP(BaseOCP, FuncBVP):
    def __init__(self):
        BaseOCP.__init__(self)
        FuncBVP.__init__(self)

        self.compute_f = None
        self._control_syms = []

    def make_sym_lists_for_args(self):
        FuncBVP.make_sym_lists_for_args(self)
        self._control_syms = self.list_syms(self.controls)
        return self

    def compile_deriv_func(self):
        deriv_func = self.lambdify([self._state_syms, self._control_syms, self._parameter_syms, self._constant_syms],
                                   np.array(self._state_eom_vec))
        quad_func = self.lambdify([self._state_syms, self._control_syms, self._parameter_syms, self._constant_syms],
                                  np.array(self._quad_eom_vec))

        self.deriv_func = jit_compile_func(deriv_func, 4, func_name='deriv_func')
        self.compute_f = self.deriv_func
        self.quad_func = jit_compile_func(quad_func, 4, func_name='quad_func')

        return self
