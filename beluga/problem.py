"""
problem2 -- Rename to 'problem' after refactoring.

Contains class/functions related to defining the optimal control problems.
"""

import scipy.optimize
import numpy as np
import dill

import json
import logging
import os.path
import re
from functools import partialmethod
from collections import namedtuple, ChainMap
from itertools import zip_longest

from beluga.bvpsol import Scaling
from beluga.ivpsol.integrators import ode45
from beluga.utils import sympify, tic, toc
from beluga.ivpsol import Propagator

Cost = namedtuple('Cost', ['expr', 'unit'])
class OCP(object):
    """Builder class for defining optimal control problem."""

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
    state = partialmethod(set_property, property_name='states',
                    property_args=('name', 'eom', 'unit'))
    control = partialmethod(set_property, property_name='controls',
                    property_args=('name', 'unit'))
    constant = partialmethod(set_property, property_name='constants',
                    property_args=('name', 'value', 'unit'))
    quantity = partialmethod(set_property, property_name='quantities',
                    property_args=('name', 'value'))

    states = partialmethod(get_property, property_name='states')
    controls = partialmethod(get_property, property_name='controls')
    constants = partialmethod(get_property, property_name='constants')
    quantities = partialmethod(get_property, property_name='quantities')

    # TODO: Maybe write as separate function?
    def independent(self, name, unit):
        self._properties['independent'] = {'name': name, 'unit':unit}

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
    def __new__(cls, *args, **kwargs):
        obj = super(ConstraintList, cls).__new__(cls, *args, **kwargs)
        obj.adjoined = False
        return obj

    def set_adjoined(self, bool):
        self.adjoined = bool

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
    initial = partialmethod(add_constraint, constraint_type='initial',
                constraint_args=constraint_args)
    terminal = partialmethod(add_constraint, constraint_type='terminal',
                constraint_args=constraint_args)
    equality = partialmethod(add_constraint, constraint_type='equality',
                constraint_args=constraint_args)
    interior_point = partialmethod(add_constraint, constraint_type='interior_point',
                constraint_args=constraint_args)
    independent = partialmethod(add_constraint, constraint_type='independent',
                constraint_args=constraint_args)
    path = partialmethod(add_constraint, constraint_type='path',
                constraint_args=('name', 'expr', 'direction', 'bound', 'unit', 'start_eps')
                )

    # def get(self, constraint_type):
    #     """
    #     Returns list of constraints of a specific type
    #     """
    #     return [c for c in self if c.type == constraint_type]

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
    pos_args = {key: val for (key, val) in
                zip_longest(arg_list, args, fillvalue=fillvalue)}
    arg_dict = dict(ChainMap(kwargs, pos_args))
    return (arg_dict)


class SymVar(object):
    """
    Represents an object that can be used in SymPy and is created from a dict
    """

    def __init__(self, param_dict, sym_key='name', excluded=()):
        self.__dict__ = {k: sympify(v) if k not in excluded else v
                         for k, v in param_dict.items()}
        self.param_list = list(param_dict.keys())
        if sym_key is not None:
            self._sym = self.__dict__[sym_key]
        else:
            self._sym = None

    def _sympy_(self):
        """
        Makes the object usable in sympy expressions directly
        """
        return self._sym

    def __hash__(self):
        return hash(self._sym)

    def __eq__(self, other):
        return self._sym == other._sym

    def __repr__(self):
        return str(self._sym)

    def keys(self):
        return self.param_list

    def __getitem__(self, key):
        return getattr(self, key)

    def __eq__(self, other):
        return str(self._sym) == str(other)

BVP = namedtuple('BVP', 'deriv_func bc_func compute_control path_constraints')
BVP.__new__.__defaults__ = (None,) # path constraints optional

class GuessGenerator(object):
    """Generates the initial guess from a variety of sources."""

    def __init__(self, **kwargs):
        self.setup_funcs = {'auto': self.setup_auto,
                            'file': self.setup_file,
                            'static': self.setup_static,
                            }
        self.generate_funcs = {'auto': self.auto,
                               'file': self.file,
                               'static': self.static
                               }
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

    def static(self, bvp_fn, solinit):
        """Directly specify initial guess structure"""
        return self.solinit

    def setup_file(self, filename='', step=0, iteration=0):
        self.filename = filename
        self.step = step
        self.iteration = iteration
        if not os.path.exists(self.filename) or not os.path.isfile(self.filename):
            logging.error('Data file ' + self.filename + ' not found.')
            raise ValueError('Data file not found!')

    def file(self, bvp_fn, solinit):
        """Generates initial guess by loading an existing data file.

        bvp_fn : BVP
            BVP object containing functions

        solinit : Solution
            Solution object with some starting information (such as aux vars)
        """
        logging.info('Loading initial guess from ' + self.filename)
        fp = open(self.filename, 'rb')
        out = dill.load(fp)
        if self.step >= len(out['solution']):
            logging.error('Continuation step index exceeds bounds. Only ' +
                          str(len(out['solution']))
                          + ' continuation steps found.')
            raise ValueError('Initial guess step index out of bounds')

        if self.iteration >= len(out['solution'][self.step]):
            logging.error('Continuation iteration index exceeds bounds. Only '
                          + str(len(out['solution'][self.step]))
                          + ' iterations found.')
            raise ValueError('Initial guess iteration index out of bounds')

        sol = out['solution'][self.step][self.iteration]
        # sol.extra = None

        fp.close()

        logging.info('Initial guess loaded')
        return sol

    def setup_auto(self, start=None,
                   direction='forward',
                   time_integrate=0.1,
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
        self.costate_guess = costate_guess
        self.param_guess = param_guess
        self.control_guess = control_guess
        self.use_control_guess = use_control_guess

    def auto(self, bvp_fn, solinit, param_guess=None):
        """Generates initial guess by forward/reverse integration."""

        # Assume normalized time from 0 to 1
        tspan = [0, 1]

        x0 = np.array(self.start)

        # Add costates
        if isinstance(self.costate_guess, float):
            x0 = np.r_[x0, self.costate_guess * np.ones(len(self.start))]
        else:
            x0 = np.r_[x0, self.costate_guess]

        if isinstance(self.control_guess, float):
            u0 = self.control_guess*np.ones(self.dae_num_states)
        else:
            u0 = self.control_guess

        # Add time of integration to states

        # x0 = np.append(x0, self.time_integrate)

        # Guess zeros for missing parameters
        # TODO: Automatically generate parameter guess values

        if param_guess is None:
            param_guess = np.zeros(len(solinit.aux['parameters']))
        elif len(param_guess) < len(solinit.aux['parameters']):
            param_guess += np.zeros(len(solinit.aux['parameters']) - len(param_guess))
        elif len(param_guess) > len(solinit.aux['parameters']):
            # TODO: Write a better error message
            raise ValueError('param_guess too big. Maximum length allowed is ' +
                             len(solinit.aux['parameters']))

        param_guess[0] = self.time_integrate

        if self.dae_num_states > 0:
            dae_guess = u0
            if not self.use_control_guess:
                dhdu_fn = bvp_fn.get_dhdu_func(0, x0, param_guess, solinit.aux)

                dae_x0 = scipy.optimize.fsolve(dhdu_fn, dae_guess, xtol=1e-5)
            else:
                dae_x0 = dae_guess

            print('dae_x0',dae_x0)
            x0 = np.append(x0, dae_x0)  # Add dae states

        print('guess ode',id(bvp_fn.deriv_func))
        logging.debug('Generating initial guess by propagating: ')
        logging.debug(str(x0))

        if self.direction == 'reverse':
            tspan = [0, -1]

        tic()
        prop = Propagator()
        solivp = prop(bvp_fn.deriv_func_ode45, None, tspan, x0, [], param_guess, solinit.aux)
        elapsed_time = toc()
        logging.debug('Propagated initial guess in %.2f seconds' % elapsed_time)
        solinit.t = solivp.t
        solinit.y = solivp.y.T # TODO: This shouldn't be transposed, but it's gonna require significant reworking.
        solinit.parameters = param_guess
        return solinit
