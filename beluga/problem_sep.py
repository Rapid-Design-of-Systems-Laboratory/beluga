from sympy import sympify
import sympy
from beluga.utils.numerical_derivatives import gen_num_diff
from beluga.optimlib.special_functions import custom_functions
import sympy
import math


class StrOCP:
    def __init__(self, name='OCP'):

        self.name = name
        self.ind_var = None
        self.state_list = []
        self.control_list = []
        self.constant_list = []
        self.parameter_list = []
        self.quantity_list = []
        self.switch_list = []
        self.constraint_list = {'initial': [], 'terminal': [], 'path': []}
        self.cost = {'initial': 0, 'path': 0, 'terminal': 0, 'units': '1'}
        self.custom_function_list = []
        self.table_list = []
        self.scale_info = dict()

    def independent(self, name, units):
        self.ind_var = {'name': name, 'units': units}
        return self

    def state(self, name, eom, units, tol=None):
        self.state_list.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def control(self, name, units, tol=None):
        self.control_list.append({'name': name, 'units': units, 'tol': tol})
        return self

    def constant(self, name, default_value, units):
        self.control_list.append({'name': name, 'default_value': default_value, 'units': units})
        return self

    def parameter(self, name, units):
        self.parameter_list.append({'name': name, 'units': units})
        return self

    def quantity(self, name, expr):
        self.quantity_list.append({'name': name, 'expr': expr})
        return self

    def initial_constraint(self, expr, units, tol=None):
        self.constraint_list['initial'].append({'expr': expr, 'units': units, 'tol': tol})
        return self

    def path_constraint(self, expr, units, lower, upper, activator, method='utm', tol=None):
        self.constraint_list['path'].append({'expr': expr, 'units': units, 'lower': lower, 'upper': upper,
                                             'activator': activator, 'method': method, 'tol': tol})
        return self

    def terminal_constraint(self, expr, units, tol=None):
        self.constraint_list['terminal'].append({'expr': expr, 'units': units, 'tol': tol})
        return self

    def initial_cost(self, expr, units):
        self.cost['initial'] = expr
        # TODO Add units check
        self.cost['units'] = units
        return self

    def path_cost(self, expr, units):
        self.cost['path'] = expr
        # TODO Add units check
        self.cost['units'] = units + '*s'
        return self

    def terminal_cost(self, expr, units):
        self.cost['terminal'] = expr
        # TODO Add units check
        self.cost['units'] = units
        return self

    def switch(self, name, functions, conditions, tol):
        self.switch_list.append({'name': name, 'functions': functions, 'conditions': conditions, 'tol': tol})
        return self

    def custom_function(self, name, func, func_units, arg_units):
        self.custom_function_list.append({'name': name, 'func': func, 'func_units': func_units, 'arg_units': arg_units})
        return self

    def table(self, name, kind, ret_data, arg_data, ret_units, arg_units):
        self.table_list.append({'name': name, 'kind': kind, 'ret_data': ret_data, 'arg_data': arg_data,
                                'ret_units': ret_units, 'arg_units': arg_units})
        return self

    def scale(self, **kwargs):
        self.scale_info = kwargs
        return self


class SymOCP:
    def __init__(self, str_ocp):

        self.str_ocp = str_ocp

        # Sympify that ignores some built in names
        self.ignored_sym_func = ['rad', 're']
        self.sym_func_dict = dict((sym, sympy.Symbol(sym)) for sym in self.ignored_sym_func)

        # Compile Functions and Tables
        self.custom_function_list = self.sympify_custom_functions()

        self.name = str_ocp.name
        self.ind_var = None
        self.state_list = []
        self.control_list = []
        self.constant_list = []
        self.parameter_list = []
        self.quantity_list = []
        self.switch_list = []
        self.constraint_list = {'initial': [], 'terminal': [], 'path': []}
        self.cost = {'initial': 0, 'path': 0, 'terminal': 0, 'units': '1'}
        self.table_list = []
        self.scale_info = dict()

    def sympify(self, expr):
        return sympy.sympify(expr, locals=self.sym_func_dict)

    def sympify_custom_functions(self):
        custom_function_list = self.str_ocp.custom_function_list
        for function in custom_function_list:
            function['sym_func_gen'] = custom_functions.CustomFunctionGenerator(function['func'])
        return custom_function_list
