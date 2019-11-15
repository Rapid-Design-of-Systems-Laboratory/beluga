from .finite_diff import gen_fin_diff
import numpy as np


def test_func(x):
    return np.exp(x)/(np.sin(x)**3 + np.cos(x)**3)


def gen_num_diff(func, arg_idx, method='c_diff', order=1, step_size=1e-6):

    if order == 0:
        return func

    if method == 'f_diff':
        num_diff = gen_fin_diff(func,
                                arg_idx=arg_idx, deriv_order=order, step_size=step_size / order, method='forward')
    elif method == 'b_diff':
        num_diff = gen_fin_diff(func,
                                arg_idx=arg_idx, deriv_order=order, step_size=step_size / order, method='backward')
    elif method == 'c_diff':
        num_diff = gen_fin_diff(func,
                                arg_idx=arg_idx, deriv_order=order, step_size=step_size / order, method='central')
    elif method == 'csd':
        num_diff = gen_fin_diff(func, arg_idx=arg_idx, deriv_order=order, step_size=step_size / order)
    else:
        raise NotImplementedError('Differentiation method {} is not implemented.'.format(method))

    return num_diff
