import time
import sympy
import platform
from fractions import Fraction as R
from scipy.special import comb
import signal
# import os
# import sys
# import shutil
# import tempfile
# import subprocess
# import importlib
# import theano
# from functools import partial
# import warnings
# import numpy as np
# import sympy as sm

# https://stackoverflow.com/a/22348885/538379
if platform.system() == 'Windows':
    class timeout:
        def __init__(self, seconds=1, error_message='Timeout'):
            self.seconds = seconds
            self.error_message = error_message

        def handle_timeout(self, signum, frame):
            raise TimeoutError(self.error_message)

        def __enter__(self):
            pass

        def __exit__(self, type_, value, traceback):
            pass
else:
    class timeout:
        def __init__(self, seconds=1, error_message='Timeout'):
            self.seconds = seconds
            self.error_message = error_message

        def handle_timeout(self, signum, frame):
            raise TimeoutError(self.error_message)

        def __enter__(self):
            signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.alarm(self.seconds)

        def __exit__(self, type_, value, traceback):
            signal.alarm(0)

# Source: http://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python
_tstart_stack = []


def Bernoulli(num):
    B = [R(1, 1)]

    def Sum(_m):
        total = R(0, 1)
        for k in range(0, _m):
            total += int(comb(_m, k, exact=False)) * R(B[k], _m-k+1)
        return 1 - total

    m = 1
    while m <= num:
        B.append(Sum(m))
        m += 1
    return float(B[-1])


class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type_, value, traceback):
        if self.name:
            print('[%s]' % self.name,)
        print('Elapsed: %s' % (time.time() - self.tstart))


# Sympify that ignores some built in names
__ignored_sym_func = ['rad', 're']
__ignored_sym = dict((sym, sympy.Symbol(sym)) for sym in __ignored_sym_func)


def sympify(expr, *args, **kwargs):
    """Allows using sympy on expressions with 'reserved' keywords"""
    return sympy.sympify(expr, locals=__ignored_sym, *args, **kwargs)


# Source: http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
def static_var(varname, value):
    """Decorator that defines a static variable inside a function"""
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


def fix_carets(expr):
    """Converts carets to exponent symbol in string"""
    import re as _re
    caret = _re.compile('[\\^]')
    return caret.sub('**', expr)
