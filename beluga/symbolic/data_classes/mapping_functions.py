from __future__ import annotations
import types

import numpy as np
import sympy
import copy
import logging

from beluga.utils import recursive_sub
from beluga.symbolic.data_classes.symbolic_problem import Problem
from beluga.symbolic.data_classes.components_structures \
    import (extract_syms, combine_component_lists, getattr_from_list, sym_one, sym_zero, NamedDimensionalStruct,
            DynamicStruct, DimensionalExpressionStruct, NamedDimensionalExpressionStruct, SymmetryStruct)
from beluga.symbolic.differential_geometry \
    import make_standard_symplectic_form, make_hamiltonian_vector_field, noether, is_symplectic
from beluga.numeric.data_classes.trajectory_mappers \
    import (MomentumShiftMapper, EpsTrigMapper, IdentityMapper, DualizeMapper, AlgebraicControlMapper, MF,
            DifferentialControlMapper, DifferentialControlMapperDiffyG, SquashToBVPMapper, NormalizeTimeMapper)
from beluga.numeric.data_classes.NumericProblem import NumericProblem


"""
Functors
"""

class GenericFunctor(object):
    strrep = 'Id'

    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], GenericFunctor):
            obj = GenericFunctor()
            obj.data = args[0].data
            obj.strrep = args[0].strrep
            obj.transformation = args[0].transformation
            obj._right = args[0]._right
            return obj
        
        obj = super(GenericFunctor, cls).__new__(cls)
        obj.data = None
        obj._right = None
        return obj
    
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.data = args[0]
        
        self.kwargs = kwargs
    
    def set_transformation(self, transformation):
        self.transformation = types.MethodType(transformation, self)
    
    def transformation(self, prob: Problem) -> Problem:
        return prob
    
    def __lshift__(self, other: GenericFunctor) -> GenericFunctor:
        """
        Composition operator.
        """
        return self*other
    
    def __mul__(self, other: GenericFunctor) -> GenericFunctor:
        """
        Composition operator.
        """

        obj = GenericFunctor(self)
        if obj._right is not None:
            obj._right = self._right*other
        else:
            obj._right = other
        
        return obj
    
    def __pow__(self, other: int):
        if isinstance(other, int):
            if other < 0:
                raise ValueError('operand type(s) ** or pow() for GenericFunctor only support positive integers')
            if other == 0:
                return GenericFunctor()
            
            obj = GenericFunctor()
            for _ in range(other):
                obj *= self
            return obj
        
        else:
            raise TypeError('unsupported operand type(s) for ** or pow(): \'GenericFunctor\' and \'' + str(type(other).__name__) + '\'')
    
    def __rshift__(self, other: GenericFunctor) -> GenericFunctor:
        """
        Bind operator.
        """
        return other*self

    def __repr__(self):
        if self._right is not None:
            out = self.strrep + ' . ' + str(self._right)
        else:
            out = self.strrep
        
        return out

    def __call__(self, prob: Problem) -> Problem:
        if self._right is not None:
            prob = self._right(prob)
        
        return self.transformation(prob)


class Sympify(GenericFunctor):
    """
    Sympifies a problem.
    """
    strrep = 'Sympify'

    def transformation(self, prob: Problem):
        prob.sympify_self()
        return prob


class ApplyQuantities(GenericFunctor):
    strrep = 'ApplyQuantities'

    def transformation(self, prob: Problem):
        if not prob.sympified:
            raise ValueError('Problem must be sympified.')

        # TODO Find a more elegant solution to this
        for quantity_i in prob.quantities:
            for quantity_j in prob.quantities:
                if quantity_i.sym in quantity_j.free_symbols:
                    quantity_j.subs_self(quantity_i.sym, quantity_i.expr)

        for quantity in prob.quantities:
            prob.subs_all(quantity.sym, quantity.expr)
        
        # TODO add quantity calculation to Trajectory class
        
        return prob


class MomentumShift(GenericFunctor):
    strrep = 'MomentumShift'

    def __init__(self, new_ind_name=None):
        self.data = new_ind_name
    
    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')

        ind_var = prob.independent_variable
        new_state = DynamicStruct(
            ind_var.name, sympy.Integer(1), ind_var.units, local_compiler=prob.local_compiler).sympify_self()
        prob.states.append(new_state)

        if self.data is None:
            data = '_' + prob.independent_variable.name
        else:
            data = self.data

        prob.independent_variable = NamedDimensionalStruct(data, ind_var.units,
                                                        local_compiler=prob.local_compiler)
        prob.independent_variable.sympify_self()

        for symmetry in prob.symmetries:
            symmetry.field = np.append(symmetry.field, sympy.Integer(0))

        independent_symmetry = True
        for state in prob.states:
            if state.eom.diff(new_state.sym) != 0:
                independent_symmetry = False

        if independent_symmetry:
            prob.symmetries.append(
                SymmetryStruct([sympy.Integer(0)] * (len(prob.states) - 1) + [sympy.Integer(1)], new_state.units,
                            remove=True, local_compiler=prob.local_compiler))

        # Set solution mapper
        ind_state_idx = len(prob.states) - 1
        prob.sol_map_chain.append(MomentumShiftMapper(ind_state_idx=ind_state_idx))

        return prob


class EpsTrig(GenericFunctor):
    strrep = 'EpsTrig'

    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')

        for constraint_idx, _constraint in enumerate(prob.constraints['path']):
            if _constraint.method.lower() == 'epstrig':
                constraint = prob.constraints['path'].pop(constraint_idx)
                break
        else:
            raise RuntimeWarning('No path constraint using epstrig method found\nReturning problem unchanged')
            # return prob

        control_syms = [control.sym for control in prob.controls]
        if constraint.expr in control_syms:
            control_idx = control_syms.index(constraint.expr)
            new_control_name = '_' + str(constraint.expr) + '_trig'
            new_control = \
                NamedDimensionalStruct(new_control_name, '1', local_compiler=prob.local_compiler).sympify_self()
            prob.controls[control_idx] = new_control

        else:
            raise NotImplementedError('Epsilon-Trig must be used with pure control-constraints.')

        prob.cost.path += -constraint.activator * (sympy.cos(new_control.sym))

        prob.subs_all(constraint.expr, (constraint.upper - constraint.lower) / 2 * sympy.sin(new_control.sym)
                    + (constraint.upper + constraint.lower) / 2)

        # TODO Rewrite mapper
        prob.sol_map_chain.append(EpsTrigMapper(control_idx, constraint.lower, constraint.upper,
                                                prob.independent_variable.sym,
                                                np.array([state.sym for state in prob.states]),
                                                np.array([parameter.sym for parameter in prob.parameters]),
                                                np.array([constant.sym for constant in prob.constants]),
                                                local_compiler=prob.local_compiler))

        return prob


class UTM(GenericFunctor):
    strrep = 'UTM'

    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')
        
        location = -1

        for constraint_idx, constraint in enumerate(prob.constraints['initial']):
            if constraint.method.lower() == 'utm' and (constraint.lower is not None and constraint.upper is not None):
                location = 0
                break
        
        if location == -1:
            for constraint_idx, constraint in enumerate(prob.constraints['path']):
                if constraint.method.lower() == 'utm' and (constraint.lower is not None and constraint.upper is not None):
                    location = 1
                    break
        
        if location == -1:
            for constraint_idx, constraint in enumerate(prob.constraints['terminal']):
                if constraint.method.lower() == 'utm' and (constraint.lower is not None and constraint.upper is not None):
                    location = 2
                    break

        if location == -1:
            raise RuntimeWarning('No path constraint using utm method found\nReturning problem unchanged')
            # return prob

        activator_units = None
        for constant in prob.constants:
            if constraint.activator == constant.sym:
                activator_units = constant.units

        if activator_units is None:
            raise Exception('Activator \'' + str(constraint['activator']) + '\' not found in constants.')

        expr, activator, upper, lower = constraint.expr, constraint.activator, constraint.upper, constraint.lower

        if location == 0:
            prob.cost.initial += activator * (1 / (sympy.cos(sympy.pi / 2 * (2 * expr - upper - lower) / (upper - lower))) - 1)
        
        if location == 1:
            prob.cost.path += activator * (1 / (sympy.cos(sympy.pi / 2 * (2 * expr - upper - lower) / (upper - lower))) - 1)
        
        if location == 2:
            prob.cost.terminal += activator * (1 / (sympy.cos(sympy.pi / 2 * (2 * expr - upper - lower) / (upper - lower))) - 1)

        prob.sol_map_chain.append(IdentityMapper())

        if location == 0:
            prob.constraints['initial'].pop(constraint_idx)
        
        if location == 1:
            prob.constraints['path'].pop(constraint_idx)
        
        if location == 2:
            prob.constraints['terminal'].pop(constraint_idx)

        return prob


class RASHS(GenericFunctor):
    strrep = 'RASHS'

    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')

        for switch in prob.switches:
            prob.subs_all(switch.sym, switch.sym_func)

        return prob


class Dualize(GenericFunctor):
    strrep = 'Dualize'

    def __init__(self, method='traditional'):
        self.method = method
    
    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')

        ocp = copy.deepcopy(prob)

        for idx, constraint in enumerate(prob.constraints['initial']):
            nu_name = '_nu_0_{}'.format(idx)
            nu = NamedDimensionalStruct(
                nu_name, prob.cost.units / constraint.units, local_compiler=prob.local_compiler).sympify_self()
            prob.constraint_adjoints.append(nu)
            prob.cost.initial += nu.sym * constraint.expr

        for idx, constraint in enumerate(prob.constraints['terminal']):
            nu_name = '_nu_f_{}'.format(idx)
            nu = NamedDimensionalStruct(
                nu_name, prob.cost.units / constraint.units, local_compiler=prob.local_compiler).sympify_self()
            prob.constraint_adjoints.append(nu)
            prob.cost.terminal += nu.sym * constraint.expr

        # Make costates TODO Check if quads need costates
        prob.hamiltonian = \
            DimensionalExpressionStruct(prob.cost.path, prob.cost.units
                                        / prob.independent_variable.units).sympify_self()
        for state in prob.states:
            lam_name = '_lam_{}'.format(state.name)
            lam = DynamicStruct(lam_name, '0', prob.cost.units / state.units,
                                local_compiler=prob.local_compiler).sympify_self()
            prob.costates.append(lam)
            prob.hamiltonian.expr += lam.sym * state.eom

        symmetry_costate_addition = np.array([sym_zero for _ in prob.costates])
        for idx, symmetry in enumerate(prob.symmetries):
            symmetry.field = np.concatenate((symmetry.field, symmetry_costate_addition))

        # Handle coparameters
        for parameter in prob.parameters:
            lam_name = '_lam_{}'.format(parameter.name)
            prob.coparameters.append(DynamicStruct(lam_name, '0', prob.cost.units / parameter.units))

        prob.constants_of_motion.append(
            NamedDimensionalExpressionStruct('hamiltonian', prob.hamiltonian.expr, prob.hamiltonian.units,
                                            local_compiler=prob.local_compiler).sympify_self())

        if self.method.lower() == 'traditional':
            for state, costate in zip(prob.states + prob.parameters, prob.costates + prob.coparameters):
                costate.eom = -prob.hamiltonian.expr.diff(state.sym)
        elif self.method.lower() == 'diffyg':
            state_syms = extract_syms(prob.states + prob.parameters)
            costate_syms = extract_syms(prob.costates + prob.coparameters)
            omega = make_standard_symplectic_form(state_syms, costate_syms)
            chi_h = make_hamiltonian_vector_field(prob.hamiltonian.expr, omega, state_syms + costate_syms)
            costate_rates = chi_h[-len(prob.states):]
            for costate, rate in zip(prob.costates, costate_rates):
                costate.eom = rate
            prob.omega = omega

            for idx, symmetry in enumerate(prob.symmetries):
                g_star, units = noether(prob, symmetry)
                prob.constants_of_motion.append(NamedDimensionalExpressionStruct('com_{}'.format(idx), g_star, units))

        # Make costate constraints
        for state, costate in zip(prob.states + prob.parameters, prob.costates + prob.coparameters):
            constraint_expr = costate.sym + prob.cost.initial.diff(state.sym)
            prob.constraints['initial'].append(
                DimensionalExpressionStruct(constraint_expr, costate.units, local_compiler=prob.local_compiler))

            constraint_expr = costate.sym - prob.cost.terminal.diff(state.sym)
            prob.constraints['terminal'].append(
                DimensionalExpressionStruct(constraint_expr, costate.units, local_compiler=prob.local_compiler))

        # TODO: Check Placement of Hamiltonian Constraint Placement
        # Make time/Hamiltonian constraints
        # constraint_expr = prob.cost.initial.diff(prob.independent_variable.sym) - prob.hamiltonian.expr
        # prob.constraints['initial'].append(DimensionalExpressionStruct(
        #         constraint_expr, prob.hamiltonian.units, local_compiler=prob.local_compiler))

        constraint_expr = prob.cost.terminal.diff(prob.independent_variable.sym) + prob.hamiltonian.expr
        prob.constraints['terminal'].append(DimensionalExpressionStruct(
            constraint_expr, prob.hamiltonian.units, local_compiler=prob.local_compiler))

        prob.sol_map_chain.append(DualizeMapper(len(prob.costates), len(prob.constraint_adjoints), ocp))

        prob.dualized = True

        return prob


class AlgebraicControlLaw(GenericFunctor):
    strrep = 'AlgebraicControlLaw'

    def transformation(self, prob: Problem) -> Problem:
        if not prob.dualized:
            raise ValueError('Problem must be dualized.')

        control_syms = extract_syms(prob.controls)
        prob.dh_du = [prob.hamiltonian.expr.diff(control_sym) for control_sym in control_syms]
        logging.debug("Solving dH/du...")
        control_options = sympy.solve(prob.dh_du, control_syms, minimal=True, simplify=False)
        logging.debug('Control found')

        # TODO Use algebraic equations and custom functions in future
        prob.control_law = control_options

        prob.sol_map_chain.append(AlgebraicControlMapper(prob))

        prob.prob_type = 'prob'

        return prob


class DifferentialControlLaw(GenericFunctor):
    strrep = 'DifferentialControlLaw'

    def __init__(self, method='traditional'):
        self.method = method
    
    def transformation(self, prob: Problem) -> Problem:
        if not prob.dualized:
            raise ValueError('Problem must be dualized.')

        _dynamic_structs = [prob.states, prob.costates]

        state_syms = sympy.Matrix(extract_syms(combine_component_lists(_dynamic_structs)))
        control_syms = sympy.Matrix(extract_syms(prob.controls))
        eom = sympy.Matrix([state.eom for state in combine_component_lists(_dynamic_structs)])

        g = sympy.Matrix([prob.hamiltonian.expr.diff(u_k) for u_k in control_syms])

        dg_dx = g.jacobian(state_syms)
        dg_du = g.jacobian(control_syms)

        u_dot = dg_du.LUsolve(-dg_dx * eom)  # dg_du * u_dot + dg_dx * x_dot = 0
        if sympy.zoo in u_dot.atoms():
            raise NotImplementedError('Complex infinity in differential control law. Potential bang-bang solution.')

        for g_k, control in zip(g, prob.controls):
            constraint = DimensionalExpressionStruct(
                g_k, prob.hamiltonian.units / control.units, local_compiler=prob.local_compiler)
            prob.constraints['terminal'].append(constraint)

        control_idxs = []
        if self.method.lower() == 'traditional':
            for control_rate in u_dot:
                control = prob.controls.pop(0)
                control_idxs.append(len(prob.states))
                prob.states.append(DynamicStruct(control.name, control_rate, control.units,
                                                local_compiler=prob.local_compiler).sympify_self())

            prob.sol_map_chain.append(DifferentialControlMapper(control_idxs=control_idxs))

        elif self.method.lower() == 'diffyg':
            independent_index = len(prob.states) - 1
            control_costates = []
            for control, control_rate in zip(prob.controls, u_dot):
                control_idxs.append(len(prob.states))
                prob.states.append(DynamicStruct(control.name, control_rate, control.units,
                                                local_compiler=prob.local_compiler).sympify_self())
                lam_name = '_lam_{}'.format(control.name)
                lam = DynamicStruct(lam_name, '0', prob.cost.units / control.units,
                                    local_compiler=prob.local_compiler).sympify_self()
                prob.costates.append(lam)
                control_costates.append(lam)

            omega_new = make_standard_symplectic_form(prob.states, prob.costates)
            n_states = len(prob.states)
            n_controls = len(prob.controls)
            # Add (du - u' dt) ^ (dlamU - 0 dt) to omega
            for idx, u_dot_i in enumerate(u_dot):
                omega_new[int(n_states - n_controls + idx), int(2 * n_states - n_controls + idx)] = 1
                omega_new[int(2 * n_states - n_controls + idx), int(n_states - n_controls + idx)] = -1
                omega_new[independent_index, int(2 * n_states - n_controls + idx)] = -u_dot_i
                omega_new[int(2 * n_states - n_controls + idx), independent_index] = u_dot_i

            prob.omega = omega_new
            chi_h = make_hamiltonian_vector_field(prob.hamiltonian.expr, omega_new,
                                                extract_syms(prob.states + prob.costates))

            for idx, state in enumerate(prob.states + prob.costates):
                state.eom = chi_h[idx]

            for lam_u in control_costates:
                prob.constraints['initial'].append(
                    DimensionalExpressionStruct(lam_u.sym, lam_u.units, local_compiler=prob.local_compiler))

            prob.controls = []

            prob.sol_map_chain.append(DifferentialControlMapperDiffyG(control_idxs=control_idxs))

        else:
            raise NotImplementedError('Method {} not implemented for differential control'.format(self.method))

        prob.prob_type = 'prob'

        return prob


class MishchenkoFomenko(GenericFunctor):
    strrep = 'MishchenkoFomenko'

    def __init__(self, com_index):
        self.com_index = com_index
    
    def transformation(self, prob: Problem) -> Problem:
        if not is_symplectic(prob.omega):
            logging.warning('BVP is not symplectic. Skipping reduction.')
            return prob
        
        constant_of_motion = prob.constants_of_motion[self.com_index]

        state_syms = extract_syms(prob.states)
        costates_syms = extract_syms(prob.costates)
        parameter_syms = extract_syms(prob.parameters)
        constant_syms = extract_syms(prob.constants)

        fn_p = prob.lambdify([state_syms, costates_syms, parameter_syms, constant_syms], constant_of_motion.expr)

        states_and_costates = prob.states + prob.costates

        atoms = constant_of_motion.expr.atoms()
        atoms2 = set()
        for atom in atoms:
            if isinstance(atom, sympy.Symbol) and (atom not in {item.sym for item in prob.parameters + prob.constants}):
                atoms2.add(atom)

        atoms = atoms2

        solve_for_p = sympy.solve(constant_of_motion.expr - constant_of_motion.sym, atoms, dict=True, simplify=False)

        if len(solve_for_p) > 1:
            raise ValueError

        parameter_index, symmetry, replace_p = 0, 0, None
        for parameter in solve_for_p[0].keys():
            symmetry, symmetry_unit = noether(prob, constant_of_motion)
            replace_p = parameter
            for idx, state in enumerate(states_and_costates):
                if state.sym == parameter:
                    parameter_index = idx
                    prob.parameters.append(NamedDimensionalStruct(constant_of_motion.name, constant_of_motion.units))

        symmetry_index = parameter_index - len(prob.states)

        # Derive the quad
        # Evaluate int(pdq) = int(PdQ)
        n = len(prob.quads)
        symmetry_symbol = sympy.Symbol('_q_{}'.format(n))
        _lhs = constant_of_motion.expr/constant_of_motion.sym*symmetry
        lhs = 0
        for idx, state in enumerate(states_and_costates):
            lhs += sympy.integrate(_lhs[idx], state.sym)

        lhs, _ = recursive_sub(lhs, solve_for_p[0])

        state_syms = extract_syms(prob.states)
        costates_syms = extract_syms(prob.costates)
        parameter_syms = extract_syms(prob.parameters)
        constant_syms = extract_syms(prob.constants)

        # the_p = [constant_of_motion.sym]
        fn_q = prob.lambdify([state_syms, costates_syms, parameter_syms, constant_syms], lhs)

        replace_q = states_and_costates[symmetry_index].sym
        solve_for_q = sympy.solve(lhs - symmetry_symbol, replace_q, dict=True, simplify=False)

        # Evaluate X_H(pi(., c)), pi = O^sharp
        omega = prob.omega.tomatrix()
        rvec = sympy.Matrix(([0] * len(states_and_costates)))
        for ii, state_1 in enumerate(states_and_costates):
            for jj, state_2 in enumerate(states_and_costates):
                rvec[ii] += omega[ii, jj]*sympy.diff(constant_of_motion.expr, state_2.sym)

        symmetry_eom = sym_zero
        for idx, state in enumerate(states_and_costates):
            symmetry_eom += state.eom*rvec[idx]

        # TODO: Figure out how to find units of the quads. This is only works in some specialized cases.
        symmetry_unit = states_and_costates[symmetry_index].units

        prob.quads.append(
            DynamicStruct(str(symmetry_symbol), symmetry_eom, symmetry_unit, local_compiler=prob.local_compiler))

        for idx, state in enumerate(states_and_costates):
            state.eom, _ = recursive_sub(state.eom, solve_for_p[0])
            state.eom, _ = recursive_sub(state.eom, solve_for_q[0])

        for idx, bc in enumerate(prob.constraints['initial'] + prob.constraints['terminal']):
            bc.expr, _ = recursive_sub(bc.expr, solve_for_p[0])
            bc.expr, _ = recursive_sub(bc.expr, solve_for_q[0])

        for idx, law in enumerate(prob.control_law):
            for jj, symbol in enumerate(law.keys()):
                prob.control_law[idx][symbol], _ = recursive_sub(prob.sympify(law[symbol]), solve_for_p[0])
                # prob.control_law[idx][symbol] = law[symbol]
                prob.control_law[idx][symbol], _ = recursive_sub(prob.sympify(law[symbol]), solve_for_q[0])
                # prob.control_law[idx][symbol] = law[symbol]

        for idx, com in enumerate(prob.constants_of_motion):
            if idx != self.com_index:
                com.expr, _ = recursive_sub(com.expr, solve_for_p[0])
                com.expr, _ = recursive_sub(com.expr, solve_for_q[0])

        remove_parameter = states_and_costates[parameter_index]
        remove_symmetry = states_and_costates[symmetry_index]

        remove_parameter_dict = {'location': None, 'index': None}
        if remove_parameter in prob.states:
            remove_parameter_dict = {'location': 'states', 'index': prob.states.index(remove_parameter)}
            prob.states.remove(remove_parameter)
        if remove_parameter in prob.costates:
            remove_parameter_dict = {'location': 'costates', 'index': prob.costates.index(remove_parameter)}
            prob.costates.remove(remove_parameter)

        remove_symmetry_dict = {'location': None, 'index': None}
        if remove_symmetry in prob.states:
            remove_symmetry_dict = {'location': 'states', 'index': prob.states.index(remove_symmetry)}
            prob.states.remove(remove_symmetry)
        if remove_symmetry in prob.costates:
            remove_symmetry_dict = {'location': 'costates', 'index': prob.costates.index(remove_symmetry)}
            prob.costates.remove(remove_symmetry)

        omega = prob.omega.tomatrix()
        if parameter_index > symmetry_index:
            omega.row_del(parameter_index)
            omega.col_del(parameter_index)
            omega.row_del(symmetry_index)
            omega.col_del(symmetry_index)
        else:
            omega.row_del(symmetry_index)
            omega.col_del(symmetry_index)
            omega.row_del(parameter_index)
            omega.col_del(parameter_index)

        prob.omega = sympy.MutableDenseNDimArray(omega)

        del prob.constants_of_motion[self.com_index]

        state_syms = extract_syms(prob.states)
        costates_syms = extract_syms(prob.costates)
        parameter_syms = extract_syms(prob.parameters)
        constant_syms = extract_syms(prob.constants)
        quad_syms = extract_syms(prob.quads)

        fn_q_inv = prob.lambdify([state_syms, costates_syms, quad_syms, parameter_syms, constant_syms],
                                solve_for_q[0][replace_q])
        fn_p_inv = prob.lambdify([state_syms, costates_syms, parameter_syms, constant_syms], solve_for_p[0][replace_p])

        prob.sol_map_chain.append(MF(remove_parameter_dict, remove_symmetry_dict, fn_p, fn_q, fn_p_inv, fn_q_inv))

        return prob


class SquashToBVP(GenericFunctor):
    strrep = 'SquashToBVP'

    def transformation(self, prob: Problem):
        costate_idxs = slice(len(prob.states), len(prob.states) + len(prob.costates))
        prob.states += prob.costates
        prob.costates = []

        coparameter_idxs = slice(len(prob.quads), len(prob.quads) + len(prob.coparameters))
        prob.quads += prob.coparameters
        prob.coparameters = []

        prob.constraint_parameters += prob.constraint_adjoints
        constraint_adjoints_idxs = \
            slice(len(prob.constraint_parameters),
                len(prob.constraint_parameters) + len(prob.constraint_adjoints))
        prob.constraint_adjoints = []

        prob.sol_map_chain.append(SquashToBVPMapper(costate_idxs, coparameter_idxs, constraint_adjoints_idxs))

        prob.dualized = False

        return prob


class NormalizeTime(GenericFunctor):
    strrep = 'NormalizeTime'

    def __init__(self, new_ind_name=None):
        self.new_ind_name = new_ind_name

    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')

        delta_t_name = '_delta' + prob.independent_variable.name
        delta_t = NamedDimensionalStruct(delta_t_name, prob.independent_variable.units,
                                        local_compiler=prob.local_compiler).sympify_self()
        prob.parameters.append(delta_t)

        _dynamic_structs = [prob.states, prob.costates]

        for state in combine_component_lists(_dynamic_structs):
            state.eom = state.eom * delta_t.sym

        prob.cost.path *= delta_t.sym

        if self.new_ind_name is None:
            new_ind_name = '_tau'
        else:
            new_ind_name = self.new_ind_name
        
        prob.independent_variable = \
            NamedDimensionalStruct(new_ind_name, sym_one, local_compiler=prob.local_compiler).sympify_self()

        # Set solution mapper
        delta_t_idx = len(prob.parameters) - 1
        prob.sol_map_chain.append(NormalizeTimeMapper(delta_ind_idx=delta_t_idx))

        return prob


class IgnoreQuads(GenericFunctor):
    strrep = 'IgnoreQuads'

    def transformation(self, prob: Problem) -> Problem:
        prob.states += prob.quads
        prob.quads = []
        return prob


class ComputeAnalyticalJacobians(GenericFunctor):
    strrep ='ComputeAnalyticalJacobians'

    def transformation(self, prob: Problem) -> Problem:

        states = sympy.Matrix(extract_syms(prob.states))
        dynamic_parameters = sympy.Matrix(extract_syms(prob.parameters))
        parameters = sympy.Matrix(extract_syms(prob.parameters) + extract_syms(prob.constraint_parameters))
        quads = sympy.Matrix(extract_syms(prob.quads))
        eom = sympy.Matrix(getattr_from_list(prob.states, 'eom'))
        phi_0 = sympy.Matrix(getattr_from_list(prob.constraints['initial'], 'expr'))
        phi_f = sympy.Matrix(getattr_from_list(prob.constraints['terminal'], 'expr'))

        prob.func_jac['df_dy'] = eom.jacobian(states)
        prob.bc_jac['initial']['dbc_dy'] = phi_0.jacobian(states)
        prob.bc_jac['terminal']['dbc_dy'] = phi_f.jacobian(states)

        if len(parameters) > 0:
            prob.func_jac.update({'df_dp': eom.jacobian(dynamic_parameters)})
            prob.bc_jac['initial']['dbc_dp'] = phi_0.jacobian(parameters)
            prob.bc_jac['terminal']['dbc_dp'] = phi_f.jacobian(parameters)

        if len(quads) > 0:
            prob.bc_jac['initial']['dbc_dq'] = phi_0.jacobian(quads)
            prob.bc_jac['terminal']['dbc_dq'] = phi_f.jacobian(quads)

        return prob


class CompileProblem(GenericFunctor):
    strrep = 'CompileProblem'

    def __init__(self, use_control_arg=False):
        self.use_control_arg = use_control_arg

    def transformation(self, prob: Problem) -> Problem:
        if not prob.sympified:
            raise ValueError('Problem must be sympified. Hint: did you preprocess the problem?')

        prob.functional_problem = NumericProblem(prob, local_compiler=prob.local_compiler)

        prob.functional_problem.compile_problem(use_control_arg=self.use_control_arg)
        prob.lambdified = True

        return prob


"""
Helper macro functions
"""

def make_postprocessor() -> GenericFunctor:
    """
    Processes a BVP or OCP after it has been formulated.

    Presently just compiles functions into something that can be rapidly evaluated.
    """
    return CompileProblem()

def make_preprocessor() -> GenericFunctor:
    """
    Processes a newly made OCP.

    Turns strings into symbols and performs subsitutions on quantities.
    """
    return ApplyQuantities()*Sympify()

def make_direct_method(prob: Problem, analytical_jacobian=True, reduction=False,
                   do_momentum_shift=False, do_normalize_time=False):
    functor = GenericFunctor()

    """
    Make time a state.
    """
    if do_momentum_shift:
        functor >>= MomentumShift()

    """
    Deal with inequality constraints
    """

    for constraint in copy.copy(prob.constraints['initial'] + prob.constraints['path']
                                + prob.constraints['terminal']):
        if (constraint.lower is not None and constraint.upper is not None):
            if constraint.method.lower() == 'epstrig':
                functor >>= EpsTrig()
            elif constraint.method.lower() == 'utm':
                functor >>= UTM()
            else:
                raise NotImplementedError(
                    'Unknown path constraint method \"' + str(constraint.method) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(prob.switches) > 0:
        functor >>= RASHS()

    """
    Scale eom to final time
    """
    if do_normalize_time:
        functor >>= NormalizeTime()

    """
    Reduce if needed
    """
    # TODO: Make nonsymplectic reduction strategies
    # if is_symplectic(prob.omega) and reduction:
    #     while len(prob.constants_of_motion) > 1:
    #         mf(prob, 1)

    # elif not is_symplectic(prob.omega) and reduction:
    #     logging.warning('BVP is not symplectic. Skipping reduction.')

    """
    Form analytical jacobians
    """
    if analytical_jacobian:
        functor >>= ComputeAnalyticalJacobians()

    return functor


def make_indirect_method(prob: Problem, analytical_jacobian=False, control_method='differential', method='traditional',
                     reduction=False, do_momentum_shift=True, do_normalize_time=True) -> GenericFunctor:
    """
    Pieces together individual functors and tools to create a full indirect method.
    """

    RFfunctor = GenericFunctor()

    """
    Make time a state.
    """
    if do_momentum_shift:
        RFfunctor >>= MomentumShift()

    """
    Deal with inequality constraints
    """
    
    for constraint in copy.copy(prob.constraints['initial'] + prob.constraints['path']
                                + prob.constraints['terminal']):
        if (constraint.lower is not None and constraint.upper is not None):
            if constraint.method.lower() == 'epstrig':
                RFfunctor >>= EpsTrig()
            elif constraint.method.lower() == 'utm':
                RFfunctor >>= UTM()
            else:
                raise NotImplementedError(
                    'Unknown path constraint method \"' + str(constraint.method) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(prob.switches) > 0:
        RFfunctor >>= RASHS()

    """
    Dualize Problem
    """

    RFfunctor >>= Dualize(method=method)

    """
    Form Control Law
    """
    if control_method.lower() == 'algebraic':
        RFfunctor >>= AlgebraicControlLaw()
    elif control_method.lower() == 'differential':
        RFfunctor >>= DifferentialControlLaw(method=method)
    elif control_method.lower() == 'numeric':
        raise NotImplementedError('Numerical control method not yet implemented')
    else:
        raise NotImplementedError('{} control method not implemented. Try differential or algebraic')

    """
    Scale eom to final time
    """
    if do_normalize_time:
        RFfunctor >>= NormalizeTime()

    """
    Reduce if needed
    """

    if method.lower() == 'diffyg' and reduction:
        n_reductions = len(prob.symmetries) + len(prob.constants_of_motion)
        RFfunctor >>= MishchenkoFomenko(1)**(n_reductions)

    """
    Squash dual problem to normal BVP
    """

    RFfunctor >>= SquashToBVP()

    """
    Form analytical jacobians
    """
    if analytical_jacobian:
        if control_method == 'algebraic':
            logging.info('Analytical Jacobians not available for algebraic control mode')
        else:
            RFfunctor >>= ComputeAnalyticalJacobians()

    return RFfunctor
