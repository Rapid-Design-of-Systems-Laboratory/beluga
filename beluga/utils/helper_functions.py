from typing import Iterable

import numpy as np


def tuplefy(iter_var):

    if isinstance(iter_var, Iterable):
        iter_var = tuple([tuplefy(item) for item in iter_var])

    return iter_var


def max_mag(arr: np.ndarray, axis=0):
    if arr is None:
        return np.array([])
    elif not isinstance(arr, Iterable):
        return abs(arr)
    elif not isinstance(arr, np.ndarray):
        arr = np.array(arr)

    if arr.size == 0:
        return np.array([])
    else:
        return np.max(np.fabs(arr), axis=axis)


def recursive_sub(expr, replace):
    for _ in range(0, len(replace) + 1):
        new_expr = expr.subs(replace)
        if new_expr == expr:
            return new_expr, True
        else:
            expr = new_expr

    return expr, False
