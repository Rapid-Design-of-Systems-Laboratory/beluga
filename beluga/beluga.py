import logging
import copy
import time
import pathos
import numpy as np

from beluga.utils.logging import logger, make_a_splash
from beluga.data_classes.trajectory import Trajectory
from beluga.utils import save
from beluga.data_classes.problem_components import getattr_from_list
from beluga.transforms.problem_functions.problem_functions import compile_direct, compile_indirect
from beluga.continuation import run_continuation_set, match_constants_to_states


def solve(
        autoscale=True,
        bvp=None,
        bvp_algorithm=None,
        guess_generator=None,
        initial_helper=False,
        method='traditional',
        n_cpus=1,
        ocp=None,
        ocp_map=None,
        ocp_map_inverse=None,
        optim_options=None,
        steps=None,
        save_sols=True):

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
        raise NotImplementedError('\"ocp\" must be defined.')

    """
    Main code
    """

    # f_ocp = compile_direct(ocp)

    logger.debug('Using ' + str(n_cpus) + '/' + str(pathos.multiprocessing.cpu_count()) + ' CPUs. ')

    if bvp is None:
        if method.lower() in ['indirect', 'traditional', 'brysonho', 'diffyg']:
            bvp = compile_indirect(copy.deepcopy(ocp), method=method, **optim_options)
        elif method == 'direct':
            bvp = compile_direct(copy.deepcopy(ocp), **optim_options)
        else:
            raise NotImplementedError

        logger.debug('Resulting BVP problem:')
        logger.debug(bvp.__repr__())

        ocp_map = bvp.map_sol
        ocp_map_inverse = bvp.inv_map_sol

    else:
        if ocp_map is None or ocp_map_inverse is None:
            raise ValueError('BVP problem must have an associated \'ocp_map\' and \'ocp_map_inverse\'')

    solinit = Trajectory()
    solinit.const = np.array(getattr_from_list(bvp.constants, 'default_val'))
    solinit = guess_generator.generate(bvp.functional_problem, solinit, ocp_map, ocp_map_inverse)

    if initial_helper:
        sol_ocp = copy.deepcopy(solinit)
        sol_ocp = match_constants_to_states(ocp, ocp_map_inverse(sol_ocp))
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
    out = postprocess(continuation_set, ocp_map_inverse)

    if pool is not None:
        pool.close()

    if save_sols or (isinstance(save_sols, str)):
        if isinstance(save_sols, str):
            filename = save_sols
        else:
            filename = 'data.beluga'

        save(out, ocp, bvp, filename=filename)

    return out


def postprocess(continuation_set, ocp_map_inverse):
    """
    Post processes the data after the continuation process has run.

    :param continuation_set: The set of all continuation processes.
    :param ocp: The compiled OCP.
    :param prob: The compiled BVP.
    :param ocp_map_inverse: A mapping converting BVP solutions to OCP solutions.
    :return: Set of trajectories to be returned to the user.
    """
    out = []

    # Calculate the control time-history for each trajectory
    for cont_num, continuation_step in enumerate(continuation_set):
        tempset = []
        for sol_num, sol in enumerate(continuation_step):
            tempset.append(ocp_map_inverse(sol))
        out.append(tempset)

    return out
