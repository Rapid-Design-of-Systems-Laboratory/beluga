import numpy as np
from math import *
import itertools as it

def bc_func_left(_ya, _p, _aux, _arc_seq, _pi_seq):
    arc_type = _arc_seq[0]
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p[:{{num_params}}]

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

def bc_func_right(_yb, _p, _aux, _arc_seq, _pi_seq):
    arc_type = _arc_seq[0]
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p[:{{num_params}}]

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

def bc_func_interior(_ya, _yb, _aux, _arc_seq, _pi_seq):
    full_res = []
    for arc_idx, arc_left_type, arc_right_type in zip(it.count(), _arc_seq[1:-2], _arc_seq[2:-1]):
        # Entry jn of a constraint
        if arc_left_type == 0 and arc_right_type > 0:
            y1m = _yb[:{{num_states}},arc_idx-1] # End of previous arc
            y1p = _ya[:{{num_states}},arc_idx] # Start of current arc
            u1m = control_fns[arc_left_type](0, _y1m, _p, _aux)
            u1p = control_fns[arc_right_type](0, _y1p, _p, _aux)

            [{{#state_list}}_{{.}}_1m,{{/state_list}}] = y1m
            [{{#state_list}}_{{.}}_1p,{{/state_list}}] = y1p
            [{{#control_list}}_{{.}}_m,{{/control_list}}] = u1m
            [{{#control_list}}_{{.}}_p,{{/control_list}}] = u1p

            {{#bc_list}}
            if arc_left_type == {{arctype}}:
                pi_idx = _pi_seq[arc_idx]
                if pi_idx is not None:
                    [{{#pi_list}}{{.}},{{/pi_list}}] = _p[pi_idx]
                res = np.array([{{#entry_bc}}{{.}},
                    {{/entry_bc}}])
            {{/bc_list}}
        elif arc_right_type == 0 and arc_left_type > 0: # Exit jn
            y2m = _yb[:{{num_states}},arc_idx-1] # End of previous arc
            y2p = _ya[:{{num_states}},arc_idx] # Start of current arc
            u2m = control_fns[arc_left_type](0, _y2m, _p, _aux)
            u2p = control_fns[arc_right_type](0, _y2p, _p, _aux)

            [{{#state_list}}_{{.}}_2m,{{/state_list}}] = y2m
            [{{#state_list}}_{{.}}_2p,{{/state_list}}] = y2p
            [{{#control_list}}_{{.}}_m,{{/control_list}}] = u2m
            [{{#control_list}}_{{.}}_p,{{/control_list}}] = u2p

            {{#bc_list}}
            if arc_right_type == {{arctype}}:
                pi_idx = _pi_seq[arc_idx]
                if pi_idx is not None:
                    [{{#pi_list}}{{.}},{{/pi_list}}] = _p[pi_idx]
                res = np.array([{{#exit_bc}}{{.}},
                    {{/exit_bc}}])
            {{/bc_list}}
        else:
            raise Exception('Not impl for unconstrained arc jns')

        full_res.extend(res)
    return np.hstack(full_res)


def bc_func(_ya, _yb, _p, _aux, _arc_seq=(0,), _pi_seq=(None,)):
    res_left = bc_func_left(_ya[:,0], _p, _aux, _arc_seq, _pi_seq)
    res_right = bc_func_right(_yb[:,-1], _p, _aux, _arc_seq, _pi_seq)
    return np.hstack((res_left,res_right)) # Concatenate
