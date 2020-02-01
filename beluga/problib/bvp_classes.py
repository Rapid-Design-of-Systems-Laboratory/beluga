from .base_classes import BaseProblem, BaseInput, BaseFunc, BaseSym


class BaseBVP(BaseProblem):
    def __init__(self, name=None):
        BaseProblem.__init__(name=name)

        self.costates = []
        self.coparameters = []
        self.constraint_multipliers = []

        self.algebraic_equations = []
        self.constants_of_motion = []

        self.hamiltonian = None

        self.func_jac = {'df_dy': None, 'df_dp': None}
        self.bc_jac = {'initial': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None},
                       'terminal': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None}}


class InputBVP(BaseInput, BaseBVP):
    def __init__(self, name=None):

        BaseInput.__init__(self, name=name)
        BaseBVP.__init__(self, name=name)

        self.problem_type = 'InputBVP'

    def costate(self, name, eom, units, tol=None):
        self.costates.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def coparameter(self, name, eom, units, tol=None):
        self.coparameters.append({'name': name, 'eom': eom, 'units': units, 'tol': tol})
        return self

    def constraint_multiplier(self, name, units):
        self.constraint_multipliers.append({'name': name, 'units': units})
        return self

    def algebraic_equation(self, name, expr, units):
        self.algebraic_equations.append({'name': name, 'expr': expr, 'units': units})
        return self

    def constant_of_motion(self, name, expr, units):
        self.constants_of_motion.append({'name': name, 'expr': expr, 'units': units})
        return self

    def set_hamiltonian(self, expr, units):
        self.hamiltonian = {'expr': expr, 'units': units}
        self.constants_of_motion.append({'name': 'hamiltonian', 'expr': expr, 'units': units})
        return self

    def set_func_jac_expr(self, kind, expr):
        self.func_jac[kind] = expr
        return self

    def set_bc_jac_expr(self, location, kind, expr):
        self.bc_jac[location][kind] = expr
        return self

    def sympify_vars(self, sym_prob):
        BaseInput.sympify_vars(self, sym_prob)

        # Costates
        for costate in sym_prob.costates:
            self.sympify_name(costate)

        # Coparmeters
        for coparameter in sym_prob.coparameters:
            self.sympify_name(coparameter)

        # Constraint Multipliers
        for constraint_multiplier in sym_prob.constraint_multipliers:
            self.sympify_name(constraint_multiplier)

        # Algebraic Equations
        for algebraic_equation in sym_prob.algebraic_equations:
            self.sympify_name(algebraic_equation)

        # Constants of Motion
        for constant_of_motion in sym_prob.constants_of_motion:
            self.sympify_name(constant_of_motion)

    @staticmethod
    def sympify_units(sym_prob):
        BaseInput.sympify_units(sym_prob)

        # Costates
        for costate in sym_prob.costates:
            costate['units'] = sym_prob.sympify(costate['units'])

        # Coparameters
        for coparameter in sym_prob.costates:
            coparameter['units'] = sym_prob.sympify(coparameter['units'])

        # Constraint Multipliers
        for constraint_multiplier in sym_prob.constraint_multipliers:
            constraint_multiplier['units'] = sym_prob.sympify(constraint_multiplier['units'])

        # Algebraic Equations
        for algebraic_equation in sym_prob.algebraic_equations:
            algebraic_equation['units'] = sym_prob.sympify(algebraic_equation['units'])

        # Constants of Motion
        for constant_of_motion in sym_prob.constants_of_motion:
            constant_of_motion['units'] = sym_prob.sympify(constant_of_motion['units'])

        # Cost
        sym_prob.hamiltonian['units'] = sym_prob.sympify(sym_prob.hamiltonian['units'])

    @staticmethod
    def sympify_exprs(sym_prob):
        BaseInput.sympify_exprs(sym_prob)

        # Costates
        for costate in sym_prob.costates:
            costate['eom'] = sym_prob.sympify(costate['eom'])

        # Coparameters
        for coparameter in sym_prob.costates:
            coparameter['eom'] = sym_prob.sympify(coparameter['eom'])

        # Algebraic Equations
        for algebraic_equation in sym_prob.algebraic_equations:
            algebraic_equation['expr'] = sym_prob.sympify(algebraic_equation['expr'])

        # Constants of Motion
        for constant_of_motion in sym_prob.constants_of_motion:
            constant_of_motion['expr'] = sym_prob.sympify(constant_of_motion['expr'])

        # Cost
        sym_prob.hamiltonian['units'] = sym_prob.sympify(sym_prob.hamiltonian['units'])

    def sympify_problem(self, sym_prob=None):

        if sym_prob is None:
            sym_prob = SymBVP()

        BaseInput.sympify_problem(self, sym_prob=sym_prob)
        return sym_prob


class SymBVP(BaseInput, BaseBVP):
    def __init__(self, name=None):
        BaseInput.__init__(self, name=name)
        BaseBVP.__init__(self, name=name)

        self.problem_type = 'SymBVP'
        self.omega = None


class FuncBVP(BaseBVP):
    pass


class BVP:
    def __init__(self):
        self.name = None
        self.root_ocp = None
        self.mappings = []

        self.independent_variable = None
        self.state_list = []
        self.costate_list = []
        self.constant_list = []
        self.parameter_list = []
        self.coparameter_list = []
        self.quantity_list = []
        self.lagrange_multipliers = []
        self.constraint_dict = {'initial': [], 'terminal': []}
        self.symmetry_list = []
        self.custom_function_list = []
        self.table_list = []
        self.units = []

        self.sympified_exprs = False
        self.locals_dict = dict()
        self.mod_dict = dict()

        self.constants_of_motion = []

        self.algebraic_equations = []

        self.hamiltonian = None
        self.omega = None

        self.func_jac = {'df_dy': None, 'df_dp': None}
        self.bc_jac = {'initial': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None},
                       'terminal': {'dbc_dy': None, 'dbc_dp': None, 'dbc_dq': None}}
