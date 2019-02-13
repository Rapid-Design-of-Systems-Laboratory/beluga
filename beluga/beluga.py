import inspect
import warnings
import copy
import logging

from beluga.codegen.codegen import *

import numpy as np

from beluga import problem, helpers
import beluga.bvpsol as bvpsol
from beluga.ivpsol import Trajectory
from beluga.optimlib.brysonho import ocp_to_bvp as BH_ocp_to_bvp
from beluga.optimlib.icrm import ocp_to_bvp as ICRM_ocp_to_bvp
from beluga.optimlib.diffyg import ocp_to_bvp as DIFFYG_ocp_to_bvp
from beluga.optimlib.direct import ocp_to_bvp as DIRECT_ocp_to_bvp
import time
from collections import OrderedDict
import pathos

config = dict(logfile='beluga.log', default_bvp_solver='Shooting')

def bvp_algorithm(algo, **kwargs):
    """
    Helper method to load algorithm by name
    """
    # Load algorithm from the package
    for name, obj in inspect.getmembers(bvpsol):
        if inspect.isclass(obj):
            if name.lower() == algo.lower():
                return obj(**kwargs)
    else:
        # Raise exception if the loop completes without finding an algorithm by the given name
        raise ValueError('Algorithm '+algo+' not found')


def guess_generator(*args, **kwargs):
    """
    Helper for creating Initial guess generator.
    """
    guess_gen = problem.GuessGenerator()
    guess_gen.setup(*args,**kwargs)
    return guess_gen


def add_logger(logging_level=logging.INFO, display_level=logging.INFO):
    """
    Performs initial configuration on beluga.
    """
    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Initialize logging system
    helpers.init_logging(logging_level, display_level, config['logfile'])


def set_output_file(output_file=None):
    if output_file is not None:
        config['output_file'] = output_file


def ocp2bvp(ocp, method='traditional'):
    logging.info("Computing the necessary conditions of optimality")
    if method.lower() == 'traditional' or method.lower() == 'brysonho':
        bvp_raw, ocp_map, ocp_map_inverse = BH_ocp_to_bvp(ocp)
    elif method.lower() == 'icrm':
        bvp_raw, ocp_map, ocp_map_inverse = ICRM_ocp_to_bvp(ocp)
    elif method.lower() == 'diffyg':
        bvp_raw, ocp_map, ocp_map_inverse = DIFFYG_ocp_to_bvp(ocp)
    elif method.lower() == 'direct':
        bvp_raw, ocp_map, ocp_map_inverse = DIRECT_ocp_to_bvp(ocp)
    else:
        raise NotImplementedError

    bvp_raw['custom_functions'] = ocp.custom_functions()
    bvp = preprocess(bvp_raw)
    bvp.raw = bvp_raw
    ocp._scaling.initialize(bvp.raw)
    bvp.raw['scaling'] = ocp._scaling

    return bvp, ocp_map, ocp_map_inverse


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
    | steps                  | None            | continuation_strategy                 |
    +------------------------+-----------------+---------------------------------------+

    """

    autoscale = kwargs.get('autoscale', True)
    bvp = kwargs.get('bvp', None)
    bvp_algorithm = kwargs.get('bvp_algorithm', None)
    guess_generator = kwargs.get('guess_generator', None)
    method = kwargs.get('method', 'traditional')
    ocp = kwargs.get('ocp', None)
    ocp_map = kwargs.get('ocp_map', None)
    ocp_map_inverse = kwargs.get('ocp_map_inverse', None)
    n_cpus = int(kwargs.get('n_cpus', 1))
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
        bvp, ocp_map, ocp_map_inverse = ocp2bvp(ocp, method=method)
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

    out = run_continuation_set(bvp.raw, bvp_algorithm, steps, solinit, bvp, pool, autoscale)
    total_time = time.time() - time0

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algorithm.close()

    for cont_num, continuation_set in enumerate(out):
        for sol_num, sol in enumerate(continuation_set):
            out[cont_num][sol_num] = ocp_map_inverse(sol)

    if pool is not None:
        pool.close()

    return out


def run_continuation_set(ocp_ws, bvp_algo, steps, solinit, bvp, pool, autoscale):
    # Loop through all the continuation steps
    solution_set = []
    # Initialize scaling
    s = bvp.raw['scaling']
    problem_data = ocp_ws

    # Load the derivative function into the bvp algorithm
    bvp_algo.set_derivative_function(bvp.deriv_func)
    bvp_algo.set_quadrature_function(bvp.quad_func)
    bvp_algo.set_boundarycondition_function(bvp.bc_func)
    bvp_algo.set_initial_cost_function(bvp.initial_cost)
    bvp_algo.set_path_cost_function(bvp.path_cost)
    bvp_algo.set_terminal_cost_function(bvp.terminal_cost)
    bvp_algo.set_inequality_constraint_function(bvp.ineq_constraints)
    try:
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

            if sol.converged:
                # Post-processing phase

                # Compute control history, since its required for plotting to work with control variables
                sol.ctrl_expr = problem_data['control_options']
                sol.ctrl_vars = problem_data['controls']

                if ocp_ws['method'] is not 'direct':
                    f = lambda _t, _X: bvp.compute_control(_X, sol.dynamical_parameters,
                                                           np.fromiter(sol.aux['const'].values(), dtype=np.float64))
                    sol.u = np.array(list(map(f, sol.t, list(sol.y))))

                solution_set = [[copy.deepcopy(sol)]]
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
                step.init(sol_guess, problem_data)

                for aux in step:  # Continuation step returns 'aux' dictionary
                    sol_guess.aux = aux

                    logging.info('Starting iteration '+str(step.ctr)+'/'+str(step.num_cases()))
                    time0 = time.time()

                    if autoscale:
                        s.compute_scaling(sol_guess)
                        sol_guess = s.scale(sol_guess)

                    sol_guess.const = np.fromiter(sol_guess.aux['const'].values(), dtype=np.float64)
                    sol = bvp_algo.solve(sol_guess, pool=pool)
                    step.last_sol.converged = sol.converged


                    if autoscale:
                        sol = s.unscale(sol)

                    sol_guess = copy.deepcopy(sol)

                    if sol.converged:
                        # Post-processing phase

                        # Compute control history, since its required for plotting to work with control variables
                        sol.ctrl_expr = problem_data['control_options']
                        sol.ctrl_vars = problem_data['controls']

                        if ocp_ws['method'] is not 'direct':
                            f = lambda _t, _X: bvp.compute_control(_X, sol.dynamical_parameters, np.fromiter(sol.aux['const'].values(), dtype=np.float64))
                            sol.u = np.array(list(map(f, sol.t, list(sol.y))))

                        # Copy solution object for storage and reuse `sol` in next
                        # iteration
                        solution_set[step_idx].append(copy.deepcopy(sol))
                        # sol_guess = copy.deepcopy(sol)
                        elapsed_time = time.time() - time0
                        logging.info('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                    else:
                        elapsed_time = time.time() - time0
                        logging.info('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))
    except Exception as e:
        import traceback
        traceback.print_exc()
        logging.error('Exception : ' + str(e))
        logging.error('Stopping')

    return solution_set
