import numpy as np
from math import *

import scipy.linalg
import numba

def im(Z):
    return Z.imag

def compute_hamiltonian(_t,_X,_p,_aux,_u):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:]
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    # Declare all quantities
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    return {{ham_expr}}

def compute_control(_t,_X,_p,_aux):
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

def deriv_func_nojit(_t, _X, _p, _aux, arc_idx=None):
    _arc_seq = _aux.get('arc_seq', (0,))
    _pi_seq = _aux.get('pi_seq',(None,))
    if arc_idx is None:
        arc_idx = min(floor(_t), len(_arc_seq)-1)
    arc_type = _arc_seq[arc_idx]

    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:({{num_states}}+{{dae_var_num}})]

    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p[:{{num_params}}]

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    # {{#aux_list}}{{#vars}}{{.}},{{/vars}}{{/aux_list}} = _const

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    return np.array([{{#deriv_list}}{{.}},
       {{/deriv_list}}]+
       [{{#dae_eom_list}}{{.}},
       {{/dae_eom_list}}]
    )

# def deriv_func_ode45(_t,_X,_p,_aux):
#     try:
#         return deriv_func(_t,_X,_p,list(_aux['const'].values()),0)
#     except Exception as e:
#         from beluga.utils import keyboard
#         keyboard()

deriv_func_ode45 = deriv_func_nojit

#{{#state_list}}{{.}},{{/state_list}}]
#{{#dae_var_list}}{{.}},{{/dae_var_list}}]
num_bc = {{num_bc}}
