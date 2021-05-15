import copy
import logging
from abc import ABC
from typing import Iterable

from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.compiled_problem import NumericProblem
from beluga.symbolic.differential_geometry import is_symplectic
from beluga.mappings.problem_mappings import ensure_sympified, apply_quantities, momentum_shift, \
    epstrig, utm, rashs, normalize_time, mf, compute_analytical_jacobians, dualize, algebraic_control_law, \
    differential_control_law, squash_to_bvp


class SolMapper:
    # TODO Add multiprocessing
    def __init__(self, in_place=True):
        self.in_place = in_place
        self.mapping_list = []

    def append(self, mapping):
        if mapping is not None:
            self.mapping_list.append(mapping)

    def map(self, sol):
        if not self.in_place:
            sol = copy.deepcopy(sol)

        for mapping in self.mapping_list:
            mapping(sol)

        return sol

    def map_many(self, sols):
        # TODO Make parallel
        return map(self.map, sols)

    def __call__(self, sols):
        if isinstance(sols, Iterable):
            return self.map_many(sols)
        else:
            return self.map(sols)


class RecipeBase(ABC):
    def __init__(self, in_place=True):
        self.in_place = in_place
        self.mapping_list = []

    def __call__(self, prob):
        if not self.in_place:
            prob = copy.deepcopy(prob)

        ensure_sympified(prob)

        sol_mapper, inv_sol_mapper = SolMapper(), SolMapper()

        for transformation in self.mapping_list:
            prob, sol_map, inv_sol_map = transformation()
            sol_mapper.append(sol_map), inv_sol_mapper.append(inv_sol_map)

        return prob, sol_mapper, inv_sol_mapper


class Indirect(RecipeBase):
    def __init__(self, in_place=True):
        super().__init__(in_place)
        self.mapping_list = []


def compile_direct(prob: Problem, analytical_jacobian=True, reduction=False,
                   do_momentum_shift=False, do_normalize_time=False):
    ensure_sympified(prob)

    """
    Substitute Quantities
    """
    apply_quantities(prob)

    """
    Make time a state.
    """
    if do_momentum_shift:
        momentum_shift(prob)

    """
    Deal with path constraints
    """
    for path_constraint in copy.copy(prob.constraints['path']):
        if path_constraint.method.lower() == 'epstrig':
            epstrig(prob)
        elif path_constraint.method.lower() == 'utm':
            utm(prob)
        else:
            raise NotImplementedError('Unknown path constraint method \"' + str(path_constraint.method) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(prob.switches) > 0:
        rashs(prob)

    """
    Scale eom to final time
    """
    if do_normalize_time:
        normalize_time(prob)

    """
    Reduce if needed
    """
    if is_symplectic(prob.omega) and reduction:
        while len(prob.constants_of_motion) > 1:
            mf(prob, 1)

    elif not is_symplectic(prob.omega) and reduction:
        logging.warning('BVP is not symplectic. Skipping reduction.')

    """
    Form analytical jacobians
    """
    if analytical_jacobian:
        compute_analytical_jacobians(prob)

    compile_problem(prob)


def compile_indirect(prob: Problem, analytical_jacobian=False, control_method='differential', method='traditional',
                     reduction=False, do_momentum_shift=True, do_normalize_time=True):

    ensure_sympified(prob)



    if method.lower() in ['indirect', 'traditional', 'brysonho']:
        method = 'traditional'

    """
    Substitute Quantities
    """
    apply_quantities(prob)

    """
    Make time a state.
    """
    if do_momentum_shift:
        momentum_shift(prob)

    """
    Deal with constraints inequality constraints
    """

    for constraint in copy.copy(prob.constraints['initial'] + prob.constraints['path']
                                + prob.constraints['terminal']):
        if constraint.lower is not None and constraint.upper is not None:
            if constraint.method.lower() == 'epstrig':
                epstrig(prob)
            elif constraint.method.lower() == 'utm':
                utm(prob)
            else:
                raise NotImplementedError(
                    'Unknown path constraint method \"' + str(constraint.method) + '\"')

    """
    Deal with staging, switches, and their substitutions.
    """
    if len(prob.switches) > 0:
        rashs(prob)

    """
    Dualize Problem
    """
    dualize(prob, method=method)

    """
    Form Control Law
    """
    if control_method.lower() == 'algebraic':
        algebraic_control_law(prob)
    elif control_method.lower() == 'differential':
        differential_control_law(prob, method=method)
    elif control_method.lower() == 'compilation':
        raise NotImplementedError('Numerical control method not yet implemented')
    else:
        raise NotImplementedError('{} control method not implemented. Try differential or algebraic')

    """
    Scale eom to final time
    """
    if do_normalize_time:
        normalize_time(prob)

    """
    Reduce if needed
    """
    if is_symplectic(prob.omega) and reduction:
        while len(prob.constants_of_motion) > 1:
            mf(prob, 1)

    elif not is_symplectic(prob.omega) and reduction:
        logging.warning('BVP is not symplectic. Skipping reduction.')

    """
    Squash dual problem to normal BVP
    """
    squash_to_bvp(prob)

    """
    Form analytical jacobians
    """
    if analytical_jacobian:
        if control_method == 'algebraic':
            logging.info('Analytical Jacobians not available for algebraic control mode')
        else:
            compute_analytical_jacobians(prob)

    compile_problem(prob)

    return prob


def compile_problem(prob: Problem, use_control_arg=False):
    ensure_sympified(prob)

    prob.functional_problem = NumericProblem(prob)

    prob.functional_problem.compile_problem(use_control_arg=use_control_arg)
    prob.lambdified = True

    return prob