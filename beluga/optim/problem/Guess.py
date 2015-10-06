from beluga.utils import ode45
from beluga.bvpsol import Solution
import numpy as np
from beluga.utils import keyboard

class Guess(object):
    """Generates the initial guess from a variety of sources"""

    def __init__(self, **kwargs):
        self.setup_funcs = {'auto':self.setup_auto,
                        'file':self.setup_file,
                        'static':self.setup_static,
                        # 'custom':self.setup_custom
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
        raise NotImplementedError('Not implemented')

    def static(self):
        """Directly specify initial guess structure"""
        raise NotImplementedError("Method not implemented yet!")


    def setup_file(self, filename='', step=0, iter=0):
        raise NotImplementedError('Not implemented')

    def file(self):
        """Generates initial guess by loading an existing data file"""
        raise NotImplementedError("Method not implemented yet!")

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

        [t,x] = ode45(bvp.deriv_func,tspan,x0,param_guess,bvp.solution.aux)
        # x1, y1 = ode45(SingleShooting.ode_wrap(deriv_func, paramGuess, aux), [x[0],x[-1]], y0g)
        bvp.solution.x = t
        bvp.solution.y = x.T
        bvp.solution.parameters = param_guess
        return bvp.solution
