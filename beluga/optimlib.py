"""
optimlib

Contains class/functions related to defining the optimal control problems
"""
import scipy.optimize
import numpy as np
from functools import partial
import logging
import os.path
import types
import dill
import re

from .continuation import ContinuationList
from collections import namedtuple
from itertools import zip_longest

from beluga.bvpsol import Solution
# from beluga.utils import keyboard
from beluga.utils import ode45

class Problem(object):
    """
    Defines an optimal control problem
    """
    def __init__(self,name):
        self.name = self._format_name(name)

        self._systems = {'default': {}} # Dynamic system definitions
        self._properties = {} # Problem properties
        self._constraints = []
        self.continuation = ContinuationList()
        self.steps = self.continuation  # Alias for continuation

        self.guess = Guess()    # Initial guess builder

        # Aliases that add known types of dynamic elements to systems
        # TODO: Write documentation for these aliases
        self.state = partial(self.add_dynamic_element,
                element_kind='states',
                element_struct=namedtuple('State',['name', 'eom', 'unit'])
                )
        self.control = partial(self.add_dynamic_element,
                element_kind='controls',
                element_struct=namedtuple('Control',['name','unit'])
                )
        self.constant = partial(self.add_dynamic_element,
                element_kind='constants',
                element_struct=namedtuple('Constant',['name','value','unit'])
                )
        self.quantity = partial(self.add_dynamic_element,
                element_kind='quantities',
                element_struct=namedtuple('Quantity',['name','value'])
                )

        # TODO: Maybe write as separate function?
        self.independent = partial(self.add_property,
                property_name='independent',
                property_struct=namedtuple('IndependentVar',['name','unit'])
                )

        # Aliases for defining properties of the problem
        self.cost = partial(self.add_property,
                property_name='cost',
                property_struct=namedtuple('Cost',['type', 'expr', 'unit'])
                )

        self.path_cost = partial(self.cost, 'path')
        self.terminal_cost = partial(self.cost, 'terminal')
        self.Lagrange = self.path_cost
        self.Mayer = self.terminal_cost

        # Aliases for defining constraints of different types
        self.constraint_aliases = types.SimpleNamespace()

        constraint_struct = namedtuple('Constraint',['type','expr', 'unit'])
        setattr(self.constraint_aliases,'initial',
                partial(self.add_constraint,
                    constraint_type='initial',
                    constraint_struct=constraint_struct)
                )
        setattr(self.constraint_aliases,'terminal',
                partial(self.add_constraint,
                    constraint_type='terminal',
                    constraint_struct=constraint_struct)
                )
        setattr(self.constraint_aliases,'equality',
                partial(self.add_constraint,
                    constraint_type='equality',
                    constraint_struct=constraint_struct)
                )
        setattr(self.constraint_aliases,'interior_point',
                partial(self.add_constraint,
                    constraint_type='interior_point',
                    constraint_struct=constraint_struct)
                )
        setattr(self.constraint_aliases,'independent',
                partial(self.add_constraint,
                    constraint_type='independent',
                    constraint_struct=constraint_struct)
                )
        setattr(self.constraint_aliases,'path',
                partial(self.add_constraint,
                    constraint_type='path',
                    constraint_struct=namedtuple('Constraint',
                            ['type','name','expr','direction','bound','unit']))
                )

    def add_property(self, *args, property_name, property_struct=[], **kwargs ):
        """
        Adds a property of the optimal control problem

        >> add_property('cost',type='path',expr='')

        Returns a reference to self for chaining purposes
        """
        self._properties[property_name] = _combine_args_kwargs(property_struct,
                                                                   args, kwargs)
        return self

    def add_dynamic_element(self, *props, element_kind, element_struct,
                                            system_name='default', **kwprops):
        """
        Adds an dynamic element of the problem to a specified dynamic system

        element_kind: Defines category of element such as  state, control etc.
            and a list of keyword arguments (kwagrs) that form it's properties

        element_struct: Namedtuple to represent the property

        Returns a reference to self

        >>> add_element(self, 'x','v*cos(theta)','m',
                              element_kind='states',
                              element_struct=namedtuple('State',['name','eom','unit']),
                        )
        """

        system = self._systems.get(system_name, {})
        prop_list = system.get(element_kind, []) # Get prop list of given type

        # Pair prop names and values and create an object using element_struct
        prop_obj = _combine_args_kwargs(element_struct, props, kwprops)
        prop_list.append(prop_obj)

        # Add the element with its properties to the system
        system[element_kind] = prop_list
        self._systems[system_name] = system
        return self

    def constraints(self,*args,**kwargs):
        """
        This function is purely for aesthetic purposes while method chaining
        in the input file

        Returns the constraint_aliases object with alias methods
        """
        return self.constraint_aliases

    def add_constraint(self, *args, constraint_type='', constraint_struct=[], **kwargs):
        """
        Adds constraint of the specified type

        Returns reference to self.constraint_aliases for chaining
        """
        kwargs['type'] = constraint_type
        constraint = _combine_args_kwargs(constraint_struct, args, kwargs)
        self._constraints.append(constraint)
        return self.constraint_aliases

    def sympify(self):
        """
        Creates symbolic versions of all
        """

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return str({'name': self.name,
                    'systems': self._systems,
                    'properties': self._properties,
                    'constraints': self._constraints,
                    'continuation': str(self.continuation)})

    def _format_name(self, name):
        """Validates that the name is in the right format
            Only alphabets, numbers and underscores allowed
            Should not start with a number or underscore

            Required for the in-memory compilation of code to work
        """

        if re.match(r'[a-zA-Z]\w+',name):
            return name
        else:
            raise ValueError("""Invalid problem name specified.
            Only alphabets, numbers and underscores allowed
            Should start with an alphabet""")

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
        dae_guess = np.ones(dae_num_states)*0.1
        dhdu_fn = bvp.dae_func_gen(0,x0,param_guess,bvp.solution.aux)
        dae_x0 = scipy.optimize.fsolve(dhdu_fn, dae_guess,xtol=1e-5)
        # dae_x0 = dae_guess

        x0 = np.append(x0,dae_x0) # Add dae states
        logging.debug('Generating initial guess by propagating: ')
        logging.debug(str(x0))
        [t,x] = ode45(bvp.deriv_func,tspan,x0,param_guess,bvp.solution.aux)
        # x1, y1 = ode45(SingleShooting.ode_wrap(deriv_func, paramGuess, aux), [x[0],x[-1]], y0g)
        bvp.solution.x = t
        bvp.solution.y = x.T
        bvp.solution.parameters = param_guess
        return bvp.solution

def _combine_args_kwargs(struct, args, kwargs, fillvalue=''):
    """
    arg_list: List of keys in order of positional arguments
    args: List of positional arguments
    kwargs: Dictionary of keyword arguments

    Returns a dictionary merging kwargs and args with keys from
    from args_list

    >>> _combine_args_kwargs(['foo','bar'],[1,2],{'baz':3})
    {'foo':1, 'bar':2, 'baz': 3}
    """
    arg_dict = {key: val for (key, val) in zip_longest(struct._fields, args, fillvalue=fillvalue)}
    arg_dict.update(kwargs)
    return struct(**arg_dict) # Python 3.5 unpacking syntax
