from .complex_step import gen_csd
from .finite_diff import gen_fin_diff


def gen_num_diff(func, order=(1,), method='c_diff', step_size=1e-6):

    step_mult = 10**sum(order)

    if max(order) == 0:
        diff_func = func
    elif method == 'f_diff':
        diff_func = gen_fin_diff(func, deriv_order=order, step_size=step_size * step_mult, method='forward')
    elif method == 'b_diff':
        diff_func = gen_fin_diff(func, deriv_order=order, step_size=step_size * step_mult, method='backward')
    elif method == 'c_diff':
        diff_func = gen_fin_diff(func, deriv_order=order, step_size=step_size * step_mult, method='central')
    elif method == 'csd':
        diff_func = gen_csd(func, deriv_order=order, step_size=step_size * step_mult)
    else:
        raise NotImplementedError('Differentiation method {} is not implemented.'.format(method))

    return diff_func
