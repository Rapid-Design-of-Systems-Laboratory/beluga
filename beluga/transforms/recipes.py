import copy
from abc import ABC

from beluga.data_classes.compiled_problem import CompiledProblem
from beluga.data_classes.symbolic_problem import SymbolicProblem
from beluga.transforms.constraints import regularize_control_constraints, apply_penatly_method_all
from beluga.transforms.controls import algebraic_control_law, differential_control_law_traditional, \
    differential_control_law_diffy_g
from beluga.transforms.dualize import dualize, dualize_traditional, dualize_diffyg
from beluga.transforms.independent import momentum_shift, normalize_independent
from beluga.transforms.post_process import squash_to_bvp, compute_analytical_jacobians
from beluga.transforms.pre_process import ensure_sympified, apply_quantities
from beluga.transforms.reduction import mf_all
from beluga.transforms.switching import regularize_switches
from beluga.transforms.trajectory_transformer import TrajectoryTransformerList
from beluga.utils.logging import logger


def compile_problem(prob: SymbolicProblem, use_control_arg=False):

    prob.functional_problem = CompiledProblem(prob)

    prob.functional_problem.compile_problem(use_control_arg=use_control_arg)
    prob.lambdified = True

    return prob


class RecipeBase(ABC):
    def __init__(self, in_place=True):
        self.in_place = in_place
        self.transforms = []

    def __call__(self, prob):
        if not self.in_place:
            prob = copy.deepcopy(prob)

        ensure_sympified(prob)

        recipe_traj_mapper = TrajectoryTransformerList()

        for transformation in self.transforms:
            prob, transform_traj_mapper = transformation(prob)
            recipe_traj_mapper.append(transform_traj_mapper)

        compile_problem(prob)

        return prob, recipe_traj_mapper


class IndirectMinimal(RecipeBase):
    def __init__(self, in_place=True):
        super().__init__(in_place=in_place)
        self.transforms = [
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
        self.transforms = [
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
        self.transforms = [
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
        self.transforms = [
            apply_quantities,
            momentum_shift,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches
        ]


class OptimOptionsRecipe(RecipeBase):
    def __init__(self, analytical_jacobian=False, control_method='differential', method='traditional', reduction=False):
        super().__init__()

        self.transforms = [
            apply_quantities,
            momentum_shift,
            regularize_control_constraints,
            apply_penatly_method_all,
            regularize_switches
        ]

        if method.lower() in ['indirect', 'traditional', 'brysonho']:
            method = 'traditional'
            self.transforms.append(dualize_traditional)
        elif method.lower() in ['diffyg']:
            self.transforms.append(dualize_diffyg)
        else:
            raise NotImplementedError('Method \"{}\" not implemented. Expected \"traditional\" or \"diffyg\"'
                                      .format(control_method))

        if control_method == 'algebraic':
            self.transforms.append(algebraic_control_law)
        elif control_method == 'differential' and method == 'traditional':
            self.transforms.append(differential_control_law_traditional)
        elif control_method == 'differential' and method == 'diffyg':
            self.transforms.append(differential_control_law_diffy_g)
        elif control_method.lower() == 'numeric':
            raise NotImplementedError('Numerical control method not yet implemented')
        else:
            raise NotImplementedError(
                    'Control method \"{}\" not implemented. Expected \"algebraic\" or \"differential\"'
                    .format(control_method))

        self.transforms.append(normalize_independent)

        if reduction:
            self.transforms.append(mf_all)

        self.transforms.append(squash_to_bvp)

        if analytical_jacobian:
            if control_method == 'algebraic':
                logger.info('Analytical Jacobians not available for algebraic control mode')
            else:
                self.transforms.append(compute_analytical_jacobians)
