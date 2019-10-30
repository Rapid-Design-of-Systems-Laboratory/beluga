import inspect
import sys
import warnings
import copy

from beluga.codegen.codegen import *
from tqdm import tqdm

import numpy as np

from beluga import problem, helpers
import beluga.bvpsol as bvpsol
from beluga.release import __splash__
from beluga.ivpsol import Trajectory
from beluga.utils import save
from beluga.optimlib.direct import ocp_to_bvp as DIRECT_ocp_to_bvp
from beluga.optimlib.indirect import ocp_to_bvp as BH_ocp_to_bvp
from beluga.optimlib.diffyg_deprecated import ocp_to_bvp as DIFFYG_DEP_ocp_to_bvp
import time
import pathos

config = dict(logfile='beluga.log', default_bvp_solver='Shooting')


def add_logger(logging_level=logging.ERROR, display_level=logging.ERROR):
    """
    Attaches a logger to beluga's main process.

    :keyword logging_level: The level at which logging is written to the output file.
    :keyword display_level: The level at which logging is displayed to stdout.
    :return: None
    """
    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Initialize logging system
    helpers.init_logging(logging_level, display_level, config['logfile'])


def bvp_algorithm(name, **kwargs):
    """
    Helper method to load bvp algorithm by name.

    :param name: The name of the bvp algorithm
    :keywords: Additional keyword arguments passed into the bvp solver.
    :return: An instance of the bvp solver.
    """
    # Load algorithm from the package
    for N, obj in inspect.getmembers(bvpsol):
        if inspect.isclass(obj):
            if N.lower() == name.lower():
                return obj(**kwargs)
    else:
        # Raise exception if the loop completes without finding an algorithm by the given name
        raise ValueError('Algorithm ' + name + ' not found')


def guess_generator(*args, **kwargs):
    """
    Helper for creating an initial guess generator.

    :param method: The method used to generate the initial guess
    :keywords: Additional keyword arguments passed into the guess generator.
    :return: An instance of the guess generator.
    """
    guess_gen = problem.GuessGenerator()
    guess_gen.setup(*args, **kwargs)
    return guess_gen


def ocp2bvp(ocp, **kwargs):
    """

    :param ocp: The optimal control problem.
    :return: (bvp, map, map_inverse) - A codegen compiled BVP with associated mappings to and from the OCP.
    """

    method = kwargs.get('method', 'indirect').lower()
    optim_options = kwargs.get('optim_options', dict())
    optim_options.update({'method': method})

    logging.debug("Computing the necessary conditions of optimality")
    if method == 'indirect' or method == 'traditional' or method == 'brysonho' or method == 'diffyg':
        bvp_raw, _map, _map_inverse = BH_ocp_to_bvp(ocp, **optim_options)
    elif method == 'diffyg_deprecated':
        bvp_raw, _map, _map_inverse = DIFFYG_DEP_ocp_to_bvp(ocp, **optim_options)
    elif method == 'direct':
        bvp_raw, _map, _map_inverse = DIRECT_ocp_to_bvp(ocp, **optim_options)
    else:
        raise NotImplementedError

    bvp_raw['custom_functions'] = ocp.custom_functions()
    bvp = preprocess(bvp_raw)
    bvp.raw = bvp_raw
    ocp._scaling.initialize(bvp.raw)
    bvp.raw['scaling'] = ocp._scaling

    def ocp_map(sol):
        return _map(sol)

    def ocp_map_inverse(sol):
        return _map_inverse(sol)

    return bvp, ocp_map, ocp_map_inverse


def run_continuation_set(bvp_algo, steps, solinit, bvp, pool, autoscale):
    """
    Runs a continuation set for the BVP problem.

    :param bvp_algo: BVP algorithm to be used.
    :param steps: The steps in a continuation set.
    :param solinit: Initial guess for the first problem in steps.
    :param bvp: The compiled boundary-value problem to solve.
    :param pool: A processing pool, if available.
    :param autoscale: Whether or not scaling is used.
    :return: A set of solutions for the steps.
    """
    # Loop through all the continuation steps
    solution_set = []
    # Initialize scaling
    s = bvp.raw['scaling']

    # Load the derivative function into the bvp algorithm
    bvp_algo.set_derivative_function(bvp.deriv_func)
    bvp_algo.set_derivative_jacobian(bvp.deriv_jac_func)
    bvp_algo.set_quadrature_function(bvp.quad_func)
    bvp_algo.set_boundarycondition_function(bvp.bc_func)
    bvp_algo.set_boundarycondition_jacobian(bvp.bc_func_jac)
    bvp_algo.set_initial_cost_function(bvp.initial_cost)
    bvp_algo.set_path_cost_function(bvp.path_cost)
    bvp_algo.set_terminal_cost_function(bvp.terminal_cost)
    bvp_algo.set_inequality_constraint_function(bvp.ineq_constraints)

    sol_guess = solinit
    # sol = None
    if steps is None:
        logging.info('Solving OCP...')
        time0 = time.time()
        if autoscale:
            s.compute_scaling(sol_guess)
            sol_guess = s.scale(sol_guess)

        opt = bvp_algo.solve(sol_guess, pool=pool)
        sol = opt['sol']

        if autoscale:
            sol = s.unscale(sol)

        solution_set = [[copy.deepcopy(sol)]]
        if sol.converged:
            elapsed_time = time.time() - time0
            logging.debug('Problem converged in %0.4f seconds\n' % elapsed_time)
        else:
            elapsed_time = time.time() - time0
            logging.debug('Problem failed to converge!\n')
    else:
        for step_idx, step in enumerate(steps):
            logging.debug('\nRunning Continuation Step #'+str(step_idx+1)+' : ')
            # logging.debug('Number of Iterations\t\tMax BC Residual\t\tTime to Solution')
            solution_set.append([])
            # Assign solution from last continuation set
            step.reset()
            step.init(sol_guess, bvp)
            try:
                log_level = logging.getLogger()._displayLevel
            except:
                log_level = logging.getLogger().getEffectiveLevel()

            L = len(step)
            continuation_progress = tqdm(step, disable=log_level is not logging.INFO, desc='Continuation #' + str(step_idx+1),
                                  ascii=True, unit='trajectory')
            for sol_guess in continuation_progress:
                continuation_progress.total = len(step)
                if L != continuation_progress.total:
                    L = continuation_progress.total
                    continuation_progress.refresh()

                logging.debug('START \tIter {:d}/{:d}'.format(step.ctr, step.num_cases()))
                time0 = time.time()
                if autoscale:
                    s.compute_scaling(sol_guess)
                    sol_guess = s.scale(sol_guess)

                opt = bvp_algo.solve(sol_guess, pool=pool)
                sol = opt['sol']

                if autoscale:
                    sol = s.unscale(sol)

                ya = sol.y[0,:]
                yb = sol.y[-1,:]
                if sol.q.size > 0:
                    qa = sol.q[0,:]
                    qb = sol.q[-1,:]
                else:
                    qa = []
                    qb = []

                if sol.u.size > 0:
                    ua = sol.u[0,:]
                    ub = sol.u[-1,:]
                else:
                    ua = []
                    ub = []

                dp = sol.dynamical_parameters
                ndp = sol.nondynamical_parameters
                C = sol.const

                bc_residuals_unscaled = bvp_algo.boundarycondition_function(ya, qa, ua, yb, qb, ub, dp, ndp, C)

                step.add_gamma(sol)

                """
                The following line is overwritten by the looping variable UNLESS it is the final iteration. It is
                required when chaining continuation strategies together. DO NOT DELETE!
                """
                sol_guess = copy.deepcopy(sol)
                elapsed_time = time.time() - time0
                logging.debug('STOP  \tIter {:d}/{:d}\tBVP Iters {:d}\tBC Res {:13.8E}\tTime {:13.8f}'.format(step.ctr, step.num_cases(), opt['niter'], max(bc_residuals_unscaled), elapsed_time))
                solution_set[step_idx].append(copy.deepcopy(sol))
                if not sol.converged:
                    logging.debug('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))

    return solution_set


def solve(**kwargs):
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

    autoscale = kwargs.get('autoscale', True)
    bvp = kwargs.get('bvp', None)
    bvp_algorithm = kwargs.get('bvp_algorithm', None)
    guess_generator = kwargs.get('guess_generator', None)
    initial_helper = kwargs.get('initial_helper', False)
    method = kwargs.get('method', 'traditional')
    n_cpus = int(kwargs.get('n_cpus', 1))
    ocp = kwargs.get('ocp', None)
    ocp_map = kwargs.get('ocp_map', None)
    ocp_map_inverse = kwargs.get('ocp_map_inverse', None)
    optim_options = kwargs.get('optim_options', dict())
    steps = kwargs.get('steps', None)
    save_sols = kwargs.get('save', True)

    # Display useful info about the environment to debug logger.
    logging.debug('\n'+__splash__+'\n')
    from beluga import __version__ as beluga_version
    from llvmlite import __version__ as llvmlite_version
    from numba import __version__ as numba_version
    from numpy import __version__ as numpy_version
    from scipy import __version__ as scipy_version
    from sympy import __version__ as sympy_version

    logging.debug('beluga:\t\t' + str(beluga_version))
    logging.debug('llvmlite:\t' + str(llvmlite_version))
    logging.debug('numba:\t\t' + str(numba_version))
    logging.debug('numpy:\t\t' + str(numpy_version))
    logging.debug('python:\t\t' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2]))
    logging.debug('scipy:\t\t' + str(scipy_version))
    logging.debug('sympy:\t\t' + str(sympy_version))
    logging.debug('\n')

    if n_cpus < 1:
        raise ValueError('Number of cpus must be greater than 1.')
    if n_cpus > 1:
        pool = pathos.multiprocessing.Pool(processes=n_cpus)
    else:
        pool = None

    logging.debug('Using ' + str(n_cpus) + '/' + str(pathos.multiprocessing.cpu_count()) + ' CPUs. ')

    if bvp is None:
        bvp, ocp_map, ocp_map_inverse = ocp2bvp(ocp, method=method, optim_options=optim_options)
        logging.debug('Resulting BVP problem:')
        for key in bvp.raw.keys():
            logging.debug(str(key) + ': ' + str(bvp.raw[key]))

    else:
        if ocp_map is None or ocp_map_inverse is None:
            raise ValueError('BVP problem must have an associated \'ocp_map\' and \'ocp_map_inverse\'')

    solinit = Trajectory()
    solinit.const = np.array(bvp.raw['constants_values'])

    solinit = guess_generator.generate(bvp, solinit, ocp_map, ocp_map_inverse)

    sol_temp = copy.deepcopy(solinit)

    u = np.array([bvp.compute_control(sol_temp.y[0], [], sol_temp.dynamical_parameters, sol_temp.const)])
    for ii in range(len(sol_temp.t) - 1):
        u = np.vstack((u, bvp.compute_control(sol_temp.y[ii + 1], [], sol_temp.dynamical_parameters, sol_temp.const)))
    sol_temp.u = u
    state_names = [str(s['symbol']) for s in ocp.states()] + [str(ocp.get_independent()['symbol'])]
    traj = ocp_map_inverse(sol_temp)

    initial_states = np.hstack((traj.y[0, :], traj.t[0]))
    terminal_states = np.hstack((traj.y[-1, :], traj.t[-1]))

    initial_bc = dict(zip(state_names, initial_states))
    terminal_bc = dict(zip(state_names, terminal_states))

    if steps is not None and initial_helper:
        for ii, bc0 in enumerate(initial_bc):
            if bc0 + '_0' in bvp.raw['constants']:
                jj = bvp.raw['constants'].index(bc0 + '_0')
                solinit.const[jj] = initial_bc[bc0]

        for ii, bcf in enumerate(terminal_bc):
            if bcf + '_f' in bvp.raw['constants']:
                jj = bvp.raw['constants'].index(bcf + '_f')
                solinit.const[jj] = terminal_bc[bcf]

    quad_names = bvp.raw['quads']
    n_quads = len(quad_names)
    if n_quads > 0:
        initial_quads = solinit.q[0, :]
        terminal_quads = solinit.q[-1, :]
        initial_bc = dict(zip(quad_names, initial_quads))
        terminal_bc = dict(zip(quad_names, terminal_quads))

        for ii, bc0 in enumerate(initial_bc):
            if bc0 + '_0' in bvp.raw['constants']:
                jj = bvp.raw['constants'].index(bc0 + '_0')
                solinit.const[ii + '_0'] = initial_bc[bc0]

        for ii, bcf in enumerate(terminal_bc):
            if bcf + '_f' in bvp.raw['constants']:
                jj = bvp.raw['constants'].index(bcf + '_f')
                solinit.const[jj] = terminal_bc[bcf]

    time0 = time.time()

    out = run_continuation_set(bvp_algorithm, steps, solinit, bvp, pool, autoscale)
    total_time = time.time() - time0

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algorithm.close()

    for cont_num, continuation_set in enumerate(out):
        for sol_num, sol in enumerate(continuation_set):
            u = np.array([bvp.compute_control(sol.y[0], [], sol.dynamical_parameters, sol.const)])
            for ii in range(len(sol.t) - 1):
                u = np.vstack((u, bvp.compute_control(sol.y[ii + 1], [], sol.dynamical_parameters, sol.const)))
            sol.u = u
            out[cont_num][sol_num] = ocp_map_inverse(sol)

    if pool is not None:
        pool.close()

    if save_sols or (isinstance(save_sols, str)):
        if isinstance(save_sols, str):
            filename = save_sols
        else:
            filename = 'data.beluga'
        save(ocp=ocp, bvp_solver=bvp_algorithm, sol_set=out, filename=filename)
            filename = 'data.blg'
        save(ocp=ocp, bvp=bvp, bvp_solver=bvp_algorithm, sol_set=out, filename=filename)

    return out
