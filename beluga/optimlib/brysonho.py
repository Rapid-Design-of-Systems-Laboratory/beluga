"""
Computes the necessary conditions of optimality using Bryson & Ho's method

[1] Bryson, Arthur Earl. Applied optimal control: optimization, estimation and control. CRC Press, 1975.
"""

import functools as ft
import itertools as it
import simplepipe as sp
import sympy
import re as _re
import numpy
np = numpy

from math import *
import numba

import beluga
from beluga.utils import sympify
from beluga.problem import SymVar

import sympy as sym
from sympy.utilities.lambdify import lambdastr
from beluga.utils import keyboard

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

def jacobian(expr_list, var_list, derivative_fn):
    jac = sympy.zeros(len(expr_list), len(var_list))
    for i, expr in enumerate(expr_list):
        for j, var in enumerate(var_list):
            jac[i, j] = derivative_fn(expr, var)
    return jac

def process_quantities(quantities):
    """Performs preprocessing on quantity definitions. Creates a new total
    derivative operator that takes considers these definitions.
    """
    # logging.info('Processing quantity expressions')

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

def make_augmented_cost(cost, constraints, location):
    """Augments the cost function with the given list of constraints.

    Returns the augmented cost function
    """

    def make_lagrange_mult(c, ind = 1):
        return sympify('lagrange_' + location + '_' + str(ind))
    lagrange_mult = [make_lagrange_mult(c, ind)
                     for (ind,c) in enumerate(constraints[location],1)]

    aug_cost_expr = cost.expr + sum(nu * c
                                    for (nu, c) in
                                    zip(lagrange_mult, constraints[location]))

    aug_cost = SymVar({'expr':aug_cost_expr, 'unit': cost.unit}, sym_key='expr')
    return aug_cost
    # yield aug_cost
    # yield lagrange_mult

def make_aug_params(constraints, location):
    """Make the lagrange multiplier terms for boundary conditions."""

    def make_lagrange_mult(c, ind = 1):
        return sympify('lagrange_' + location + '_' + str(ind))
    lagrange_mult = [make_lagrange_mult(c, ind)
                     for (ind,c) in enumerate(constraints[location],1)]
    return lagrange_mult


def make_hamiltonian_and_costate_rates(states, costate_names, path_cost, derivative_fn):
    """simplepipe task for creating the hamiltonian and costates

    Workspace variables
    -------------------
    states - list of dict
        List of "sympified" states

    path_cost - Object representing the path cost terminal

    Returns the hamiltonian and the list of costates
    """
    ham = path_cost.expr + sum([lam*s.eom
                             for s, lam in zip(states, costate_names)])
    yield ham
    yield make_costate_rates(ham, states, costate_names, derivative_fn)

def make_costate_names(states):
    return [sympify('lam'+str(s.name).upper()) for s in states]

def make_costate_rates(ham, states, costate_names, derivative_fn):
    """Make costates."""
    costates = [SymVar({'name': lam, 'eom':derivative_fn(-1*(ham), s)})
                for s, lam in zip(states, costate_names)]
    return costates

def sanitize_constraint_expr(constraint,
            states,
            location, prefix_map
            ):
    """
    Checks the initial/terminal constraint expression for invalid symbols
    Also updates the constraint expression to reflect what would be in code
    """

    if location not in prefix_map:
        raise ValueError('Invalid constraint type')

    pattern, prefix, _ = dict(prefix_map)[location]
    m = _re.findall(pattern,str(constraint.expr))
    invalid = [x for x in m if x not in states]

    if not all(x is None for x in invalid):
        raise ValueError('Invalid expression(s) in boundary constraint:\n'+str([x for x in invalid if x is not None]))

    return _re.sub(pattern,prefix,str(constraint.expr))


def make_boundary_conditions(constraints,
                             states,
                             costates,
                             cost,
                             derivative_fn,
                             location,
                             prefix_map=(('initial',(r'([\w\d\_]+)_0', r"_x0['\1']", sympify('-1'))),
                                         ('terminal',(r'([\w\d\_]+)_f', r"_xf['\1']", sympify('1'))))):
    """simplepipe task for creating boundary conditions for initial and terminal
    constraints."""
    prefix_map = dict(prefix_map)
    bc_list = [sanitize_constraint_expr(x, states, location, prefix_map)
                    for x in constraints[location]]

    *_, sign = dict(prefix_map)[location]

    cost_expr = sign * cost

    #TODO: Fix hardcoded if conditions
    #TODO: Change to symbolic
    bc_list += [str(costate - derivative_fn(cost_expr, state))
                        for state, costate in zip(states, costates)]

    return bc_list

def make_time_bc(constraints, bc_terminal):
    """Makes free or fixed final time boundary conditions."""
    time_constraints = constraints.get('independent', [])
    if len(time_constraints) > 0:
        return bc_terminal+['tf - 1']
    else:
        # Add free final time boundary condition
        return bc_terminal+['_H - 0']



def make_dhdu(ham, controls, derivative_fn):
    """Computes the partial of the hamiltonian w.r.t control variables."""
    dhdu = []
    for ctrl in controls:
        dHdu = derivative_fn(ham, ctrl)
        custom_diff = dHdu.atoms(sympy.Derivative)
        # Substitute "Derivative" with complex step derivative
        repl = {(d,im(f.func(v+1j*1e-30))/1e-30) for d in custom_diff
                    for f,v in zip(d.atoms(sympy.AppliedUndef),d.atoms(Symbol))}

        dhdu.append(dHdu.subs(repl))

    return dhdu

def make_control_law(dhdu, controls):
    """Solves control equation to get control law."""
    ctrl_sol = sympy.solve(dhdu, controls, dict=True)
    # control_options = [ [{'name':str(ctrl), 'expr':str(expr)}
    #                         for (ctrl,expr) in option.items()]
    #                         for option in ctrl_sol]
    control_options = ctrl_sol
    return control_options

def process_constraint(s,
                       s_idx,
                       states,
                       costates,
                       controls,
                       ham,
                       quantity_vars,
                       jacobian_fn,
                       derivative_fn,
                       max_iter=5):
    """Processes one constraint expression to create constrained control eqn,
    constrained arc bc function"""

    print('Processing constraint: ',s.name)
    s_bound = sympy.sympify(s.name)
    s_q = sympy.Matrix([s.expr - s_bound])
    control_found = False

    order = 0
    found = False

    num_states = len(states)
    stateAndLam = [*states, *costates]
    stateAndLamDot = [s.eom*sympify('tf') for s in it.chain(states, costates)]
    costate_names = make_costate_names(states)

    ham_mat = sympy.Matrix([ham])
    mult = sympy.symbols('_mu'+str(s_idx))

    tangency = []
    for i in range(max_iter):
        s_q = s_q.subs(quantity_vars)
        control_found = any(u in s_q.free_symbols for u in controls)
        if control_found:
            print('Constraint',s.name,'is of order',order)
            found = True
            ham_aug = ham_mat + mult*s_q  # Augmented hamiltonian
            lamdot_aug = - mult * jacobian_fn(s_q, states)  # Augmented costate equations in constrained arc

            # First solve for controls and then for mu
            dh_du = jacobian_fn(ham_aug, [*controls, mult])
            u_sol_list = make_control_law(dh_du[1], controls)
            mu_sol_list = []
            constrained_control_law = []
            for u_sol in u_sol_list:
                mu_sol = make_control_law(dh_du[0].subs(u_sol), mult)
                control_law = {**u_sol, **mu_sol[0]}
                constrained_control_law.append(control_law)

            # from beluga.utils import keyboard
            # keyboard()

            # constrained_control_law = make_control_law(dhdu, [*controls, mult])
            constrained_costate_rates = make_costate_rates(ham_aug[0], states, costate_names, derivative_fn)
            break

        tangency.append(s_q[0])
        s_q = jacobian_fn(s_q, stateAndLam)*sympy.Matrix([stateAndLamDot]).T

        order += 1

    N_x = jacobian_fn(sympy.Matrix(tangency), states)
    # print(sympy.Matrix(N_x))
    if order > 0:
        pi_list = sympy.symbols('pi'+str(s_idx)+':'+str(len(tangency)))
        corner_conditions = sympy.Matrix([pi_list]) * N_x
    else:
        pi_list = []
        corner_conditions = sympy.Matrix([0]*len(costates)).T

    if not found:
        raise Exception("Invalid path constrant")

    return constrained_control_law, constrained_costate_rates, ham_aug[0], order, mult, pi_list, corner_conditions, tangency


def process_path_constraints(path_constraints,
                             states,
                             costates,
                             constants,
                             controls,
                             ham,
                             quantity_vars,
                             jacobian_fn,
                             derivative_fn):

    s_list = []
    mu_vars = []
    for i, s in enumerate(path_constraints):
        u_aug, lamdot, ham_aug, order, mu_i, pi_list, corner_conditions, tangency = \
                process_constraint(s, i, states, costates, controls, ham, quantity_vars, jacobian_fn, derivative_fn)

        s_list.append({'name': str(s['name']),
                       'expr': str(s['expr'].subs(quantity_vars)),
                       'unit': str(s['unit']),
                       'direction': s['direction'],
                       'control_law': u_aug,
                       'lamdot': lamdot,
                       'ham': ham_aug,
                       'order': order,
                       'mu': mu_i,
                       'pi_list': pi_list,
                       'corner': corner_conditions,
                       'tangency': tangency,
                       'bound_val': s['bound']})
        mu_vars.append(mu_i)

    yield s_list
    yield mu_vars


def make_parameters(initial_lm_params, terminal_lm_params, s_list):
    all_pi_names = [p['pi_list'] for p in s_list]
    params_list = [str(p) for p in it.chain(initial_lm_params,
                                            terminal_lm_params)] #, *all_pi_names)]
    parameters = sym.symbols(' '.join(params_list))
    return parameters

def make_constraint_bc(s, states, costates, parameters, constants, controls, mu_vars, quantity_vars, ham):

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

def make_constrained_arc_fns(workspace):
    """Creates constrained arc control functions."""
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
              'arctype':arc_type,
              'pi_list': pi_list,
              'name': s['name']}
        bc_list.append(bc)

        # control_fns.append(u_fn)
        costate_eoms.append(costate_eom)

    # yield control_fns
    yield costate_eoms
    yield bc_list

#
# def make_odefn(workspace):
#
#     control_opts = workspace['control_law']
#     controls = sym.Matrix([_.name for _ in workspace['controls']])
#     constants = sym.Matrix([_.name for _ in workspace['constants']])
#     states = sym.Matrix([_.name for _ in workspace['states']])
#     costates = sym.Matrix([_.name for _ in workspace['costates']])
#     parameters = sym.Matrix(workspace['parameters'])
#
#     state_eoms = sym.Matrix([_.eom for _ in workspace['states']]).T
#     costate_eoms = sym.Matrix([_.eom for _ in workspace['costates']]).T
#
#     compute_control = workspace['control_fn']
#
#     state_eom_fn = make_sympy_fn([*states, *costates, *parameters, *constants, *controls], state_eoms)
#     costate_eom_fn = make_sympy_fn([*states, *costates, *parameters, *constants, *controls], costate_eoms)
#     zero_eom = np.array([0])
#
#     def eom_fn(t, X, p, C):
#         u = compute_control(t, X, p, C)
#         return np.hstack((state_eom_fn(*X,*p,*C,*u), costate_eom_fn(*X,*p,*C,*u), zero_eom))
#
#     return eom_fn
#
# def make_bcfn(workspace):
#     controls = sym.Matrix([_.name for _ in workspace['controls']])
#     constants = sym.Matrix([_.name for _ in workspace['constants']])
#     states = sym.Matrix([_.name for _ in workspace['states']])
#     costates = sym.Matrix([_.name for _ in workspace['costates']])
#     parameters = workspace['parameters']
#     constraints = workspace['constraints']
#     derivative_fn = workspace['derivative_fn']
#
#     compute_control = workspace['control_fn']
#     ham_fn = workspace['ham_fn']
#
#     prefix_map = (('initial',(r'([\w\d\_]+)_0', r"_ic_\1", sympify('-1'))),
#                   ('terminal',(r'([\w\d\_]+)_f', r"_fc_\1", sympify('1'))))
#
#     xAndLamSyms = set(it.chain(states, costates, parameters, constants))
#     bc_map = {}
#     bc_param_map = {}
#     for location in ('initial', 'terminal'):
#         cost = workspace['aug_'+location+'_cost']
#         bc = make_boundary_conditions(constraints,
#                              workspace['states'],
#                              workspace['costates'],
#                              cost,
#                              derivative_fn,
#                              location,
#                              prefix_map)
#         bc_map[location] = sym.Matrix([bc])
#         new_syms = bc_map[location].free_symbols - xAndLamSyms
#         bc_param_map[location] = new_syms
#
#
#     xic = bc_param_map['initial']
#     xfc = bc_param_map['terminal']
#
#     bc0_fn = make_sympy_fn([*states, *costates, *parameters, *constants, *xic, *xfc], bc_map['initial'])
#     bcf_fn = make_sympy_fn([*states, *costates, *parameters, *constants, *xic, *xfc], bc_map['terminal'])
#
#     def bc_fn(y0, yf, p, C, xic, xfc):
#         return np.hstack((bc0_fn(y0, p, C, xic, xfc),
#                           bcf_fn(yf, p, C, xic, xfc)))
#
#     return bc_fn, xic, xfc

def generate_problem_data(workspace):
    """Generates the `problem_data` dictionary used for code generation."""

    tf_var = sympify('tf') #TODO: Change to independent var?
    problem_data = {
        'method':'brysonho',
        'problem_name': workspace['problem_name'],
        'aux_list': [
            {
            'type' : 'const',
            'vars': [str(k) for k in workspace['constants']]
            }
        ],
        'state_list':
         [str(x) for x in it.chain(workspace['states'], workspace['costates'])]
         + ['tf']
        ,
        'parameter_list': [str(p) for p in workspace['parameters']],
        'x_deriv_list': [str(tf_var*state.eom) for state in workspace['states']],
        'lam_deriv_list':[str(tf_var*costate.eom) for costate in workspace['costates']],
        'deriv_list':
         [str(tf_var*state.eom) for state in workspace['states']] +
         [str(tf_var*costate.eom) for costate in workspace['costates']] +
         [0]   # TODO: Hardcoded 'tf'
        ,
        'states': workspace['states'],
        'costates': workspace['costates'],
        'constants': workspace['constants'],
        'parameters': workspace['parameters'],
        'controls': workspace['controls'],
        'mu_vars': workspace['mu_vars'],
        'quantity_vars': workspace['quantity_vars'],

        'costate_eoms': workspace['costate_eoms'],
        'bc_list': workspace['bc_list'],
        'ham': workspace['ham'],
        'quantity_vars': workspace['quantity_vars'],
        's_list': workspace['s_list'],
        'bc_list': workspace['bc_list'],
        'num_states': 2*len(workspace['states']) + 1,
        'num_params': len(workspace['parameters']),
        'dHdu': workspace['dhdu'],
        'bc_initial': [str(_) for _ in workspace['bc_initial']],
        'bc_terminal': [str(_) for _ in workspace['bc_terminal']],
        'control_options': workspace['control_law'],
        'control_list': [str(u) for u in workspace['controls']+workspace['mu_vars']],
        'num_controls': len(workspace['controls'])+len(workspace['mu_vars']),
        'ham_expr': str(workspace['ham']),
        'quantity_list': workspace['quantity_list'],
    }

    return problem_data


def init_workspace(ocp):
    """Initializes the simplepipe workspace using an OCP definition.

    All the strings in the original definition are converted into symbolic
    expressions for computation.
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


# Implement workflow using simplepipe and functions defined above
BrysonHo = sp.Workflow([
    sp.Task(init_workspace, inputs=('problem',), outputs='*'),
    sp.Task(process_quantities,
            inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn', 'jacobian_fn')),

    sp.Task(ft.partial(make_augmented_cost, location='initial'),
            inputs=('initial_cost', 'constraints'),
            outputs=('aug_initial_cost')),
    sp.Task(ft.partial(make_aug_params, location='initial'),
            inputs=('constraints'),
            outputs=('initial_lm_params')),

    sp.Task(ft.partial(make_augmented_cost, location='terminal'),
            inputs=('terminal_cost', 'constraints'),
            outputs=('aug_terminal_cost')),
    sp.Task(ft.partial(make_aug_params, location='terminal'),
            inputs=('constraints'),
            outputs=('terminal_lm_params')),
    sp.Task(make_costate_names,
            inputs=('states'),
            outputs=('costate_names')),
    sp.Task(make_hamiltonian_and_costate_rates,
            inputs=('states', 'costate_names', 'path_cost', 'derivative_fn'),
            outputs=('ham', 'costates')),
    sp.Task(ft.partial(make_boundary_conditions, location='initial'),
            inputs=('constraints', 'states', 'costates', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_initial')),
    sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
            inputs=('constraints', 'states', 'costates', 'aug_terminal_cost', 'derivative_fn'),
            outputs=('bc_terminal')),
    sp.Task(make_time_bc, inputs=('constraints', 'bc_terminal'), outputs=('bc_terminal')),
    sp.Task(make_dhdu,
            inputs=('ham', 'controls', 'derivative_fn'),
            outputs=('dhdu')),

    sp.Task(process_path_constraints,
            inputs=('path_constraints',
                    'states',
                    'costates',
                    'constants',
                    'controls',
                    'ham',
                    'quantity_vars',
                    'jacobian_fn',
                    'derivative_fn'),
            outputs=['s_list', 'mu_vars']),

    sp.Task(make_control_law,
            inputs=('dhdu','controls'),
            outputs=('control_law')),

    sp.Task(make_parameters, inputs=['initial_lm_params', 'terminal_lm_params', 's_list'],
        outputs='parameters'),

    sp.Task(make_constrained_arc_fns, inputs='*', outputs=['costate_eoms', 'bc_list']),
    # sp.Task(make_odefn, inputs='*', outputs='ode_fn'),
    # sp.Task(make_bcfn, inputs='*', outputs='bc_fn'),
    sp.Task(generate_problem_data,
            inputs='*',
            outputs=('problem_data')),
], description='Traditional optimal control workflow')

traditional = BrysonHo


## Unit tests ##################################################################
from beluga.problem import ConstraintList
from beluga.problem import SymVar

def test_process_quantities():
    quantities = [SymVar(dict(name='rho', val='rho0*exp(-h/H)')),
                  SymVar(dict(name='D', val='0.5*rho*v^2*Cd*Aref'))]
    qvars, qlist, _ = process_quantities(quantities)

    qvars_expected = dict(rho= sympify('rho0*exp(-h/H)'),
                          D= sympify('0.5*Aref*Cd*rho0*v**2*exp(-h/H)'))
    qlist_expected = [{'expr': 'rho0*exp(-h/H)', 'name': 'rho'},
                      {'expr': '0.5*Aref*Cd*rho0*v**2*exp(-h/H)', 'name': 'D'}]

    assert qvars == qvars_expected
    assert qlist == qlist_expected

def test_ham_and_costates():
    states = [SymVar({'name':'x','eom':'v*cos(theta)','unit':'m'}),
              SymVar({'name':'y','eom':'-v*sin(theta)','unit':'m'}),
              SymVar({'name':'v','eom':'g*sin(theta)','unit':'m/s'})]
    path_cost = SymVar({'expr': 1}, sym_key='expr')

    expected_output = (sympify('g*lamV*sin(theta) + lamX*v*cos(theta) - lamY*v*sin(theta) + 1'),
                       [SymVar({'name':'lamX','eom':'0'}),
                       SymVar({'name':'lamY','eom':'0'}),
                       SymVar({'name':'lamV','eom':'-lamX*cos(theta) - lamY*sin(theta)'})])

    costate_names = make_costate_names(states)
    ham, costates = make_hamiltonian_and_costate_rates(states, costate_names, path_cost, total_derivative)

    assert ham == expected_output[0]
    assert costates == expected_output[1]

def test_augmented_cost():
    constraints = ConstraintList()
    constraints.initial('h - h_0', 'm') # doctest:+ELLIPSIS
    constraints.terminal('h - h_f', 'm')
    terminal_cost = SymVar({'expr': '-v^2', 'unit': 'm^2/s^2'}, sym_key='expr')

    expected_output = SymVar({'expr': 'lagrange_terminal_1*(h - h_f) - v**2',
                       'unit': 'm**2/s**2'}, sym_key='expr')
    expected_params = [sympify('lagrange_terminal_1')]
    aug_cost = make_augmented_cost(terminal_cost, constraints, 'terminal')
    params = make_aug_params(constraints, 'terminal')
    assert aug_cost == expected_output
    assert params == expected_params


def test_make_boundary_conditions():
    states = [SymVar({'name':'h','eom':'v*cos(theta)','unit':'m'}),
              SymVar({'name':'theta','eom':'v*sin(theta)/r','unit':'rad'})]
    path_cost = SymVar({'expr': 1}, sym_key='expr')
    costate_names = make_costate_names(states)
    ham, costates = make_hamiltonian_and_costate_rates(states, costate_names, path_cost, total_derivative)

    constraints = ConstraintList()
    constraints.initial('h - h_0', 'm') # doctest:+ELLIPSIS
    constraints.terminal('theta - theta_f', 'rad') # doctest:+ELLIPSIS

    initial_cost = sympify('0')
    bc_initial = make_boundary_conditions(constraints, states, costates, initial_cost, total_derivative, 'initial')
    assert bc_initial == ["h - _x0['h']", 'lamH', 'lamTHETA']

    terminal_cost = sympify('-theta^2')
    bc_terminal = make_boundary_conditions(constraints, states, costates, terminal_cost, total_derivative, 'terminal')
    assert bc_terminal == ["theta - _xf['theta']", 'lamH', 'lamTHETA + 2*theta']

def test_make_control_law():
    states = [SymVar({'name':'x','eom':'v*cos(theta)','unit':'m'}),
              SymVar({'name':'y','eom':'v*sin(theta)','unit':'m'}),
              SymVar({'name':'v','eom':'g*sin(theta)','unit':'m/s'})]
    path_cost = SymVar({'expr': 1}, sym_key='expr')
    controls = [SymVar({'name':'theta','unit':'rad'})]
    costate_names = make_costate_names(states)
    ham, costates = make_hamiltonian_and_costate_rates(states, costate_names, path_cost, total_derivative)

    dhdu = make_dhdu(ham, controls, total_derivative)
    assert dhdu == [sympify('g*lamV*cos(theta) - lamX*v*sin(theta) + lamY*v*cos(theta)')]
    control_law = make_control_law(dhdu, controls)
    assert control_law == [{controls[0]._sym: sympify('-2*atan((lamX*v - sqrt(g**2*lamV**2 + 2*g*lamV*lamY*v + lamX**2*v**2 + lamY**2*v**2))/(g*lamV + lamY*v))')},
                           {controls[0]._sym: sympify('-2*atan((lamX*v + sqrt(g**2*lamV**2 + 2*g*lamV*lamY*v + lamX**2*v**2 + lamY**2*v**2))/(g*lamV + lamY*v))')}]

def test_compile_equations(tmpdir):
    workspace = {'mult': 2}

    code_mod = create_module('test_problem')

    # Write test template file
    code_file = tmpdir.mkdir("templates").join('test.py.mu')
    test_code_tmpl = """def test(foo):
    return foo*{{mult}}"""
    code_file.write(test_code_tmpl)

    # Check if codee generation works
    out_code = load_eqn_template(workspace, str(code_file))

    test_code_expected = """def test(foo):
    return foo*2"""
    assert out_code == test_code_expected
    # Check if code compilation works
    out_fn = compile_code_py(out_code, code_mod, 'test')
    assert out_fn(3) == 6
