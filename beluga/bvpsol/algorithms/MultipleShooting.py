# from autodiff import Function, Gradient
import numpy as np

from .. import Solution
from ..Algorithm import Algorithm
from math import *
from beluga.utils import *
from beluga.utils import keyboard
from beluga.utils.joblib import Memory
from beluga.utils import Propagator
from beluga.utils.Worker import Worker
import logging

try:
    from mpi4py import MPI
    HPCSUPPORTED = 1
except ImportError:
    HPCSUPPORTED = 0

class MultipleShooting(Algorithm):
    def __init__(self, tolerance=1e-6, max_iterations=100, derivative_method='csd',cache_dir = None,verbose=False,cached=True,number_arcs=-1):
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
        self.number_arcs = number_arcs

        # TODO: Implement the host worker in a nicer way
        # Start Host MPI process
        # self.worker = Worker(mode='HOST')
        # self.worker.startWorker()
        # self.worker.Propagator.setSolver(solver='ode45')
        self.worker = None

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

        nOdes = ya[0].shape[0]
        nBCs = nOdes + nOdes*(self.number_arcs - 1)
        if parameters is not None:
            nBCs += parameters.size

        fx = bc_func(ya,yb,parameters,aux)

        M = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        N = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        J = [None for _ in range(self.number_arcs)]
        for arc in range(self.number_arcs):
            for i in range(nOdes):
                ya[arc][i] += h*1j
                f = bc_func(ya,yb,p,aux)
                M[arc][:,i] = np.imag(f)/h
                ya[arc][i] -= h*1j

                yb[arc][i] += h*1j
                f = bc_func(ya,yb,p,aux)
                N[arc][:,i] = np.imag(f)/h
                yb[arc][i] -= h*1j
            J[arc] = M[arc]+np.dot(N[arc],phi[arc])

        if parameters is not None:
            P = np.zeros((nBCs, p.size))
            for i in range(p.size):
                p[i] = p[i] + h*1j
                f = bc_func(ya,yb,p,aux)
                P[:,i] = np.imag(f)/h
                p[i] = p[i] - h*1j
            J.append(P)

        J = np.hstack(J)
        return J

    def __bcjac_fd(self, bc_func, ya, yb, phi, parameters, aux, StepSize=1e-7):
        # if parameters is not None:
        p  = np.array(parameters)
        h = StepSize

        nOdes = ya[0].shape[0]
        nBCs = nOdes + nOdes*(self.number_arcs - 1)
        if parameters is not None:
            nBCs += parameters.size

        fx = bc_func(ya,yb,parameters,aux)

        M = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        N = [np.zeros((nBCs, nOdes)) for _ in range(self.number_arcs)]
        J = [None for _ in range(self.number_arcs)]
        for arc in range(self.number_arcs):
            for i in range(nOdes):
                ya[arc][i] += h
                f = bc_func(ya,yb,p,aux)
                M[arc][:,i] = (f-fx)/h
                ya[arc][i] -= h

                yb[arc][i] += h
                f = bc_func(ya,yb,p,aux)
                N[arc][:,i] = (f-fx)/h
                yb[arc][i] -= h
            J[arc] = M[arc]+np.dot(N[arc],phi[arc])

        if parameters is not None:
            P = np.zeros((nBCs, p.size))
            for i in range(p.size):
                p[i] = p[i] + h
                f = bc_func(ya,yb,p,aux)
                P[:,i] = (f-fx)/h
                p[i] = p[i] - h
            J.append(P)

        J = np.hstack(J)
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

    def get_bc(self,ya,yb,p,aux):
        f1 = self.bc_func(ya[0],yb[-1],p,aux)
        for i in range(self.number_arcs-1):
            nextbc = yb[i]-ya[i+1]
            f1 = np.concatenate((f1,nextbc))
        return f1

    def solve(self,bvp):
        """Solve a two-point boundary value problem
            using the multiple shooting method

        Args:
            deriv_func: the ODE function
            bc_func: the boundary conditions function
            solinit: a "Solution" object containing the initial guess
        Returns:
            solution of TPBVP
        Raises:
        """
        guess = bvp.solution
        if self.number_arcs == 1:
            # Single Shooting
            from .SingleShooting import SingleShooting
            Single = SingleShooting(self.tolerance, self.max_iterations, self.derivative_method, self.cache_dir, self.verbose, self.cached)
            return Single.solve(bvp)

        if self.worker is not None:
            ode45 = self.worker.Propagator
        else:
            # Start local pool
            ode45 = Propagator(solver='ode45',process_count=self.number_arcs)
            ode45.startPool()

        # Decrease time step if the number of arcs is greater than the number of indices
        if self.number_arcs >= len(guess.x):
            x,ynew = ode45.solve(bvp.deriv_func, np.linspace(guess.x[0],guess.x[-1],self.number_arcs+1), guess.y[:,0], guess.parameters, guess.aux)
            guess.y = np.transpose(ynew)
            guess.x = x

        solinit = guess
        x = solinit.x
        # Get initial states from the guess structure
        y0g = [solinit.y[:,np.floor(i/self.number_arcs*x.shape[0])] for i in range(self.number_arcs)]
        paramGuess = solinit.parameters

        deriv_func = bvp.deriv_func
        self.bc_func = bvp.bc_func
        aux = bvp.solution.aux
        # Only the start and end times are required for ode45
        t0 = x[0]
        tf = x[-1]
        t = x

        # Extract number of ODEs in the system to be solved
        nOdes = solinit.y.shape[0]

        # Initial state of STM is an identity matrix
        stm0 = np.eye(nOdes).reshape(nOdes*nOdes)

        if solinit.parameters is None:
            nParams = 0
        else:
            nParams = solinit.parameters.size

        iter = 1            # Initialize iteration counter
        converged = False   # Convergence flag

        # Ref: Solving Nonlinear Equations with Newton's Method By C. T. Kelley
        # Global Convergence and Armijo's Rule, pg. 11
        alpha = 1
        beta = 1
        r0 = None
        phiset = [np.eye(nOdes) for i in range(self.number_arcs)]
        tspanset = [np.empty(t.shape[0]) for i in range(self.number_arcs)]

        tspan = [t0,tf]

        while True:
            if iter>self.max_iterations:
                logging.WARN("Maximum iterations exceeded!")
                break

            y0set = [np.concatenate( (y0g[i], stm0) ) for i in range(self.number_arcs)]

            for i in range(self.number_arcs):
                left = np.floor(i/self.number_arcs*t.shape[0])
                right = np.floor((i+1)/self.number_arcs*t.shape[0])
                if i == self.number_arcs-1:
                    right = t.shape[0] - 1
                tspanset[i] = [t[left],t[right]]
                #tspanset[i] = np.linspace(t[left],t[right],np.ceil(5000/self.number_arcs))

            # Propagate STM and original system together
            tset,yySTM = ode45.solve(self.stm_ode_func, tspanset, y0set, deriv_func, paramGuess, aux)

            # Obtain just last timestep for use with correction
            yf = [yySTM[i][-1] for i in range(self.number_arcs)]
            # Extract states and STM from ode45 output
            yb = [yf[i][:nOdes] for i in range(self.number_arcs)]  # States
            phiset = [np.reshape(yf[i][nOdes:],(nOdes, nOdes)) for i in range(self.number_arcs)] # STM

            # Evaluate the boundary conditions
            res = self.get_bc(y0g, yb, paramGuess, aux)
            # Solution converged if BCs are satisfied to tolerance
            if max(abs(res)) < self.tolerance:
                if self.verbose:
                    logging.info("Converged in "+str(iter)+" iterations.")
                converged = True
                break
            logging.debug(paramGuess)
            # Compute Jacobian of boundary conditions using numerical derviatives
            J   = self.bc_jac_func(self.get_bc, y0g, yb, phiset, paramGuess, aux)
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

            dy0 = alpha*beta*np.linalg.solve(J,-res)

            #dy0 = -alpha*beta*np.dot(np.transpose(np.dot(np.linalg.inv(np.dot(J,np.transpose(J))),J)),res)

            # dy0 = np.linalg.solve(J,-res)
            # if abs(r1 - 0.110277711594) < 1e-4:
            #     from beluga.utils import keyboard

            # Apply corrections to states and parameters (if any)

            if nParams > 0:
                dp = dy0[(nOdes*self.number_arcs):]
                dy0 = dy0[:(nOdes*self.number_arcs)]
                paramGuess = paramGuess + dp
                for i in range(self.number_arcs):
                    y0g[i] = y0g[i] + dy0[(i*nOdes):((i+1)*nOdes)]
            else:
                y0g = y0g + dy0
            iter = iter+1

            # print iter

        # If problem converged, propagate solution to get full trajectory
        # Possibly reuse 'yy' from above?
        if converged:
            x1, y1 = ode45.solve(deriv_func, [x[0],x[-1]], y0g[0], paramGuess, aux, abstol=1e-6, reltol=1e-6)
            sol = Solution(x1,y1.T,paramGuess)
        else:
            # Return initial guess if it failed to converge
            sol = solinit

        sol.converged = converged
        bvp.solution = sol
        sol.aux = aux

        if self.worker is None:
            ode45.closePool()
        return sol
