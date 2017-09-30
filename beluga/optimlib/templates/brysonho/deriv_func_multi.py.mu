import numpy as np
from math import *

def compute_control(_t, _X, _p, _aux, arc_type=0):
    return control_fns[arc_type](_t,_X,_p,_aux)

def deriv_func(_t, _X, _p, _aux, _arcs=(0,), arc_idx=0):
    arc_type = _arcs[arc_idx]

    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    u_ = compute_control(_t,_X,_p,_aux)
    [{{#control_list}}{{.}},{{/control_list}}] = u_
    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

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
    constants = [val for key,val in _aux['const'].items()]
{{#costate_eoms}}
    if arc_type == {{arcid}}:
        lam_eom = [{{#eom}}{{.}},
                   {{/eom}}]
{{/costate_eoms}}

    return np.hstack((state_eom, lam_eom, [0]))
