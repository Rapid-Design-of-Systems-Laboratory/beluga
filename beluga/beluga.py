import inspect
import sys
import warnings
import copy
# import logging

# from beluga.codegen import *
from tqdm import tqdm

# import numpy as np

from beluga import problem, helpers
from beluga.codegen.codegen import *
import beluga.bvpsol as bvpsol
from beluga.release import __splash__
from beluga.ivpsol import Trajectory
from beluga.utils import save
# from beluga.optimlib.direct import ocp_to_bvp as DIRECT_ocp_to_bvp
# from beluga.optimlib.indirect import ocp_to_bvp as BH_ocp_to_bvp
# from beluga.optimlib.diffyg_deprecated import ocp_to_bvp as DIFFYG_DEP_ocp_to_bvp
import time
import pathos
import scipy.integrate as integrate

config = dict(logfile='beluga.log', default_bvp_solver='spbvp')


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
    Helper method to load prob algorithm by name.

    :param name: The name of the prob algorithm
    :keywords: Additional keyword arguments passed into the prob solver.
    :return: An instance of the prob solver.
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


def run_continuation_set(bvp_algo, steps, solinit, bvp, pool, autoscale):
    """
    Runs a continuation set for the BVP problem.

    :param bvp_algo: BVP algorithm to be used.
    :param steps: The steps in a continuation set.
    :param solinit: Initial guess for the first problem in steps.
    :param s_bvp: The raw boundary-value problem.
    :param f_bvp: The compiled boundary-value problem.
    :param pool: A processing pool, if available.
    :param scaling: Scaling tool.
    :param autoscale: Whether or not scaling is used.
    :return: A set of solutions for the steps.
    """
    # Loop through all the continuation steps
    solution_set = []
    # Initialize scaling
    s = scaling

    # Load the derivative function into the prob algorithm
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
            logging.debug('\nRunning Continuation Step #{} ({})'.format(step_idx+1, step)+' : ')
            # logging.debug('Number of Iterations\t\tMax BC Residual\t\tTime to Solution')
            solution_set.append([])
            # Assign solution from last continuation set
            step.reset()
            step.init(sol_guess, s_bvp)
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
                    qa = sol.q[0, :]
                    qb = sol.q[-1, :]
                else:
                    qa = np.array([])
                    qb = np.array([])

                if sol.u.size > 0:
                    ua = sol.u[0,:]
                    ub = sol.u[-1,:]
                else:
                    ua = np.array([])
                    ub = np.array([])

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
    | prob                    | None            | codegen'd BVPs                        |
    +------------------------+-----------------+---------------------------------------+
    | bvp_algorithm          | None            | prob algorithm                         |
    +------------------------+-----------------+---------------------------------------+
    | guess_generator        | None            | guess generator                       |
    +------------------------+-----------------+---------------------------------------+
    | initial_helper         | False           | bool                                  |
    +------------------------+-----------------+---------------------------------------+
    | method                 | 'traditional'   | string                                |
    +------------------------+-----------------+---------------------------------------+
    | n_cpus                 | 1               | integer                               |
    +------------------------+-----------------+---------------------------------------+
    | prob                    | None            | :math:`\\Sigma`                       |
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
    bvp = kwargs.get('prob', None)
    bvp_algorithm = kwargs.get('bvp_algorithm', None)
    guess_generator = kwargs.get('guess_generator', None)
    initial_helper = kwargs.get('initial_helper', False)
    method = kwargs.get('method', 'traditional')
    n_cpus = int(kwargs.get('n_cpus', 1))
    ocp = kwargs.get('prob', None)
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
            u = np.array([bvp.compute_u(sol.y[0], sol.dynamical_parameters, sol.const)])
            for ii in range(len(sol.t) - 1):
                u = np.vstack((u, bvp.compute_u(sol.y[ii + 1], sol.dynamical_parameters, sol.const)))
            sol.u = u

            tempset.append(ocp_map_inverse(sol))
        out.append(tempset)

    # Calculate the cost for each trajectory
    for cont_num, continuation_step in enumerate(out):
        for sol_num, sol in enumerate(continuation_step):
            c0 = ocp.initial_cost(np.array([sol.t[0]]), sol.y[0], sol.u[0], sol.dynamical_parameters, sol.const)
            cf = ocp.terminal_cost(np.array([sol.t[-1]]), sol.y[-1], sol.u[-1], sol.dynamical_parameters, sol.const)
            cpath = ocp.path_cost(np.array([sol.t[0]]), sol.y[0], sol.u[0], sol.dynamical_parameters, sol.const)
            for ii in range(len(sol.t) - 1):
                cpath = np.hstack((cpath, ocp.path_cost(np.array([sol.t[ii+1]]), sol.y[ii+1], sol.u[ii+1], sol.dynamical_parameters, sol.const)))

            cpath = integrate.simps(cpath, sol.t)
            sol.cost = c0 + cpath + cf

    return out
