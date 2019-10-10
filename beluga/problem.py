import numpy as np
import copy
import json
import logging
import re
from functools import partialmethod
from collections import namedtuple
from sympy import Expr, Symbol
from beluga.utils import sympify, _combine_args_kwargs

from .scaling import Scaling
import time
from beluga.ivpsol import Propagator
from beluga.optimlib import BVP
Cost = namedtuple('Cost', ['expr', 'unit'])


class OCP(BVP):
    """
    Class defining an optimal control problem.

    Examples
    ========

    >>> from beluga.problem import OCP
    >>> sigma = OCP()

    """

    def __init__(self):
        """Initializes problem object.
        Parameters
        ----------
        name - str
            Unique name for the problem
        """

        self._systems = {'default': {}}  # Dynamic system definitions
        self._properties = {}  # Problem properties
        self._constraints = ConstraintList()

        self._scaling = Scaling()

        self.continuation = None

    def __repr__(self):
        if self._properties.keys():
            m = max(map(len, list(self._properties.keys()))) + 1
            return '\n'.join([k.rjust(m) + ': ' + repr(v)
                              for k, v in sorted(self._properties.items())])
        else:
            return self.__class__.__name__ + "()"

    def control(self, symbol, unit):
        r"""Defines a control variable.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.control('u', 'rad')
        controls: [{'symbol': u, 'unit': rad}]

        .. seealso::
            get_controls
        """
        if not isinstance(symbol, str):
            raise ValueError
        if not isinstance(unit, str):
            raise ValueError

        temp = self._properties.get('controls', [])
        temp.append({'symbol': Symbol(symbol), 'unit': sympify(unit)})
        self._properties['controls'] = temp
        return self

    def get_controls(self):
        r"""Returns a list of the control variables.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.control('u', 'rad')
        controls: [{'symbol': u, 'unit': rad}]
        >>> sigma.get_controls()
        [{'symbol': u, 'unit': rad}]

        .. seealso::
            control
        """
        temp = self._properties.get('controls', [])
        return temp

    def get_independent(self):
        r"""Gets the independent variable.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.independent('t', 's')
        independent: {'symbol': t, 'unit': s}
        >>> sigma.get_independent()
        {'symbol': t, 'unit': s}

        .. seealso::
            independent
        """
        temp = self._properties.get('independent', None)
        return temp

    def get_initial_cost(self):
        r"""Gets the initial cost of the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.initial_cost('x^2', 'm^2')
        initial_cost: {'function': x**2, 'unit': m**2}
        >>> sigma.get_initial_cost()
        {'function': x**2, 'unit': m**2}

        .. seealso::
            initial_cost, terminal_cost, get_initial_cost
        """
        return self._properties.get('initial_cost', None)

    def get_path_constraints(self):
        r"""Gets the path constraints for the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.path_constraint('x^2', 'm^2', lower='x_min', upper='x_max', activator='eps', method='utm')
        path_constraints: [{'function': x**2, 'unit': m**2, 'lower': x_min, 'upper': x_max, 'activator': eps, 'method': 'utm'}]
        >>> sigma.get_path_constraints()
        [{'function': x**2, 'unit': m**2, 'lower': x_min, 'upper': x_max, 'activator': eps, 'method': 'utm'}]

        .. seealso::
            path_constraints

        """
        return self._properties.get('path_constraints', [])

    def get_path_cost(self):
        r"""Gets the path cost of the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.path_cost('x^2', 'm^2')
        path_cost: {'function': x**2, 'unit': m**2}
        >>> sigma.get_path_cost()
        {'function': x**2, 'unit': m**2}

        .. seealso::
            path_cost, get_initial_cost, get_terminal_cost
        """
        return self._properties.get('path_cost', None)

    def get_quantities(self):
        r"""Gets the quantities for the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.quantity('m', 'x^2+y')
        switches: [{'symbol': m, 'function': x**2 + y}]
        >>> sigma.get_quantities()
        [{'symbol': m, 'function': x**2 + y}]

        .. seealso::
            quantity, get_switches
        """
        temp = self._properties.get('switches', [])
        return temp

    def get_switches(self):
        r"""Gets the switches for the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.switch('mass_flow', ['m0', 'm1'], [['m_0f - x'], ['x - m_0f']], 'eps')
        switches: [{'symbol': mass_flow, 'function': [m0, m1], 'conditions': [[m_0f - x], [-m_0f + x]], 'tolerance': eps}]
        >>> sigma.get_switches()
        [{'symbol': mass_flow, 'function': [m0, m1], 'conditions': [[m_0f - x], [-m_0f + x]], 'tolerance': eps}]

        .. seealso::
            switch, get_quantities
        """
        temp = self._properties.get('switches', [])
        return temp

    def get_terminal_cost(self):
        r"""Gets the terminal cost of the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.terminal_cost('x^2', 'm^2')
        terminal_cost: {'function': x**2, 'unit': m**2}
        >>> sigma.get_terminal_cost()
        {'function': x**2, 'unit': m**2}

        .. seealso::
            terminal_cost, get_initial_cost, get_path_cost
        """
        return self._properties.get('terminal_cost', None)

    def independent(self, symbol, unit):
        r"""Sets the independent variable.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.independent('t', 's')
        independent: {'symbol': t, 'unit': s}

        .. seealso::
            get_independent
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(unit, str):
            unit = sympify(unit)
        if not isinstance(symbol, Symbol):
            raise ValueError
        if not isinstance(unit, Expr):
            raise ValueError

        temp = {'symbol': symbol, 'unit': unit}
        self._properties['independent'] = temp
        return self

    def initial_cost(self, function, unit):
        r"""Sets the initial cost of the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.initial_cost('x^2', 'm^2')
        initial_cost: {'function': x**2, 'unit': m**2}

        .. seealso::
            path_cost, terminal_cost, get_initial_cost
        """
        if isinstance(function, str):
            function = sympify(function)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(function, Expr):
            raise ValueError
        if not isinstance(unit, Expr):
            raise ValueError

        temp = {'function': sympify(function), 'unit': sympify(unit)}
        self._properties['initial_cost'] = temp
        return self

    def path_constraint(self, function, unit, lower, upper, activator, method):
        r"""Defines a path constraint for the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.path_constraint('x^2', 'm^2', lower='x_min', upper='x_max', activator='eps', method='utm')
        path_constraints: [{'function': x**2, 'unit': m**2, 'lower': x_min, 'upper': x_max, 'activator': eps, 'method': 'utm'}]

        .. seealso::
            get_path_constraints

        """
        if isinstance(function, str):
            function = sympify(function)
        if isinstance(unit, str):
            unit = sympify(unit)
        if isinstance(lower, str):
            lower = sympify(lower)
        if isinstance(upper, str):
            upper = sympify(upper)
        if isinstance(activator, str):
            activator = sympify(activator)

        if not isinstance(function, Expr):
            raise ValueError
        if not isinstance(unit, Expr):
            raise ValueError
        if not isinstance(lower, Expr):
            raise ValueError
        if not isinstance(upper, Expr):
            raise ValueError
        if not isinstance(activator, Expr):
            raise ValueError
        if not isinstance(method, str):
            raise ValueError

        temp = self._properties.get('path_constraints', [])
        temp.append({'function': function, 'unit': unit, 'lower': lower, 'upper': upper, 'activator': activator, 'method': method})
        self._properties['path_constraints'] = temp
        return self

    def path_cost(self, function, unit):
        r"""Sets the path cost of the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.path_cost('x^2', 'm^2')
        path_cost: {'function': x**2, 'unit': m**2}

        .. seealso::
            initial_cost, terminal_cost, get_path_cost
        """
        if isinstance(function, str):
            function = sympify(function)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(function, Expr):
            raise ValueError
        if not isinstance(unit, Expr):
            raise ValueError

        temp = {'function': function, 'unit': unit}
        self._properties['path_cost'] = temp
        return self

    def switch(self, symbol, functions, conditions, tolerance):
        r"""Defines a switch for the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.switch('mass_flow', ['m0', 'm1'], [['m_0f - x'], ['x - m_0f']], 'eps')
        switches: [{'symbol': mass_flow, 'function': [m0, m1], 'conditions': [[m_0f - x], [-m_0f + x]], 'tolerance': eps}]

        .. seealso::
            quantity, get_switches
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)

        if not isinstance(functions, list):
            raise ValueError
        else:
            for ii, f in enumerate(functions):
                if isinstance(f, str):
                    functions[ii] = sympify(f)

        if not isinstance(conditions, list):
            raise ValueError
        else:
            for ii, l in enumerate(conditions):
                if not isinstance(l, list):
                    raise ValueError
                for jj, l2 in enumerate(l):
                    if isinstance(l2, str):
                        conditions[ii][jj] = sympify(l2)

        if isinstance(tolerance, str):
            tolerance = sympify(tolerance)

        if not isinstance(symbol, Symbol):
            raise ValueError

        for f in functions:
            if not isinstance(f, Expr):
                raise ValueError

        for l in conditions:
            for f in l:
                if not isinstance(f, Expr):
                    raise ValueError

        if not isinstance(tolerance, Expr):
            raise ValueError

        temp = self._properties.get('switches', [])
        temp.append({'symbol': symbol, 'function': functions, 'conditions': conditions, 'tolerance': tolerance})
        self._properties['switches'] = temp
        return self

    def terminal_cost(self, function, unit):
        r"""Sets the terminal cost of the OCP.

        Examples
        ========

        >>> from beluga.problem import OCP
        >>> sigma = OCP()
        >>> sigma.terminal_cost('x^2', 'm^2')
        terminal_cost: {'function': x**2, 'unit': m**2}

        .. seealso::
            initial_cost, path_cost, get_terminal_cost
        """
        if isinstance(function, str):
            function = sympify(function)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(function, Expr):
            raise ValueError
        if not isinstance(unit, Expr):
            raise ValueError

        temp = {'function': function, 'unit': unit}
        self._properties['terminal_cost'] = temp
        return self

    def get_cost(self, cost_type):
        """Retrieves the cost function for the problem.
        Parameters
        ----------
        cost_type - str
            Type of cost function - path, initial or terminal
        """
        return self._properties.get(cost_type + '_cost', {'expr': '0', 'unit': '0'})

    def get_property(self, property_name):
        """
        Returns the property specified by the name
        """
        return self._properties.get(property_name, [])

    def set_cost(self, expr, unit, cost_type):
        """Sets cost function for problem.
        Parameters
        ----------
        expr - str
            Expression for cost function
        unit - str
            Unit of cost function
        cost_type - str
            Type of cost function - path, initial or terminal
        """
        self._properties[cost_type+'_cost'] = {'expr': expr, 'unit': unit}

    def set_property(self, *args, property_name, property_args, **kwargs):
        """
        Adds a property of the optimal control problem
        Parameters
        ----------
        args
        property_name
        property_args
        kwargs
        Returns a reference to self for chaining purposes
        """
        prop = self._properties.get(property_name, [])
        prop.append(_combine_args_kwargs(property_args, args, kwargs))
        self._properties[property_name] = prop
        return self

    def quantity(self, symbol, function):
        r"""

        :param symbol:
        :param function:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(function, str):
            function = sympify(function)

        if not isinstance(symbol, Symbol):
            raise ValueError
        if not isinstance(function, Expr):
            raise ValueError

        temp = self._properties.get('switches', [])
        temp.append({'symbol': symbol, 'function': function})
        self._properties['switches'] = temp
        return self

    custom_function = partialmethod(set_property, property_name='custom_functions',
                                    property_args=('name', 'args', 'handle', 'derivs'))

    constants_of_motion = partialmethod(get_property, property_name='constants_of_motion')
    parameters = partialmethod(get_property, property_name='parameters')
    custom_functions = partialmethod(get_property, property_name='custom_functions')

    def constraints(self):
        """
        Returns the ConstraintList object containing alias methods
        This function is purely for aesthetic purposes while method chaining
        in the input file
        """
        return self._constraints

    def scale(self, **scale_mappings):
        """Defines scaling for dimensional units in the problem."""
        for unit, scale_expr in scale_mappings.items():
            self._scaling.unit(unit, scale_expr)

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return str({'properties': self._properties,
                    'constraints': self._constraints,
                    'continuation': str(self.continuation)})


class ConstraintList(dict):
    """
    Class containing information for the constraints on an optimal control problem.

    Valid parameters and their arguments are in the following table.

    +--------------------------------+----------------------------------------+----------------------------------------+
    | Valid parameters               | arguments                              | datatype                               |
    +================================+========================================+========================================+
    | initial                        | (function, unit)                       | (string, string)                       |
    +--------------------------------+----------------------------------------+----------------------------------------+
    | terminal                       | (function, unit)                       | (string, string)                       |
    +--------------------------------+----------------------------------------+----------------------------------------+
    | path                           | (function, unit, lb, ub, activator)    | (string, string, str/num, str/num,     |
    |                                |                                        |                               string)  |
    +--------------------------------+----------------------------------------+----------------------------------------+

    """
    # def __new__(cls, *args, **kwargs):
    #     obj = super(ConstraintList, cls).__new__(cls, *args, **kwargs)
    #     return obj

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def add_constraint(self, *args, constraint_type='', constraint_args=None, **kwargs):
        """
        Adds constraint of the specified type
        Returns reference to self.constraint_aliases for chaining
        """

        c_list = self.get(constraint_type, [])

        if constraint_args is None:
            constraint_args = list()

        constraint = _combine_args_kwargs(constraint_args, args, kwargs)
        c_list.append(constraint)
        self[constraint_type] = c_list

        return self

    def initial(self, function, unit):
        if not isinstance(function, str):
            raise ValueError
        if not isinstance(unit, str):
            raise ValueError

        temp = self.get('initial', [])
        temp.append({'function': sympify(function), 'unit': sympify(unit)})
        self['initial'] = temp
        return self

    def terminal(self, function, unit):
        if not isinstance(function, str):
            raise ValueError
        if not isinstance(unit, str):
            raise ValueError

        temp = self.get('terminal', [])
        temp.append({'function': sympify(function), 'unit': sympify(unit)})
        self['terminal'] = temp
        return self

    # def path(self, function, unit, lower, upper, activator, method):
    #

    # Aliases for defining constraints of different types
    constraint_args = ('expr', 'unit')


BVP = namedtuple('BVP', 'deriv_func bc_func compute_control path_constraints')
BVP.__new__.__defaults__ = (None,)  # path constraints optional


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

        self.mode = None
        self.solinit = None
        self.direction = None
        self.time_integrate = None
        self.start = None
        self.quad_guess = None
        self.costate_guess = None
        self.param_guess = None
        self.control_guess = None
        self.use_control_guess = None

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
        solinit.t = tspan
        solinit.y = np.array([x0, x0])
        solinit.dual = np.array([d0, d0])
        solinit.q = np.array([q0, q0])
        solinit.u = np.array([u0, u0])
        solinit.dynamical_parameters = param_guess
        solinit.nondynamical_parameters = nondynamical_param_guess
        sol = guess_map(solinit)
        solivp = prop(bvp_fn.deriv_func, bvp_fn.quad_func, sol.t, sol.y[0], sol.q[0], sol.u[0],
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
        solinit.y = np.array([x0, x0, x0, x0])
        solinit.dual = np.array([d0, d0, d0, d0])
        solinit.q = np.array([q0, q0, q0, q0])
        solinit.u = np.array([u0, u0, u0, u0])
        solinit.dynamical_parameters = param_guess
        solinit.nondynamical_parameters = nondynamical_param_guess
        sol = guess_map(solinit)
        solout = copy.deepcopy(sol)
        solout.const = sol.const
        elapsed_time = time.time() - time0
        logging.debug('Initial guess generated in %.2f seconds' % elapsed_time)
        logging.debug('Terminal states of guess:')
        logging.debug(str(solout.y[-1, :]))

        return solout
