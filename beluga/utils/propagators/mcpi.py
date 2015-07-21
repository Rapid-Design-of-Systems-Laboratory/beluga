import numpy as np
from math import *
def mcpi(ode, tSpan, x0, *args, N = 100):
    """
    Propagates a system of ODEs using the Modified Chebyshev-Picard Iteration method
    """
    tau = np.cos(np.linspace(N,0,N+1)*pi/N)
    omega1 = (tSpan[-1]+tSpan[0])/2
    omega2 = (tSpan[-1]-tSpan[0])/2

    T = chebypoly(np.array(range(0,N+1,1)),tau);
    print(T.shape)
    len(tau)
    # V = np.ones(1,len(tau))/N;
    # V[1:-2] = V[1:-1]*2;
    # TV1 = bsxfun(@times,T(1:N,:),V);
    # TV1 = T[0:N-1,:]
    # TV2 = bsxfun(@times,T(3:N+2,:),V);
    # TV = bsxfun(@rdivide,(TV1-TV2),(2.*(1:N))');
    # TV(end,:) = TV1(end,:)./(2*N)';
    # S = 2.*((-1).^((1:N)+1));
    # Cx = T(1:N+1,1:N+1)';
    # Cx(:,1) = Cx(:,1)./2;


    # print(T)
    pass

def chebypoly(k, tau):
    # Computes T_k(x) for all points in tau for all k
    return k*np.arccos(tau);

if __name__ == '__main__':
    mcpi(None,[0, 1],[1])
