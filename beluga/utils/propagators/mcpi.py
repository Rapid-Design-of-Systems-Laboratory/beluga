import numpy as np
import numpy.matlib as matlib
from math import *
def mcpi(ode, tSpan, x0, *args, N = 10, tol = 1e-4):
    """
    Propagates a system of ODEs using the Modified Chebyshev-Picard Iteration method
    """

    x0 = np.array(x0)
    # Convert to 2D numpy array if 1D
    if len(x0.shape) == 1:
        x0 = np.array([x0])

    # Convert to row vector if col vector given
    if x0.shape[1] == 1:
        x0 = x0.T

    # If column vector is given, convert to matrix using repetition
    if x0.shape[0] != N+1:
        x_guess = matlib.repmat(x0[0,:],N+1,1);
    else:
        x_guess = x0;

    tau = np.cos(np.linspace(N,0,N+1)*pi/N)

    omega1 = (tSpan[-1]+tSpan[0])/2
    omega2 = (tSpan[-1]-tSpan[0])/2

    vec_1_Nt = matlab_colon(1,N).T # (1:N)'
    vec_0_Np1t = matlab_colon(0,N+1).T # (0:N+1)'
    vec_0_N  = matlab_colon(0,N)    # 0:N
    vec_1_Np1 = matlab_colon(1,N+1) # 1:N+1

    T = chebypoly(vec_0_Np1t,tau);
    V = np.ones_like(tau)/N
    V[1:-1] *= 2

    TV1 = T[0:N,:]*V
    TV2 = T[2:N+2,:]*V;
    TV = (TV1-TV2)/(2*vec_1_Nt)
    TV[-1,:] = TV1[-1,:]/(2*N)
    S = 2*((-1)**(vec_1_Nt.T+1))     # S = 2.*((-1).^((1:N)+1));

    Cx = T[0:N+1,0:N+1].T   # Cx = T(1:N+1,1:N+1)';
    Cx[:,0] /= 2

    # tau = tau[np.newaxis,:]   # Convert to row vector
    err1 = err2 = np.inf
    ctr = 0
    max_iter = 100

    vode = vectorize_ode(ode)
    # xdot = vode(tau,x_guess)

    s_tau = tau*omega2 + omega1  # Scaled tau
    x_new = np.empty_like(x_guess)

    while ((tol < err1 or tol < err2) and (ctr < max_iter)):
        ctr = ctr + 1

        F = vode(s_tau,x_guess,*args)*omega2
        Beta_r = np.dot(TV,F)
        Beta_k = np.r_[np.dot(S,Beta_r) + 2*x_guess[0,:],Beta_r]    # [2*x0+S*Beta_r; Beta_r]
        x_new = np.dot(Cx,Beta_k)
        err2 = err1;
        err1 = np.amax(abs(x_new - x_guess))
        x_guess = x_new

    return (s_tau,x_new)

def chebypoly(k, tau):
    # Computes T_k(x) for all points in tau for all k
    return np.cos(k*np.arccos(tau));

def vectorize_ode(ode):
    """
    Vectorizes the ode function to be evaluated over entire trajectory space
        Input is assumed to be matrix with one row per "timestep" with columns
        making up each state
    """
    def wrapper(t, x, *args,**vargs):
        """
        Wrapper that evaluates the ODE for entire trajectory space
        """
        out = np.empty_like(x)
        out[:] = np.NaN
        for index in range(len(t)):
            out[index,:] = ode(t[index],x[index,:],*args,**vargs)
        return out
    return wrapper

def matlab_colon(a,b):
    # Returns the same result as (a:b) in matlab
    #   Converts the result to a row-vector
    return np.linspace(a,b,b-a+1,dtype=int)[np.newaxis,:]

if __name__ == '__main__':
    def test_ode(t, X):
        y = X[0];
        ydot = X[1];
        return np.array([ydot,-y])

    mcpi(test_ode,[0, pi/2],[100,1.45], 10)
