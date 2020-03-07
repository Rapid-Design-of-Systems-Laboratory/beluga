# from .bvp_classes import BaseBVP, InputBVP, FuncBVP, SymBVP
from .ocp_classes import BaseOCP, InputOCP, FuncOCP, SymOCP, default_tol
from beluga.optimlib import *
from collections import OrderedDict
from copy import copy


class BaseDual(BaseOCP):
    def __init__(self, name=None):
        BaseOCP.__init__(self, name=name)

        self.problem_type = 'BaseDual'

        self.costates = []
        # self.coparameters = []
        self.constraint_multipliers = {'initial': [], 'terminal': []}

        self.hamiltonian = {'expr': None, 'units': None}

    def generate_repr_data(self):
        display_dict = OrderedDict()
        display_dict['States'] = self.states
        display_dict['Parameters'] = self.parameters
        display_dict['Initial Constraints'] = self.constraints['initial']
        display_dict['Terminal Constraints'] = self.constraints['terminal']
        return display_dict

    def copy_problem_data(self, duplicate):
        BaseOCP.copy_problem_data(self, duplicate)
        duplicate.costates = self.copy_list_items(self.costates)
        # duplicate.coparameters = self.copy_list_items(self.coparameters)
        duplicate.constraint_multipliers = self.copy_list_items(self.constraint_multipliers)
        duplicate.control_options = self.copy_list_items(self.control_options)

        duplicate.algebraic_equations = self.copy_list_items(self.algebraic_equations)
        duplicate.constants_of_motion = self.copy_list_items(self.constants_of_motion)

        duplicate.hamiltonian = copy(self.hamiltonian)
        duplicate.func_jac = copy(self.func_jac)
        duplicate.bc_jac = copy(self.bc_jac)

    def load_from_ocp(self, ocp: BaseOCP):
        ocp.copy_problem_data(self)
        return self


class InputDual(InputOCP, BaseDual):
    def __init__(self, name=None):

        InputOCP.__init__(self, name=name)
        BaseDual.__init__(self, name=name)

        self.problem_type = 'InputDual'

    def costate(self, name, eom, units, tol=default_tol):
        self.costates.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    # def coparameter(self, name, eom, units, tol=None):
    #     self.coparameters.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
    #     return self

    def constraint_multiplier(self, name, units, location):
        self.constraint_multipliers[location].append({'name': name, 'units': units})
        return self

    def control_option(self, controls, exprs):
        self.control_options.append({'controls': controls, 'exprs': exprs})

    def algebraic_equation(self, name, expr, units):
        self.algebraic_equations.append({'name': name, 'expr': expr, 'units': units})
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
            sym_prob = SymDual()

        InputOCP.sympify_problem(self, sym_prob=sym_prob)
        return sym_prob


class SymDual(SymOCP, BaseDual):
    def __init__(self, name=None):
        SymOCP.__init__(self, name=name)
        BaseDual.__init__(self, name=name)

        self.problem_type = 'SymDual'
        self.omega = None

    def sympify_vars(self):
        SymOCP.sympify_vars(self)

        # Costates
        for costate in self.costates:
            self.sympify_name(costate)

        # Coparmeters
        # for coparameter in self.coparameters:
        #     self.sympify_name(coparameter)

        # Constraint Multipliers
        for constraint_multiplier in self.constraint_multipliers:
            self.sympify_name(constraint_multiplier)

        # Control Options
        for control_option in self.control_options:
            control_option['controls'] = self.sympify(control_option['controls'])

        # Algebraic Equations
        for algebraic_equation in self.algebraic_equations:
            self.sympify_name(algebraic_equation)

    def sympify_units(self):
        SymOCP.sympify_units(self)

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
        SymOCP.sympify_exprs(self)

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


class FuncDual(FuncOCP, BaseDual):
    pass
