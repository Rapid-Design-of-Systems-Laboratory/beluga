import copy
from abc import ABC

from beluga.utils.logging import logger
from beluga.data_classes.symbolic_problem import Problem
from beluga.data_classes.compiled_problem import NumericProblem
from beluga.mappings.mapping_files.constraints import regularize_control_constraints, apply_penatly_method_all
from beluga.mappings.mapping_files.controls import algebraic_control_law, differential_control_law_traditional, \
    differential_control_law_diffy_g
from beluga.mappings.mapping_files.dualize import dualize, dualize_traditional, dualize_diffyg
from beluga.mappings.mapping_files.independent import momentum_shift, normalize_independent
from beluga.mappings.mapping_files.post_process import squash_to_bvp, compute_analytical_jacobians
from beluga.mappings.mapping_files.pre_process import ensure_sympified, apply_quantities
from beluga.mappings.mapping_files.reduction import mf_all
from beluga.mappings.mapping_files.switching import regularize_switches
from beluga.mappings.trajectory_mapper import TrajectoryMapperList


def compile_problem(prob: Problem, use_control_arg=False):

    prob.functional_problem = NumericProblem(prob)

    prob.functional_problem.compile_problem(use_control_arg=use_control_arg)
    prob.lambdified = True

    return prob


class RecipeBase(ABC):
    def __init__(self, in_place=True):
        self.in_place = in_place
        self.mapping_list = []

    def __call__(self, prob):
        if not self.in_place:
            prob = copy.deepcopy(prob)

        ensure_sympified(prob)

        recipe_traj_mapper = TrajectoryMapperList()

        for transformation in self.mapping_list:
            prob, transform_traj_mapper = transformation(prob)
            recipe_traj_mapper.append(transform_traj_mapper)

        compile_problem(prob)

        return prob, recipe_traj_mapper


class IndirectMinimal(RecipeBase):
    def __init__(self, in_place=True):
        super().__init__(in_place=in_place)
        self.mapping_list = [
            apply_quantities,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches,
            dualize,
            differential_control_law_traditional
        ]


class IndirectForSPBVP(RecipeBase):
    def __init__(self, in_place=True):
        super().__init__(in_place=in_place)
        self.mapping_list = [
            apply_quantities,
            momentum_shift,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches,
            dualize,
            differential_control_law_traditional,
            normalize_independent,
            squash_to_bvp,
            compute_analytical_jacobians
        ]


class IndirectDiffyG(RecipeBase):
    def __init__(self, in_place=True):
        super().__init__(in_place=in_place)
        self.mapping_list = [
            apply_quantities,
            momentum_shift,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches,
            dualize,
            differential_control_law_diffy_g,
            mf_all
        ]


class Direct(RecipeBase):
    def __init__(self, in_place=True):
        super().__init__(in_place=in_place)
        self.mapping_list = [
            apply_quantities,
            momentum_shift,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches
        ]


class OptimOptionsRecipe(RecipeBase):
    def __init__(self, analytical_jacobian=False, control_method='differential', method='traditional', reduction=False):
        super().__init__()

        self.mapping_list = [
            apply_quantities,
            momentum_shift,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches
        ]

        if method.lower() in ['indirect', 'traditional', 'brysonho']:
            method = 'traditional'
            self.mapping_list.append(dualize_traditional)
        elif method.lower() in ['diffyg']:
            self.mapping_list.append(dualize_diffyg)
        else:
            raise NotImplementedError('Method \"{}\" not implemented. Expected \"traditional\" or \"diffyg\"'
                                      .format(control_method))

        if control_method == 'algebraic':
            self.mapping_list.append(algebraic_control_law)
        elif control_method == 'differential' and method == 'traditional':
            self.mapping_list.append(differential_control_law_traditional)
        elif control_method == 'differential' and method == 'diffyg':
            self.mapping_list.append(differential_control_law_diffy_g)
        elif control_method.lower() == 'numeric':
            raise NotImplementedError('Numerical control method not yet implemented')
        else:
            raise NotImplementedError(
                    'Control method \"{}\" not implemented. Expected \"algebraic\" or \"differential\"'
                    .format(control_method))

        self.mapping_list.append(normalize_independent)

        if reduction:
            self.mapping_list.append(mf_all)

        self.mapping_list.append(squash_to_bvp)

        if analytical_jacobian:
            if control_method == 'algebraic':
                logger.info('Analytical Jacobians not available for algebraic control mode')
            else:
                self.mapping_list.append(compute_analytical_jacobians)
