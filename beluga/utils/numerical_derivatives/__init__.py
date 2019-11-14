from .finite_diff import gen_fin_diff

import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]


def gen_num_diff(func, arg_idx, method='c_diff', order=1, step_size=1e-6):

    if order == 0:
        return func

    if method == 'f_diff':
        num_diff = gen_fin_diff(func, step_size=step_size/order, method='forward')
    elif method == 'c_diff':
        pass
    else:
        raise NotImplementedError('Differentiation method {} is not implemented.'.format(method))

    return num_diff
