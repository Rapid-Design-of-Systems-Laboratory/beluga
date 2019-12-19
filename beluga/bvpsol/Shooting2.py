import cloudpickle as pickle
import copy
import logging
import numpy as np
from math import isclose


from beluga.bvpsol.BaseAlgorithm import BaseAlgorithm, BVPResult
from beluga.ivpsol import Propagator, Trajectory, reconstruct
from scipy.sparse import coo_matrix, csc_matrix
from scipy.sparse.linalg import splu
from scipy.optimize.slsqp import approx_jacobian
from scipy.optimize import minimize, root, fsolve
scipy_minimize_algorithms = {'Nelder-Mead', 'Powell', 'CG', 'BFGS', 'Newton-CG', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP',
                             'trust-constr', 'dogleg', 'trust-ncg', 'trust-exact', 'trust-krylov'}
scipy_root_algorithms = {'hybr', 'lm', 'broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden',
                         'excitingmixing', 'krylov', 'df-sane'}

# filename = 'space_shuttle.beluga'
#
# with open(filename, 'rb') as file:
#     save_dict = pickle.load(file)
#
# bvp_test = save_dict['bvp']
# sols = save_dict['solutions']
#
# sol_int = sols[-1][0]
# sol_tar = sols[-1][1]
#
# with open('test_set.beluga', 'wb') as file:
#     pickle.dump((bvp_test, (sol_int, sol_tar)), file)

with open('test_set.beluga', 'rb') as file:
    load_test = pickle.load(file)

bvp_test = load_test[0]
sols = load_test[1]


class Shooting2:
    def __init__(self, bvp):

        self.bvp = bvp

        self.tol = 1e-4
        self.n_y = len(bvp.sym_bvp.x)
        self.n_q = len(bvp.sym_bvp.q)
        self.n_p_d = len(bvp.sym_bvp.p_d)
        self.n_p_n = len(bvp.sym_bvp.p_n)
        self.k = len(bvp.sym_bvp.k)

        self.num_deriv_type = 'csd'

        self.f_func = bvp.deriv_func
        self.g_func = bvp.quad_func
        self.bc_func = bvp.bc_func

        if bvp.deriv_jac_func:
            self.df_dx = bvp.deriv_jac_func
        else:
            self.derivative_function_jac = self.make_num_df_dx
        self.boundarycondition_function_jac = bvp.bc_func_jac

        self.bc_func_ms = None
        self.stm_ode_func = None

    def make_num_jacobians(self):
        if self.num_deriv_type == 'csd':
            h = 1e-100
            h_y_mat = h * np.eye(self.n_y, self.n_y)
            h_p_mat = h * np.eye(self.n_p_d, self.n_p_d)


shooter = Shooting2(bvp_test)
