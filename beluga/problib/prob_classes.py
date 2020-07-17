from .component_structs import *
from beluga.problib.traj_classes import *
# from beluga.optimlib.functional_maps.sol_maps import *
from beluga.optimlib.optimlib import make_standard_symplectic_form, make_hamiltonian_vector_field, noether

import sympy
import numpy as np

from beluga.codegen import jit_compile_func, compile_control
from ..codegen import LocalCompiler
from typing import Iterable, List
import copy


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
        self.constraints['initial'].append(DimensionalExpressionStruct(expr, units))
        return self

    def path_constraint(self, expr, units, lower, upper, activator, method='utm'):
        self.constraints['path'].append(
            PathConstraintStruct(expr, units, lower, upper, activator,
                                 method=method, local_compiler=self.local_compiler))
        return self

    def terminal_constraint(self, expr, units):
        self.constraints['terminal'].append(DimensionalExpressionStruct(expr, units))
        return self

    def constraint_parameter(self, name, units):
        self.constraint_parameters.append(DimensionalStruct(name, units))
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

    def _subs_struct(self, items: Union[Iterable, GenericStruct], old, new):
        if isinstance(items, dict):
            for item in items.values():
                self._subs_struct(item, old, new)
        elif isinstance(items, Iterable):
            for item in items:
                self._subs_struct(item, old, new)
        elif hasattr(items, 'subs_self'):
            items.subs_self(old, new)
        elif items is None:
            pass
        else:
            raise RuntimeWarning('Tried to sympy {} which does not have method "subs_self"'.format(items))

    def _subs_all(self, old, new):
        self._ensure_sympified()

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
            self._subs_struct(struct, old, new)

        return self

    @staticmethod
    def extract_syms(structs: Union[List[NamedStruct], NamedStruct]):
        if isinstance(structs, Iterable):
            return [struct.sym for struct in structs]
        elif hasattr(structs, 'sym'):
            return [structs.sym]
        else:
            raise RuntimeError('{} has no attribute "sym"'.format(structs))

    @staticmethod
    def getattr_from_list(structs: List[NamedStruct], attr: str):
        if isinstance(structs, Iterable):
            return [getattr(struct, attr) for struct in structs]
        elif hasattr(structs, attr):
            return [getattr(structs, attr)]
        else:
            raise RuntimeError('{} has no attribute "{}"'.format(structs, attr))

    @staticmethod
    def _combined_lists(items):
        out = []
        if isinstance(items, Iterable):
            for item in items:
                out += Problem._combined_lists(item)
        else:
            out.append(items)

        return out

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

    def _ensure_sympified(self):
        if not self.sympified:
            self.sympify_self()

    def _ensure_dualized(self):
        if not self.dualized:
            self.dualize()

    """
    Functional Maps    
    """
    def apply_quantities(self):
        self._ensure_sympified()

        # TODO Find a more elegant solution to this
        for quantity_i in self.quantities:
            for quantity_j in self.quantities:
                if quantity_i.sym in quantity_j.free_symbols:
                    quantity_j.subs_self(quantity_i.sym, quantity_i.expr)

        for quantity in self.quantities:
            self._subs_all(quantity.sym, quantity.expr)

        # TODO add quantity calculation to Trajectory class

    def momentum_shift(self, new_ind_name=None):

        self._ensure_sympified()

        ind_var = self.independent_variable
        new_state = DynamicStruct(
            ind_var.name, sympy.Integer(1), ind_var.units, local_compiler=self.local_compiler).sympify_self()
        self.states.append(new_state)

        if new_ind_name is None:
            new_ind_name = '_' + self.independent_variable.name

        self.independent_variable = NamedDimensionalStruct(new_ind_name, ind_var.units,
                                                           local_compiler=self.local_compiler)
        self.independent_variable.sympify_self()

        for symmetry in self.symmetries:
            symmetry['field'].append(sympy.Integer(0))

        independent_symmetry = True
        for state in self.states:
            if state.eom.diff(new_state.sym) != 0:
                independent_symmetry = False

        if independent_symmetry:
            self.symmetries.append(
                SymmetryStruct([sympy.Integer(0)] * (len(self.states) - 1) + [sympy.Integer(1)], new_state.units,
                               remove=True, local_compiler=self.local_compiler))

        # Set solution mapper
        ind_state_idx = len(self.states) - 1
        self.sol_map_chain.append(MomentumShiftMapper(ind_state_idx=ind_state_idx))

        return self

    def epstrig(self):
        self._ensure_sympified()

        for constraint_idx, _constraint in enumerate(self.constraints['path']):
            if _constraint.method.lower() == 'epstrig':
                constraint = self.constraints['path'].pop(constraint_idx)
                break
        else:
            raise RuntimeWarning('No path constraint using epstrig method found\nReturning problem unchanged')
            # return self

        control_syms = [control.sym for control in self.controls]
        if constraint.expr in control_syms:
            control_idx = control_syms.index(constraint.expr)
            new_control_name = '_' + str(constraint.expr) + '_trig'
            new_control = \
                NamedDimensionalStruct(new_control_name, '1', local_compiler=self.local_compiler).sympify_self()
            self.controls[control_idx] = new_control

        else:
            raise NotImplementedError('Epsilon-Trig must be used with pure control-constraints.')

        self.cost.path += -constraint.activator*(sympy.cos(new_control.sym))

        self._subs_all(constraint.expr, (constraint.upper - constraint.lower) / 2 * sympy.sin(new_control.sym)
                       + (constraint.upper + constraint.lower) / 2)

        # TODO Rewrite mapper
        self.sol_map_chain.append(EpsTrigMapper(control_idx, constraint.lower, constraint.upper,
                                                self.independent_variable.sym,
                                                np.array([state.sym for state in self.states]),
                                                np.array([parameter.sym for parameter in self.parameters]),
                                                np.array([constant.sym for constant in self.constants]),
                                                local_compiler=self.local_compiler))

        return self

    def utm(self):
        self._ensure_sympified()

        for constraint_idx, constraint in enumerate(self.constraints['path']):
            if constraint.method.lower() == 'utm':
                break
        else:
            raise RuntimeWarning('No path constraint using utm method found\nReturning problem unchanged')
            # return self

        activator_units = None
        for constant in self.constants:
            if constraint.activator == constant.sym:
                activator_units = constant.units

        if activator_units is None:
            raise Exception('Activator \'' + str(constraint['activator']) + '\' not found in constants.')

        expr, activator, upper, lower = constraint.expr, constraint.activator, constraint.upper, constraint.lower
        self.cost.path += activator*(1/(sympy.cos(sympy.pi/2*(2*expr - upper - lower) / (upper - lower))) - 1)

        self.sol_map_chain.append(IdentityMapper())

        self.constraints['path'].pop(constraint_idx)

        return self

    def rashs(self):
        self._ensure_sympified()

        for switch in self.switches:
            self._subs_all(switch.sym, switch.sym_func)

        return self

    def dualize(self, method='traditional'):
        self._ensure_sympified()

        location_suffix_dict = {'initial': '0', 'terminal': 'f'}

        for location in location_suffix_dict.keys():
            for idx, constraint in enumerate(self.constraints[location]):
                loc_subscript = location_suffix_dict[location]
                nu_name = '_nu_{}_{}'.format(loc_subscript, idx)
                nu = NamedDimensionalStruct(
                    nu_name, self.cost.units / constraint.units, local_compiler=self.local_compiler).sympify_self()
                self.constraint_adjoints.append(nu)
                self.cost.initial += nu.sym*constraint.expr

        # Make costates TODO Check if quads need costates
        self.hamiltonian = \
            DimensionalExpressionStruct(self.cost.path, self.cost.units
                                        / self.independent_variable.units).sympify_self()
        for state in self.states:
            lam_name = '_lam_{}'.format(state.name)
            lam = DynamicStruct(lam_name, '0', self.cost.units/state.units,
                                local_compiler=self.local_compiler).sympify_self()
            self.costates.append(lam)
            self.hamiltonian.expr += lam.sym * state.eom

        # Handle coparameters
        for parameter in self.parameters:
            lam_name = '_lam_{}'.format(parameter.name)
            self.coparameters.append(DynamicStruct(lam_name, '0', self.cost.units/parameter.units))

        self.constants_of_motion.append(
            NamedDimensionalExpressionStruct('hamiltonian', self.hamiltonian.expr, self.hamiltonian.units,
                                             local_compiler=self.local_compiler).sympify_self())

        if method.lower() == 'traditional':
            for state, costate in zip(self.states + self.parameters, self.costates + self.coparameters):
                costate.eom = -self.hamiltonian.expr.diff(state.sym)
        elif method.lower() == 'diffyg':
            state_syms = self.extract_syms(self.states + self.parameters)
            costate_syms = self.extract_syms(self.costates + self.coparameters)
            omega = make_standard_symplectic_form(state_syms, costate_syms)
            x_h = make_hamiltonian_vector_field(self.hamiltonian.expr, omega, state_syms + costate_syms, sympy.diff)
            costate_rates = x_h[-len(self.states):]
            for costate, rate in zip(self.costates, costate_rates):
                costate.eom = rate
            self.omega = omega

            for idx, symmetry in enumerate(self.symmetries):
                g_star, units = noether(self, symmetry)
                self.constants_of_motion.append(NamedDimensionalExpressionStruct('com_{}'.format(idx), g_star,  units))

        # Make costate constraints
        for location in ['initial', 'terminal']:
            for state, costate in zip(self.states + self.parameters, self.costates + self.coparameters):
                constraint_expr = costate.sym + self.cost.__getattribute__(location).diff(state.sym)
                self.constraints[location].append(
                    DimensionalExpressionStruct(constraint_expr, costate.units, local_compiler=self.local_compiler))

        # Make time/Hamiltonian constraints
            constraint_expr = self.cost.__getattribute__(location).diff(self.independent_variable.sym)
            self.constraints[location].append(DimensionalExpressionStruct(
                constraint_expr, self.hamiltonian.units, local_compiler=self.local_compiler))

        self.sol_map_chain.append(DualizeMapper())

        self.dualized = True

        return self

    def algebraic_control_law(self):

        self._ensure_dualized()

        # control_syms = [control['sym'] for control in prob.controls]
        control_syms = self.extract_syms(self.controls)
        self.dh_du = [self.hamiltonian.expr.diff(control_sym) for control_sym in control_syms]
        logging.debug("Solving dH/du...")
        control_options = sympy.solve(self.dh_du, control_syms,  minimal=True, simplify=True)
        logging.debug('Control found')

        # TODO Use algebraic equations and custom functions in future
        self.control_law = control_options

        self.sol_map_chain.append(AlgebraicControlMapper(self))

        self.prob_type = 'bvp'

        return self

    def differential_control_law(self, method='traditional'):

        self._ensure_dualized()

        _dynamic_structs = [self.states, self.costates]

        state_syms = sympy.Matrix(self.extract_syms(self._combined_lists(_dynamic_structs)))
        control_syms = sympy.Matrix(self.extract_syms(self.controls))
        eom = sympy.Matrix([state.eom for state in self._combined_lists(_dynamic_structs)])

        g = sympy.Matrix([self.hamiltonian.expr.diff(u_k) for u_k in control_syms])

        dg_dx = g.jacobian(state_syms)
        dg_du = g.jacobian(control_syms)

        u_dot = dg_du.LUsolve(-dg_dx * eom)  # dg_du * u_dot + dg_dx * x_dot = 0
        if sympy.zoo in u_dot.atoms():
            raise NotImplementedError('Complex infinity in differential control law. Potential bang-bang solution.')

        for g_k, control in zip(g, self.controls):
            constraint = DimensionalExpressionStruct(
                g_k, self.hamiltonian.units/control.units, local_compiler=self.local_compiler)
            self.constraints['terminal'].append(constraint)

        control_idxs = []
        if method == 'traditional':
            for control_rate in u_dot:
                control = self.controls.pop(0)
                control_idxs.append(len(self.states))
                self.states.append(DynamicStruct(control.name, control_rate, control.units,
                                                 local_compiler=self.local_compiler).sympify_self())
        elif method == 'diffyg':
            # TODO: Finsih this when you know what's up
            raise NotImplementedError('Need to reimplement diffyg')
        else:
            raise NotImplementedError('Method {} not implemented for differential control'.format(method))

        self.sol_map_chain.append(DifferentialControlMapper(control_idxs=control_idxs))

        self.prob_type = 'bvp'

        return self

    def mf(self, com_index=0):
        constant_of_motion = self.constants_of_motion[com_index]

        state_syms = self.getattr_from_list(self.states, 'sym')
        parameter_syms = self.getattr_from_list(self.parameters, 'sym')
        constant_syms = self.getattr_from_list(self.constants, 'sym')

    def squash_to_bvp(self):

        costate_idxs = slice(len(self.states), len(self.states) + len(self.costates))
        self.states += self.costates
        self.costates = []

        coparameter_idxs = slice(len(self.quads), len(self.quads) + len(self.coparameters))
        self.quads += self.coparameters
        self.coparameters = []

        self.constraint_parameters += self.constraint_adjoints
        constraint_adjoints_idxs = \
            slice(len(self.constraint_parameters),
                  len(self.constraint_parameters) + len(self.constraint_adjoints))
        self.constraint_adjoints = []

        self.sol_map_chain.append(SquashToBVPMapper(costate_idxs, coparameter_idxs, constraint_adjoints_idxs))

        self.dualized = False

        return self

    def normalize_time(self, new_ind_name=None):
        self._ensure_sympified()

        delta_t_name = '_delta' + self.independent_variable.name
        delta_t = NamedDimensionalStruct(delta_t_name, self.independent_variable.units,
                                         local_compiler=self.local_compiler).sympify_self()
        self.parameters.append(delta_t)

        _dynamic_structs = [self.states, self.costates]

        for state in self._combined_lists(_dynamic_structs):
            state.eom = state.eom * delta_t.sym

        self.cost.path *= delta_t.sym

        if new_ind_name is None:
            new_ind_name = '_tau'
        self.independent_variable = \
            NamedDimensionalStruct(new_ind_name, sym_one, local_compiler=self.local_compiler).sympify_self()

        # Set solution mapper
        delta_t_idx = len(self.parameters) - 1
        self.sol_map_chain.append(NormalizeTimeMapper(delta_ind_idx=delta_t_idx))

        return self

    def ignore_quads(self):
        self.states += self.quads
        self.quads = []

        return self

    def compute_analytical_jacobians(self):

        states = sympy.Matrix(self.extract_syms(self.states))
        parameters = sympy.Matrix(self.extract_syms(self.parameters))
        quads = sympy.Matrix(self.extract_syms(self.quads))
        eom = sympy.Matrix(self.getattr_from_list(self.states, 'eom'))
        phi_0 = sympy.Matrix(self.getattr_from_list(self.constraints['initial'], 'expr'))
        phi_f = sympy.Matrix(self.getattr_from_list(self.constraints['terminal'], 'expr'))

        self.func_jac['df_dy'] = eom.jacobian(states)
        self.bc_jac['initial']['dbc_dy'] = phi_0.jacobian(states)
        self.bc_jac['terminal']['dbc_dy'] = phi_f.jacobian(states)

        if len(parameters) > 0:
            self.func_jac.update({'df_dp': eom.jacobian(parameters)})
            self.bc_jac['initial']['dbc_dp'] = phi_0.jacobian(parameters)
            self.bc_jac['terminal']['dbc_dp'] = phi_f.jacobian(parameters)

        if len(quads) > 0:
            self.bc_jac['initial']['dbc_dq'] = phi_0.jacobian(quads)
            self.bc_jac['terminal']['dbc_dq'] = phi_f.jacobian(quads)

        return self

    def compile_direct(self, analytical_jacobian=False, reduction=False,
                       do_momentum_shift=False, do_normalize_time=False):
        self._ensure_sympified()

        """
        Substitute Quantities
        """
        self.apply_quantities()

        """
        Make time a state.
        """
        if do_momentum_shift:
            self.momentum_shift()

        """
        Deal with path constraints
        """
        for path_constraint in copy.copy(self.constraints['path']):
            if path_constraint.method.lower() == 'epstrig':
                self.epstrig()
            elif path_constraint.method.lower() == 'utm':
                self.utm()
            else:
                raise NotImplementedError(
                    'Unknown path constraint method \"' + str(path_constraint.method) + '\"')

        """
        Deal with staging, switches, and their substitutions.
        """
        if len(self.switches) > 0:
            self.rashs()

        """
        Scale eom to final time
        """
        if do_normalize_time:
            self.normalize_time()

        """
        Reduce if needed
        """
        # TODO Implement MF
        if reduction:
            pass

        """
        Ignore quads (until the bvp solver gets better)
        """
        self.ignore_quads()

        """
        Form analytical jacobians
        """
        if analytical_jacobian:
            self.compute_analytical_jacobians()

        self.compile_problem()

    def compile_indirect(self, analytical_jacobian=False, control_method='differential', method='traditional',
                         reduction=False, do_momentum_shift=False, do_normalize_time=False):

        self._ensure_sympified()

        """
        Substitute Quantities
        """
        self.apply_quantities()

        """
        Make time a state.
        """
        if do_momentum_shift:
            self.momentum_shift()

        """
        Deal with path constraints
        """
        for path_constraint in copy.copy(self.constraints['path']):
            if path_constraint.method.lower() == 'epstrig':
                self.epstrig()
            elif path_constraint.method.lower() == 'utm':
                self.utm()
            else:
                raise NotImplementedError(
                    'Unknown path constraint method \"' + str(path_constraint.method) + '\"')

        """
        Deal with staging, switches, and their substitutions.
        """
        if len(self.switches) > 0:
            self.rashs()

        """
        Dualize Problem
        """
        self.dualize(method=method)

        """
        Form Control Law
        """
        if control_method.lower() == 'algebraic':
            self.algebraic_control_law()
        elif control_method.lower() == 'differential':
            self.differential_control_law(method=method)
        elif control_method.lower() == 'numerical':
            raise NotImplementedError('Numerical control method not yet implemented')
        else:
            raise NotImplementedError('{} control method not implemented. Try differential or algebraic')

        """
        Scale eom to final time
        """
        if do_normalize_time:
            self.normalize_time()

        """
        Reduce if needed
        """
        # TODO Implement MF
        if reduction:
            pass

        """
        Ignore quads (until the bvp solver gets better)
        """
        self.ignore_quads()

        """
        Squash dual problem to normal BVP
        """
        self.squash_to_bvp()

        """
        Form analytical jacobians
        """
        if analytical_jacobian:
            if control_method == 'algebraic':
                pass
            else:
                self.compute_analytical_jacobians()

        self.compile_problem()

        return self

    def compile_problem(self, use_control_arg=False):
        self._ensure_sympified()

        if self.functional_problem is None:
            self.functional_problem = FuncProblem(self, local_compiler=self.local_compiler)

        self.functional_problem.compile_problem(use_control_arg=use_control_arg)
        self.lambdified = True

        return self

    def map_sol(self, sol, inverse=False):
        for sol_map in self.sol_map_chain:
            if inverse:
                sol = sol_map.inv_map(sol)
            else:
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


class FuncProblem:
    def __init__(self, prob, local_compiler=None):

        if local_compiler is None:
            self.local_compiler = LocalCompiler()
        else:
            self.local_compiler = local_compiler

        self.lambdify = self.local_compiler.lambdify

        self.prob = prob

        self.ham_func = None
        self.compute_u = None
        self.compute_y_dot = None
        self.compute_q_dot = None

        self.deriv_func = None
        self.quad_func = None
        self.deriv_func_jac = None

        self.compute_initial_bc = None
        self.compute_terminal_bc = None

        self.bc_func = None
        self.bc_func_jac = None

        self.initial_cost_func, self.path_cost_func, self.terminal_cost_func = None, None, None
        self.ineq_constraints = None

        self._state_syms = []
        self._control_syms = []
        self._parameter_syms = []
        self._constraint_parameters_syms = []
        self._constant_syms = []

        self._dynamic_args = []
        self._dynamic_args_w_controls = []

        self._bc_args = []
        self._bc_args_w_quads = []

        self._initialized = False

    def _initialize(self):

        self._state_syms = self.prob.extract_syms(self.prob.states)
        self._control_syms = self.prob.extract_syms(self.prob.controls)
        self._parameter_syms = self.prob.extract_syms(self.prob.parameters)
        self._constant_syms = self.prob.extract_syms(self.prob.constants)

        self._quad_syms = self.prob.extract_syms(self.prob.quads)
        self._constraint_parameters_syms = self.prob.extract_syms(self.prob.constraint_parameters)

        self._dynamic_args = \
            [self.prob.independent_variable.sym, self._state_syms, self._parameter_syms, self._constant_syms]
        self._dynamic_args_w_controls = \
            [self.prob.independent_variable.sym, self._state_syms, self._control_syms,
             self._parameter_syms, self._constant_syms]

        self._bc_args = \
            [self.prob.independent_variable.sym, self._state_syms, self._parameter_syms,
             self._constraint_parameters_syms, self._constant_syms]
        self._bc_args_w_quads = \
            [self.prob.independent_variable.sym, self._state_syms, self._quad_syms, self._parameter_syms,
             self._constraint_parameters_syms, self._constant_syms]

        self._initialized = True

    def compile_problem(self, use_time_arg=False, use_control_arg=False, use_quad_arg=False):

        self._initialize()

        if hasattr(self.prob.hamiltonian, 'expr'):
            self.ham_func = self.lambdify(self._dynamic_args_w_controls, self.prob.hamiltonian.expr)

        self.compile_control()
        self.compile_deriv_func(use_control_arg=use_control_arg)

        self.compile_bc(use_quad_arg=use_quad_arg)

        self.compile_cost(use_quad_arg=use_quad_arg, use_control_arg=use_control_arg)

        return self

    def compile_control(self):

        self.compute_u = compile_control(self.prob.control_law, self._dynamic_args, self.ham_func, self.lambdify)

        return self.compute_u

    def compile_deriv_func(self, use_control_arg=False):
        sym_eom = self.prob.getattr_from_list(self.prob.states, 'eom')
        sym_eom_q = self.prob.getattr_from_list(self.prob.quads, 'eom')

        if self.compute_u is None:
            if use_control_arg:
                _args = self._dynamic_args_w_controls
            else:
                _args = self._dynamic_args

            self.compute_y_dot = self.lambdify(_args, sym_eom)
            self.compute_q_dot = self.lambdify(_args, sym_eom_q)

            self.deriv_func, self.quad_func = self.compute_y_dot, self.compute_q_dot

        else:
            self.compute_y_dot = self.lambdify(self._dynamic_args_w_controls, sym_eom)
            self.compute_q_dot = self.lambdify(self._dynamic_args_w_controls, sym_eom_q)

            compute_u = self.compute_u
            compute_y_dot = self.compute_y_dot
            compute_q_dot = self.compute_q_dot

            def deriv_func(_t, _y, _p, _k):
                _u = compute_u(_t, _y, _p, _k)
                return np.array(compute_y_dot(_t, _y, _u, _p, _k))

            def quad_func(_t, _y, _p, _k):
                _u = compute_u(_t, _y, _p, _k)
                return np.array(compute_q_dot(_t, _y, _u, _p, _k))

            self.deriv_func = jit_compile_func(deriv_func, self._dynamic_args)
            self.quad_func = jit_compile_func(quad_func, self._dynamic_args)

        return self.deriv_func, self.quad_func

    def compile_bc(self, use_quad_arg=False):

        sym_initial_bc = self.prob.getattr_from_list(self.prob.constraints['initial'], 'expr')
        sym_terminal_bc = self.prob.getattr_from_list(self.prob.constraints['terminal'], 'expr')

        if use_quad_arg:
            _args = self._bc_args_w_quads

            compute_initial_bc = self.lambdify(_args, sym_initial_bc)
            compute_terminal_bc = self.lambdify(_args, sym_terminal_bc)

            def bc_func(_t0, _y0, _q0, _tf, _yf, _qf, _p, _p_con, _k):
                bc_0 = np.array(compute_initial_bc(_t0, _y0, _q0, _p, _p_con, _k))
                bc_f = np.array(compute_terminal_bc(_tf, _yf, _qf, _p, _p_con, _k))
                return np.concatenate((bc_0, bc_f))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms + self._quad_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms
            self.bc_func = jit_compile_func(bc_func, _combined_args)
            self.compute_initial_bc, self.compute_terminal_bc = compute_initial_bc, compute_terminal_bc

        else:
            _args = self._bc_args

            compute_initial_bc = self.lambdify(_args, sym_initial_bc)
            compute_terminal_bc = self.lambdify(_args, sym_terminal_bc)

            def bc_func(_t0, _y0, _tf, _yf, _p, _p_con, _k):
                bc_0 = np.array(compute_initial_bc(_t0, _y0, _p, _p_con, _k))
                bc_f = np.array(compute_terminal_bc(_tf, _yf, _p, _p_con, _k))
                return np.concatenate((bc_0, bc_f))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms

            self.bc_func = jit_compile_func(bc_func, _combined_args)
            self.compute_initial_bc, self.compute_terminal_bc = compute_initial_bc, compute_terminal_bc

        return self.bc_func

    def compile_deriv_jac_func(self, use_control_arg=False):

        if any([item is None for item in self.prob.func_jac.items()]):
            return None

        elif use_control_arg:
            df_dy = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dy'])
            df_dp = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dp'])

            def deriv_func_jac(_t, _y, _u, _p, _k):
                return np.array(df_dy(_t, _y, _u, _p, _k)), np.array(df_dp(_t, _y, _u, _p, _k))

            self.deriv_func_jac = jit_compile_func(deriv_func_jac, self._dynamic_args_w_controls,
                                                   func_name='deriv_func_jac')

        elif self.compute_u is not None:
            df_dy = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dy'])
            df_dp = self.lambdify(self._dynamic_args_w_controls, self.prob.func_jac['df_dp'])

            compute_u = self.compute_u

            def deriv_func_jac(_t, _y, _p, _k):
                _u = compute_u(_t, _y, _p, _k)
                return np.array(df_dy(_t, _y, _u, _p, _k)), np.array(df_dp(_t, _y, _u, _p, _k))

            self.deriv_func_jac = jit_compile_func(deriv_func_jac, self._dynamic_args,
                                                   func_name='deriv_func_jac')

        else:
            df_dy = self.lambdify(self._dynamic_args, self.prob.func_jac['df_dy'])
            df_dp = self.lambdify(self._dynamic_args, self.prob.func_jac['df_dp'])

            def deriv_func_jac(_t, _y, _p, _k):
                return np.array(df_dy(_t, _y, _p, _k)), np.array(df_dp(_t, _y, _p, _k))

            self.deriv_func_jac = jit_compile_func(deriv_func_jac, self._dynamic_args,
                                                   func_name='deriv_func_jac')

        return self.deriv_func_jac

    def compile_bc_jac_func(self, use_quad_arg=False):

        if all([item is None
                for item in list(self.prob.bc_jac['initial'].values()) + list(self.prob.bc_jac['terminal'].values())]):
            return None

        elif use_quad_arg:
            _args = self._bc_args_w_quads

        else:
            _args = self._bc_args

        dbc_0_dy = self.lambdify(_args, self.prob.bc_jac['initial']['dbc_dy'])
        dbc_f_dy = self.lambdify(_args, self.prob.bc_jac['terminal']['dbc_dp'])
        dbc_0_dp = self.lambdify(_args, self.prob.bc_jac['initial']['dbc_dy'])
        dbc_f_dp = self.lambdify(_args, self.prob.bc_jac['terminal']['dbc_dp'])

        if use_quad_arg:
            dbc_0_dq = self.lambdify(_args, self.prob.bc_jac['initial']['dbc_dq'])
            dbc_f_dq = self.lambdify(_args, self.prob.bc_jac['terminal']['dbc_dq'])

            def bc_func_jac(_t0, _y0, _q0, _tf, _yf, _qf, _p, _p_con, _k):
                return np.array(dbc_0_dy(_t0, _y0, _q0, _p, _p_con, _k)), \
                       np.array(dbc_f_dy(_tf, _yf, _qf, _p, _p_con, _k)), \
                       np.array(dbc_0_dq(_t0, _y0, _q0, _p, _p_con, _k)), \
                       np.array(dbc_f_dq(_tf, _yf, _qf, _p, _p_con, _k)), \
                       (np.array(dbc_0_dp(_t0, _y0, _q0, _p, _p_con, _k))
                        + np.array(dbc_f_dp(_tf, _yf, _qf, _p, _p_con, _k)))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms + self._quad_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms

        else:
            def bc_func_jac(_t0, _y0, _tf, _yf, _p, _p_con, _k):
                return np.array(dbc_0_dy(_t0, _y0, _p, _p_con, _k)), \
                       np.array(dbc_f_dy(_tf, _yf, _p, _p_con, _k)), \
                       (np.array(dbc_0_dp(_t0, _y0, _p, _p_con, _k))
                        + np.array(dbc_f_dp(_tf, _yf, _p, _p_con, _k)))

            _combined_args = \
                ([self.prob.independent_variable.sym] + self._state_syms) * 2 \
                + self._parameter_syms + self._constraint_parameters_syms + self._constant_syms

        self.bc_func_jac = jit_compile_func(bc_func_jac, _combined_args, func_name='bc_func_jac')

        return self.bc_func_jac

    def compile_cost(self, use_quad_arg=False, use_control_arg=False):

        if use_quad_arg:
            _bc_args = self._bc_args_w_quads
        else:
            _bc_args = self._bc_args

        self.initial_cost_func = self.lambdify(_bc_args, self.prob.cost.initial)

        self.terminal_cost_func = self.lambdify(_bc_args, self.prob.cost.terminal)

        if self.compute_u is None:
            if use_control_arg:
                _dyn_args = self._dynamic_args_w_controls
            else:
                _dyn_args = self._dynamic_args

            self.path_cost_func = self.lambdify(_dyn_args, self.prob.cost.path)

        else:
            _compute_u = self.compute_u
            _compute_path_cost = self.lambdify(self._dynamic_args_w_controls, self.prob.cost.path)

            def path_cost_func(_t, _y, _p, _k):
                _u = _compute_u(_t, _y, _p, _k)
                return np.array(_compute_path_cost(_t, _y, _u, _p, _k))

            self.path_cost_func = jit_compile_func(path_cost_func, self._dynamic_args)

        return self.initial_cost_func, self.path_cost_func, self.terminal_cost_func


