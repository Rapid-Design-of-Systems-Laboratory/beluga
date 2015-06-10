# Example input
# ctrl = {'control_options':[
#     [{'name':'theta','expr':'atan(y/x)'},
#      {'name':'sigma','expr':'acos(a/b)'}],
#
#     [{'name':'theta','expr':'-atan(y/x)'},{'name':'sigma','expr':'-acos(a/b)'}],
#     ],
#     'control_list':['theta','sigma']
# }


#
# def CLfunction(alfa):
#     return 1.5658*alfa
#
# def CDfunction(alfa):
#     return 1.6537*alfa**2 + 0.0612

import numpy as np
import scipy.optimize
from math import *
# from joblib import Memory
# memory = Memory(cachedir='~/dev/mjgrant-beluga/examples/_cache', mmap_mode='r', verbose=0)

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

    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

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
{{^control_options}}
    def dHdu(_u):
        [{{#control_list}}{{.}},{{/control_list}}] = _u
        im = np.imag
        I = 1j
        return [{{#dHdu}}{{.}},
                {{/dHdu}}]
    guess_u = [{{#control_list}}0,{{/control_list}}]

    from beluga.utils import keyboard
    _saved = scipy.optimize.fsolve(dHdu, guess_u)
{{/control_options}}
    return _saved
