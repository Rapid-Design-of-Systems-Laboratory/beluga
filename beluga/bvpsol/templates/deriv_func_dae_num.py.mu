import numpy as np
import scipy.linalg
from math import *
from beluga.utils import keyboard
from beluga.utils.math import *

def im(exprss):
    return np.imag(exprss)

I=1j

# Complex step jacobian
def compute_jacobian(f, X, indices=None, StepSize=1e-100, *args):
    I = np.eye({{num_states}}+{{dae_var_num}})*1j*StepSize
    if indices is None:
        indices = range({{num_states}}+{{dae_var_num}})

    return np.array([f(X[:({{num_states}}+{{dae_var_num}})]+ih, *args).imag/StepSize
                for index, ih in enumerate(I)
                if index in indices],order='F').T

def compute_jacobian_fd(f, X, indices=None, StepSize=1e-6, *args):
    I = np.eye({{num_states}}+{{dae_var_num}})*StepSize
    if indices is None:
        indices = range({{num_states}}+{{dae_var_num}})

    fx = f(X[:({{num_states}}+{{dae_var_num}})], *args)
    return np.array([ (f(X[:({{num_states}}+{{dae_var_num}})]+h, *args) - fx)/StepSize
                for index, h in enumerate(I)
                if index in indices],order='F').T

def compute_g(_t, _X, _p, _aux):
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:({{num_states}})]
    [{{#dae_var_list}}{{.}},{{/dae_var_list}}] = _X[{{num_states}}:({{num_states}}+{{dae_var_num}})]

    # Declare all auxiliary variables
    {{#aux_list}}
    {{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
    {{/vars}}
    {{/aux_list}}

    # Declare all quantities
    {{#quantity_list}}
    {{name}} = {{expr}}
    {{/quantity_list}}

    return np.array([{{#dHdu}}{{.}},
            {{/dHdu}}])

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

    # Declare all predefined expressions
{{#quantity_list}}
    {{name}} = {{expr}}
{{/quantity_list}}

    Xdot = np.array([{{#deriv_list}}{{.}},
        {{/deriv_list}}])

    # create function wrapper for taking numerical derivatives
    ham_fn = lambda x: compute_hamiltonian(_t, x, _p, _aux)
    g_fn   = lambda x: compute_g(_t, x, _p, _aux)

    lamdot = -compute_jacobian(ham_fn, _X, range(int({{num_states}}/2)))
    Xdot[int({{num_states}}/2):({{num_states}}-1)] = tf*lamdot

    dg     = compute_jacobian(g_fn, _X)
    #keyboard()
    dgdX   = dg[:,:{{num_states}}]
    dgdU   = dg[:,{{num_states}}:({{num_states}}+{{dae_var_num}})]
    # dgdU   = compute_jacobian(g_fn, _X, range({{num_states}},{{num_states}}+{{dae_var_num}}))

    # dgdU * udot + dgdX * xdot = 0
    # udot   = scipy.linalg.solve(dgdU, np.dot(-dgdX, Xdot[:{{num_states}}]))
    udot   = numpy.linalg.lstsq(dgdU, np.dot(-dgdX, Xdot[:{{num_states}}]))

#    udot = np.array([{{#dae_eom_list}}{{.}},
#    {{/dae_eom_list}}])
    return tf*np.append(Xdot,
        udot
    )