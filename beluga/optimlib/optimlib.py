"""
Base functions shared by all optimization methods.
"""


from beluga.utils import sympify, _combine_args_kwargs, recursive_sub
import copy
import numpy as np
import sympy
from sympy import Expr, Symbol, zoo
import functools as ft
import re
import logging


class BVP(object):
    """
    Class containing information for a Hamiltonian boundary-value problem.

    Valid parameters and their arguments are in the following table.

    +--------------------------------+--------------------------------+------------------------------------------------+
    | Valid parameters               | arguments                      | datatype                                       |
    +================================+================================+================================================+
    | state                          | (name, EOM, unit)              | (string, string, string)                       |
    +--------------------------------+--------------------------------+------------------------------------------------+

    """

    def __init__(self):
        self._properties = dict()  # Problem properties

    def __repr__(self):
        if self._properties.keys():
            m = max(map(len, list(self._properties.keys()))) + 1
            return '\n'.join([k.rjust(m) + ': ' + repr(v)
                              for k, v in sorted(self._properties.items())])
        else:
            return self.__class__.__name__ + "()"

    def state(self, symbol, eom, unit):
        r"""

        :param symbol:
        :param eom:
        :param unit:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(eom, str):
            eom = sympify(eom)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(eom, Expr):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError

        temp = self._properties.get('states', [])
        temp.append({'symbol': symbol, 'eom': eom, 'unit': unit})
        self._properties['states'] = temp
        return self

    def states(self):
        r"""

        :return:
        """
        return self._properties.get('states', dict())

    def quad(self, symbol, eom, unit):
        r"""

        :param symbol:
        :param eom:
        :param unit:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(eom, str):
            eom = sympify(eom)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(eom, Expr):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError

        temp = self._properties.get('quads', [])
        temp.append({'symbol': symbol, 'eom': eom, 'unit': unit})
        self._properties['quads'] = temp
        return self

    def quads(self):
        r"""

        :return:
        """
        return self._properties.get('quads', [])

    def constant_of_motion(self, symbol, function, unit):
        r"""

        :param symbol:
        :param function:
        :param unit:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(function, str):
            function = sympify(function)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(function, Expr):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError

        temp = self._properties.get('constants_of_motion', [])
        temp.append({'symbol': symbol, 'function': function, 'unit': unit})
        self._properties['constants_of_motion'] = temp
        return self

    def constants_of_motion(self):
        r"""

        :return:
        """
        return self._properties.get('constants_of_motion', [])

    def control(self, symbol, unit):
        r"""

        :param symbol:
        :param unit:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError

        temp = self._properties.get('controls', [])
        temp.append({'symbol': symbol, 'unit': unit})
        self._properties['controls'] = temp
        return self

    def controls(self):
        r"""

        :return:
        """
        return self._properties.get('controls', [])

    def initial_bc(self, function):
        r"""

        :param function:
        :return:
        """
        if isinstance(function, str):
            function = sympify(function)

        if not isinstance(function, Expr):
            raise TypeError

        temp = self._properties.get('initial_bc', [])
        temp.append({'function': function})
        self._properties['initial_bc'] = temp
        return self

    def initial_bcs(self):
        r"""

        :return:
        """
        return self._properties.get('initial_bc', [])

    def terminal_bc(self, function):
        r"""

        :param function:
        :return:
        """
        if isinstance(function, str):
            function = sympify(function)

        if not isinstance(function, Expr):
            raise TypeError

        temp = self._properties.get('terminal_bc', [])
        temp.append({'function': function})
        self._properties['terminal_bc'] = temp
        return self

    def terminal_bcs(self):
        r"""

        :return:
        """
        return self._properties.get('terminal_bc', [])

    def all_bcs(self):
        r"""

        :return:
        """
        return self.initial_bcs() + self.terminal_bcs()

    def parameter(self, symbol, unit, noquad=False):
        r"""

        :param symbol:
        :param unit:
        :param noquad:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError
        if not isinstance(noquad, bool):
            raise TypeError

        temp = self._properties.get('parameters', [])
        temp.append({'symbol': symbol, 'unit': unit, 'noquad': noquad})
        self._properties['parameters'] = temp
        return self

    def parameters(self):
        r"""

        :return:
        """
        return self._properties.get('parameters', [])

    def nd_parameter(self, symbol, unit):
        r"""

        :param symbol:
        :param unit:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError

        temp = self._properties.get('nd_parameters', [])
        temp.append({'symbol': symbol, 'unit': unit})
        self._properties['nd_parameters'] = temp
        return self

    def nd_parameters(self):
        r"""

        :return:
        """
        return self._properties.get('nd_parameters', [])

    def all_parameters(self):
        r"""

        :return:
        """
        return self.parameters() + self.nd_parameters()

    def independent(self, symbol, unit):
        r"""

        :param symbol:
        :param unit:
        :return:
        """
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
        if isinstance(unit, str):
            unit = sympify(unit)

        if not isinstance(symbol, Symbol):
            raise TypeError
        if not isinstance(unit, Expr):
            raise TypeError

        temp = {'symbol': symbol, 'unit': unit}
        self._properties['independent'] = temp
        return self

    def omega(self, omega):
        r"""

        :param omega:
        :return:
        """
        if not isinstance(omega, sympy.DenseNDimArray):
            raise ValueError

        self._properties['omega'] = omega
        return self

    def the_omega(self):
        r"""

        :return:
        """
        temp = self._properties.get('omega', None)
        return temp


def Id(x, _compute_control=None):
    return x


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
    workspace['independent_var'] = ocp._properties['independent']['symbol']
    workspace['independent_var_units'] = ocp._properties['independent']['unit']
    workspace['states'] = [s['symbol'] for s in ocp.states()]
    workspace['states_rates'] = [s['eom'] for s in ocp.states()]
    workspace['states_units'] = [s['unit'] for s in ocp.states()]
    workspace['controls'] = [u['symbol'] for u in ocp.controls()]
    workspace['controls_units'] = [u['unit'] for u in ocp.controls()]
    workspace['constants'] = [k['symbol'] for k in ocp.constants()]
    workspace['constants_values'] = [k['value'] for k in ocp.constants()]
    workspace['constants_units'] = [k['unit'] for k in ocp.constants()]
    workspace['constants_of_motion'] = [k['symbol'] for k in ocp.constants_of_motion()]
    workspace['constants_of_motion_values'] = [k['function'] for k in ocp.constants_of_motion()]
    workspace['constants_of_motion_units'] = [k['unit'] for k in ocp.constants_of_motion()]
    workspace['symmetries'] = [k['function'] for k in ocp.symmetries()]
    workspace['parameters'] = [k['name'] for k in ocp.parameters()]
    workspace['parameters_units'] = [k['unit'] for k in ocp.parameters()]

    constraints = ocp.constraints()
    constraints['path'] = ocp.path_constraints()

    workspace['constraints'] = {c_type: [sympify(c_obj['function']) for c_obj in c_list]
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

    workspace['path_constraints'] = [sympify(c_obj['function']) for c_obj in constraints.get('path', [])]
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

    workspace['initial_cost'] = ocp.get_cost('initial')['function']
    workspace['initial_cost_units'] = ocp.get_cost('initial')['unit']
    workspace['terminal_cost'] = ocp.get_cost('terminal')['function']
    workspace['terminal_cost_units'] = ocp.get_cost('terminal')['unit']
    workspace['path_cost'] = ocp.get_cost('path')['function']
    workspace['path_cost_units'] = ocp.get_cost('path')['unit']
    return workspace


def exterior_derivative(f, basis, derivative_fn):
    r"""

    :param f:
    :param basis:
    :return:
    """

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

        if len(n) > 2:
            raise NotImplementedError

        # t = [range(d) for d in df.shape]
        # for indices in it.product(*t):
        #     if all(x < y for x, y in zip(indices, indices[1:])):
        #         for ind in it.permutations(indices):
        #             df[ind] = derivative_fn(f[ind[1:]], basis[ind[0]])
        #             breakpoint()
        #     # df[indices] = 1
        #     # breakpoint()

    return df


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
        dHdu.append(derivative_fn(ham, ctrl['symbol']))

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


def make_hamiltonian_vector_field(hamiltonian, omega, basis, derivative_fn):
    r"""
    Makes a Hamiltonian vector field.

    :param states: A list of state variables, :math:`x`.
    :param states_rates: A list of rates of change for the state variables :math:`\dot{x} = f'.
    :param costates: A list of co-state variables, :math:`\lambda`.
    :param costates_rates: A list of costate rates, :math:`\dot{\lambda}_x`
    :return: :math:`\X_H`, the Hamiltonian vector field.
    """
    if omega.shape[0] != omega.shape[1]:
        raise ValueError('omega must be square.')

    if omega.shape[0] % 2 != 0:
        raise ValueError('omega must be even-dimensional.')

    dH = exterior_derivative(hamiltonian, basis, derivative_fn)
    dH = sympy.Matrix(dH)
    O = omega.tomatrix()
    X_H = -O.LUsolve(dH)
    return X_H


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
            if jj-ii == n:
                omega[ii,jj] = 1
            if ii-jj == n:
                omega[ii,jj] = -1

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


def F_momentumshift(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)

    # _tf = Symbol('_tf')
    ocp.state(str(ocp._properties['independent']['symbol']), '1', str(ocp._properties['independent']['unit']))
    # ocp.parameter(_tf, ocp._properties['independent']['unit'], noquad=True)

    # for s in ocp.states():
    #     s['eom'] *= _tf
    #     s['unit'] *= 1  # temp_unit

    # ocp.the_path_cost()['function'] *= _tf
    # ocp.the_path_cost()['unit'] *= 1  # ocp._properties['independent']['unit']

    ocp.independent('_TAU', ocp._properties['independent']['unit'])
    # ocp.constraints().terminal('_TAU - 1', '1')
    def gamma_map(gamma, _compute_control=None):
        if len(gamma.dual_t) == 0:
            gamma.dual_t = np.zeros_like(gamma.t)

        gamma.y = np.column_stack((gamma.y, gamma.t))
        # gamma.dynamical_parameters = np.hstack((gamma.dynamical_parameters, gamma.t[-1] - gamma.t[0]))
        # gamma.t = gamma.t / gamma.t[-1]  # TODO: Check if this should be gamma.t / (gamma.t[-1] - gamma.t[0])

        if len(gamma.dual) == 0:
            gamma.dual = np.zeros_like(gamma.y)

        gamma.dual = np.column_stack((gamma.dual, gamma.dual_t))

        return gamma

    def gamma_map_inverse(gamma, _compute_control=None):
        gamma.t = gamma.y[:, -1]
        gamma.dual_t = gamma.dual[:, -1]
        gamma.y = np.delete(gamma.y, np.s_[-1:], axis=1)
        gamma.dual = np.delete(gamma.dual, np.s_[-1:], axis=1)
        # gamma.dynamical_parameters = np.delete(gamma.dynamical_parameters, np.s_[-1:])
        return gamma

    return ocp, gamma_map, gamma_map_inverse


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

    bvp.independent('_TAU', bvp._properties['independent']['unit'])

    def gamma_map(gamma, _compute_control=None):
        gamma = copy.deepcopy(gamma)
        gamma.dynamical_parameters = np.hstack((gamma.dynamical_parameters, gamma.t[-1] - gamma.t[0]))
        gamma.t = gamma.t / gamma.t[-1]  # TODO: Check if this should be gamma.t / (gamma.t[-1] - gamma.t[0])
        return gamma

    def gamma_map_inverse(gamma, _compute_control=None):
        gamma = copy.deepcopy(gamma)
        gamma.t = gamma.t * gamma.dynamical_parameters[-1]
        gamma.dynamical_parameters = np.delete(gamma.dynamical_parameters, np.s_[-1:])
        return gamma

    return bvp, gamma_map, gamma_map_inverse

def F_RASHS(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)

    # TODO: compose switches
    for q in ocp.switches():
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
    for q in ocp.switches():
        subber.update({q['symbol']: q['function']})

    ocp.the_initial_cost()['function'], _ = recursive_sub(ocp.the_initial_cost()['function'], subber)
    ocp.the_path_cost()['function'], _ = recursive_sub(ocp.the_path_cost()['function'], subber)
    ocp.the_terminal_cost()['function'], _ = recursive_sub(ocp.the_terminal_cost()['function'], subber)
    for s in ocp.states():
        s['eom'], _ = recursive_sub(s['eom'], subber)

    gamma_map = Id
    gamma_map_inverse = Id
    return ocp, gamma_map, gamma_map_inverse


def F_EPSTRIG(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)

    set_cost = False
    if ocp.the_path_cost()['function'] == 0:
        set_cost = True

    the_constraint = ocp.path_constraints()[0]
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
    for const in ocp.constants():
        if activator == const['symbol']:
            activator_unit = const['unit']

    if activator_unit is None:
        raise Exception('Activator \'' + str(activator) + '\' not found in constants.')

    if ocp.the_path_cost()['unit'] != activator_unit and ocp.the_path_cost()['function'] != 0:
        logging.warning('Dimension mismatch in path constraint \'' + str(f) + '\'')

    ocp.the_path_cost()['function'] += epstrig_path(f, lower, upper, activator)
    if set_cost:
        ocp.the_path_cost()['unit'] = activator_unit

    subber = dict(zip([f], [(upper - lower) / 2 * sympy.sin(the_constraint['function']) + (upper + lower) / 2]))
    for ii in range(len(ocp.states())):
        ocp.states()[ii]['eom'] = ocp.states()[ii]['eom'].subs(subber, simultaneous=True)

    def gamma_map(gamma, _compute_control=None):
        gamma = copy.deepcopy(gamma)
        return gamma

    def gamma_map_inverse(gamma, _compute_control=None, control_index=control_index, the_constraint=the_constraint, const=ocp.constants()):
        gamma = copy.deepcopy(gamma)
        subber = dict()
        for c in const:
            subber.update({c['symbol']: c['value']})

        lower, _ = recursive_sub(the_constraint['lower'], subber)
        upper, _ = recursive_sub(the_constraint['upper'], subber)
        gamma.u[:, control_index] = (upper - lower) * (np.sin(gamma.u[:, control_index]) + 1) / 2 + lower
        return gamma

    del ocp.path_constraints()[0]

    return ocp, gamma_map, gamma_map_inverse


def F_UTM(ocp):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)
    the_constraint = ocp.path_constraints()[0]
    activator = the_constraint['activator']
    set_cost = False
    if ocp.the_path_cost()['function'] == 0:
        set_cost = True

    activator_unit = None
    for const in ocp.constants():
        if activator == const['symbol']:
            activator_unit = const['unit']

    if activator_unit is None:
        raise Exception('Activator \'' + str(activator) + '\' not found in constants.')

    L_UTM = utm_path(ocp.path_constraints()[0]['function'], ocp.path_constraints()[0]['lower'],
                     ocp.path_constraints()[0]['upper'], ocp.path_constraints()[0]['activator'])
    ocp.the_path_cost()['function'] += L_UTM
    if set_cost:
        ocp.the_path_cost()['unit'] = activator_unit

    del ocp.path_constraints()[0]
    gamma_map = Id
    gamma_map_inverse = Id
    return ocp, gamma_map, gamma_map_inverse


def Dualize(ocp, method='indirect'):
    r"""

    :param ocp:
    :return:
    """
    ocp = copy.deepcopy(ocp)
    independent_variable = ocp._properties['independent']['symbol']
    independent_variable_units = ocp._properties['independent']['unit']

    n_states = len(ocp.states())

    terminal_bcs_to_aug = [[bc['function'], bc['unit']] for bc in ocp.constraints()['terminal'] if
                           total_derivative(bc['function'], independent_variable) == 0]

    terminal_bcs_time = [[bc['function'], bc['unit']] for bc in ocp.constraints()['terminal'] if
                         total_derivative(bc['function'], independent_variable) != 0]

    ocp.constraints()['terminal'] = [{'function': bc[0], 'unit':bc[1]} for bc in terminal_bcs_to_aug]

    # TODO: The following can be cleaned up by rewriting `make_augmented_cost`
    constraints = dict()
    constraints_units = dict()
    constraints['initial'] = [b['function'] for b in ocp.constraints()['initial']]
    constraints_units['initial'] = [b['unit'] for b in ocp.constraints()['initial']]
    constraints['terminal'] = [bc[0] for bc in terminal_bcs_to_aug]
    constraints_units['terminal'] = [bc[1] for bc in terminal_bcs_to_aug]
    initial_cost = ocp.the_initial_cost()['function']
    initial_cost_unit = ocp.the_initial_cost()['unit']
    terminal_cost = ocp.the_terminal_cost()['function']
    terminal_cost_unit = ocp.the_terminal_cost()['unit']
    path_cost = ocp.the_path_cost()['function']
    path_cost_unit = ocp.the_path_cost()['unit']
    states = [s['symbol'] for s in ocp.states()]
    states_rates = [s['eom'] for s in ocp.states()]
    states_units = [s['unit'] for s in ocp.states()]
    parameters = [p['symbol'] for p in ocp.parameters()]
    parameters_units = [p['unit'] for p in ocp.parameters()]

    if initial_cost_unit != path_cost_unit*initial_cost_unit and (initial_cost != 0) and (path_cost != 0):
        raise Exception('Initial and path cost units mismatch: ' + str(initial_cost_unit) + ' =/= ' + str(path_cost_unit * independent_variable_units))

    if initial_cost_unit != terminal_cost_unit and (initial_cost != 0) and (terminal_cost != 0):
        raise Exception('Initial and terminal cost units mismatch: ' + str(initial_cost_unit) + ' =/= ' + str(terminal_cost_unit))

    if terminal_cost_unit != path_cost_unit*independent_variable_units and (terminal_cost != 0) and (path_cost != 0):
        raise Exception('Terminal and path cost units mismatch: ' + str(terminal_cost_unit) + ' =/= ' + str(path_cost_unit * independent_variable_units))

    if initial_cost != 0:
        cost_unit = initial_cost_unit
    elif terminal_cost != 0:
        cost_unit = terminal_cost_unit
    elif path_cost != 0:
        cost_unit = path_cost_unit * independent_variable_units

    augmented_initial_cost, augmented_initial_cost_units, initial_lm_params, initial_lm_params_units = \
        make_augmented_cost(initial_cost, cost_unit, constraints, constraints_units, location='initial')

    augmented_terminal_cost, augmented_terminal_cost_units, terminal_lm_params, terminal_lm_params_units = \
        make_augmented_cost(terminal_cost, cost_unit, constraints, constraints_units, location='terminal')

    hamiltonian_function, hamiltonian_units, costates, costates_units = \
        make_hamiltonian(states, states_rates, states_units, path_cost, cost_unit)

    bvp = BVP()

    if method == 'indirect':
        costates_rates = make_costate_rates(hamiltonian_function, states, costates, total_derivative)
    elif method == 'diffyg':
        omega = make_standard_symplectic_form(states, costates)
        ocp.omega(omega)
        X_H = make_hamiltonian_vector_field(hamiltonian_function, omega, states + costates, total_derivative)
        n = len(states)
        costates_rates = X_H[-n:]
        bvp.omega(omega)

    for ii, s in enumerate(states + costates):
        _eom = (states_rates + costates_rates)[ii]
        _unit = (states_units + costates_units)[ii]
        bvp.state(s, _eom, _unit)

    coparameters = make_costate_names(parameters)
    coparameters_units = [cost_unit / parameter_units for parameter_units in parameters_units]
    coparameters_rates = make_costate_rates(hamiltonian_function, parameters, coparameters, total_derivative)

    d = []
    for ii in range(len(coparameters)):
        if ocp.parameters()[ii]['noquad'] is True:
            d += [ii]

    coparameters = [p for ii, p in enumerate(coparameters) if ii not in d]
    coparameters_rates = [p for ii, p in enumerate(coparameters_rates) if ii not in d]
    coparameters_units = [p for ii, p in enumerate(coparameters_units) if ii not in d]

    initial_bc = make_boundary_conditions(
        constraints, states, costates, parameters, coparameters,
        augmented_initial_cost, total_derivative, location='initial')

    terminal_bc = make_boundary_conditions(
        constraints, states, costates, parameters, coparameters,
        augmented_terminal_cost, total_derivative, location='terminal')

    constraints['terminal'] += [bc[0] for bc in terminal_bcs_time]
    terminal_bc += [bc[0] for bc in terminal_bcs_time]
    constraints_units['terminal'] += [bc[1] for bc in terminal_bcs_time]

    # TODO: Hardcoded handling of time bc. I should fix this sometime.
    time_bc = make_time_bc(constraints, total_derivative, hamiltonian_function, independent_variable)

    # if method.lower() == 'diffyg':
    # breakpoint()
    # time_bc = total_derivative(time_bc, ocp.parameters()[-1]['symbol']) + 1

    if time_bc is not None:
        terminal_bc += [time_bc]

    bvp.constant_of_motion('hamiltonian', hamiltonian_function, hamiltonian_units)

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

    def gamma_map(gamma, _compute_control=None, ndp=len(initial_lm_params + terminal_lm_params)):
        gamma = copy.deepcopy(gamma)
        gamma.y = np.column_stack((gamma.y, gamma.dual))
        gamma.dual = np.array([])
        gamma.nondynamical_parameters = np.hstack((gamma.nondynamical_parameters, np.ones(ndp)))
        return gamma

    def gamma_map_inverse(gamma, _compute_control=None, n=n_states, ndp=len(initial_lm_params + terminal_lm_params)):
        gamma = copy.deepcopy(gamma)
        gamma.dual = gamma.y[:, -n:]
        gamma.y = gamma.y[:, :n]
        gamma.nondynamical_parameters = gamma.nondynamical_parameters[:-ndp]
        return gamma

    return bvp, gamma_map, gamma_map_inverse


def F_PMP(bvp):
    r"""

    :param bvp:
    :return:
    """
    bvp = copy.deepcopy(bvp)

    dHdu = make_dhdu(bvp.constants_of_motion()[0]['function'], bvp.controls(), total_derivative)
    control_law = make_control_law(dHdu, [u['symbol'] for u in bvp.controls()])
    bvp._control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]

    def gamma_map(gamma, _compute_control=None):
        gamma = copy.deepcopy(gamma)
        return gamma

    def gamma_map_inverse(gamma, _compute_control=None):
        gamma = copy.deepcopy(gamma)

        u = np.array([_compute_control(gamma.y[0], [], np.hstack((gamma.dynamical_parameters, gamma.t[-1])), gamma.const)])
        for ii in range(len(gamma.t)-1):
            u = np.vstack((u, _compute_control(gamma.y[ii+1], [], np.hstack((gamma.dynamical_parameters, gamma.t[-1])), gamma.const)))

        gamma.u = u
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

    dHdu = make_dhdu(bvp.constants_of_motion()[0]['function'], bvp.controls(), total_derivative)
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
        cost_unit = bvp.constants_of_motion()[0]['unit']
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
        X_H = make_hamiltonian_vector_field(bvp.constants_of_motion()[0]['function'], bvp.the_omega(), basis, total_derivative)

        for ii, s in enumerate(bvp.states()):
            s['eom'] = X_H[ii]

        for ii, lU in enumerate(lamU):
            bvp.initial_bc(lU)

    for ii, s in enumerate(dae_bc):
        bvp.terminal_bc(s)

    del bvp._properties['controls']
    bvp._control_law = []

    def gamma_map(gamma, _compute_control=None, n=n_states, m=n_controls, method=method):
        gamma = copy.deepcopy(gamma)
        if len(gamma.dual_u) == 0:
            gamma.dual_u = np.zeros_like(gamma.u)

        if method == 'indirect':
            gamma.y = np.column_stack((gamma.y[:, :int(n / 2)], gamma.u, gamma.y[:, -int(n / 2):]))
        elif method == 'diffyg':
            gamma.y = np.column_stack((gamma.y[:, :int(n / 2)], gamma.u, gamma.y[:, -int(n / 2):], gamma.dual_u))
        gamma.u = np.array([]).reshape((n, 0))
        return gamma

    def gamma_map_inverse(gamma, _compute_control=None, n=n_states, m=n_controls, method=method):
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
