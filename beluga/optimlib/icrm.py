"""
Contains classes and functions related to Optimal Control.

Module: optimlib
"""

from .brysonho import *

def sigmoid_two_sided(x, ub, lb, slopeAtZero=1):
    """Two-sided saturation function based on the sigmoid function."""
    pass


def sigmoid_one_sided(x, ub=None, lb=None, slopeAtZero=1):
    """
    One-sided saturation function based on the sigmoid function.

    Only of the bounds must be defined.
    """
    pass

def process_path_constraints(self, workspace):
    constraints = workspace['path_constraints']
    quantity_subs = workspace['quantity_vars']

    path_cost_expr = sympify(problem.cost['path'].expr)
    path_cost_unit = sympify(problem.cost['path'].unit)
    if path_cost_expr == 0:
        logging.debug('No path cost specified, using unit from terminal cost function')
        problem.cost['path'].unit = problem.cost['terminal'].unit
        path_cost_unit = sympify(problem.cost['terminal'].unit)

    logging.debug('Path cost is of unit: '+str(path_cost_unit))
    time_unit = Symbol('s')

    for (ind,c) in enumerate(constraints):
        # Determine order of constraint
        logging.debug('Processing path constraint: '+c.label)
        order = 0
        cq = [sympify(c.expr)]
        dxdt = [sympify(state.process_eqn) for state in problem.states()]

        # Zeroth order constraints have no 'xi' state
        xi_vars = []
        h = []
        while True:
            control_found = False

            for u in problem.controls():
                if u.sym in cq[-1].subs(quantity_subs).atoms():
                    logging.info('Constraint is of order '+str(order))
                    control_found = True
                    break
            if control_found:
                break

            dcdx = [self.derivative(cq[-1], state.sym, self.quantity_vars) for state in problem.states()]

            # Chain rule (Assume there is no explciit time-dependence) to find dcdt
            cq.append(sum(d1*d2 for d1,d2 in zip(dcdx, dxdt)))
            order = order + 1

            # Create the auxiliary state variables
            xi_vars.append(Symbol('xi'+str(ind+1)+str(order)))

        # Create the smoothing control variable
        xi_vars.append(Symbol('ue'+str(ind+1)))

        # TODO: Fix constraint object to accept two limits
        c_limit = sympify(c.limit)
        if c_limit.is_Number:
            # TODO: Allow continuation on constraints
            # Define new hidden constant
            c_limit = sympify('_'+c.label)
            print(c.limit)
            problem.constant(str(c_limit),float(c.limit),c.unit)
            logging.debug('Added constant '+str(c_limit))

        if c.direction == '>':
            c.lbound = c_limit
            c.ubound = -c_limit
        elif c.direction == '<':
            c.ubound = c_limit
            c.lbound = -c_limit
        else:
            raise ValueError('Invalid direction specified for constraint')

        psi = self.get_satfn(xi_vars[0], ubound=c.ubound, lbound=c.lbound, slopeAtZero=50)
        psi_vars = [(Symbol('psi'+str(ind+1)), psi)]

        # Add to quantity list
        self.quantity_vars[Symbol('psi'+str(ind+1))] = psi
        self.quantity_list.append({'name':('psi'+str(ind+1)), 'expr':str(psi)})

        # m-th order constraint needs up to m-th derivative of psi to be defined
        psi_i = psi
        for i in range(order):
            psi_i = diff(psi_i, xi_vars[0])
            # psi_vars.append((Symbol('psi'+str(ind+1)+str(i+1)+'('+str(xi_vars[0])+')'), psi_i))
            psi_vars.append((Symbol('psi'+str(ind+1)+str(i+1)), psi_i))
            self.quantity_vars[Symbol('psi'+str(ind+1)+str(i+1))] =  psi_i
            self.quantity_list.append({'name':('psi'+str(ind+1)+str(i+1)), 'expr':str(psi_i)})

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
            problem.state(str(xi_vars[i]), str(xi_vars[i+1]),'('+c.unit+')/s^('+str(i)+')')
            # Constraint all cq at initial point (forms constraints for xi_ij)
            problem.constraints().initial(str(cq[i] - h[i]),'('+c.unit+')/s^('+str(i)+')')
            # Add to initial guess vector
            problem.guess.start.append(c_vals[i])

            dhdxi = [diff(h[i], xi_v) for xi_v in xi_vars[:-1]]
            dhdt  = sum(d1*d2 for d1,d2 in zip(dhdxi,xi_vars[1:])) # xi11dot = xi12 etc.
            dhdt = dhdt.subs(psi_var_sub)
            h.append(dhdt)

        # Add the smoothing control with the right unit
        ue_unit = sympify('('+c.unit+')/(s^('+str(order)+'))')
        problem.control(str(xi_vars[-1]), str(ue_unit))
        logging.debug('Adding control '+str(xi_vars[-1])+' with unit '+str(ue_unit))

        # Add equality constraint
        cqi_unit = ue_unit*time_unit
        problem.constraints().equality(str(cq[-1] - h[-1]),str(cqi_unit))

        # Add smoothing factor
        eps_const = Symbol('eps_'+c.label)
        eps_unit = (path_cost_unit/ue_unit**2)/time_unit #Unit of integrand
        problem.constant(str(eps_const), 1e-2, str(eps_unit))
        logging.debug('Adding smoothing factor '+str(eps_const)+' with unit '+str(eps_unit))

        # Append new control to path cost
        path_cost_expr = path_cost_expr + eps_const*xi_vars[-1]**2

    logging.debug('Updated path cost is: '+str(path_cost_expr))
    problem.cost['path'].expr = str(path_cost_expr)

    u_constraints = problem.constraints().get('control')

    for (ind,c) in enumerate(u_constraints):
        w_i = sympify('uw'+str(ind+1))
        psi = self.get_satfn(w_i, ubound=sympify(c.ubound), lbound = sympify(c.lbound))

        # Add the smoothing control
        problem.control(str(w_i), c.unit)

        # Add equality constraint
        csym = sympify(c.expr)
        problem.constraints().equality(str(csym - psi),c.unit)

        uw_unit = symipfy2(c.unit)
        eps_const = Symbol('eps_'+str(ind+1))
        eps_unit = (path_cost_unit/uw_unit**2)/time_unit #Unit of integrand
        problem.constant(str(eps_const), 1, str(eps_unit))

# Implement workflow using simplepipe and functions defined above
ICRM = sp.Workflow([
    sp.Task(process_quantities,
            inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn')),

    sp.Task(process_path_constraints, inputs='*', outputs=('oo')),
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
    sp.Task(make_hamiltonian_and_costates,
            inputs=('states', 'path_cost', 'derivative_fn'),
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
    sp.Task(make_control_law,
            inputs=('dhdu','controls'),
            outputs=('control_law')),

    sp.Task(generate_problem_data,
            inputs='*',
            outputs=('problem_data')),
], description='Traditional optimal control workflow')


# Call doctest if the script is run directly
if __name__ == "__main__":
    import doctest
    doctest.testmod()
