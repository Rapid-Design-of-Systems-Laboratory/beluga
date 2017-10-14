# TODO: Preprocess, postprocess hooks?
import numpy as np
from math import *
def bc_func_left(_ya, _aux):
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    _p = _ya[{{num_states}}+{{num_controls}}:{{num_states}}+{{num_controls}}+{{num_params}}]
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Generalize to multipoint later
    # Left BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _ya[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _ya[{{num_states}}:{{num_states}}+{{num_controls}}]

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _x0 = _aux['initial']

    # _H = compute_hamiltonian(0,_ya,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_left = np.array([{{#bc_initial}}{{.}},
                    {{/bc_initial}} ])
    return res_left

def bc_func_right(_yb, _aux):
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    _p = _yb[{{num_states}}+{{num_controls}}:{{num_states}}+{{num_controls}}+{{num_params}}]
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Right BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _yb[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _yb[{{num_states}}:{{num_states}}+{{num_controls}}]
    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _xf = _aux['terminal']

    _H = compute_hamiltonian(1,_yb,_p,_aux['const'].values(),[{{#control_list}}{{.}},{{/control_list}}])
    res_right = np.array([{{#bc_terminal}}{{.}},
                {{/bc_terminal}}])
    return res_right

def bc_func(_ya, _yb, _aux):
    res_left = bc_func_left(_ya, _aux)
    res_right = bc_func_right(_yb, _aux)

    return np.hstack((res_left, res_right))


left_bc_mask = np.array([0]*({{num_states}}-1)+[1]*({{num_params}}+{{num_controls}}+1))
