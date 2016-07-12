"""
optimlib

Contains class/functions related to defining the optimal control problems
"""
import functools
import re

from beluga.continuation import ContinuationList
class Problem(object):
    """
    Defines an optimal control problem
    """
    def __init__(self,name):
        self.name = self._format_name(name)

        self.systems = {'default': {}} # Dynamic system definitions
        self.properties = {} # Problem properties
        self.steps = [] # Continuation sets

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

        # TODO: Maybe write as separte function?
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

        # Aliases for continuation
        self.steps = ContinuationList()

    def add_property(self, *args, property_name, arg_list=[], **kwargs ):
        """
        Adds a property of the optimal control problem

        >> add_property('cost',type='path',expr='')

        Returns a reference to self for chaining purposes
        """
        self.properties[property_name] = _combine_args_kwargs(arg_list,
                                                                   args, kwargs)
        return self

    def add_dynamic_element(self, *props, element_kind, element_props,
                                            system_name='default', **kwprops):
        """
        Adds an dynamic element of the problem to a specified dynamic system

        element_kind: Defines category of element state, control, constant etc.
        and a list of keyword arguments that form it's properties

        element_props: List of properties in order that they appear in *props


        Returns a reference to self for chaining purposes

        >>> add_element(self, 'states', element_props=['name','eom','unit'],
                                                                'default',...)
        """

        system = self.systems.get(system_name, {})
        prop_list = system.get(element_kind, []) # Get prop list of given type

        # Pair prop names and values.
        # Ignores extra prop names if enough values are not passed in
        prop_dict = _combine_args_kwargs(element_props, props, kwprops)
        prop_list.append(prop_dict) # Python 3.5 unpacking syntax

        system[element_kind] = prop_list
        self.systems[system_name] = system
        return self

    def __str__(self):
        return str({'name': self.name,
                    'systems': self.systems,
                    'properties': self.properties})

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
