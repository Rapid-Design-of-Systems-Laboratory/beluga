from beluga.bvpsol import algorithms
from beluga import problem

import os
import sys
import inspect
import logging

def initial_guess(*args, **kwargs):
    """Creates initial guess"""
    guess = problem.Guess()
    guess.setup(*args,**kwargs)
    return guess

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
        # Raise exception if the loop completes without finding an algorithm
        # by the given name
        raise ValueError('Algorithm '+algo+' not found')

def solve(ocp, **kwargs):
    """Runs the solver on the given problem package."""
    problem = dict(ocp=ocp, **kwargs)

def root():
    """Get the installation path for beluga."""
    return os.path.dirname(__file__)

def init_logging(logging_level, display_level, logfile):
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

    fh = logging.FileHandler(logfile)
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
