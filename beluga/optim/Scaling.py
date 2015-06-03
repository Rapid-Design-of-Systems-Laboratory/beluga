import numbers as num# Avoid clashing with Number in sympy

from sympy import *
# from sympy.utilities.lambdify import lambdastr
from beluga.utils import fix_carets, sympify2
class Scaling(dict):
    def __init__(self):
        self.units = {}
        self.scale_func = {}
        self.problem_data = {}

    """Defines scaling for a set of units"""
    def unit(self,unit_str,unit_scale):
        """Adds scaling factor for a given unit
        Allows method chaining
        """
        self.units[unit_str] = unit_scale
        return self

    def initialize(self, nec_cond):
        """Initializes the scaling process"""
        self.scale_val = {}
        self.problem_data = nec_cond.problem_data

        for unit,scale in self.units.items():
            pass
            # if isinstance(scale,num.Number):
            #     scale_func[unit] =
                # Custom scaling factor
            # print((unit,scale,isinstance(scale,num.Number)))

        # Generate scaling functions for states, costates
        # constants, constraints, lagrange multipliers

        problem = nec_cond.problem

        # Convert units to symbols
        units_sym = symbols(list(self.units))

        # Growing list TODO: Put inside utils
        # Make sympify2 ?

        # TODO: Automate the following sections

        # Scaling functions for constants
        self.scale_func['constants'] = {}
        for const in problem.constants():
            self.scale_func['constants'][str(const)] = lambdify(units_sym,sympify2(const.unit))

        self.scale_func['states'] = {}
        self.scale_func['costates'] = {}

        cost_used = [key for (key,val) in problem.cost.items() if val.expr is not '0']

        if len(cost_used) < 1:
            raise ValueError('At least one cost function must be specified as nonzero!')

        cost_unit = problem.cost[cost_used[0]].unit

        # Scaling function for the independent variable
        self.scale_func['independent_var'] = lambdify(units_sym,sympify2(problem.indep_var().unit))

        # Scaling functions for states & costates
        self.scale_func['states'] = {}
        for state in problem.states():
            self.scale_func['states'][str(state)] = lambdify(units_sym,sympify2(state.unit))

            costate = state.make_costate();
            costate_scale = '('+cost_unit+')/('+state.unit+')'
            self.scale_func['costates'][costate] = lambdify(units_sym,sympify2(costate_scale))

        # Scaling functions for constraint multipliers
        self.scale_func['multipliers'] = {}
        indices = {}
        for c in problem.constraints():
            if c.type not in indices:
                indices[c.type] = 1 # initialize multiplier index

            mul_var  = c.make_multiplier(indices[c.type])
            mul_unit = '('+cost_unit+')/('+c.unit+')'
            self.scale_func['multipliers'][mul_var] = lambdify(units_sym, sympify2(mul_unit))
            indices[c.type] += 1 # increment multiplier index

    def compute_scaling(self,sol):
        self.scale_val = {}
        for unit,scale_factor in self.units.items():
            if isinstance(scale_factor,num.Number):
                # If scaling factor is a number, use it
                self.scale_val[unit] = scale_factor
            else:
                # If it is an expression, evaluate it

                # Setup environment to evaluate expression
                # Add list of states, costates and time and their peak values
                variables  = [(state,max(sol.y[idx,:]))
                                for idx,state in enumerate(self.problem_data['state_list'])]

                # Add auxiliary variables and their values (hopefully they dont clash)
                variables += [(var,sol.aux[aux['type']][var]) for aux in self.problem_data['aux_list'] for var in aux['vars']]
                var_dict = dict(variables)

                scale_expr = sympify2(scale_factor)

                # Evaluate expression to get scaling factor
                self.scale_val[unit] = scale_expr.subs(var_dict)
        print (self.scale_val)

    def scale(self,sol):
        """Scales a solution object"""
        pass

    def unscale(self,sol):
        """Unscales a solution object"""
        pass
