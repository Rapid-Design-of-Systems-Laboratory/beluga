from beluga.utils.numerical_derivatives import gen_num_diff
from beluga.optimlib.special_functions import custom_functions_lib, table_lib
from beluga.optimlib.optimlib import *
from beluga.optimlib.bvp import BVP
import sympy

# TODO Seperate into input, symbolic, and functional OCP


class OCP:
    def __init__(self, name='OCP'):

        self.name = name
        self.independent_variable = {'name': 't', 'sym': sympy.Symbol('t'), 'units': sympy.Symbol('s')}
        self.state_list = []
        self.control_list = []
        self.constant_list = []
        self.parameter_list = []
        self.quantity_list = []
        self.constraint_dict = {'initial': [], 'terminal': [], 'path': []}
        self.cost = {'initial': 0., 'path': 0., 'terminal': 0., 'units': None, 'tol': None}
        self.symmetry_list = []
        self.switch_list = []
        self.custom_function_list = []
        self.table_list = []
        self.units = []

        # TODO Make special class to clearly pass this information
        self.sympified_exprs = False
        self.locals_dict = dict()
        self.mod_dict = dict()

    def independent(self, name, units):
        self.independent_variable = {'name': name, 'sym': sympy.Symbol(name), 'units': units}
        self.add_to_locals(name)
        return self

    def state(self, name, eom, units, tol=None):
        self.state_list.append({'name': name, 'sym': sympy.Symbol(name), 'eom': eom, 'units': units, 'tol': tol})
        self.add_to_locals(name)
        return self

    def control(self, name, units, tol=None):
        self.add_to_locals(name)
        self.control_list.append({'name': name, 'sym': sympy.Symbol(name), 'units': units, 'tol': tol})
        return self

    def constant(self, name, default_value, units):
        self.add_to_locals(name)
        self.control_list.append({'name': name, 'sym': sympy.Symbol(name), 'default_value': default_value,
                                  'units': units})
        return self

    def parameter(self, name, units):
        self.add_to_locals(name)
        self.parameter_list.append({'name': name, 'sym': sympy.Symbol(name), 'units': units})
        return self

    def quantity(self, name, expr):
        self.add_to_locals(name)
        self.quantity_list.append({'name': name, 'sym': sympy.Symbol(name), 'expr': expr})
        return self

    def initial_constraint(self, expr, units, tol=None):
        self.constraint_dict['initial'].append({'expr': expr, 'units': units, 'tol': tol})
        return self

    def path_constraint(self, expr, units, lower, upper, activator, method='utm', tol=None):
        self.constraint_dict['path'].append({'expr': expr, 'units': units, 'lower': lower, 'upper': upper,
                                             'activator': activator, 'method': method, 'tol': tol})
        return self

    def terminal_constraint(self, expr, units, tol=None):
        self.constraint_dict['terminal'].append({'expr': expr, 'units': units, 'tol': tol})
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
        self.cost['units'] = units + '*' + self.independent_variable['units']
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

    def switch(self, name, functions, conditions, tol):
        self.switch_list.append({'name': name, 'sym': sympy.Symbol(name), 'functions': functions,
                                 'conditions': conditions, 'tol': tol})
        return self

    def custom_function(self, name, func, func_units, arg_units):
        custom_function_info = {'name': name, 'sym': sympy.Symbol(name), 'func': func, 'func_units': func_units,
                                'arg_units': arg_units,
                                'sym_func': custom_functions_lib.CustomFunctionGenerator(func, name=name,
                                                                                         func_dict=self.mod_dict)}
        self.custom_function_list.append(custom_function_info)
        self.locals_dict[name] = custom_function_info['sym_func']
        return self

    def table(self, name, kind, ret_data, arg_data, ret_units, arg_units):
        if kind.lower() == '1d_spline':
            table = table_lib.TableSpline1D(name, arg_data, ret_data)
        else:
            raise NotImplementedError('{} is not a implemented table kind'.format(kind))

        table_info = {'name': name, 'sym': sympy.Symbol(name), 'kind': kind, 'ret_data': ret_data, 'arg_data': arg_data,
                      'ret_units': ret_units, 'arg_units': arg_units, 'sym_table': table_lib.SymTableGenerator(table)}
        self.table_list.append(table_info)
        self.locals_dict[name] = table_info['sym_table']
        return self

    def symmetry(self, field, units, remove=None):
        self.symmetry_list.append({'field': field, 'units': units, 'remove': remove})

        return self

    def scale(self, **kwargs):
        for name in kwargs.keys():
            self.add_to_locals(name)
            self.units.append({'name': name, 'sym': sympy.Symbol(name), 'expr': kwargs[name]})
        return self

    def add_to_locals(self, name):
        if name in self.locals_dict.keys():
            raise UserWarning('{} is already defined'.format(name))
        self.locals_dict[name] = sympy.Symbol(name)

    def sympify(self, expr):
        return sympy.sympify(expr, locals=self.locals_dict)

    def sympify_all(self):
        for var in [self.independent_variable] + self.state_list + self.control_list + self.constant_list \
                   + self.parameter_list + self.constraint_dict['initial'] + self.constraint_dict['path'] \
                   + self.constraint_dict['terminal'] + [self.cost]:
            var['units'] = self.sympify(var['units'])

        for _ in enumerate(self.quantity_list):
            for quantity in self.quantity_list:
                quantity['expr'] = self.sympify(str(quantity['expr']))
                self.locals_dict[quantity['name']] = quantity['expr']

        for state in self.state_list:
            state['eom'] = self.sympify(state['eom'])

        for constraint_list in [self.constraint_dict['initial'] + self.constraint_dict['terminal']]:
            for constraint in constraint_list:
                constraint['expr'] = self.sympify(constraint['expr'])

        for constraint in self.constraint_dict['path']:
            constraint['expr'] = self.sympify(constraint['expr'])
            constraint['lower'] = self.sympify(constraint['lower'])
            constraint['upper'] = self.sympify(constraint['upper'])
            constraint['activator'] = self.sympify(constraint['activator'])

        for switch in self.switch_list:
            switch['functions'] = self.sympify(switch['functions'])
            switch['conditions'] = self.sympify(switch['conditions'])
            switch['tol'] = self.sympify(switch['tol'])

        self.cost['initial'] = self.sympify(self.cost['initial'])
        self.cost['path'] = self.sympify(self.cost['path'])
        self.cost['terminal'] = self.sympify(self.cost['terminal'])

    def dualize(self):
        self.sympify_all()
        return dualize(self)
