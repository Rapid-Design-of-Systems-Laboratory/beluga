import logging
import sys
import warnings

"""
This file contains functions to enable logging
"""


def add_logger(display_level: int = logging.INFO, file_level: int = logging.NOTSET, filename: str = 'beluga.log',
               suppress_warinings: bool = False) -> logging.Logger:
    """
    Initializes logger to display information about solver.

    Setting logging level to `logging.INFO` will show continuation progress with progress bars.
    Setting logging level to `logging.DEBUG` will show additional information about the symbolic manipulation as well
    as more detail about each bvp solver call

    :param display_level: Level of information to output to console.
    :param file_level: Level of information to store to log file
    :param filename: Name of log file
    :param suppress_warinings: Specify whether or not to ignore warnings from external function (e.g. SciPy's solve_bvp)
    :return: Logger for beluga processes

    :Example:

    >> beluga.add_logger(display_level=logging.INFO, file_level=logging.DEBUG, filename='space_shuttle.log')

    .. warning:: Logging to file with level logging.INFO will render each step of the progess bars on a different line.

    """

    if suppress_warinings:
        warnings.filterwarnings("ignore")

    if display_level > logging.NOTSET and file_level > logging.NOTSET:
        logging_level = min(display_level, file_level)
    else:
        logging_level = max(display_level, file_level, logging.NOTSET)

    beluga_logger = logging.getLogger('beluga')
    beluga_logger.setLevel(logging_level)
    beluga_logger.propagate = False
    beluga_logger.display_level_ = display_level

    beluga_logger.handlers = []

    if display_level > logging.NOTSET:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(display_level)
        ch_formatter = logging.Formatter('%(filename)s:%(lineno)d: %(message)s')
        ch.setFormatter(ch_formatter)
        beluga_logger.addHandler(ch)

    if file_level > logging.NOTSET:
        config = {'filename': filename, 'mode': 'w', 'delay': True}
        fh = logging.FileHandler(**config)
        fh.setLevel(file_level)
        fh_formatter = logging.Formatter('%(filename)s:%(lineno)d: %(message)s')
        fh.setFormatter(fh_formatter)
        beluga_logger.addHandler(fh)

    return beluga_logger


def fit_string(s: str, width: int, justification='center') -> str:
    """
    Fit string to specified width.

    .. note:: Original usage for displaying continuation step information for logging

    :param s: String to be fit within space
    :param width: Width of output string
    :param justification: Justification of original string if size is less than width (`'left'`, `'center'`, `'right'`)
    :return: String of specified width
    """

    if len(s) > width:
        return s[:width - 3] + '...'
    elif justification == 'left':
        return s.ljust(width, ' ')
    elif justification == 'center':
        return s.center(width, ' ')
    elif justification == 'right':
        return s.rjust(width, ' ')
    else:
        raise ValueError('justification should be set to ''left'', ''right'', or ''center''')


def make_a_splash() -> str:
    """
    Creates string with splash of whale art and version info of beluga, Python, and important packages for debugging

    :return: Splash string
    """

    # Display useful info about the environment to debug logger.
    from beluga import __splash__
    from beluga import __version__ as beluga_version
    from llvmlite import __version__ as llvmlite_version
    from numba import __version__ as numba_version
    from numpy import __version__ as numpy_version
    from scipy import __version__ as scipy_version
    from sympy.release import __version__ as sympy_version

    splash_str = \
        '\n{}\n\n' \
        'beluga:\t\t{}\n' \
        'python:\t\t{}.{}.{}\n' \
        'llvmlite:\t{}\n' \
        'numba:\t\t{}\n' \
        'numpy:\t\t{}\n' \
        'scipy:\t\t{}\n' \
        'sympy:\t\t{}\n\n'\
        .format(__splash__, beluga_version, *sys.version_info[:3], llvmlite_version, numba_version, numpy_version,
                scipy_version, sympy_version)

    return splash_str


# Sets logger's default values
logger = add_logger()
