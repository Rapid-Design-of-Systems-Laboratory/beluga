"""
optimlib

Contains class/functions related to defining the optimal control problems
"""
import functools
class Problem(object):
    """
    Defines an optimal control problem
    """
    def __init__(self,name):
        self.name = self._format_name(name)

        # Dynamic system definitions dictionary
        #  with a default definition
        self.systems = {'default': {}}

        # Partial functions that add known types of elements
        self.state = functools.partial(self.add_element, element_kind='states')
        self.control = functools.partial(self.add_element, element_kind='controls')
        self.constant = functools.partial(self.add_element, element_kind='constants')
        self.quantity = functools.partial(self.add_element, element_kind='quantities')

    def add_element(self, element_kind, system_name='default', **properties):
        """
        Adds an element of the problem to a specified dynamic system

        element_kind: Defines category of element state, control, constant etc. and
        a list of keyword arguments that form it's properties

        Returns a reference to self for chaining purposes
        """
        system = self.systems.get(system_name, {})
        prop_list = system.get(prop_type, []) # Get prop list of given type
        prop_list.append(content)
        system[element_kind] = prop_list
        self.systems[system_name] = system
        return self

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
