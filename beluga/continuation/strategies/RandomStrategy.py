#==============================================================================#
# Author: Justin Mansell (2016)
# Description: Continuation for 2 variables using a random path.
# Note: Many functions redundant with manual strategy. This is intentional
#       to avoid being dependent on ManualStrategy.py (which may be updated).
#==============================================================================#
from beluga.continuation.ContinuationVariable import ContinuationVariable
#from RandomPathGen import RandomPath
import numpy as np
import random
import logging

def RandomPath(Xi, Xf, minsteps, agg = 0.5):
      #Random Path generation routine.
      #INPUT: Xi = array of initial coordinates
      #       Xf = array of target coordinates
      #      agg = aggression parameter (0 < agg <= 1)
      # minsteps = minimum number of steps for the path
      #OUTPUT: X = array of step coordinates for each variable
      Xi = np.array(Xi)
      Xf = np.array(Xf)
      dl = np.linalg.norm(abs(Xf - Xi)/minsteps) #Compute nominal step length
      maxsteps = 1000 #Maximum number of steps
      alfa = (1 - agg) * np.pi/2.0 #Maximum angle from center line for step direction

      #-----------------------------Generate Path--------------------------------#
      step = 0 #Step counter
      X = [Xi] #List of step coordinates
      while step < maxsteps:
          Xc = X[step] #Current location
          delX = Xf - Xc #Target vector
          if np.linalg.norm(delX) <= dl:
              X.append(Xf) #Within a step length of target. We're done.
              break

          ##Create list of angles defining the target vector
          cline = [] #List of angles to define delX vector
          cline.append(np.arctan2(delX[1], delX[0]))

          ##Randomize each hyperspherical coordiante
          phi = []
          for theta in cline:
              phi.append(random.uniform(theta - alfa, theta + alfa))

          ##Compute the step
          dx = np.array([0.0] * len(Xi)) #Step length vector
          dx[0] = dl * np.cos(phi[0])
          dx[1] = dl * np.sin(phi[0])
          X.append(Xc + dx)
          step = step + 1
      return X



# Can be subclassed to allow automated stepping
class RandomStrategy(object):
    """Defines one continuation step in continuation set"""
    # A unique short name to select this class
    name = 'random'

    def __init__(self, num_cases = 1, vars=[], bvp=None):
        self.bvp = bvp
        self._num_cases = num_cases
        self._agg = 0.5 # aggression parameter (can range from 0 to 1)
        self.vars = {}  # dictionary of values
        self.ctr  = 0   # iteration counter
        self.last_bvp = None

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_bvp = None

    def clear(self):
        """Clears all the previously set continuation variables"""
        self.vars = {}
        self.reset()
    #
    # def get_ctr(self):
    #     return self.ctr

    def set_bvp(self, bvp):
        self.bvp = bvp
        #Check that we have the correct number of variables
        #TODO: Generalize random path to any number of continuation variables
        num_cont_vars = 0
        for var_type in self.vars.keys(): #Count all the continuation variables
            num_cont_vars+=len(self.vars[var_type])
        if num_cont_vars > 2:
            raise ValueError('Cannot yet run random continuation for more than two variables')

        # Iterate through all types of variables
        Xi=[] #Initial vector in the continuation space
        Xf=[] #Target vector in the continuation space
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():

                # Look for the variable name from continuation in the BVP
                if var_name not in bvp.solution.aux[var_type].keys():
                    raise ValueError('Variable '+var_name+' not found in boundary value problem')

                # Set current value of each continuation variable
                self.vars[var_type][var_name].value = bvp.solution.aux[var_type][var_name]

                #Append the start and end states of the variable to X
                Xi.append(self.vars[var_type][var_name].value)
                Xf.append(self.vars[var_type][var_name].target)

        #Generate the continuation path
        Xpath = RandomPath(Xi,Xf,self._num_cases,self._agg)

        #Desseminate the steps for each variable
        varsteps1, varsteps2 = zip(*Xpath)
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                if self.vars[var_type][var_name].target == varsteps1[-1]:
                    self.vars[var_type][var_name].steps=varsteps1
                else:
                    self.vars[var_type][var_name].steps=varsteps2

    def set(self, var_type,name,target):
        if var_type not in self.vars.keys():
            self.vars[var_type] = {}

        # Create continuation variable object
        self.vars[var_type][name] = ContinuationVariable(name,target)
        return self

    def num_cases(self,num_cases=None, agg=0.5):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self._agg   = agg
            return self

    def terminal(self, name,target):
        self.set('terminal',name,target)
        return self

    def initial(self, name,target):
        self.set('initial',name,target)
        return self

    def const(self, name,target):
        self.set('const',name,target)
        return self

    # def constraint(self, name,target):
    #     self.set('constraint',name,target)
    #     return self

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        return self.next()

    def next(self, ignore_last_step = False):
        """Generator class to create BVPs for the continuation step iterations
        ignore_last_bvp: Should the non-convergence of previous step be ignored?
        """

        if self.bvp is None:
            raise ValueError('No boundary value problem associated with this object')

        if not ignore_last_step and self.last_bvp is not None and not self.last_bvp.solution.converged:
            logging.error('The last step did not converge!')
            raise RuntimeError('Solution diverged! Stopping.')

        #Check the actual number of cases (may be less than specified number
        #due to the random path)
        actual_num_cases=[]
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                actual_num_cases.append(len(self.vars[var_type][var_name].steps))
        for ncases in actual_num_cases:
            if ncases != actual_num_cases[0]:
                raise ValueError('Step vector for different variables have different lengths')

        if self.ctr >= ncases:
            raise StopIteration

        # Update auxiliary variables using previously calculated step sizes
        for var_type in self.vars:
            for var_name in self.vars[var_type]:
                self.bvp.solution.aux[var_type][var_name] = self.vars[var_type][var_name].steps[self.ctr]

        self.ctr += 1
        self.last_bvp = self.bvp
        return self.bvp
