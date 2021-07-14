"""Generates the initial guess from a variety of sources."""
import copy
import logging
import time
from abc import ABC, abstractmethod

import numpy as np

import beluga
from beluga.data_classes.trajectory import Trajectory
from beluga.data_classes.problem_components import getattr_from_list
from beluga.data_classes.symbolic_problem import SymbolicProblem
from beluga.solvers.ivp_solvers import Propagator


def guess_generator(mode, *args, **kwargs):
    if mode == 'auto':
        generator_object = AutoGuessGenerator(*args, **kwargs)
    elif mode == 'static':
        generator_object = StaticGuessGenerator(*args, **kwargs)
    elif mode == 'ones':
        generator_object = OnesGuessGenerator(*args, **kwargs)
    else:
        raise NotImplementedError('Guess generator mode {} not implemented.'.format(mode))

    return generator_object


class GuessGenerator(ABC):
    def __init__(self, *args, **kwargs):
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

    @abstractmethod
    def generate(self, *args, **kwargs) -> Trajectory:
        return Trajectory()


class AutoGuessGenerator(GuessGenerator):
    def __init__(self, start=None, direction='forward', time_integrate=1, quad_guess=np.array([]), costate_guess=0.1,
                 control_guess=0.1, use_control_guess=False, param_guess=None):

        super().__init__()

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

    def generate(self, bvp_fn, solinit, guess_map, guess_map_inverse, param_guess=None) -> Trajectory:

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
            param_guess = np.ones(len(solinit.p))
        elif len(param_guess) < len(solinit.p):
            param_guess += np.ones(len(solinit.p) - len(param_guess))
        elif len(param_guess) > len(solinit.p):
            raise ValueError('param_guess too big. Maximum width allowed is ' + str(len(solinit.aux['parameters'])))
        nondynamical_param_guess = np.ones(len(solinit.nu))

        logging.debug('Generating initial guess by propagating: ')
        logging.debug(str(x0))

        time0 = time.time()
        prop = Propagator()
        solinit.t = np.array(tspan, dtype=beluga.DTYPE)
        solinit.y = np.array([x0, x0], dtype=beluga.DTYPE)
        solinit.lam = np.array([d0, d0], dtype=beluga.DTYPE)
        solinit.q = np.array([q0, q0], dtype=beluga.DTYPE)
        solinit.u = np.array([u0, u0], dtype=beluga.DTYPE)
        solinit.p = np.array(param_guess, dtype=beluga.DTYPE)
        solinit.nu = np.array(nondynamical_param_guess, dtype=beluga.DTYPE)
        sol = guess_map(solinit)
        solivp = prop(bvp_fn.deriv_func, bvp_fn.quad_func, sol.t, sol.y[0], sol.q[0],
                      sol.p, sol.k)
        solout = copy.deepcopy(solivp)
        solout.p = sol.p
        solout.nu = sol.nu
        solout.k = sol.k
        elapsed_time = time.time() - time0
        logging.debug('Initial guess generated in %.2f seconds' % elapsed_time)
        logging.debug('Terminal states of guess:')
        logging.debug(str(solout.y[-1, :]))

        return solout


class StaticGuessGenerator(GuessGenerator):
    def __init__(self, solinit):
        super(StaticGuessGenerator, self).__init__()
        self.solinit = solinit

    def generate(self, bvp_fn, solinit, ocp_map, ocp_map_inverse) -> Trajectory:
        """Directly specify initial guess structure"""
        return ocp_map(self.solinit)


class OnesGuessGenerator(GuessGenerator):
    def __init__(self, start=None, direction='forward', time_integrate=1, quad_guess=np.array([]), costate_guess=0.1,
                 control_guess=0.1, use_control_guess=False, param_guess=None):

        super().__init__()

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

    def generate(self, bvp_fn, solinit, guess_map, guess_map_inverse, param_guess=None) -> Trajectory:

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
            param_guess = np.ones(len(solinit.p))
        elif len(param_guess) < len(solinit.p):
            param_guess += np.ones(len(solinit.p) - len(param_guess))
        elif len(param_guess) > len(solinit.p):
            raise ValueError('param_guess too big. Maximum width allowed is ' + str(len(solinit.aux['parameters'])))
        nondynamical_param_guess = np.ones(len(solinit.nu))

        logging.debug('Generating initial guess by propagating: ')
        logging.debug(str(x0))

        time0 = time.time()
        solinit.t = np.linspace(tspan[0], tspan[-1], num=4)
        solinit.y = np.array([x0, x0, x0, x0], dtype=beluga.DTYPE)
        solinit.lam = np.array([d0, d0, d0, d0], dtype=beluga.DTYPE)
        solinit.q = np.array([q0, q0, q0, q0], dtype=beluga.DTYPE)
        solinit.u = np.array([u0, u0, u0, u0], dtype=beluga.DTYPE)
        solinit.p = np.array(param_guess, dtype=beluga.DTYPE)
        solinit.nu = np.array(nondynamical_param_guess, dtype=beluga.DTYPE)
        sol = guess_map(solinit)
        solout = copy.deepcopy(sol)
        solout.k = sol.k
        elapsed_time = time.time() - time0
        logging.debug('Initial guess generated in %.2f seconds' % elapsed_time)
        logging.debug('Terminal states of guess:')
        logging.debug(str(solout.y[-1, :]))

        return solout


def match_constants_to_states(prob: SymbolicProblem, sol: Trajectory):
    state_names = getattr_from_list(prob.states + [prob.independent_variable], 'name')

    initial_states = np.hstack((sol.y[0, :], sol.t[0]))
    terminal_states = np.hstack((sol.y[-1, :], sol.t[-1]))

    initial_bc = dict(zip(state_names, initial_states))
    terminal_bc = dict(zip(state_names, terminal_states))

    constant_names = getattr_from_list(prob.constants, 'name')
    for ii, bc0 in enumerate(initial_bc):
        if bc0 + '_0' in constant_names:
            jj = getattr_from_list(prob.constants, 'name').index(bc0 + '_0')
            sol.k[jj] = initial_bc[bc0]

    for ii, bcf in enumerate(terminal_bc):
        if bcf + '_f' in constant_names:
            jj = getattr_from_list(prob.constants, 'name').index(bcf + '_f')
            sol.k[jj] = terminal_bc[bcf]

    return sol
