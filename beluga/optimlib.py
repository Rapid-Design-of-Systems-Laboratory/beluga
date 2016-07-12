"""
optimlib

Contains class/functions related to defining the optimal control problems
"""
import functools
import types
import re

from beluga.continuation2 import ContinuationList
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
        self.steps = self.continuation

        # Aliases that add known types of dynamic elements to systems
        # TODO: Write documentation for these aliases
        self.state = functools.partial(self.add_dynamic_element,
                element_kind='states',
                element_props=['name', 'eom', 'unit'])
        self.control = functools.partial(self.add_dynamic_element,
                element_kind='controls',
                element_props=['name','unit']
                )
        self.constant = functools.partial(self.add_dynamic_element,
                element_kind='constants',
                element_props=['name','value','unit'])
        self.quantity = functools.partial(self.add_dynamic_element,
                element_kind='quantities',
                element_props=['name','value'])

        # TODO: Maybe write as separate function?
        self.independent = functools.partial(self.add_property,
                property_name='independent',
                arg_list=['name','unit'])

        # Aliases for defining properties of the problem
        self.cost = functools.partial(self.add_property,
                property_name='cost', arg_list=['type', 'expr', 'unit'])

        self.path_cost = functools.partial(self.cost, 'path')
        self.terminal_cost = functools.partial(self.cost, 'terminal')
        self.Lagrange = self.path_cost
        self.Mayer = self.terminal_cost

        # Aliases for defining constraints of different types
        self.constraint_aliases = types.SimpleNamespace()

        constraint_arg_list = ['expr', 'unit']
        setattr(self.constraint_aliases,'initial',
                functools.partial(self.add_constraint,
                    type='initial',
                    arg_list=constraint_arg_list)
                )
        setattr(self.constraint_aliases,'terminal',
                functools.partial(self.add_constraint,
                    type='terminal',
                    arg_list=constraint_arg_list)
                )
        setattr(self.constraint_aliases,'equality',
                functools.partial(self.add_constraint,
                    type='equality',
                    arg_list=constraint_arg_list)
                )
        setattr(self.constraint_aliases,'interior_point',
                functools.partial(self.add_constraint,
                    type='interior_point',
                    arg_list=constraint_arg_list)
                )
        setattr(self.constraint_aliases,'independent',
                functools.partial(self.add_constraint,
                    type='independent',
                    arg_list=constraint_arg_list)
                )

    def add_property(self, *args, property_name, arg_list=[], **kwargs ):
        """
        Adds a property of the optimal control problem

        >> add_property('cost',type='path',expr='')

        Returns a reference to self for chaining purposes
        """
        self._properties[property_name] = _combine_args_kwargs(arg_list,
                                                                   args, kwargs)
        return self

    def add_dynamic_element(self, *props, element_kind, element_props,
                                            system_name='default', **kwprops):
        """
        Adds an dynamic element of the problem to a specified dynamic system

        element_kind: Defines category of element such as  state, control etc.
            and a list of keyword arguments (kwagrs) that form it's properties

        element_props: Names of properties in order that they appear in *props

        Returns a reference to self

        >>> add_element(self, 'x','v*cos(theta)','m',
                              element_kind='states',
                              element_props=['name','eom','unit'],
                        )
        """

        system = self._systems.get(system_name, {})
        prop_list = system.get(element_kind, []) # Get prop list of given type

        # Pair prop names and values.
        # Ignores extra prop names if enough values are not passed in
        prop_dict = _combine_args_kwargs(element_props, props, kwprops)
        prop_list.append(prop_dict) # Python 3.5 unpacking syntax

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

    def add_constraint(self, *args, type, arg_list=[], **kwargs):
        """
        Adds constraint of the specified type

        Returns reference to self.constraint_aliases for chaining
        """
        constraint = _combine_args_kwargs(arg_list, args, kwargs)
        constraint['type'] = type
        self._constraints.append(constraint)
        return self.constraint_aliases

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

def _combine_args_kwargs(arg_list, args, kwargs):
    """
    arg_list: List of keys in order of positional arguments
    args: List of positional arguments
    kwargs: Dictionary of keyword arguments

    Returns a dictionary merging kwargs and args with keys from
    from args_list

    >>> _combine_args_kwargs(['foo','bar'],[1,2],{'baz':3})
    {'foo':1, 'bar':2, 'baz': 3}
    """
    arg_dict = {key: val for (key, val) in zip(arg_list, args)}
    return {**arg_dict, **kwargs} # Python 3.5 unpacking syntax
