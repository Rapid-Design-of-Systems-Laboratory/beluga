from .components_structures import *
from ...numeric.compilation import LocalCompiler
from typing import Iterable


class Problem:
    def __init__(self, name=None, prob_type='ocp'):

        self.prob_type = prob_type

        if name is None:
            self.name = 'Beluga_Problem'
        else:
            self.name = name

        self.local_compiler = LocalCompiler()
        self.sol_map_chain = []
        # self.solution_set = SolSet()
        self.solution_set = []

        self.independent_variable = None

        self.states = []
        self.costates = []

        self.parameters = []
        self.coparameters = []

        self.controls = []
        self.control_law = []

        self.constraints = {'initial': [], 'path': [], 'terminal': []}
        self.constraint_parameters = []
        self.constraint_adjoints = []
        self.cost = CostStruct(local_compiler=self.local_compiler)

        self.constants = []
        self.quantities = []
        self.custom_functions = []
        self.tables = []
        self.switches = []

        self.hamiltonian = None
        self.dh_du = None

        self.quads = []
        self.symmetries = []
        self.constants_of_motion = []
        self.omega = None

        self.units = []

        self.func_jac = {'df_dy': None, 'df_dp': None}
        self.bc_jac = {'initial': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None},
                       'terminal': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None}}

        self.sympify = self.local_compiler.sympify
        self.lambdify = self.local_compiler.lambdify

        self.add_symbolic_local = self.local_compiler.add_symbolic_local
        self.add_function_local = self.local_compiler.add_function_local

        self.functional_problem = None

        self.sympified = False
        self.dualized = False
        self.lambdified = False

    def __repr__(self):
        return '{}_{}'.format(self.prob_type, self.name)

    def reset(self):
        self.sympified = False
        self.lambdified = False

    """
    Input Functions
    """

    # TODO Implement tolerances
    default_tol = 1e-4

    def independent(self, name, units):
        self.independent_variable = NamedDimensionalStruct(name, units, local_compiler=self.local_compiler)
        return self

    def state(self, name, eom, units):
        self.states.append(DynamicStruct(name, eom, units, local_compiler=self.local_compiler))
        return self

    def costate(self, name, eom, units):
        self.costates.append(DynamicStruct(name, eom, units, local_compiler=self.local_compiler))
        return self

    def parameter(self, name, units):
        self.parameters.append(NamedDimensionalStruct(name, units, local_compiler=self.local_compiler))
        return self

    def coparameter(self, name, eom, units):
        self.coparameters.append(DynamicStruct(name, eom, units, local_compiler=self.local_compiler))
        return self

    def control(self, name, units):
        self.controls.append(NamedDimensionalStruct(name, units, local_compiler=self.local_compiler))
        return self

    def initial_constraint(self, expr, units):
        self.constraints['initial'].append(
            DimensionalExpressionStruct(expr, units, local_compiler=self.local_compiler))
        return self

    def path_constraint(self, expr, units, lower, upper, activator, method='utm'):
        self.constraints['path'].append(
            PathConstraintStruct(expr, units, lower, upper, activator,
                                 method=method, local_compiler=self.local_compiler))
        return self

    def terminal_constraint(self, expr, units):
        self.constraints['terminal'].append(
            DimensionalExpressionStruct(expr, units, local_compiler=self.local_compiler))
        return self

    def constraint_parameter(self, name, units):
        self.constraint_parameters.append(NamedDimensionalStruct(name, units, local_compiler=self.local_compiler))
        return self

    def constant(self, name, default_value, units):
        self.constants.append(Constant(name, default_value, units, local_compiler=self.local_compiler))
        return self

    def quantity(self, name, expr):
        self.quantities.append(NamedExpressionStruct(name, expr, local_compiler=self.local_compiler))
        return self

    def custom_function(self, name, func, func_units, arg_units):
        self.custom_functions.append(
            FunctionStruct(name, func, func_units, arg_units,
                           local_compiler=self.local_compiler, dim_consistent=True))
        return self

    def table(self, name, kind, ret_data, arg_data, table_units, arg_units):
        self.tables.append(
            TableStruct(name, kind, ret_data, arg_data, table_units, arg_units,
                        local_compiler=self.local_compiler, dim_consistent=True))
        return self

    def switch(self, name, functions, conditions, activator):
        self.switches.append(
            SwitchStruct(name, functions, conditions, activator, local_compiler=self.local_compiler))
        return self

    def quad(self, name, eom, units):
        self.quads.append(DynamicStruct(name, eom, units, local_compiler=self.local_compiler))
        return self

    def symmetry(self, field, units, remove=True):
        self.symmetries.append(SymmetryStruct(field, units, remove=remove, local_compiler=self.local_compiler))
        return self

    def constant_of_motion(self, name, expr, units):
        self.constants_of_motion.append(NamedDimensionalExpressionStruct(name, expr, units))
        return self

    def initial_cost(self, expr, units):
        # TODO Add units check
        self.cost.initial = expr
        self.cost.units = units
        return self

    def path_cost(self, expr, units):
        self.cost.path = expr
        self.cost.units = units
        return self

    def terminal_cost(self, expr, units):
        self.cost.terminal = expr
        self.cost.units = units
        return self

    # TODO Rename cost
    def set_cost(self, initial=None, path=None, terminal=None, units=None):
        self.cost = CostStruct(initial=initial, path=path, terminal=terminal, units=units,
                               local_compiler=self.local_compiler)

    def scale(self, **kwargs):
        for name in kwargs.keys():
            self.units.append(NamedExpressionStruct(name, kwargs[name], local_compiler=self.local_compiler))
        return self

    """
    Sympify
    """
    def _sympify_struct(self, items: Union[Iterable, GenericStruct]):
        if isinstance(items, dict):
            for item in items.values():
                self._sympify_struct(item)
        elif isinstance(items, Iterable):
            for item in items:
                self._sympify_struct(item)
        elif hasattr(items, 'sympify_self'):
            items.sympify_self()
        elif items is None:
            pass
        else:
            raise RuntimeWarning('Tried to sympy {} which does not have method "sympify_self"'.format(items))

    def subs_struct(self, items: Union[Iterable, GenericStruct], old, new):
        if isinstance(items, dict):
            for item in items.values():
                self.subs_struct(item, old, new)
        elif isinstance(items, Iterable):
            for item in items:
                self.subs_struct(item, old, new)
        elif hasattr(items, 'subs_self'):
            items.subs_self(old, new)
        elif items is None:
            pass
        else:
            raise RuntimeWarning('Tried to sympy {} which does not have method "subs_self"'.format(items))

    def subs_all(self, old, new):
        if not self.sympified:
            self.sympify_self()

        _expr_structs = [
            self.states,
            self.costates,
            self.coparameters,
            self.controls,
            self.constraints,
            self.cost,
            self.quantities,
            self.custom_functions,
            self.tables,
            self.switches,
            self.hamiltonian,
            self.quads,
            self.symmetries,
            self.constants_of_motion,
            self.units,
        ]

        for struct in _expr_structs:
            self.subs_struct(struct, old, new)

        return self

    def sympify_self(self):
        """
        Sympifies the property structures that have components that cannont be symplified at initialization (i.e. eom
        for states because not all the symbols exist when inputed)
        :return: self
        """

        _sym_structs = [
            self.independent_variable,
            self.states,
            self.costates,
            self.parameters,
            self.coparameters,
            self.controls,
            self.constraints,
            self.constraint_parameters,
            self.constraint_adjoints,
            self.cost,
            self.constants,
            self.quantities,
            self.custom_functions,
            self.tables,
            self.switches,
            self.hamiltonian,
            self.quads,
            self.symmetries,
            self.constants_of_motion,
            self.units,
        ]

        for struct in _sym_structs:
            self._sympify_struct(struct)

        self.sympified = True
        return self

    def map_sol(self, sol, inverse=False):
        if inverse:
            for sol_map in reversed(self.sol_map_chain):
                sol = sol_map.inv_map(sol)
        else:
            for sol_map in self.sol_map_chain:
                sol = sol_map.map(sol)

        return sol

    def inv_map_sol(self, sol):
        return self.map_sol(sol, inverse=True)

    def map_sol_set(self, inverse=False):
        new_solutions = []
        for cont_set in self.solution_set.solutions:
            new_cont_set = []
            for sol in cont_set:
                new_cont_set.append(self.map_sol(sol, inverse=inverse))
            new_solutions.append(new_cont_set)
        self.solution_set.solutions = new_solutions

        return self.solution_set

    def inv_map_sol_set(self):
        return self.map_sol_set(inverse=True)
