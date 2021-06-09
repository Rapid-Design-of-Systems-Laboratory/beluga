import copy
import logging
import time

import numpy as np
import pathos

from beluga.continuation import run_continuation_set, match_constants_to_states
from beluga.data_classes.problem_components import getattr_from_list
from beluga.data_classes.trajectory import Trajectory
from beluga.transforms.recipes import OptimOptionsRecipe, Direct
from beluga.utils import save
from beluga.utils.logging import logger, make_a_splash


def solve(autoscale=True, bvp=None, bvp_algorithm=None, guess_generator=None, initial_helper=False,
          method='traditional', n_cpus=1, ocp=None, ocp_transform=None, ocp_inv_transform=None, optim_options=None,
          steps=None, save_sols=True):

    if optim_options is None:
        optim_options = {}

    if logger.level <= logging.DEBUG:
        logger.debug(make_a_splash())

    """
    Error checking
    """
    if n_cpus < 1:
        raise ValueError('Number of cpus must be greater than 1.')
    if n_cpus > 1:
        pool = pathos.multiprocessing.Pool(processes=n_cpus)
    else:
        pool = None

    if ocp is None:
        raise NotImplementedError('\"prob\" must be defined.')

    """
    Main code
    """

    # f_ocp = compile_direct(prob)

    logger.debug('Using ' + str(n_cpus) + '/' + str(pathos.multiprocessing.cpu_count()) + ' CPUs. ')

    if bvp is None:
        if method.lower() in ['indirect', 'traditional', 'brysonho', 'diffyg']:
            bvp, traj_mapper = OptimOptionsRecipe(method=method, **optim_options)(copy.deepcopy(ocp))
        elif method == 'direct':
            bvp, traj_mapper = Direct()(copy.deepcopy(ocp))
        else:
            raise NotImplementedError

        logger.debug('Resulting BVP problem:')
        logger.debug(bvp.__repr__())

        ocp_transform = traj_mapper.transform
        ocp_inv_transform = traj_mapper.inv_transform
        ocp_inv_transform_many = traj_mapper.inv_transform_many

    else:
        if ocp_transform is None or ocp_inv_transform is None:
            raise ValueError('BVP problem must have an associated \'ocp_map\' and \'ocp_map_inverse\'')

    solinit = Trajectory()
    solinit.const = np.array(getattr_from_list(bvp.constants, 'default_val'))
    solinit = guess_generator.generate(bvp.functional_problem, solinit, ocp_transform, ocp_inv_transform)

    if initial_helper:
        sol_ocp = copy.deepcopy(solinit)
        sol_ocp = match_constants_to_states(ocp, ocp_inv_transform(sol_ocp))
        solinit.const = sol_ocp.const

    if bvp.functional_problem.compute_u is not None:
        u = np.array([bvp.functional_problem.compute_u(solinit.y[0], solinit.dynamical_parameters, solinit.const)])
        for ii in range(len(solinit.t) - 1):
            u = np.vstack(
                (u, bvp.functional_problem.compute_u(solinit.y[ii + 1], solinit.dynamical_parameters, solinit.const)))
        solinit.u = u

    """
    Main continuation process
    """
    time0 = time.time()
    continuation_set = run_continuation_set(bvp_algorithm, steps, solinit, bvp, pool, autoscale)
    total_time = time.time() - time0
    logger.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algorithm.close()

    """
    Post processing and output
    """
    # Calculate the control time-history for each trajectory
    out = []
    for continuation_step in continuation_set:
        out.append(ocp_inv_transform_many(continuation_step))

    if pool is not None:
        pool.close()

    if save_sols or (isinstance(save_sols, str)):
        if isinstance(save_sols, str):
            filename = save_sols
        else:
            filename = 'data.beluga'

        save(out, ocp, bvp, filename=filename)

    return out
