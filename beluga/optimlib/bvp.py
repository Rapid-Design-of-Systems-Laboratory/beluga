import sympy


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
