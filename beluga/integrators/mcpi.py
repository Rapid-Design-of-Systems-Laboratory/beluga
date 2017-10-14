import numpy as np
from numba import vectorize
from functools import lru_cache
from math import *

@vectorize(['float64(float64, float64)'], nopython=True, target='cpu')
def absdiff(a, b):
    return abs(a-b)

@lru_cache(maxsize=None)
def mcpi_init(N):
    """
    Given Chebyshev series of order N
    Returns tau, C_x and C_a matrices used in MCPI
    """
    tau = np.fromiter((cheby_node(i, N) for i in range(N+1)), np.float64)
    T = np.array([[cheby_poly(tau_j, k) for k in range(N+1)] for tau_j in tau])   # Matrix used for computation
    W = np.diag(np.ones(N+1))
    W[0,0] /= 2
    C_x = T @ W  # x = C_x * alpha for coefficients alpha

    V = np.diag((2/N)*np.ones(N+1))
    V[0,0] /= 2
    V[N, N] /= 2

    R = np.diag([1] + [1/(2*r) for r in range(1, N+1)])
    S = np.diag(np.ones(N), k=-1) + np.diag(-np.ones(N), k=1)
    S[0,2:N] = np.fromiter(((-1)**(r+1)*(1/(r-1) - 1/(r+1)) for r in range(2, N)), np.float64)  ## r = 2, 3, ..., N-1
    S[0, :2] = [1, -1/2]
    S[0, -1] = (-1)**(N+1)/(N-1)

    C_a = R @ S @ T @ V # For each variable, Beta = x_0 + C_a * g()

    return (tau, C_x, C_a)

@lru_cache(maxsize=None)
def cheby_node(j, N):
    """
    Evaluates CGL-node tau_j for chebyshev series of order 'N'
    """
    return cos(j*pi/N)


@lru_cache(maxsize=None)
def cheby_poly(tau_j, k):
    """
    Evaluates chebyshev polynomial of order 'k' at point tau_j
    """
    return cos(k*acos(tau_j))

def cheby_eval(beta, tspan):
    """
    Evaluates chebyshev series given by coefficients 'beta' over the given mesh 'tspan'
    """
    N = len(beta)-1
    tau_fine = np.linspace(-1, 1, len(tspan))
    T = np.array([[cheby_poly(tau_j, k) for tau_j in tau_fine] for k in range(N+1)])
    W = np.diag(np.ones(N+1))
    W[0,0] /= 2
    x_new = (W @ T).T @ beta
    return x_new

def mcpi(ode_fn, tspan, x_0, N=51, maxiter=501, xtol=1e-4, args=()):
    """
    Propagates equations in EOM with initial conditions in x_0
    Returns:
        tt: Mesh points for the solution
        x_new: Solution (each column = time history of one state)
    """
    #TODO: Use numexpr and strings to speed up EOMs
    x_0 = np.array(x_0, dtype=np.float64)
    w1 = (tspan[-1]-tspan[0])/2
    w2 = (tspan[-1]+tspan[0])/2

    tau, C_x, C_a = mcpi_init(N)      # tau is in reverse order (1 to -1)
    C_a = w1 * C_a
    t_arr = tau * w1 + w2

    x_guess = np.tile(x_0, [N+1, 1])  # Each column -> time history of one state
    x0_twice = 2*x_guess[0]
    g = np.empty_like(x_guess)

    for ctr in range(maxiter):
        # Evaluate vectorized EOM over full time domain
        ode_fn(t_arr, x_guess, g, *args)

        beta = C_a @ g
        beta[0]+= x0_twice          # Compute Chebyshev coefficients of solution
        x_new = C_x @ beta          # Compute solution

        err1 = np.max(absdiff(x_new, x_guess))
        if (err1 < xtol):
#             print('Converged in %d iterations.' % ctr)
            break
        x_guess = x_new

    if len(tspan) > 2:
        # If tspan is bigger than 2 elements, evaluate solution on that mesh
        return tspan, cheby_eval(beta, tspan)
    else:
        # Else return solution on CGL mesh
        return t_arr, np.array(list(reversed(x_new)))
