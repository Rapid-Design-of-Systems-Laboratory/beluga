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
from .utils import tic, toc
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
    """
    num_cpus = int(kwargs.get('num_cpus', 1))

    if num_cpus < 1:
        raise ValueError('Number of cpus must be greater than 1.')

    if num_cpus > 1:
        logging.debug('Starting processing pool with ' + str(num_cpus) + 'cpus... ')
        pool = pathos.multiprocessing.Pool(processes=num_cpus)
        logging.debug('Done.')
    else:
        pool = None

    output_file = config['output_file']
    logging.info("Computing the necessary conditions of optimality")

    if method.lower() == 'traditional' or method.lower() == 'brysonho':
        ocp_ws = BH_ocp_to_bvp(ocp, guess_generator)
    elif method.lower() == 'icrm':
        ocp_ws = ICRM_ocp_to_bvp(ocp, guess_generator)
    else:
        raise NotImplementedError

    ocp_ws['problem'] = ocp
    ocp_ws['guess'] = guess_generator
    ocp_ws['problem_data']['custom_functions'] = ocp.custom_functions()
    solinit = Solution()

    solinit.aux['const'] = OrderedDict((str(const),float(val)) for const, val in zip(ocp_ws['constants'], ocp_ws['constants_value']))
    for const in ocp_ws['problem_data']['constants']:
        if not str(const) in solinit.aux['const'].keys():
            solinit.aux['const'][str(const)] = 0

    solinit.aux['dynamical_parameters'] = [str(p) for p in ocp_ws['problem_data']['dynamical_parameters']]
    solinit.aux['nondynamical_parameters'] = [str(p) for p in ocp_ws['problem_data']['nondynamical_parameters']]

    bvp = preprocess(ocp_ws['problem_data'])
    solinit = ocp_ws['guess'].generate(bvp, solinit)

    state_names = ocp_ws['problem_data']['state_list']

    initial_states = solinit.y[0, :]
    terminal_states = solinit.y[-1, :]

    initial_bc = dict(zip(state_names,initial_states))
    terminal_bc = dict(zip(state_names,terminal_states))

    for ii in initial_bc:
        if ii+'_0' in solinit.aux['const'].keys():
            solinit.aux['const'][ii+'_0'] = initial_bc[ii]

    for ii in terminal_bc:
        if ii+'_f' in solinit.aux['const'].keys():
            solinit.aux['const'][ii+'_f'] = terminal_bc[ii]

    tic()
    # TODO: Start from specific step for restart capability
    # TODO: Make class to store result from continuation set?
    out = dict()

    out['problem_data'] = ocp_ws['problem_data']

    ocp._scaling.initialize(ocp_ws)
    ocp_ws['scaling'] = ocp._scaling

    out['solution'] = run_continuation_set(ocp_ws, bvp_algorithm, steps, solinit, bvp, pool)
    total_time = toc()

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)
    bvp_algorithm.close()

    # Final time is appended as a parameter, so scale the output x variables to show the correct time
    for continuation_set in out['solution']:
        for sol in continuation_set:
            tf_ind = [i for i, s in enumerate(out['problem_data']['dynamical_parameters']) if str(s) is 'tf'][0]
            tf = sol.dynamical_parameters[tf_ind]
            sol.t = sol.t*tf

    # Save data
    # del out['problem_data']['s_list']
    del out['problem_data']['states']
    del out['problem_data']['costates']

    qvars = out['problem_data']['quantity_vars']
    qvars = {str(k): str(v) for k, v in qvars.items()}
    out['problem_data']['quantity_vars'] = qvars

    if pool is not None:
        pool.close()

    with open(output_file, 'wb') as outfile:
        pickle.dump(out, outfile)

    return out['solution'][-1][-1]


def run_continuation_set(ocp_ws, bvp_algo, steps, solinit, bvp, pool):
    # Loop through all the continuation steps
    solution_set = []
    # Initialize scaling
    s = ocp_ws['scaling']
    problem_data = ocp_ws['problem_data']

    # Load the derivative function into the bvp algorithm
    bvp_algo.set_derivative_function(bvp.deriv_func)
    bvp_algo.set_quadrature_function(None)
    bvp_algo.set_boundarycondition_function(bvp.bc_func)
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
                tic()

                s.compute_scaling(sol_guess)
                sol_guess = s.scale(sol_guess)

                sol = bvp_algo.solve(sol_guess, pool=pool)
                step.last_sol.converged = sol.converged
                sol = s.unscale(sol)

                if sol.converged:
                    # Post-processing phase

                    # Compute control history, since its required for plotting to work with control variables
                    sol.ctrl_expr = problem_data['control_options']
                    sol.ctrl_vars = problem_data['controls']

                    # TODO: Make control computation more efficient
                    # for i in range(len(sol.x)):
                    #     _u = bvp.control_func(sol.x[i],sol.y[:,i],sol.parameters,sol.aux)
                    #     sol.u[:,i] = _u

                    ## DAE mode
                    # sol.u = sol.y[problem_data['num_states']:,:]
                    # Non-DAE:
                    f = lambda _t, _X: bvp.compute_control(_t, _X, sol.dynamical_parameters, sol.aux)
                    sol.u = np.array(list(map(f, sol.t, list(sol.y))))
                    # keyboard()

                    # Copy solution object for storage and reuse `sol` in next
                    # iteration
                    solution_set[step_idx].append(copy.deepcopy(sol))
                    sol_guess = copy.deepcopy(sol)
                    elapsed_time = toc()
                    logging.info('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                else:
                    elapsed_time = toc()
                    logging.info('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))
    except Exception as e:
        import traceback
        traceback.print_exc()
        logging.error('Exception : ' + str(e))
        logging.error('Stopping')

    return solution_set
