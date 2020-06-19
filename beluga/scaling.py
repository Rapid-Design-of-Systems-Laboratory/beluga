from collections import OrderedDict
import copy
import numbers as num
from sympy import *
from beluga.utils import sympify


class Scaling(dict):
    excluded_aux = ['function']

    def __init__(self):

        dict.__init__(self)

        self.units = {}
        self.units_sym = []
        self.scale_func = {}
        self.problem_data = {}
        self.scale_factors = None
        self.scale_vals = {}

    """Defines scaling for a set of units"""
    def unit(self, unit_str, unit_scale):
        """Adds scaling factor for a given unit
        Allows method chaining
        """
        self.units[unit_str] = unit_scale
        return self

    def initialize(self, ws):
        """Initializes the scaling process.

        Parameters
        ----------
        ws - dict
            Workspace processed by OCP workflow
        """
        self.problem_data = ws

        # Generate scaling functions for states, costates
        # constants, constraints, lagrange multipliers

        # Convert units to symbols
        self.units_sym = symbols(list(self.units))

        # Growing list TODO: Put inside utils
        # TODO: Automate the following sections

        # Scaling functions for constants
        self.scale_func['const'] = {str(s['symbol']): s['unit'] for s in ws.get_constants()}

        # Scaling functions for states & quads
        self.scale_func['states'] = {}
        self.scale_func['states'] = {str(s['symbol']): s['unit'] for s in ws.states()}
        self.scale_func['quads'] = {str(s['symbol']): s['unit'] for s in ws.quads()}

        self.scale_func['initial'] = self.scale_func['states']
        self.scale_func['terminal'] = self.scale_func['states']

        # Scaling functions for constraint multipliers and other parameters
        self.scale_func['parameters'] = {str(s['symbol']): s['unit'] for s in ws.parameters()}
        self.scale_func['parameters'].update({str(s['symbol']): s['unit'] for s in ws.nd_parameters()})

    def create_scale_fn(self, unit_expr):
        return lambdify(self.units_sym, sympify(unit_expr))

    def compute_base_scaling(self, sol, scale_expr):
        if isinstance(scale_expr, num.Number):
            # If scaling factor is a number, use it
            return scale_expr
        else:
            variables = [(const_name, const_val) for (const_name, const_val) in zip(self.problem_data['constants'], self.problem_data['constants_values'])]
            # Have to do in this order to override state values with arrays
            variables += [(state, max(abs(sol.y[:, idx]))) for idx, state in enumerate(self.problem_data['states'])]
            variables += [(quad, max(abs(sol.q[:, idx]))) for idx, quad in enumerate(self.problem_data['quads'])]

            var_dict = dict(variables)

            # Evaluate expression to get scaling factor
            return float(sympify(scale_expr).subs_self(var_dict, dtype=float).evalf())

    def compute_scaling(self, sol):
        # Units should be stored in order to be used as function arguments
        self.scale_factors = OrderedDict()
        # Evaluate scaling factors for each base unit
        for (unit, scale_expr) in self.units.items():
            self.scale_factors[unit] = self.compute_base_scaling(sol, scale_expr)

        # Ordered list of unit scaling factors for use as function parameters
        scale_factor_list = [v for (k, v) in self.scale_factors.items()]

        # Find scaling factors for each entity in problem
        self.scale_vals = {}

        for var_type, var_funcs in self.scale_func.items():
            # If there are no sub items, use the scale factor directly
            if callable(var_funcs):
                self.scale_vals[var_type] = var_funcs(*scale_factor_list)
            else:
                # Else call scaling function for each sub item
                self.scale_vals[var_type] = {}
                for var_name, var_func in var_funcs.items():
                    self.scale_vals[var_type][var_name] = var_func(*scale_factor_list)

    def scale(self, sol):
        """Scales a BVP solution"""
        solout = copy.deepcopy(sol)

        # Scale the states and costates
        for idx, state in enumerate(self.problem_data['states']):
            solout.y[:, idx] /= self.scale_vals['states'][state]

        for idx, quad in enumerate(self.problem_data['quads']):
            solout.q[:, idx] /= self.scale_vals['quads'][quad]

        # Scale auxiliary variables
        for idx, const in enumerate(self.problem_data['consts']):
            solout.const[idx] /= self.scale_vals['const'][const]

        # for aux in (self.problem_data['aux_list']):
        #     if aux['type'] not in Scaling.excluded_aux:
        #         for var_ in aux['vars']:
        #             solout.aux[aux['type']][var_] /= self.scale_vals[aux['type']][var_]

        # Scale parameters
        for idx, param in enumerate([str(p) for p in self.problem_data['dynamical_parameters']]):
            solout.p[idx] /= self.scale_vals['parameters'][param]

        for idx, param in enumerate([str(p) for p in self.problem_data['nondynamical_parameters']]):
            solout.nondynamical_parameters[idx] /= self.scale_vals['parameters'][param]

        return solout

    def unscale(self, sol):
        """ Unscales a solution object"""
        solout = copy.deepcopy(sol)

        # Scale the states and costates
        for idx, state in enumerate(self.problem_data['states']):
            solout.y[:, idx] *= self.scale_vals['states'][state]

        for idx, quad in enumerate(self.problem_data['quads']):
            solout.q[:, idx] *= self.scale_vals['quads'][quad]

        # Scale auxiliary variables
        for idx, const in enumerate(self.problem_data['consts']):
            solout.const[idx] *= self.scale_vals['const'][const]
        # for aux in (self.problem_data['aux_list']):
        #     if aux['type'] not in Scaling.excluded_aux:
        #         for var_ in aux['vars']:
        #             solout.aux[aux['type']][var_] *= self.scale_vals[aux['type']][var_]

        # Scale parameters
        for idx, param in enumerate([str(p) for p in self.problem_data['dynamical_parameters']]):
            solout.p[idx] *= self.scale_vals['parameters'][param]

        for idx, param in enumerate([str(p) for p in self.problem_data['nondynamical_parameters']]):
            solout.nondynamical_parameters[idx] *= self.scale_vals['parameters'][param]

        return solout
