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
import scipy.optimize
from math import *
from beluga.utils import static_var

def compute_hamiltonian(_t,_X,_p,_aux,_u):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}


    [{{#control_list}}{{.}},{{/control_list}}] = _u

    # Declare all quantities
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    return {{ham_expr}}

@static_var('guess_u',[{{#control_list}}0,{{/control_list}}])
def compute_control(_t,_X,_p,_aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]

    # Declare all auxiliary variables
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}

    [{{#parameter_list}}{{.}},{{/parameter_list}}] = _p

    # Define controls beforehand in case some quantity uses it
    __nancontrols = np.empty({{num_controls}})
    __nancontrols[:] = np.nan
    [{{#control_list}}{{.}},{{/control_list}}] = __nancontrols

    # Declare all quantities
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    _saved = np.empty({{num_controls}})
    _saved[:] = np.nan
    
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

    # guess_u = [{{#control_list}}0,{{/control_list}}]

    _saved = scipy.optimize.fsolve(dHdu, compute_control.guess_u)
{{/control_options}}
    compute_control.guess_u = _saved
    return _saved
