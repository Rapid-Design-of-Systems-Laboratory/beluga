"""
Base functions required by all optimization methods.
"""


from beluga.utils import sympify, sympify2, keyboard
from beluga.problem import SymVar
import sympy
import functools as ft
import itertools as it
import simplepipe as sp
import re as _re
from beluga.problem import SymVar
import logging
import numpy as np
import sympy as sym


def add_equality_constraints(hamiltonian, equality_constraints):
    r"""
    Adjoins equality constraints to a Hamiltonian function.

    .. math::
        \begin{aligned}
            \text{add_equality_constraints} : C^\infty(M) &\rightarrow C^\infty(M) \\
            (H, f) &\mapsto H + \mu_i f_i \; \forall \; i \in f
        \end{aligned}

    :param ham: A Hamiltonian function, :math:`H`.
    :param equality_constraints: List of equality constraints, :math:`f`.
    :return: Augmented Hamiltonian function.
    """
    # Adjoin equality constraints
    for i in range(len(equality_constraints)):
        hamiltonian += sympify('mu'+str(i+1)) * (sympify2(equality_constraints[i].expr))

    return hamiltonian


def get_satfn(var, ubound=None, lbound=None, slopeAtZero=1):
    """
    Documentation needed.

    :param var:
    :param ubound:
    :param lbound:
    :param slopeAtZero:
    :return:
    """

    # var -> variable inside saturation function
    if ubound is None and lbound is None:
        raise ValueError('At least one bound should be specified for the constraint.')
    if ubound == lbound:
        raise ValueError('The upper and lower bounds should be different.')

    # Symmetric bounds
    if ubound is None:
        # Return lower bound sat fn
        #ubound = -lbound
        satfcn = lbound + sym.exp(var)
        print('Using one-sided saturation function', satfcn)
        return satfcn
    elif lbound is None:
        # Return upper bound sat fn
        satfcn = ubound - sym.exp(-var)
        print('Using one-sided saturation function', satfcn)
        return satfcn
    else:
        s = 4*slopeAtZero/(ubound - lbound)
        print('Using two sided saturation function')
        return ubound - (ubound - lbound)/(1 + sym.exp(s*var))


def init_workspace(ocp, guess):
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
    # sort_map = [i[0] for i in sorted(enumerate(ocp.constants()), key=lambda x:x[1]['name'])]
    # workspace['constants'] = [SymVar(ocp.constants()[k]) for k in sort_map]
    workspace['constants'] = [SymVar(k) for k in ocp.constants()]

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


# TODO: Check if this function is ever used. I don't think it's needed.
def jacobian(expr_list, var_list, derivative_fn):
    r"""
    Returns a Jacobian matrix for a given set of functions and variables.

    .. math::
        \begin{aligned}
            \text{jacobian} : \Gamma^1(M) &\rightarrow \Gamma^2(M) \\
            (f, x, d) &\mapsto J_{ij} = d_{x_j} f_i \; \forall \; i,j
        \end{aligned}

    :param expr_list: List of expressions to take the partials of, :math:`f`.
    :param var_list: List of variables to take the partials with respect to, :math:`x`.
    :param derivative_fn: Derivative function, :math:`d`
    :return: The Jacobian matrix, :math:`J_{ij}`.
    """

    jac = sympy.zeros(len(expr_list), len(var_list))
    for i, expr in enumerate(expr_list):
        for j, var in enumerate(var_list):
            jac[i, j] = derivative_fn(expr, var)
    return jac


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
    """
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


def make_bc_mask(states, controls, mu_vars, cost, aug_cost, derivative_fn):

    """Creates mask marking free and bound variables at t=0

    free = 1, constrained = 0
    """
    aug_cost_expr = (aug_cost.expr - cost.expr)

    state_mask = []
    costate_mask = []
    for state in states:
        if derivative_fn(aug_cost_expr, state) == 0:
            # State not constrained -> costate = 0
            state_mask.append(1)    # State free
            costate_mask.append(0)  # Costate fixed
        else:
            state_mask.append(0)    # State constrained
            costate_mask.append(1)  # Costate free

    return state_mask+costate_mask+[1]*(len(controls)+len(mu_vars)+1)  # Add tf as free param


def make_boundary_conditions(constraints, constraints_adjoined, states, costates, cost, derivative_fn, location,
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
    if constraints_adjoined:
        bc_list += [str(costate - derivative_fn(cost_expr, state)) for state, costate in zip(states, costates)]
    else:
        refd = [sum(derivative_fn(c, s) for c in constraints[location]) for s in states]
        bc_list += [str(costate - derivative_fn(cost_expr, state)) for i, (state, costate) in enumerate(zip(states,costates)) if refd[i] == False]

    return bc_list


def make_constrained_arc_fns(workspace):
    """
    Creates constrained arc control functions.

    :param workspace:
    :return:
    """
    controls = workspace['controls']
    constants = workspace['constants']
    states = workspace['states']
    costates = workspace['costates']
    parameters = workspace['parameters']
    quantity_vars = workspace['quantity_vars']
    fn_args_lamdot = [list(it.chain(states, costates)), parameters, constants, controls]
    # control_fns = [workspace['control_fn']]
    tf_var = sympify('tf')
    costate_eoms = [ {'eom':[str(_.eom*tf_var) for _ in workspace['costates']], 'arctype':0} ]
    bc_list = [] # Unconstrained arc placeholder

    mu_vars = workspace['mu_vars']


    for arc_type, s in enumerate(workspace['s_list'],1):
        pi_list = [str(_) for _ in s['pi_list']]


        costate_eom = {'eom':[str(_.eom*tf_var) for _ in s['lamdot']],
                       'arctype':arc_type,
                       'pi_list': pi_list}

        entry_bc, exit_bc = make_constraint_bc(s,
                                workspace['states'],
                                workspace['costates'],
                                workspace['parameters'],
                                workspace['constants'],
                                workspace['controls'], mu_vars, workspace['quantity_vars'], workspace['ham'])
        bc = {'entry_bc': entry_bc,
              'exit_bc': exit_bc,
              'arctype': arc_type,
              'pi_list': pi_list,
              'name': s['name']}
        bc_list.append(bc)

        # control_fns.append(u_fn)
        costate_eoms.append(costate_eom)

    # yield control_fns
    yield costate_eoms
    yield bc_list


def make_constraint_bc(s, states, costates, parameters, constants, controls, mu_vars, quantity_vars, ham):
    """
    Documentation needed.

    :param s:
    :param states:
    :param costates:
    :param parameters:
    :param constants:
    :param controls:
    :param mu_vars:
    :param quantity_vars:
    :param ham:
    :return:
    """
    num_states = len(states)
    costate_slice = slice(num_states, 2*num_states)
    ham_aug = s['ham']
    corner_conditions = s['corner']
    tangency = s['tangency']
    tf_var = sympify('tf')

    y1m = sympy.symbols(' '.join('_'+str(_.name)+'_1m' for _ in it.chain(states, costates, [tf_var])))
    y1m_x = sympy.Matrix([y1m[:num_states]])
    y1m_l = sympy.Matrix([y1m[costate_slice]])

    y1p = sympy.symbols(' '.join('_'+str(_.name)+'_1p' for _ in it.chain(states, costates, [tf_var])))
    y1p_x = sympy.Matrix([y1p[:num_states]])
    y1p_l = sympy.Matrix([y1p[costate_slice]])

    y2m = sympy.symbols(' '.join('_'+str(_.name)+'_2m' for _ in it.chain(states, costates, [tf_var])))
    y2p = sympy.symbols(' '.join('_'+str(_.name)+'_2p' for _ in it.chain(states, costates, [tf_var])))
    y2m = sympy.Matrix([y2m])
    y2p = sympy.Matrix([y2p])

    u_m = sympy.symbols(' '.join('_'+str(_.name)+'_m' for _ in it.chain(controls, mu_vars)))
    u_p = sympy.symbols(' '.join('_'+str(_.name)+'_p' for _ in it.chain(controls, mu_vars)))
    if not hasattr(u_m, '__len__'):
        u_m = (u_m,)
    if not hasattr(u_p, '__len__'):
        u_m = (u_p,)
    def make_subs(in_vars, out_vars):
        return {k: v for k,v in zip(in_vars, out_vars)}

    subs_1m = make_subs(it.chain(states, costates, [tf_var], controls, mu_vars), it.chain(y1m, u_m))
    subs_1p = make_subs(it.chain(states, costates, [tf_var], controls, mu_vars), it.chain(y1p, u_p))
    subs_2m = make_subs(it.chain(states, costates, [tf_var], controls, mu_vars), it.chain(y2m, u_m))
    subs_2p = make_subs(it.chain(states, costates, [tf_var], controls, mu_vars), it.chain(y2p, u_p))

    ham1m = ham.subs(quantity_vars).subs(subs_1m)
    ham1p = ham_aug.subs(quantity_vars).subs(subs_1p)
    ham2m = ham_aug.subs(quantity_vars).subs(subs_2m)
    ham2p = ham.subs(quantity_vars).subs(subs_2p)
    tangency_1m = sympy.Matrix(tangency).subs(subs_1p)

    entry_bc = [
        *tangency_1m,  # Tangency conditions, N(x,t) = 0
        *(y1m_x - y1p_x), # Continuity in states at entry
        *(y1m_l - y1p_l - corner_conditions.subs(subs_1p)), # Corner condns on costates
        ham1m - ham1p
    ]
    exit_bc = [
        *(y2m - y2p)[:-1], # Continuity in states and costates at exit (excluding tf)
        ham2m - ham2p
    ]
    # bc_arc = [*tangency_1m,  # Tangency conditions, N(x,t) = 0
    #           *(y1m_x - y1p_x), # Continuity in states at entry
    #           *(y1m_l - y1p_l - corner_conditions), # Corner condns on costates
    #
    #           ham1m - ham1p,
    #           ham2m - ham2p]

    entry_bc = [str(_) for _ in entry_bc]
    exit_bc = [str(_) for _ in exit_bc]
    return entry_bc, exit_bc


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

    dhdu = []
    for ctrl in controls:
        dHdu = derivative_fn(ham, ctrl)
        custom_diff = dHdu.atoms(sympy.Derivative)
        # Substitute "Derivative" with complex step derivative
        repl = {(d, im(f.func(v+1j*1e-30))/1e-30) for d in custom_diff
                    for f,v in zip(d.atoms(sympy.AppliedUndef), d.atoms(Symbol))}

        dhdu.append(dHdu.subs(repl))

    return dhdu


def make_ham_lamdot_with_eq_constraint(states, constraints, path_cost, derivative_fn):
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
    ham = add_equality_constraints(ham, constraints.get('equality', []))
    yield ham
    yield make_costate_rates(ham, states, costate_names, derivative_fn)


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


def process_path_constraints(workspace):
    """
    Documentation needed.

    :param workspace:
    :return:
    """
    states = workspace['states']
    controls = workspace['controls']
    constants = workspace['constants']
    constraints = workspace['constraints']
    derivative_fn = workspace['derivative_fn']
    quantity_vars = workspace['quantity_vars']
    quantity_list = workspace['quantity_list']

    path_cost_expr = workspace['path_cost'].expr
    path_cost_unit = workspace['path_cost'].unit
    if path_cost_expr == 0:
        logging.debug('No path cost specified, using unit from terminal cost function')
        path_cost_expr = None
        path_cost_unit = workspace['terminal_cost'].unit

    logging.debug('Path cost is of unit: '+str(path_cost_unit))
    time_unit = workspace['indep_var'].unit
    path_constraints = workspace['path_constraints']

    eq = constraints.get('equality', [])
    xi_init_vals = []
    for (ind, c) in enumerate(path_constraints):
        # Determine order of constraint
        logging.debug('Processing path constraint: '+str(c.name))
        order = 0
        cq = [c.expr]
        dxdt = [state.eom for state in states]

        # Zeroth order constraints have no 'xi' state
        xi_vars = []
        h = []
        while True:
            control_found = False
            for u in controls:
                if u in cq[-1].subs(quantity_vars).atoms():
                    logging.info('Constraint is of order '+str(order))
                    control_found = True
                    break
            if control_found:
                break

            dcdx = [derivative_fn(cq[-1], state) for state in states]

            # Chain rule (Assume there is no explciit time-dependence) to find dcdt
            cq.append(sum(d1*d2 for d1,d2 in zip(dcdx, dxdt)))
            order = order + 1

            # Create the auxiliary state variables
            xi_vars.append(sym.Symbol('xi'+str(ind+1)+str(order)))

        # Create the smoothing control variable
        xi_vars.append(sym.Symbol('ue'+str(ind+1)))

        # TODO: Fix constraint object to accept two limits
        c_limit = sym.sympify(c.bound)
        if c_limit.is_Number:
            # TODO: Allow continuation on constraints
            # Define new hidden constant
            c_limit = sympify('_'+str(c.name))
            constants.append(SymVar({'name': str(c_limit), 'value': float(c.bound), 'unit': c.unit}))
            logging.debug('Added constant '+str(c_limit))

        c_lbound = c_ubound = None
        if c.direction == '>':
            c_lbound = c_limit
        elif c.direction == '<':
            c_ubound = c_limit
        elif c.direction == '<>':
            c_ubound = c_limit
            c_lbound = -c_limit
        else:
            raise ValueError('Invalid direction specified for constraint')

        psi = get_satfn(xi_vars[0], ubound=c_ubound, lbound=c_lbound, slopeAtZero=1)
        psi_vars = [(sympify2('psi'+str(ind+1)+'0('+str(xi_vars[0])+')'), psi)]

        # Add to quantity list
        quantity_vars['psi'+str(ind+1)+'0'] = str(psi)
        quantity_list.append({'name':('psi'+str(ind+1)+'0'), 'expr':str(psi)})

        # m-th order constraint needs up to m-th derivative of psi to be defined
        psi_i = psi
        psi_vars_deriv = []
        psi_var_func = [(psi_vars[0][0], sym.Symbol('psi'+str(ind+1)+'0'))]
        for i in range(order):

            psi_i = derivative_fn(psi_i, xi_vars[0])
            # psi_vars.append((Symbol('psi'+str(ind+1)+str(i+1)+'('+str(xi_vars[0])+')'), psi_i))
            current_psi_var = sym.Symbol('psi'+str(ind+1)+str(i+1))
            current_psi_var_func = sympify2(str(current_psi_var)+'('+str(xi_vars[0])+')')
            psi_vars.append((current_psi_var, psi_i))
            psi_var_func.append((current_psi_var_func, current_psi_var))
            psi_vars_deriv.append((sympify2('Derivative(psi'+str(ind+1)+str(i)+'('+str(xi_vars[0])+'), '+str(xi_vars[0])+')'),
                                   current_psi_var_func))
            quantity_vars[str(current_psi_var)] = str(psi_i)
            quantity_list.append({'name':str(current_psi_var), 'expr':str(psi_i)})

        # psi_vars = psi_vars + []
        # psi_var_sub = [(v,k) for k,v in psi_vars]

        # FIXME: Hardcoded h derivatives for now
        # h = [psi_vars[0][0]]
        # h.append(psi_vars[1][0]*xi_vars[1]) # psi'*xi12
        # h.append(psi_vars[2][0]*xi_vars[1] + psi_vars[1][0]*xi_vars[2]) # psi''*xi12 + psi'*xi13
        # psi'''*xi12 + xi13*psi12'' + psi12*xi13 + psi11*ue1
        # h.append(psi_vars[3][0]*xi_vars[1] + 2 * psi_vars[2][0]*xi_vars[2] + psi_vars[1][0]*xi_vars[3] )

        #TODO: Hardcoded 't' as independent variable with unit of 's'
        # c_vals = [80e3, -5000, 9.539074102210087] # third number is vdot at zero approx
        c_vals = np.ones(order)*0.1
        h = [psi_vars[0][0]]

        for i in range(order):
            # Add 'xi' state
            states.append(SymVar({'name':str(xi_vars[i]), 'eom':str(xi_vars[i+1]), 'unit':(c.unit/(time_unit**i))}))
            # Constraint all cq at initial point (forms constraints for xi_ij)
            # ocp.constraints().initial(str(cq[i] - h[i]),'('+c.unit+')/s^('+str(i)+')')
            constraints['terminal'].append(SymVar({'expr':str(cq[i] - h[i].subs(psi_var_func)), 'unit':c.unit/(time_unit**i)}, sym_key='expr'))

            # Add to initial guess vector
            print('Adding {} = {}'.format(xi_vars[i], c_vals[i]))
            xi_init_vals.append(c_vals[i])

            dhdxi = [derivative_fn(h[i], xi_v).subs(psi_vars_deriv) for xi_v in xi_vars[:-1]]
            dhdt  = sum(d1*d2 for d1,d2 in zip(dhdxi,xi_vars[1:])) # xi11dot = xi12 etc.
            # dhdt = dhdt.subs(psi_var_sub)
            h.append(dhdt)

        h = [h_i.subs(psi_var_func) for h_i in h]
        # Add the smoothing control with the right unit
        ue_unit = c.unit/(time_unit**order)
        controls.append(SymVar({'name':str(xi_vars[-1]), 'unit':str(ue_unit)}))

        logging.debug('Adding control '+str(xi_vars[-1])+' with unit '+str(ue_unit))

        # Add equality constraint
        cqi_unit = ue_unit*time_unit
        # ocp.constraints().equality(str(cq[-1] - h[-1]),str(cqi_unit))

        eq.append(SymVar({'type':'equality', 'expr':str(cq[-1] - h[-1]), 'unit':str(cqi_unit), 'name':'_eq_'+str(ind)}))

        # Add smoothing factor
        eps_const = sympify('eps_'+str(c.name))
        eps_unit = (path_cost_unit/ue_unit**2)/time_unit #Unit of integrand
        eps_unit = sym.Symbol('nd')
        if not c.start_eps:
            c.start_eps = 1
        constants.append(SymVar({'name':eps_const, 'value': c.start_eps, 'unit':str(eps_unit)}))
        logging.debug('Adding smoothing factor '+str(eps_const)+' with unit '+str(eps_unit))

        # Append new control to path cost
        if path_cost_expr is None:
            path_cost_expr = eps_const*xi_vars[-1]**2
        else:
            path_cost_expr = path_cost_expr + eps_const*xi_vars[-1]**2

    constraints['equality'] = eq
    if path_cost_expr is not None:
        logging.debug('Updated path cost is: '+str(path_cost_expr))
        path_cost = SymVar({'expr': path_cost_expr, 'unit':path_cost_unit}, sym_key='expr')
    else:
        path_cost = SymVar({'expr': '0', 'unit':path_cost_unit}, sym_key='expr')
    derivative_fn = ft.partial(total_derivative, dependent_vars=quantity_vars)
    jacobian_fn = ft.partial(jacobian, derivative_fn=derivative_fn)

    s_list = []
    mu_vars = []

    yield states
    yield controls
    yield constants
    yield constraints
    yield path_cost
    yield s_list
    yield mu_vars
    yield xi_init_vals
    yield derivative_fn
    yield jacobian_fn


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


BaseWorkflow = sp.Workflow([
    sp.Task(init_workspace, inputs=('problem','guess'), outputs='*'),
    sp.Task(process_quantities,
            inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn', 'jacobian_fn')),
    sp.Task(process_path_constraints, inputs='*',
            outputs=('states', 'controls', 'constants', 'constraints', 'path_cost', 's_list', 'mu_vars', 'xi_init_vals', 'derivative_fn', 'jacobian_fn')),
    sp.Task(ft.partial(make_augmented_cost, location='initial'),
            inputs=('initial_cost', 'constraints', 'constraints_adjoined'),
            outputs=('aug_initial_cost')),
    sp.Task(ft.partial(make_augmented_params, location='initial'),
            inputs=('constraints', 'constraints_adjoined'),
            outputs=('initial_lm_params')),
    sp.Task(ft.partial(make_augmented_cost, location='terminal'),
            inputs=('terminal_cost', 'constraints', 'constraints_adjoined'),
            outputs=('aug_terminal_cost')),
    sp.Task(ft.partial(make_augmented_params, location='terminal'),
            inputs=('constraints', 'constraints_adjoined'),
            outputs=('terminal_lm_params')),
    # sp.Task(make_costate_names,
    #         inputs=('states'),
    #         outputs=('costate_names')),
    sp.Task(make_ham_lamdot_with_eq_constraint,
            inputs=('states', 'constraints', 'path_cost', 'derivative_fn'),
            outputs=('ham', 'costates')),
    sp.Task(ft.partial(make_boundary_conditions, location='initial'),
            inputs=('constraints', 'constraints_adjoined', 'states', 'costates', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_initial')),
    sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
            inputs=('constraints', 'constraints_adjoined', 'states', 'costates', 'aug_terminal_cost', 'derivative_fn'),
            outputs=('bc_terminal')),
    sp.Task(make_time_bc, inputs=('constraints', 'bc_terminal'), outputs=('bc_terminal')),
    sp.Task(make_dhdu,
            inputs=('ham', 'controls', 'derivative_fn'),
            outputs=('dhdu')),
    sp.Task(make_parameters, inputs=['initial_lm_params', 'terminal_lm_params', 's_list'],
            outputs='parameters'),
    sp.Task(make_bc_mask,
            inputs=('states', 'controls', 'mu_vars', 'initial_cost', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_free_mask')),
    sp.Task(make_constrained_arc_fns, inputs='*', outputs=['costate_eoms', 'bc_list'])])
