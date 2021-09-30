import logging
from typing import Iterable, Union

from .problem_components import GenericStruct, DimensionalExpressionStruct, NamedDimensionalStruct, Constant, \
    DynamicStruct, NamedExpressionStruct, NamedDimensionalExpressionStruct, CostStruct, FunctionStruct, \
    TableStruct, SwitchStruct, SymmetryStruct, InequalityConstraintStruct


class ComponentStruct:
    def __init__(self):
        pass


class InputOCP:
    def __init__(self, name=None):

        if name is None:
            self.name = 'beluga_problem'
        else:
            self.name = name

        self.independent_variable = None

        self.states = []
        self.parameters = []
        self.controls = []

        self.equality_constraints = {'initial': [], 'path': [], 'terminal': []}
        self.inequality_constraints = {'initial': [], 'path': [], 'control': [], 'terminal': []}
        self.constraint_parameters = []

        self.cost = CostStruct()

        self.constants = []
        self.quantities = []
        self.custom_functions = []
        self.tables = []
        self.switches = []

        self.quads = []
        self.symmetries = []
        self.constants_of_motion = []

        self.units = []

        self.aux = {}

    def set_independent(self, name, units):
        pass

    def add_state(self, name, eom, units):
        pass

    def add_control(self, name, units):
        pass

    def add_constant(self, name, default_value, units):
        pass

    def add_constraint(self, location, expr, u):
        pass

    def set_cost(self, initial, path, terminal):
        pass

    def add_unit(self, name, scale_expr):
        pass


