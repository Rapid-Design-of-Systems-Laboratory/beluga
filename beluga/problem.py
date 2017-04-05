"""
problem2 -- Rename to 'problem' after refactoring.

Contains class/functions related to defining the optimal control problems.
"""

import scipy.optimize
import numpy as np
from functools import partialmethod
import logging
import os.path
import dill
import re

from beluga.continuation import ContinuationList

from collections import namedtuple, ChainMap
from itertools import zip_longest
from beluga.optim.Scaling import Scaling  # BUG
# from beluga.bvpsol import Solution
from beluga.utils import ode45, sympify2  # , keyboard

Cost = namedtuple('Cost', ['expr', 'unit'])
class OCP(object):
    """Builder class for defining optimal control problem."""

    def __init__(self, name=''):
        """Initializes problem object."""
        # self.name = self._format_name(name)
        self.name = name

        self._systems = {'default': {}}  # Dynamic system definitions
        self._properties = {}  # Problem properties
        self._constraints = ConstraintList()

        self._scaling = Scaling()

    # Alias for returning cost function by type
    def get_cost(self, cost_type):
        return self._properties.get(cost_type + '_cost', {'expr':'0','unit':'0'})

    def set_cost(self, expr, unit, cost_type):
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


class ConstraintList(list):

    def add_constraint(self, *args, constraint_type='', constraint_args=[], **kwargs):
        """
        Adds constraint of the specified type

        Returns reference to self.constraint_aliases for chaining
        """
        constraint = _combine_args_kwargs(constraint_args, args, kwargs)
        cobj = SymbolicVariable(constraint, sym_key='expr')
        cobj.type = constraint_type
        self.append(cobj)
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
                constraint_args=('type', 'name', 'expr', 'direction', 'bound', 'unit')
                )

    def get(self, constraint_type):
        """
        Returns list of constraints of a specific type
        """
        return [c for c in self if c.type == constraint_type]

def _combine_args_kwargs(arg_list, args, kwargs, fillvalue=''):
    """
    arg_list: List of keys in order of positional arguments
    args: List of positional arguments
    kwargs: Dictionary of keyword arguments

    Returns a dictionary merging kwargs and args with keys from
    from args_list

    >>> _combine_args_kwargs(['foo','bar'],[1,2],{'baz':3})
    {'foo':1, 'bar':2, 'baz': 3}
    """
    pos_args = {key: val for (key, val) in
                zip_longest(arg_list, args, fillvalue=fillvalue)}
    arg_dict = dict(ChainMap(kwargs, pos_args))
    return (arg_dict)

class SymbolicVariable(object):
    """
    Represents an object that can be used in SymPy and is created from a dict
    """

    def __init__(self, param_dict, sym_key='name'):
        self.__dict__ = {k: sympify2(v) for k,v in param_dict.items()}
        self.param_list = param_dict.keys()
        if sym_key is not None:
            self._sym = self.__dict__[sym_key]
        else:
            self._sym = None

    def _sympy_(self):
        """
        Makes the object usable in sympy expressions directly
        """
        return self._sym

    def __repr__(self):
        return str(self._sym)

    def keys(self):
        return self.param_list

    def __getitem__(self, key):
        return getattr(self, key)

    def __eq__(self, other):
        return str(self._sym) == str(other)


class Guess(object):
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

    def static(self, bvp):
        """Directly specify initial guess structure"""
        bvp.solution = self.solinit
        return self.solinit

    def setup_file(self, filename='', step=0, iteration=0):
        self.filename = filename
        self.step = step
        self.iteration = iteration
        if not os.path.exists(self.filename) or not os.path.isfile(self.filename):
            logging.error('Data file ' + self.filename + ' not found.')
            raise ValueError('Data file not found!')

    def file(self, bvp):
        """Generates initial guess by loading an existing data file"""
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
        fp.close()
        bvp.solution = sol
        logging.info('Initial guess loaded')
        return sol

    def setup_auto(self, start=None,
                   direction='forward',
                   time_integrate=0.1,
                   costate_guess=0.1,
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

    def auto(self, bvp, param_guess=None):
        """Generates initial guess by forward/reverse integration."""

        # Assume normalized time from 0 to 1
        tspan = [0, 1]

        x0 = np.array(self.start)

        # Add costates
        if isinstance(self.costate_guess, float):
            x0 = np.r_[x0, self.costate_guess * np.ones(len(self.start))]
        else:
            x0 = np.r_[x0, self.costate_guess]
        # Add time of integration to states
        x0 = np.append(x0, self.time_integrate)

        # Guess zeros for missing parameters
        # TODO: Automatically generate parameter guess values

        if param_guess is None:
            param_guess = np.zeros(len(bvp.solution.aux['parameters']))
        elif len(param_guess) < len(bvp.solution.aux['parameters']):
            param_guess += np.zeros(len(bvp.solution.aux['parameters']) - len(param_guess))
        elif len(param_guess) > len(bvp.solution.aux['parameters']):
            # TODO: Write a better error message
            raise ValueError('param_guess too big. Maximum length allowed is ' +
                             len(bvp.solution.aux['parameters']))

        # dae_num_states = bvp.dae_num_states
        # dae_guess = np.ones(dae_num_states) * 0.1
        # dhdu_fn = bvp.dae_func_gen(0, x0, param_guess, bvp.solution.aux)
        #
        # dae_x0 = scipy.optimize.fsolve(dhdu_fn, dae_guess, xtol=1e-5)
        # # dae_x0 = dae_guess
        #
        # x0 = np.append(x0, dae_x0)  # Add dae states

        logging.debug('Generating initial guess by propagating: ')
        # logging.debug(str(x0))
        [t, x] = ode45(bvp.deriv_func, tspan, x0, param_guess, bvp.solution.aux)
        # x1, y1 = ode45(SingleShooting.ode_wrap(deriv_func, paramGuess, aux), [x[0],x[-1]], y0g)
        bvp.solution.x = t
        bvp.solution.y = x.T
        bvp.solution.parameters = param_guess
        return bvp.solution
