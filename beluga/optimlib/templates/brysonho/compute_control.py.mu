import numpy as np
import scipy
import scipy.optimize
from math import *
from beluga.utils import static_var, keyboard
import logging

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

@static_var('guess_u',[{{#control_list}}0.1,{{/control_list}}])
@static_var('ctr',0)
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
    except Exception as e:
        {{#.}}
        {{name}} = 0
        {{/.}}
        logging.error('Error : '+str(e))
        raise
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

    _saved = scipy.optimize.fsolve(dHdu, compute_control.guess_u,xtol=1e-5)
{{/control_options}}
    compute_control.guess_u = _saved
    return _saved
