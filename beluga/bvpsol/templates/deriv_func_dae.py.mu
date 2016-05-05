import numpy as np
from math import *
def deriv_func(_t,_X,_p,_aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:({{num_states}}+{{dae_var_num}})]

    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    # print(eps_alfaLim)

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    return np.array([{{#deriv_list}}{{.}},
        {{/deriv_list}}]+
        [{{#dae_eom_list}}{{.}},
        {{/dae_eom_list}}]
    )
