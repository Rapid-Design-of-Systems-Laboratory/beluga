from collections import ChainMap
from itertools import zip_longest
import time
import sympy
import platform
from fractions import Fraction as R
from scipy.special import comb
import signal
import cloudpickle as pickle
import beluga


def recursive_sub(expr, replace):
    for _ in range(0, len(replace) + 1):
        new_expr = expr.subs(replace)
        if new_expr == expr:
            return new_expr, True
        else:
            expr = new_expr
    return new_expr, False


def save(ocp=None, bvp=None, bvp_solver=None, sol_set=None, filename='data.blg'):
    assert any([ocp is not None, bvp_solver is not None, sol_set is not None]), 'No data given to save.'

    save_dict = {}
    if ocp is not None:
        assert ocp.__class__ is beluga.problem.OCP, 'ocp should be of beluga.problem.OCP class'
        save_dict['ocp'] = ocp

    if bvp is not None:
        save_dict['bvp'] = bvp

    if bvp_solver is not None:
        assert issubclass(bvp_solver.__class__, beluga.bvpsol.BaseAlgorithm), 'bvp_solver should be subclass ' \
                                                                              'of beluga.bvpsol.BaseAlgorithm'
        save_dict['bvp solver'] = bvp_solver

    if sol_set is not None:
        assert all([sol.__class__ is beluga.ivpsol.ivpsol.Trajectory for cont_set in sol_set for sol in cont_set]),\
            'all solutions in sol_set should be of class beluga.ivpsol.ivpsol.Trajectory'
        save_dict['solutions'] = sol_set

    with open(filename, 'wb') as file:
        pickle.dump(save_dict, file)


def load(filename):
    with open(filename, 'rb') as file:
        save_dict = pickle.load(file)

    return save_dict


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


def _combine_args_kwargs(arg_list, args, kwargs, fillvalue=''):
    """Combines positional and keyword arguments
    Parameters
    ----------
    arg_list - list of str
        List of keys in order of positional arguments
    args - list of str
        List of positional arguments
    kwargs: dict
        Dictionary of keyword arguments
    Returns
    -------
    A dictionary merging kwargs and args with keys from
    from args_list
    Example
    -------
    >>> _combine_args_kwargs(['foo','bar'],[1,2],{'baz':3})
    {'foo':1, 'bar':2, 'baz': 3}
    """
    pos_args = {key: val for (key, val) in zip_longest(arg_list, args, fillvalue=fillvalue)}
    arg_dict = dict(ChainMap(kwargs, pos_args))
    return arg_dict
