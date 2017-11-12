"""
Contains classes and functions related to Optimal Control.

Module: optimlib
"""

from .brysonho import *
import sympy as sym
from beluga.utils import sympify2, keyboard
from beluga.problem import SymVar
import logging

def get_satfn(var, ubound=None, lbound=None, slopeAtZero=1):
    # var -> varible inside saturation function
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
        return ubound - ( ubound - lbound )/( 1 + sym.exp(s*var) )

def make_bc(constraints,
             states,
             costates,
             cost,
             aug_cost,
             derivative_fn,
             location,
             prefix_map=(('initial',(r'([\w\d\_]+)_0', r"_x0['\1']", sympify('-1'))),
                         ('terminal',(r'([\w\d\_]+)_f', r"_xf['\1']", sympify('1'))))):

    prefix_map = dict(prefix_map)
    bc_list = [sanitize_constraint_expr(x, states, location, prefix_map)
                    for x in constraints[location]]

    *_, sign = dict(prefix_map)[location]

    cost_expr = sign * cost
    aug_cost_expr = sign * (aug_cost.expr - cost.expr)

    #TODO: Fix hardcoded if conditions
    #TODO: Change to symbolic
    for state,costate in zip(states, costates):
        if derivative_fn(aug_cost_expr, state) == 0:
            # State not constrained -> costate = 0
            bc_list.append(str(costate - derivative_fn(cost_expr, state)))

    return bc_list

def make_bc_mask(states,
             controls,
             mu_vars,
             cost,
             aug_cost,
             derivative_fn):
    """Creates mask marking free and bound variables at t=0

    free = 1, constrained = 0
    """
    aug_cost_expr = (aug_cost.expr - cost.expr)

    state_mask = []
    costate_mask = []
    for state in states:
        if derivative_fn(aug_cost_expr, state) == 0:
            # State not constrained -> costate = 0
            state_mask.append(1) # State free
            costate_mask.append(0) # Costate fixed
        else:
            state_mask.append(0)    # State constrained
            costate_mask.append(1)  # Costate free

    return state_mask+costate_mask+[1]*(len(controls)+len(mu_vars)+1) # Add tf as free param


def add_equality_constraints(ham, constraints):

    equality_constraints = constraints.get('equality', [])
    # Adjoin equality constraints
    for i in range(len(equality_constraints)):
        ham += sympify('mu'+str(i+1)) * (sympify2(equality_constraints[i].expr))

    return ham

def make_ham_lamdot_with_eq_constraint(states, costate_names, constraints, path_cost, derivative_fn):
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
    ham = add_equality_constraints(ham, constraints)
    yield ham
    yield make_costate_rates(ham, states, costate_names, derivative_fn)

def process_path_constraints(workspace):
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
    for (ind,c) in enumerate(path_constraints):
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
            constants.append(SymVar({'name':str(c_limit),'value':float(c.bound),'unit':c.unit}))
            logging.debug('Added constant '+str(c_limit))

        c_lbound = c_ubound = None
        if c.direction == '>':
            c_lbound = c_limit
            # c.ubound = -c_limit
        elif c.direction == '<':
            c_ubound = c_limit
            # c.lbound = -c_limit
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
            print(f'Adding {xi_vars[i]} = {c_vals[i]}')
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

    yield states
    yield controls
    yield constants
    yield constraints
    yield path_cost
    yield s_list
    yield xi_init_vals
    yield derivative_fn
    yield jacobian_fn
    # ocp.path_cost(str(path_cost_expr), )

    # u_constraints = ocp.constraints().get('control')
    #
    # for (ind,c) in enumerate(u_constraints):
    #     w_i = sympify('uw'+str(ind+1))
    #     psi = self.get_satfn(w_i, ubound=sympify(c.ubound), lbound = sympify(c.lbound))
    #
    #     # Add the smoothing control
    #     problem.control(str(w_i), c.unit)
    #
    #     # Add equality constraint
    #     csym = sympify(c.expr)
    #     problem.constraints().equality(str(csym - psi),c.unit)
    #
    #     uw_unit = symipfy2(c.unit)
    #     eps_const = Symbol('eps_'+str(ind+1))
    #     eps_unit = (path_cost_unit/uw_unit**2)/time_unit #Unit of integrand
    #     problem.constant(str(eps_const), 1, str(eps_unit))
    return ocp

def make_ctrl_dae(states, costates, controls, constraints, dhdu, xi_init_vals, guess, derivative_fn):
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

    udot = dgdU.LUsolve(-dgdX*xdot); # dgdU * udot + dgdX * xdot = 0

    dae_states = U
    dae_equations = list(udot)
    dae_bc = g

    if guess.start is not None:
        guess.start.extend(xi_init_vals)
    guess.dae_num_states = len(U)

    # from beluga.utils import keyboard
    # keyboard()
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

    tf_var = sympify('tf') #TODO: Change to independent var?

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
    'method':'icrm',
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
    #  'parameter_list': [str(p) for p in workspace['parameters']],
     'parameter_list': [],
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
    #  'parameters': workspace['parameters'],
     'parameters': [],
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
     'num_states': 2*len(workspace['states']) + 1,
    #  'num_params': len(workspace['parameters']),
     'num_params': 0,
     'dHdu': [str(_) for _ in it.chain(workspace['dhdu'], workspace['mu_lhs'])],
    #  'bc_initial': [str(_) for _ in it.chain(workspace['bc_initial'], workspace['dae_bc'])],
    #  'bc_terminal': [str(_) for _ in workspace['bc_terminal']],
     'bc_initial': [str(_) for _ in workspace['bc_initial']],
     'bc_terminal': [str(_) for _ in it.chain(workspace['bc_terminal'], workspace['dae_bc'])],
     'control_options': [],
     'control_list': [str(u) for u in workspace['controls']+workspace['mu_vars']],
     'num_controls': len(workspace['controls'])+len(workspace['mu_vars']),
     'ham_expr': str(workspace['ham']),
     'quantity_list': workspace['quantity_list'],
     'bc_free_mask': workspace['bc_free_mask'],
     #'dgdX': str(workspace['dgdX'][:]),
     'dgdX': dgdX,#str(workspace['dgdX'][:]),
     # 'dgdU': str(workspace['dgdU'][:]),
     'dgdU': dgdU,
     'nOdes':2*len(workspace['states']) + len(workspace['dae_states'])+ 1,
    }
    # from beluga.utils import keyboard
    # keyboard()
    # print(sympy.latex(udot[0], symbol_names={sympy.Symbol('lamX'):r'\lambda_x', sympy.Symbol('lamY'):r'\lambda_y', sympy.Symbol('lamV'):r'\lambda_v', sympy.Symbol('lamXI11'):r'\lambda_{\xi_1}'}))

    return problem_data
# Implement workflow using simplepipe and functions defined above
ICRM = sp.Workflow([
    sp.Task(init_workspace, inputs=('problem',), outputs='*'),
    sp.Task(process_quantities, inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn', 'jacobian_fn')),
    sp.Task(process_path_constraints, inputs='*',
            outputs=('states', 'controls', 'constants', 'constraints', 'path_cost', 's_list', 'xi_init_vals', 'derivative_fn', 'jacobian_fn')),

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
    sp.Task(make_ham_lamdot_with_eq_constraint,
            inputs=('states', 'costate_names', 'constraints', 'path_cost', 'derivative_fn'),
            outputs=('ham', 'costates')),
    # sp.Task(ft.partial(make_boundary_conditions, location='initial'),
    #         inputs=('constraints', 'states', 'costates', 'aug_initial_cost', 'derivative_fn'),
    #         outputs=('bc_initial')),
    sp.Task(ft.partial(make_bc, location='initial'),
            inputs=('constraints', 'states', 'costates', 'initial_cost', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_initial')),
    # sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
    #         inputs=('constraints', 'states', 'costates', 'aug_terminal_cost', 'derivative_fn'),
    #         outputs=('bc_terminal')),
    sp.Task(ft.partial(make_bc, location='terminal'),
            inputs=('constraints', 'states', 'costates', 'terminal_cost', 'aug_terminal_cost', 'derivative_fn'),
            outputs=('bc_terminal')),
    sp.Task(make_time_bc, inputs=('constraints', 'bc_terminal'), outputs=('bc_terminal')),
    sp.Task(make_dhdu,
            inputs=('ham', 'controls', 'derivative_fn'),
            outputs=('dhdu')),
    sp.Task(make_ctrl_dae,
            inputs=('states', 'costates', 'controls', 'constraints', 'dhdu', 'xi_init_vals', 'guess', 'derivative_fn'),
            outputs=('mu_vars', 'mu_lhs', 'dae_states', 'dae_equations', 'dae_bc', 'guess', 'dgdX', 'dgdU')),
    sp.Task(make_parameters, inputs=['initial_lm_params', 'terminal_lm_params', 's_list'],
        outputs='parameters'),
    sp.Task(make_bc_mask,
            inputs=('states', 'controls', 'mu_vars', 'initial_cost', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_free_mask')),

    # sp.Task(make_dhdu,
    #         inputs=('ham', 'controls', 'derivative_fn'),
    #         outputs=('dhdu')),
    #
    # sp.Task(make_control_law,
    #         inputs=('dhdu','controls'),
    #         outputs=('control_law')),
    #
    sp.Task(generate_problem_data,
            inputs='*',
            outputs=('problem_data')),
], description='ICRM workflow')


# Call doctest if the script is run directly
if __name__ == "__main__":
    import doctest
    doctest.testmod()
