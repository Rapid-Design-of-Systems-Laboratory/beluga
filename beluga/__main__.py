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
import docopt
def main():
    options = docopt(__doc__,version=0.1)
    print(options)
