"""Generates the initial guess from a variety of sources."""
import logging
import time
import numpy as np
import copy
from abc import ABC
from typing import Callable
from ..ivpsol.propagators import Propagator
from ..problib import Solution, Problem


class AutoGuessGenerator:
    def __init__(self, tspan=None, state_guess=None, parameter_guess=None, constraint_parameter_guess=None,
                 control_guess=None, costate_guess=-0.1, coparameter_guess=-0.1, constraint_multiplier_guess=-0.1):

        if tspan is None:
            self.tspan = [0, 0.1]
        else:
            self.tspan = tspan

        self.state_guess = state_guess
        self.parameter_guess = parameter_guess
        self.constraint_multiplier_guess = constraint_multiplier_guess
        self.control_guess = control_guess
        self.constraint_parameter_guess = constraint_parameter_guess
        self.costate_guess = costate_guess
        self.coparameter_guess = coparameter_guess
        self.constraint_multiplier_guess = constraint_multiplier_guess

    def __call__(self, prob: Problem):
        if self.state_guess is None:
            raise RuntimeError('"state_guess" needed for "auto" guess generator')

        y0 = np.array([self.state_guess], dtype=np.float64)

        if self.parameter_guess is None:
            p = np.array([])
        else:
            p = np.array(self.parameter_guess)

        k = np.array(prob.getattr_from_list(prob.constants, 'default_val'))

        if self.control_guess is None:
            control_generator = None
        elif isinstance(self.control_guess, Callable):
            control_generator = self.control_guess
        else:
            _u = np.array(self.control_guess)

            def control_generator(*_):
                return _u

        prop = Propagator(prob, control_generator=control_generator, propagate_quads=False)
        sol_prop = prop(prob.functional_problem.deriv_func, self.tspan, y0, p, k)

        return


class StaticGuessGenerator:
    pass


class OnesGuessGenerator:
    pass


def initial_helper(prob: Problem, sol: Solution):

    constant_names = prob.getattr_from_list(prob.constants, 'name')
    for state_idx, state_name in prob.getattr_from_list(prob.states, 'name'):
        initial_state_name = state_name + '_0'
        terminal_state_name = state_name + '_f'
        if initial_state_name in constant_names:
            sol.k[constant_names.index(initial_state_name)] = sol.y[0, state_idx]

        if terminal_state_name in constant_names:
            sol.k[constant_names.index(initial_state_name)] = sol.y[-1, state_idx]

    for quad_idx, quad_name in prob.getattr_from_list(prob.quads, 'name'):
        initial_quad_name = quad_name + '_0'
        terminal_quad_name = quad_name + '_f'
        if initial_quad_name in constant_names:
            sol.k[constant_names.index(initial_quad_name)] = sol.y[0, quad_idx]

        if terminal_quad_name in constant_names:
            sol.k[constant_names.index(terminal_quad_name)] = sol.y[-1, quad_idx]



