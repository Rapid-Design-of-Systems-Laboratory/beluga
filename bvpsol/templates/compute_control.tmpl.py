# Example input    
# ctrl = {'control_options':[
#     [{'name':'theta','expr':'atan(y/x)'},
#      {'name':'sigma','expr':'acos(a/b)'}],
#
#     [{'name':'theta','expr':'-atan(y/x)'},{'name':'sigma','expr':'-acos(a/b)'}],
#     ],
#     'control_list':['theta','sigma']
# }


import numpy as np
from math import *
def compute_hamiltonian(_t,_X,_p,_aux,_u):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
        
    [{{#control_list}}{{.}},{{/control_list}}] = _u
    return {{ham_expr}}

def compute_control(_t,_X,_p,_aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    
    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    
    _saved = []
    _ham_saved = float('inf')
# Evaluate all control options

{{#control_options}}
    try:
        {{#.}}
        {{name}} = {{expr}}
        {{/.}}
    except:
        {{#.}}
        {{name}} = 0
        {{/.}}
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[{{#control_list}}{{.}},{{/control_list}}])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [{{#control_list}}{{.}},{{/control_list}}]
        
################################################################
{{/control_options}}

    return _saved