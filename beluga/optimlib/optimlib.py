"""
Base functions shared by all optimization methods.
"""


from beluga.utils import sympify
import sympy
from sympy import Symbol, zoo
import functools as ft
import re


def init_workspace(ocp):
    r"""
    Initializes the symbolic workspace using an OCP definition.

    All the strings in the original definition are converted into symbolic
    expressions for computation.

    :param ocp: An optimal control problem.
    :return:
    """

    workspace = dict()
    workspace['problem_name'] = ocp.name
    workspace['independent_var'] = Symbol(ocp._properties['independent']['name'])
    workspace['independent_var_units'] = sympify(ocp._properties['independent']['unit'])
    workspace['states'] = [Symbol(s['name']) for s in ocp.states()]
    workspace['states_rates'] = [sympify(s['eom']) for s in ocp.states()]
    workspace['states_units'] = [sympify(s['unit']) for s in ocp.states()]
    workspace['controls'] = [Symbol(u['name']) for u in ocp.controls()]
    workspace['controls_units'] = [sympify(u['unit']) for u in ocp.controls()]
    workspace['constants'] = [Symbol(k['name']) for k in ocp.constants()]
    workspace['constants_values'] = [k['value'] for k in ocp.constants()]
    workspace['constants_units'] = [sympify(k['unit']) for k in ocp.constants()]
    workspace['constants_of_motion'] = [Symbol(k['name']) for k in ocp.constants_of_motion()]
    workspace['constants_of_motion_values'] = [sympify(k['function']) for k in ocp.constants_of_motion()]
    workspace['constants_of_motion_units'] = [sympify(k['unit']) for k in ocp.constants_of_motion()]
    workspace['symmetries'] = [sympify(k['function']) for k in ocp.symmetries()]
    workspace['parameters'] = [sympify(k['name']) for k in ocp.parameters()]
    workspace['parameters_units'] = [sympify(k['unit']) for k in ocp.parameters()]

    constraints = ocp.constraints()
    workspace['constraints'] = {c_type: [sympify(c_obj['expr']) for c_obj in c_list]
                                for c_type, c_list in constraints.items()}

    workspace['constraints_units'] = {c_type: [sympify(c_obj['unit']) for c_obj in c_list]
                                      for c_type, c_list in constraints.items()}

    workspace['constraints_lower'] = {c_type: [sympify(c_obj['lower']) for c_obj in c_list]
                                      for c_type, c_list in constraints.items() if c_type == 'path'}

    workspace['constraints_upper'] = {c_type: [sympify(c_obj['upper']) for c_obj in c_list]
                                      for c_type, c_list in constraints.items() if c_type == 'path'}

    workspace['constraints_activators'] = {c_type: [sympify(c_obj['activator']) for c_obj in c_list]
                                           for c_type, c_list in constraints.items() if c_type == 'path'}

    workspace['constraints_method'] = {c_type: [c_obj['method'] for c_obj in c_list]
                                           for c_type, c_list in constraints.items() if c_type == 'path'}

    if 'initial' not in workspace['constraints'].keys():
        workspace['constraints']['initial'] = []
        workspace['constraints_units']['initial'] = []

    if 'terminal' not in workspace['constraints'].keys():
        workspace['constraints']['terminal'] = []
        workspace['constraints_units']['terminal'] = []

    if 'path' not in workspace['constraints'].keys():
        workspace['constraints']['path'] = []
        workspace['constraints_units']['path'] = []
        workspace['constraints_lower']['path'] = []
        workspace['constraints_upper']['path'] = []

    workspace['path_constraints'] = [sympify(c_obj['expr']) for c_obj in constraints.get('path', [])]
    workspace['switches'] = []
    workspace['switches_values'] = []
    workspace['switches_conditions'] = []
    workspace['switches_tolerance'] = []
    for q in ocp.switches():
        workspace['switches'] += [sympify(q['name'])]
        if isinstance(q['value'], list):
            workspace['switches_values'] += [[sympify(v) for v in q['value']]]
            main_condition = []
            for cond in q['conditions']:
                if not isinstance(cond, list):
                    raise ValueError('Conditions for switches must be a list of lists')
                main_condition += [[sympify(v) for v in cond]]
            workspace['switches_conditions'] += [main_condition]
            workspace['switches_tolerance'] += [sympify(q['tolerance'])]
        else:
            workspace['switches_values'] += [sympify(q['value'])]
            workspace['switches_conditions'] += [None]
            workspace['switches_tolerance'] += [None]

    workspace['initial_cost'] = sympify(ocp.get_cost('initial')['expr'])
    workspace['initial_cost_units'] = sympify(ocp.get_cost('initial')['unit'])
    workspace['terminal_cost'] = sympify(ocp.get_cost('terminal')['expr'])
    workspace['terminal_cost_units'] = sympify(ocp.get_cost('terminal')['unit'])
    workspace['path_cost'] = sympify(ocp.get_cost('path')['expr'])
    workspace['path_cost_units'] = sympify(ocp.get_cost('path')['unit'])
    return workspace


def make_augmented_cost(cost, cost_units, constraints, constraints_units, location):
    r"""
    Augments the cost function with the given list of constraints.

    .. math::
        \begin{aligned}
            \text{make_augmented_cost} : C^\infty(M) &\rightarrow C^\infty(M) \\
            (f, g) &\mapsto f + g_i \nu_i \; \forall \; i \in g
        \end{aligned}

    :param cost: The cost function, :math:`f`.
    :param cost_units: The units of the cost function,
    :param constraints: List of constraints to adjoin to the cost function, :math:`g`.
    :param constraints_units: The units of the constraints,
    :param location: Location of each constraint.

    Returns the augmented cost function
    """

    lagrange_mult, lagrange_mult_units = make_augmented_params(constraints, constraints_units, cost_units, location)
    aug_cost_expr = cost + sum(nu * c for (nu, c) in zip(lagrange_mult, constraints[location]))
    return aug_cost_expr, cost_units, lagrange_mult, lagrange_mult_units


def make_augmented_params(constraints, constraints_units, cost_units, location):
    r"""
    Make the lagrange multiplier terms for adjoining boundary conditions.

    :param constraints: List of constraints at the boundaries.
    :param constraints_units: Units of the constraints.
    :param cost_units: Units of the cost function.
    :param location: Location of each constraint.
    :return: Lagrange multipliers for the given constraints.
    """

    def make_lagrange_mult(c, ind=1):
        return sympify('lagrange_' + location + '_' + str(ind))

    lagrange_mult = [make_lagrange_mult(c, ind) for (ind, c) in enumerate(constraints[location], 1)]
    lagrange_mult_cost = [cost_units/c_units for c_units in constraints_units[location]]
    return lagrange_mult, lagrange_mult_cost


def make_boundary_conditions(constraints, states, costates, parameters, coparameters, cost, derivative_fn, location):
    """
    Creates boundary conditions for initial and terminal constraints.

    :param constraints: List of boundary constraints.
    :param states: List of state variables.
    :param costates: List of costate variables.
    :param parameters: List of parameter variables.
    :param coparameters: List of coparameter variables.
    :param cost: Cost function.
    :param derivative_fn: Total derivative function.
    :param location: Location of each boundary constraint.
    :return: List of boundary conditions.
    """
    prefix_map = (('initial', (r'([\w\d\_]+)_0', r"_x0['\1']", sympify('-1'))),
                  ('terminal', (r'([\w\d\_]+)_f', r"_xf['\1']", sympify('1'))))
    prefix_map = dict(prefix_map)
    bc_list = []
    for x in constraints[location]:
        bc = sanitize_constraint_expr(x, states, location, prefix_map)
        bc_list.append(bc)

    *_, sign = dict(prefix_map)[location]
    cost_expr = sign * cost
    bc_list += [costate - derivative_fn(cost_expr, state) for state, costate in zip(states, costates)]
    bc_list += [coparameter - derivative_fn(cost_expr, parameter)
                for parameter, coparameter in zip(parameters, coparameters)]

    return bc_list


def make_constrained_arc_fns(states, costates, costates_rates, controls, parameters, constants, quantity_vars,
                             hamiltonian):
    """
    Creates constrained arc control functions. Deprecated.

    :param states:
    :param costates:
    :param costates_rates:
    :param controls:
    :param parameters:
    :param constants:
    :param quantity_vars:
    :param hamiltonian:
    :return:
    """

    raise NotImplementedError
    # tf_var = sympify('tf')
    # costate_eoms = [{'eom':[str(rate*tf_var) for rate in costates_rates], 'arctype':0}]
    # bc_list = []  # Unconstrained arc placeholder

    # return costate_eoms, bc_list


def make_control_dae(states, costates, states_rates, costates_rates, controls, dhdu, derivative_fn):
    """
    Make's control law for dae (ICRM) formulation.

    :param states:
    :param costates:
    :param states_rates:
    :param costates_rates:
    :param controls:
    :param dhdu:
    :param derivative_fn:
    :return:
    """

    g = dhdu
    X = [state for state in states] + [costate for costate in costates]
    U = [c for c in controls]
    xdot = sympy.Matrix([sympify(state) for state in states_rates] + [sympify(lam) for lam in costates_rates])
    # Compute Jacobian
    dgdX = sympy.Matrix([[derivative_fn(g_i, x_i) for x_i in X] for g_i in g])
    dgdU = sympy.Matrix([[derivative_fn(g_i, u_i) for u_i in U] for g_i in g])

    udot = dgdU.LUsolve(-dgdX*xdot)  # dgdU * udot + dgdX * xdot = 0
    if zoo in udot.atoms():
        raise NotImplementedError('Complex infinity in ICRM control law. Potential bang-bang solution.')

    dae_states = U
    dae_equations = list(udot)
    dae_bc = g

    yield dae_states
    yield dae_equations
    yield dae_bc
    yield dgdX
    yield dgdU


def make_costate_names(states):
    r"""
    Makes a list of variables representing each costate.

    :param states: List of state variables, :math:`x`.
    :return: List of costate variables, :math:`\lambda_x`.
    """

    return [sympify('lam'+str(s.name).upper()) for s in states]


def make_costate_rates(hamiltonian, states, costates, derivative_fn):
    """
    Makes a list of rates of change for each of the costates.

    :param hamiltonian: Hamiltonian function.
    :param states: List of state variables.
    :param costates: List of costate variables.
    :param derivative_fn: Total derivative function.
    :return: Rates of change for each costate.
    """
    costates_rates = [derivative_fn(-1*hamiltonian, s) for s in states]
    return costates_rates


# TODO: Determine if make_dhdu() is ever even used. Like 2 of the functions show up as not imported.
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


def make_hamiltonian(states, states_rates, states_units, path_cost, path_cost_units):
    r"""
    Creates a Hamiltonian function.

    :param states: A list of state variables, :math:`x`.
    :param states_rates: A list of rates of change for the state variables :math:`\dot{x} = f'.
    :param states_units: A list of units for each state variable.
    :param path_cost: The path cost to be minimized.
    :param path_cost_units: The units on the path cost.
    :return: A Hamiltonian function, :math:`H`.
    :return: A list of costate rates, :math:`\dot{\lambda}_x`
    :return: A list of units for each costate variable.
    """
    costates = make_costate_names(states)
    costates_units = [path_cost_units / state_units for state_units in states_units]
    hamiltonian = path_cost + sum([rate*lam for rate, lam in zip(states_rates, costates)])
    hamiltonian_units = path_cost_units

    return hamiltonian, hamiltonian_units, costates, costates_units


def make_time_bc(constraints, derivative_fn, hamiltonian, independent_var):
    """
    Makes free or fixed final time boundary conditions.

    :param constraints: List of constraints.
    :param derivative_fn: Derivative function
    :param hamiltonian: A Hamiltonian function.
    :param independent_var: Independent variable
    :return: New terminal boundary condition.
    """
    hamiltonian_free_final_time = all([derivative_fn(c, independent_var) == 0 for c in constraints['terminal']])
    if hamiltonian_free_final_time:
        return hamiltonian
    else:
        return None


def process_quantities(quantities, quantities_values):
    """
    Performs preprocessing on quantity definitions. Creates a new total
    derivative operator that takes considers these definitions.

    :param quantities: List of quantities.
    :param quantities_values: List of quantity values.

    :return: quantity_vars, quantity_list, derivative_fn, jacobian_fn
    """

    # Trivial case when no quantities are defined
    if len(quantities) == 0:
        return dict(), list(), total_derivative

    quantity_subs = [(q, q_val) for q, q_val in zip(quantities, quantities_values)]
    quantity_sym, quantity_expr = zip(*quantity_subs)
    quantity_expr = [qty_expr.subs(quantity_subs) for qty_expr in quantity_expr]

    # Use substituted expressions to recreate quantity expressions
    quantity_subs = [(str(qty_var), qty_expr) for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]
    # Dictionary for substitution
    quantity_vars = dict(quantity_subs)

    # Dictionary for use with mustache templating library
    quantity_list = [{'name': str(qty_var), 'expr': str(qty_expr)}
                     for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]

    # Function partial that takes derivative while considering quantities
    derivative_fn = ft.partial(total_derivative, dependent_vars=quantity_vars)
    return quantity_vars, quantity_list, derivative_fn


def sanitize_constraint_expr(constraint, states, location, prefix_map):
    """
    Checks the initial/terminal constraint expression for invalid symbols.

    Returns symbols representing constants in the expressions.

    :param constraint: List of constraints.
    :param states: List of state variables.
    :param location: Location of the constraints.
    :param prefix_map: Prefix mapping.
    """

    if location not in prefix_map:
        raise ValueError('Invalid constraint type')

    pattern, prefix, _ = dict(prefix_map)[location]
    m = re.findall(pattern, str(constraint))
    invalid = [x for x in m if x not in [str(s) for s in states]]
    if not all(x is None for x in invalid):
        raise ValueError('Invalid expression(s) in boundary constraint:\n' + str([x for x in invalid if x is not None]))

    return constraint


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
    dep_var_expr = [expr for (_, expr) in dependent_vars.items()]

    dFdq = [sympy.diff(expr, dep_var).subs(dependent_vars.items()) for dep_var in dep_var_names]
    dqdx = [sympy.diff(qexpr, var) for qexpr in dep_var_expr]
    out = sum(d1 * d2 for d1, d2 in zip(dFdq, dqdx)) + sympy.diff(expr, var)
    return out


def epstrig_path(constraint, lower, upper, activator):
    r"""
    Creates an interior penalty-type term to enforce path constraints.

    :param constraint: The path constraint.
    :param lower: Lower bounds on the path constraint.
    :param upper: Upper bounds on the path constraint.
    :param activator: Activation term used in the path constraint.
    :return: Term to augment a Hamiltonian with.
    """
    if lower is None or upper is None:
        raise NotImplementedError('Lower and upper bounds on epsilon-trig-style path constraints MUST be defined.')
    return -activator*(sympy.cos(constraint))


def utm_path(constraint, lower, upper, activator):
    r"""
    Creates an interior penalty-type term to enforce path constraints.

    :param constraint: The path constraint.
    :param lower: Lower bounds on the path constraint.
    :param upper: Upper bounds on the path constraint.
    :param activator: Activation term used in the path constraint.
    :return: Term to augment a Hamiltonian with.
    """
    if lower is None or upper is None:
        raise NotImplementedError('Lower and upper bounds on UTM-style path constraints MUST be defined.')
    return activator*(1/(sympy.cos(sympy.pi/2*(2*constraint - upper - lower) / (upper - lower))) - 1)

def rash_mult(condition, tolerance):
    return 1/(1+sympy.exp(condition/tolerance))
