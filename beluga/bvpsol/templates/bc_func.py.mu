# TODO: Preprocess, postprocess hooks?
import numpy as np
from math import *
def bc_func(_ya,_yb,_p,_aux):
    # Constants and constraints
    # constant_name = constant_value
    # etc.

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    # Generalize to multipoint later
    # Left BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _ya[:{{num_states}}]
    [{{#control_list}}{{.}},{{/control_list}}] = compute_control(0,_ya,_p,_aux)
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Declare all predefined expressions
    {{#quantity_list}}
    {{name}} = {{expr}}
    {{/quantity_list}}

    _x0 = _aux['initial']
    _xf = _aux['terminal']

    _H = compute_hamiltonian(0,_ya,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_left = np.array([{{#left_bc_list}}{{.}},
                    {{/left_bc_list}} ])

    # Right BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _yb[:{{num_states}}]
    [{{#control_list}}{{.}},{{/control_list}}] = compute_control(1,_yb,_p,_aux)
    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}
    _H = compute_hamiltonian(1,_yb,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_right = np.array([{{#right_bc_list}}{{.}},
                {{/right_bc_list}}])

    return np.r_[res_left,res_right] # Concatenate
