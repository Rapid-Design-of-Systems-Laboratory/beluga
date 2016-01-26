# from autodiff import Function, Gradient
import numpy as np

from .. import Solution
from beluga.utils.ode45 import ode45
from ..Algorithm import Algorithm
from math import *
from beluga.utils.joblib import Memory
import logging

class BroydenShooting(Algorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, verbose=False):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose

    def set_cache_dir(self,cache_dir):
        self.cache_dir = cache_dir

    def solve(self,bvp,worker=None):
        """Solve a two-point boundary value problem
            using the single shooting method

        Args:
            deriv_func: the ODE function
            bc_func: the boundary conditions function
            solinit: a "Solution" object containing the initial guess
        Returns:
            solution of TPBVP
        Raises:
        """
        solinit = bvp.solution
        x  = solinit.x
        # Get initial states from the guess structure
        y0g = solinit.y[:,0]
        paramGuess = solinit.parameters

        deriv_func = bvp.deriv_func
        bc_func = bvp.bc_func

        aux = bvp.solution.aux
        # Only the start and end times are required for ode45
        t0 = x[0]
        tf = x[-1]

        # Extract number of ODEs in the system to be solved
        nOdes = y0g.shape[0]
        if solinit.parameters is None:
            nParams = 0
        else:
            nParams = solinit.parameters.size

        iter = 1            # Initialize iteraiton counter
        converged = False   # Convergence flag

        tspan = [t0,tf]
        old_res = np.nan;
        # tspan = np.linspace(0,1,100)

        # Evaluate the boundary conditions
        J    = np.eye(nOdes+nParams);
        # Propagate trajectory
        t,yy = ode45(deriv_func, tspan, y0g, paramGuess, aux)
        yf = yy[-1]
        yb = yf[:nOdes]  # States
        res = bc_func(y0g, yb, paramGuess, aux)

        while True:
            iter = iter+1
            # Solution converged if BCs are satisfied to tolerance
            if max(abs(res)) < self.tolerance:
                if self.verbose:
                    logging.info("Converged in "+str(iter)+" iterations.")
                converged = True
                break

            r1 = np.linalg.norm(res)
            if self.verbose:
                logging.debug('Residue: '+str(r1))

            dy = -0.1*np.dot(J, res);

            # Apply corrections to states and parameters (if any)

            if nParams > 0:
                dp = dy[nOdes:]
                dy0 = dy[:nOdes]
                paramGuess = paramGuess + dp
                y0g = y0g + dy0
            else:
                y0g = y0g + dy0

            old_res = res;
            # Propagate trajectory
            t,yy = ode45(deriv_func, tspan, y0g, paramGuess, aux)
            # Evaluate the boundary conditions
            res = bc_func(y0g, yb, paramGuess, aux)

            # Update approximation to Jacobian using Broydens formula
            d_res = res - old_res;
            old_J = J;

            oyp = np.dot(old_J, d_res) - dy;
            dyT = dy.reshape((1,nOdes+nParams));
            pB  = np.dot(dyT, old_J);
            M   = np.zeros((nOdes+nParams, nOdes+nParams))

            for i in range(0, nOdes+nParams):  # 1:n
                for j in range(0, nOdes+nParams): # 1:n
                  M[i][j] = oyp[i] * pB[0,j];

            print(np.dot(dyT,old_J).shape)
            rh = np.dot(np.dot(dyT,old_J),d_res)
            # print(M)
            print(rh)
            J = old_J - np.linalg.solve(M, rh);
            if iter>self.max_iterations:
                logging.warn("Maximum iterations exceeded!")
                break
            print('Iteration #');
            print(iter)

        # If problem converged, propagate solution to get full trajectory
        # Possibly reuse 'yy' from above?
        if converged:
            x1, y1 = ode45(deriv_func, [x[0],x[-1]], y0g, paramGuess, aux, abstol=1e-5, reltol=1e-5)
            sol = Solution(x1,y1.T,paramGuess,aux)
        else:
            # Fix this to be something more elegant
            sol = Solution(np.nan, np.nan, np.nan)
        bvp.solution = sol
        sol.aux = aux
        logging.debug(sol.y[:,0])
        return sol
