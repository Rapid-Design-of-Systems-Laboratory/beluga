import numbers as num# Avoid clashing with Number in sympy

from sympy import *
# from sympy.utilities.lambdify import lambdastr
from beluga.utils import fix_carets, sympify2, keyboard
class Scaling(dict):
    excluded_aux = ['function']

    def __init__(self):
        self.units = {}
        self.units_sym = []
        self.scale_func = {}
        self.problem_data = {}

    """Defines scaling for a set of units"""
    def unit(self,unit_str,unit_scale):
        """Adds scaling factor for a given unit
        Allows method chaining
        """
        self.units[unit_str] = unit_scale
        return self

    def initialize(self, problem, problem_data):
        """Initializes the scaling process"""
        self.problem_data = problem_data

        # Generate scaling functions for states, costates
        # constants, constraints, lagrange multipliers

        # Convert units to symbols
        self.units_sym = symbols(list(self.units))

        # Growing list TODO: Put inside utils
        # TODO: Automate the following sections

        # Scaling functions for constants
        # self.scale_func['const'] = {str(const): self.create_scale_fn(const.unit)
        #                             for const in problem.constants()}
        self.scale_func['const'] = {str(const): lambdify(self.units_sym,sympify2(const.unit))
                                    for const in problem.constants()}

        # Cost function used for scaling costates
        cost_used = [key for (key,val) in problem.cost.items() if val.expr is not '0']
        if len(cost_used) < 1:
            raise ValueError('At least one cost function must be specified as nonzero!')
        cost_unit = problem.cost[cost_used[0]].unit

        # Scaling functions for states & costates
        self.scale_func['states'] = {}
        self.scale_func['states'] = {str(state): self.create_scale_fn(state.unit)
                            for state in problem.states()}
        self.scale_func['states'].update({ state.make_costate():
                            self.create_scale_fn('('+cost_unit+')/('+state.unit+')')
                            for state in problem.states()})

        # Scaling function for the independent variable
        # TODO: Fix hardcoding
        # self.scale_func['independent_var'] = lambdify(units_sym,sympify2(problem.indep_var().unit))
        self.scale_func['states']['tf'] = self.create_scale_fn(problem.indep_var().unit)

        self.scale_func['initial'] = self.scale_func['states']
        self.scale_func['terminal'] = self.scale_func['states']

        # Scaling functions for constraint multipliers and other parameters
        self.scale_func['parameters'] = {}
        indices = {}
        for c in problem.constraints():
            if c.type not in indices:
                indices[c.type] = 1 # initialize multiplier index

            mul_var  = c.make_multiplier(indices[c.type])
            mul_unit = '('+cost_unit+')/('+c.unit+')'
            self.scale_func['parameters'][mul_var] = self.create_scale_fn(mul_unit)
            indices[c.type] += 1 # increment multiplier index

    def create_scale_fn(self,unit_expr):
        return lambdify(self.units_sym,sympify2(unit_expr))

    def compute_base_scaling(self,bvp,sol,scale_expr):
        if isinstance(scale_expr,num.Number):
            # If scaling factor is a number, use it
            return scale_expr
        else:
            # If it is an expression, evaluate it
            # Setup environment to evaluate expression
            # Add list of states, costates and time and their peak values
            variables  = [(state,max(abs(sol.y[idx,:])))
                            for idx,state in enumerate(self.problem_data['state_list'])]

            # Add auxiliary variables and their values (hopefully they dont clash)
            variables += [(var,bvp.aux_vars[aux['type']][var])
                            for aux in self.problem_data['aux_list']
                            for var in aux['vars']
                            if aux['type'] not in Scaling.excluded_aux]
            var_dict = dict(variables)

            # Evaluate expression to get scaling factor
            return float(sympify2(scale_expr).subs(var_dict,dtype=float).evalf())

    def compute_scaling(self,bvp,sol):
        from collections import OrderedDict
        # Units should be stored in order to be used as function arguments
        self.scale_factors = OrderedDict()
        # Evaluate scaling factors for each base unit
        for (unit,scale_expr) in self.units.items():
            self.scale_factors[unit] = self.compute_base_scaling(bvp,sol,scale_expr)

        # Ordered list of unit scaling factors for use as function parameters

        scale_factor_list = [v for (k,v) in self.scale_factors.items()]

        # Find scaling factors for each entity in problem
        self.scale_vals = {}
        # Dictionary comprehension version -- remove for lack of readability
        # self.scale_vals = {var_type:
        #                     var_funcs(*self.scale_factors)
        #                     if callable(var_funcs)
        #                     else {
        #                         var_name: var_func(*scale_factor_list)
        #                         for var_name,var_func in var_funcs.items()
        #                     }
        #                     for var_type,var_funcs in self.scale_func.items() }

        for var_type,var_funcs in self.scale_func.items():
            # If there are no sub items, use the scale factor directly
            if callable(var_funcs):
                self.scale_vals[var_type] = var_funcs(*scale_factor_list)
            else:
                # Else call scaling function for each sub item
                self.scale_vals[var_type] = {}
                for var_name,var_func in var_funcs.items():
                    self.scale_vals[var_type][var_name] = var_func(*scale_factor_list)


    def scale(self,bvp_aux_vars,sol):
        """Scales a boundary value problem"""

        # Additional aux entries for initial and terminal BCs
        extras = [{'type':'initial','vars':self.problem_data['state_list']},
                  {'type':'terminal','vars':self.problem_data['state_list']}]

        # Scale the states and costates
        for idx,state in enumerate(self.problem_data['state_list']):
            sol.y[idx,:] /= self.scale_vals['states'][state]

        # Scale auxiliary variables
        for aux in (self.problem_data['aux_list']+extras):
            if aux['type'] not in Scaling.excluded_aux:
                for var in aux['vars']:
                    bvp_aux_vars[aux['type']][var] /= self.scale_vals[aux['type']][var]

        # Scale parameters
        for idx, param in enumerate(self.problem_data['parameter_list']):
            sol.parameters[idx] /= self.scale_vals['parameters'][param]

    def unscale(self,bvp_aux_vars,sol):
        """Unscales a solution object"""
        # Additional aux entries for initial and terminal BCs
        extras = [{'type':'initial','vars':self.problem_data['state_list']},
                  {'type':'terminal','vars':self.problem_data['state_list']}]

        # Scale the states and costates
        for idx,state in enumerate(self.problem_data['state_list']):
            sol.y[idx,:] *= self.scale_vals['states'][state]

        # Scale auxiliary variables
        for aux in (self.problem_data['aux_list']+extras):
            if aux['type'] not in Scaling.excluded_aux:
                for var in aux['vars']:
                    bvp_aux_vars[aux['type']][var] *= self.scale_vals[aux['type']][var]

        # Scale parameters
        for idx, param in enumerate(self.problem_data['parameter_list']):
            sol.parameters[idx] *= self.scale_vals['parameters'][param]
