# from autodiff import Function, Gradient
import numpy as np

from beluga.bvpsol import Solution, BVP, Algorithm
from beluga.utils.propagators import ode45, mcpi
from beluga.utils import keyboard

from math import *

from beluga.utils.joblib import Memory

class GACPI(Algorithm):
    """
    Class that implements the Generalized Adaptive Chebyshev-Picard Iteration
       method in Python
    """
    def solve(self,bvp):
        """Solves the given BVP"""
        tol = 1e-4
        N = 40;
        ode = bvp.deriv_func
        bc  = bvp.bc_func
        tSpan = bvp.solution.x
        x_guess = bvp.solution.y.T   # Following bvp4c convention for input/output

        params = bvp.solution.parameters
        aux  =  bvp.solution.aux
        [tau_1,x_guess,Beta_k] = mcpi(ode,tSpan,x_guess,params,aux,N = N,tol = tol,return_Beta = True)

        [Beta_lim,_] = np.where(Beta_k > tol/10); # We are only interested in row index
        Beta_idx = Beta_lim[-1]                   # Get last row index
        N = Beta_idx + 3;                         # Use polynomials three orders higher
        tSpan = np.linspace(tSpan[0],tSpan[-1],x_guess.shape[0])    # Resize tSpan
        [tau,x_guess] = mcpi(ode,tSpan,x_guess,params,aux,N = N,tol = tol)

        #
        # tau = np.cos(np.linspace(N,0,N+1)*pi/N)
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

        k = matlab_colon(1,N)
        K1_S = -1**k
        K2_S = np.ones_like(k)
        K1_S[0,0] = K2_S[0,0] = 0 # Ignore Beta1 in the sum

        err1 = err2 = np.inf
        ctr = 0
        max_iter = 100

        vode = wrap_params(vectorize_ode(ode))
        s_tau = tau*omega2 + omega1  # Scaled tau
        x_new = np.empty_like(x_guess)

        while ((tol < err1 or tol < err2) and (ctr < max_iter)):
            ctr = ctr + 1

            F = vode(s_tau,x_guess,p,aux)*omega2
            Beta_r = np.dot(TV,F)
            Beta_k = np.r_[np.dot(S,Beta_r) + 2*x_guess[0,:],Beta_r]    # [2*x0+S*Beta_r; Beta_r]
            x_new = np.dot(Cx,Beta_k)
            err2 = err1;
            err1 = np.amax(abs(x_new - x_guess))
            x_guess = x_new

    def __bcjac_fd(self, bc_func, ya, yb, phi, parameters, aux, StepSize=1e-7):

        ya = np.array(ya, ndmin=1)
        yb = np.array(yb, ndmin=1)

        # if parameters is not None:
        p  = np.array(parameters)
        h = StepSize

        nOdes = ya.shape[0]
        nBCs = nOdes
        if parameters is not None:
            nBCs += parameters.size

        fx = bc_func(ya,yb,p,aux)

        M = np.zeros((nBCs, nOdes))
        N = np.zeros((nBCs, nOdes))
        for i in range(nOdes):
            ya[i] = ya[i] + h
            # if parameters is not None:
            f = bc_func(ya,yb,p,aux)
            # else:
            #     f = bc_func(ya,yb)

            M[:,i] = (f-fx)/h
            ya[i] = ya[i] - h
        # for i in range(nOdes):
            yb[i] = yb[i] + h
            # if parameters is not None:
            f = bc_func(ya,yb,p,aux)
            # else:
            #     f = bc_func(ya,yb)
            N[:,i] = (f-fx)/h
            yb[i] = yb[i] - h

        if parameters is not None:
            P = np.zeros((nBCs, p.size))
            for i in range(p.size):
                p[i] = p[i] + h
                f = bc_func(ya,yb,p,aux)
                P[:,i] = (f-fx)/h
                p[i] = p[i] - h
            J = np.hstack((M+np.dot(N,phi),P))
        else:
            J = M+np.dot(N,phi)
        return J
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

def wrap_params(ode):
    def param_wrapper(t, x, p, aux):
        dxdt = ode(t,x,p,aux)
        return np.r_[dxdt, np.zeros((dxdt.shape[0],len(p)))]
    return param_wrapper

def matlab_colon(a,b):
    # Returns the same result as (a:b) in matlab
    #   Converts the result to a row-vector
    return np.linspace(a,b,b-a+1,dtype=int)[np.newaxis,:]

if __name__ == '__main__':
    solver = GACPI()
    def odefn(t,X,p,aux):
        y = X[0]
        ydot = X[1]
        xf = p[0]
        # y'' + y(x) = 0
        return xf*np.array([
            ydot,
            -y
        ])

    def bcfn(ya,yb,p,aux):
        # y(0) = 0
        # y(pi/2) = 2
        return np.array([
                    ya[0] - 0,
                    yb[0] - 2,
                    p[0]  - pi/2])

    bvp = BVP(odefn,bcfn)

    x = np.linspace(0,1,3)
    y = np.array([[0,0.05,0.1],[0.1,1,2]])
    bvp.solution = Solution(x,y,[pi/2])

    sol = solver.solve(bvp)
