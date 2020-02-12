"""
Base functions shared by all optimization methods.
"""


from beluga.utils import sympify, recursive_sub
from beluga.codegen import lambdify_
import copy
import numpy as np
import sympy
from sympy import Symbol, zoo
import functools as ft
import re
import logging

from .bvp import BVP


# TODO Implement Full Units Check

def identity(x):
    return x


def exterior_derivative(f, basis, derivative_fn):

    r"""

    :param f:
    :param basis:
    :param derivative_fn:
    :return:
    """

    df = None

    # Handle the (0)-grade case
    if isinstance(f, sympy.Expr):
        n = len(basis)
        df = [0]*len(basis)
        df = sympy.MutableDenseNDimArray(df)
        for ii in range(n):
            df[ii] = derivative_fn(f, basis[ii])

    # Handle the (1+)-grade cases
    if isinstance(f, sympy.Array) or isinstance(f, sympy.NDimArray):
        n = (len(basis),) + f.shape
        df = sympy.MutableDenseNDimArray(sympy.zeros(*n))
        if len(n) == 2:
            for ii in range(df.shape[0]):
                for jj in range(df.shape[1]):
                    if ii == jj:
                        df[ii, jj] = 0

                    if ii < jj:
                        df[ii, jj] += derivative_fn(f[jj], basis[ii])
                        df[ii, jj] += -derivative_fn(f[ii], basis[jj])
                        df[jj, ii] += -derivative_fn(f[jj], basis[ii])
                        df[jj, ii] += derivative_fn(f[ii], basis[jj])

        # TODO Check if this is valid statement
        if len(n) > 2:
            raise NotImplementedError('Grade greater than 2 not implemeted')

    return df


def form_units_and_tol_mult(*args):
    out_units = 1
    for arg in args:
        out_units *= arg['units']
    if all([arg['tol'] for arg in args]):
        out_tol = 1
        for arg in args:
            out_tol *= arg['tol']
    else:
        out_tol = None

    return out_units, out_tol


def form_units_and_tol_divide(num, den):
    out_units = num['units'] / den['units']
    if all([num['tol'], den['tol']]):
        out_tol = num['tol'] / den['tol']
    else:
        out_tol = None

    return out_units, out_tol


def make_augmented_cost(cost, initial_constraints, terminal_constraints):
    r"""
    Augments the cost function with the given list of constraints.

    .. math::
        \begin{aligned}
            \text{make_augmented_cost} : C^\infty(M) &\rightarrow C^\infty(M) \\
            (f, g) &\mapsto f + g_i \nu_i \; \forall \; i \in g
        \end{aligned}

    :param cost: The cost function, :math:`f`.
    :param initial_constraints: List of initial constraints to adjoin to the cost function, :math:`g`.
    :param terminal_constraints: List of initial constraints to adjoin to the cost function, :math:`g`.

    Returns the augmented cost function
    """

    def make_lagrange_mult_name(idx=1, location=None):

        if location == 'initial':
            suffix = '0'
        elif location == 'terminal':
            suffix = 'f'
        else:
            suffix = location

        return 'nu_' + suffix + '_' + str(idx)

    augmented_cost = copy.copy(cost)
    lagrange_multipliers = []

    for n, constraint in enumerate(initial_constraints):
        nu_name = make_lagrange_mult_name(idx=n, location='initial')
        nu_units, nu_tol = form_units_and_tol_divide(cost, constraint)
        lagrange_multipliers.append({'name': nu_name, 'sym': sympy.Symbol(nu_name), 'units': nu_units, 'tol': nu_tol})
        augmented_cost['initial'] += sympy.Symbol(nu_name) * constraint['expr']

    for n, constraint in enumerate(terminal_constraints):
        nu_name = make_lagrange_mult_name(idx=n, location='terminal')
        nu_units, nu_tol = form_units_and_tol_divide(cost, constraint)
        lagrange_multipliers.append({'name': nu_name, 'sym': sympy.Symbol(nu_name), 'units': nu_units, 'tol': nu_tol})
        augmented_cost['terminal'] += sympy.Symbol(nu_name) * constraint['expr']

    return augmented_cost, lagrange_multipliers


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
    x = [state for state in states] + [costate for costate in costates]
    u = [c for c in controls]
    xdot = sympy.Matrix([sympify(state) for state in states_rates] + [sympify(lam) for lam in costates_rates])
    # Compute Jacobian
    dgdx = sympy.Matrix([[derivative_fn(g_i, x_i) for x_i in x] for g_i in g])
    dgdu = sympy.Matrix([[derivative_fn(g_i, u_i) for u_i in u] for g_i in g])

    udot = dgdu.LUsolve(-dgdx*xdot)  # dgdU * udot + dgdX * xdot = 0
    if zoo in udot.atoms():
        raise NotImplementedError('Complex infinity in ICRM control law. Potential bang-bang solution.')

    dae_states = u
    dae_equations = list(udot)
    dae_bc = g

    yield dae_states
    yield dae_equations
    yield dae_bc
    yield dgdx
    yield dgdu


def make_control_law(dhdu, controls):
    r"""
    Solves control equation to get control law.

    .. math::
        \frac{dH}{d\textbf{u}} = 0

    :param dhdu: The expression for :math:`dH / d\textbf{u}`.
    :param controls: A list of control variables, :math:`[u_1, u_2, \cdots, u_n]`.
    :return: Control law options.
    """
    var_list = list(controls)
    logging.debug("Solving dH/du...")
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.debug('Control found')
    control_options = ctrl_sol
    return control_options


def make_dhdu(ham, controls, derivative_fn):
    r"""
    Computes the partial of the hamiltonian w.r.t control variables.

    :param ham: Hamiltonian function.
    :param controls: A list of each control variable.
    :param derivative_fn: Total derivative function.
    :return: :math:`dH/du`
    """

    dhdu = []
    for ctrl in controls:
        dhdu.append(derivative_fn(ham, ctrl['symbol']))

    return dhdu


def make_hamiltonian_vector_field(hamiltonian, omega, basis, derivative_fn):
    r"""
    Makes a Hamiltonian vector field.


    :return: :math:`\X_H`, the Hamiltonian vector field.

    """
    if omega.shape[0] != omega.shape[1]:
        raise ValueError('omega must be square.')

    if omega.shape[0] % 2 != 0:
        raise ValueError('omega must be even-dimensional.')

    dh = exterior_derivative(hamiltonian, basis, derivative_fn)
    dh = sympy.Matrix(dh)
    o = omega.tomatrix()
    x_h = -o.LUsolve(dh)
    return x_h


def make_standard_symplectic_form(states, costates):
    r"""
    Makes the standard symplectic form.

    :param states: A list of state variables, :math:`x`.
    :param costates: A list of co-state variables, :math:`\lambda`.
    :return: :math:`\omega`, the standard symplectic form
    """
    if len(states) != len(costates):
        raise ValueError('Number of states and costates must be equal.')

    n = len(states)
    omega = sympy.zeros(2*n, 2*n)
    omega = sympy.MutableDenseNDimArray(omega)
    for ii in range(2*n):
        for jj in range(2*n):
            if jj - ii == n:
                omega[ii, jj] = 1
            if ii - jj == n:
                omega[ii, jj] = -1

    return omega


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

    dfdq = [expr.diff(dep_var).subs(dependent_vars.items()) for dep_var in dep_var_names]
    dqdx = [qexpr.diff(var) for qexpr in dep_var_expr]
    out = sum(d1 * d2 for d1, d2 in zip(dfdq, dqdx)) + sympy.diff(expr, var)
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


def is_symplectic(form):
    r"""
    Checks whether or not a given form is symplectic.

    :param form: A form.
    :return: Boolean representing if a form is symplectic or not.
    """
    if form is None:
        return False

    if len(form.shape) != 2:
        return False

    if (form.shape[0] % 2 != 0) or (form.shape[0] != form.shape[1]):
        return False

    out = True
    for ii in range(form.shape[0]):
        for jj in range(form.shape[1]):
            if ii == jj:
                if form[ii, jj] != 0:
                    out = False

            if ii != jj:
                if form[ii, jj] != -form[jj, ii]:
                    out = False

    return out


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
    r"""
    Creates a smooth multiplier to model switching conditions.

    :param condition: The condition.
    :param tolerance: Tolerance on the switching condition
    :return: Term to augment a quantity with.
    """
    return 1/(1+sympy.exp(condition/tolerance))


def pb(f, g, bvp):
    r"""

    :param f:
    :param g:
    :param bvp:
    :return:
    """
    if f is None and g is not None:
        o = bvp.the_omega().tomatrix()
        h = sympy.MutableDenseNDimArray([0] * o.shape[0])
        for ii, s in enumerate(bvp.states()):
            for jj, t in enumerate(bvp.states()):
                h[ii] += o[ii, jj]*total_derivative(g['function'], t['symbol'])

        return h
    raise NotImplementedError


def noether(bvp, quantity):
    r"""

    :param bvp:
    :param quantity:
    :return:
    """
    if not is_symplectic(bvp.omega):
        raise ValueError('Can\'t use Noether\'. System does not appear to be symplectic.')

    if 'field' in quantity.keys():
        is_symmetry = True
    else:
        is_symmetry = False

    if is_symmetry:
        o = bvp.the_omega().tomatrix()
        x = sympy.Matrix(quantity['field'])
        omega_x = o.LUsolve(x)
        gstar = 0
        for jj, state in enumerate(bvp.states()):
            gstar += sympy.integrate(omega_x[jj], state['symbol'])

        unit = bvp.constants_of_motion[0]['unit']/quantity['unit']

        return gstar, unit

    if not is_symmetry:
        g = pb(None, quantity, bvp)
        nonz = np.nonzero(g)
        if len(nonz) == 1:
            unit = bvp.state_list[nonz[0][0]]['unit']
        else:
            raise NotImplementedError

        return g, unit


def momentum_shift(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)
    independent = ocp.get_independent()
    ocp.state(str(ocp._properties['independent']['symbol']), '1', str(ocp._properties['independent']['unit']))
    ocp.independent('_TAU', ocp._properties['independent']['unit'])

    for ii, s in enumerate(ocp.get_symmetries()):
        ocp.get_symmetries()[ii]['field'].append(sympify('0'))

    independent_symmetry = True
    for ii, s in enumerate(ocp.states()):
        if total_derivative(s['eom'], independent['symbol']) != 0:
            independent_symmetry = False

    if independent_symmetry:
        ocp.symmetry(['0']*(len(ocp.states())-1) + ['1'], independent['unit'])

    def gamma_map(gamma):
        if len(gamma.dual_t) == 0:
            gamma.dual_t = np.zeros_like(gamma.t)

        gamma.y = np.column_stack((gamma.y, gamma.t))
        # gamma.dynamical_parameters = np.hstack((gamma.dynamical_parameters, gamma.t[-1] - gamma.t[0]))
        # gamma.t = gamma.t / gamma.t[-1]  # TODO: Check if this should be gamma.t / (gamma.t[-1] - gamma.t[0])

        if len(gamma.dual) == 0:
            gamma.dual = np.zeros_like(gamma.y)

        gamma.dual = np.column_stack((gamma.dual, gamma.dual_t))

        return gamma

    def gamma_map_inverse(gamma):
        gamma.t = gamma.y[:, -1]
        gamma.dual_t = gamma.dual[:, -1]
        gamma.y = np.delete(gamma.y, np.s_[-1:], axis=1)
        gamma.dual = np.delete(gamma.dual, np.s_[-1:], axis=1)
        # gamma.dynamical_parameters = np.delete(gamma.dynamical_parameters, np.s_[-1:])
        return gamma

    return ocp, gamma_map, gamma_map_inverse


def F_RASHS(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)

    # TODO: compose switches
    for q in ocp.get_switches():
        if isinstance(q['function'], list):
            true_value = 0
            for jj in range(len(q['function'])):
                temp_value = q['function'][jj]
                for kk in range(len(q['conditions'][jj])):
                    temp_value *= rash_mult(q['conditions'][jj][kk], q['tolerance'])
                true_value += temp_value

            q['function'] = true_value

    """
    Make substitutions with the switches
    """

    subber = dict()
    for q in ocp.get_switches():
        subber.update({q['symbol']: q['function']})

    if ocp.get_initial_cost() is not None:
        ocp.get_initial_cost()['function'], _ = recursive_sub(ocp.get_initial_cost()['function'], subber)

    if ocp.get_path_cost() is not None:
        ocp.get_path_cost()['function'], _ = recursive_sub(ocp.get_path_cost()['function'], subber)

    if ocp.get_terminal_cost() is not None:
        ocp.get_terminal_cost()['function'], _ = recursive_sub(ocp.get_terminal_cost()['function'], subber)

    for s in ocp.states():
        s['eom'], _ = recursive_sub(s['eom'], subber)

    gamma_map = identity
    gamma_map_inverse = identity
    return ocp, gamma_map, gamma_map_inverse


def F_EPSTRIG(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)

    path_cost = ocp.get_path_cost()
    the_constraint = ocp.get_path_constraints()[0]
    f = the_constraint['function']
    lower = the_constraint['lower']
    upper = the_constraint['upper']
    activator = the_constraint['activator']
    constraint_is_control = False
    for jj, u in enumerate(ocp.controls()):
        if the_constraint['function'] == u['symbol']:
            constraint_is_control = True
            control_index = jj

    if not constraint_is_control:
        raise NotImplementedError('Epsilon-Trig must be used with pure control-constraints.')

    activator_unit = None
    for const in ocp.get_constants():
        if activator == const['symbol']:
            activator_unit = const['unit']

    if activator_unit is None:
        raise Exception('Activator \'' + str(activator) + '\' not found in constants.')

    if path_cost is not None:
        if ocp.get_path_cost()['unit'] != activator_unit and ocp.get_path_cost()['function'] != 0:
            logging.warning('Dimension mismatch in path constraint \'' + str(f) + '\'')
        ocp.get_path_cost()['function'] += epstrig_path(f, lower, upper, activator)
    else:
        ocp.path_cost(epstrig_path(f, lower, upper, activator), activator_unit)

    subber = dict(zip([f], [(upper - lower) / 2 * sympy.sin(the_constraint['function']) + (upper + lower) / 2]))
    for ii in range(len(ocp.states())):
        ocp.states()[ii]['eom'] = ocp.states()[ii]['eom'].subs(subber, simultaneous=True)

    def gamma_map(gamma):
        gamma = copy.deepcopy(gamma)
        return gamma

    def gamma_map_inverse(gamma, control_index=control_index, the_constraint=the_constraint, const=ocp.get_constants()):
        gamma = copy.deepcopy(gamma)
        subber = dict()
        for c in const:
            subber.update({c['symbol']: c['value']})

        lower, _ = recursive_sub(the_constraint['lower'], subber)
        upper, _ = recursive_sub(the_constraint['upper'], subber)
        gamma.u[:, control_index] = (upper - lower) * (np.sin(gamma.u[:, control_index]) + 1) / 2 + lower
        return gamma

    del ocp.get_path_constraints()[0]

    return ocp, gamma_map, gamma_map_inverse


def F_UTM(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)
    the_constraint = ocp.get_path_constraints()[0]
    activator = the_constraint['activator']
    path_cost = ocp.get_path_cost()

    activator_unit = None
    for const in ocp.get_constants():
        if activator == const['symbol']:
            activator_unit = const['unit']

    if activator_unit is None:
        raise Exception('Activator \'' + str(activator) + '\' not found in constants.')

    L_UTM = utm_path(the_constraint['function'], the_constraint['lower'],
                     the_constraint['upper'], the_constraint['activator'])

    if path_cost is None:
        ocp.path_cost(L_UTM, activator_unit)
    else:
        ocp.get_path_cost()['function'] += L_UTM

    del ocp.get_path_constraints()[0]
    gamma_map = identity
    gamma_map_inverse = identity
    return ocp, gamma_map, gamma_map_inverse


def dualize(ocp, method='indirect'):
    r"""
    :param ocp:
    :param method:
    :return:
    """

    bvp = BVP()

    # TODO move this to be internal to BVP
    bvp.independent_variable = copy.copy(ocp.independent_variable)
    bvp.state_list = copy.copy(ocp.state_list)
    bvp.parameter_list = copy.copy(ocp.parameter_list)
    bvp.constant_list = copy.copy(ocp.constant_list)

    bvp.locals_dict = ocp.locals_dict
    bvp.mod_dict = ocp.mod_dict

    terminal_bcs_to_aug = [bc for bc in ocp.constraint_dict['terminal']
                           if bc['expr'].diff(ocp.independent_variable['sym']) == 0]

    terminal_bcs_time = [bc for bc in ocp.constraint_dict['terminal']
                         if bc['expr'].diff(ocp.independent_variable['sym']) != 0]

    augmented_cost, lagrange_multipliers = \
        make_augmented_cost(ocp.cost, ocp.constraint_dict['initial'], terminal_bcs_to_aug)

    for state in bvp.state_list:
        costate_name = 'lam_' + str(state['name'])
        units, tol = form_units_and_tol_divide(ocp.cost, state)
        bvp.costate_list.append({'name': costate_name, 'sym': sympy.Symbol(costate_name), 'eom': None,
                                 'units': units, 'tol': tol})

    bvp.hamiltonian = {'expr': ocp.cost['path'] + sum([costate['sym'] * state['eom']
                                                       for state, costate in zip(bvp.state_list, bvp.costate_list)]),
                       'units': ocp.cost['units'], 'tol': ocp.cost['tol']}

    if method == 'indirect':
        for state, costate in zip(bvp.state_list, bvp.costate_list):
            costate['eom'] = -bvp.hamiltonian['expr'].diff(state['sym'])

    elif method == 'diffyg':
        omega = make_standard_symplectic_form(bvp.state_list, bvp.costate_list)
        x_h = make_hamiltonian_vector_field(bvp.hamiltonian['expr'], omega,
                                            [item['sym'] for item in bvp.state_list + bvp.costate_list],
                                            total_derivative)
        n = len(bvp.state_list)
        costate_rates = x_h[-n:]
        for costate, rate in zip(bvp.costate_list, costate_rates):
            costate['eom'] = rate
        bvp.omega = omega

    else:
        raise NotImplementedError(method.capitalize() +
                                  ' for dualization is not implemented. Use ''indirect'' or ''diffyg''')

    if method == 'diffyg':
        # Evaluate integral(omega^-1(X,.))
        for ii, s in enumerate(bvp.symmetry_list):
            gstar, unit = noether(bvp, s)
            bvp.constants_of_motion.append({'name': '_c' + str(ii), 'expr': gstar, 'units': unit})

    for parameter in bvp.parameter_list:
        coparameter_name = 'lam_' + str(parameter['name'])
        units, tol = form_units_and_tol_divide(ocp.cost, parameter)
        bvp.coparameter_list.append({'name': coparameter_name, 'sym': sympy.Symbol(coparameter_name),
                                     'eom': -bvp.hamiltonian['expr'].diff(parameter['sym']),
                                     'units': units, 'tol': tol})

    # TODO: investigate use of noquad
    # d = []
    # for ii in range(len(coparameters)):
    #     if prob.parameters()[ii]['noquad'] is True:
    #         d += [ii]
    #
    # coparameters = [p for ii, p in enumerate(coparameters) if ii not in d]
    # coparameters_rates = [p for ii, p in enumerate(coparameters_rates) if ii not in d]
    # coparameters_units = [p for ii, p in enumerate(coparameters_units) if ii not in d]

    initial_bc = make_boundary_conditions(
        constraints, states, costates, parameters, coparameters,
        augmented_initial_cost, total_derivative, location='initial')

    for ii, s in enumerate(ocp.get_symmetries()):
        bvp.symmetry(s['field'] + [sympify('0') for _ in costates], s['unit'], s['remove'])


    bvp.constants_of_motion.append({'name': 'hamiltonian', 'expr': bvp.hamiltonian['expr'],
                                    'units': bvp.hamiltonian['units'], 'tol': bvp.hamiltonian['tol']})

    # TODO: Hardcoded handling of time bc. I should fix this sometime.
    time_bc = make_time_bc(constraints, total_derivative, hamiltonian_function, independent_variable)

    if time_bc is not None:
        terminal_bc += [time_bc]

    for ii, s in enumerate(ocp.controls()):
        bvp.control(s['symbol'], s['unit'])

    for ii, s in enumerate(initial_bc):
        bvp.initial_bc(s)

    for ii, s in enumerate(terminal_bc):
        bvp.terminal_bc(s)

    for ii, s in enumerate(parameters):
        bvp.parameter(s, parameters_units[ii])

    for ii, s in enumerate(coparameters):
        bvp.quad(s, coparameters_rates[ii], coparameters_units[ii])

    for ii, s in enumerate(initial_lm_params + terminal_lm_params):
        _unit = (initial_lm_params_units + terminal_lm_params_units)[ii]
        bvp.nd_parameter(s, _unit)

    bvp.independent(independent_variable, independent_variable_units)

    def gamma_map(gamma, ndp=len(initial_lm_params + terminal_lm_params)):
        gamma = copy.deepcopy(gamma)
        gamma.y = np.column_stack((gamma.y, gamma.dual))
        gamma.dual = np.array([])
        gamma.nondynamical_parameters = np.hstack((gamma.nondynamical_parameters, np.ones(ndp)))
        return gamma

    def gamma_map_inverse(gamma, n=n_states, ndp=len(initial_lm_params + terminal_lm_params)):
        gamma = copy.deepcopy(gamma)
        gamma.dual = gamma.y[:, -n:]
        gamma.y = gamma.y[:, :n]
        gamma.nondynamical_parameters = gamma.nondynamical_parameters[:-ndp]
        return gamma

    return bvp, gamma_map, gamma_map_inverse


def F_scaletime(bvp):
    r"""

    :param bvp:
    :return:
    """
    bvp = copy.deepcopy(bvp)

    _tf = Symbol('_tf')
    bvp.parameter(_tf, bvp._properties['independent']['unit'], noquad=True)

    for s in bvp.states():
        s['eom'] *= _tf

    for s in bvp.quads():
        s['eom'] *= _tf

    # O = bvp.the_omega()
    # if O is not None:
    #     bvp.omega(O/_tf)

    bvp.independent('_TAU', bvp._properties['independent']['unit'])

    def gamma_map(gamma):
        gamma = copy.deepcopy(gamma)
        gamma.dynamical_parameters = np.hstack((gamma.dynamical_parameters, gamma.t[-1] - gamma.t[0]))
        gamma.t = gamma.t / gamma.t[-1]  # TODO: Check if this should be gamma.t / (gamma.t[-1] - gamma.t[0])
        return gamma

    def gamma_map_inverse(gamma):
        gamma = copy.deepcopy(gamma)
        gamma.t = gamma.t * gamma.dynamical_parameters[-1]
        gamma.dynamical_parameters = np.delete(gamma.dynamical_parameters, np.s_[-1:])
        return gamma

    return bvp, gamma_map, gamma_map_inverse


def F_PMP(bvp):
    r"""

    :param bvp:
    :return:
    """
    bvp = copy.deepcopy(bvp)

    dhdu = make_dhdu(bvp.get_constants_of_motion()[0]['function'], bvp.controls(), total_derivative)
    control_law = make_control_law(dhdu, [u['symbol'] for u in bvp.controls()])
    bvp._control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]

    def gamma_map(gamma):
        gamma = copy.deepcopy(gamma)
        return gamma

    def gamma_map_inverse(gamma):
        gamma = copy.deepcopy(gamma)
        return gamma

    return bvp, gamma_map, gamma_map_inverse


def F_ICRM(bvp, method='indirect'):
    r"""

    :param bvp:
    :return:
    """
    bvp = copy.deepcopy(bvp)

    n_states = len(bvp.states())
    n_controls = len(bvp.controls())

    dHdu = make_dhdu(bvp.get_constants_of_motion()[0]['function'], bvp.controls(), total_derivative)
    g = dHdu
    X = [s['symbol'] for s in bvp.states()]
    U = [c['symbol'] for c in bvp.controls()]
    xdot = sympy.Matrix([s['eom'] for s in bvp._properties['states']])

    # Compute Jacobian
    dgdX = sympy.Matrix([[total_derivative(g_i, x_i) for x_i in X] for g_i in g])
    dgdU = sympy.Matrix([[total_derivative(g_i, u_i) for u_i in U] for g_i in g])

    udot = dgdU.LUsolve(-dgdX * xdot)  # dgdU * udot + dgdX * xdot = 0
    if zoo in udot.atoms():
        raise NotImplementedError('Complex infinity in ICRM control law. Potential bang-bang solution.')

    dae_states = U
    dae_equations = list(udot)
    dae_bc = g
    n_dae = len(dae_states)

    if method == 'indirect':
        states_old = bvp.states()
        n = int(len(states_old)/2)
        states_new = states_old[:n]
        for ii, s in enumerate(dae_states):
            states_new.append({'symbol': s, 'eom': dae_equations[ii], 'unit': bvp._properties['controls'][ii]['unit']})
            # bvp.state(s, dae_equations[ii], bvp._properties['controls'][ii]['unit'])
        states_new += states_old[-n:]
        bvp._properties['states'] = states_new

    elif method == 'diffyg':
        cost_unit = bvp.get_constants_of_motion()[0]['unit']
        controls_unit = [u['unit'] for u in bvp.controls()]
        lamU = make_costate_names(dae_states)
        lamU_units = [cost_unit / unit for unit in controls_unit]
        omega = bvp.the_omega()
        _u = []
        _lamu = []
        for ii in range(len(dae_states)):
            _u += [{'symbol': dae_states[ii], 'eom': dae_equations[ii], 'unit': bvp.controls()[ii]['unit']}]
            _lamu += [{'symbol': lamU[ii], 'eom': '0', 'unit': lamU_units[ii]}]

        bvp._properties['states'] = bvp.states()[:int(n_states/2)] + _u + bvp.states()[-int(n_states/2):] + _lamu
        n = len(bvp.states())
        omega_new = make_standard_symplectic_form(bvp.states()[:int(n/2)], bvp.states()[-int(n/2):])
        independent_index = int(n_states/2) - 1
        nhalf = int(len(bvp.states())/2)
        # Add (du - u' dt) ^ (dlamU - 0 dt) to omega
        for ii, u in enumerate(dae_equations):
            omega_new[int(nhalf - n_dae + ii), int(2 * nhalf - n_dae + ii)] = 1
            omega_new[int(2 * nhalf - n_dae + ii), int(nhalf - n_dae + ii)] = -1
            omega_new[independent_index, int(2 * nhalf - n_dae + ii)] = -dae_equations[ii]
            omega_new[int(2 * nhalf - n_dae + ii), independent_index] = dae_equations[ii]

        bvp.omega(omega_new)
        basis = [x['symbol'] for x in bvp.states()]
        X_H = make_hamiltonian_vector_field(bvp.get_constants_of_motion()[0]['function'], bvp.the_omega(), basis, total_derivative)

        for ii, s in enumerate(bvp.states()):
            s['eom'] = X_H[ii]

        for ii, lU in enumerate(lamU):
            bvp.initial_bc(lU)

    for ii, s in enumerate(dae_bc):
        bvp.terminal_bc(s)

    del bvp._properties['controls']
    bvp._control_law = []

    def gamma_map(gamma, n=n_states, m=n_controls, method=method):
        gamma = copy.deepcopy(gamma)
        if len(gamma.dual_u) == 0:
            gamma.dual_u = np.zeros_like(gamma.u)

        if method == 'indirect':
            gamma.y = np.column_stack((gamma.y[:, :int(n / 2)], gamma.u, gamma.y[:, -int(n / 2):]))
        elif method == 'diffyg':
            gamma.y = np.column_stack((gamma.y[:, :int(n / 2)], gamma.u, gamma.y[:, -int(n / 2):], gamma.dual_u))
        gamma.u = np.array([]).reshape((n, 0))
        return gamma

    def gamma_map_inverse(gamma, n=n_states, m=n_controls, method=method):
        gamma = copy.deepcopy(gamma)
        if method == 'indirect':
            y1h = gamma.y[:, :int(n / 2)]
            gamma.u = gamma.y[:, int(n / 2):int(n / 2)+m]
            y2h = gamma.y[:, int(n/2)+m:n+m]
            gamma.y = np.hstack((y1h, y2h))
        elif method == 'diffyg':
            y1h = gamma.y[:, :int(n / 2)]
            gamma.u = gamma.y[:, int(n / 2):int(n / 2) + m]
            y2h = gamma.y[:, int(n / 2) + m:n + m]
            gamma.dual_u = gamma.y[:, -m:]
            gamma.y = np.hstack((y1h, y2h))
        return gamma

    return bvp, gamma_map, gamma_map_inverse


def F_MF(bvp, com_index):
    r"""

    :param bvp:
    :param com_index:
    :return:
    """
    bvp = copy.deepcopy(bvp)
    # hamiltonian = bvp.get_constants_of_motion()[0]['function']
    # O = bvp.the_omega()
    # X_H = make_hamiltonian_vector_field(hamiltonian, O, [s['symbol'] for s in bvp.states()], total_derivative)

    com = bvp.get_constants_of_motion()[com_index]

    # states = [str(s['symbol']) for s in bvp.states()]
    # parameters = [str(s['symbol']) for s in bvp.parameters()]
    # constants = [str(s['symbol']) for s in bvp.get_constants()]
    # fn_p = make_jit_fn(states + parameters + constants, str(com['function']))

    states = [(s['symbol']) for s in bvp.states()]
    parameters = [(s['symbol']) for s in bvp.parameters()]
    constants = [(s['symbol']) for s in bvp.get_constants()]
    fn_p = lambdify_([states, parameters, constants], com['function'])

    atoms = com['function'].atoms()
    atoms2 = set()
    for a in atoms:
        if isinstance(a, Symbol) and (a not in {s['symbol'] for s in bvp.parameters() + bvp.get_constants()}):
            atoms2.add(a)

    atoms = atoms2

    solve_for_p = sympy.solve(com['function'] - com['symbol'], atoms, dict=True, simplify=False)

    if len(solve_for_p) > 1:
        raise ValueError

    for parameter in solve_for_p[0].keys():
        the_symmetry, symmetry_unit = noether(bvp, com)
        replace_p = parameter
        for ii, s in enumerate(bvp.states()):
            if s['symbol'] == parameter:
                parameter_index = ii
                bvp.parameter(com['symbol'], com['unit'])

    symmetry_index = parameter_index - int(len(bvp.states())/2)

    # Derive the quad
    # Evaluate int(pdq) = int(PdQ)
    n = len(bvp.quads())
    symmetry_symbol = Symbol('_q' + str(n))
    _lhs = com['function']/com['symbol']*the_symmetry
    lhs = 0
    for ii, s in enumerate(bvp.states()):
        lhs += sympy.integrate(_lhs[ii], s['symbol'])

    lhs, _ = recursive_sub(lhs, solve_for_p[0])

    # states = [str(s['symbol']) for s in bvp.states()]
    # parameters = [str(s['symbol']) for s in bvp.parameters()]
    # constants = [str(s['symbol']) for s in bvp.get_constants()]
    # the_p = [str(com['symbol'])]
    # fn_q = make_jit_fn(states + parameters + constants, str(lhs))

    states = [s['symbol'] for s in bvp.states()]
    parameters = [s['symbol'] for s in bvp.parameters()]
    constants = [s['symbol'] for s in bvp.get_constants()]
    the_p = [com['symbol']]
    fn_q = lambdify_([states, parameters, constants], lhs)

    replace_q = bvp.states()[symmetry_index]['symbol']
    solve_for_q = sympy.solve(lhs - symmetry_symbol, replace_q, dict=True, simplify=False)

    # Evaluate X_H(pi(., c)), pi = O^sharp
    O = bvp.the_omega().tomatrix()
    rvec = sympy.Matrix(([0]*len(bvp.states())))
    for ii, s1 in enumerate(bvp.states()):
        for jj, s2 in enumerate(bvp.states()):
            rvec[ii] += O[ii,jj]*total_derivative(com['function'], s2['symbol'])

    symmetry_eom = 0
    for ii, s in enumerate(bvp.states()):
        symmetry_eom += s['eom']*rvec[ii]

    # TODO: Figure out how to find units of the quads. This is only works in some specialized cases.
    symmetry_unit = bvp.states()[symmetry_index]['unit']

    bvp.quad(symmetry_symbol, symmetry_eom, symmetry_unit)

    for ii, s in enumerate(bvp.states()):
        s['eom'], _ = recursive_sub(s['eom'], solve_for_p[0])
        s['eom'], _ = recursive_sub(s['eom'], solve_for_q[0])

    for ii, s in enumerate(bvp.all_bcs()):
        s['function'], _ = recursive_sub(s['function'], solve_for_p[0])
        s['function'], _ = recursive_sub(s['function'], solve_for_q[0])

    for ii, law in enumerate(bvp._control_law):
        for jj, symbol in enumerate(law.keys()):
            bvp._control_law[ii][symbol], _ = recursive_sub(sympify(bvp._control_law[ii][symbol]), solve_for_p[0])
            bvp._control_law[ii][symbol] = str(bvp._control_law[ii][symbol])
            bvp._control_law[ii][symbol], _ = recursive_sub(sympify(bvp._control_law[ii][symbol]), solve_for_q[0])
            bvp._control_law[ii][symbol] = str(bvp._control_law[ii][symbol])

    for ii, s in enumerate(bvp.get_constants_of_motion()):
        if ii != com_index:
            s['function'], _ = recursive_sub(s['function'], solve_for_p[0])
            s['function'], _ = recursive_sub(s['function'], solve_for_q[0])

    O = bvp.the_omega().tomatrix()
    if parameter_index > symmetry_index:
        del bvp.states()[parameter_index]
        del bvp.states()[symmetry_index]
        O.row_del(parameter_index)
        O.col_del(parameter_index)
        O.row_del(symmetry_index)
        O.col_del(symmetry_index)
    else:
        del bvp.states()[symmetry_index]
        del bvp.states()[parameter_index]
        O.row_del(symmetry_index)
        O.col_del(symmetry_index)
        O.row_del(parameter_index)
        O.col_del(parameter_index)

    bvp.omega(sympy.MutableDenseNDimArray(O))

    del bvp.get_constants_of_motion()[com_index]

    # states = [str(s['symbol']) for s in bvp.states()]
    # quads = [str(s['symbol']) for s in bvp.quads()]
    # parameters = [str(s['symbol']) for s in bvp.parameters()]
    # constants = [str(s['symbol']) for s in bvp.get_constants()]
    # fn_q_inv = make_jit_fn(states + quads + parameters + constants, str(solve_for_q[0][replace_q]))

    states = [s['symbol'] for s in bvp.states()]
    quads = [s['symbol'] for s in bvp.quads()]
    parameters = [s['symbol'] for s in bvp.parameters()]
    constants = [s['symbol'] for s in bvp.get_constants()]
    fn_q_inv = lambdify_([states, quads, parameters, constants], solve_for_q[0][replace_q])

    fn_p_inv = lambdify_([states, parameters, constants], solve_for_p[0][replace_p])

    def gamma_map(gamma, parameter_index=parameter_index, symmetry_index=symmetry_index, fn_q=fn_q, fn_p=fn_p):
        gamma = copy.deepcopy(gamma)
        cval = fn_p(gamma.y[0], gamma.dynamical_parameters, gamma.const)
        qval = np.ones_like(gamma.t)
        gamma.dynamical_parameters = np.hstack((gamma.dynamical_parameters, cval))
        for ii, t in enumerate(gamma.t):
            qval[ii] = fn_q(gamma.y[ii], gamma.dynamical_parameters, gamma.const)

        if parameter_index > symmetry_index:
            gamma.y = np.delete(gamma.y, np.s_[parameter_index], axis=1)
            gamma.y = np.delete(gamma.y, np.s_[symmetry_index], axis=1)
        else:
            gamma.y = np.delete(gamma.y, np.s_[symmetry_index], axis=1)
            gamma.y = np.delete(gamma.y, np.s_[parameter_index], axis=1)

        gamma.q = np.column_stack((gamma.q, qval))
        return gamma

    def gamma_map_inverse(gamma, parameter_index=parameter_index, symmetry_index=symmetry_index, fn_q_inv=fn_q_inv, fn_p_inv=fn_p_inv):
        gamma = copy.deepcopy(gamma)
        qinv = np.ones_like(gamma.t)
        pinv = np.ones_like(gamma.t)
        for ii, t in enumerate(gamma.t):
            qinv[ii] = fn_q_inv(gamma.y[ii], gamma.q[ii], gamma.dynamical_parameters, gamma.const)
            pinv[ii] = fn_p_inv(gamma.y[ii], gamma.dynamical_parameters, gamma.const)
        # breakpoint()
        cval = gamma.dynamical_parameters[-1]
        state = np.ones_like(gamma.t)*cval
        state = pinv
        qval = qinv
        if parameter_index > symmetry_index:
            gamma.y = np.column_stack((gamma.y[:, :symmetry_index], qval, gamma.y[:, symmetry_index:]))
            gamma.y = np.column_stack((gamma.y[:, :parameter_index], state, gamma.y[:, parameter_index:]))
        else:
            gamma.y = np.column_stack((gamma.y[:, :parameter_index], state, gamma.y[:, parameter_index:]))
            gamma.y = np.column_stack((gamma.y[:, :symmetry_index], qval, gamma.y[:, symmetry_index:]))

        gamma.q = np.delete(gamma.q, np.s_[-1], axis=1)
        gamma.dynamical_parameters = gamma.dynamical_parameters[:-1]
        return gamma

    return bvp, gamma_map, gamma_map_inverse
