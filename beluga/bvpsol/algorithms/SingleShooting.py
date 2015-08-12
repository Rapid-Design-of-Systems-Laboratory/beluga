# from autodiff import Function, Gradient
import numpy as np

from .. import Solution
from beluga.utils.ode45 import ode45
from ..Algorithm import Algorithm
from math import *

from beluga.utils.joblib import Memory

class SingleShooting(Algorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, derivative_method='csd',cache_dir = None,verbose=False,cached=True):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.derivative_method = derivative_method
        if derivative_method == 'csd':
            self.stm_ode_func = self.__stmode_csd
            self.bc_jac_func  = self.__bcjac_csd
        elif derivative_method == 'fd':
            self.stm_ode_func = self.__stmode_fd
            self.bc_jac_func  = self.__bcjac_fd
        else:
            raise ValueError("Invalid derivative method specified. Valid options are 'csd' and 'fd'.")
        self.cached = cached
        if cached and cache_dir is not None:
            self.set_cache_dir(cache_dir)

    def set_cache_dir(self,cache_dir):
        self.cache_dir = cache_dir
        if self.cached and cache_dir is not None:
            memory = Memory(cachedir=cache_dir, mmap_mode='r', verbose=0)
            self.solve = memory.cache(self.solve)

    def __bcjac_csd(self, bc_func, ya, yb, phi, parameters, aux, StepSize=1e-50):
        ya = np.array(ya, dtype=complex)
        yb = np.array(yb, dtype=complex)
        # if parameters is not None:
        p  = np.array(parameters, dtype=complex)
        h = StepSize

        nOdes = ya.shape[0]
        nBCs = nOdes
        if parameters is not None:
            nBCs += parameters.size
        M = np.zeros((nBCs, nOdes))
        N = np.zeros((nBCs, nOdes))
        for i in range(nOdes):
            ya[i] = ya[i] + h*1.j
            # if parameters is not None:
            f = bc_func(ya,yb,p,aux)
            # else:
            #     f = bc_func(ya,yb)

            M[:,i] = np.imag(f)/h
            ya[i] = ya[i] - h*1.j
        # for i in range(nOdes):
            yb[i] = yb[i] + h*1.j
            # if parameters is not None:
            f = bc_func(ya,yb,p,aux)
            # else:
            #     f = bc_func(ya,yb)
            N[:,i] = np.imag(f)/h
            yb[i] = yb[i] - h*1.j

        if parameters is not None:
            P = np.zeros((nBCs, p.size))
            for i in range(p.size):
                p[i] = p[i] + h*1.j
                f = bc_func(ya,yb,p,aux)
                P[:,i] = np.imag(f)/h
                p[i] = p[i] - h*1.j
            J = np.hstack((M+np.dot(N,phi),P))
        else:
            J = M+np.dot(N,phi)
        return J

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
            f = bc_func(ya,yb,p,aux)
            M[:,i] = (f-fx)/h
            ya[i] = ya[i] - h

            yb[i] = yb[i] + h
            f = bc_func(ya,yb,p,aux)
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

    def __stmode_fd(self, x, y, odefn, parameters, aux, nOdes = 0, StepSize=1e-6):
        "Finite difference version of state transition matrix"
        N = y.shape[0]
        nOdes = int(0.5*(sqrt(4*N+1)-1))

        phi = y[nOdes:].reshape((nOdes, nOdes)) # Convert STM terms to matrix form
        Y = np.array(y[0:nOdes])  # Just states
        F = np.zeros((nOdes,nOdes))

        # Compute Jacobian matrix, F using finite difference
        fx = odefn(x,Y,parameters,aux)
        for i in range(nOdes):
            Y[i] = Y[i] + StepSize
            F[:,i] = (odefn(x, Y, parameters,aux)-fx)/StepSize
            Y[i] = Y[i] - StepSize

        # Phidot = F*Phi (matrix product)
        phiDot = np.real(np.dot(F,phi))
        return np.concatenate( (odefn(x,y,parameters,aux), np.reshape(phiDot, (nOdes*nOdes) )) )

    def __stmode_csd(self, x, y, odefn, parameters, aux, StepSize=1e-50):
        "Complex step version of State Transition Matrix"
        N = y.shape[0]
        nOdes = int(0.5*(sqrt(4*N+1)-1))

        phi = y[nOdes:].reshape((nOdes, nOdes)) # Convert STM terms to matrix form
        Y = np.array(y[0:nOdes],dtype=complex)  # Just states
        F = np.zeros((nOdes,nOdes))
        # Compute Jacobian matrix using complex step derivative
        for i in range(nOdes):
            Y[i] = Y[i] + StepSize*1.j
            F[:,i] = np.imag(odefn(x, Y, parameters, aux))/StepSize
            Y[i] = Y[i] - StepSize*1.j

        # Phidot = F*Phi (matrix product)
        phiDot = np.real(np.dot(F,phi))
        # phiDot = np.real(np.dot(g(x,y,paameters,aux),phi))
        return np.concatenate( (odefn(x,y, parameters, aux), np.reshape(phiDot, (nOdes*nOdes) )) )
        # return np.concatenate( f(x,y,parameters,aux), np.reshape(phiDot, (nOdes*nOdes) ))

    # def __stmode_ad(self, x, y, odefn, parameters, aux, nOdes = 0, StepSize=1e-50):
    #     "Automatic differentiation version of State Transition Matrix"
    #     phi = y[nOdes:].reshape((nOdes, nOdes)) # Convert STM terms to matrix form
    #     # Y = np.array(y[0:nOdes],dtype=complex)  # Just states
    #     # F = np.zeros((nOdes,nOdes))
    #     # # Compute Jacobian matrix using complex step derivative
    #     # for i in range(nOdes):
    #     #     Y[i] = Y[i] + StepSize*1.j
    #     #     F[:,i] = np.imag(odefn(x, Y, parameters, aux))/StepSize
    #     #     Y[i] = Y[i] - StepSize*1.j
    #     f = Function(odefn)
    #     g = Gradient(odefn)
    #
    #     # Phidot = F*Phi (matrix product)
    #     # phiDot = np.real(np.dot(F,phi))
    #     phiDot = np.real(np.dot(g(x,y,paameters,aux),phi))
    #     # return np.concatenate( (odefn(x,y, parameters, aux), np.reshape(phiDot, (nOdes*nOdes) )) )
    #     return np.concatenate( f(x,y,parameters,aux), np.reshape(phiDot, (nOdes*nOdes) ))


    # @staticmethod
    # def ode_wrap(func,*args, **argd):
    #    def func_wrapper(x,y0):
    #        return func(x,y0,*args,**argd)
    #    return func_wrapper

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

        # Initial state of STM is an identity matrix
        stm0 = np.eye(nOdes).reshape(nOdes*nOdes)
        iter = 1            # Initialize iteraiton counter
        converged = False   # Convergence flag

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None

        tspan = [t0,tf]
        # tspan = np.linspace(0,1,100)
        while True:
            if iter>self.max_iterations:
                print("Maximum iterations exceeded!")
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

            self.bc_jac_func = self.__bcjac_csd
            # Solution converged if BCs are satisfied to tolerance
            if max(abs(res)) < self.tolerance:
                if self.verbose:
                    print("Converged in "+str(iter)+" iterations.")
                converged = True
                break

            # Compute Jacobian of boundary conditions using numerical derviatives
            J   = self.bc_jac_func(bc_func, y0g, yb, phi, paramGuess, aux)
            # Compute correction vector
            r1 = np.linalg.norm(res)
            if self.verbose:
                print(r1)
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
                    dy0 = alpha*beta*np.dot(np.linalg.pinv(J),-res)
                else:
                    # Re-raise exception if system is infeasible
                    raise


            # Apply corrections to states and parameters (if any)
            if nParams > 0:
                dp = dy0[nOdes:]
                dy0 = dy0[:nOdes]
                paramGuess = paramGuess + dp
                y0g = y0g + dy0
            else:
                y0g = y0g + dy0
            iter = iter+1
            # print iter

        # If problem converged, propagate solution to get full trajectory
        # Possibly reuse 'yy' from above?
        if converged:
            x1, y1 = ode45(deriv_func, [x[0],x[-1]], y0g, paramGuess, aux, abstol=1e-6, reltol=1e-6)
            sol = Solution(x1,y1.T,paramGuess,aux)
        else:
            # Fix this to be something more elegant
            sol = Solution(np.nan, np.nan, np.nan)
        bvp.solution = sol
        sol.aux = aux
        return sol
