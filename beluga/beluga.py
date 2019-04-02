import inspect
import warnings
import copy

from beluga.codegen.codegen import *

import numpy as np

from beluga import problem, helpers
import beluga.bvpsol as bvpsol
from beluga.ivpsol import Trajectory
from beluga.optimlib.indirect import ocp_to_bvp as BH_ocp_to_bvp
from beluga.optimlib.diffyg import ocp_to_bvp as DIFFYG_ocp_to_bvp
from beluga.optimlib.direct import ocp_to_bvp as DIRECT_ocp_to_bvp
import time
from collections import OrderedDict
import pathos

config = dict(logfile='beluga.log', default_bvp_solver='Shooting')


def add_logger(logging_level=logging.INFO, display_level=logging.INFO):
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
    guess_gen.setup(*args,**kwargs)
    return guess_gen


def ocp2bvp(ocp, **kwargs):
    """

    :param ocp: The optimal control problem.
    :return: (bvp, map, map_inverse) - A codegen compiled BVP with associated mappings to and from the OCP.
    """

    method = kwargs.get('method', 'indirect').lower()
    optim_options = kwargs.get('optim_options', dict())

    logging.info("Computing the necessary conditions of optimality")
    if method == 'indirect' or method == 'traditional' or method == 'brysonho':
        bvp_raw, _map, _map_inverse = BH_ocp_to_bvp(ocp, **optim_options)
    elif method == 'diffyg':
        bvp_raw, _map, _map_inverse = DIFFYG_ocp_to_bvp(ocp, **optim_options)
    elif method == 'direct':
        bvp_raw, _map, _map_inverse = DIRECT_ocp_to_bvp(ocp, **optim_options)
    else:
        raise NotImplementedError

    bvp_raw['custom_functions'] = ocp.custom_functions()
    bvp = preprocess(bvp_raw)
    bvp.raw = bvp_raw
    ocp._scaling.initialize(bvp.raw)
    bvp.raw['scaling'] = ocp._scaling
    ocp_map = lambda sol: _map(sol, _compute_control=bvp.compute_control)
    ocp_map_inverse = lambda sol: _map_inverse(sol, _compute_control=bvp.compute_control)
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
    bvp_algo.set_quadrature_function(bvp.quad_func)
    bvp_algo.set_boundarycondition_function(bvp.bc_func)
    bvp_algo.set_initial_cost_function(bvp.initial_cost)
    bvp_algo.set_path_cost_function(bvp.path_cost)
    bvp_algo.set_terminal_cost_function(bvp.terminal_cost)
    bvp_algo.set_inequality_constraint_function(bvp.ineq_constraints)

    sol_guess = solinit
    sol = None
    if steps is None:
        logging.info('Solving OCP...')
        time0 = time.time()
        if autoscale:
            s.compute_scaling(sol_guess)
            sol_guess = s.scale(sol_guess)

        sol_guess.const = np.fromiter(sol_guess.aux['const'].values(), dtype=np.float64)
        sol = bvp_algo.solve(sol_guess, pool=pool)

        if autoscale:
            sol = s.unscale(sol)

        solution_set = [[copy.deepcopy(sol)]]
        if sol.converged:
            elapsed_time = time.time() - time0
            logging.info('Problem converged in %0.4f seconds\n' % (elapsed_time))
        else:
            elapsed_time = time.time() - time0
            logging.info('Problem failed to converge!\n')
    else:
        for step_idx, step in enumerate(steps):
            logging.info('\nRunning Continuation Step #'+str(step_idx+1)+' : ')
            solution_set.append([])
            # Assign solution from last continuation set
            step.reset()
            step.init(sol_guess)

            for sol_guess in step:  # Continuation step returns 'aux' dictionary
                # gamma_guess = step.get_closest_gamma(aux)
                # sol_guess.aux = aux

                logging.info('Starting iteration '+str(step.ctr)+'/'+str(step.num_cases()))
                time0 = time.time()

                if autoscale:
                    s.compute_scaling(sol_guess)
                    sol_guess = s.scale(sol_guess)

                sol_guess.const = np.fromiter(sol_guess.aux['const'].values(), dtype=np.float64)
                sol = bvp_algo.solve(sol_guess, pool=pool)

                if autoscale:
                    sol = s.unscale(sol)

                step.add_gamma(sol)

                """
                The following line is overwritten by the looping variable UNLESS it is the final iteration. It is
                required when chaining continuation strategies together. DO NOT DELETE!
                """
                sol_guess = copy.deepcopy(sol)

                if sol.converged:
                    solution_set[step_idx].append(copy.deepcopy(sol))

                    elapsed_time = time.time() - time0
                    logging.info('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                else:
                    elapsed_time = time.time() - time0
                    logging.info('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))

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
    | method                 | 'traditional'   | string                                |
    +------------------------+-----------------+---------------------------------------+
    | n_cpus                 | 1               | integer                               |
    +------------------------+-----------------+---------------------------------------+
    | ocp_map                | None            | :math:`\gamma \rightarrow \gamma`     |
    +------------------------+-----------------+---------------------------------------+
    | ocp_map_inverse        | None            | :math:`\gamma \rightarrow \gamma`     |
    +------------------------+-----------------+---------------------------------------+
    | optim_options          | None            | dict()                                |
    +------------------------+-----------------+---------------------------------------+
    | steps                  | None            | continuation_strategy                 |
    +------------------------+-----------------+---------------------------------------+

    """

    autoscale = kwargs.get('autoscale', True)
    bvp = kwargs.get('bvp', None)
    bvp_algorithm = kwargs.get('bvp_algorithm', None)
    guess_generator = kwargs.get('guess_generator', None)
    method = kwargs.get('method', 'traditional')
    n_cpus = int(kwargs.get('n_cpus', 1))
    ocp = kwargs.get('ocp', None)
    ocp_map = kwargs.get('ocp_map', None)
    ocp_map_inverse = kwargs.get('ocp_map_inverse', None)
    optim_options = kwargs.get('optim_options', dict())
    steps = kwargs.get('steps', None)

    if n_cpus < 1:
        raise ValueError('Number of cpus must be greater than 1.')

    if n_cpus > 1:
        logging.debug('Starting processing pool with ' + str(n_cpus) + 'cpus... ')
        pool = pathos.multiprocessing.Pool(processes=n_cpus)
        logging.debug('Done.')
    else:
        pool = None

    if bvp is None:
        bvp, ocp_map, ocp_map_inverse = ocp2bvp(ocp, method=method, optim_options=optim_options)
        logging.debug('Resulting BVP problem:')
        for key in bvp.raw.keys():
            logging.debug(str(key) + ': ' + str(bvp.raw[key]))

    else:
        if ocp_map is None or ocp_map_inverse is None:
            raise ValueError('BVP problem must have an associated \'ocp_map\' and \'ocp_map_inverse\'')

    solinit = Trajectory()

    solinit.aux['const'] = OrderedDict((const, val) for const, val in zip(bvp.raw['constants'], bvp.raw['constants_values']))
    for const in bvp.raw['constants']:
        if not str(const) in solinit.aux['const'].keys():
            solinit.aux['const'][str(const)] = 0

    solinit = guess_generator.generate(bvp, solinit, ocp_map, ocp_map_inverse)

    state_names = bvp.raw['states']

    initial_states = solinit.y[0, :]
    terminal_states = solinit.y[-1, :]

    initial_bc = dict(zip(state_names,initial_states))
    terminal_bc = dict(zip(state_names,terminal_states))

    if steps is not None:
        for ii in initial_bc:
            if ii + '_0' in solinit.aux['const'].keys():
                solinit.aux['const'][ii + '_0'] = initial_bc[ii]

        for ii in terminal_bc:
            if ii + '_f' in solinit.aux['const'].keys():
                solinit.aux['const'][ii + '_f'] = terminal_bc[ii]

    quad_names = bvp.raw['quads']
    n_quads = len(quad_names)
    if n_quads > 0:
        initial_quads = solinit.q[0, :]
        terminal_quads = solinit.q[-1, :]
        initial_bc = dict(zip(quad_names, initial_quads))
        terminal_bc = dict(zip(quad_names, terminal_quads))

        for ii in initial_bc:
            if ii + '_0' in solinit.aux['const'].keys():
                solinit.aux['const'][ii + '_0'] = initial_bc[ii]

        for ii in terminal_bc:
            if ii + '_f' in solinit.aux['const'].keys():
                solinit.aux['const'][ii + '_f'] = terminal_bc[ii]

    time0 = time.time()

    out = run_continuation_set(bvp_algorithm, steps, solinit, bvp, pool, autoscale)
    total_time = time.time() - time0

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algorithm.close()

    for cont_num, continuation_set in enumerate(out):
        for sol_num, sol in enumerate(continuation_set):
            out[cont_num][sol_num] = ocp_map_inverse(sol)

    if pool is not None:
        pool.close()

    return out
