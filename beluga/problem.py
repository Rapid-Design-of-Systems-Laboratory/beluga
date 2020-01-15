from sympy import sympify


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

    def path_constraint(self, expr, units, tol=None):
        self.constraint_list['path'].append({'expr': expr, 'units': units, 'tol': tol})
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
