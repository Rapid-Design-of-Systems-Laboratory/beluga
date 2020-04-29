from collections import OrderedDict, Iterable
from copy import copy

import sympy
import numpy as np

from beluga.codegen import jit_compile_func, compile_control
from beluga import LocalCompiler
from beluga.optimlib.special_functions import custom_functions, tables


class Problem:
    def __init__(self, name=None, prob_type='input'):

        self.prob_type = prob_type
        self.name = name

        self.independent = {'name': None, 'units': None}
        self.states = []
        self.parameters = []
        self.constants = []
        self.quads = []
        self.constraint_parameters = {'initial': [], 'terminal': []}
        self.constraints = {'initial': [], 'terminal': []}
        self.quantities = []
        self.custom_functions = []
        self.tables = []
        self.switches = []

        self.algebraic_control_options = None
        self.control_options = []

        self.func_jac = {'df_dy': None, 'df_dp': None}
        self.bc_jac = {'initial': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None},
                       'terminal': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None}}

        self.symmetries = []

        self.units = []

        self.local_compiler = LocalCompiler()

        self.sympify = self.local_compiler.sympify
        self.lambdify = self.local_compiler.lambdify

        self.add_symbolic_local = self.local_compiler.add_symbolic_local
        self.add_function_local = self.local_compiler.add_function_local

