import os
import sys
import logging


def root():
    """Returns beluga installation path."""
    return os.path.dirname(__file__)


def init_logging(display_level=logging.INFO, file_level=logging.NOTSET, filename='beluga.log'):

    logging_level = min(display_level, file_level)

    beluga_logger = logging.getLogger('beluga')
    beluga_logger.setLevel(logging_level)
    beluga_logger.propagate = False
    beluga_logger.display_level_ = display_level

    beluga_logger.handlers = []

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


logger = init_logging()
