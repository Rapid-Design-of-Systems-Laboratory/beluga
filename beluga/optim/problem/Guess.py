from beluga.utils import ode45
from beluga.bvpsol import Solution
import numpy as np
import scipy
import scipy.optimize
from beluga.utils import keyboard
import os.path
import dill
import logging
from math import *
class Guess(object):
    """Generates the initial guess from a variety of sources"""

    def __init__(self, **kwargs):
        self.setup_funcs = {'auto':self.setup_auto,
                        'file':self.setup_file,
                        'static':self.setup_static,
                        }
        self.generate_funcs = {'auto':self.auto,
                        'file':self.file,
                        'static':self.static
                        }
        self.setup(**kwargs)

    def setup(self,mode='auto',**kwargs):
        """Sets up the initial guess generation process"""

        self.mode = mode
        if mode in self.setup_funcs:
            self.setup_funcs[mode](**kwargs)
        else:
            raise ValueError('Invalid initial guess mode specified')

        return self

    def generate(self,*args):
        """Generates initial guess data from given settings"""
        if self.mode in self.generate_funcs:
            return self.generate_funcs[self.mode](*args)
        else:
            raise ValueError('Invalid initial guess mode specified')


    def setup_static(self, solinit=None):
        self.solinit = solinit

    def static(self, bvp):
        """Directly specify initial guess structure"""
        bvp.solution = self.solinit
        return self.solinit

    def setup_file(self, filename='', step=0, iteration=0):
        self.filename = filename
        self.step = step
        self.iteration = iteration
        if not os.path.exists(self.filename) or not os.path.isfile(self.filename):
            logging.error('Data file '+self.filename+' not found.')
            raise ValueError('Data file not found!')

    def file(self, bvp):
        """Generates initial guess by loading an existing data file"""
        logging.info('Loading initial guess from '+self.filename)
        fp = open(self.filename,'rb')
        out = dill.load(fp)
        if self.step >= len(out['solution']):
            logging.error('Continuation step index exceeds bounds. Only '+str(len(out['solution']))+' continuation steps found.')
            raise ValueError('Initial guess step index out of bounds')

        if self.iteration >= len(out['solution'][self.step]):
            logging.error('Continuation iteration index exceeds bounds. Only '+str(len(out['solution'][self.step]))+' iterations found.')
            raise ValueError('Initial guess iteration index out of bounds')

        sol = out['solution'][self.step][self.iteration]
        fp.close()
        bvp.solution = sol
        logging.info('Initial guess loaded')
        return sol

    def setup_auto(self,start=None,
                        direction='forward',
                        time_integrate=0.1,
                        costate_guess =0.1,
                        param_guess = None):
        """Setup automatic initial guess generation"""

        if direction in ['forward','reverse']:
            self.direction = direction
        else:
            raise ValueError('Direction must be either forward or reverse.')


        self.time_integrate = abs(time_integrate)
        if time_integrate == 0:
            raise ValueError('Integration time must be non-zero')

        # TODO: Check size against number of states here
        self.start = start
        self.costate_guess = costate_guess
        self.param_guess = param_guess

    def auto(self,bvp,param_guess = None):
        """Generates initial guess by forward/reverse integration"""

        # Assume normalized time from 0 to 1
        tspan = [0, 1]

        x0 = np.array(self.start)

        # Add costates
        if isinstance(self.costate_guess,float):
            x0 = np.r_[x0,self.costate_guess*np.ones(len(self.start))]
        else:
            x0 = np.r_[x0,self.costate_guess]
        # Add time of integration to states
        x0 = np.append(x0,self.time_integrate)

        # Guess zeros for missing parameters
        # TODO: Automatically generate parameter guess values

        if param_guess is None:
            param_guess = np.zeros(len(bvp.solution.aux['parameters']))
        elif len(param_guess) < len(bvp.solution.aux['parameters']):
            param_guess += np.zeros(len(bvp.solution.aux['parameters'])-len(param_guess))
        elif len(param_guess) > len(bvp.solution.aux['parameters']):
            # TODO: Write a better error message
            raise ValueError('param_guess too big. Maximum length allowed is '+len(bvp.solution.aux['parameters']))

        dae_num_states = bvp.dae_num_states
        if dae_num_states > 0:
            dae_guess = np.ones(dae_num_states)*0.1
            dhdu_fn = bvp.dae_func_gen(0,x0,param_guess,bvp.solution.aux)
            dae_x0 = scipy.optimize.fsolve(dhdu_fn, dae_guess,xtol=1e-5)
            # dae_x0 = dae_guess

            x0 = np.append(x0,dae_x0) # Add dae states
        
        logging.debug('Generating initial guess by propagating: ')
        logging.debug('x0: '+str(x0))
        [t,x] = ode45(bvp.deriv_func,tspan,x0,param_guess,bvp.solution.aux)
        logging.debug('xf: '+str(x[-1]))
        # x1, y1 = ode45(SingleShooting.ode_wrap(deriv_func, paramGuess, aux), [x[0],x[-1]], y0g)
        bvp.solution.x = t
        bvp.solution.y = x.T
        bvp.solution.parameters = param_guess
        return bvp.solution
