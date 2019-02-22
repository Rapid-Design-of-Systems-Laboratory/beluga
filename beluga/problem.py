"""
problem2 -- Rename to 'problem' after refactoring.
Contains class/functions related to defining the optimal control problems.
"""

import numpy as np
import copy
import json
import logging
import re
from functools import partialmethod
from collections import namedtuple, ChainMap
from itertools import zip_longest

from .scaling import Scaling
import time
from beluga.ivpsol import Propagator

Cost = namedtuple('Cost', ['expr', 'unit'])
class OCP(object):
    """
    Class containing information for an optimal control problem.

    Valid parameters and their arguments are in the following table.

    +--------------------------------+--------------------------------+--------------------------------+
    | Valid parameters               | arguments                      | datatype                       |
    +================================+================================+================================+
    | state                          | (name, EOM, unit)              | (string, string, string)       |
    +--------------------------------+--------------------------------+--------------------------------+
    | control                        | (name, unit)                   | (string, string)               |
    +--------------------------------+--------------------------------+--------------------------------+
    | constant                       | (name, value, unit)            | (string, float, string)        |
    +--------------------------------+--------------------------------+--------------------------------+
    | constant_of_motion             | (name, function, unit)         | (string, string, string)       |
    +--------------------------------+--------------------------------+--------------------------------+
    | quantity                       | (name, value)                  | (string, string)               |
    +--------------------------------+--------------------------------+--------------------------------+
    | custom_function                | (name, args, function)         | (string, list, function handle)|
    +--------------------------------+--------------------------------+--------------------------------+
    | symmetry                       | (function)                     | (string)                       |
    +--------------------------------+--------------------------------+--------------------------------+
    | parameter                      | (function, unit)               | (string, string)               |
    +--------------------------------+--------------------------------+--------------------------------+
    | path_cost                      | (function, unit)               | (string, string)               |
    +--------------------------------+--------------------------------+--------------------------------+
    | initial_cost                   | (function, unit)               | (string, string)               |
    +--------------------------------+--------------------------------+--------------------------------+
    | terminal_cost                  | (function, unit)               | (string, string)               |
    +--------------------------------+--------------------------------+--------------------------------+

    """

    def __init__(self, name=''):
        """Initializes problem object.
        Parameters
        ----------
        name - str
            Unique name for the problem
        """
        self.name = self._format_name(name)

        self._systems = {'default': {}}  # Dynamic system definitions
        self._properties = {}  # Problem properties
        self._constraints = ConstraintList()

        self._scaling = Scaling()

    # Alias for returning cost function by type
    def get_cost(self, cost_type):
        """Retrieves the cost function for the problem.
        Parameters
        ----------
        cost_type - str
            Type of cost function - path, initial or terminal
        """
        return self._properties.get(cost_type + '_cost', {'expr':'0','unit':'0'})

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
        self._properties[cost_type+'_cost'] = {'expr':expr, 'unit':unit}

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

    def get_property(self, property_name):
        """
        Returns the property specified by the name
        """
        return self._properties.get(property_name, [])

    # TODO: Write documentation for these aliases
    state = partialmethod(set_property, property_name='states', property_args=('name', 'eom', 'unit'))
    control = partialmethod(set_property, property_name='controls', property_args=('name', 'unit'))
    constant = partialmethod(set_property, property_name='constants', property_args=('name', 'value', 'unit'))
    constant_of_motion = partialmethod(set_property, property_name='constants_of_motion', property_args=('name', 'function', 'unit'))
    quantity = partialmethod(set_property, property_name='quantities', property_args=('name', 'value'))
    symmetry = partialmethod(set_property, property_name='symmetries', property_args=('function',))
    parameter = partialmethod(set_property, property_name='parameters', property_args=('name','unit'))
    custom_function = partialmethod(set_property, property_name='custom_functions', property_args=('name','args','handle'))

    states = partialmethod(get_property, property_name='states')
    controls = partialmethod(get_property, property_name='controls')
    constants = partialmethod(get_property, property_name='constants')
    constants_of_motion = partialmethod(get_property, property_name='constants_of_motion')
    quantities = partialmethod(get_property, property_name='quantities')
    symmetries = partialmethod(get_property, property_name='symmetries')
    parameters = partialmethod(get_property, property_name='parameters')
    custom_functions = partialmethod(get_property, property_name='custom_functions')

    # TODO: Maybe write as separate function?
    def independent(self, name, unit):
        self._properties['independent'] = {'name': name, 'unit': unit}

    # Aliases for defining properties of the problem
    path_cost = partialmethod(set_cost, cost_type='path')
    initial_cost = partialmethod(set_cost, cost_type='initial')
    terminal_cost = partialmethod(set_cost, cost_type='terminal')

    Lagrange = path_cost
    Mayer = terminal_cost


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
        return str({'name': self.name,
                    'properties': self._properties,
                    'constraints': self._constraints,
                    'continuation': str(self.continuation)})

    def _format_name(self, name):
        """Validates that the name is in the right format
            Only alphabets, numbers and underscores allowed
            Should not start with a number or underscore
            Required for the in-memory compilation of code to work
        """

        if re.match(r'[a-zA-Z]\w+', name):
            return name
        else:
            raise ValueError("""Invalid problem name specified.
            Only alphabets, numbers and underscores allowed
            Should start with an alphabet""")

    def as_json(self):
        """Converts the problem definition into a pure dictionary."""
        output = self._properties
        output['problem_name'] = self.name
        output['constraints'] = self._constraints
        return json.dumps(output)


class ConstraintList(dict):
    """
    Class containing information for the constraints on an optimal control problem.

    Valid parameters and their arguments are in the following table.

    +--------------------------------+----------------------------------------+---------------------------------------------+
    | Valid parameters               | arguments                              | datatype                                    |
    +================================+========================================+=============================================+
    | initial                        | (function, unit)                       | (string, string)                            |
    +--------------------------------+----------------------------------------+---------------------------------------------+
    | terminal                       | (function, unit)                       | (string, string)                            |
    +--------------------------------+----------------------------------------+---------------------------------------------+
    | path                           | (function, unit, lb, ub, activator)    | (string, string, str/num, str/num, string)  |
    +--------------------------------+----------------------------------------+---------------------------------------------+

    """
    def __new__(cls, *args, **kwargs):
        obj = super(ConstraintList, cls).__new__(cls, *args, **kwargs)
        return obj

    def add_constraint(self, *args, constraint_type='', constraint_args=[], **kwargs):
        """
        Adds constraint of the specified type
        Returns reference to self.constraint_aliases for chaining
        """

        c_list = self.get(constraint_type, [])

        constraint = _combine_args_kwargs(constraint_args, args, kwargs)
        c_list.append(constraint)
        self[constraint_type] = c_list

        return self

    # Aliases for defining constraints of different types
    constraint_args = ('expr', 'unit')
    initial = partialmethod(
        add_constraint, constraint_type='initial',
        constraint_args=constraint_args)
    path = partialmethod(
        add_constraint, constraint_type='path',
        constraint_args=constraint_args)
    terminal = partialmethod(
        add_constraint, constraint_type='terminal',
        constraint_args=constraint_args)


def _combine_args_kwargs(arg_list, args, kwargs, fillvalue=''):
    """Combines positional and keyword arguments
    Parameters
    ----------
    arg_list - list of str
        List of keys in order of positional arguments
    args - list of str
        List of positional arguments
    kwargs: dict
        Dictionary of keyword arguments
    Returns
    -------
    A dictionary merging kwargs and args with keys from
    from args_list
    Example
    -------
    >>> _combine_args_kwargs(['foo','bar'],[1,2],{'baz':3})
    {'foo':1, 'bar':2, 'baz': 3}
    """
    pos_args = {key: val for (key, val) in zip_longest(arg_list, args, fillvalue=fillvalue)}
    arg_dict = dict(ChainMap(kwargs, pos_args))
    return (arg_dict)


BVP = namedtuple('BVP', 'deriv_func bc_func compute_control path_constraints')
BVP.__new__.__defaults__ = (None,) # path constraints optional


class GuessGenerator(object):
    """Generates the initial guess from a variety of sources."""
    def __init__(self, **kwargs):
        self.setup_funcs = {'auto': self.setup_auto,
                            'static': self.setup_static}
        self.generate_funcs = {'auto': self.auto,
                               'static': self.static}
        self.setup(**kwargs)
        self.dae_num_states = 0

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

    def setup_auto(self, start=None,
                   direction='forward',
                   time_integrate=1,
                   quad_guess=np.array([]),
                   costate_guess=0.1,
                   control_guess=0.1,
                   use_control_guess=False,
                   param_guess=None):
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

        if self.direction == 'reverse':
            tspan = [0, -self.time_integrate]

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
        solivp = prop(bvp_fn.deriv_func, bvp_fn.quad_func, sol.t, sol.y[0], sol.q[0], sol.u[0], sol.dynamical_parameters, np.fromiter(sol.aux['const'].values(), dtype=np.float64))
        solout = copy.deepcopy(solivp)
        solout.dynamical_parameters = sol.dynamical_parameters
        solout.nondynamical_parameters = sol.nondynamical_parameters
        solout.aux = sol.aux
        elapsed_time = time.time() - time0
        logging.debug('Initial guess generated in %.2f seconds' % elapsed_time)
        logging.debug('Terminal states of guess:')
        logging.debug(str(solout.y[-1, :]))

        return solout
