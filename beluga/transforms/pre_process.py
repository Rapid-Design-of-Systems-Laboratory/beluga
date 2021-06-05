from itertools import permutations

import sympy

from beluga.data_classes.symbolic_problem import SymbolicProblem
from beluga.data_classes.trajectory import Trajectory as Solution
from beluga.transforms.trajectory_transformer import TrajectoryTransformer
from beluga.utils.logging import logger


def ensure_sympified(prob):
    if not prob.sympified:
        prob.sympify_self()


class QuantityCalculator(TrajectoryTransformer):
    def transform(self, traj: Solution) -> Solution:
        return traj

    def inv_transform(self, traj: Solution) -> Solution:
        return traj


def apply_quantities(prob: SymbolicProblem):

    if len(prob.quantities) == 0:
        return prob, None

    quantities = prob.quantities

    dependencies = []
    for quantity_i, quantity_j in permutations(quantities, 2):
        if quantity_i.expr.has(quantity_j.sym):
            dependencies.append((quantity_i, quantity_j))

    try:
        ordered_quantities = sympy.topological_sort((quantities, dependencies), key=lambda _q: _q.name)
    except ValueError:
        logger.exception('Error: Cycle found in dependencies in quantities.')
        raise ValueError('Cycle found in dependencies in quantities.')

    for quantity in ordered_quantities:
        prob.subs_all(quantity.sym, quantity.expr)
        prob.quantities.remove(quantity)

    # TODO add quantity calculation to Trajectory class
    # traj_mapper = QuantityCalculator()
    traj_mapper = None

    return prob, traj_mapper

