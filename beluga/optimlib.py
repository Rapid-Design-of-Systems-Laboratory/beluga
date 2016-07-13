"""
Contains classes and functions related to Optimal Control.

Module: optimlib
"""
# Make chain-rule differentiation a utility function
#
#   1. Process quantities
#   2. Process path constraints
#   3. Create hamiltonian and costates with rates
# **Create pure functions where possible**
from beluga.utils import sympify2

def sympify_element(element, keys='all'):
    """
    Creates new element with symbolic variables in place of strings for the
    given keys

    Converts all keys if keys == 'all'

    >>> sorted(sympify_element({'name':'x', 'eom':'v*cos(theta)', 'unit':'m'},\
                        keys='all').items())
    [('eom': v*cos(theta)), ('name': x), ('unit': m)]

    >>> sorted(sympify_element({'name':'x', 'eom':'v*cos(theta)', 'unit':'m'},\
                        keys=['name', 'eom']).items())
    [('eom': v*cos(theta)), ('name': x), ('unit': 'm')]
    """
    if keys == 'all':
        keys = element.keys()
    new_element = {k: (sympify2(v) if k in keys and v is not '' else v)
                   for (k, v) in element.items()
                   }
    return new_element


def hamiltonian_and_costates(states, path_cost, constraints):
    """
    Creates the hamiltonian expression and costates

    states: Array of states
    path_cost: Object representing the path cost terminal
    constraints: Array of all constraints in the problem

    Returns a tuple with the hamiltonian and the list of costates

    >>> states = sympify_element([{'name':'x','eom':'v*cos(theta)'},
                                  {'name':'y','eom':'v*sin(theta)'}])
    >>> path_cost = {'expr': 1}
    >>> hamiltonian_and_costates(states, path_cost, [])
    (1 + lamX*v*cos(theta) + lamY*v*sin(theta), [{'name':'lamX','eom':''},
                                  {'name':'lamY','eom':''}])
    """
    costates = [sympify_element({'name': 'lam'+str(s.name).upper(), 'eom': ''})
                for s in states]
    ham = path_cost.expr + [lam.name*s.eom
                             for (s, lam) in zip(states, costates)]
    return (ham, costates)


def sigmoid_two_sided(x, ub, lb, slopeAtZero=1):
    """Two-sided saturation function based on the sigmoid function."""
    pass


def sigmoid_one_sided(x, ub=None, lb=None, slopeAtZero=1):
    """
    One-sided saturation function based on the sigmoid function.

    Only of the bounds must be defined.
    """
    pass


# def make_costate(state):
#     """Creates and returns costates corresponding to list of states.
#
#     >>> make_costates({'name':'x','eom':'v*cos(t)'})
#     {'name':'lamX'}
#     """
#     return dict(name='lam'+state['name'].upper())


class OCProblem(object):
    """Describes an optimal control problem."""
    pass
#  OCProblem
#     -> states (array from Problem object)
#     -> costates (similar array as states)
#     -> Hamiltonian

# Call doctest if the script is run directly
if __name__ == "__main__":
    import doctest
    doctest.testmod()
