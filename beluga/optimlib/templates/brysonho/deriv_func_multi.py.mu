import numpy as np
from math import *

def compute_hamiltonian(t, X, p, aux, u):
    # C = [v for k,v in aux['const'].items()]
    return ham_fn(*X[:-1], *p[:{{num_params}}], *aux['const'].values(), *u)

def compute_control(_t, _X, _p, _aux, _arc_seq, _pi_seq, arc_idx=None):
    if arc_idx is None:
        arc_idx = min(floor(_t), len(_arc_seq)-1)
    arc_type = _arc_seq[arc_idx]
    try:
        return control_fns[arc_type](_t,_X[:{{num_states}}-1],_p[:{{num_params}}],_aux)
    except:
        from beluga.utils import keyboard
        keyboard()

def deriv_func(_t, _X, _p, _aux, _arc_seq, _pi_seq, arc_idx=None):
    if arc_idx is None:
        arc_idx = min(floor(_t), len(_arc_seq)-1)
    arc_type = _arc_seq[arc_idx]

    {{#state_list}}{{.}},{{/state_list}} = _X[:{{num_states}}]
    tf = abs(tf)
    _X[{{num_states}}-1] = tf

    u_ = compute_control(_t,_X,_p,_aux,_arc_seq,_pi_seq, arc_idx)

    {{#control_list}}{{.}},{{/control_list}} = u_
    {{#parameter_list}}{{.}},{{/parameter_list}} = _p[:{{num_params}}]

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    state_eom = [{{#x_deriv_list}}{{.}},
                 {{/x_deriv_list}}]
{{#costate_eoms}}
    if arc_type == {{arctype}}:
        lam_eom = [{{#eom}}{{.}},
                   {{/eom}}]
{{/costate_eoms}}

    return np.hstack((state_eom, lam_eom, [0]))
