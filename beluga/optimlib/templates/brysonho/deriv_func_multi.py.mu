import numpy as np
from math import *

def compute_hamiltonian(t, X, p, aux, u):
    # C = [v for k,v in aux['const'].items()]
    return ham_fn(*X[:-1], *p[:{{num_params}}], *aux['const'].values(), *u)

def compute_control(_t, _X, _p, _aux, arc_type=0):
    return control_fns[arc_type](_t,_X[:{{num_states}}-1],_p[:{{num_params}}],_aux)

def deriv_func(_t, _X, _p, _aux, _arc_seq=(0,), _pi_seq=(None,), arc_idx=0):
    arc_type = _arc_seq[arc_idx]

    {{#state_list}}{{.}},{{/state_list}} = _X[:{{num_states}}]
    tf = abs(tf)
    _X[{{num_states}}-1] = tf

    u_ = compute_control(_t,_X,_p,_aux,arc_type)
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
        # pi_idx = _pi_seq[arc_idx]
        # if pi_idx is not None:
        #    [{{#pi_list}}{{.}},{{/pi_list}}] = _p[pi_idx]
        lam_eom = [{{#eom}}{{.}},
                   {{/eom}}]
{{/costate_eoms}}

    return np.hstack((state_eom, lam_eom, [0]))
