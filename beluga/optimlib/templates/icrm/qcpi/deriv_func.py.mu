import numpy as np
from numpy import *
import numba
import scipy.linalg

def im(Z):
    return Z.imag


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

@numba.njit(parallel=False,cache=False)
def deriv_func_mcpi(_t,_X,dXdt_,_const):
    dXdt_[:] = deriv_func(_t, _X[:{{num_states}}+{{dae_var_num}}], _X[{{num_states}}+{{dae_var_num}}:{{num_states}}+{{dae_var_num}}+{{num_params}}], _const)
    #dXdt_[{{num_states}}+{{dae_var_num}}:] = 0

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

    return np.array([{{#deriv_list}}{{.}},
       {{/deriv_list}}]+
       [{{#dae_eom_list}}{{.}},
       {{/dae_eom_list}}]
    )


num_dae_vars = {{dae_var_num}}
deriv_func = numba.njit(parallel=False,cache=False)(deriv_func_nojit)

#{{#state_list}}{{.}},{{/state_list}}]
#{{#dae_var_list}}{{.}},{{/dae_var_list}}]
#{{num_states}} = num_odes
#{{dae_var_num}} = num_controls
