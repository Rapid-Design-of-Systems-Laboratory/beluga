# from autodiff import Function, Gradient
import numpy as np

from .. import Solution
from beluga.utils.ode45 import ode45
from ..Algorithm import Algorithm
from math import *
from beluga.utils.joblib import Memory
import logging

class NewtonArmijo(Algorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, verbose=False):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose

    def set_cache_dir(self,cache_dir):
        self.cache_dir = cache_dir

    def solve(self,bvp):
        """Solve a two-point boundary value problem
            using Newton-Armijo root solving method

        Args:
            bvp: Boundary value problem object
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


        while True:
            if iter>self.max_iterations:
                logging.warn("Maximum iterations exceeded!")
                break
            y0 = np.concatenate( (y0g, stm0) )  # Add STM states to system

            # Propagate STM and original system together
            # stm_ode45 = SingleShooting.ode_wrap(self.stm_ode_func,deriv_func, paramGuess, aux, nOdes = y0g.shape[0])

            # t,yy = ode45(stm_ode45, tspan, y0)
            t,yy = ode45(self.stm_ode_func, tspan, y0, deriv_func, paramGuess, aux, nOdes = y0g.shape[0])
            # Obtain just last timestep for use with correction
            yf = yy[-1]
            # Extract states and STM from ode45 output
            yb = yf[:nOdes]  # States
            phi = np.reshape(yf[nOdes:],(nOdes, nOdes)) # STM

            # Evaluate the boundary conditions
            res = bc_func(y0g, yb, paramGuess, aux)

            # self.bc_jac_func = self.__bcjac_csd
            # Solution converged if BCs are satisfied to tolerance
            if max(abs(res)) < self.tolerance:
                if self.verbose:
                    logging.info("Converged in "+str(iter)+" iterations.")
                converged = True
                break

            # Compute Jacobian of boundary conditions using numerical derviatives
            J   = self.bc_jac_func(bc_func, y0g, yb, phi, paramGuess, aux)
            # Compute correction vector
            r1 = np.linalg.norm(res)
            if self.verbose:
                logging.debug('Residue: '+str(r1))
            if r0 is not None:
                beta = (r0-r1)/(alpha*r0)
                if beta < 0:
                    beta = 1
            if r1>1:
                alpha = 1/(2*r1)
            else:
                alpha = 1
            r0 = r1

            try:
                dy0 = alpha*beta*np.linalg.solve(J,-res)
            except:
                rank1 = np.linalg.matrix_rank(J)
                rank2 = np.linalg.matrix_rank(np.c_[J,-res])
                if rank1 == rank2:
                    # dy0 = alpha*beta*np.dot(np.linalg.pinv(J),-res)
                    dy0 = -alpha*beta*np.dot(np.dot(np.linalg.inv(np.dot(J,J.T)),J).T,res)
                    # dy0 = -alpha*beta*np.dot( np.linalg.inv(np.dot(J.T,J)), J.T  )
                else:
                    # Re-raise exception if system is infeasible
                    raise
            # dy0 = -alpha*beta*np.dot(np.dot(np.linalg.inv(np.dot(J,J.T)),J).T,res)

            # Apply corrections to states and parameters (if any)
            if nParams > 0:
                dp = dy0[nOdes:]
                dy0 = dy0[:nOdes]
                paramGuess = paramGuess + dp
                y0g = y0g + dy0
            else:
                y0g = y0g + dy0

            iter = iter+1
            logging.debug('Iteration #'+str(iter))

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
