"""
Contains classes and functions related to Optimal Control.

Module: optimlib
"""

from .brysonho import *
import sympy as sym
from beluga.utils import keyboard
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
        return lbound + sym.exp(var)
    elif lbound is None:
        # Return upper bound sat fn
        #lbound = -ubound
        return ubound - sym.exp(-var)
    else:
        print(ubound)
        s = 4*slopeAtZero/(ubound - lbound)
        return ubound - ( ubound - lbound )/( 1 + sym.exp(s*var) )

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
        path_cost_expr = workspace['terminal_cost'].expr
        path_cost_unit = workspace['terminal_cost'].unit

    logging.debug('Path cost is of unit: '+str(path_cost_unit))
    time_unit = workspace['indep_var'].unit
    path_constraints = workspace['path_constraints']

    eq = constraints.get('equality', [])
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
            ocp.constant(str(c_limit),float(c.bound),c.unit)
            logging.debug('Added constant '+str(c_limit))

        if c.direction == '>':
            c.lbound = c_limit
            c.ubound = -c_limit
        elif c.direction == '<':
            c.ubound = c_limit
            c.lbound = -c_limit
        else:
            raise ValueError('Invalid direction specified for constraint')

        psi = get_satfn(xi_vars[0], ubound=c.ubound, lbound=c.lbound, slopeAtZero=50)
        psi_vars = [(sym.Symbol('psi'+str(ind+1)), psi)]

        # Add to quantity list
        quantity_vars[sym.Symbol('psi'+str(ind+1))] = psi
        quantity_list.append({'name':('psi'+str(ind+1)), 'expr':str(psi)})

        # m-th order constraint needs up to m-th derivative of psi to be defined
        psi_i = psi

        for i in range(order):
            psi_i = derivative_fn(psi_i, xi_vars[0])
            # psi_vars.append((Symbol('psi'+str(ind+1)+str(i+1)+'('+str(xi_vars[0])+')'), psi_i))
            psi_vars.append((sym.Symbol('psi'+str(ind+1)+str(i+1)), psi_i))
            quantity_vars['psi'+str(ind+1)+str(i+1)] =  psi_i
            quantity_list.append({'name':('psi'+str(ind+1)+str(i+1)), 'expr':str(psi_i)})

        # psi_vars = psi_vars + []
        psi_var_sub = [(v,k) for k,v in psi_vars]

        # FIXME: Hardcoded h derivatives for now
        # h = [psi_vars[0][0]]
        # h.append(psi_vars[1][0]*xi_vars[1]) # psi'*xi12
        # h.append(psi_vars[2][0]*xi_vars[1] + psi_vars[1][0]*xi_vars[2]) # psi''*xi12 + psi'*xi13
        # psi'''*xi12 + xi13*psi12'' + psi12*xi13 + psi11*ue1
        # h.append(psi_vars[3][0]*xi_vars[1] + 2 * psi_vars[2][0]*xi_vars[2] + psi_vars[1][0]*xi_vars[3] )

        #TODO: Hardcoded 't' as independent variable with unit of 's'
        # c_vals = [80e3, -5000, 9.539074102210087] # third number is vdot at zero approx
        c_vals = np.ones(order)*0.1
        h = [psi_vars[0][1]]
        for i in range(order):
            # Add 'xi' state
            states.append(SymVar({'name':str(xi_vars[i]), 'eom':str(xi_vars[i+1]), 'unit':c.unit/(time_unit^i)}))
            # Constraint all cq at initial point (forms constraints for xi_ij)
            # ocp.constraints().initial(str(cq[i] - h[i]),'('+c.unit+')/s^('+str(i)+')')
            constraints['initial'].append(SymVar({'expr':str(cq[i] - h[i]), 'unit':c.unit/(time_unit^i)}, sym_key='expr'))
            # Add to initial guess vector
            # guess.start.append(c_vals[i]) # FIXME

            dhdxi = [derivative_fn(h[i], xi_v) for xi_v in xi_vars[:-1]]
            dhdt  = sum(d1*d2 for d1,d2 in zip(dhdxi,xi_vars[1:])) # xi11dot = xi12 etc.
            dhdt = dhdt.subs(psi_var_sub)
            h.append(dhdt)

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
        # ocp.constant(str(eps_const), 1e-2, str(eps_unit))
        constants.append(SymVar({'name':eps_const, 'value': 1e-2, 'unit':str(eps_unit)}))
        logging.debug('Adding smoothing factor '+str(eps_const)+' with unit '+str(eps_unit))

        # Append new control to path cost
        path_cost_expr = path_cost_expr + eps_const*xi_vars[-1]**2

    constraints['equality'] = eq

    logging.debug('Updated path cost is: '+str(path_cost_expr))

    derivative_fn = ft.partial(total_derivative, dependent_vars=quantity_vars)
    jacobian_fn = ft.partial(jacobian, derivative_fn=derivative_fn)

    s_list = []

    yield states
    yield controls
    yield constants
    yield constraints
    yield s_list
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

def make_ctrl_dae(states, costates, controls, constraints, dhdu, derivative_fn):
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

    yield mu_vars
    yield mu_lhs
    yield dae_states
    yield dae_equations
    yield dae_bc
def generate_problem_data(workspace):
    """Generates the `problem_data` dictionary used for code generation."""

    tf_var = sympify('tf') #TODO: Change to independent var?

    problem_data = {
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
     'num_params': len(workspace['parameters']),
     'dHdu': [str(_) for _ in it.chain(workspace['dhdu'], workspace['mu_lhs'])],
     'bc_initial': [str(_) for _ in it.chain(workspace['bc_initial'], workspace['dae_bc'])],
     'bc_terminal': [str(_) for _ in workspace['bc_terminal']],
     'control_options': [],
     'control_list': [str(u) for u in workspace['controls']+workspace['mu_vars']],
     'num_controls': len(workspace['controls'])+len(workspace['mu_vars']),
     'ham_expr': str(workspace['ham']),
     'quantity_list': workspace['quantity_list'],
    }

    return problem_data
# Implement workflow using simplepipe and functions defined above
ICRM = sp.Workflow([
    sp.Task(init_workspace, inputs=('problem',), outputs='*'),
    sp.Task(process_quantities, inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn', 'jacobian_fn')),
    sp.Task(process_path_constraints, inputs='*',
            outputs=('states', 'controls', 'constants', 'constraints', 's_list', 'derivative_fn', 'jacobian_fn')),

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
    sp.Task(make_ctrl_dae,
            inputs=('states', 'costates', 'controls', 'constraints', 'dhdu', 'derivative_fn'),
            outputs=('mu_vars', 'mu_lhs', 'dae_states', 'dae_equations', 'dae_bc')),
    sp.Task(make_parameters, inputs=['initial_lm_params', 'terminal_lm_params', 's_list'],
        outputs='parameters'),
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
