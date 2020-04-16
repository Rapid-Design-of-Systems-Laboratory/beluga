# from .bvp_classes import BaseBVP, InputBVP, FuncBVP, SymBVP
from .ocp_classes import BaseOCP, InputOCP, FuncOCP, SymOCP, default_tol
from beluga.optimlib import *
from collections import OrderedDict
from copy import copy
from beluga.codegen import jit_compile_func
from .. import LocalCompiler
import numpy as np
from beluga.optimlib.special_functions import custom_functions_lib, table_lib


class BaseDual(BaseOCP):
    def __init__(self, name=None):
        BaseOCP.__init__(self, name=name)

        self.problem_type = 'BaseDual'

        self.costates = []
        self.coparameters = []
        self.constraint_adjoints = {'initial': [], 'terminal': []}

        self.hamiltonian = {'expr': None, 'units': None}

    def generate_repr_data(self):
        display_dict = OrderedDict()
        display_dict['States'] = self.states
        display_dict['Parameters'] = self.parameters
        display_dict['Initial Constraints'] = self.constraints['initial']
        display_dict['Terminal Constraints'] = self.constraints['terminal']
        return display_dict

    def copy_data_to_prob(self, duplicate):
        BaseOCP.copy_data_to_prob(self, duplicate)
        duplicate.costates = self.copy_list_items(self.costates)
        for location in ['intitial', 'terminal']:
            duplicate.constraint_adjoints[location] = self.copy_list_items(self.constraint_adjoints[location])
        duplicate.constants_of_motion = self.copy_list_items(self.constants_of_motion)

        duplicate.hamiltonian = copy(self.hamiltonian)
        duplicate.func_jac = copy(self.func_jac)
        duplicate.bc_jac = copy(self.bc_jac)

    def load_from_ocp(self, ocp: BaseOCP):
        ocp.copy_data_to_prob(self)
        return self


class InputDual(InputOCP, BaseDual):
    def __init__(self, name=None):

        InputOCP.__init__(self, name=name)
        BaseDual.__init__(self, name=name)

        self.problem_type = 'InputDual'

    def costate(self, name, eom, units, tol=default_tol):
        self.costates.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def coparameter(self, name, eom, units, tol=None):
        self.coparameters.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def constraint_multiplier(self, name, units, location):
        self.constraint_adjoints[location].append({'name': name, 'units': units})
        return self

    # def control_option(self, controls, exprs):
    #     self.control_options.append({'controls': controls, 'exprs': exprs})

    # def algebraic_equation(self, name, expr, units):
    #     self.algebraic_equations.append({'name': name, 'expr': expr, 'units': units})
    #     return self

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
        for coparameter in self.coparameters:
            self.sympify_name(coparameter)

        # # Constraint Multipliers
        # for constraint_multiplier in self.constraint_multipliers:
        #     self.sympify_name(constraint_multiplier)

        # # Control Options
        # for control_option in self.control_options:
        #     control_option['controls'] = self.sympify(control_option['controls'])

        # # Algebraic Equations
        # for algebraic_equation in self.algebraic_equations:
        #     self.sympify_name(algebraic_equation)

    def sympify_units(self):
        SymOCP.sympify_units(self)

        # Costates
        for costate in self.costates:
            costate['units'] = self.sympify(costate['units'])

        # Coparameters
        for coparameter in self.costates:
            coparameter['units'] = self.sympify(coparameter['units'])

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

        # Constants of Motion
        for constant_of_motion in self.constants_of_motion:
            constant_of_motion['expr'] = self.sympify(constant_of_motion['expr'])

        # Cost
        self.hamiltonian['units'] = self.sympify(self.hamiltonian['units'])


class FuncDual(FuncOCP, BaseDual):
    def __init__(self, name=None):
        BaseDual.__init__(self, name=name)

        self.problem_type = 'FuncDual'

        self._arg_syms = {
            'states': [],
            'parameters': [],
            'constants': [],
            'quads': []
        }

        # TODO Review names for these
        self.x_dot_func = None
        self.q_dot_func = None

        self.deriv_func = None
        self.quad_func = None

        self.bc_func = None

    def make_arg_lists(self):
        # Compile symbolic lists for arguments
        self._arg_syms['states'] = self.list_syms(self.states)
        self._arg_syms['parameters'] = self.list_syms(self.parameters)
        self._arg_syms['constants'] = self.list_syms(self.constants)
        self._arg_syms['quads'] = self.list_syms(self.quads)

        return self

    # TODO Modify for more complex deriv_func's with algebraic expressions
    def compile_eoms(self):
        x_dot_func = self.lambdify([self._arg_syms['states'], self._arg_syms['parameters'],
                                    self._arg_syms['constants']], self.list_syms(self.states, 'eom'))
        q_dot_func = self.lambdify([self._arg_syms['states'],+ self._arg_syms['parameters'],
                                    self._arg_syms['constants']], self.list_syms(self.quads, 'eom'))

        def deriv_func(x, _, p_d, k):
            return np.array(x_dot_func(x, p_d, k))

        def quad_func(x, _, p_d, k):
            return np.array(q_dot_func(x, p_d, k))

        self.x_dot_func, self.q_dot_func = x_dot_func, q_dot_func
        self.deriv_func = jit_compile_func(deriv_func, 4, func_name='deriv_func')
        self.quad_func = jit_compile_func(quad_func, 4, func_name='quad_func')

        return deriv_func, quad_func

    def compile_bc(self):
        bc_0_func = self.lambdify([self._arg_syms['states'], self._arg_syms['quads'], self._arg_syms['parameters'],
                                   [], self._arg_syms['constants']],
                                  self.list_syms(self.constraints['initial'], 'expr'))
        bc_f_func = self.lambdify([self._arg_syms['states'], self._arg_syms['quads'], self._arg_syms['parameters'],
                                   [], self._arg_syms['constants']],
                                  self.list_syms(self.constraints['terminal'], 'expr'))

        def bc_func(x_0, q_0, _, x_f, q_f, __, p_d, p_n, k):
            bc_0 = np.array(bc_0_func(x_0, q_0, p_d, p_n, k))
            bc_f = np.array(bc_f_func(x_f, q_f, p_d, p_n, k))
            return np.concatenate((bc_0, bc_f))

        self.bc_func = jit_compile_func(bc_func, 9, func_name='bc_func')
