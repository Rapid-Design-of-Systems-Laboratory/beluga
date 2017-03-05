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

import functools as ft
import re as _re
import simplepipe as sp
import sympy

from beluga.utils import sympify2
from beluga.problem2 import SymbolicVariable

# def sympify_element(element, keys='all'):
#     """
#     Creates new element with symbolic variables in place of strings for the
#     given keys
#
#     Converts all keys if keys == 'all'
#
#     >>> sorted(sympify_element({'name':'x', 'eom':'v*cos(theta)', 'unit':'m'},\
#                         keys='all').items())
#     [('eom': v*cos(theta)), ('name': x), ('unit': m)]
#
#     >>> sorted(sympify_element({'name':'x', 'eom':'v*cos(theta)', 'unit':'m'},\
#                         keys=['name', 'eom']).items())
#     [('eom': v*cos(theta)), ('name': x), ('unit': 'm')]
#     """
#     if keys == 'all':
#         keys = element.keys()
#     new_element = {k: (sympify2(v) if k in keys and v is not '' else v)
#                    for (k, v) in element.items()
#                    }
#     return new_element

def total_derivative(expr, var, dependent_vars=None):
    """
    Take derivative taking pre-defined quantities into consideration

    dependent_variables: Dictionary containing dependent variables as keys and
                         their expressions as values
    """
    if dependent_vars is None:
        dependent_vars = {}

    dep_var_names = dependent_vars.keys()
    dep_var_expr = [(expr) for (_,expr) in dependent_vars.items()]

    dFdq = [sympy.diff(expr, dep_var).subs(dependent_vars.items()) for dep_var in dep_var_names]
    dqdx = [sympy.diff(qexpr, var) for qexpr in dep_var_expr]

    # Chain rule + total derivative
    out = sum(d1*d2 for d1,d2 in zip(dFdq, dqdx)) + sympy.diff(expr, var)
    return out

def process_quantities(quantities):
    # logging.info('Processing quantity expressions')

    # TODO: Sanitize quantity expressions
    # TODO: Check for circular references in quantity expressions

    quantity_subs = [(q.name, q.val) for q in quantities]
    quantity_sym, quantity_expr = zip(*quantity_subs)
    quantity_expr = [qty_expr.subs(quantity_subs) for qty_expr in quantity_expr]

    # Use substituted expressions to recreate quantity expressions
    quantity_subs = [(str(qty_var),qty_expr) for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]
    # Dictionary for substitution
    quantity_vars = dict(quantity_subs)

    # Dictionary for use with mustache templating library
    quantity_list = [{'name':str(qty_var), 'expr':str(qty_expr)} for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]

    # Function partial that takes derivative while considering quantities
    derivative_fn = ft.partial(total_derivative, dependent_vars=quantity_vars)

    yield quantity_vars
    yield quantity_list
    yield derivative_fn

def make_augmented_cost(cost, constraints, location):
    """Augments the cost function with the given list of constraints.

    Returns the augmented cost function
    """

    filtered_list = constraints.get(location)
    # TODO: Add to parameter list in workspace
    # parameter_list += [c.make_multiplier(ind) for (ind,c) in enumerate(filtered_list,1)]
    #
    def augment_constraint(c, ind = 1):
        return sympify2('lagrange_' + c.type + '_' + str(ind) + '*(' + str(c.expr) + ')')

    aug_cost = cost.expr + sum(augment_constraint(c, ind) for (ind,c) in enumerate(filtered_list,1))

    return SymbolicVariable({'expr':aug_cost, 'unit': cost.unit}, sym_key='expr')

def make_hamiltonian_and_costates(states, path_cost):
    """simplepipe task for creating the hamiltonian and costates

    Workspace variables
    -------------------
    states - list of dict
        List of "sympified" states

    path_cost - Object representing the path cost terminal

    Returns the hamiltonian and the list of costates
    """
    costates = [SymbolicVariable({'name': 'lam'+str(s.name).upper()})
                for s in states]

    ham = path_cost.expr + sum([lam.name*s.eom
                             for (s, lam) in zip(states, costates)])

    yield ham
    yield costates


def sanitize_constraint_expr(constraint,states):
    """
    Checks the initial/terminal constraint expression for invalid symbols
    Also updates the constraint expression to reflect what would be in code
    """
    if constraint.type == 'initial':
        pattern = r'([\w\d\_]+)_0'
        prefix = '_x0'
    elif constraint.type == 'terminal':
        pattern = r'([\w\d\_]+)_f'
        prefix = '_xf'
    else:
        raise ValueError('Invalid constraint type')

    m = _re.findall(pattern,str(constraint.expr))
    invalid = [x for x in m if x not in states]

    if not all(x is None for x in invalid):
        raise ValueError('Invalid expression(s) in boundary constraint:\n'+str([x for x in invalid if x is not None]))

    return _re.sub(pattern,prefix+r"['\1']",str(constraint.expr))


def make_boundary_conditions(constraints, states, costates, cost, derivative_fn, location):
    """simplepipe task for creating boundary conditions for initial and terminal
    constraints."""

    bc_list = [sanitize_constraint_expr(x, states)
                    for x in constraints.get(location)]
    # bc_terminal = [sanitize_constraint_expr(x, states)
    #                 for x in constraints.get('terminal')]

    if location == 'initial':
        sign = sympify2('-1')
    elif location == 'terminal':
        sign = sympify2('1')

    cost_expr = sign * cost

    #TODO: Fix hardcoded if conditions
    #TODO: Change to symbolic
    bc_list += [str(costate - derivative_fn(cost_expr, state))
                        for state, costate in zip(states, costates)]

    return bc_list

def make_costate_rates(ham, states, costates, derivative_fn):
    """Computes costate rates."""
    return [SymbolicVariable(dict(name=costate.name, eom=derivative_fn(-1*(ham),state)))
            for state, costate in zip(states, costates)]


def init_workspace(ocp):
    """Initializes the simplepipe workspace using an OCP definition."""

# Implement workflow using simplepipe and functions defined above
BrysonHo = sp.Workflow([
            sp.Task(process_quantities,
                    inputs=('quantities'),
                    outputs=('quantity_vars', 'quantity_list', 'derivative_fn')),
            sp.Task(ft.partial(make_augmented_cost, location='initial'),
                    inputs=('initial_cost', 'constraints'),
                    outputs=('initial_cost')),
            sp.Task(ft.partial(make_augmented_cost, location='terminal'),
                    inputs=('terminal_cost', 'constraints'),
                    outputs=('terminal_cost')),
            sp.Task(make_hamiltonian_and_costates,
                    inputs=('states', 'path_cost'),
                    outputs=('ham', 'costates')),
            sp.Task(ft.partial(make_boundary_conditions, location='initial'),
                    inputs=('constraints', 'states', 'costates', 'derivative_fn'),
                    outputs=('bc_initial')),
            sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
                    inputs=('constraints', 'states', 'costates', 'derivative_fn'),
                    outputs=('bc_terminal')),
            sp.Task(make_costate_rates,
                    inputs=('ham', 'states', 'costates', 'derivative_fn'),
                    outputs=('costates')
                    )
  ], description='Tradition optimal control workflow')

## Unit tests ##################################################################
from beluga.problem2 import ConstraintList
from beluga.problem2 import SymbolicVariable

def test_process_quantities():
    quantities = [SymbolicVariable(dict(name='rho', val='rho0*exp(-h/H)')),
                  SymbolicVariable(dict(name='D', val='0.5*rho*v^2*Cd*Aref'))]
    qvars, qlist, _ = process_quantities(quantities)

    qvars_expected = dict(rho= sympify2('rho0*exp(-h/H)'),
                          D= sympify2('0.5*Aref*Cd*rho0*v**2*exp(-h/H)'))
    qlist_expected = [{'expr': 'rho0*exp(-h/H)', 'name': 'rho'},
                      {'expr': '0.5*Aref*Cd*rho0*v**2*exp(-h/H)', 'name': 'D'}]

    assert qvars == qvars_expected
    assert qlist == qlist_expected

def test_ham_and_costates():
    states = [SymbolicVariable({'name':'x','eom':'v*cos(theta)','unit':'m'}),
              SymbolicVariable({'name':'y','eom':'v*sin(theta)','unit':'rad'})]
    path_cost = SymbolicVariable({'expr': 1}, sym_key='expr')

    expected_output = (sympify2('1 + lamX*v*cos(theta) + lamY*v*sin(theta)'),
                       [SymbolicVariable({'name':'lamX'}),
                       SymbolicVariable({'name':'lamY'})])

    ham, costates = make_hamiltonian_and_costates(states, path_cost)

    assert ham == expected_output[0]
    assert costates == expected_output[1]

def test_augmented_cost():
    constraints = ConstraintList()
    constraints.initial('h - h_0', 'm') # doctest:+ELLIPSIS
    constraints.terminal('h - h_f', 'm')
    terminal_cost = SymbolicVariable({'expr': '-v^2', 'unit': 'm^2/s^2'}, sym_key='expr')

    expected_output = SymbolicVariable({'expr': 'lagrange_terminal_1*(h - h_f) - v**2',
                       'unit': 'm**2/s**2'}, sym_key='expr')
    assert make_augmented_cost(terminal_cost, constraints, 'terminal') == expected_output

def test_make_boundary_conditions():
    states = [SymbolicVariable({'name':'h','eom':'v*cos(theta)','unit':'m'}),
              SymbolicVariable({'name':'theta','eom':'v*sin(theta)/r','unit':'rad'})]
    path_cost = SymbolicVariable({'expr': 1}, sym_key='expr')
    ham, costates = make_hamiltonian_and_costates(states, path_cost)

    constraints = ConstraintList()
    constraints.initial('h - h_0', 'm') # doctest:+ELLIPSIS
    constraints.terminal('theta - theta_f', 'rad') # doctest:+ELLIPSIS

    initial_cost = sympify2('0')
    bc_initial = make_boundary_conditions(constraints, states, costates, initial_cost, total_derivative, 'initial')
    assert bc_initial == ["h - _x0['h']", 'lamH', 'lamTHETA']

    terminal_cost = sympify2('-theta^2')
    bc_terminal = make_boundary_conditions(constraints, states, costates, terminal_cost, total_derivative, 'terminal')
    assert bc_terminal == ["theta - _xf['theta']", 'lamH', 'lamTHETA + 2*theta']

def test_make_costate_rates():
    states = [SymbolicVariable({'name':'h','eom':'v*cos(theta)','unit':'m'}),
              SymbolicVariable({'name':'theta','eom':'v*sin(theta)/r','unit':'rad'})]
    path_cost = SymbolicVariable({'expr': 1}, sym_key='expr')
    ham, costates = make_hamiltonian_and_costates(states, path_cost)
    costates_1 = make_costate_rates(ham, states, costates, total_derivative)
    costates_expected = [SymbolicVariable({'name':'lamH', 'eom':'0'}),
                         SymbolicVariable({'name':'lamTHETA', 'eom':'lamH*v*sin(theta) - lamTHETA*v*cos(theta)/r'})]
    assert costates_1 == costates_expected
