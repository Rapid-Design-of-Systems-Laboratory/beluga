# from beluga.optim import *
from optimalcontrol.elements import Problem
from sympy import *
from sympy.core.function import AppliedUndef, Function
import pystache, imp, inspect, logging, os
import re as _re

import beluga.bvpsol.BVP as BVP

from beluga.utils import sympify, keyboard, ipsh
from beluga.optim.problem import *
import dill
import numpy as np
from collections import Iterable

class OCDAENumerical(object):
    name = 'dae-numerical'

    def get_actions(self):
        # Tuple: (func, arg1, arg2, ...)
        self.actions = [
            (self.process_quantities),
            (self.make_costates),
            (self.make_aug_cost, 'initial'),
            (self.make_aug_cost, 'terminal'),
            # (self.process_path_constraints, problem),
        ]
        return self.actions

    def run(self):
        for action in self.actions:
            if isinstance(action, Iterable):
                action[0](*action[1:])
            else:
                action()

        # pystache renderer without HTML escapes
        renderer = pystache.Renderer(escape=lambda u: u)

    def __init__(self, problem, cached=True):
        """!
        \brief     Initializes all of the relevant necessary conditions of opimality.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.2
        \date      05/15/16
        """

        self.problem = problem
        self.get_actions()

        self.aug_cost = {}
        self.costates = []
        self.costate_rates = []
        self.ham = sympify('0')
        self.ham_ctrl_partial = []
        self.ctrl_free = []
        self.parameter_list = []
        self.bc_initial = []
        self.bc_terminal = []
        # from .. import Beluga # helps prevent cyclic imports
        self.compile_list = ['deriv_func','bc_func','compute_control']
        # self.template_prefix = Beluga.config.getroot()+'/beluga/bvpsol/templates/'
        self.template_suffix = '.py.mu'
        self.dae_states = []
        self.dae_equations = []

    def cache_bvp(self, problem, filename=None):
        """
        \brief Saves BVP object into file on disk
        Arguments:
            problem : Problem object
            filename: Full path to cache file (optional)
                      default value: <self.problem.name>_bvp.dat
        \date  01/27/2016
        """
        if filename is None:
            filename = problem.name+'_bvp.dat'

        with open(filename,'wb') as f:
            try:
                logging.info('Caching BVP information to file')
                bvp = dill.dump(self.bvp,f)
                return True
            except:
                logging.warn('Failed to save BVP to '+filename)
                return False

    def load_bvp(self, problem, filename=None):
        """
        \brief  Loads pre-computed BVP object from cache file
        \author Thomas Antony
        Arguments:
            problem : Problem object
            filename: Full path to cache file (optional)
                      default value: <self.problem.name>_bvp.dat
        \date  01/27/2016
        """
        if filename is None:
            filename = problem.name+'_bvp.dat'

        if not os.path.exists(filename):
            return None

        with open(filename,'rb') as f:
            try:
                logging.info('Loading BVP information from cache')
                bvp = dill.load(f)
                return bvp
            except Exception as e:
                logging.warn('Failed to load BVP from '+filename)
                logging.debug(e)
                return None

    def derivative(self, expr, var, dependent_variables):
        """
        Take derivative taking pre-defined quantities into consideration

        dependent_variables: Dictionary containing dependent variables as keys and
                             their expressions as values
        """
        dep_var_names = dependent_variables.keys()
        dep_var_expr = [(expr) for (_,expr) in dependent_variables.items()]

        dFdq = [diff(expr, dep_var).subs(dependent_variables.items()) for dep_var in dep_var_names]
        dqdx = [diff(qexpr, var) for qexpr in dep_var_expr]

        # Chain rule + total derivative
        out = sum(d1*d2 for d1,d2 in zip(dFdq, dqdx)) + diff(expr, var)
        return out

    def make_costate_rate(self, states):
        """!
        \brief     Creates the symbolic differential equations for the costates.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        # TODO: Automate partial derivatives of numerical functions
        # for state in states:
        #     rate = diff(sympify('-1*(' + self.ham + ')'),state)
        #     # numerical_diff = rate.atoms(Derivative)
        #     self.costate_rates.append(str(rate))
        self.costate_rates = [self.derivative(-1*(self.ham),state, self.quantity_vars) for state in states]
        # self.costate_rates.append(str(diff(sympify(
        # '-1*(' + self.ham + ')'),state)))

        for state in states:
            corate=self.derivative(-1*(self.ham),state,self.quantity_vars)
            custom_diff=corate.atoms(Derivative)
            repl = [] #Replacements for custom functions
            for d in custom_diff:
                for f in d.atoms(AppliedUndef): #Just extracts (never more than 1 f)
                    for v in f.atoms(Symbol):
                        if str(v)==str(state): #This should only happen once!
                            replv=sympify('im('+str(f.subs(v,v+_h))+')/1e-30')
                            repl.append((d,replv))
            self.costate_rates.append(corate.subs(repl))
        self.costate_rates=sympify2(self.costate_rates)

        #h = 1e-30
        #j = symbols('1j')

        #self.costate_rates = []

        #for state in states:
        #    state = sympify(state)
        #    H = self.make_state_dep_ham(state, self.problem)
        #    if H != 0:
        #        self.costate_rates.append('im(' + str((H.subs(state, (state + h * j)))) + ')/' + str(h))
        #    else:
        #        self.costate_rates.append('0')
        #self.costate_rates=sympify2(self.costate_rates)
        #print(Matrix([sympify2(state.process_eqn) for state in self.problem.states()]+ self.costate_rates))
        #quit()

    def make_costate_rate_numeric(self, states):
        """!
        \brief     Creates the symbolic differential equations for the costates.
        \author    Michael Grant
        \author    Sean Nolan
        \version   0.1
        \date      06/22/16
        """

        h = 1e-100
        j = symbols('1j')

        self.costate_rates = []

        for state in states:
            state = sympify(state)
            H = self.make_state_dep_ham(state, self.problem)
            if H != 0:
                self.costate_rates.append('-np.imag(' + str((H.subs(state, (state + h * j)))) + ')/' + str(h))
            else:
                self.costate_rates.append('0')


    def make_ctrl_partial(self, controls):
        """!
        \brief     Symbolically compute dH/du where H is the Hamiltonian and u is the control.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        self.ham_ctrl_partial = []
        _h = sympify2('1j*(1e-30)')

        for ctrl in controls:
            dHdu = self.derivative(sympify(self.ham), ctrl, self.quantity_vars)
            custom_diff = dHdu.atoms(Derivative)
            for d in custom_diff:
                for f in d.atoms(AppliedUndef):
                    for v in f.atoms(Symbol):
                        if str(v)==str(ctrl):
                            replv=sympify('im('+str(f.subs(v,v+_h))+')/1e-30')
                            repl.append((d,replv))

            self.ham_ctrl_partial.append(dHdu.subs(repl))
            # Substitute "Derivative" with complex step derivative
            #repl = {(d,im(f.func(v+1j*1e-30))/1e-30) for d in custom_diff
            #            for f,v in zip(d.atoms(AppliedUndef),d.atoms(Symbol))}

            #self.ham_ctrl_partial.append(dHdu.subs(repl))

    def selective_expand(self, expr, var_select, subs_list):
        # Expands the expressions specified by subs_list if they contain the
        # variables in var_select
        select_subs = [qty for qty in subs_list.items() for var in var_select if var.sym in qty[1].atoms()]
        # Substitute only relevant symbols in the expression
        return expr.subs(select_subs)

    def make_ctrl(self, problem, mode='dae'):
        if mode == 'dae':
            self.make_ctrl_dae(problem)
        else:
            self.make_ctrl_analytic(problem.controls())

    def make_ctrl_dae(self, problem):
        """!
        \brief     Compute EOMs for controls.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      04/10/16
        """
        if len(self.equality_constraints) > 0:
            self.mu_vars = [sympify('mu'+str(i+1)) for i in range(len(self.equality_constraints))]
            self.mu_lhs = [sympify(c.expr) for c in self.equality_constraints]
        else:
            self.mu_vars = self.mu_lhs = []

        g = self.ham_ctrl_partial + self.mu_lhs
        X = [state.sym for state in problem.states()] + [Symbol(costate) for costate in self.costates]
        U = [c.sym for c in problem.controls()] + self.mu_vars

        xdot = Matrix([sympify(state.process_eqn) for state in problem.states()] + self.costate_rates)
        # Compute Jacobian
        dgdX = Matrix([[self.derivative(g_i, x_i, self.quantity_vars) for x_i in X] for g_i in g])
        dgdU = Matrix([[self.derivative(g_i, u_i, self.quantity_vars) for u_i in U] for g_i in g])

        udot = dgdU.LUsolve(-dgdX*xdot); # dgdU * udot + dgdX * xdot = 0

        self.dae_states = U

        self.dae_equations = list(udot)
        self.dae_bc = g


    def make_ctrl_analytic(self, controls):
        """!
        \brief     Symbolically compute the solutions for the control along control-unconstrained arcs.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """
        # Solve all controls simultaneously
        logging.info("Finding optimal control law ...")

        # If equality constraints are present
        # We need to solve for 'mu's as well
        lhs = self.ham_ctrl_partial
        vars = [c.sym for c in controls]
        self.mu_vars = []
        self.mu_lhs = []

        if len(self.equality_constraints) > 0:
            self.mu_vars = [sympify('mu'+str(i+1)) for i in range(len(self.equality_constraints))]

            self.mu_lhs = [sympify(c.expr) for c in self.equality_constraints]
        try:
            var_list = list(vars + self.mu_vars)
            # var_list = vars
            eqn_list = []
            for eqn in list(lhs + self.mu_lhs ):
                eqn_list.append(self.selective_expand(eqn, controls, self.quantity_vars))
            logging.info("Attempting using SymPy ...")
            logging.debug("dHdu = "+str(eqn_list))

            ctrl_sol = solve(eqn_list, var_list, dict=True)
            #TODO: ^ uncomment once done with the aircraft noise problem
            #ctrl_sol = CtrlSols() #I'm going to hell for this
            #logging.info("Grabbed the control laws for the aircraft noise!")

            # raise ValueError() # Force mathematica
        except ValueError as e:  # FIXME: Use right exception name here
            logging.debug(e)
            logging.info("No control law found")
            from beluga.utils.pythematica import mathematica_solve
            logging.info("Attempting using Mathematica ...")
            #var_sol = mathematica_solve(lhs+self.mu_lhs,vars+self.mu_vars)
            # TODO: Extend numerical control laws to mu's
            ctrl_sol = var_sol
            if ctrl_sol == []:
                logging.info("No analytic control law found, switching to numerical method")

        #logging.info("Done")
        # solve() returns answer in the form
        # [ {ctrl1: expr11, ctrl2:expr22},
        #   {ctrl1: expr21, ctrl2:expr22}]
        # Convert this to format required by template
        self.control_options = [ [{'name':str(ctrl), 'expr':str(expr)}
                                    for (ctrl,expr) in option.items()]
                                for option in ctrl_sol]

    def make_aug_cost(self, location):
        """!
        \brief     Symbolically create the augmented cost functional.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """
        aug_cost   = self.problem.cost[location].expr
        constraint = self.problem.constraints(location)
        # Do in two steps so that indices are "right"
        # TODO: apply quantities
        filtered_list = [c for c in constraint if c.type==location]
        self.parameter_list += [c.make_multiplier(ind) for (ind,c) in enumerate(filtered_list,1)]
        # self.aug_cost[location] = aug_cost + ''.join(' + (%s)' % c.make_aug_cost(ind)
        #                         for (ind,c) in enumerate(filtered_list,1))

        self.aug_cost[location] = aug_cost + sum([c.make_aug_cost(ind)
                                                 for (ind,c) in enumerate(filtered_list,1)])

    def make_costate_bc(self, states, location):
        """!
        \brief     Symbolically create the boundary conditions at initial and final locations.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        if location is 'initial':
            sign = sympify('-1')
        elif location is 'terminal':
            sign = sympify('1')

        cost_expr = sign * (self.aug_cost[location])

        #TODO: Fix hardcoded if conditions
        #TODO: Change to symbolic
        if location == 'initial':
            # Using list comprehension instead of loops
            # lagrange_ changed to l. Removed hardcoded prefix
            self.bc_initial += [str(sympify(state.make_costate()) - self.derivative(sympify(cost_expr),state.sym, self.quantity_vars))
                                    for state in states]
        else:
            # Using list comprehension instead of loops
            self.bc_terminal += [str(sympify(state.make_costate()) - self.derivative(sympify(cost_expr),state.sym,self.quantity_vars))
                                    for state in states]

    def make_ham(self, problem):
        """!
        \brief     Symbolically create the Hamiltonian.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """
        #TODO: Make symbolic
        self.ham = sympify(problem.cost['path'].expr)
        for i in range(len(problem.states())):
            self.ham += sympify(self.costates[i]) * (sympify(problem.states()[i].process_eqn))

        # Adjoin equality constraints
        for i in range(len(self.equality_constraints)):
            self.ham += sympify('mu'+str(i+1)) * (sympify(self.equality_constraints[i].expr))

    def make_state_dep_ham(self, state, problem):
        """!
        \brief     Symbolically create the Hamiltonian.
        \author    Michael Grant
        \author    Sean Nolan
        \version   0.1
        \date      06/22/16
        """

        H = sympify(0)

        new_terms = sympify2(problem.cost['path'].expr)
        atoms = new_terms.atoms()
        if state in atoms:
            H += new_terms


        for i in range(len(problem.states())):
            new_terms = sympify2(self.costates[i]) * (sympify2(problem.states()[i].process_eqn))
            atoms = new_terms.atoms()
            if state in atoms:
                H += new_terms

        # Adjoin equality constraints
        for i in range(len(self.equality_constraints)):
            new_terms = sympify2('mu' + str(i + 1)) * (sympify2(self.equality_constraints[i].expr))
            atoms = new_terms.atoms()
            if state in atoms:
                H += new_terms

        raw_terms = H.as_terms()
        H_parts = [raw_terms[0][k][0] for k in range(len(raw_terms[0]))]
        new_H = sympify(0)
        for part in H_parts:
            store = sympify(0)
            tries = 0
            while (part != store) & (tries <= 5):
                store = part
                part = part.expand()
                tries += 1
            raw_terms = part.as_terms()
            sub_parts = [raw_terms[0][k][0] for k in range(len(raw_terms[0]))]
            new_part = sympify(0)
            for sub_part in sub_parts:
                atoms = sub_part.atoms()
                if state in atoms:
                    # sub_part = sub_part.factor()
                    new_part += sub_part
            new_part = new_part.factor()
            if len(str(new_part)) < 50:
                 new_part = new_part.simplify(ratio=1.0)
            new_H += new_part

        # print('New:' + str(len(str(new_H))))
        # print('Old:' + str(len(str(H))))

        return new_H

    # Compiles a function template file into a function object
    # using the given data
    def compile_function(self,filename,verbose=False):
        """
        Compiles a function specified by template in filename and stores it in
        self.compiled

        Returns:
            bool: True if successful

        Raises:
            ValueError: If 'problem_data' or 'compiled' is not defined
        """
        with open(filename) as f:
            tmpl = f.read()

            if self.problem_data is None:
                raise ValueError('Problem data not defined. Unable to compile function.')

            if self.compiled is None:
                raise ValueError('Problem module not defined. Unable to compile function.')

            # Render the template using the data
            code = self.renderer.render(tmpl,self.problem_data)
            # if verbose and 'compute_control' in filename:
            # if verbose:
            logging.debug(code)

            # For security
            self.compiled.__dict__.update({'__builtin__':{}})
            return exec(code,self.compiled.__dict__)

    # TODO: Maybe change all constraint limits (initial, terminal etc.) to be 'constants' that can be changed by continuation?
    def sanitize_constraint(self,constraint,problem):
        """
        Checks the initial/terminal constraint expression for invalid symbols
        Also updates the constraint expression to reflect what would be in code
        """
        if constraint.type == 'initial':
            pattern = r'([\w\d\_]+)_0'
            prefix = '_x0'
        elif constraint.type == 'terminal':
            pattern = r'([\w\d\_]+)_f'
            prefix = '_xf'
        else:
            raise ValueError('Invalid constraint type')

        m = _re.findall(pattern,constraint.expr)
        invalid = [x for x in m if x not in problem.states()]

        if not all(x is None for x in invalid):
            raise ValueError('Invalid expression(s) in boundary constraint:\n'+str([x for x in invalid if x is not None]))

        # Create new variable for output to avoid mutating original object
        output = Constraint()
        output.type = constraint.type
        output.unit = constraint.unit
        output.expr = _re.sub(pattern,prefix+r"['\1']",constraint.expr)

        return output

    # def process_systems(self,problem):
    #     """Traverses dynamic systems list and extracts information"""
    #     for (system_type,system_list) in problem.systems.items():
    #         for idx,system_inst in enumerate(system_list):
    #             # new_states = [state.add_prefix(system_type+'_'+str(idx)+'_')
    #             #                 for state in system_inst.states]
    #             new_states = [state
    #                             for state in system_inst.states]
    #     # print(new_states)

    # 1/4 s (c1-c2) = slope at x=0
    # when slope = 1, s = 4/(c1-c2)
    # wyen slope = 10, s = 40/(c1-c2)
    def get_satfn(self, var, ubound=None, lbound=None, slopeAtZero=1):
        # var -> varible inside saturation function
        if ubound is None and lbound is None:
            raise ValueError('At least one bound should be specified for the constraint.')
        if ubound == lbound:
            raise ValueError('The upper and lower bounds should be different.')

        # Symmetric bounds
        if ubound is None:
            # Return lower bound sat fn
            #ubound = -lbound
            return lbound + exp(var)
        elif lbound is None:
            # Return upper bound sat fn
            #lbound = -ubound
            return ubound - exp(-var)
        else:
            print(ubound)
            s = 4*slopeAtZero/(ubound - lbound)
            return ubound - ( ubound - lbound )/( 1 + exp(s*var) )

    def process_path_constraints(self, problem):
        constraints = problem.constraints().get('path')
        quantity_subs = self.quantity_vars.items()

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

            psi = self.get_satfn(xi_vars[0], ubound=c.ubound, lbound=c.lbound, slopeAtZero=1)
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
            problem.constant(str(eps_const), 1e-6, str(eps_unit))
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

            # problem.state('costC2','eps2*('+str(w_i)+'^2)','m^2/s^2')
    def process_quantities(self,):
        # Should this be moved into __init__ ?
        # self.process_systems(problem)
        logging.info('Processing quantity expressions')
        # Process quantities
        # Substitute all quantities that show up in other quantities with their expressions
        # TODO: Sanitize quantity expressions
        # TODO: Check for circular references in quantity expressions
        if len(self.problem.quantity()) > 0:
            quantity_subs = [(qty.var, qty.expr) for qty in self.problem.quantity()]
            quantity_sym, quantity_expr = zip(*quantity_subs)
            quantity_expr = [qty_expr.subs(quantity_subs) for qty_expr in quantity_expr]

            # Use substituted expressions to recreate quantity expressions
            quantity_subs = [(qty_var,qty_expr) for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]
            # Dictionary for use with mustache templating library
            self.quantity_list = [{'name':str(qty_var), 'expr':str(qty_expr)} for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]

            # Dictionary for substitution
            self.quantity_vars = dict(quantity_subs)
        else:
            self.quantity_list = quantity_subs = []
            self.quantity_vars = {}

    def make_costates(self):
        self.costates = [state.make_costate() for state in self.problem.states()]

    def get_bvp(self,problem,mode='dae'):
        """Perform variational calculus calculations on optimal control problem
           and returns an object describing the boundary value problem to be solved

        Returns: bvpsol.BVP object
        """
        # Process intermediate variables
        self.process_quantities(problem)

        # Regularize path constraints using saturation functions
        self.process_path_constraints(problem)

        # self.state_subs = [(state.sym, sympify(state.process_eqn)) for state in problem.states()]
        ## Create costate list
        # self.costates = [state.make_costate() for state in problem.states()]
        self.make_costates(problem)

        # for i in range(len(self.problem.states())):
        #     self.costates.append(self.problem.states()[i].make_costate())

        # Build augmented cost strings
        # aug_cost_init = sympify(problem.cost['initial'].expr)
        self.make_aug_cost('initial')
        # self.make_aug_cost(aug_cost_init, problem.constraints(), 'initial')

        # aug_cost_term = sympify(problem.cost['terminal'].expr)
        self.make_aug_cost('terminal')
        # self.make_aug_cost(aug_cost_term, problem.constraints(), 'terminal')

        # Add state boundary conditions
        self.bc_initial = [self.sanitize_constraint(x,problem).expr
                            for x in problem.constraints().get('initial')]
        self.bc_terminal = [self.sanitize_constraint(x,problem).expr
                    for x in problem.constraints().get('terminal')]

        self.equality_constraints = problem.constraints().get('equality')

        ## Unconstrained arc calculations
        # Construct Hamiltonian
        self.make_ham(problem)
        logging.debug('Hamiltonian : '+str(self.ham))
        # Get list of all custom functions in the problem
        # TODO: Check in places other than the Hamiltonian?
        # TODO: Move to separate method?
        func_list = sympify(self.ham).atoms(AppliedUndef)

        # TODO: Change this to not be necessary
        self.problem = problem

        # Load required functions from the input file
        new_functions = {(str(f.func),getattr(problem.input_module,str(f.func)))
                            for f in func_list
                            if hasattr(problem.input_module,str(f.func)) and
                                inspect.isfunction(getattr(problem.input_module,str(f.func)))}

        problem.functions.update(new_functions)

        undefined_func = [f.func for f in func_list if str(f.func) not in problem.functions]

        if not all(x is None for x in undefined_func):
            raise ValueError('Invalid function(s) specified: '+str(undefined_func))

        # Compute costate conditions
        self.make_costate_bc(problem.states(),'initial')
        self.make_costate_bc(problem.states(),'terminal')

        # TODO: Make this more generalized free final time condition
        # HARDCODED tf variable
        time_constraints = problem.constraints().get('independent')
        if len(time_constraints) > 0:
            self.bc_terminal.append('tf - 1')
        else:
            # Add free final time boundary condition
            self.bc_terminal.append('_H - 0')

        # Compute costate process equations
        if mode == 'numerical':
            self.make_costate_rate_numeric(problem.states())
        else:
            self.make_costate_rate(problem.states())
        self.make_ctrl_partial(problem.controls())

        # # Add support for state and control constraints
        # problem.state('xi11','xi12','m')
        # problem.state('xi12','ue1','m')
        # self.costates += ['eta11','eta12']   # Costates for xi
        #
        # # Add new states to hamiltonian
        # h1_3 = '(psi12*xi12^2 + psi11*ue1)';  # xi12dot = ue1
        # c1_2 = 'u'
        # self.ham += sympify('eta11*xi12 + eta12*ue1')  #
        # self.ham += sympify('mu1 * ('+c1_2+' - '+h1_3')')
        #
        # # TODO: Compute these automatically
        # self.costate_rates += ['mu1*(xi12**2*psi1_3 + psi12*ue1)',
        #                        'mu1*(2*psi12*xi12)  - eta1']
        #
        # Compute unconstrained control law
        # (need to add singular arc and bang/bang smoothing, numerical solutions)
        self.make_ctrl(problem, mode)

        # Create problem dictionary
        # NEED TO ADD BOUNDARY CONDITIONS

        # bc1 = [self.sanitize_constraint(x) for x in initial_bc]

        self.problem_data = {
        'aux_list': [
                {
                'type' : 'const',
                'vars': [const.var for const in problem.constants()]
                },
                {
                'type' : 'constraint',
                'vars': []
                },
                {
                'type' : 'function',
                'vars' : [func_name for func_name in problem.functions]
                }
         ],
         # TODO: Generalize 'tf' to independent variable for current arc
         'state_list':
             [str(state) for state in problem.states()] +
             [str(costate) for costate in self.costates] +
             ['tf']
         ,
         'parameter_list': [str(param) for param in self.parameter_list],
         'deriv_list':
             ['(tf)*(' + str(sympify(state.process_eqn)) + ')' for state in problem.states()] +
             ['(tf)*(' + str(costate_rate) + ')' for costate_rate in self.costate_rates] +
            #  ['(tf)*((' + str(costate_rate) + ').imag)' for costate_rate in self.costate_rates] +
             ['tf*0']   # TODO: Hardcoded 'tf'
         ,
         'state_rate_list':
            ['(tf)*(' + str(sympify2(state.process_eqn)) + ')' for state in problem.states()]
         ,
         'dae_var_list':
             [str(dae_state) for dae_state in self.dae_states],
         'dae_eom_list':
             ['(tf)*('+str(dae_eom)+')' for dae_eom in self.dae_equations],
         'dae_var_num': len(self.dae_states),
         'num_states': 2*len(problem.states()) + 1,
         'dHdu': [str(dHdu) for dHdu in self.ham_ctrl_partial] + self.mu_lhs,
         'left_bc_list': self.bc_initial + (self.dae_bc if (mode == 'dae') else []),
         'right_bc_list': self.bc_terminal,
         'control_options': [] if (mode == 'dae') else self.control_options,
         'control_list': [str(u) for u in problem.controls()] + [str(mu) for mu in self.mu_vars],
         'num_controls': len(problem.controls()) + len(self.mu_vars),  # Count mu multipliers
         'ham_expr':self.ham,
         # 'contr_dep_ham': [],
         'quantity_list': self.quantity_list,
        #  'dae_mode': mode == 'dae',
        }
    #    problem.constraints[i].expr for i in range(len(problem.constraints))

        # Create problem functions by importing from templates
        self.compiled = imp.new_module('_probobj_'+problem.name)

        if mode == 'dae':
            # self.template_suffix = '_dae' + self.template_suffix
            self.template_suffix = '_dae_num' + self.template_suffix
        if mode == 'num':
            self.template_suffix = '_num' + self.template_suffix

        compile_result = [self.compile_function(self.template_prefix+func+self.template_suffix, verbose=True)
                                        for func in self.compile_list]

        dhdu_fn = self.compiled.get_dhdu_func
        dae_num = len(problem.controls()) + len(self.mu_vars)

        self.bvp = BVP(self.compiled.deriv_func,self.compiled.bc_func,dae_func_gen=dhdu_fn,dae_num_states=dae_num)
        self.bvp.solution.aux['const'] = dict((const.var,const.val) for const in problem.constants())
        self.bvp.solution.aux['parameters'] = self.problem_data['parameter_list']
        self.bvp.solution.aux['function']  = problem.functions

        # TODO: Fix hardcoding of function handle name (may be needed for multivehicle/phases)?
        self.bvp.control_func = self.compiled.compute_control
        self.bvp.problem_data = self.problem_data
        # TODO: ^^ Do same for constraint values
        return self.bvp

if __name__ == '__main__':
    problem = Problem('brachisto')
    problem.quantity('foo','bar')
    im = OCDAENumerical(problem)
    im.run()
    print(im.quantity_list)
