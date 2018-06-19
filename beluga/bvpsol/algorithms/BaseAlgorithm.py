import abc
import logging
import collections as cl
import functools as ft
import simplepipe as sp
import numba
import sys
import pickle
from beluga.codegen import *
from beluga.utils import keyboard


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
    def solve(self, deriv_func, bc_func, solinit):
        '''
        Method to solve the bvp with given arguments

        :param deriv_func: The ODE function.
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

        out_ws = PythonCodeGen({'problem_data': problem_data})
        logging.debug(out_ws['bc_func_code'])
        logging.debug(out_ws['deriv_func_code'])

        if use_numba:
            deriv_func = numba.njit(parallel=False, nopython=True)(out_ws['code_module'].deriv_func_nojit)
        else:
            deriv_func = out_ws['code_module'].deriv_func_nojit

        out_ws['deriv_func_fn'] = deriv_func
        out_ws['code_module'].deriv_func = deriv_func

        out_ws = out_ws

        bvp = BVP(out_ws['deriv_func_fn'], out_ws['bc_func_fn'], out_ws['compute_control_fn'])

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

PythonCodeGen = sp.Workflow([
    # Create module for holding compiled code
    sp.Task(ft.partial(create_module), inputs='problem_data', outputs=('code_module')),

    sp.Task(make_functions, inputs=('problem_data', 'code_module'), outputs=('code_module','compute_control_fn')),
    # Load equation template files and generate code
    sp.Task(ft.partial(load_eqn_template,
            template_file='deriv_func.py.mu'),
            inputs='problem_data',
            outputs='deriv_func_code'),
    sp.Task(ft.partial(load_eqn_template,
            template_file='bc_func.py.mu'),
            inputs='problem_data',
            outputs='bc_func_code'),

    # Compile generated code
    sp.Task(ft.partial(compile_code_py, function_name='deriv_func'),
            inputs=['deriv_func_code', 'code_module'],
            outputs='deriv_func_fn'),
    sp.Task(ft.partial(compile_code_py, function_name='bc_func'),
            inputs=['bc_func_code', 'code_module'],
            outputs='bc_func_fn'),
], description='Generates and compiles the required BVP functions from problem data')
