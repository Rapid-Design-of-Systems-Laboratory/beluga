"""
Base functions required by all optimization methods.
"""


from beluga.utils import sympify
from beluga.problem import SymVar
import sympy
import functools as ft
import itertools as it
import re as _re


def init_workspace(ocp):
    """
    Initializes the simplepipe workspace using an OCP definition.

    All the strings in the original definition are converted into symbolic
    expressions for computation.

    :param ocp: An optimal control problem.
    :return:
    """

    workspace = {}
    # variable_list = ['states', 'controls', 'constraints', 'quantities', 'initial_cost', 'terminal_cost', 'path_cost']
    workspace['problem_name'] = ocp.name
    workspace['indep_var'] = SymVar(ocp._properties['independent'])
    workspace['states'] = [SymVar(s) for s in ocp.states()]
    workspace['controls'] = [SymVar(u) for u in ocp.controls()]
    workspace['constants'] = [SymVar(k) for k in ocp.constants()]

    constraints = ocp.constraints()
    workspace['constraints'] = {c_type: [SymVar(c_obj, sym_key='expr') for c_obj in c_list]
                                for c_type, c_list in constraints.items()
                                if c_type != 'path'}
    workspace['path_constraints'] = [SymVar(c_obj, sym_key='expr', excluded=('direction', 'start_eps'))
                                     for c_obj in constraints.get('path', [])]

    workspace['quantities'] = [SymVar(q) for q in ocp.quantities()]
    workspace['initial_cost'] = SymVar(ocp.get_cost('initial'), sym_key='expr')
    workspace['terminal_cost'] = SymVar(ocp.get_cost('terminal'), sym_key='expr')
    workspace['path_cost'] = SymVar(ocp.get_cost('path'), sym_key='expr')
    return workspace


def jacobian(expr_list, var_list, derivative_fn):
    """
    Defines the Jacobian matrix.

    :param expr_list: List of expressions to take the partials of.
    :param var_list: List of variables to take the partials with respect to.
    :param derivative_fn: Derivative function that evaluates
    :return: The Jacobian matrix.
    """

    jac = sympy.zeros(len(expr_list), len(var_list))
    for i, expr in enumerate(expr_list):
        for j, var in enumerate(var_list):
            jac[i, j] = derivative_fn(expr, var)
    return jac


def make_augmented_cost(cost, constraints, location):
    """
    Augments the cost function with the given list of constraints.

    :param cost: The original cost function.
    :param constraints: List of constraint to adjoin to the cost function.
    :param location: Location of each constraint.

    Returns the augmented cost function
    """

    # TODO: Replace the next 4 lines with make_aug_params???
    def make_lagrange_mult(c, ind = 1):
        return sympify('lagrange_' + location + '_' + str(ind))
    lagrange_mult = [make_lagrange_mult(c, ind)
                     for (ind,c) in enumerate(constraints[location],1)]

    aug_cost_expr = cost.expr + sum(nu * c
                                    for (nu, c) in
                                    zip(lagrange_mult, constraints[location]))

    aug_cost = SymVar({'expr':aug_cost_expr, 'unit': cost.unit}, sym_key='expr')
    return aug_cost


def make_augmented_params(constraints, location):
    """
    Make the lagrange multiplier terms for boundary conditions.

    :param constraints: List of constraints at the boundaries.
    :param location: Location of each constraint.
    :return: Lagrange multipliers for the given constraints.
    """

    def make_lagrange_mult(c, ind = 1):
        return sympify('lagrange_' + location + '_' + str(ind))
    lagrange_mult = [make_lagrange_mult(c, ind)
                     for (ind,c) in enumerate(constraints[location],1)]
    return lagrange_mult


def make_boundary_conditions(constraints, states, costates, cost, derivative_fn, location,
                             prefix_map=(('initial',(r'([\w\d\_]+)_0', r"_x0['\1']", sympify('-1'))),
                                         ('terminal',(r'([\w\d\_]+)_f', r"_xf['\1']", sympify('1'))))):
    """
    Creates boundary conditions for initial and terminal constraints.

    :param constraints: List of boundary constraints.
    :param states: List of state variables.
    :param costates: List of costate variables.
    :param cost: Cost function.
    :param derivative_fn: Total derivative function.
    :param location: Location of each boundary constraint.
    :param prefix_map: Prefix mapping.
    :return: List of boundary conditions.
    """
    prefix_map = dict(prefix_map)
    bc_list = [sanitize_constraint_expr(x, states, location, prefix_map) for x in constraints[location]]

    *_, sign = dict(prefix_map)[location]

    cost_expr = sign * cost

    #TODO: Fix hardcoded if conditions
    #TODO: Change to symbolic
    bc_list += [str(costate - derivative_fn(cost_expr, state)) for state, costate in zip(states, costates)]

    return bc_list


def make_costate_names(states):
    """
    Makes a list of variables representing each costate.

    :param states: List of state variables.
    :return: List of costate variables.
    """

    return [sympify('lam'+str(s.name).upper()) for s in states]


def make_costate_rates(ham, states, costate_names, derivative_fn):
    """
    Makes a list of rates of change for each of the costates.

    :param ham: Hamiltonian function.
    :param states: List of state variables.
    :param costate_names: List of costate variables.
    :param derivative_fn: Total derivative function.
    :return: Rates of change for each costate.
    """
    costates = [SymVar({'name': lam, 'eom':derivative_fn(-1*(ham), s)})
                for s, lam in zip(states, costate_names)]
    return costates


#TODO: Determine if make_dhdu() is ever even used. Like 2 of the functions show up as not imported.
def make_dhdu(ham, controls, derivative_fn):
    """
    Computes the partial of the hamiltonian w.r.t control variables.

    :param ham: Hamiltonian function.
    :param controls: A list of each control variable.
    :param derivative_fn: Total derivative function.
    :return: :math:`dH/du`
    """

    dhdu = []
    for ctrl in controls:
        dHdu = derivative_fn(ham, ctrl)
        custom_diff = dHdu.atoms(sympy.Derivative)
        # Substitute "Derivative" with complex step derivative
        repl = {(d, im(f.func(v+1j*1e-30))/1e-30) for d in custom_diff
                    for f,v in zip(d.atoms(sympy.AppliedUndef), d.atoms(Symbol))}

        dhdu.append(dHdu.subs(repl))

    return dhdu


def make_parameters(initial_lm_params, terminal_lm_params, s_list):
    """
    Makes parameters.

    :param initial_lm_params:
    :param terminal_lm_params:
    :param s_list:
    :return: List of parameters.
    """
    all_pi_names = [p['pi_list'] for p in s_list]
    params_list = [str(p) for p in it.chain(initial_lm_params,
                                            terminal_lm_params)] #, *all_pi_names)]
    parameters = sympy.symbols(' '.join(params_list))
    return parameters


def make_time_bc(constraints, bc_terminal):
    """
    Makes free or fixed final time boundary conditions.

    :param constraints: List of constraints.
    :param bc_terminal: Terminal boundary condition.
    :return: New terminal boundary condition.
    """
    time_constraints = constraints.get('independent', [])
    if len(time_constraints) > 0:
        return bc_terminal+['tf - 1']
    else:
        # Add free final time boundary condition
        return bc_terminal+['_H - 0']


def process_quantities(quantities):
    """
    Performs preprocessing on quantity definitions. Creates a new total
    derivative operator that takes considers these definitions.

    :param quantities: List of quantities.
    :return:
    """

    # TODO: Sanitize quantity expressions
    # TODO: Check for circular references in quantity expressions

    # Trivial case when no quantities are defined
    if len(quantities) == 0:
        yield {}
        yield []
        yield total_derivative
        yield ft.partial(jacobian, derivative_fn=total_derivative)

    quantity_subs = [(q.name, q.value) for q in quantities]
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
    jacobian_fn = ft.partial(jacobian, derivative_fn=derivative_fn)

    yield quantity_vars
    yield quantity_list
    yield derivative_fn
    yield jacobian_fn


def sanitize_constraint_expr(constraint, states, location, prefix_map):
    """
    Checks the initial/terminal constraint expression for invalid symbols
    Also updates the constraint expression to reflect what would be in code

    :param constraint: List of constraints.
    :param states: List of state variables.
    :param location: Location of the constraints.
    :param prefix_map: Prefix mapping.
    """

    if location not in prefix_map:
        raise ValueError('Invalid constraint type')

    pattern, prefix, _ = dict(prefix_map)[location]
    m = _re.findall(pattern,str(constraint.expr))
    invalid = [x for x in m if x not in states]

    if not all(x is None for x in invalid):
        raise ValueError('Invalid expression(s) in boundary constraint:\n'+str([x for x in invalid if x is not None]))

    return _re.sub(pattern,prefix,str(constraint.expr))


def total_derivative(expr, var, dependent_vars=None):
    """
    Take derivative taking pre-defined quantities into consideration

    :param expr: Expression to evaluate the derivative of.
    :param var: Variable to take the derivative with respect to.
    :param dependent_vars: Other dependent variables to consider with chain rule.
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
