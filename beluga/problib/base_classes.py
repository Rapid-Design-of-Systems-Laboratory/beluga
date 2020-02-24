from collections import OrderedDict, Iterable
from copy import copy

import sympy
import numpy as np

from beluga.codegen import LocalCompiler, jit_compile_func
from beluga.optimlib.special_functions import custom_functions_lib, table_lib


class BaseProblem:
    def __init__(self, name=None):
        self.problem_type = 'BaseProblem'
        self.name = name

        self.ind_var = {'name': None, 'units': None}
        self.states = []
        self.parameters = []
        self.constants = []
        self.quads = []
        self.constraints = {'initial': [], 'terminal': []}
        self.quantities = []
        self.custom_functions = []
        self.tables = []
        self.switches = []

        self.symmetries = []

        self.units = []

        self.local_compiler = LocalCompiler()

        self.sympify = self.local_compiler.sympify
        self.lambdify = self.local_compiler.lambdify

        self.add_symbolic_local = self.local_compiler.add_symbolic_local
        self.add_function_local = self.local_compiler.add_function_local

    def __str__(self):
        return '{}_{}'.format(self.problem_type, self.name)

    def __repr__(self):
        display_dict = self.generate_repr_data()
        out_str = '{}: {}\n'.format(self.problem_type, self.name)
        out_str += self.str_display_dict(display_dict, tabs=1)
        return out_str

    def generate_repr_data(self):
        display_dict = OrderedDict()
        display_dict['States'] = self.states
        display_dict['Parameters'] = self.parameters
        display_dict['Initial Constraints'] = self.constraints['initial']
        display_dict['Terminal Constraints'] = self.constraints['terminal']
        return display_dict

    def str_display_dict(self, display_dict, tabs=0):
        tab_str = '\t' * tabs
        out_str = ''
        for name, item in display_dict.items():
            if isinstance(item, Iterable) and not isinstance(item, str):
                out_str += self.str_list_info(item, tabs=tabs, name=name)
            else:
                out_str += tab_str + '{}: {}\n'.format(name, item)
        return out_str

    @staticmethod
    def str_list_info(data, name=None, tabs=0):
        tab_str = '\t' * tabs

        if name is not None:
            out_str = tab_str + name + ':\n'
            tab_str += '\t'
        else:
            out_str = ''

        for datum in data:
            out_str += tab_str + str(datum) + '\n'

        return out_str

    @staticmethod
    def copy_list_items(original):
        dupicate = []
        for item in original:
            dupicate.append(copy(item))
        return dupicate

    def copy_problem_data(self, duplicate):

        duplicate.ind_var = copy(self.ind_var)
        duplicate.states = self.copy_list_items(self.states)
        duplicate.parameters = self.copy_list_items(self.parameters)
        duplicate.constants = self.copy_list_items(self.constants)
        duplicate.quads = self.copy_list_items(self.quads)
        for location in ['initial', 'terminal']:
            duplicate.constraints[location] = self.copy_list_items(self.constraints[location])
        duplicate.quantities = self.copy_list_items(self.quantities)
        duplicate.custom_functions = self.copy_list_items(self.custom_functions)
        duplicate.tables = self.copy_list_items(self.tables)
        duplicate.switches = self.copy_list_items(self.switches)
        duplicate.symmetries = self.symmetries

        duplicate.units = self.copy_list_items(self.units)

        # This should not be a copy but the same object (as intended)
        duplicate.local_compiler = self.local_compiler
        duplicate.sympify = self.sympify
        duplicate.lambdify = self.lambdify
        duplicate.add_symbolic_local = self.add_symbolic_local
        duplicate.add_function_local = self.add_function_local

        return duplicate


class BaseInput(BaseProblem):
    def __init__(self, name=None):
        BaseProblem.__init__(self, name=name)

        self.problem_type = 'BaseInput'

    def independent(self, name, units):
        self.ind_var = {'name': name, 'units': units}
        return self

    def state(self, name, eom, units, tol=None):
        self.states.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def constant(self, name, default_value, units):
        self.constants.append({'name': name, 'default_value': default_value, 'units': units})
        return self

    def parameter(self, name, units):
        self.parameters.append({'name': name, 'units': units})
        return self

    def quad(self, name, eom, units, tol=None):
        self.quads.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def quantity(self, name, expr):
        self.quantities.append({'name': name, 'expr': expr})
        return self

    def initial_constraint(self, expr, units, tol=None):
        self.constraints['initial'].append({'expr': expr, 'units': units, 'tol': tol})
        return self

    def terminal_constraint(self, expr, units, tol=None):
        self.constraints['terminal'].append({'expr': expr, 'units': units, 'tol': tol})
        return self

    def custom_function(self, name, func, func_units, arg_units):
        self.custom_functions.append({'name': name, 'func': func, 'func_units': func_units, 'arg_units': arg_units})
        return self

    def table(self, name, kind, ret_data, arg_data, table_units, arg_units):
        if kind.lower() == '1d_spline':
            table = table_lib.TableSpline1D(name, table_units, arg_data)
        else:
            raise NotImplementedError('{} is not a implemented table kind'.format(kind))

        self.tables.append({'name': name, 'kind': kind, 'ret_data': ret_data, 'arg_data': arg_data, 'table': table,
                            'table_units': table_units, 'arg_units': arg_units})
        return self

    def switch(self, name, functions, conditions, tol):
        self.switches.append({'name': name, 'sym': sympy.Symbol(name), 'functions': functions, 'conditions': conditions,
                              'tol': tol})
        return self

    def scale(self, **kwargs):
        for name in kwargs.keys():
            self.units.append({'name': name, 'expr': kwargs[name]})
        return self

    def symmetry(self, field, units, remove=True):
        self.symmetries.append({'field': field, 'units': units, 'remove': remove})

        return self

    def sympify_problem(self, sym_prob=None):

        if sym_prob is None:
            sym_prob = BaseSym()

        self.copy_problem_data(sym_prob)

        sym_prob.sympify_vars()
        sym_prob.sympify_units()
        sym_prob.sympify_exprs()

        return sym_prob


class BaseSym(BaseProblem):
    def __init__(self, name=None):
        BaseProblem.__init__(self, name=name)

        self.problem_type = 'BaseSym'
        self.mappings = []

    def sympify_name(self, item):
        item['sym'] = sympy.Symbol(item['name'])
        self.add_symbolic_local(item['name'], item['sym'])

    def sympify_vars(self):

        # Independent
        self.sympify_name(self.ind_var)

        # States
        for state in self.states:
            self.sympify_name(state)

        # Parmeters
        for parameter in self.parameters:
            self.sympify_name(parameter)

        # Constants
        for constant in self.constants:
            self.sympify_name(constant)

        # Custom Functions
        for custom_function in self.custom_functions:
            custom_function['sym'] = sympy.Symbol(custom_function['name'])
            custom_function['sym_func'] = custom_functions_lib.CustomFunctionGenerator(
                custom_function['func'], name=custom_function['name'], func_dict=self.local_compiler.func_locals)
            self.add_symbolic_local(custom_function['name'], custom_function['sym_func'])

        # Tables
        for table in self.tables:
            table['sym'] = sympy.Symbol(table['name'])
            if table['kind'].lower() == '1d_spline':
                table['table_func'] = table_lib.TableSpline1D(table['name'], table['arg_data'], table['ret_data'])
            else:
                raise NotImplementedError('{} is not a implemented table kind'.format(table['kind']))
            table['sym_table'] =\
                table_lib.SymTableGenerator(table['table_func'], func_dict=self.local_compiler.func_locals, order=0)
            self.add_symbolic_local(table['name'], table['sym_table'])

        # Switches
        for switch in self.switches:
            self.sympify_name(switch)

        # Quantites TODO Find a more elegant solution to this
        for _ in enumerate(self.quantities):
            for quantity in self.quantities:
                quantity['expr'] = self.local_compiler.sympify(str(quantity['expr']))
                self.add_symbolic_local(quantity['name'], quantity['expr'])

        return self

    def sympify_units(self):
        # Units
        for unit in self.units:
            unit['sym'] = sympy.Symbol(unit['name'])
            self.add_symbolic_local(unit['name'], unit['sym'])

        # Independent
        self.ind_var['units'] = self.sympify(self.ind_var['units'])

        # States
        for state in self.states:
            state['units'] = self.sympify(state['units'])

        # Quads
        for quad in self.quads:
            quad['units'] = self.sympify(quad['units'])

        # Parmeters
        for parameter in self.parameters:
            parameter['units'] = self.sympify(parameter['units'])

        # Constants
        for constant in self.constants:
            constant['units'] = self.sympify(constant['units'])

            # Constraints
            for location in ['initial', 'terminal']:
                for constraint in self.constraints[location]:
                    constraint['units'] = self.sympify(constraint['units'])

        # Quad
        for quad in self.quads:
            quad['units'] = self.sympify(quad['units'])

        # Custom Functions
        for custom_function in self.custom_functions:
            custom_function['func_units'] = self.sympify(custom_function['func_units'])
            custom_function['arg_units'] = [self.sympify(arg_units) for arg_units in custom_function['arg_units']]

        # Tables
        for table in self.tables:
            table['ret_units'] = self.sympify(table['ret_units'])
            table['arg_units'] = [self.sympify(arg_units) for arg_units in table['arg_units']]

        # Symmetries
        for symmetry in self.symmetries:
            symmetry['units'] = self.sympify(symmetry['units'])

        # Symmetries
        for symmetry in self.symmetries:
            symmetry['units'] = self.sympify(symmetry['units'])

        return self

    def sympify_exprs(self):

        # States
        for state in self.states:
            state['eom'] = self.sympify(state['eom'])

        # Constraints
        for location in ['initial', 'terminal']:
            for constraint in self.constraints[location]:
                constraint['expr'] = self.sympify(constraint['expr'])

        # Switches
        for switch in self.switches:
            switch['functions'] = self.sympify(switch['functions'])
            switch['conditions'] = self.sympify(switch['conditions'])
            switch['tol'] = self.sympify(switch['tol'])

        # Symmetries
        for symmetry in self.symmetries:
            symmetry['field'] = self.sympify(symmetry['field'])

        return self

    def lambdify_problem(self, func_prob=None):

        if func_prob is None:
            func_prob = BaseFunc()

        self.copy_problem_data(func_prob)

        func_prob.make_arg_lists()
        func_prob.compile_eoms()
        func_prob.compile_bc()

        return func_prob


class BaseFunc(BaseProblem):
    def __init__(self, name=None):
        BaseProblem.__init__(self, name=name)

        self.problem_type = 'BaseFunc'

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

    @staticmethod
    def list_syms(info_list, field='sym'):
        sym_list = []
        for item in info_list:
            sym_list.append(item[field])
        return sym_list

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
        q_dot_func = self.lambdify([self._arg_syms['states'], self._arg_syms['parameters'],
                                    self._arg_syms['constants']], self.list_syms(self.quads, 'eom'))

        def deriv_func(x, _, p_d, k):
            return np.array(x_dot_func(x, p_d, k))

        def quad_func(x, _, p_d, k):
            return np.array(q_dot_func(x, p_d, k))

        self.x_dot_func, self.q_dot_func = x_dot_func, q_dot_func
        self.deriv_func = jit_compile_func(deriv_func, 4, func_name='deriv_func')
        self.quad_func = jit_compile_func(quad_func, 4, func_name='quad_func')

        return

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


