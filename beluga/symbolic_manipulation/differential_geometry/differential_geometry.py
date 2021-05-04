"""
Base functions shared by all symbolic_manipulation methods.
"""

import numpy as np
import sympy


# TODO Implement Full Units Check

def exterior_derivative(f, basis):

    r"""

    :param f:
    :param basis:
    :return:
    """

    df = None

    # Handle the (0)-grade case
    if isinstance(f, sympy.Expr):
        n = len(basis)
        df = [0]*len(basis)
        for ii in range(n):
            df[ii] = sympy.diff(f, basis[ii])
        df = sympy.MutableDenseNDimArray(df)

    # Handle the (1+)-grade cases
    if isinstance(f, sympy.Array) or isinstance(f, sympy.Matrix) or isinstance(f, sympy.MutableDenseNDimArray):
        n = (len(basis),) + f.shape
        df = sympy.MutableDenseNDimArray(sympy.zeros(*n))
        if len(n) == 2:
            for ii in range(df.shape[0]):
                for jj in range(df.shape[1]):
                    if ii == jj:
                        df[ii, jj] = 0

                    if ii < jj:
                        df[ii, jj] += sympy.diff(f[jj], basis[ii])
                        df[ii, jj] += -sympy.diff(f[ii], basis[jj])
                        df[jj, ii] += -sympy.diff(f[jj], basis[ii])
                        df[jj, ii] += sympy.diff(f[ii], basis[jj])

        # TODO Check if this is valid statement
        if len(n) > 2:
            raise NotImplementedError('Grade greater than 2 not implemeted')

    return df


def make_hamiltonian_vector_field(hamiltonian, omega, basis):
    r"""
    Makes a Hamiltonian vector field.


    :return: :math:`\X_H`, the Hamiltonian vector field.

    """
    if omega.shape[0] != omega.shape[1]:
        raise ValueError('omega must be square.')

    if omega.shape[0] % 2 != 0:
        raise ValueError('omega must be even-dimensional.')

    dh = exterior_derivative(hamiltonian, basis)
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


def total_derivative(expr, var, dependent_vars=None):
    """
    Take derivative taking pre-defined quantities into consideration

    :param expr: NamedExpression to evaluate the derivative of.
    :param var: Variable to take the derivative with respect to.
    :param dependent_vars: Other dependent variables to consider with chain rule.
    """
    if dependent_vars is None:
        dependent_vars = {}

    dep_var_names = dependent_vars.keys()
    dep_var_expr = [expr for (_, expr) in dependent_vars.items()]

    dfdq = [expr.diff(dep_var).subs_self(dependent_vars.items()) for dep_var in dep_var_names]
    dqdx = [qexpr.diff(var) for qexpr in dep_var_expr]
    out = sum(d1 * d2 for d1, d2 in zip(dfdq, dqdx)) + sympy.diff(expr, var)
    return out


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


def pb(f, g, prob):
    r"""

    :param f:
    :param g:
    :param prob:
    :return:
    """
    if f is None and g is not None:
        omega = prob.omega.tomatrix()
        h = sympy.MutableDenseNDimArray([0] * omega.shape[0])
        for i, states_i in enumerate(prob.states + prob.costates):
            for j, states_j in enumerate(prob.states + prob.costates):
                h[(i,)] += omega[i, j]*total_derivative(g.expr, states_j.sym)

        return h
    raise NotImplementedError


# TODO Check this
def noether(prob, quantity):
    r"""

    :param prob:
    :param quantity:
    :return:
    """
    if not is_symplectic(prob.omega):
        raise ValueError('Can\'t use Noether\'. System does not appear to be symplectic.')

    if hasattr(quantity, 'field'):
        is_symmetry = True
    else:
        is_symmetry = False

    if is_symmetry:
        omega = prob.omega.tomatrix()
        chi = sympy.Matrix(quantity.field)
        omega_chi = omega.LUsolve(chi)
        gstar = 0
        for jj, state in enumerate(prob.states + prob.costates):
            gstar += sympy.integrate(omega_chi[jj], state.sym)

        unit = prob.constants_of_motion[0].units / quantity.units

        return gstar, unit

    if not is_symmetry:
        g = pb(None, quantity, prob)
        nonz = np.nonzero(g)
        if len(nonz) == 1:
            unit = prob.states[nonz[0][0]].units
        else:
            raise NotImplementedError

        return g, unit


# def F_MF(prob, com_index):
#     r"""
#
#     :param prob:
#     :param com_index:
#     :return:
#     """
#     prob = copy.deepcopy(prob)
#     # hamiltonian = prob.get_constants_of_motion()[0]['function']
#     # O = prob.the_omega()
#     # X_H = make_hamiltonian_vector_field(hamiltonian, O, [s['symbol'] for s in prob.states()], total_derivative)
#
#     com = prob.get_constants_of_motion()[com_index]
#
#     # states = [str(s['symbol']) for s in prob.states()]
#     # parameters = [str(s['symbol']) for s in prob.parameters()]
#     # constants = [str(s['symbol']) for s in prob.get_constants()]
#     # fn_p = make_jit_fn(states + parameters + constants, str(com['function']))
#
#     states = [(s['symbol']) for s in prob.states()]
#     parameters = [(s['symbol']) for s in prob.parameters()]
#     constants = [(s['symbol']) for s in prob.get_constants()]
#     fn_p = jit_lambdify([states, parameters, constants], com['function'])
#
#     atoms = com['function'].atoms()
#     atoms2 = set()
#     for a in atoms:
#         if isinstance(a, Symbol) and (a not in {s['symbol'] for s in prob.parameters() + prob.get_constants()}):
#             atoms2.add(a)
#
#     atoms = atoms2
#
#     solve_for_p = sympy.solve(com['function'] - com['symbol'], atoms, dict=True, simplify=False)
#
#     if len(solve_for_p) > 1:
#         raise ValueError
#
#     for parameter in solve_for_p[0].keys():
#         the_symmetry, symmetry_unit = noether(prob, com)
#         replace_p = parameter
#         for ii, s in enumerate(prob.states()):
#             if s['symbol'] == parameter:
#                 parameter_index = ii
#                 prob.parameter(com['symbol'], com['unit'])
#
#     symmetry_index = parameter_index - int(len(prob.states())/2)
#
#     # Derive the quad
#     # Evaluate int(pdq) = int(PdQ)
#     n = len(prob.quads())
#     symmetry_symbol = Symbol('_q' + str(n))
#     _lhs = com['function']/com['symbol']*the_symmetry
#     lhs = 0
#     for ii, s in enumerate(prob.states()):
#         lhs += sympy.integrate(_lhs[ii], s['symbol'])
#
#     lhs, _ = recursive_sub(lhs, solve_for_p[0])
#
#     # states = [str(s['symbol']) for s in prob.states()]
#     # parameters = [str(s['symbol']) for s in prob.parameters()]
#     # constants = [str(s['symbol']) for s in prob.get_constants()]
#     # the_p = [str(com['symbol'])]
#     # fn_q = make_jit_fn(states + parameters + constants, str(lhs))
#
#     states = [s['symbol'] for s in prob.states()]
#     parameters = [s['symbol'] for s in prob.parameters()]
#     constants = [s['symbol'] for s in prob.get_constants()]
#     the_p = [com['symbol']]
#     fn_q = jit_lambdify([states, parameters, constants], lhs)
#
#     replace_q = prob.states()[symmetry_index]['symbol']
#     solve_for_q = sympy.solve(lhs - symmetry_symbol, replace_q, dict=True, simplify=False)
#
#     # Evaluate X_H(pi(., c)), pi = O^sharp
#     O = prob.the_omega().tomatrix()
#     rvec = sympy.Matrix(([0]*len(prob.states())))
#     for ii, s1 in enumerate(prob.states()):
#         for jj, s2 in enumerate(prob.states()):
#             rvec[ii] += O[ii,jj]*total_derivative(com['function'], s2['symbol'])
#
#     symmetry_eom = 0
#     for ii, s in enumerate(prob.states()):
#         symmetry_eom += s['eom']*rvec[ii]
#
#     # TODO: Figure out how to find units of the quads. This is only works in some specialized cases.
#     symmetry_unit = prob.states()[symmetry_index]['unit']
#
#     prob.quad(symmetry_symbol, symmetry_eom, symmetry_unit)
#
#     for ii, s in enumerate(prob.states()):
#         s['eom'], _ = recursive_sub(s['eom'], solve_for_p[0])
#         s['eom'], _ = recursive_sub(s['eom'], solve_for_q[0])
#
#     for ii, s in enumerate(prob.all_bcs()):
#         s['function'], _ = recursive_sub(s['function'], solve_for_p[0])
#         s['function'], _ = recursive_sub(s['function'], solve_for_q[0])
#
#     for ii, law in enumerate(prob._control_law):
#         for jj, symbol in enumerate(law.keys()):
#             prob._control_law[ii][symbol], _ = recursive_sub(sympify(prob._control_law[ii][symbol]), solve_for_p[0])
#             prob._control_law[ii][symbol] = str(prob._control_law[ii][symbol])
#             prob._control_law[ii][symbol], _ = recursive_sub(sympify(prob._control_law[ii][symbol]), solve_for_q[0])
#             prob._control_law[ii][symbol] = str(prob._control_law[ii][symbol])
#
#     for ii, s in enumerate(prob.get_constants_of_motion()):
#         if ii != com_index:
#             s['function'], _ = recursive_sub(s['function'], solve_for_p[0])
#             s['function'], _ = recursive_sub(s['function'], solve_for_q[0])
#
#     O = prob.the_omega().tomatrix()
#     if parameter_index > symmetry_index:
#         del prob.states()[parameter_index]
#         del prob.states()[symmetry_index]
#         O.row_del(parameter_index)
#         O.col_del(parameter_index)
#         O.row_del(symmetry_index)
#         O.col_del(symmetry_index)
#     else:
#         del prob.states()[symmetry_index]
#         del prob.states()[parameter_index]
#         O.row_del(symmetry_index)
#         O.col_del(symmetry_index)
#         O.row_del(parameter_index)
#         O.col_del(parameter_index)
#
#     prob.omega(sympy.MutableDenseNDimArray(O))
#
#     del prob.get_constants_of_motion()[com_index]
#
#     # states = [str(s['symbol']) for s in prob.states()]
#     # quads = [str(s['symbol']) for s in prob.quads()]
#     # parameters = [str(s['symbol']) for s in prob.parameters()]
#     # constants = [str(s['symbol']) for s in prob.get_constants()]
#     # fn_q_inv = make_jit_fn(states + quads + parameters + constants, str(solve_for_q[0][replace_q]))
#
#     states = [s['symbol'] for s in prob.states()]
#     quads = [s['symbol'] for s in prob.quads()]
#     parameters = [s['symbol'] for s in prob.parameters()]
#     constants = [s['symbol'] for s in prob.get_constants()]
#     fn_q_inv = jit_lambdify([states, quads, parameters, constants], solve_for_q[0][replace_q])
#
#     fn_p_inv = jit_lambdify([states, parameters, constants], solve_for_p[0][replace_p])
#
#     def gamma_map(gamma, parameter_index=parameter_index, symmetry_index=symmetry_index, fn_q=fn_q, fn_p=fn_p):
#         gamma = copy.deepcopy(gamma)
#         cval = fn_p(gamma.y[0], gamma.p, gamma.const)
#         qval = np.ones_like(gamma.t)
#         gamma.p = np.hstack((gamma.p, cval))
#         for ii, t in enumerate(gamma.t):
#             qval[ii] = fn_q(gamma.y[ii], gamma.p, gamma.const)
#
#         if parameter_index > symmetry_index:
#             gamma.y = np.delete(gamma.y, np.s_[parameter_index], axis=1)
#             gamma.y = np.delete(gamma.y, np.s_[symmetry_index], axis=1)
#         else:
#             gamma.y = np.delete(gamma.y, np.s_[symmetry_index], axis=1)
#             gamma.y = np.delete(gamma.y, np.s_[parameter_index], axis=1)
#
#         gamma.q = np.column_stack((gamma.q, qval))
#         return gamma
#
#     def gamma_map_inverse(gamma, parameter_index=parameter_index, symmetry_index=symmetry_index, fn_q_inv=fn_q_inv, fn_p_inv=fn_p_inv):
#         gamma = copy.deepcopy(gamma)
#         qinv = np.ones_like(gamma.t)
#         pinv = np.ones_like(gamma.t)
#         for ii, t in enumerate(gamma.t):
#             qinv[ii] = fn_q_inv(gamma.y[ii], gamma.q[ii], gamma.p, gamma.const)
#             pinv[ii] = fn_p_inv(gamma.y[ii], gamma.p, gamma.const)
#         # breakpoint()
#         cval = gamma.p[-1]
#         state = np.ones_like(gamma.t)*cval
#         state = pinv
#         qval = qinv
#         if parameter_index > symmetry_index:
#             gamma.y = np.column_stack((gamma.y[:, :symmetry_index], qval, gamma.y[:, symmetry_index:]))
#             gamma.y = np.column_stack((gamma.y[:, :parameter_index], state, gamma.y[:, parameter_index:]))
#         else:
#             gamma.y = np.column_stack((gamma.y[:, :parameter_index], state, gamma.y[:, parameter_index:]))
#             gamma.y = np.column_stack((gamma.y[:, :symmetry_index], qval, gamma.y[:, symmetry_index:]))
#
#         gamma.q = np.delete(gamma.q, np.s_[-1], axis=1)
#         gamma.p = gamma.p[:-1]
#         return gamma
#
#     return prob, gamma_map, gamma_map_inverse
