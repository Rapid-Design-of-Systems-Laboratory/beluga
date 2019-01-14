import inspect
import warnings
import copy
import logging

from beluga.codegen.codegen import *

import cloudpickle as pickle
import numpy as np
import collections as cl

from beluga import problem, helpers
from beluga.bvpsol import algorithms, Solution
from beluga.optimlib.brysonho import ocp_to_bvp as BH_ocp_to_bvp
from beluga.optimlib.icrm import ocp_to_bvp as ICRM_ocp_to_bvp
from beluga.optimlib.diffyg import ocp_to_bvp as DIFFYG_ocp_to_bvp
from beluga.optimlib.direct import ocp_to_bvp as DIRECT_ocp_to_bvp
import time
from collections import OrderedDict
import pathos

config = dict(logfile='beluga.log',
              default_bvp_solver='Shooting',
              output_file='data.dill')

BVP = cl.namedtuple('BVP', 'deriv_func bc_func compute_control')


def bvp_algorithm(algo, **kwargs):
    """
    Helper method to load algorithm by name
    """
    # Load algorithm from the package
    for name, obj in inspect.getmembers(algorithms):
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


def solve(ocp, method, bvp_algorithm, steps, guess_generator, **kwargs):
    """
    Solves the OCP using specified method

    +------------------------+-----------------+-----------------+
    | Valid kwargs           | Default Value   | Valid Values    |
    +========================+=================+=================+
    | autoscale              | True            | bool            |
    +------------------------+-----------------+-----------------+
    | n_cpus                 | 1               | integer         |
    +------------------------+-----------------+-----------------+

    """

    autoscale = kwargs.get('autoscale', True)
    n_cpus = int(kwargs.get('n_cpus', 1))

    if n_cpus < 1:
        raise ValueError('Number of cpus must be greater than 1.')

    if n_cpus > 1:
        logging.debug('Starting processing pool with ' + str(n_cpus) + 'cpus... ')
        pool = pathos.multiprocessing.Pool(processes=n_cpus)
        logging.debug('Done.')
    else:
        pool = None

    output_file = config['output_file']
    logging.info("Computing the necessary conditions of optimality")

    if method.lower() == 'traditional' or method.lower() == 'brysonho':
        bvp_ws, guess_mapper = BH_ocp_to_bvp(ocp)
    elif method.lower() == 'icrm':
        bvp_ws, guess_mapper = ICRM_ocp_to_bvp(ocp)
    elif method.lower() == 'diffyg':
        bvp_ws, guess_mapper = DIFFYG_ocp_to_bvp(ocp)
    elif method.lower() == 'direct':
        bvp_ws, guess_mapper = DIRECT_ocp_to_bvp(ocp)
    else:
        raise NotImplementedError

    logging.debug('Resulting BVP problem:')
    for key in bvp_ws.keys():
        logging.debug(str(key) + ': ' + str(bvp_ws[key]))

    bvp_ws['problem'] = ocp
    bvp_ws['guess'] = guess_generator
    bvp_ws['custom_functions'] = ocp.custom_functions()
    solinit = Solution()

    solinit.aux['const'] = OrderedDict((const, val) for const, val in zip(bvp_ws['constants'], bvp_ws['constants_values']))
    for const in bvp_ws['constants']:
        if not str(const) in solinit.aux['const'].keys():
            solinit.aux['const'][str(const)] = 0

    solinit.aux['dynamical_parameters'] = bvp_ws['dynamical_parameters']
    solinit.aux['nondynamical_parameters'] = bvp_ws['nondynamical_parameters']

    bvp, initial_cost, path_cost, terminal_cost, ineq_constraints = preprocess(bvp_ws)
    solinit = bvp_ws['guess'].generate(bvp, solinit, guess_mapper)

    state_names = bvp_ws['states']

    initial_states = solinit.y[0, :]
    terminal_states = solinit.y[-1, :]

    initial_bc = dict(zip(state_names,initial_states))
    terminal_bc = dict(zip(state_names,terminal_states))

    for ii in initial_bc:
        if ii + '_0' in solinit.aux['const'].keys():
            solinit.aux['const'][ii + '_0'] = initial_bc[ii]

    for ii in terminal_bc:
        if ii + '_f' in solinit.aux['const'].keys():
            solinit.aux['const'][ii + '_f'] = terminal_bc[ii]

    quad_names = bvp_ws['quads']
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
    out = dict()

    out['problem_data'] = bvp_ws
    ocp._scaling.initialize(bvp_ws)
    bvp_ws['scaling'] = ocp._scaling

    out['solution'] = run_continuation_set(bvp_ws, bvp_algorithm, steps, solinit, bvp, initial_cost, path_cost, terminal_cost, ineq_constraints, pool, autoscale)
    total_time = time.time() - time0

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algorithm.close()

    # Final time is appended as a parameter, so scale the output x variables to show the correct time
    for continuation_set in out['solution']:
        for sol in continuation_set:
            if autoscale:
                tf_ind = [i for i, s in enumerate(out['problem_data']['dynamical_parameters']) if str(s) is 'tf'][0]
                tf = sol.dynamical_parameters[tf_ind]
                sol.t = sol.t*tf

    if pool is not None:
        pool.close()

    # Save data
    with open(output_file, 'wb') as outfile:
        pickle.dump(out, outfile)

    return out['solution'][-1][-1]


def run_continuation_set(ocp_ws, bvp_algo, steps, solinit, bvp, initial_cost, path_cost, terminal_cost, ineq_constraints, pool, autoscale):
    # Loop through all the continuation steps
    solution_set = []
    # Initialize scaling
    s = ocp_ws['scaling']
    problem_data = ocp_ws

    # Load the derivative function into the bvp algorithm
    bvp_algo.set_derivative_function(bvp.deriv_func)
    bvp_algo.set_quadrature_function(bvp.quad_func)
    bvp_algo.set_boundarycondition_function(bvp.bc_func)
    bvp_algo.set_initial_cost_function(initial_cost)
    bvp_algo.set_path_cost_function(path_cost)
    bvp_algo.set_terminal_cost_function(terminal_cost)
    bvp_algo.set_inequality_constraint_function(ineq_constraints)
    try:
        sol_guess = solinit
        sol = None
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
                        f = lambda _t, _X: bvp.compute_control(_t, _X, sol.dynamical_parameters, sol.aux)
                        sol.u = np.array(list(map(f, sol.t, list(sol.y))))
                    # keyboard()

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
