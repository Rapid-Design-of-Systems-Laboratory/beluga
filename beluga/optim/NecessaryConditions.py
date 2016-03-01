from sympy import *
from sympy.core.function import AppliedUndef, Function
# from sympy.parsing.sympy_parser import parse_expr
import pystache, imp, inspect, logging, os
import re as _re

import beluga.bvpsol.BVP as BVP

from beluga.utils import sympify2, keyboard
from beluga.optim.problem import *
import dill

class NecessaryConditions(object):
    """Defines necessary conditions of optimality."""

    # pystache renderer without HTML escapes
    renderer = pystache.Renderer(escape=lambda u: u)

    def __init__(self, cached=True):
        """!
        \brief     Initializes all of the relevant necessary conditions of opimality.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        self.aug_cost = {}
        self.costates = []
        self.costate_rates = []
        self.ham = sympify2('0')
        self.ham_ctrl_partial = []
        self.ctrl_free = []
        self.parameter_list = []
        self.bc_initial = []
        self.bc_terminal = []
        from .. import Beluga # helps prevent cyclic imports
        self.compile_list = ['deriv_func','bc_func','compute_control']
        self.template_prefix = Beluga.config.getroot()+'/beluga/bvpsol/templates/'
        self.template_suffix = '.py.mu'

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
        #     rate = diff(sympify2('-1*(' + self.ham + ')'),state)
        #     # numerical_diff = rate.atoms(Derivative)
        #     self.costate_rates.append(str(rate))
        self.costate_rates = [self.derivative(-1*(self.ham),state, self.quantity_vars) for state in states]
        # self.costate_rates.append(str(diff(sympify2(
        # '-1*(' + self.ham + ')'),state)))

    def make_ctrl_partial(self, controls):
        """!
        \brief     Symbolically compute dH/du where H is the Hamiltonian and u is the control.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        # TODO: Automate partial derivatives of numerical functions
        self.ham_ctrl_partial = []
        for ctrl in controls:
            dHdu = self.derivative(sympify2(self.ham),ctrl, self.quantity_vars)
            keyboard()
            custom_diff = dHdu.atoms(Derivative)

            repl = {(d,im(f.func(v+1j*1e-30))/1e-30) for d in custom_diff
                        for f,v in zip(d.atoms(AppliedUndef),d.atoms(Symbol))}

            self.ham_ctrl_partial.append(dHdu.subs(repl))#.subs(self.quantity_subs))
        # self.ham_ctrl_partial = [diff(sympify2(self.ham),ctrl) for ctrl in controls]
        # self.ham_ctrl_partial.append(str(diff(sympify2(self.ham),
        #     symbols(ctrl))))

    def make_ctrl(self, controls):
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
            self.mu_vars = [sympify2('mu'+str(i+1)) for i in range(len(self.equality_constraints))]
            # self.mu_lhs = [sympify2(c.expr).subs(self.quantity_subs) for c in self.equality_constraints]
            self.mu_lhs = [sympify2(c.expr) for c in self.equality_constraints]
        try:
            # var_list = list(vars + self.mu_vars)
            # eqn_list = list(self.mu_lhs + lhs)

            # for (i,ctrl_v) in enumerate(var_list):
            #     logging.debug('Solving for '+str(ctrl_v)+' ...')
            #     keyboard()
            #     sol = solve(eqn_list[i], ctrl_v, dict=True)
            #
            #     # Substitute solution in other equations
            #     for (j,eqn) in enumerate(eqn_list):
            #         if j>i:
            #             eqn_list[j] = eqn.subs(ctrl_v,sol[0][ctrl_v])
            #     var_sol.append(sol)
            # keyboard()

            logging.info("Attempting using SymPy ...")
            logging.debug("dHdu = "+str(lhs+self.mu_lhs))
            # keyboard()
            var_sol = solve(lhs+self.mu_lhs,vars+self.mu_vars,dict=True)
            logging.debug(var_sol)
            ctrl_sol = var_sol
            # var_sol = []
            # raise ValueError() # Force mathematica
        except ValueError as e:  # FIXME: Use right exception name here
            logging.debug(e)
            logging.info("No control law found")
            from beluga.utils.pythematica import mathematica_solve
            logging.info("Attempting using Mathematica ...")
            # var_sol = mathematica_solve(lhs+self.mu_lhs,vars+self.mu_vars)
            # TODO: Extend numerical control laws to mu's
            ctrl_sol = var_sol
            if ctrl_sol == []:
                logging.info("No analytic control law found, switching to numerical method")

        logging.info("Done")
        # solve() returns answer in the form
        # [ {ctrl1: expr11, ctrl2:expr22},
        #   {ctrl1: expr21, ctrl2:expr22}]
        # Convert this to format required by template
        self.control_options = [ [{'name':str(ctrl), 'expr':str(expr)}
                                    for (ctrl,expr) in option.items()]
                                for option in ctrl_sol]

    def make_aug_cost(self, aug_cost, constraint, location):
        """!
        \brief     Symbolically create the augmented cost functional.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

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
            sign = sympify2('-1')
        elif location is 'terminal':
            sign = sympify2('1')

        cost_expr = sign * (self.aug_cost[location])

        #TODO: Fix hardcoded if conditions
        #TODO: Change to symbolic
        if location == 'initial':
            # Using list comprehension instead of loops
            # lagrange_ changed to l. Removed hardcoded prefix
            self.bc_initial += [str(sympify2(state.make_costate()) - self.derivative(sympify2(cost_expr),state.sym, self.quantity_vars))
                                    for state in states]
        else:
            # Using list comprehension instead of loops
            self.bc_terminal += [str(sympify2(state.make_costate()) - self.derivative(sympify2(cost_expr),state.sym,self.quantity_vars))
                                    for state in states]

        # for i in range(len(state)):
        #     self.bc_initial.append(
        #         diff(sympify2(sign + '(' + self.aug_cost[location] + ')'),
        #         state[i].sym))

    def make_ham(self, problem):
        """!
        \brief     Symbolically create the Hamiltonian.
        \author    Michael Grant
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """
        #TODO: Make symbolic
        self.ham = sympify2(problem.cost['path'].expr)
        for i in range(len(problem.states())):
            self.ham += sympify2(self.costates[i]) * (sympify2(problem.states()[i].process_eqn))

        # Adjoin equality constraints
        for i in range(len(self.equality_constraints)):
            self.ham += sympify2('mu'+str(i+1)) * (sympify2(self.equality_constraints[i].expr))

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
    def process_path_constraints(self, problem):
        return
        constraints = problem.constraints().get('path')
        for c in constraints:
            # Determine order of constraint

            # c0 = sympify2(c.expr)
            order = 0
            cq = sympify2(c.expr)
            while True:
                control_found = False

                for u in problem.controls():
                    if u in cq.atoms():
                        control_found = True
                        break

                order = order + 1

            pass

    def get_bvp(self,problem):
        """Perform variational calculus calculations on optimal control problem
           and returns an object describing the boundary value problem to be solved

        Returns: bvpsol.BVP object
        """


        # Should this be moved into __init__ ?
        # self.process_systems(problem)
        logging.info('Processing quantity expressions')
        # Process quantities
        # Substitute all quantities that show up in other quantities with their expressions
        # TODO: Sanitize quantity expressions
        # TODO: Check for circular references in quantity expressions
        if len(problem.quantity()) > 0:
            self.quantity_subs = [(sympify2(qty.var), sympify2(qty.value)) for qty in problem.quantity()]
            self.quantity_sym, self.quantity_expr = zip(*self.quantity_subs)
            self.quantity_expr = [qty_expr.subs(self.quantity_subs) for qty_expr in self.quantity_expr]

            # Use substituted expressions to recreate quantity expressions
            self.quantity_subs = [(qty_var,qty_expr) for qty_var, qty_expr in zip(self.quantity_sym, self.quantity_expr)]
            # Dictionary for use with mustache templating library
            self.quantity_list = [{'name':str(qty_var), 'expr':str(qty_expr)} for qty_var, qty_expr in zip(self.quantity_sym, self.quantity_expr)]
            self.quantity_vars = dict(self.quantity_subs)
        else:
            self.quantity_list = self.quantity_sym = self.quantity_expr = self.quantity_subs = []
            self.quantity_vars = {}


        ## Create costate list
        self.costates = [state.make_costate() for state in problem.states()]

        # for i in range(len(self.problem.states())):
        #     self.costates.append(self.problem.states()[i].make_costate())

        # Build augmented cost strings
        aug_cost_init = sympify2(problem.cost['initial'].expr)
        self.make_aug_cost(aug_cost_init, problem.constraints(), 'initial')

        aug_cost_term = sympify2(problem.cost['terminal'].expr)
        self.make_aug_cost(aug_cost_term, problem.constraints(), 'terminal')

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
        func_list = sympify2(self.ham).atoms(AppliedUndef)

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
        self.make_costate_rate(problem.states())
        self.make_ctrl_partial(problem.controls())

        # Regularize path constraints using saturation functions
        self.process_path_constraints(problem)
        # # Add support for state and control constraints
        # problem.state('xi11','xi12','m')
        # problem.state('xi12','ue1','m')
        # self.costates += ['eta11','eta12']   # Costates for xi
        #
        # # Add new states to hamiltonian
        # h1_3 = '(psi12*xi12^2 + psi11*ue1)';  # xi12dot = ue1
        # c1_2 = 'u'
        # self.ham += sympify2('eta11*xi12 + eta12*ue1')  #
        # self.ham += sympify2('mu1 * ('+c1_2+' - '+h1_3')')
        #
        # # TODO: Compute these automatically
        # self.costate_rates += ['mu1*(xi12**2*psi1_3 + psi12*ue1)',
        #                        'mu1*(2*psi12*xi12)  - eta1']
        #
        # Compute unconstrained control law
        # (need to add singular arc and bang/bang smoothing, numerical solutions)
        self.make_ctrl(problem.controls())

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
             ['(tf)*(' + str(sympify2(state.process_eqn)) + ')' for state in problem.states()] +
             ['(tf)*(' + str(costate_rate) + ')' for costate_rate in self.costate_rates] +
             ['tf*0']   # TODO: Hardcoded 'tf'
         ,
         'num_states': 2*len(problem.states()) + 1,
         'dHdu': [str(dHdu) for dHdu in self.ham_ctrl_partial] + self.mu_lhs,
         'left_bc_list': self.bc_initial,
         'right_bc_list': self.bc_terminal,
         'control_options': self.control_options,
         'control_list': [str(u) for u in problem.controls()] + [str(mu) for mu in self.mu_vars],
         'num_controls': len(problem.controls()) + len(self.mu_vars),  # Count mu multipliers
         'ham_expr':self.ham,
         'quantity_list': self.quantity_list
        }

    #    problem.constraints[i].expr for i in range(len(problem.constraints))

        # Create problem functions by importing from templates
        self.compiled = imp.new_module('_probobj_'+problem.name)
        # self.compiled = imp.new_module("blaaaa")

        compile_result = [self.compile_function(self.template_prefix+func+self.template_suffix, verbose=True)
                                        for func in self.compile_list]


        self.bvp = BVP(self.compiled.deriv_func,self.compiled.bc_func)
        self.bvp.solution.aux['const'] = dict((const.var,const.val) for const in problem.constants())
        self.bvp.solution.aux['parameters'] = self.problem_data['parameter_list']
        self.bvp.solution.aux['function']  = problem.functions

        # TODO: Fix hardcoding of function handle name (may be needed for multivehicle/phases)?
        self.bvp.control_func = self.compiled.compute_control
        self.bvp.problem_data = self.problem_data
        # TODO: ^^ Do same for constraint values
        return self.bvp
