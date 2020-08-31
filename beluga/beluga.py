import inspect
import sys
import warnings
import copy
import logging

from tqdm import tqdm

import numpy as np

import beluga.numeric.bvp_solvers as bvpsol
from beluga.release import __splash__
from beluga.numeric.ivp_solvers import Trajectory
from beluga.utils import save, init_logging
from beluga.continuation import GuessGenerator
from beluga.symbolic import Problem, getattr_from_list
from .symbolic.problem_classes.mapping_functions import compile_problem, compile_direct, compile_indirect

import time
import pathos
import scipy.integrate as integrate

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
    init_logging(logging_level, display_level, config['logfile'])


# TODO: What's the point of this?
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


# TODO: What's the point of this?
def guess_generator(*args, **kwargs):
    """
    Helper for creating an initial guess generator.

    :param method: The method used to generate the initial guess
    :keywords: Additional keyword arguments passed into the guess generator.
    :return: An instance of the guess generator.
    """
    guess_gen = GuessGenerator()
    guess_gen.setup(*args, **kwargs)
    return guess_gen


def run_continuation_set(bvp_algo, steps, solinit, bvp: Problem, pool, autoscale):
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

    functional_problem = bvp.functional_problem

    # Initialize scaling
    scale = functional_problem.scale_sol
    compute_factors = functional_problem.compute_scale_factors

    # Load the derivative function into the bvp algorithm
    bvp_algo.set_derivative_function(functional_problem.deriv_func)
    bvp_algo.set_derivative_jacobian(functional_problem.deriv_func_jac)
    bvp_algo.set_quadrature_function(functional_problem.quad_func)
    bvp_algo.set_boundarycondition_function(functional_problem.bc_func)
    bvp_algo.set_boundarycondition_jacobian(functional_problem.bc_func_jac)
    # bvp_algo.set_initial_cost_function(functional_problem.initial_cost)
    # bvp_algo.set_path_cost_function(functional_problem.path_cost)
    # bvp_algo.set_terminal_cost_function(functional_problem.terminal_cost)
    bvp_algo.set_inequality_constraint_function(functional_problem.ineq_constraints)

    sol_guess = solinit
    # sol = None
    if steps is None:
        logging.info('Solving OCP...')
        time0 = time.time()
        if autoscale:
            scale_factors = compute_factors(sol_guess)
            sol_guess = scale(sol_guess, scale_factors)
        else:
            scale_factors = None

        opt = bvp_algo.solve(sol_guess, pool=pool)
        sol = opt['sol']

        if autoscale:
            sol = scale(sol, scale_factors, inv=True)

        solution_set = [[copy.deepcopy(sol)]]
        if sol.converged:
            elapsed_time = time.time() - time0
            logging.debug('Problem converged in %0.4f seconds\n' % elapsed_time)
        else:
            elapsed_time = time.time() - time0
            logging.debug('Problem failed to converge!\n')
    else:
        for step_idx, step in enumerate(steps):
            logging.debug('\nRunning Continuation Step #{} ({})'.format(step_idx+1, step)+' : ')
            # logging.debug('Number of Iterations\t\tMax BC Residual\t\tTime to Solution')
            solution_set.append([])
            # Assign solution from last continuation set
            step.reset()
            step.init(sol_guess, bvp)
            try:
                log_level = logging.getLogger()._displayLevel
            except AttributeError:
                log_level = logging.getLogger().getEffectiveLevel()

            step_len = len(step)
            continuation_progress = tqdm(
                step, disable=log_level is not logging.INFO, desc='Continuation #' + str(step_idx+1),
                ascii=True, unit='trajectory')
            for sol_guess in continuation_progress:
                continuation_progress.total = len(step)
                if step_len != continuation_progress.total:
                    step_len = continuation_progress.total
                    continuation_progress.refresh()

                logging.debug('START \tIter {:d}/{:d}'.format(step.ctr, step.num_cases()))
                time0 = time.time()
                if autoscale:
                    scale_factors = compute_factors(sol_guess)
                    sol_guess = scale(sol_guess, scale_factors)
                else:
                    scale_factors = None

                opt = bvp_algo.solve(sol_guess, pool=pool)
                sol = opt['sol']

                if autoscale:
                    sol = scale(sol, scale_factors, inv=True)

                ya = sol.y[0, :]
                yb = sol.y[-1, :]
                if sol.q.size > 0:
                    qa = sol.q[0, :]
                    qb = sol.q[-1, :]
                else:
                    qa = np.array([])
                    qb = np.array([])

                # if sol.u.size > 0:
                #     ua = sol.u[0, :]
                #     ub = sol.u[-1, :]
                # else:
                #     ua = np.array([])
                #     ub = np.array([])

                dp = sol.dynamical_parameters
                ndp = sol.nondynamical_parameters
                k = sol.const

                bc_residuals_unscaled = bvp_algo.boundarycondition_function(ya, qa, yb, qb, dp, ndp, k)

                step.add_gamma(sol)

                """
                The following line is overwritten by the looping variable UNLESS it is the final iteration. It is
                required when chaining continuation strategies together. DO NOT DELETE!
                """
                sol_guess = copy.deepcopy(sol)
                elapsed_time = time.time() - time0
                logging.debug('STOP  \tIter {:d}/{:d}\tBVP Iters {:d}\tBC Res {:13.8E}\tTime {:13.8f}'
                              .format(step.ctr, step.num_cases(), opt['niter'],
                                      max(bc_residuals_unscaled), elapsed_time))
                solution_set[step_idx].append(copy.deepcopy(sol))
                if not sol.converged:
                    logging.debug('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))

    return solution_set


def solve(
        autoscale=True,
        bvp=None,
        bvp_algo=None,
        guess_gen=None,
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
    logging.debug('python:\t\t' + str(sys.version_info[0]) + '.' + str(sys.version_info[1])
                  + '.' + str(sys.version_info[2]))
    logging.debug('scipy:\t\t' + str(scipy_version))
    logging.debug('sympy:\t\t' + str(sympy_version))

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

    f_ocp = compile_problem(ocp, use_control_arg=True)

    logging.debug('Using ' + str(n_cpus) + '/' + str(pathos.multiprocessing.cpu_count()) + ' CPUs. ')

    if bvp is None:
        # bvp, ocp_map, ocp_map_inverse = ocp2bvp(ocp, method=method, optim_options=optim_options)
        logging.debug("Computing the necessary conditions of optimality")
        if method == 'indirect' or method == 'traditional' or method == 'brysonho' or method == 'diffyg':
            bvp = compile_indirect(copy.copy(ocp), **optim_options)
        elif method == 'direct':
            bvp = compile_direct(copy.copy(ocp), **optim_options)
        else:
            raise NotImplementedError
        logging.debug('Resulting BVP problem:')
        logging.debug(bvp.__repr__())

        ocp_map = bvp.map_sol
        ocp_map_inverse = bvp.inv_map_sol

    else:
        if ocp_map is None or ocp_map_inverse is None:
            raise ValueError('BVP problem must have an associated \'ocp_map\' and \'ocp_map_inverse\'')

    solinit = Trajectory()
    solinit.const = np.array(getattr_from_list(bvp.constants, 'default_val'))

    solinit = guess_gen.generate(bvp.functional_problem, solinit, ocp_map, ocp_map_inverse)

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

    # quad_names = bvp.raw['quads']
    # n_quads = len(quad_names)
    # if n_quads > 0:
    #     initial_quads = solinit.q[0, :]
    #     terminal_quads = solinit.q[-1, :]
    #     initial_bc = dict(zip(quad_names, initial_quads))
    #     terminal_bc = dict(zip(quad_names, terminal_quads))
    #
    #     for ii, bc0 in enumerate(initial_bc):
    #         if bc0 + '_0' in bvp.raw['constants']:
    #             jj = bvp.raw['constants'].index(bc0 + '_0')
    #             solinit.k[str(ii) + '_0'] = initial_bc[bc0]
    #
    #     for ii, bcf in enumerate(terminal_bc):
    #         if bcf + '_f' in bvp.raw['constants']:
    #             jj = bvp.raw['constants'].index(bcf + '_f')
    #             solinit.k[jj] = terminal_bc[bcf]

    """
    Main continuation process
    """
    time0 = time.time()
    continuation_set = run_continuation_set(bvp_algo, steps, solinit, bvp, pool, autoscale)
    total_time = time.time() - time0
    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algo.close()

    """
    Post processing and output
    """
    out = postprocess(continuation_set, f_ocp, bvp, ocp_map_inverse)

    if pool is not None:
        pool.close()

    if save_sols or (isinstance(save_sols, str)):
        if isinstance(save_sols, str):
            filename = save_sols
        else:
            filename = 'data.beluga'

        save(ocp=ocp, bvp=bvp, bvp_solver=bvp_algorithm, sol_set=out, filename=filename)

    return out


def postprocess(continuation_set, ocp, bvp, ocp_map_inverse):
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

    # Calculate the cost for each trajectory
    # for cont_num, continuation_step in enumerate(out):
    #     for sol_num, sol in enumerate(continuation_step):
    #         c0 = ocp.initial_cost(np.array([sol.t[0]]), sol.y[0], sol.u[0], sol.p, sol.const)
    #         cf = ocp.terminal_cost(np.array([sol.t[-1]]), sol.y[-1], sol.u[-1], sol.p, sol.const)
    #         cpath = ocp.path_cost(np.array([sol.t[0]]), sol.y[0], sol.u[0], sol.p, sol.const)
    #         for ii in range(len(sol.t) - 1):
    #             cpath = np.hstack(
    #                 (cpath, ocp.path_cost(np.array([sol.t[ii+1]]), sol.y[ii+1], sol.u[ii+1], sol.p, sol.const)))
    #
    #         cpath = integrate.simps(cpath, sol.t)
    #         sol.cost = c0 + cpath + cf

    return out
