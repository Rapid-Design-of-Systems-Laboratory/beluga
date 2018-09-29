"""
Base functions required by all optimization methods.
"""


from beluga.utils import sympify
import sympy
from sympy import Symbol, im
from sympy.core.function import AppliedUndef
import functools as ft
import itertools as it
import re as _re
from beluga.problem import SymVar


def init_workspace(ocp, guess):
    r"""
    Initializes the workspace using an OCP definition.

    All the strings in the original definition are converted into symbolic
    expressions for computation.

    :param ocp: An optimal control problem.
    :return:
    """

    workspace = {}
    workspace['problem_name'] = ocp.name
    workspace['indep_var'] = SymVar(ocp._properties['independent'])
    workspace['states'] = [SymVar(s) for s in ocp.states()]
    workspace['controls'] = [SymVar(u) for u in ocp.controls()]
    workspace['constants'] = [SymVar(k) for k in ocp.constants()]
    workspace['constants_of_motion'] = [SymVar(k) for k in ocp.constants_of_motion()]

    constraints = ocp.constraints()
    workspace['constraints'] = {c_type: [SymVar(c_obj, sym_key='expr') for c_obj in c_list]
                                for c_type, c_list in constraints.items()
                                if c_type != 'path'}

    workspace['constraints_adjoined'] = ocp.constraints().adjoined

    workspace['path_constraints'] = [SymVar(c_obj, sym_key='expr', excluded=('direction', 'start_eps'))
                                     for c_obj in constraints.get('path', [])]

    workspace['quantities'] = [SymVar(q) for q in ocp.quantities()]
    workspace['initial_cost'] = SymVar(ocp.get_cost('initial'), sym_key='expr')
    workspace['terminal_cost'] = SymVar(ocp.get_cost('terminal'), sym_key='expr')
    workspace['path_cost'] = SymVar(ocp.get_cost('path'), sym_key='expr')
    guess.dae_num_states = 0
    return workspace


def make_augmented_cost(cost, constraints, constraints_adjoined, location):
    r"""
    Augments the cost function with the given list of constraints.

    .. math::
        \begin{aligned}
            \text{make_augmented_cost} : C^\infty(M) &\rightarrow C^\infty(M) \\
            (f, g) &\mapsto f + g_i \nu_i \; \forall \; i \in g
        \end{aligned}

    :param cost: The cost function, :math:`f`.
    :param constraints: List of constraint to adjoin to the cost function, :math:`g`.
    :param constraints_adjoined: Boolean value on whether or not the adjoined method is used. Skips if `False`.
    :param location: Location of each constraint.

    Returns the augmented cost function
    """

    if not constraints_adjoined:
        return cost

    lagrange_mult = make_augmented_params(constraints, constraints_adjoined, location)
    aug_cost_expr = cost.expr + sum(nu * c for (nu, c) in zip(lagrange_mult, constraints[location]))

    aug_cost = SymVar({'expr':aug_cost_expr, 'unit': cost.unit}, sym_key='expr')
    return aug_cost


def make_augmented_params(constraints, constraints_adjoined, location):
    r"""
    Make the lagrange multiplier terms for adjoining boundary conditions.

    :param constraints: List of constraints at the boundaries.
    :param constraints_adjoined: Boolean value on whether or not the adjoined method is used.
    :param location: Location of each constraint.
    :return: Lagrange multipliers for the given constraints.
    """
    if not constraints_adjoined:
        return []

    def make_lagrange_mult(c, ind = 1):
        return sympify('lagrange_' + location + '_' + str(ind))

    lagrange_mult = [make_lagrange_mult(c, ind) for (ind,c) in enumerate(constraints[location], 1)]

    return lagrange_mult


def make_boundary_conditions(constraints, constraints_adjoined, states, costates, cost, derivative_fn, location,
                             prefix_map=(('initial',(r'([\w\d\_]+)_0', r"_x0['\1']", sympify('-1'))),
                                         ('terminal',(r'([\w\d\_]+)_f', r"_xf['\1']", sympify('1'))))):
    """
    Creates boundary conditions for initial and terminal constraints.

    :param constraints: List of boundary constraints.
    :param constraints_adjoined: Boolean value on whether or not constraints are adjoined with Lagrange multipliers.
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

    if constraints_adjoined:
        bc_list += [str(costate - derivative_fn(cost_expr, state)) for state, costate in zip(states, costates)]
    else:
        refd = [sum(derivative_fn(c, s) for c in constraints[location]) for s in states]
        bc_list += [str(costate - derivative_fn(cost_expr, state)) for i, (state, costate) in enumerate(zip(states,costates)) if refd[i] == False]

    return bc_list


def make_constrained_arc_fns(states, costates, controls, parameters, constants, quantity_vars, hamiltonian):
    """
    Creates constrained arc control functions.

    :param workspace:
    :return:
    """
    tf_var = sympify('tf')
    costate_eoms = [ {'eom':[str(_.eom*tf_var) for _ in costates], 'arctype':0} ]
    bc_list = []  # Unconstrained arc placeholder

    return costate_eoms, bc_list


def make_costate_names(states):
    r"""
    Makes a list of variables representing each costate.

    :param states: List of state variables, :math:`x`.
    :return: List of costate variables, :math:`\lambda_x`.
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

    costates = [SymVar({'name': lam, 'eom':derivative_fn(-1*(ham), s)}) for s, lam in zip(states, costate_names)]
    return costates


#TODO: Determine if make_dhdu() is ever even used. Like 2 of the functions show up as not imported.
def make_dhdu(ham, controls, derivative_fn):
    r"""
    Computes the partial of the hamiltonian w.r.t control variables.

    :param ham: Hamiltonian function.
    :param controls: A list of each control variable.
    :param derivative_fn: Total derivative function.
    :return: :math:`dH/du`
    """

    dHdu = []
    for ctrl in controls:
        dHdu.append(derivative_fn(ham, ctrl))

    return dHdu


def make_ham_lamdot(states, path_cost, derivative_fn):
    r"""
    Creates a Hamiltonian function and costate rates.

    :param states: A list of state variables, :math:`x`.
    :param constraints: A set of constraints.
    :param path_cost: The path cost to be minimized.
    :param derivative_fn: The derivative function.
    :return: A Hamiltonian function, :math:`H`.
    :return: A list of costate rates, :math:`\dot{\lambda}_x`
    """
    costate_names = make_costate_names(states)
    ham = path_cost.expr + sum([lam*s.eom for s, lam in zip(states, costate_names)])
    yield ham
    yield make_costate_rates(ham, states, costate_names, derivative_fn)


def make_parameters(initial_lm_params, terminal_lm_params):
    """
    Makes parameters.

    :param initial_lm_params:
    :param terminal_lm_params:
    :param s_list:
    :return: List of parameters.
    """
    params_list = [str(p) for p in it.chain(initial_lm_params,
                                            terminal_lm_params)] #, *all_pi_names)]
    if len(params_list) > 0:
        parameters = [sympy.symbols(p) for p in params_list]
    else:
        parameters = []

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
    :return: quantity_vars, quantity_list, derivative_fn, jacobian_fn
    """

    # Trivial case when no quantities are defined
    if len(quantities) == 0:
        return dict(), list(), total_derivative

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
    return quantity_vars, quantity_list, derivative_fn


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
    m = _re.findall(pattern, str(constraint.expr))
    invalid = [x for x in m if x not in states]

    if not all(x is None for x in invalid):
        raise ValueError('Invalid expression(s) in boundary constraint:\n'+str([x for x in invalid if x is not None]))

    return _re.sub(pattern, prefix, str(constraint.expr))


def total_derivative(expr, var, dependent_vars=None):
    """
    Take derivative taking pre-defined quantities into consideration

    :param expr: Expression to evaluate the derivative of.
    :param var: Variable to take the derivative with respect to.
    :param dependent_vars: Other dependent variables to consider with chain rule.
    """

    complex_step = False
    if dependent_vars is None:
        dependent_vars = {}

    dep_var_names = dependent_vars.keys()
    dep_var_expr = [(expr) for (_,expr) in dependent_vars.items()]

    dFdq = [sympy.diff(expr, dep_var).subs(dependent_vars.items()) for dep_var in dep_var_names]
    dqdx = [sympy.diff(qexpr, var) for qexpr in dep_var_expr]
    out = sum(d1 * d2 for d1, d2 in zip(dFdq, dqdx)) + sympy.diff(expr, var)
    custom_diff = out.atoms(sympy.Derivative)
    # Substitute "Derivative" with complex step derivative
    if complex_step == True:
        repl = {(d, im(f.subs(v, v + 1j * 1e-30)) / 1e-30) for d in custom_diff
                for f, v in zip(d.atoms(AppliedUndef), d.atoms(Symbol))}
    else:
        repl = {(d, (f.subs(v, v + 1 * 1e-4) - f) / (1e-4)) for d in custom_diff
                for f, v in zip(d.atoms(AppliedUndef), d.atoms(Symbol))}
    out = out.subs(repl)
    p = out.atoms(sympy.Subs)
    q = [_ for _ in p]
    for term in q:
        rep = zip([term], [term.doit()])
        out = out.subs(rep)

    return out
