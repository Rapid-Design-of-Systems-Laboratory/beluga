import abc
import logging
import collections as cl
import numba
import sys
import pickle
from beluga.codegen import *


class BaseAlgorithm(object):
    '''
    Object representing an algorithm that solves boundary valued problems.

    This object serves as a base class for other algorithms.
    '''
    # Define class as abstract class
    __metaclass__ = abc.ABCMeta

    # Define common interface for algorithm classes
    def __new__(cls, *args, **kwargs):
        obj = super(BaseAlgorithm, cls).__new__(cls)
        return obj

    @abc.abstractmethod
    def solve(self, deriv_func, quad_func, bc_func, solinit):
        '''
        Method to solve the bvp with given arguments

        :param deriv_func: The ODE function.
        :param quad_func: The quad func.
        :param bc_func: The boundary conditions function.
        :param solinit: An initial guess for a solution to the BVP.
        :return: A solution to the BVP.
        '''
        raise NotImplementedError()

    def close(self):
        pass

    def preprocess(self, problem_data, use_numba=False):
        '''
        Code generation and compilation before running solver.

        :param problem_data:
        :param use_numba:
        :return: Code module.
        '''
        out_ws = dict()
        code_module = create_module(problem_data)
        code_module, compute_control_fn = make_functions(problem_data, code_module)
        out_ws['code_module'] = code_module
        deriv_func_code = load_eqn_template(problem_data, template_file='deriv_func.py.mu')
        bc_func_code = load_eqn_template(problem_data, template_file='bc_func.py.mu')
        deriv_func_fn = compile_code_py(deriv_func_code, code_module, 'deriv_func')
        bc_func_fn = compile_code_py(bc_func_code, code_module, 'bc_func')
        out_ws['deriv_func_code'] = deriv_func_code
        out_ws['bc_func_code'] = bc_func_code
        logging.debug(out_ws['bc_func_code'])
        logging.debug(out_ws['deriv_func_code'])

        if use_numba:
            deriv_func = numba.njit(parallel=False, nopython=True)(code_module.deriv_func_nojit)
        else:
            deriv_func = code_module.deriv_func_nojit

        deriv_func_fn = deriv_func
        code_module.deriv_func = deriv_func
        out_ws['code_module'].deriv_func = deriv_func

        bvp = BVP(deriv_func_fn, bc_func_fn, compute_control_fn)

        sys.modules['_beluga_' + problem_data['problem_name']] = out_ws['code_module']
        return out_ws['code_module'], bvp

    @staticmethod
    def load_code():
        logging.info('Loading compiled code ...')
        with open('codecache.pkl', 'rb') as f:
            bvp_data = pickle.load(f)

        return bvp_data

    def save_code(self):
        logging.info('Saving compiled code ...')
        bvp_data = {'deriv_fn': self.out_ws['code_module'].deriv_func}
        with open('codecache.pkl', 'wb') as f:
            pickle.dump(bvp_data, f, pickle.HIGHEST_PROTOCOL)

BVP = cl.namedtuple('BVP', 'deriv_func bc_func compute_control')
