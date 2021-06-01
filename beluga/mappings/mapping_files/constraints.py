import numpy as np
import sympy

from beluga.compilation.compiler import lambdify, add_symbolic_local
from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.problem_components import NamedDimensionalStruct, extract_syms
from beluga.data_classes.trajectory import Trajectory
from beluga.mappings.trajectory_mapper import TrajectoryMapperList, TrajectoryMapper


def normalize_constraint(expr, lower, upper):
    return (2 * expr - upper - lower) / (upper - lower)


def make_regularized_control_name(u_sym):
    reg_u_name = '_{}_reg'.format(u_sym.name)
    return reg_u_name


def make_control_reg_func(u_sym, eps_sym, lower, upper, method='atan', reg_u_sym=None):

    if reg_u_sym is None:
        reg_u_sym = add_symbolic_local(make_regularized_control_name(u_sym))

    norm_u_sym = normalize_constraint(u_sym, lower, upper)

    method = method.lower()
    if method in ['trig', 'utm', 'eps_trig', 'trig_eps']:
        reg_func = sympy.sin(reg_u_sym)
        err_ctrl = eps_sym * sympy.cos(reg_u_sym)
        inv_func = sympy.asin(norm_u_sym)

    elif method in ['atan', 'arctan']:
        reg_func = sympy.atan(reg_u_sym / eps_sym) * 2 / sympy.pi
        err_ctrl = eps_sym * sympy.log(1 + (reg_u_sym / eps_sym) ** 2) / sympy.pi
        inv_func = eps_sym * sympy.tan(sympy.pi * norm_u_sym / 2)

    elif method in ['erf', 'error', 'error_function']:
        reg_func = sympy.erf(reg_u_sym / eps_sym)
        err_ctrl = eps_sym * (1 - sympy.exp(-(reg_u_sym / eps_sym) ** 2)) / sympy.sqrt(sympy.pi)
        inv_func = eps_sym * sympy.erfinv(norm_u_sym)

    elif method in ['tanh', 'hyper_tan']:
        reg_func = sympy.tanh(reg_u_sym / eps_sym)
        err_ctrl = reg_u_sym * sympy.tanh(reg_u_sym / eps_sym) + eps_sym * sympy.log(sympy.cosh(reg_u_sym / eps_sym))
        inv_func = eps_sym * sympy.atanh(norm_u_sym)

    elif method in ['log', 'logistic']:
        reg_func = 2 / (1 + sympy.exp(-reg_u_sym / eps_sym)) - 1
        err_ctrl = 2 * (-eps_sym * sympy.log((1 + sympy.exp(-reg_u_sym / eps_sym)) / 2)
                        + reg_u_sym * (1 / (1 + sympy.exp(-reg_u_sym / eps_sym)) - 1))
        inv_func = eps_sym * sympy.log((-norm_u_sym - 1)/(norm_u_sym - 1))

    elif method in ['alg', 'algebraic']:
        reg_func = (reg_u_sym / eps_sym) / sympy.sqrt(1 + (reg_u_sym / eps_sym) ** 2)
        err_ctrl = eps_sym * (1 - 1 / sympy.sqrt(1 + (reg_u_sym / eps_sym) ** 2))
        inv_func = eps_sym*norm_u_sym*sympy.sqrt(-1/(norm_u_sym**2 - 1))

    else:
        raise NotImplementedError('Control bounding method {} not implemented'.format(method))

    reg_func = ((upper - lower) * reg_func + (upper + lower)) / 2

    return reg_func, err_ctrl, inv_func


class ControlConstraintMapper(TrajectoryMapper):
    def __init__(self, control_idx, control_expr, inv_control_expr, u_sym, reg_u_sym, map_args):
        super().__init__()

        self.control_idx = control_idx

        self.map_func = lambdify([u_sym] + map_args, inv_control_expr)
        self.inv_map_func = lambdify([reg_u_sym] + map_args, control_expr)

    # TODO: "Vectorize" this
    def map(self, traj: Trajectory) -> Trajectory:
        for idx, (t_i, y_i) in enumerate(zip(traj.t, traj.y)):
            traj.u[idx, self.control_idx] = self.map_func(
                traj.u[idx, self.control_idx], t_i, y_i, traj.dynamical_parameters, traj.const)
        return traj

    def inv_map(self, traj: Trajectory) -> Trajectory:
        for idx, (t_i, y_i) in enumerate(zip(traj.t, traj.y)):
            traj.u[idx, self.control_idx] = self.inv_map_func(
                traj.u[idx, self.control_idx], t_i, y_i, traj.dynamical_parameters, traj.const)
        return traj


def regularize_control_constraint(prob: Problem, constraint_idx: int = 0, reg_u_name: str = None):

    constraint = prob.inequality_constraints['control'].pop(constraint_idx)

    u_sym, eps_sym, lower, upper, method = \
        constraint.expr, constraint.activator, constraint.lower, constraint.upper, constraint.method

    try:
        control_idx = extract_syms(prob.controls).index(u_sym)
    except ValueError:
        raise ValueError('{} not a control variable in problem.'
                         ' Control constraint must only be applied to control variables'. format(u_sym))

    if reg_u_name is None:
        reg_u_name = make_regularized_control_name(u_sym)

    prob.controls[control_idx] = NamedDimensionalStruct(reg_u_name, '1').sympify_self()
    reg_u_sym = prob.controls[control_idx].sym

    reg_func, err_ctrl, inv_func = make_control_reg_func(u_sym, eps_sym, lower, upper,
                                                         method=method, reg_u_sym=prob.controls[control_idx].sym)

    prob.subs_all(u_sym, reg_func)
    prob.cost.path += err_ctrl

    map_args = [prob.independent_variable.sym,
                np.array(extract_syms(prob.states)),
                np.array(extract_syms(prob.parameters)),
                np.array(extract_syms(prob.constants))]

    traj_mapper = ControlConstraintMapper(control_idx, reg_func, inv_func, u_sym, reg_u_sym, map_args)

    return prob, traj_mapper


def regularize_control_constraints(prob: Problem):

    if prob.inequality_constraints['control']:
        traj_mapper = TrajectoryMapperList()

        for _ in prob.inequality_constraints['control']:
            prob, traj_mapper_i = regularize_control_constraint(prob)
            traj_mapper.append(traj_mapper_i)

    else:
        traj_mapper = None

    return prob, traj_mapper


def make_penalty_func(expr, eps_sym, lower, upper, method='utm'):

    norm_expr = normalize_constraint(expr, lower, upper)

    method = method.lower()

    if method in ['utm', 'zero_utm']:
        penalty_func = 1 / sympy.cos(sympy.pi / 2 * norm_expr) - 1

    elif method in ['orig_utm']:
        penalty_func = 1 / sympy.cos(sympy.pi / 2 * norm_expr)

    else:
        raise NotImplementedError('Constraint method {} not implemented'.format(method))

    penalty_func *= eps_sym

    return penalty_func


def apply_penatly_method(prob: Problem, location, constraint_idx: int = 0):
    if location not in ['initial', 'path', 'terminal']:
        raise NotImplementedError(
                'Invalid location {} given. Location must be initial, path, or terminal.'.format(location))

    constraint = prob.inequality_constraints[location].pop(constraint_idx)

    expr, eps_sym, lower, upper, method = \
        constraint.expr, constraint.activator, constraint.lower, constraint.upper, constraint.method

    penalty_func = make_penalty_func(expr, eps_sym, lower, upper, method=method)

    # Add penalty function to cost function at specified location
    setattr(prob.cost, location, getattr(prob.cost, location) + penalty_func)

    return prob, None, None


def apply_penatly_method_initial(prob: Problem, constraint_idx: int = 0):
    return apply_penatly_method(prob, 'initial', constraint_idx=constraint_idx)


def apply_penatly_method_path(prob: Problem, constraint_idx: int = 0):
    return apply_penatly_method(prob, 'path', constraint_idx=constraint_idx)


def apply_penatly_method_terminal(prob: Problem, constraint_idx: int = 0):
    return apply_penatly_method(prob, 'terminal', constraint_idx=constraint_idx)


def apply_penatly_method_all(prob: Problem):
    for location in ['initial', 'path', 'terminal']:
        for _ in range(len(prob.inequality_constraints[location])):
            apply_penatly_method(prob, location, constraint_idx=0)

    return prob, None
