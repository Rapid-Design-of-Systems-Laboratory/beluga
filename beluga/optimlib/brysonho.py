"""
Computes the necessary conditions of optimality using Bryson & Ho's method

[1] Bryson, Arthur Earl. Applied optimal control: optimization, estimation and control. CRC Press, 1975.
"""
# Make chain-rule differentiation a utility function
#
#   1. Process quantities
#   2. Process path constraints
#   3. Create hamiltonian and costates with rates
# **Create pure functions where possible**

import simplepipe as sp
import functools as ft
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


def make_augmented_cost(cost, constraints, location):
    """Augments the cost function with the given list of constraints.

    Returns the augmented cost function

    """
    filtered_list = constraints.get(location)
    # TODO: Add to parameter list in workspace
    # parameter_list += [c.make_multiplier(ind) for (ind,c) in enumerate(filtered_list,1)]
    #
    cost = cost + sum([c.make_aug_cost(ind) for (ind,c) in enumerate(filtered_list,1)])

    return cost

def make_hamiltonian_and_costates(states, path_cost):
    """simplepipe task for creating the hamiltonian and costates

    Workspace variables
    -------------------
    states - list of dict
        List of "sympified" states

    path_cost - Object representing the path cost terminal

    Returns the hamiltonian and the list of costates

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
    yield ham
    yield costates


# Implement workflow using simplepipe and functions defined above
BrysonHo = sp.Workflow([
            sp.Task(ft.partial(make_augmented_cost, location='initial'),
                    inputs=('initial_cost', 'constraints'),
                    outputs=('initial_cost')),
            sp.Task(ft.partial(make_augmented_cost, location='terminal'),
                    inputs=('terminal_cost', 'constraints'),
                    outputs=('terminal_cost')),
            sp.Task(make_hamiltonian_and_costates,
                    inputs=('states', 'path_cost'),
                    outputs=('ham', 'costates'))
        ])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
