"""
Computes the necessary conditions of optimality using Bryson & Ho's method

[1] Bryson, Arthur Earl. Applied optimal control: optimization, estimation and control. CRC Press, 1975.
"""

import numpy
import logging
np = numpy

from .optimlib import *

from math import *
import numba

# import beluga
from beluga.utils import sympify
from beluga.problem import SymVar
import simplepipe as sp

from sympy.utilities.lambdify import lambdastr
from beluga.utils import keyboard


# def ocp_to_bvp(ocp, guess_maker):
#     """
#     This converts a user-defined OCP to a MPBVP
#
#     :param ocp:
#     :return:
#     """
#     ws = init_workspace(ocp)
#     quantity_vars, quantity_list, derivative_fn, jacobian_fn = process_quantities(ws['quantities'])
#     augmented_initial_cost = make_augmented_cost(ws['initial_cost'], ws['constraints'], 'initial')
#     initial_lm_params = make_augmented_params(ws['constraints'], 'initial')
#     augmented_terminal_cost = make_augmented_cost(ws['terminal_cost'], 'terminal')
#     terminal_lm_params = make_augmented_params(ws['constraints'], 'terminal')
#     sp.Workflow([
#         sp.Task(init_workspace, inputs=('problem',), outputs='*'),
#         sp.Task(process_quantities,
#                 inputs=('quantities'),
#                 outputs=('quantity_vars', 'quantity_list', 'derivative_fn', 'jacobian_fn')),
#
#         sp.Task(ft.partial(make_augmented_cost, location='initial'),
#                 inputs=('initial_cost', 'constraints'),
#                 outputs=('aug_initial_cost')),
#         sp.Task(ft.partial(make_augmented_params, location='initial'),
#                 inputs=('constraints'),
#                 outputs=('initial_lm_params')),
#
#         sp.Task(ft.partial(make_augmented_cost, location='terminal'),
#                 inputs=('terminal_cost', 'constraints'),
#                 outputs=('aug_terminal_cost')),
#         sp.Task(ft.partial(make_augmented_params, location='terminal'),
#                 inputs=('constraints'),
#                 outputs=('terminal_lm_params')),
#         sp.Task(make_costate_names,
#                 inputs=('states'),
#                 outputs=('costate_names')),
#         sp.Task(make_hamiltonian_and_costate_rates,
#                 inputs=('states', 'costate_names', 'path_cost', 'derivative_fn'),
#                 outputs=('ham', 'costates')),
#         sp.Task(ft.partial(make_boundary_conditions, location='initial'),
#                 inputs=('constraints', 'states', 'costates', 'aug_initial_cost', 'derivative_fn'),
#                 outputs=('bc_initial')),
#         sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
#                 inputs=('constraints', 'states', 'costates', 'aug_terminal_cost', 'derivative_fn'),
#                 outputs=('bc_terminal')),
#         sp.Task(make_time_bc, inputs=('constraints', 'bc_terminal'), outputs=('bc_terminal')),
#         sp.Task(make_dhdu,
#                 inputs=('ham', 'controls', 'derivative_fn'),
#                 outputs=('dhdu')),
#
#         sp.Task(process_path_constraints,
#                 inputs=('path_constraints',
#                         'states',
#                         'costates',
#                         'constants',
#                         'controls',
#                         'ham',
#                         'quantity_vars',
#                         'jacobian_fn',
#                         'derivative_fn'),
#                 outputs=['s_list', 'mu_vars']),
#
#         sp.Task(make_control_law,
#                 inputs=('dhdu', 'controls'),
#                 outputs=('control_law')),
#
#         sp.Task(make_parameters, inputs=['initial_lm_params', 'terminal_lm_params', 's_list'],
#                 outputs='parameters'),
#
#         sp.Task(make_constrained_arc_fns, inputs='*', outputs=['costate_eoms', 'bc_list']),
#         # sp.Task(make_odefn, inputs='*', outputs='ode_fn'),
#         # sp.Task(make_bcfn, inputs='*', outputs='bc_fn'),
#         sp.Task(generate_problem_data,
#                 inputs='*',
#                 outputs=('problem_data')),
#     ], description='Traditional optimal control workflow')
#
#     return 1

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


def make_control_law(dhdu, controls):
    """Solves control equation to get control law."""
    try:
        logging.info(controls)
        var_list = list(controls)
        logging.info("Attempting using SymPy ...")
        logging.debug("dHdu = "+str(dhdu))
        ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)

        # raise ValueError() # Force mathematica
    except ValueError as e:  # FIXME: Use right exception name here
        logging.debug(e)
        logging.info("No control law found")
        from beluga.utils_old.pythematica import mathematica_solve
        logging.info("Attempting using Mathematica ...")
        var_sol = mathematica_solve(dhdu,var_list)
        # TODO: Extend numerical control laws to mu's
        ctrl_sol = var_sol
    logging.info('Control found')
    logging.info(ctrl_sol)
    # ctrl_sol = sympy.solve(dhdu, controls, dict=True)
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
    stateAndLamDot = [s.eom for s in it.chain(states, costates)]
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
                mu_sol = make_control_law(dh_du[0].subs(u_sol), [mult])
                control_law = {**u_sol, **mu_sol[0]}
                constrained_control_law.append(control_law)

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
              'arctype': arc_type,
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

    tf_var = sympify('tf')
    problem_data = {
        'method': 'brysonho',
        'problem_name': workspace['problem_name'],
        'aux_list': [
            {
            'type' : 'const',
            'vars': [str(k) for k in workspace['constants']]
            }
        ],
        'state_list':
            [str(x) for x in it.chain(workspace['states'], workspace['costates'])]
        ,
        'parameter_list': [str(tf_var)] + [str(p) for p in workspace['parameters']],
        'x_deriv_list': [str(tf_var*state.eom) for state in workspace['states']],
        'lam_deriv_list':[str(tf_var*costate.eom) for costate in workspace['costates']],
        'deriv_list':
            [str(tf_var*state.eom) for state in workspace['states']] +
            [str(tf_var*costate.eom) for costate in workspace['costates']]
        ,
        'states': workspace['states'],
        'costates': workspace['costates'],
        'constants': workspace['constants'],
        'parameters': [tf_var] + workspace['parameters'],
        'controls': workspace['controls'],
        'mu_vars': workspace['mu_vars'],
        'quantity_vars': workspace['quantity_vars'],

        'costate_eoms': workspace['costate_eoms'],
        'bc_list': workspace['bc_list'],
        'ham': workspace['ham'],
        's_list': workspace['s_list'],
        'num_states': 2*len(workspace['states']),
        'num_params': len(workspace['parameters']) + 1,
        'dHdu': workspace['dhdu'],
        'bc_initial': [str(_) for _ in workspace['bc_initial']],
        'bc_terminal': [str(_) for _ in workspace['bc_terminal']],
        'control_options': workspace['control_law'],
        'control_list': [str(u) for u in workspace['controls']+workspace['mu_vars']],
        'num_controls': len(workspace['controls'])+len(workspace['mu_vars']),
        'ham_expr': str(workspace['ham']),
        'quantity_list': workspace['quantity_list'],
        'nOdes': 2*len(workspace['states'])
    }

    return problem_data


# Implement workflow using simplepipe and functions defined above
BrysonHo = sp.Workflow([
    sp.Task(init_workspace, inputs=('problem',), outputs='*'),
    sp.Task(process_quantities,
            inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn', 'jacobian_fn')),
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
    sp.Task(make_costate_names,
            inputs=('states'),
            outputs=('costate_names')),
    sp.Task(make_hamiltonian_and_costate_rates,
            inputs=('states', 'costate_names', 'path_cost', 'derivative_fn'),
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


