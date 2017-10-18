import numpy as np
from numpy import *
import numba
import scipy.linalg

def im(Z):
    return Z.imag

# Complex step jacobian
def compute_jacobian(f, X, indices=None, StepSize=1e-100, args=()):
    I = np.eye({{num_states}}+{{dae_var_num}})*1j*StepSize
    if indices is None:
        indices = range({{num_states}}+{{dae_var_num}})

    return np.array([f(X[:({{num_states}}+{{dae_var_num}})]+ih, *args).imag/StepSize
                for index, ih in enumerate(I)
                if index in indices],order='F').T

@numba.njit
def compute_jacobian_fd(X, _const, step_size=1e-6):
    jac = np.zeros(({{dae_var_num}}, {{num_states}}+{{dae_var_num}}))
    fx = compute_g(X, _const)
    steps = np.eye({{num_states}}+{{dae_var_num}})*step_size + X[:{{num_states}}+{{dae_var_num}}]
    for i in numba.prange({{num_states}}+{{dae_var_num}}):
        fxh = compute_g(steps[i], _const)
        jac[:,i] = (fxh - fx)/step_size

    return jac

@numba.njit
def compute_g(_X, _const):
    I = 1j
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:({{num_states}})]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:({{num_states}}+{{dae_var_num}})]

    # Declare all auxiliary variables
    {{#aux_list}}{{#vars}}{{.}},{{/vars}}{{/aux_list}} = _const

    # Declare all quantities
    {{#quantity_list}}
    {{name}} = {{expr}}
    {{/quantity_list}}

    return np.array([{{#dHdu}}{{.}},
            {{/dHdu}}])

def compute_hamiltonian(_t,_X,_p,_const,_u):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:{{num_states}}+{{dae_var_num}}]
    # Declare all auxiliary variables
    {{#aux_list}}{{#vars}}{{.}},{{/vars}}{{/aux_list}} = _const
    # Declare all quantities
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    return {{ham_expr}}

def compute_control(_t,_X,_p,_const):
  return _X[{{num_states}}:({{num_states}}+{{dae_var_num}})]

# Used to solve initial guess
def get_dhdu_func(_t,_X,_p,_aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:({{num_states}})]

    # Declare all auxiliary variables
    {{#aux_list}}
    {{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
    {{/vars}}
    {{/aux_list}}

    def dHdu(_u):
      [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _u
      # Declare all quantities
      {{#quantity_list}}
      {{name}} = {{expr}}
      {{/quantity_list}}

      return np.array([{{#dHdu}}{{.}},
                {{/dHdu}}])

    return dHdu


def deriv_func_ode45(_t,_X,_p,_aux):
    return deriv_func_nojit(_t,_X,_p,list(_aux['const'].values()))

@numba.njit(parallel=True)
def deriv_func_mcpi(_t,_X,dXdt_,_const):
    dXdt_[:{{num_states}}+{{dae_var_num}}] = deriv_func(_t, _X[:{{num_states}}+{{dae_var_num}}], _X[{{num_states}}+{{dae_var_num}}:{{num_states}}+{{dae_var_num}}+{{num_params}}], _const)
    dXdt_[{{num_states}}+{{dae_var_num}}:] = 0

def deriv_func_nojit(_t,_X,_p,_const):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:({{num_states}}+{{dae_var_num}})]
    tf = abs(tf)
    _X[{{num_states}}-1] = tf

    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Declare all auxiliary variables
    {{#aux_list}}{{#vars}}{{.}},{{/vars}}{{/aux_list}} = _const

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    #Xdot = np.array([{{#deriv_list}}{{.}},
    #                 {{/deriv_list}}])
    #dg     = compute_jacobian_fd(_X, _const)
    #dgdX   = dg[:,:{{num_states}}]
    #dgdU   = dg[:,{{num_states}}:({{num_states}}+{{dae_var_num}})]
    #udot   = np.linalg.solve(dgdU, np.dot(-dgdX, Xdot[:{{num_states}}]))
    #udot2 = np.array([{{#dae_eom_list}}{{.}},{{/dae_eom_list}}])
    #print(udot, udot2)
    #from beluga.utils import keyboard
    #keyboard()
    #return np.hstack((Xdot, udot))
    return np.array([{{#deriv_list}}{{.}},
        {{/deriv_list}}
        {{#dae_eom_list}}{{.}},
        {{/dae_eom_list}}]
    )


num_dae_vars = {{dae_var_num}}
deriv_func = numba.njit(parallel=True)(deriv_func_nojit)
