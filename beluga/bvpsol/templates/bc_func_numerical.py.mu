# TODO: Preprocess, postprocess hooks?
import numpy as np
# from math import *
from beluga.utils.math import *

def bc_func_left(_ya, _p, _aux):
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Generalize to multipoint later
    # Left BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _ya[:{{num_states}}]
    [{{#control_list}}{{.}},{{/control_list}}] = compute_control(0,_ya,_p,_aux)

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _x0 = _aux['initial']

    _H = compute_hamiltonian(0,_ya,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_left = np.array([{{#left_bc_list}}{{.}},
                    {{/left_bc_list}} ])
    return res_left

def bc_func_right(_yb, _p, _aux):
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Right BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _yb[:{{num_states}}]
    [{{#control_list}}{{.}},{{/control_list}}] = compute_control(1,_yb,_p,_aux)
    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _xf = _aux['terminal']

    _H = compute_hamiltonian(1,_yb,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_right = np.array([{{#right_bc_list}}{{.}},
                {{/right_bc_list}}])
    return res_right

def bc_func(_ya, _yb, _p, _aux):
    res_left = bc_func_left(_ya, _p, _aux)
    res_right = bc_func_right(_yb, _p, _aux)

    return np.r_[res_left,res_right] # Concatenate
