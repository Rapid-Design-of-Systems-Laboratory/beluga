#!/usr/bin/env python
"""Beluga Optimal Control Solver.

Usage:
  beluga --config
  beluga (-v | --version)
  beluga (-h | --help)
  beluga SCENARIO
                  [-o | --output <file>]
                  ([--nolog] | [-l | --log <level>])
                  ([-q] | [-d | --display <level>])

Options:
  -h, --help                show this screen and exit
  -v, --version             show version

  Logging options
  -l, --log <level>         specify minimum logging level [default: ERROR]
  -l0,-l1,-l2,-l3,-l4       shortcuts for ALL, INFO, WARN, ERROR and CRITICAL
                            respectively
  -loff, --nolog            suppress logging, equivalent to --log=off

  -q                        quiet mode, equivalent to --display=off
  -d, --display <level>     specify minimum verbose output level [default: INFO]
  -d0,-d1,-d2,-d3,-d4       shortcuts for ALL, INFO, WARN, ERROR and CRITICAL
                            respectively

  -o, --output <file>       specify data file for solution
                            (overrides option specified in input file)

Arguments:
  SCENARIO                  name of python module orpath to python/json/yaml file
                            containing the problem scenario [REQUIRED]

  <file>                    path to the data file for solution
  <level>                   logging level [ALL, INFO, WARN, ERROR, CRITICAL, OFF]

Example:
  Run problem using python module name :
    beluga brachisto

  Run using path to input file:
    beluga /path/to/problem.py

  Specify logging and display levels (0 -> all messages including debug messages)
    beluga -d0 -l0 /path/to/brachisto.py

  Specify output data file
    beluga brachisto --output=brachisto_out.dill

  Run configuration tool
    beluga --config

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.rcac.purdue.edu/RDSL/beluga

"""

from math import *
# from beluga.utils import *

import sys
import os
import inspect
import warnings
import copy
import logging

import dill
import docopt
import numpy as np

# from beluga.continuation import *
from beluga import problem, helpers
from beluga.utils import tic, toc

config = dict(logfile='beluga.log',
              default_bvp_solver='SingleShooting',
              output_file='data.dill')

def setup_beluga(logging_level=logging.INFO, display_level=logging.INFO, output_file=None):
    """Performs initial configuration on beluga."""

    # Get reference to the input file module
    frm = inspect.stack()[1]
    input_module = (inspect.getmodule(frm[0]))

    # Get information about input file
    info = inspect.getframeinfo(frm[0])

    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Initialize logging system
    helpers.init_logging(logging_level,display_level, config['logfile'])

    # Set the output file name
    if output_file is not None:
        config['output_file'] = output_file

    # solve(problem)
    return

def solve(ocp, method, bvp_algorithm, steps, initial_guess):
    """
    Solves the OCP using specified method
    """

    # Initialize necessary conditions of optimality object
    # print("Computing the necessary conditions of optimality")
    logging.info("Computing the necessary conditions of optimality")
    from beluga.optimlib import brysonho

    wf = brysonho.BrysonHo
    workspace = brysonho.init_workspace(ocp)
    ocp_ws = wf(workspace)
    bvp = ocp_ws['bvp']

    # TODO: Try loading cached BVP from disk

    # The initial guess is automatically stored in the bvp object
    # solinit is just a reference to it
    solinit = initial_guess.generate(bvp)

    # # includes costates
    state_names = bvp.problem_data['state_list']
    initial_states = solinit.y[:,0] # First column
    terminal_states = solinit.y[:,-1] # Last column
    initial_bc = dict(zip(state_names,initial_states))
    terminal_bc = dict(zip(state_names,terminal_states))
    bvp.solution.aux['initial'] = initial_bc
    bvp.solution.aux['terminal'] = terminal_bc

    tic()
    # TODO: Start from specific step for restart capability
    # TODO: Make class to store result from continuation set?
    out = {};

    out['problem_data'] = bvp.problem_data;

    ocp._scaling.initialize(ocp_ws)
    ocp_ws['scaling'] = ocp._scaling

    out['solution'] = run_continuation_set(ocp_ws, bvp_algorithm, steps, bvp)
    total_time = toc();

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)

    # Save data
    output_file = 'data.dill'
    with open(output_file, 'wb') as outfile:
    # dill.settings['recurse'] = True
        dill.dump(out, outfile) # Dill Beluga object only


# TODO: Refactor how code deals with initial guess
def run_continuation_set(ocp_ws, bvp_algo, steps, bvp_start):
    # Loop through all the continuation steps
    solution_set = []

    # Initialize scaling
    s = ocp_ws['scaling']
    problem_data = ocp_ws['problem_data']
    try:
        for step_idx,step in enumerate(steps):
            # Assign BVP from last continuation set
            step.reset()
            logging.info('\nRunning Continuation Step #'+str(step_idx+1)+' : ')

            solution_set.append([])
            if step_idx == 0:
                step.set_bvp(bvp_start)
            else:
                # Use the bvp & solution from last continuation set
                step.set_bvp(steps[step_idx-1].bvp)

            for bvp in step:
                logging.info('Starting iteration '+str(step.ctr)+'/'+str(step.num_cases()))
                tic()

                s.compute_scaling(bvp)
                s.scale(bvp)

                # sol is just a reference to bvp.solution
                sol = bvp_algo.solve(bvp)

                s.unscale(bvp)
                if sol.converged:
                    # Post-processing phase
                    # Compute control history
                    # sol.u = np.zeros((len(self.nec_cond.problem_data['control_list']),len(sol.x)))

                    # Required for plotting to work with control variables
                    sol.ctrl_expr = problem_data['control_options']
                    sol.ctrl_vars = problem_data['control_list']

                    #TODO: Make control computation more efficient
                    # for i in range(len(sol.x)):
                    #     _u = bvp.control_func(sol.x[i],sol.y[:,i],sol.parameters,sol.aux)
                    #     sol.u[:,i] = _u
                    ## DAE mode
                    # sol.u = sol.y[problem_data['num_states']:,:]

                    # Non Dae:
                    f = lambda _t, _X: bvp.control_func(_t,_X,sol.parameters,sol.aux)
                    sol.u = np.array(list(map(f, sol.x, list(sol.y.T)))).T

                    # Update solution for next iteration
                    solution_set[step_idx].append(copy.deepcopy(bvp.solution))

                    elapsed_time = toc()
                    logging.info('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                else:
                    elapsed_time = toc()
                    logging.info('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))
    except Exception as e:
        import traceback
        traceback.print_exc()
        logging.error('Exception : '+str(e))
        logging.error('Stopping')

    return solution_set

if __name__ == '__main__':
    main()
