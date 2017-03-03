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
from beluga.utils import *
from beluga.optim import *

import matplotlib.pyplot as plt
import numpy as np
import sys,os,imp,inspect,warnings,copy
import scipy.optimize

from beluga.continuation import *
from beluga.bvpsol import algorithms
from beluga.problem2 import Problem
import dill, logging


config = dict(logfile='beluga.log', default_bvp_solver='SingleShooting')
problem = Problem()

def init_logging(logging_level, display_level):
    """Initializes the logging system"""
    # Define custom formatter class that formats messages based on level
    # Ref: http://stackoverflow.com/a/8349076/538379
    class InfoFormatter(logging.Formatter):
        """Custom logging formatter to output info messages by themselves"""
        info_fmt = '%(message)s'
        def format(self, record):
            # Save the original format configured by the user
            # when the logger formatter was instantiated
            format_orig = self._fmt

            # Replace the original format with one customized by logging level
            if record.levelno == logging.INFO:
                self._fmt = self.info_fmt
                # For Python>3.2
                self._style = logging.PercentStyle(self._fmt)

            # Call the original formatter class to do the grunt work
            result = logging.Formatter.format(self, record)

            # Restore the original format configured by the user
            self._fmt = format_orig
            # For Python>3.2
            self._style = logging.PercentStyle(self._fmt)

            return result

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(config['logfile'])
    fh.setLevel(logging_level)

    # Set default format string based on logging level
    # TODO: Change this to use logging configuration file?
    if logging_level == logging.DEBUG:
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s-%(module)s#%(lineno)d-%(funcName)s(): %(message)s')
    else:
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s-%(filename)s:%(lineno)d: %(message)s')

    # Create logging handler for console output
    ch = logging.StreamHandler(sys.stdout)
    # Set console logging level and formatter
    ch.setLevel(display_level)
    formatter = InfoFormatter('%(filename)s:%(lineno)d: %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

def run_solver(problem, logging_level=logging.INFO, display_level=logging.INFO, output_file=None):
    """!
    \brief     Returns Beluga object.
    \details   Takes a problem statement, instantiates a solver object and begins
                the solution process.
    """

    # Get reference to the input file module
    frm = inspect.stack()[1]
    input_module = (inspect.getmodule(frm[0]))

    # Get information about input file
    info = inspect.getframeinfo(frm[0])

    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Include configuration file path
    # sys.path.append(cls.config.getroot())

    # TODO: Get default solver options from configuration or a defaults file
    if problem.bvp_solver is None:
        # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)
        problem.bvp_solver = get_algorithm(config['default_bvp_solver'])
        # problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False, number_arcs=2)

    # # Set the cache directory to be in the current folder
    # cache_dir = os.getcwd()+'/_cache'
    # # cache_dir = os.path.dirname(info.filename)+'/_cache'
    # try:
    #     os.mkdir(cache_dir)
    # except:
    #     pass
    # problem.bvp_solver.set_cache_dir(cache_dir)

    # Initialize logging system
    init_logging(logging_level,display_level)

    # Set the output file name
    if output_file is not None:
        problem.output_file = output_file

    solve(problem)
    return

def solve(problem):
    """
    Solves the OCP
    """

    # Initialize necessary conditions of optimality object
    # print("Computing the necessary conditions of optimality")
    logging.info("Computing the necessary conditions of optimality")
    nec_cond = NecessaryConditions()

    # Try loading cached BVP from disk
    # bvp = self.nec_cond.load_bvp(self.problem)
    # if bvp is None:
    #     # Create corresponding boundary value problem
    #     bvp = self.nec_cond.get_bvp(self.problem)
    #     self.nec_cond.cache_bvp(self.problem)
    bvp = nec_cond.get_bvp(problem)

    # TODO: Implement other types of initial guess depending on data type
    #       Array: Automatic?
    #       Guess object: Directly use
    #       Function handle: Call function
    #       String: Load file?

    # The initial guess is automatically stored in the bvp object
    # solinit is just a reference to it
    solinit = problem.guess.generate(bvp)

    # includes costates
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
    out['solution'] = run_continuation_set(problem.steps, bvp)
    total_time = toc();

    logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)

    # Save data
    with open(problem.output_file, 'wb') as outfile:
    # dill.settings['recurse'] = True
        dill.dump(out, outfile) # Dill Beluga object only


    # plt.title('Solution for Brachistochrone problem')
    # plt.plot(self.out['solution'][-1][1,:]*180/pi,self.out['solution'][-1][0,:]/1000)
    # plt.xlabel('theta')
    # plt.ylabel('h')
    # plt.show()

# TODO: Refactor how code deals with initial guess
def run_continuation_set(problem, bvp_start):
    # Loop through all the continuation steps
    solution_set = []

    # Initialize scaling
    s = problem.scale
    steps = problem.steps

    s.initialize(problem,nec_cond.problem_data)
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
                sol = problem.bvp_solver.solve(bvp)

                s.unscale(bvp)
                if sol.converged:
                    # Post-processing phase
                    # Compute control history
                    # sol.u = np.zeros((len(self.nec_cond.problem_data['control_list']),len(sol.x)))

                    # Required for plotting to work with control variables
                    sol.ctrl_expr = self.nec_cond.problem_data['control_options']
                    sol.ctrl_vars = self.nec_cond.problem_data['control_list']

                    #TODO: Make control computation more efficient
                    # for i in range(len(sol.x)):
                    #     _u = bvp.control_func(sol.x[i],sol.y[:,i],sol.parameters,sol.aux)
                    #     sol.u[:,i] = _u
                    ## DAE mode
                    sol.u = sol.y[self.nec_cond.problem_data['num_states']:,:]
                    # f = lambda _t, _X: bvp.control_func(_t,_X,sol.parameters,sol.aux)
                    # sol.u = np.array(list(map(f, sol.x, list(sol.y.T)))).T

                    # Update solution for next iteration
                    solution_set[step_idx].append(copy.deepcopy(bvp.solution))

                    elapsed_time = toc()
                    logging.info('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                else:
                    elapsed_time = toc()
                    logging.info('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))
    except Exception as e:
        # import traceback
        # traceback.print_exc()
        logging.error('Exception : '+str(e))
        logging.error('Stopping')

    return solution_set

def get_algorithm(algo, **kwargs):
    """
    Helper method to load algorithm by name
    """
    # Load algorithm from the package
    for name, obj in inspect.getmembers(algorithms):
        if inspect.isclass(obj):
            if name.lower() == algo.lower():
                return obj(**kwargs)
    else:
        # Raise exception if the loop completes without finding an algorithm
        # by the given name
        raise ValueError('Algorithm '+algo+' not found')


def build_problem(name):
    """
    Helper method to create new problem object
    """
    global problem
    problem.name = name
    return problem

def load_scenario(scenario_name):
    """Loads a scenario from python module name or file name/path"""
    # TODO: Log error messages on failure

    # Check if a python filename was given
    if scenario_name.endswith('.py') and os.path.exists(scenario_name) and os.path.isfile(scenario_name):
        module_dir, module_file = os.path.split(scenario_name)
        module_name, module_ext = os.path.splitext(module_file)
        sys.path.append(module_dir)
    # elif (scenario_name.endswith('.yml') or scenario_name.endswith('.json'))and os.path.exists(scenario_name) and os.path.isfile(scenario_name):
    #     # print('Loading from YAML scenario ..')
    #     return load_yaml(scenario_name)
    else:
        if scenario_name.isidentifier():
            module_name = scenario_name
        else:
            print('Invalid scenario filename or module name')
            return None
    try:
        scenario = importlib.import_module(module_name)
         # Check if module has a get_problem() function
        if hasattr(scenario,'get_problem') and callable(scenario.get_problem):
            # Module loaded successfully
            # print('Module loaded successfully. 😂')
            return scenario.get_problem()
        else:
            print('Unable to find get_problem function in scenario module')
            return None

    except ImportError:
        print('Scenario module not found')
        return None

def main():
    global problem
    options = docopt(__doc__,version=0.1)

    # if options['--config']:
    #     import beluga.BelugaConfig as BelugaConfig
    #     BelugaConfig(run_tool=True)
    #     return

    scenario = load_scenario(options['SCENARIO'].strip())
    if scenario is None:
        return

    levels = {  'ALL': logging.DEBUG,
                'DEBUG': logging.DEBUG,
                '0': logging.DEBUG,
                'INFO': logging.INFO,
                '1': logging.INFO,
                'WARNING': logging.WARN,
                'WARN': logging.WARN,
                '2': logging.WARN,
                'ERROR': logging.ERROR,
                '3': logging.ERROR,
                'CRITICAL': logging.CRITICAL,
                '4': logging.CRITICAL,
                'OFF': logging.CRITICAL + 1}

    # Process logging options
    if options['--nolog']:
        # Suppress all logging
        options['--log'][0] = 'off'

    if options['--log'][0].upper() not in levels:
        print('Invalid value specified for logging level')
        return
    logging_lvl = levels[options['--log'][0].upper()]

    # Process console output options
    if options['-q']:
        # Suppress all console output
        options['--display'][0] = 'off'

    if options['--display'][0].upper() not in levels:
        print('Invalid value specified for display level')
        return
    display_lvl = levels[options['--display'][0].upper()]

    if len(options['--output']) > 0:
        output = os.path.abspath(options['--output'][0].strip())
        # Check if the file locaton is writeable
        if not os.access(os.path.dirname(output), os.W_OK):
            print('Unable to access output file location or invalid filename 😭 😭')
            return
    else:
        output = None

    run(scenario, logging_level=logging_lvl, display_level=display_lvl, output_file=output)
    # print(options)


if __name__ == '__main__':
    main()
