from collections import OrderedDict

import sympy

from .base_classes import BaseProblem, BaseInput, BaseSym, BaseFunc


class BaseOCP(BaseProblem):
    def __init__(self, name=None):
        BaseProblem.__init__(self, name=name)

        self.problem_type = 'BaseOCP'

        self.controls = []
        self.constraints = {'initial': [], 'path': [], 'terminal': []}
        self.cost = {'initial': 0., 'path': 0., 'terminal': 0., 'units': None, 'tol': None}
        self.symmetries = []

    def generate_repr_data(self):
        display_dict = OrderedDict()
        display_dict['States'] = self.states
        display_dict['Parameters'] = self.parameters
        display_dict['Initial Cost'] = self.cost['initial']
        display_dict['Path Cost'] = self.cost['path']
        display_dict['Terminal Cost'] = self.cost['terminal']
        return display_dict

    def copy_problem_data(self, duplicate):
        BaseProblem.copy_problem_data(self, duplicate)
        duplicate.controls = self.copy_list_items(self.controls)
        duplicate.constraints['path'] = self.copy_list_items(self.constraints['path'])
        duplicate.cost = self.cost


class InputOCP(BaseInput, BaseOCP):
    def __init__(self, name=None):
        BaseInput.__init__(self, name=name)
        BaseOCP.__init__(self, name=name)

        self.problem_type = 'InputOCP'

    def control(self, name, units, tol=None):
        self.controls.append({'name': name, 'sym': sympy.Symbol(name), 'units': units, 'tol': tol})
        self.local_compiler.add_symbolic_local(name, sympy.Symbol(name))
        return self

    def path_constraint(self, expr, units, lower, upper, activator, method='utm', tol=None):
        self.constraints['path'].append({'expr': expr, 'units': units, 'lower': lower, 'upper': upper,
                                         'activator': activator, 'method': method, 'tol': tol})
        return self

    def initial_cost(self, expr, units, tol=None):
        self.cost['initial'] = expr
        # TODO Add units check
        self.cost['units'] = units
        self.cost['tol'] = tol
        return self

    def path_cost(self, expr, units, tol=None):
        self.cost['path'] = expr
        # TODO Add units check
        self.cost['units'] = units + '*' + self.ind_var['units']
        self.cost['tol'] = tol
        return self

    def terminal_cost(self, expr, units, tol=None):
        self.cost['terminal'] = expr
        # TODO Add units check
        self.cost['units'] = units
        self.cost['tol'] = tol
        return self

    # TODO Rename cost
    def set_cost(self, initial=None, path=None, terminal=None, units=None, tol=None):
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

    def symmetry(self, field, units, remove=True):
        self.symmetries.append({'field': field, 'units': units, 'remove': remove})

        return self

    def sympify_vars(self, sym_prob):
        BaseInput.sympify_vars(self, sym_prob)

        # Controls
        for control in sym_prob.controls:
            self.sympify_name(control)

    @staticmethod
    def sympify_units(sym_prob):
        BaseInput.sympify_units(sym_prob)

        # Controls
        for control in sym_prob.controls:
            control['units'] = sym_prob.sympify(control['units'])

        # Path Constraints
        for constraint in sym_prob.constraints['path']:
            constraint['units'] = sym_prob.sympify(constraint['units'])

        # Cost
        sym_prob.cost['units'] = sym_prob.sympify(sym_prob.cost['units'])

        # Symmetries
        for symmetry in sym_prob.symmetries:
            symmetry['units'] = sym_prob.sympify(symmetry['units'])

    @staticmethod
    def sympify_exprs(sym_prob):
        BaseInput.sympify_exprs(sym_prob)

        # Path Constraints
        for constraint in sym_prob.constraints['path']:
            constraint['expr'] = sym_prob.sympify(constraint['expr'])
            constraint['lower'] = sym_prob.sympify(constraint['lower'])
            constraint['upper'] = sym_prob.sympify(constraint['upper'])
            constraint['activator'] = sym_prob.sympify(constraint['activator'])

        # Cost
        sym_prob.cost['initial'] = sym_prob.sympify(sym_prob.cost['initial'])
        sym_prob.cost['path'] = sym_prob.sympify(sym_prob.cost['path'])
        sym_prob.cost['terminal'] = sym_prob.sympify(sym_prob.cost['terminal'])

        # Symmetries
        for symmetry in sym_prob.symmetries:
            symmetry['field'] = sym_prob.sympify(symmetry['field'])

    def sympify_problem(self, sym_prob=None):

        if sym_prob is None:
            sym_prob = SymOCP()

        BaseInput.sympify_problem(self, sym_prob=sym_prob)
        return sym_prob


class SymOCP(BaseOCP, BaseSym):
    def __init__(self, name=None):
        BaseOCP.__init__(self, name=name)
        BaseSym.__init__(self, name=name)
        self.problem_type = 'SymOCP'


class FuncOCP(BaseOCP, BaseFunc):
    pass
