# TODO: Preprocess, postprocess hooks?
# stuff = {'aux_list': [
#             {
#             'type' : 'const',
#             'vars': ['g','foo']
#             },
#             {
#             'type' : 'constraint',
#             'vars': ['qdot']
#             }
#          ],
#          'state_list': [
#              'a','b','c','d'
#          ],
#          'num_states': 4,
#         }
import numpy as np
from math import *
def deriv_func(_t,_X,_p,_aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    [{{#control_list}}{{.}},{{/control_list}}] = compute_control(_t,_X,_p,_aux)    
    return np.array([{{#deriv_list}}{{.}},
        {{/deriv_list}}])