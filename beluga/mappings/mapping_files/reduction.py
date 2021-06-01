import numpy as np
import sympy

from beluga.utils.logging import logger
from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.trajectory import Trajectory
from beluga.data_classes.problem_components import extract_syms, sym_zero, DynamicStruct, NamedDimensionalStruct
from beluga.symbolic.differential_geometry.differential_geometry import noether, is_symplectic
from beluga.utils.helper_functions import recursive_sub
from beluga.mappings.trajectory_mapper import TrajectoryMapper, TrajectoryMapperList


class MFMapper(TrajectoryMapper):
    def __init__(self, remove_parameter_dict, remove_symmetry_dict, fn_p, fn_q, fn_p_inv, fn_q_inv):
        super(MFMapper, self).__init__()

        self.remove_parameter_dict = remove_parameter_dict
        self.remove_symmetry_dict = remove_symmetry_dict

        self.fn_p = fn_p
        self.fn_q = fn_q

        self.fn_p_inv = fn_p_inv
        self.fn_q_inv = fn_q_inv

    def map(self, traj: Trajectory) -> Trajectory:
        cval = self.fn_p(traj.y[0], traj.dual[0], traj.dynamical_parameters, traj.const)
        qval = np.ones_like(traj.t)

        traj.dynamical_parameters = np.hstack((traj.dynamical_parameters, cval))
        for ii, t in enumerate(traj.t):
            qval[ii] = self.fn_q(traj.y[ii], traj.dual[ii], traj.dynamical_parameters, traj.const)

        if self.remove_parameter_dict['location'] == 'states':
            traj.y = np.delete(traj.y, np.s_[self.remove_parameter_dict['index']], axis=1)
        elif self.remove_parameter_dict['location'] == 'costates':
            traj.dual = np.delete(traj.dual, np.s_[self.remove_parameter_dict['index']], axis=1)

        if self.remove_symmetry_dict['location'] == 'states':
            traj.y = np.delete(traj.y, np.s_[self.remove_symmetry_dict['index']], axis=1)
        elif self.remove_symmetry_dict['location'] == 'costates':
            traj.dual = np.delete(traj.dual, np.s_[self.remove_symmetry_dict['index']], axis=1)

        traj.q = np.column_stack((traj.q, qval))

        return traj

    def inv_map(self, traj: Trajectory) -> Trajectory:
        qinv = np.ones_like(traj.t)
        pinv = np.ones_like(traj.t)
        for ii, t in enumerate(traj.t):
            qinv[ii] = self.fn_q_inv(traj.y[ii], traj.dual[ii], traj.q[ii], traj.dynamical_parameters, traj.const)
            pinv[ii] = self.fn_p_inv(traj.y[ii], traj.dual[ii], traj.dynamical_parameters, traj.const)

        state = pinv
        qval = qinv
        if self.remove_parameter_dict['location'] == 'states':
            traj.y = np.column_stack(
                (traj.y[:, :self.remove_parameter_dict['index']], state,
                 traj.y[:, self.remove_parameter_dict['index']:]))
        elif self.remove_parameter_dict['location'] == 'costates':
            traj.dual = np.column_stack(
                (traj.dual[:, :self.remove_parameter_dict['index']], state,
                 traj.dual[:, self.remove_parameter_dict['index']:]))

        if self.remove_symmetry_dict['location'] == 'states':
            traj.y = np.column_stack(
                (traj.y[:, :self.remove_symmetry_dict['index']], qval,
                 traj.y[:, self.remove_symmetry_dict['index']:]))
        elif self.remove_symmetry_dict['location'] == 'costates':
            traj.dual = np.column_stack(
                (traj.dual[:, :self.remove_symmetry_dict['index']], qval,
                 traj.dual[:, self.remove_symmetry_dict['index']:]))

        traj.q = np.delete(traj.q, np.s_[-1], axis=1)
        traj.dynamical_parameters = traj.dynamical_parameters[:-1]
        return traj


def mf_com(prob: Problem, com_index=0):
    constant_of_motion = prob.constants_of_motion[com_index]

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
    _lhs = constant_of_motion.expr / constant_of_motion.sym * symmetry
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
            rvec[ii] += omega[ii, jj] * sympy.diff(constant_of_motion.expr, state_2.sym)

    symmetry_eom = sym_zero
    for idx, state in enumerate(states_and_costates):
        symmetry_eom += state.eom * rvec[idx]

    # TODO: Figure out how to find units of the quads. This is only works in some specialized cases.
    symmetry_unit = states_and_costates[symmetry_index].units

    prob.quads.append(
            DynamicStruct(str(symmetry_symbol), symmetry_eom, symmetry_unit))

    for idx, state in enumerate(states_and_costates):
        state.eom, _ = recursive_sub(state.eom, solve_for_p[0])
        state.eom, _ = recursive_sub(state.eom, solve_for_q[0])

    for idx, bc in enumerate(prob.equality_constraints['initial'] + prob.equality_constraints['terminal']):
        bc.expr, _ = recursive_sub(bc.expr, solve_for_p[0])
        bc.expr, _ = recursive_sub(bc.expr, solve_for_q[0])

    for idx, law in enumerate(prob.control_law):
        for jj, symbol in enumerate(law.keys()):
            prob.control_law[idx][symbol], _ = recursive_sub(prob.sympify(law[symbol]), solve_for_p[0])
            # prob.control_law[idx][symbol] = law[symbol]
            prob.control_law[idx][symbol], _ = recursive_sub(prob.sympify(law[symbol]), solve_for_q[0])
            # prob.control_law[idx][symbol] = law[symbol]

    for idx, com in enumerate(prob.constants_of_motion):
        if idx != com_index:
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

    del prob.constants_of_motion[com_index]

    state_syms = extract_syms(prob.states)
    costates_syms = extract_syms(prob.costates)
    parameter_syms = extract_syms(prob.parameters)
    constant_syms = extract_syms(prob.constants)
    quad_syms = extract_syms(prob.quads)

    fn_q_inv = prob.lambdify([state_syms, costates_syms, quad_syms, parameter_syms, constant_syms],
                             solve_for_q[0][replace_q])
    fn_p_inv = prob.lambdify([state_syms, costates_syms, parameter_syms, constant_syms], solve_for_p[0][replace_p])

    traj_mapper = MFMapper(remove_parameter_dict, remove_symmetry_dict, fn_p, fn_q, fn_p_inv, fn_q_inv)

    return prob, traj_mapper


def mf_all(prob: Problem):

    if not is_symplectic(prob.omega):
        logger.warning('BVP is not symplectic. Skipping reduction.')
        traj_mapper = None

    elif prob.constants_of_motion[1:]:
        traj_mapper = TrajectoryMapperList()

        for _ in range(len(prob.constants_of_motion[1:])):
            prob, traj_mapper_i = mf_com(prob, com_index=1)
            traj_mapper.append(traj_mapper_i)

    else:
        traj_mapper = None

    return prob, traj_mapper
