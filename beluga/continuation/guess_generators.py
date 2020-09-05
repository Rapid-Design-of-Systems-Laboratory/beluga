"""Generates the initial guess from a variety of sources."""
import logging
import time
import numpy as np
import copy

import beluga
from beluga.numeric.ivp_solvers import Propagator


def guess_generator(*args, **kwargs):
    """
    Helper for creating an initial guess generator.

    :param method: The method used to generate the initial guess
    :keywords: Additional keyword arguments passed into the guess generator.
    :return: An instance of the guess generator.
    """
    guess_gen = GuessGenerator()
    guess_gen.setup(*args, **kwargs)
    return guess_gen


class GuessGenerator(object):
    """Generates the initial guess from a variety of sources."""
    def __init__(self, **kwargs):
        self.setup_funcs = {'auto': self.setup_auto,
                            'static': self.setup_static,
                            'ones': self.setup_ones}
        self.generate_funcs = {'auto': self.auto,
                               'static': self.static,
                               'ones': self.ones}
        self.setup(**kwargs)
        self.dae_num_states = 0

        self.mode = 'auto'
        self.solinit = None
        self.direction = 'forward'
        self.time_integrate = 0.1
        self.start = None
        self.quad_guess = None
        self.costate_guess = None
        self.param_guess = None
        self.control_guess = None
        self.use_control_guess = False

    def setup(self, mode='auto', **kwargs):
        """Sets up the initial guess generation process"""
        self.mode = mode
        if mode in self.setup_funcs:
            self.setup_funcs[mode](**kwargs)
        else:
            raise ValueError('Invalid initial guess mode specified')

        return self

    def generate(self, *args):
        """Generates initial guess data from given settings"""
        if self.mode in self.generate_funcs:
            return self.generate_funcs[self.mode](*args)
        else:
            raise ValueError('Invalid initial guess mode specified')

    def setup_static(self, solinit=None):
        self.solinit = solinit

    def static(self, bvp_fn, solinit, ocp_map, ocp_map_inverse):
        """Directly specify initial guess structure"""
        return ocp_map(self.solinit)

    def setup_auto(self, start=None, direction='forward', time_integrate=1, quad_guess=np.array([]), costate_guess=0.1,
                   control_guess=0.1, use_control_guess=False, param_guess=None):
        """Setup automatic initial guess generation"""

        if direction in ['forward', 'reverse']:
            self.direction = direction
        else:
            raise ValueError('Direction must be either forward or reverse.')

        self.time_integrate = abs(time_integrate)
        if time_integrate == 0:
            raise ValueError('Integration time must be non-zero')

        # TODO: Check size against number of states here
        self.start = start
        self.quad_guess = quad_guess
        self.costate_guess = costate_guess
        self.param_guess = param_guess
        self.control_guess = control_guess
        self.use_control_guess = use_control_guess

    def auto(self, bvp_fn, solinit, guess_map, guess_map_inverse, param_guess=None):
        """Generates initial guess by forward/reverse integration."""

        if self.direction == 'forward':
            tspan = np.array([0, self.time_integrate])
        elif self.direction == 'reverse':
            tspan = np.array([0, -self.time_integrate])
        else:
            tspan = np.array([0, self.time_integrate])

        x0 = np.array(self.start)
        q0 = np.array(self.quad_guess)

        # Add costates
        if isinstance(self.costate_guess, float) or isinstance(self.costate_guess, int):
            d0 = np.r_[self.costate_guess * np.ones(len(self.start))]
        else:
            d0 = np.r_[self.costate_guess]

        if isinstance(self.control_guess, float) or isinstance(self.control_guess, float):
            u0 = self.control_guess*np.ones(self.dae_num_states)
        else:
            u0 = self.control_guess

        # Guess zeros for missing parameters
        if param_guess is None:
            param_guess = np.ones(len(solinit.dynamical_parameters))
        elif len(param_guess) < len(solinit.dynamical_parameters):
            param_guess += np.ones(len(solinit.dynamical_parameters) - len(param_guess))
        elif len(param_guess) > len(solinit.dynamical_parameters):
            raise ValueError('param_guess too big. Maximum length allowed is ' + str(len(solinit.aux['parameters'])))
        nondynamical_param_guess = np.ones(len(solinit.nondynamical_parameters))

        logging.debug('Generating initial guess by propagating: ')
        logging.debug(str(x0))

        time0 = time.time()
        prop = Propagator()
        solinit.t = np.array(tspan, dtype=beluga.DTYPE)
        solinit.y = np.array([x0, x0], dtype=beluga.DTYPE)
        solinit.dual = np.array([d0, d0], dtype=beluga.DTYPE)
        solinit.q = np.array([q0, q0], dtype=beluga.DTYPE)
        solinit.u = np.array([u0, u0], dtype=beluga.DTYPE)
        solinit.dynamical_parameters = np.array(param_guess, dtype=beluga.DTYPE)
        solinit.nondynamical_parameters = np.array(nondynamical_param_guess, dtype=beluga.DTYPE)
        sol = guess_map(solinit)
        solivp = prop(bvp_fn.deriv_func, bvp_fn.quad_func, sol.t, sol.y[0], sol.q[0],
                      sol.dynamical_parameters, sol.const)
        solout = copy.deepcopy(solivp)
        solout.dynamical_parameters = sol.dynamical_parameters
        solout.nondynamical_parameters = sol.nondynamical_parameters
        solout.const = sol.const
        elapsed_time = time.time() - time0
        logging.debug('Initial guess generated in %.2f seconds' % elapsed_time)
        logging.debug('Terminal states of guess:')
        logging.debug(str(solout.y[-1, :]))

        return solout

    def setup_ones(self, start=None, direction='forward', time_integrate=1, quad_guess=np.array([]), costate_guess=0.1,
                   control_guess=0.1, use_control_guess=False, param_guess=None):
        """Setup automatic initial guess generation"""

        if direction in ['forward', 'reverse']:
            self.direction = direction
        else:
            raise ValueError('Direction must be either forward or reverse.')

        self.time_integrate = abs(time_integrate)
        if time_integrate == 0:
            raise ValueError('Integration time must be non-zero')

        # TODO: Check size against number of states here
        self.start = start
        self.quad_guess = quad_guess
        self.costate_guess = costate_guess
        self.param_guess = param_guess
        self.control_guess = control_guess
        self.use_control_guess = use_control_guess

    def ones(self, bvp_fn, solinit, guess_map, guess_map_inverse, param_guess=None):

        if self.direction == 'forward':
            tspan = np.array([0, self.time_integrate])
        elif self.direction == 'reverse':
            tspan = np.array([0, -self.time_integrate])
        else:
            tspan = np.array([0, self.time_integrate])

        x0 = np.array(self.start)
        q0 = np.array(self.quad_guess)

        # Add costates
        if isinstance(self.costate_guess, float) or isinstance(self.costate_guess, int):
            d0 = np.r_[self.costate_guess * np.ones(len(self.start))]
        else:
            d0 = np.r_[self.costate_guess]

        if isinstance(self.control_guess, float) or isinstance(self.control_guess, float):
            u0 = self.control_guess * np.ones(self.dae_num_states)
        else:
            u0 = self.control_guess

        # Guess zeros for missing parameters
        if param_guess is None:
            param_guess = np.ones(len(solinit.dynamical_parameters))
        elif len(param_guess) < len(solinit.dynamical_parameters):
            param_guess += np.ones(len(solinit.dynamical_parameters) - len(param_guess))
        elif len(param_guess) > len(solinit.dynamical_parameters):
            raise ValueError('param_guess too big. Maximum length allowed is ' + str(len(solinit.aux['parameters'])))
        nondynamical_param_guess = np.ones(len(solinit.nondynamical_parameters))

        logging.debug('Generating initial guess by propagating: ')
        logging.debug(str(x0))

        time0 = time.time()
        solinit.t = np.linspace(tspan[0], tspan[-1], num=4)
        solinit.y = np.array([x0, x0, x0, x0], dtype=beluga.DTYPE)
        solinit.dual = np.array([d0, d0, d0, d0], dtype=beluga.DTYPE)
        solinit.q = np.array([q0, q0, q0, q0], dtype=beluga.DTYPE)
        solinit.u = np.array([u0, u0, u0, u0], dtype=beluga.DTYPE)
        solinit.dynamical_parameters = np.array(param_guess, dtype=beluga.DTYPE)
        solinit.nondynamical_parameters = np.array(nondynamical_param_guess, dtype=beluga.DTYPE)
        sol = guess_map(solinit)
        solout = copy.deepcopy(sol)
        solout.const = sol.const
        elapsed_time = time.time() - time0
        logging.debug('Initial guess generated in %.2f seconds' % elapsed_time)
        logging.debug('Terminal states of guess:')
        logging.debug(str(solout.y[-1, :]))

        return solout
