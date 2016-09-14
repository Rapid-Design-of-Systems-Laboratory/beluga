import numpy as np
from math import *
from beluga.utils.math import *
# from beluga.utils.tictoc import *

def im(exprss):
    return np.imag(exprss)

I=1j

def deriv_func(_t,_X,_p,_aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    [{{#control_list}}{{.}},{{/control_list}}] = compute_control(_t,_X,_p,_aux)
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

    return np.array([{{#deriv_list}}{{.}},
        {{/deriv_list}}])
