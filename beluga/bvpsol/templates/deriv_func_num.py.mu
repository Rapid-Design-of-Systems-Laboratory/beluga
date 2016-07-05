import numpy as np
import scipy.linalg
from math import *
from beluga.utils import keyboard
from beluga.utils.math import *

# Complex step jacobian
def compute_jacobian(f, X, indices=None, StepSize=1e-100, *args):
    I = np.eye({{num_states}})*1j*StepSize
    if indices is None:
        indices = range({{num_states}})

    return np.array([f(X[:({{num_states}})]+ih, *args).imag/StepSize
                for index, ih in enumerate(I)
                if index in indices], order='F').T

def compute_jacobian_fd(f, X, indices=None, StepSize=1e-6, *args):
    I = np.eye({{num_states}})*StepSize
    if indices is None:
        indices = range({{num_states}})

    fx = f(X[:({{num_states}})], *args)
    return np.array([ (f(X[:({{num_states}})]+h, *args) - fx)/StepSize
                for index, h in enumerate(I)
                if index in indices],order='F').T

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

    # create function wrapper for taking numerical derivatives
    u = compute_control(_t,_X,_p,_aux)
    ham_fn = lambda x: compute_hamiltonian(_t, x, _p, _aux, u)

    lamdot = -compute_jacobian(ham_fn, _X, range(int({{num_states}}/2)))

    Xdot = np.array([{{#state_rate_list}}{{.}},
        {{/state_rate_list}}])
    Xdot = np.append(Xdot, tf*lamdot)
    Xdot = np.append(Xdot, 0)

    return tf*(Xdot)


