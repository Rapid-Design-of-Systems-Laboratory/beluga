from .optimlib import *
import sympy as sym
from beluga.utils import sympify2, keyboard
import simplepipe as sp
from beluga.problem import SymVar
import logging
import numpy as np


def make_control_dae(states, costates, controls, constraints, dhdu, xi_init_vals, guess, derivative_fn):
    """
    Make's control law for dae (ICRM) formulation.

    :param states:
    :param costates:
    :param controls:
    :param constraints:
    :param dhdu:
    :param xi_init_vals:
    :param guess:
    :param derivative_fn:
    :return:
    """
    equality_constraints = constraints.get('equality', [])
    if len(equality_constraints) > 0:
        mu_vars = [sympify('mu'+str(i+1)) for i in range(len(equality_constraints))]
        mu_lhs = [sympify(c.expr) for c in equality_constraints]
    else:
        mu_vars = mu_lhs = []

    g = dhdu + mu_lhs
    X = [state for state in states] + [costate for costate in costates]
    U = [c for c in controls] + mu_vars

    xdot = sym.Matrix([sympify(state.eom) for state in states] + [sympify(lam.eom) for lam in costates])
    # Compute Jacobian
    dgdX = sym.Matrix([[derivative_fn(g_i, x_i) for x_i in X] for g_i in g])
    dgdU = sym.Matrix([[derivative_fn(g_i, u_i) for u_i in U] for g_i in g])

    udot = dgdU.LUsolve(-dgdX*xdot) # dgdU * udot + dgdX * xdot = 0

    dae_states = U
    dae_equations = list(udot)
    dae_bc = g

    if guess.start is not None:
        guess.start.extend(xi_init_vals)
    guess.dae_num_states = len(U)

    yield mu_vars
    yield mu_lhs
    yield dae_states
    yield dae_equations
    yield dae_bc
    yield guess
    yield dgdX
    yield dgdU


def generate_problem_data(workspace):
    """Generates the `problem_data` dictionary used for code generation."""

    tf_var = sympify('tf')

    dgdX = []
    for i, row in enumerate(workspace['dgdX'].tolist()):
        for j, expr in enumerate(row):
            if expr != 0:
                dgdX.append(f'dgdX[{i},{j}] = {expr}')

    dgdU = []
    for i, row in enumerate(workspace['dgdU'].tolist()):
        for j, expr in enumerate(row):
            if expr != 0:
                dgdU.append(f'dgdU[{i},{j}] = {expr}')

    problem_data = {
        'method': 'icrm',
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
        'dae_var_list':
            [str(dae_state) for dae_state in workspace['dae_states']],
        'dae_eom_list':
            ['(tf)*('+str(dae_eom)+')' for dae_eom in workspace['dae_equations']],
        'dae_var_num': len(workspace['dae_states']),

        'costate_eoms': [ {'eom':[str(_.eom*tf_var) for _ in workspace['costates']], 'arctype':0} ],
        'ham': workspace['ham'],

        's_list': [],
        'bc_list': [],
        'num_states': 2*len(workspace['states']),
        'num_params': len(workspace['parameters']) + 1,
        'dHdu': [str(_) for _ in it.chain(workspace['dhdu'], workspace['mu_lhs'])],
        'bc_initial': [str(_) for _ in workspace['bc_initial']],
        'bc_terminal': [str(_) for _ in it.chain(workspace['bc_terminal'], workspace['dae_bc'])],
        'num_bc': len(workspace['bc_initial'])+len(workspace['bc_terminal'])+ len(workspace['dae_bc']),
        'control_options': [],
        'control_list': [str(u) for u in workspace['controls']+workspace['mu_vars']],
        'num_controls': len(workspace['controls'])+len(workspace['mu_vars']),
        'ham_expr': str(workspace['ham']),
        'quantity_list': workspace['quantity_list'],
        'bc_free_mask': workspace['bc_free_mask'],
        'dgdX': dgdX,
        'dgdU': dgdU,
        'nOdes': 2*len(workspace['states']) + len(workspace['dae_states']),
    }

    return problem_data


# Implement workflow using simplepipe and functions defined above
ICRM = sp.Workflow()
ICRM.add_task(BaseWorkflow)
ICRM.add_task(make_control_dae,
            inputs=('states', 'costates', 'controls', 'constraints', 'dhdu', 'xi_init_vals', 'guess', 'derivative_fn'),
            outputs=('mu_vars', 'mu_lhs', 'dae_states', 'dae_equations', 'dae_bc', 'guess', 'dgdX', 'dgdU'))
ICRM.add_task(generate_problem_data, inputs='*', outputs=('problem_data'))
