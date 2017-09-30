# TODO: Preprocess, postprocess hooks?
import numpy as np
from math import *
def bc_func_left(_ya, _p, _aux, _arcs):
    arc_type = _arcs[0]
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
    u_ = compute_control(0,_ya,_p,_aux)
    [{{#control_list}}{{.}},{{/control_list}}] = u_


    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _x0 = _aux['initial']

    _H = compute_hamiltonian(0,_ya,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_left = np.array([{{#bc_initial}}{{.}},
                    {{/bc_initial}} ])
    return res_left

def bc_func_right(_yb, _p, _aux, _arcs):
    arc_type = _arcs[0]
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Right BCs
    [{{#state_list}}{{.}},{{/state_list}}] = _yb[:{{num_states}}]
    u_ = compute_control(1,_yb,_p,_aux)
    [{{#control_list}}{{.}},{{/control_list}}] = u_
    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _xf = _aux['terminal']

    _H = compute_hamiltonian(1,_yb,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    res_right = np.array([{{#bc_terminal}}{{.}},
                {{/bc_terminal}}])
    return res_right

def bc_func(_ya, _yb, _p, _aux, _arcs=(0,)):
    res_left = bc_func_left(_ya, _p, _aux, _arcs)
    res_right = bc_func_right(_yb, _p, _aux, _arcs)

    return np.r_[res_left,res_right] # Concatenate
