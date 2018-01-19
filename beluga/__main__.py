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
import os
import sys
import logging
import importlib

import docopt

def load_scenario(scenario_name):
    """Loads a scenario from python module name or file name/path"""
    # TODO: Log error messages on failure

    # Check if a python filename was given
    if scenario_name.endswith('.py') and os.path.exists(scenario_name) and os.path.isfile(scenario_name):
        module_dir, module_file = os.path.split(scenario_name)
        module_name, module_ext = os.path.splitext(module_file)
        sys.path.append(module_dir)
    elif (scenario_name.endswith('.yml') or scenario_name.endswith('.json'))and os.path.exists(scenario_name) and os.path.isfile(scenario_name):
        print('Loading from YAML scenario ..')
        return load_yaml(scenario_name)
    else:
        if scenario_name.isidentifier():
            sys.path.append(os.getcwd())
            module_name = scenario_name
        else:
            print('Invalid scenario filename or module name')
            return None
    try:
        scenario = importlib.import_module(module_name)
         # Check if module has a get_problem() function
        # if hasattr(scenario,'get_problem') and callable(scenario.get_problem):
        #     # Module loaded successfully
        #     # print('Module loaded successfully. 😂')
        #     return scenario.get_problem()
        # else:
        #     print('Unable to find get_problem function in scenario module')
        #     return None

    except ImportError as e:
        print('Error loading scenario: ')
        import traceback
        traceback.print_exc(e)
        return None


def main():
    options = docopt.docopt(__doc__,version=0.1)

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


    import builtins
    # import beluga
    beluga = sys.modules['beluga']
    builtins.beluga = beluga

    beluga.setup_beluga(logging_level=logging_lvl, display_level=display_lvl, output_file=output)

    scenario = load_scenario(options['SCENARIO'].strip())
    if scenario is None:
        return
