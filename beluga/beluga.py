import sys
import warnings
import copy
import time
import pathos
import logging
import numpy as np

from beluga.release import __splash__
from beluga.numeric.data_classes.Trajectory import Trajectory
from beluga.utils import save, init_logging
from beluga.symbolic.data_classes.components_structures import getattr_from_list
from beluga.symbolic.data_classes.mapping_functions import compile_direct, compile_indirect
from beluga.continuation import run_continuation_set


def add_logger(logging_level=logging.ERROR, display_level=logging.ERROR, **kwargs):
    """
    Attaches a logger to beluga's main process.

    :keyword logging_level: The level at which logging is written to the output file.
    :keyword display_level: The level at which logging is displayed to stdout.
    :keyword filename: Name of the log file. Default is `beluga.log`.
    :keyword mode: File mode. Default is 'w' (overwrite).
    :keyword encoding: Log file encoding.
    :keyword delay: Delays opening log file until first call to emit().
    :return: None

    .. seealso::
            logging.FileHandler
    """
    # Suppress warnings
    warnings.filterwarnings("ignore")

    # logfile options for logging.FileHandler
    config = {'filename': 'beluga.log', 'mode': 'w'}
    config.update(kwargs)

    # Initialize logging system
    init_logging(logging_level, display_level, config)


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

    """
    Solves the OCP using specified method

    +------------------------+-----------------+---------------------------------------+
    | Valid kwargs           | Default Value   | Valid Values                          |
    +========================+=================+=======================================+
    | autoscale              | True            | bool                                  |
    +------------------------+-----------------+---------------------------------------+
    | bvp                    | None            | codegen'd BVPs                        |
    +------------------------+-----------------+---------------------------------------+
    | bvp_algorithm          | None            | bvp algorithm                         |
    +------------------------+-----------------+---------------------------------------+
    | guess_generator        | None            | guess generator                       |
    +------------------------+-----------------+---------------------------------------+
    | initial_helper         | False           | bool                                  |
    +------------------------+-----------------+---------------------------------------+
    | method                 | 'traditional'   | string                                |
    +------------------------+-----------------+---------------------------------------+
    | n_cpus                 | 1               | integer                               |
    +------------------------+-----------------+---------------------------------------+
    | ocp                    | None            | :math:`\\Sigma`                       |
    +------------------------+-----------------+---------------------------------------+
    | ocp_map                | None            | :math:`\\gamma \rightarrow \\gamma`   |
    +------------------------+-----------------+---------------------------------------+
    | ocp_map_inverse        | None            | :math:`\\gamma \rightarrow \\gamma`   |
    +------------------------+-----------------+---------------------------------------+
    | optim_options          | None            | dict()                                |
    +------------------------+-----------------+---------------------------------------+
    | steps                  | None            | continuation_strategy                 |
    +------------------------+-----------------+---------------------------------------+
    | save                   | False           | bool, str                             |
    +------------------------+-----------------+---------------------------------------+

    """

    if optim_options is None:
        optim_options = {}

    # Display useful info about the environment to debug logger.
    logging.beluga('\n'+__splash__+'\n')
    from beluga import __version__ as beluga_version
    from llvmlite import __version__ as llvmlite_version
    from numba import __version__ as numba_version
    from numpy import __version__ as numpy_version
    from scipy import __version__ as scipy_version
    from sympy.release import __version__ as sympy_version

    logging.beluga('beluga:\t\t' + str(beluga_version))
    logging.beluga('llvmlite:\t' + str(llvmlite_version))
    logging.beluga('numba:\t\t' + str(numba_version))
    logging.beluga('numpy:\t\t' + str(numpy_version))
    logging.beluga('python:\t\t'
                   + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2]))
    logging.beluga('scipy:\t\t' + str(scipy_version))
    logging.beluga('sympy:\t\t' + str(sympy_version))
    logging.beluga('\n')

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

    logging.beluga('Using ' + str(n_cpus) + '/' + str(pathos.multiprocessing.cpu_count()) + ' CPUs. ')

    if bvp is None:
        logging.beluga('Resulting BVP problem:')
        if method.lower() in ['indirect', 'traditional', 'brysonho']:
            method = 'traditional'
        if method == 'traditional' or method == 'diffyg':
            bvp = compile_indirect(copy.deepcopy(ocp), method=method, **optim_options)
        elif method == 'direct':
            bvp = compile_direct(copy.deepcopy(ocp), **optim_options)
        else:
            raise NotImplementedError
        logging.beluga('Resulting BVP problem:')
        logging.beluga(bvp.__repr__())

        ocp_map = bvp.map_sol
        ocp_map_inverse = bvp.inv_map_sol

    else:
        if ocp_map is None or ocp_map_inverse is None:
            raise ValueError('BVP problem must have an associated \'ocp_map\' and \'ocp_map_inverse\'')

    solinit = Trajectory()
    solinit.const = np.array(getattr_from_list(bvp.constants, 'default_val'))

    solinit = guess_generator.generate(bvp.functional_problem, solinit, ocp_map, ocp_map_inverse)

    sol_temp = copy.deepcopy(solinit)

    if bvp.functional_problem.compute_u is not None:
        u = np.array([bvp.functional_problem.compute_u(sol_temp.y[0], sol_temp.dynamical_parameters, sol_temp.const)])
        for ii in range(len(sol_temp.t) - 1):
            u = np.vstack((u, bvp.functional_problem.compute_u(sol_temp.y[ii + 1],
                                                               sol_temp.dynamical_parameters, sol_temp.const)))
        sol_temp.u = u

    state_names = getattr_from_list(bvp.states, 'name')
    traj = ocp_map_inverse(sol_temp)

    initial_states = np.hstack((traj.y[0, :], traj.t[0]))
    terminal_states = np.hstack((traj.y[-1, :], traj.t[-1]))

    initial_bc = dict(zip(state_names, initial_states))
    terminal_bc = dict(zip(state_names, terminal_states))

    if steps is not None and initial_helper:
        for ii, bc0 in enumerate(initial_bc):
            if bc0 + '_0' in getattr_from_list(bvp.constants, 'name'):
                jj = getattr_from_list(bvp.constants, 'name').index(bc0 + '_0')
                solinit.const[jj] = initial_bc[bc0]

        for ii, bcf in enumerate(terminal_bc):
            if bcf + '_f' in getattr_from_list(bvp.constants, 'name'):
                jj = getattr_from_list(bvp.constants, 'name').index(bcf + '_f')
                solinit.const[jj] = terminal_bc[bcf]

    """
    Main continuation process
    """
    time0 = time.time()
    continuation_set = run_continuation_set(bvp_algorithm, steps, solinit, bvp, pool, autoscale)
    total_time = time.time() - time0
    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
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

        save(out, filename=filename)

    return out


def postprocess(continuation_set, ocp_map_inverse):
    """
    Post processes the data after the continuation process has run.

    :param continuation_set: The set of all continuation processes.
    :param ocp: The compiled OCP.
    :param bvp: The compiled BVP.
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
