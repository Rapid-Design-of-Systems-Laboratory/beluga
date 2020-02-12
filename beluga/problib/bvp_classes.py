from .base_classes import BaseProblem, BaseInput, BaseFunc, BaseSym
from beluga.optimlib import *
from collections import OrderedDict
from copy import copy


class BaseBVP(BaseProblem):
    def __init__(self, name=None):
        BaseProblem.__init__(name=name)

        self.costates = []
        self.coparameters = []
        self.constraint_multipliers = []
        self.control_options = []

        self.algebraic_equations = []
        self.constants_of_motion = []

        self.hamiltonian = None
        self.func_jac = {'df_dy': None, 'df_dp': None}
        self.bc_jac = {'initial': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None},
                       'terminal': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None}}

    def generate_repr_data(self):
        display_dict = OrderedDict()
        display_dict['States'] = self.states
        display_dict['Parameters'] = self.parameters
        display_dict['Initial Constraints'] = self.constraints['initial']
        display_dict['Terminal Constraints'] = self.constraints['terminal']
        return display_dict

    def copy_problem_data(self, duplicate):
        BaseProblem.copy_problem_data(self, duplicate)
        duplicate.costates = self.copy_list_items(self.costates)
        duplicate.coparameters = self.copy_list_items(self.coparameters)
        duplicate.constraint_multipliers = self.copy_list_items(self.constraint_multipliers)
        duplicate.control_options = self.copy_list_items(self.control_options)

        duplicate.algebraic_equations = self.copy_list_items(self.algebraic_equations)
        duplicate.constants_of_motion = self.copy_list_items(self.constants_of_motion)

        duplicate.hamiltonian = copy(self.hamiltonian)
        duplicate.func_jac = copy(self.func_jac)
        duplicate.bc_jac = copy(self.bc_jac)


class InputBVP(BaseInput, BaseBVP):
    def __init__(self, name=None):

        BaseInput.__init__(self, name=name)
        BaseBVP.__init__(self, name=name)

        self.problem_type = 'InputBVP'

    def costate(self, name, eom, units, tol=None):
        self.costates.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def coparameter(self, name, eom, units, tol=None):
        self.coparameters.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def constraint_multiplier(self, name, units):
        self.constraint_multipliers.append({'name': name, 'units': units})
        return self

    def control_option(self, controls, exprs):
        self.control_options.append({'controls': controls, 'exprs': exprs})

    def algebraic_equation(self, name, expr, units):
        self.algebraic_equations.append({'name': name, 'expr': expr, 'units': units})
        return self

    def constant_of_motion(self, name, expr, units):
        self.constants_of_motion.append({'name': name, 'expr': expr, 'units': units})
        return self

    def set_hamiltonian(self, expr, units):
        self.hamiltonian = {'expr': expr, 'units': units}
        self.constants_of_motion.append({'name': 'hamiltonian', 'expr': expr, 'units': units})
        return self

    def set_func_jac_expr(self, kind, expr):
        self.func_jac[kind] = expr
        return self

    def set_bc_jac_expr(self, location, kind, expr):
        self.bc_jac[location][kind] = expr
        return self

    def sympify_problem(self, sym_prob=None):

        if sym_prob is None:
            sym_prob = SymBVP()

        BaseInput.sympify_problem(self, sym_prob=sym_prob)
        return sym_prob


class SymBVP(BaseSym, BaseBVP):
    def __init__(self, name=None):
        BaseSym.__init__(self, name=name)
        BaseBVP.__init__(self, name=name)

        self.problem_type = 'SymBVP'
        self.omega = None

    def sympify_vars(self):
        BaseSym.sympify_vars(self)

        # Costates
        for costate in self.costates:
            self.sympify_name(costate)

        # Coparmeters
        for coparameter in self.coparameters:
            self.sympify_name(coparameter)

        # Constraint Multipliers
        for constraint_multiplier in self.constraint_multipliers:
            self.sympify_name(constraint_multiplier)

        # Control Options
        for control_option in self.control_options:
            control_option['controls'] = self.sympify(control_option['controls'])

        # Algebraic Equations
        for algebraic_equation in self.algebraic_equations:
            self.sympify_name(algebraic_equation)

        # Constants of Motion
        for constant_of_motion in self.constants_of_motion:
            self.sympify_name(constant_of_motion)

    def sympify_units(self):
        BaseSym.sympify_units(self)

        # Costates
        for costate in self.costates:
            costate['units'] = self.sympify(costate['units'])

        # Coparameters
        for coparameter in self.costates:
            coparameter['units'] = self.sympify(coparameter['units'])

        # Constraint Multipliers
        for constraint_multiplier in self.constraint_multipliers:
            constraint_multiplier['units'] = self.sympify(constraint_multiplier['units'])

        # Algebraic Equations
        for algebraic_equation in self.algebraic_equations:
            algebraic_equation['units'] = self.sympify(algebraic_equation['units'])

        # Constants of Motion
        for constant_of_motion in self.constants_of_motion:
            constant_of_motion['units'] = self.sympify(constant_of_motion['units'])

        # Cost
        self.hamiltonian['units'] = self.sympify(self.hamiltonian['units'])

    def sympify_exprs(self):
        BaseSym.sympify_exprs(self)

        # Costates
        for costate in self.costates:
            costate['eom'] = self.sympify(costate['eom'])

        # Coparameters
        for coparameter in self.costates:
            coparameter['eom'] = self.sympify(coparameter['eom'])

        # Algebraic Equations
        for algebraic_equation in self.algebraic_equations:
            algebraic_equation['expr'] = self.sympify(algebraic_equation['expr'])

        # Constants of Motion
        for constant_of_motion in self.constants_of_motion:
            constant_of_motion['expr'] = self.sympify(constant_of_motion['expr'])

        # Cost
        self.hamiltonian['units'] = self.sympify(self.hamiltonian['units'])


class FuncBVP(BaseFunc, BaseBVP):
    pass
